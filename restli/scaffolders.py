import os
from jinja2 import Environment, PackageLoader
from restli.utils import OutputMessages, logger

class Scaffolder(object):

    def __init__(self, args):
        self.name = args.scaffold
        self.package = args.namespace


class ProjectScaffolder(Scaffolder):
    
    def scaffold(self):
        self.gen_project_structure()
        self.gen_gradle_build_files()
        logger.info("\tGenerated project structure: ")
        logger.info("\n" + OutputMessages.tree(os.path.join(os.getcwd(), self.name)))

    def gen_project_structure(self):
        project_name = self.name
        root = os.path.join(os.getcwd(), project_name)
        if not os.path.exists(root):
            os.makedirs(root)
        for subdir in ['api', 'client', 'server']:
            if not os.path.exists(os.path.join(root, subdir)):
                os.makedirs(os.path.join(root, subdir))

        api_dir = os.path.join(root, 'api')
        for api_subdir in ['idl', 'pegasus', 'mainGeneratedDataTemplate']:
            if not os.path.exists(os.path.join(api_dir, 'src', 'main', api_subdir)):
                os.makedirs(os.path.join(api_dir, 'src', 'main', api_subdir))

        server_dir = os.path.join(root, 'server')
        for server_subdir in ['java', 'mainGeneratedRest']:
            if not os.path.exists(os.path.join(server_dir, 'src', 'main', server_subdir)):
                os.makedirs(os.path.join(server_dir, 'src', 'main', server_subdir))

        if not os.path.exists(os.path.join(server_dir, 'src', 'test', 'java')):
            os.makedirs(os.path.join(server_dir, 'src', 'test', 'java'))

    def gen_gradle_build_files(self):
        project_name = self.name
        env = Environment(loader=PackageLoader('restli', 'templates'))
        root = os.path.join(os.getcwd(), project_name)
        gradles_to_build = [
                (os.path.join(root, 'api', 'build.gradle'), 'api_build.gradle'),
                (os.path.join(root, 'server', 'settings.gradle'), 'server_settings.gradle'),
                (os.path.join(root, 'build.gradle'), 'toplevel_build.gradle'),
                (os.path.join(root, 'settings.gradle'), 'toplevel_settings.gradle'),
        ]
        for file_path, template_name in gradles_to_build:
            with open(file_path, 'w') as gradle_file:
                template = env.get_template(template_name)
                # TODO: Determine if any of these templates will need context variables.
                gradle_file.write(template.render({}))

        with open(os.path.join(os.getcwd(), project_name, 'server', 'build.gradle'), 'w') as server_gradle_build:
            template = env.get_template('server_build.gradle')
            #TODO: fix package name with DI?
            server_gradle_build.write(template.render({ 'package': self.package }))


