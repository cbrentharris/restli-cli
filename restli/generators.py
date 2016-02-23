import os
from jinja2 import Environment, PackageLoader
from restli.utils import OutputMessages, logger, user_input, find_directory

class Generator(object):
    
    TEMPLATE_ENV = Environment(loader=PackageLoader('restli', 'templates'))

    def generate_file(self, file_name, directory, template_name, template_var):
        full_file_path = os.path.join(directory, file_name)
        need_to_prompt = os.path.exists(full_file_path)
        if need_to_prompt:
            question = OutputMessages.WOULD_YOU_LIKE_TO_OVERWRITE.format(file_name, directory)
            response = user_input(question)
        if not need_to_prompt or response == 'y':
            with open(full_file_path, 'w') as output_file:
                template = self.TEMPLATE_ENV.get_template(template_name)
                if not need_to_prompt:
                    logger.info(OutputMessages.GENERATING.format(full_file_path))
                else:
                    logger.info(OutputMessages.OVERWRITING.format(full_file_path))
                output_file.write(template.render({ template_var : self }))


class PegasusGenerator(Generator):

    def __init__(self, args):
        self.name = args.generate
        self.type = args.type
        self.namespace = args.namespace
        self.doc = args.doc
        self.fields = []
        for field in args.fields.split(" "):
            self.fields.append(field.split(":"))

    def generate(self):
        pegasus_root_dir = find_directory('pegasus')
        # A namespace is a java namespace that looks like "com.example"
        pegasus_file_dir = os.path.join(os.path.join(pegasus_root_dir, *self.namespace.split(".")), self.name.lower())
        if not os.path.exists(pegasus_file_dir):
            os.makedirs(pegasus_file_dir)
        pegasus_file_name = "{}.pdsc".format(self.name) 
        self.generate_file(pegasus_file_name, pegasus_file_dir, 'DataTemplate.pdsc', 'schema')


class ResourceGenerator(Generator):

    def __init__(self, args):
        self.methods = args.methods.split(" ")
        self.namespace = args.namespace
        self.name = args.generate

    def generate(self):
        resource_root_dir = find_directory('server/src/main/java')
        resource_file_dir = os.path.join(os.path.join(resource_root_dir, *self.namespace.split(".")), self.name.lower(), "impl")
        if not os.path.exists(resource_file_dir):
            os.makedirs(resource_file_dir)
        resource_file_name = "{}sResource.java".format(self.name)
        self.generate_file(resource_file_name, resource_file_dir, 'Resource.java', 'resource')

        resource_test_root_dir = find_directory('server/src/test/java')
        resource_test_dir = os.path.join(os.path.join(resource_test_root_dir, *self.namespace.split(".")), self.name.lower())
        if not os.path.exists(resource_test_dir):
            os.makedirs(resource_test_dir)
        resource_test_file_name = "Test{}sResource.java".format(self.name)
        self.generate_file(resource_test_file_name, resource_test_dir, "TestResource.java", "resource")


