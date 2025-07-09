# COMMANDS. An example of a function to run as a command-line command.
# If you aren't providing a command, you don't need this file.

from .dprs_compute import dprs_compute

# This file and function are mentioned in pyproject.toml in the
# [project.scripts] section, like this:

import sys

def dprs(x,y):
    """Calls file with implementation"""
    return dprs_compute(x,y)


def dprs_cli():
    """Calls file with implementation"""
    param1 = sys.argv[1]
    param2 = sys.argv[2]
    return dprs(param1,param2)
    
    
