#!/usr/bin/env python
"""
Commandline Tool For Doing CSV operations:

    * Aggregation
    * TBD

"""

import sys

import click
from sensible.loginit import logger

import nlib
from nlib import csvops
from nlib import utils

log = logger(__name__)


@click.version_option(nlib.__version__)
@click.group()
def cli():
    """CSV Operations Tool

    """
@cli.command("cvsops")
@click.option('--file', help='Name of csv file')
@click.option('--groupby', help='GroupBy Column Name')
@click.option('--applyname', help='Apply Column Name')
@click.option('--func', help='Appliable Function')
def agg(file,groupby, applyname, func):
    """Operates on a groupby column in a csv file and applies a function

    Example Usage:
   ./csvcli.py cvsops --file ext/input.csv --groupby last_name --applyname count --func npmedian
    Processing csvfile: ext/input.csv and groupby name: last_name and applyname: count
    2017-06-22 14:07:52,532 - nlib.utils - INFO - Loading appliable functions/plugins: npmedian
    2017-06-22 14:07:52,533 - nlib.utils - INFO - Loading appliable functions/plugins: npsum
    2017-06-22 14:07:52,533 - nlib.utils - INFO - Loading appliable functions/plugins: numpy
    2017-06-22 14:07:52,533 - nlib.utils - INFO - Loading appliable functions/plugins: tanimoto
    last_name
    eagle    17.0
    lee       3.0
    smith    13.5
    Name: count, dtype: float64

    """
    if not file and not groupby and not applyname and not func:
        click.echo("--file and --column and --applyname --func are required")
        sys.exit(1)

    click.echo("Processing csvfile: {file} and groupby name: {groupby} and applyname: {applyname}".\
            format(file=file, groupby=groupby, applyname=applyname))
    #Load Plugins and grab correct one
    plugins = utils.plugins_map()
    appliable_func = plugins[func]
    res = csvops.group_by_operations(data=file, 
            groupby_column_name=groupby, apply_column_name=applyname,
            func=appliable_func)
    click.echo(res)

@cli.command("listfuncs")
def listfuncs():
    """Lists functions that can be applied to a GroupBy Operation

    Example Usage:

    ./csvcli.py listfuncs
    Appliable Functions: ['npmedian', 'npsum', 'numpy', 'tanimoto']
    """

    funcs = utils.appliable_functions()
    click.echo("Appliable Functions: {funcs}".format(funcs=funcs))


if __name__ == "__main__":
    cli()