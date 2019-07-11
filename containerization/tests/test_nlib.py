"""pytest tests for library"""

import pytest
import sys
sys.path.append("..")
from nlib import csvops

def test_list_csv_column_names():
    expected = ['first_name', 'last_name', 'count']
    actual = csvops.list_csv_column_names("../ext/input.csv")
    assert expected == actual

def test_group_by_operations():
    """
    data, groupby_column_name, apply_column_name
    """
    expected = {"john":22,"kristen":17,"piers":10,"sam":15}
    actual = csvops.aggregate_column_name(data="../ext/input.csv", 
            groupby_column_name="first_name", apply_column_name="count")
    assert expected == actual.to_dict()