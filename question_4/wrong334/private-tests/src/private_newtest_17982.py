from wrong_4_334 import *

import pytest
@pytest.mark.timeout(5)
def test_17982():
    assert sort_age([('F', 5), ('M', 6)]) == [('M', 6), ('F', 5)]