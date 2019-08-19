# coding: utf-8
"""
POSTMAN TO ROBOTFRAMEWORK

Usage:
  postman2robot [--ifile <inputfile>] [--ofile <outputfile>] [options]
  postman2robot -h

Options:
  -i <inputfile>, --ifile <inputfile>       Path to the postman collection. [default: collection.json]
  -o <outputfile>, --ofile <outputfile>     Path to the output folder. [default: ./postman_libraries]
Options-Flags:
  -h, --help                                Show the help screen.
"""

# Utilitaire pour gérer les commande lines
from docopt import docopt
from .h_colors import *
from deepmerge import always_merger
from jinja2 import Environment, PackageLoader

import logging
import json
import os

from src.postman_parser import PostmanParser

# Parse command line argument
def main():
    ################################################################################################
    #### Pre-processing
    ################################################################################################
    cli_args = docopt(__doc__, argv=None, help=True, version=None, options_first=False)

    print("""
    ####################################
    #                                  #
    #     POSTMAN TO ROBOTFRAMEWOK     #
    #                                  #
    ####################################
    """)

    print("{tag} Use {color} postman2robot -h {reset} to learn how to use the command line"
      .format(tag=tag.info,color=fg.green,reset=ft.reset))

    rc_file = ".postman2robotrc"
    if os.path.exists(rc_file):
        print("{tag} Loading runtime config from .cpmrc file {reset}"
          .format(tag=tag.info,reset=ft.reset,))
        with open(rc_file) as f:
            cli_args_rc = json.load(f)

        cli_args = always_merger.merge(cli_args, cli_args_rc)
    else:
        print("{tag} You can use a {color}.postman2robotrc file {reset} to avoide typing options everytime"
          .format(tag=tag.info,color=fg.green,reset=ft.reset))

    run(cli_args)

# Execute the 
def run(cli_args):

    if not os.path.exists(cli_args["--ifile"]):
      print("""
      {tag} Expecting to fing  {color} cli_args["--ifile"] {reset} use --ifile to define the collection to convert"
      """.format(tag=tag.warn,color=fg.green,reset=ft.reset))

      exit(1)

    parser = PostmanParser(cli_args["--ifile"])

    lib = parser.get_library_from_collection()

    env = Environment(
      loader=PackageLoader('src', 'assets'),
    )

    template = env.get_template('library_template.py')
    
    os.makedirs(cli_args["--ofile"], exist_ok=True)

    # to save the results
    with open(cli_args["--ofile"] + "/" + lib["name"] + ".py", "w") as fh:
        fh.write(template.render(name=lib["name"],items=lib["items"],variables=lib["variables"]))
