from wrong_4_324 import *

import pytest
@pytest.mark.timeout(5)
def test_18781():
    assert sort_age([('M', 16)]) == [('M', 16)]
