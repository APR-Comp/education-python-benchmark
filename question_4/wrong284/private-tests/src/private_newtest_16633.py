from wrong_4_284 import *

import pytest
@pytest.mark.timeout(5)
def test_16633():
    assert sort_age([('F', 5)]) == [('F', 5)]
