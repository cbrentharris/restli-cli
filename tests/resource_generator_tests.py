from tests.restli_tests import BaseTest
from restli.generators import ResourceGenerator
from restli.command_line import create_parser
import os
import mock

class ResourceGeneratorTest(BaseTest):

    def test_it_creates_the_resource_file(self):
        os.chdir(self.random_dir)
        self.scaffolder.gen_project_structure()
        generator_args = ['restli', '--generate', 'Fortune', '--namespace', self.package]
        with mock.patch('sys.argv', generator_args):
            generator = ResourceGenerator(create_parser().parse_args())
        generator.generate()
        resource_path = os.path.join(self.project_name, 'server', 'src', 'main', 'java', *self.package.split("."))
        self.assertTrue(os.path.exists(os.path.join(self.random_dir, resource_path, 'fortune', 'impl', "FortunesResource.java")))
