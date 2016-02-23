from restli.generators import PegasusGenerator
from restli.command_line import create_parser
from tests.restli_tests import BaseTest
import os
import mock

class PegasusGeneratorTest(BaseTest):

    def setUp(self):
        super(PegasusGeneratorTest, self).setUp()
        os.chdir(self.random_dir)
        self.scaffolder.gen_project_structure()

    def test_it_creates_the_pegasus_file(self):
        generator_args = ['restli', '--generate', 'Fortune', '--namespace', self.package]
        with mock.patch('sys.argv', generator_args):
            generator = PegasusGenerator(create_parser().parse_args())
        generator.generate()
        self.assertTrue(os.path.exists(os.path.join(self.random_dir, self.pegasus_path(), 'fortune',  "Fortune.pdsc")))

    @mock.patch('restli.generators.user_input', return_value='n')
    def test_it_doesnt_overwrite_a_pegasus_file(self, mock_user_input):
        generator_args = ['restli', '--generate', 'Todo', '--namespace', self.package, '--fields', 'name:string']
        generator = self.new_pegasus_generator(generator_args)
        generator.generate()
        # Remove the name field.
        generator_args = ['restli', '--generate', 'Todo', '--namespace', self.package]
        generator = self.new_pegasus_generator(generator_args)
        generator.generate()
        with open(os.path.join(self.random_dir, self.pegasus_path(), 'todo', 'Todo.pdsc'), 'r') as pegasus_file:
            self.assertTrue('"name": "name", "type": "string"' in pegasus_file.read())

    @mock.patch('restli.generators.user_input', return_value='y')
    def test_it_does_overwrite_a_pegasus_file(self, mock_user_input):
        generator_args = ['restli', '--generate', 'Task', '--namespace', self.package, '--fields', 'name:string']
        generator = self.new_pegasus_generator(generator_args)
        generator.generate()
        # Remove the name field.
        generator_args = ['restli', '--generate', 'Task', '--namespace', self.package]
        generator = self.new_pegasus_generator(generator_args)
        generator.generate()
        with open(os.path.join(self.random_dir, self.pegasus_path(), 'task', 'Task.pdsc'), 'r') as pegasus_file:
            self.assertTrue('"name": "name", "type": "string"' not in pegasus_file.read())

    def pegasus_path(self):
        return os.path.join(self.project_name, 'api', 'src', 'main', 'pegasus', *self.package.split("."))

    def new_pegasus_generator(self, args):
        with mock.patch('sys.argv', args):
            return PegasusGenerator(create_parser().parse_args())

        
