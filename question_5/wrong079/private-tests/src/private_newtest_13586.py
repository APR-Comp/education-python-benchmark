from wrong_5_079 import *

import pytest
@pytest.mark.timeout(5)
def test_13586():
    assert top_k([5958, 72, 28],1) == [5958]
