from wrong_4_299 import *

import pytest
@pytest.mark.timeout(5)
def test_380():
    assert sort_age([('F', 7)]) == [('F', 7)]
