import json

import pytest

from number_swap import app

def test_split_numbers():
    assert app.split_numbers("1,2") == [1,2]

def test_is_number_swap():
    assert app.is_number_swap([2,5]) == (5,2)