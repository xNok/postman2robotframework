# coding: utf-8
"""
CONCOURSE PIPELINE MAKER

Usage:
  postman2robot [--ifile <inputfile>] [--ofile <outputfile>] [options]
  postman2robot -h

Options:
  -i <inputfile>, --ifile <inputfile>       Path to the postman collection. [default: cellection.json]
  -o <outputfile>, --ofile <outputfile>     Path to the output folder. [default: ./postman_libraries]
Options-Flags:
  -h, --help                                Show the help screen.
"""

# Utilitaire pour gérer les commande lines
from docopt import docopt
from .h_colors import *
from deepmerge import always_merger

import logging
import json

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

    print("""
    {tag} Use {color} postman2robot -h {reset} to lear how to use the command line"
    """.format(tag=tag.info,color=fg.green,reset=ft.reset,))

    rc_file = ".postman2robotrc"
    if os.path.exists(rc_file):
        print("""
        {tag} Loading runtime config from .cpmrc file {reset}"
        """.format(tag=tag.info,reset=ft.reset,))
        with open(rc_file) as f:
            cli_args_rc = json.load(f)
    else:
        print("""
        {tag} Locally you can use {color}.postman2robotrc file {reset} to avoide typing options everytime"
        """.format(tag=tag.info,color=fg.green,reset=ft.reset,))

    cli_args = always_merger.merge(cli_args, cli_args_rc)

    run(cli_args)

# Execute the 
def run(cli_args):

    pass