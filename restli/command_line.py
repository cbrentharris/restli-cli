import argparse
from restli.scaffolders import ProjectScaffolder
from restli.generators import PegasusGenerator, ResourceGenerator

def create_parser():
    parser = argparse.ArgumentParser(description="A command line tool for restli projects.")
    parser.add_argument('-s', '--scaffold', help="Scaffold a new restli project. usage: --scaffold [name] [package]")
    parser.add_argument('-g', '--generate', help="What restli file you would like to generate", choices=['pegasus', 'resource'])
    parser.add_argument('-n', '--name', help="Name of the restli pegasus schema")
    parser.add_argument('-t', '--type', help="Type of the restli pegasus schema")
    parser.add_argument('-f', '--fields', help="The fields included in your pegasus schema")
    parser.add_argument('-d', '--doc', help="The doc for the pegasus schema")
    parser.add_argument('-ns', '--namespace', help="The namespace for the pegasus schema")
    parser.add_argument('-m', '--methods', help="The CRUD methods to implement for your resource")
    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()
    if args.scaffold:
        scaffolder = ProjectScaffolder(args)
        scaffolder.scaffold()
    elif args.generate == 'pegasus':
        generator = PegasusGenerator(args)
        generator.generate()
    elif args.generate == 'resource':
        generator = ResourceGenerator(args)
        generator.generate()

if __name__ == "__main__":
    main()
