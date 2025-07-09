# COMMANDS. An example of a function to run as a command-line command.
# If you aren't providing a command, you don't need this file.

from .dprs_compute import dprs_compute

# This file and function are mentioned in pyproject.toml in the
# [project.scripts] section, like this:


def dprs():
    """Calls file with implementation"""
    return dprs_compute(42,42)
    
    
