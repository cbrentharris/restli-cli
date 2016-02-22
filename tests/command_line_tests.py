from restli.command_line import main
from unittest import TestCase
import mock

class ConsoleTest(TestCase):
    
    def test_it_scaffolds_a_project(self):
        args = ['restli', '--scaffold', 'my_project com.linkedin']
        with mock.patch('sys.argv', args):
            with mock.patch('restli.scaffolders.ProjectScaffolder.scaffold') as fake_scaffold:
                main()
                fake_scaffold.assert_called_with()

    def test_it_generates_a_pegasus_file(self):
        args = ['restli', '--generate', 'pegasus', '--name' , 'Fortune', '--type', 'record', '--fields', 'name:string id:long', '--namespace', 'com.linkedin']
        with mock.patch('sys.argv', args):
            with mock.patch('restli.generators.PegasusGenerator.generate') as fake_generate:
                main()
                fake_generate.assert_called_with()

    def test_it_generates_a_restli_resource(self):
        args = ['restli', '--generate', 'resource', '--name', 'Fortune', '--namespace', 'com.linkedin', '--methods', 'get']
        with mock.patch('sys.argv', args):
            with mock.patch('restli.generators.ResourceGenerator.generate') as fake_generate:
                main()
                fake_generate.assert_called_with()
