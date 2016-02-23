from tests.restli_tests import BaseTest
from restli.generators import ResourceGenerator
from restli.command_line import create_parser
import os

class ResourceGeneratorTest(BaseTest):

    def test_it_creates_the_resource_file(self):
        os.chdir(self.random_dir)
        self.scaffolder.gen_project_structure()
        args = create_parser().parse_args()
        args.generate = "Fortune"
        args.namespace = self.package
        generator = ResourceGenerator(args)
        generator.generate()
        resource_path = os.path.join(self.project_name, 'server', 'src', 'main', 'java', *self.package.split("."))
        self.assertTrue(os.path.exists(os.path.join(self.random_dir, resource_path, args.generate.lower(), 'impl', args.generate + "sResource.java")))
