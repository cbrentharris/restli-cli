from tests.restli_tests import BaseTest
from restli.generators import ResourceGenerator
from restli.command_line import create_parser
import os
import mock

class ResourceGeneratorTest(BaseTest):

    def setUp(self):
        super(ResourceGeneratorTest, self).setUp()
        os.chdir(self.random_dir)
        self.scaffolder.gen_project_structure()

    def test_it_creates_the_resource_file(self):
        generator_args = ['restli', '--generate', 'Fortune', '--namespace', self.package]
        with mock.patch('sys.argv', generator_args):
            generator = ResourceGenerator(create_parser().parse_args())
        generator.generate()
        self.assertTrue(os.path.exists(os.path.join(self.random_dir, self.resource_path(), 'fortune', 'impl', "FortunesResource.java")))

    @mock.patch('restli.generators.user_input', return_value='n')
    def test_it_doesnt_overwrite_a_resource_file(self, mock_user_input):
        generator_args = ['restli', '--generate', 'Foo', '--namespace', self.package, '--methods', 'get']
        generator = self.new_resource_generator(generator_args)
        generator.generate()
        # Remove the methods arg
        generator_args = ['restli', '--generate', 'Foo', '--namespace', self.package]
        generator = self.new_resource_generator(generator_args)
        generator.generate()
        with open(os.path.join(self.random_dir, self.resource_path(), 'foo', 'impl', 'FoosResource.java'), 'r') as resource_file:
            self.assertTrue('update' not in resource_file.read())

    @mock.patch('restli.generators.user_input', return_value='y')
    def test_it_overwrites_a_resource_file(self, mock_user_input):
        generator_args = ['restli', '--generate', 'Foo', '--namespace', self.package, '--methods', 'get']
        generator = self.new_resource_generator(generator_args)
        generator.generate()
        # Remove the methods arg
        generator_args = ['restli', '--generate', 'Foo', '--namespace', self.package]
        generator = self.new_resource_generator(generator_args)
        generator.generate()
        with open(os.path.join(self.random_dir, self.resource_path(), 'foo', 'impl', 'FoosResource.java'), 'r') as resource_file:
            self.assertTrue('update' in resource_file.read())

    def resource_path(self):
        return os.path.join(self.project_name, 'server', 'src', 'main', 'java', *self.package.split("."))

    def new_resource_generator(self, args):
        with mock.patch('sys.argv', args):
            return ResourceGenerator(create_parser().parse_args())
