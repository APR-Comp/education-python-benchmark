from wrong_4_284 import *

import pytest
@pytest.mark.timeout(5)
def test_11798():
    assert sort_age([('M', 26)]) == [('M', 26)]
