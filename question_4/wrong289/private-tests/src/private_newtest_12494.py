from wrong_4_289 import *

import pytest
@pytest.mark.timeout(5)
def test_12494():
    assert sort_age([('M', 3)]) == [('M', 3)]
