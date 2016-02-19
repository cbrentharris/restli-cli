from unittest import TestCase, mock
from restli.command_line import main

class ConsoleTest(TestCase):
    
    def test_it_scaffolds_a_project():
        args = ['restli', '--scaffold', 'project', '--name', 'my_project']
        with mock.patch('sys.argv', args):
            # TODO: Figure out best way to avoid logic in other scaffolder tests
            pass
