#!/usr/bin/env python



"""
Commandline tool for interacting with library
"""
import click

from myrepolib.repomod import print_name
from myrepolib import __version__


@click.version_option(__version__)
@click.command()
@click.option("--name", help="name to print")
def pname(name):
    """Prints a name out with apple at the end"""
    try:
        res = print_name(name)
        click.echo(click.style(res, bg='blue', fg='white'))
    except TypeError:
        click.echo("Must pass in Name")
if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    pname()
