from tests.restli_tests import BaseTest
import os

class ProjectScaffolderTest(BaseTest):

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
                os.path.join(self.project_name, 'server', 'src', 'test', 'java'),
        ]
        self.scaffolder.gen_project_structure()
        for _dir in desired_project_folders:
            self.assertTrue(os.path.exists(os.path.join(self.random_dir, _dir)))

    def test_it_creates_gradle_build_files(self):
        os.chdir(self.random_dir)
        self.scaffolder.gen_project_structure()
        self.scaffolder.gen_gradle_build_files()
        desired_gradle_files = [
                os.path.join(self.random_dir, self.project_name, 'api', 'build.gradle'),
                os.path.join(self.random_dir, self.project_name, 'server', 'build.gradle'),
                os.path.join(self.random_dir, self.project_name, 'server', 'settings.gradle'),
                os.path.join(self.random_dir, self.project_name, 'build.gradle'),
                os.path.join(self.random_dir, self.project_name, 'settings.gradle'),
        ]
        for _file in desired_gradle_files:
            self.assertTrue(os.path.exists(_file))

