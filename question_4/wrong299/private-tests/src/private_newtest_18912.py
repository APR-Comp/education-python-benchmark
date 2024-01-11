from wrong_4_299 import *

import pytest
@pytest.mark.timeout(5)
def test_18912():
    assert sort_age([('M', 12)]) == [('M', 12)]
