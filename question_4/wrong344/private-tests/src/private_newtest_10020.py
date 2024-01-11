from wrong_4_344 import *

import pytest
@pytest.mark.timeout(5)
def test_10020():
    assert sort_age([('M', 24), ('M', 2)]) == [('M', 24), ('M', 2)]
