import argparse
from restli.scaffolders import *

class Scaffold:
    PROJECT = "project"
    PEGASUS = "pegasus"
    RESOURCE = "resource"

    CHOICES = [PROJECT, PEGASUS, RESOURCE]

def create_parser():
    parser = argparse.ArgumentParser(description="A command line tool for restli projects.")
    parser.add_argument('-s', '--scaffold', help="What you would like to scaffold. pegasus = A pegasus pdsc data template, project = General project layout, resource = A restli resource.", choices=Scaffold.CHOICES, default=Scaffold.PROJECT)
    parser.add_argument('-n', '--name', help="Name of the project, pegasus data schema, or resource")
    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()
    scaffolders = { Scaffold.PROJECT : ProjectScaffolder, Scaffold.PEGASUS : PegasusScaffolder, Scaffold.PROJECT : ProjectScaffolder }
    scaffolder_class = scaffolders.get(args.scaffold)
    scaffolder = scaffolder_class(args)
    scaffolder.scaffold()


if __name__ == "__main__":
    main()
