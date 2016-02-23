import argparse
from restli.scaffolders import ProjectScaffolder
from restli.generators import PegasusGenerator, ResourceGenerator

def create_parser():
    parser = argparse.ArgumentParser(description="A command line tool for restli projects.")
    parser.add_argument('-s', '--scaffold', help="THe name of your restli project")
    parser.add_argument('-g', '--generate', help="The name of the pegasus / resource file")
    parser.add_argument('-t', '--type', help="Type of the restli pegasus schema", default="record")
    parser.add_argument('-f', '--fields', help="The fields included in your pegasus schema", default="id:long")
    parser.add_argument('-d', '--doc', help="The doc for the pegasus schema")
    parser.add_argument('-ns', '--namespace', help="The namespace for the pegasus / resource file")
    parser.add_argument('-m', '--methods', help="The CRUD methods to implement for your resource", default="get update create delete")
    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()
    if args.scaffold:
        scaffolder = ProjectScaffolder(args)
        scaffolder.scaffold()
    if args.generate:
        pegasus_generator = PegasusGenerator(args)
        pegasus_generator.generate()
        resource_generator = ResourceGenerator(args)
        resource_generator.generate()

if __name__ == "__main__":
    main()
