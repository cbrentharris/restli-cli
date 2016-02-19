from unittest import TestCase
from restli.scaffolders import ProjectScaffolder
import uuid
import os
import shutil
import tempfile

class ProjectScaffolderTest(TestCase):
    def setUp(self):
        self.s = ProjectScaffolder()
        self.random_dir = os.path.join(tempfile.gettempdir(), uuid.uuid4().hex)
        os.makedirs(self.random_dir)

    def tearDown(self):
        del(self.s)
        if self.random_dir is not None:
            shutil.rmtree(self.random_dir)

    def test_it_creates_the_project_structure(self):
        os.chdir(self.random_dir)
        desired_project_folders = [
                os.path.join('my_project', 'api'),
                os.path.join('my_project', 'api', 'src', 'main', 'idl'),
                os.path.join('my_project', 'api', 'src', 'main', 'pegasus'),
                os.path.join('my_project', 'api', 'src', 'main', 'mainGeneratedDataTemplate'),
                os.path.join('my_project', 'client'),
                os.path.join('my_project', 'server'),
                os.path.join('my_project', 'server', 'src', 'main', 'java'),
                os.path.join('my_project', 'server', 'src', 'main', 'mainGeneratedRest'),
        ]
        self.s.gen_project_structure('my_project')
        for _dir in desired_project_folders:
            self.assertTrue(os.path.exists(os.path.join(self.random_dir, _dir)))

    def test_it_creates_gradle_build_files(self):
        os.chdir(self.random_dir)
        self.s.gen_project_structure('my_project')
        self.s.gen_gradle_build_files('my_project')
        desired_gradle_files = [
                os.path.join(self.random_dir, 'my_project', 'api', 'build.gradle'),
                os.path.join(self.random_dir, 'my_project', 'server', 'build.gradle'),
                os.path.join(self.random_dir, 'my_project', 'server', 'settings.gradle'),
                os.path.join(self.random_dir, 'my_project', 'build.gradle'),
                os.path.join(self.random_dir, 'my_project', 'settings.gradle'),
        ]
        for _file in desired_gradle_files:
            self.assertTrue(os.path.exists(_file))

