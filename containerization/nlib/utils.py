"""Utilities


Main use it to serve as a 'plugins' utility so that functions can be:
    * registered
    * discovered
    * documented

"""

import importlib

from sensible.loginit import logger

log = logger(__name__)

def appliable_functions():
    """Returns a list of appliable functions to be used in GroupBy Operations"""

    from . import appliable
    module_items = dir(appliable)
    #Filter out special items __
    func_list = list(filter(lambda x: not x.startswith("__"), module_items))
    return func_list


def plugins_map():
    """Create a dictionary of callable functions

    In [2]: plugins = utils.plugins_map()
    2017-06-22 10:34:25,312 - nlib.utils - INFO - Loading appliable functions/plugins: npmedian
    2017-06-22 10:34:25,312 - nlib.utils - INFO - Loading appliable functions/plugins: npsum
    2017-06-22 10:34:25,312 - nlib.utils - INFO - Loading appliable functions/plugins: numpy
    2017-06-22 10:34:25,312 - nlib.utils - INFO - Loading appliable functions/plugins: tanimoto

    In [3]: plugins
    Out[3]: 
    {'npmedian': <function nlib.appliable.npmedian>,
    'npsum': <function nlib.appliable.npsum>,
    'numpy': <module 'numpy' from '/Users/noahgift/.nflixenv/lib/python3.6/site-packages/numpy/__init__.py'>,
    'tanimoto': <function nlib.appliable.tanimoto>}

    In [4]: plugins['npmedian']([1,3])
    Out[4]: 2.0
    """

    plugins = {}
    funcs = appliable_functions()
    for func in funcs:
        plugin_load_msg = "Loading appliable functions/plugins: {func}".format(func=func)
        log.info(plugin_load_msg)
        plugins[func] = getattr(importlib.import_module("nlib.appliable"), func)
    return plugins
