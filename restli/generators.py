class PegasusGenerator(object):

    def __init__(self, args):
        self.name = args.name
        self.schema_type = args.schema_type
        self.namespace = args.namespace
        self.fields = []
        for field in args.fields.split(" "):
            self.fields.append(field.split(":"))

    def generate(self):
        pass

class ResourceGenerator(object):

    def __init__(self, args):
        pass

