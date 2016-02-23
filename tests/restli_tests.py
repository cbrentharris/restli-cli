from unittest import TestCase
from restli.command_line import create_parser
from restli.scaffolders import ProjectScaffolder
import os
import tempfile
import shutil
import uuid
import mock

class BaseTest(TestCase):
    """
    This base test case sets up a random directory from the temp directory on a machine
    to be able to generate files and project structure.
    """

    def setUp(self):
        self.project_name = "my_project"
        self.package = "com.linkedin"
        scaffolder_args = ['restli', '--scaffold', self.project_name, '--namespace', self.package]
        with mock.patch('sys.argv', scaffolder_args):
            self.scaffolder = ProjectScaffolder(create_parser().parse_args())
        self.random_dir = os.path.join(tempfile.gettempdir(), uuid.uuid4().hex)
        os.makedirs(self.random_dir)

    def tearDown(self):
        if self.random_dir is not None:
            shutil.rmtree(self.random_dir)

