import os
from jinja2 import Environment, PackageLoader
from restli.utils import OutputMessages, logger

class PegasusGenerator(object):

    def __init__(self, args):
        self.name = args.generate
        self.type = args.type
        self.namespace = args.namespace
        self.doc = args.doc
        self.fields = []
        for field in args.fields.split(" "):
            self.fields.append(field.split(":"))

    def generate(self):
        pegasus_root_dir = self.find_pegasus_directory()
        # A namespace is a java namespace that looks like "com.example"
        pegasus_file_dir = os.path.join(os.path.join(pegasus_root_dir, *self.namespace.split(".")), self.name.lower())
        if not os.path.exists(pegasus_file_dir):
            os.makedirs(pegasus_file_dir)
        pegasus_file_name = "{}.pdsc".format(self.name) 
        pegasus_file_full_path = os.path.join(pegasus_file_dir, pegasus_file_name)
        # We don't want to overwrite an existing pdsc file if it already exists
        need_to_prompt = os.path.exists(pegasus_file_full_path)
        if need_to_prompt:
            question = OutputMessages.WOULD_YOU_LIKE_TO_OVERWRITE.format(pegasus_file_name, pegasus_file_dir)
            response = input(question)
        if not need_to_prompt or response == 'y':
            with open(pegasus_file_full_path, 'w') as pegasus_file:
                env = Environment(loader=PackageLoader('restli', 'templates'))
                template = env.get_template('DataTemplate.pdsc')
                if not need_to_prompt:
                    logger.info(OutputMessages.GENERATING.format(pegasus_file_full_path))
                else:
                    logger.info(OutputMessages.OVERWRITING.format(pegasus_file_full_path))
                pegasus_file.write(template.render({ 'schema' : self }))

    def find_pegasus_directory(self):
        for dir_name, _, _ in os.walk(os.getcwd()):
            if dir_name.endswith('pegasus'):
                return dir_name
        raise Exception(OutputMessages.NO_DIRECTORY_FOUND.format('pegasus'))


class ResourceGenerator(object):

    def __init__(self, args):
        self.methods = args.methods.split(" ")
        self.namespace = args.namespace
        self.name = args.generate

    def generate(self):
        resource_root_dir = self.find_resource_directory()
        resource_file_dir = os.path.join(os.path.join(resource_root_dir, *self.namespace.split(".")), self.name.lower(), "impl")
        if not os.path.exists(resource_file_dir):
            os.makedirs(resource_file_dir)
        resource_file_name = "{}sResource.java".format(self.name)
        resource_file_full_path = os.path.join(resource_file_dir, resource_file_name)
        # We don't want to overwrite an existing java file if it already exists
        need_to_prompt = os.path.exists(resource_file_full_path)
        if need_to_prompt:
            question = OutputMessages.WOULD_YOU_LIKE_TO_OVERWRITE.format(resource_file_name, resource_file_dir)
            response = input(question)
        if not need_to_prompt or response == 'y':
            with open(resource_file_full_path, 'w') as resource_file:
                env = Environment(loader=PackageLoader('restli', 'templates'))
                template = env.get_template("Resource.java")
                if not need_to_prompt:
                    logger.info(OutputMessages.GENERATING.format(resource_file_full_path))
                else:
                    logger.info(OutputMessages.OVERWRITING.format(resource_file_full_path))
                resource_file.write(template.render({ 'resource' : self }))

    def find_resource_directory(self):
        for dir_name, _, _ in os.walk(os.getcwd()):
            if dir_name.endswith('server/src/main/java'):
                return dir_name
        raise Exception(OutputMessages.NO_DIRECTORY_FOUND.format('server/src/main/java'))

