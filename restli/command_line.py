import argparse
from restli.scaffolders import ProjectScaffolder

def create_parser():
    parser = argparse.ArgumentParser(description="A command line tool for restli projects.")
    parser.add_argument('-s', '--scaffold', help="Scaffold a new restli project. usage: --scaffold [name] [package]")
    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()
    if args.scaffold:
        scaffolder = ProjectScaffolder(args)
        scafffolder.scaffold()

if __name__ == "__main__":
    main()
