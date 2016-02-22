import os
from jinja2 import Environment, PackageLoader

class PegasusGenerator(object):

    def __init__(self, args):
        self.name = args.name
        self.schema_type = args.schema_type
        self.namespace = args.namespace
        self.fields = []
        for field in args.fields.split(" "):
            self.fields.append(field.split(":"))

    def generate(self):
        pegasus_root_dir = self.find_pegasus_directory()
        # A namespace is a java namespace that looks like "com.example"
        pegasus_file_dir = os.path.join(os.path.join(pegasus_root_dir, *self.namespace.split(".")), self.name.lower())
        if not os.path.exists(pegasus_file_dir):
            os.makedirs(pegasus_file_dir)
        with open(os.path.join(pegasus_file_dir, "{}.pdsc".format(self.name)), 'w') as pegasus_file:
            env = Environment(loader=PackageLoader('restli', 'templates'))
            template = env.get_template('DataTemplate.pdsc')
            pegasus_file.write(template.render({ 'schema' : self }))

    def find_pegasus_directory(self):
        for dir_name, _, _ in os.walk(os.getcwd()):
            if dir_name.endswith('pegasus'):
                return dir_name
        raise Exception("No pegasus directory found in current directory structure. Please run restli --scaffold [project-name] to generate a restli directory structure")


class ResourceGenerator(object):

    def __init__(self, args):
        pass

