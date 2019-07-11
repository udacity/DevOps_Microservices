"""
CSV Operations Module:

See this for notes on I/O Performance in Pandas:
    http://pandas.pydata.org/pandas-docs/stable/io.html#io-perf

"""

from sensible.loginit import logger
import pandas as pd

log = logger(__name__)
log.debug("imported csvops module")


def ingest_csv(data):
    """Ingests a CSV using Pandas CSV I/O"""

    df = pd.read_csv(data)
    return df

def list_csv_column_names(data):
    """Returns a list of column names from csv"""

    df = ingest_csv(data)
    colnames = list(df.columns.values)
    colnames_msg = "Column Names: {colnames}".format(colnames=colnames)
    log.info(colnames_msg)
    return colnames

def aggregate_column_name(data, groupby_column_name, apply_column_name):
    """Returns aggregated results of csv by column name as json"""

    
    df = ingest_csv(data)
    res = df.groupby(groupby_column_name)[apply_column_name].sum()
    return res

def group_by_operations(data, groupby_column_name, apply_column_name, func):
    """
    
    Allows a groupby operation to take arbitrary functions
    
    In [14]: res_sum = group_by_operations(data=data, groupby_column_name="last_name", columns="count", func=npsum)

    In [15]: res_sum
    Out[15]: 
    last_name
    eagle    34
    lee       3
    smith    27
    Name: count, dtype: int64

    """

    df = ingest_csv(data)
    grouped = df.groupby(groupby_column_name)[apply_column_name] #GroupBy with filter to specific column(s)
    applied_data = grouped.apply(func)
    return applied_data
