from unittest import TestCase
from restli.scaffolders import ProjectScaffolder
from restli.command_line import create_parser
import uuid
import os
import shutil
import tempfile

class ProjectScaffolderTest(TestCase):

    def setUp(self):
        self.project_name = "my_project"
        args = create_parser().parse_args()
        args.name = self.project_name
        self.s = ProjectScaffolder(args)
        self.random_dir = os.path.join(tempfile.gettempdir(), uuid.uuid4().hex)
        os.makedirs(self.random_dir)

    def tearDown(self):
        del(self.s)
        if self.random_dir is not None:
            shutil.rmtree(self.random_dir)

    def test_it_creates_the_project_structure(self):
        os.chdir(self.random_dir)
        desired_project_folders = [
                os.path.join(self.project_name, 'api'),
                os.path.join(self.project_name, 'api', 'src', 'main', 'idl'),
                os.path.join(self.project_name, 'api', 'src', 'main', 'pegasus'),
                os.path.join(self.project_name, 'api', 'src', 'main', 'mainGeneratedDataTemplate'),
                os.path.join(self.project_name, 'client'),
                os.path.join(self.project_name, 'server'),
                os.path.join(self.project_name, 'server', 'src', 'main', 'java'),
                os.path.join(self.project_name, 'server', 'src', 'main', 'mainGeneratedRest'),
        ]
        self.s.gen_project_structure()
        for _dir in desired_project_folders:
            self.assertTrue(os.path.exists(os.path.join(self.random_dir, _dir)))

    def test_it_creates_gradle_build_files(self):
        os.chdir(self.random_dir)
        self.s.gen_project_structure()
        self.s.gen_gradle_build_files()
        desired_gradle_files = [
                os.path.join(self.random_dir, self.project_name, 'api', 'build.gradle'),
                os.path.join(self.random_dir, self.project_name, 'server', 'build.gradle'),
                os.path.join(self.random_dir, self.project_name, 'server', 'settings.gradle'),
                os.path.join(self.random_dir, self.project_name, 'build.gradle'),
                os.path.join(self.random_dir, self.project_name, 'settings.gradle'),
        ]
        for _file in desired_gradle_files:
            self.assertTrue(os.path.exists(_file))

