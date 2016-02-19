import os
from jinja2 import Environment, Environment, PackageLoader

class PegasusScaffolder(object):
    pass

class ResourceScaffolder(object):
    pass

class ProjectScaffolder(object):

    def gen_project_structure(self, project_name):
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

    def gen_gradle_build_files(self, project_name):
        env = Environment(loader=PackageLoader('restli', 'templates'))
        with open(os.path.join(os.getcwd(), project_name, 'api', 'build.gradle'), 'w') as api_gradle_build:
            template = env.get_template('api_build.gradle')
            api_gradle_build.write(template.render({}))

        with open(os.path.join(os.getcwd(), project_name, 'server', 'build.gradle'), 'w') as server_gradle_build:
            template = env.get_template('server_build.gradle')
            #TODO: fix package name with DI?
            server_gradle_build.write(template.render({'package': 'some.fake.package'}))

        with open(os.path.join(os.getcwd(), project_name, 'server', 'settings.gradle'), 'w') as server_gradle_settings:
            template = env.get_template('server_settings.gradle')
            server_gradle_settings.write(template.render({}))

        with open(os.path.join(os.getcwd(), project_name, 'build.gradle'), 'w') as toplevel_gradle_build:
            template = env.get_template('toplevel_build.gradle')
            toplevel_gradle_build.write(template.render({}))

        with open(os.path.join(os.getcwd(), project_name, 'settings.gradle'), 'w') as toplevel_gradle_settings:
            template = env.get_template('toplevel_settings.gradle')
            toplevel_gradle_settings.write(template.render({}))


