from wrong_4_354 import *

import pytest
@pytest.mark.timeout(5)
def test_5143():
    assert sort_age([('M', 5)]) == [('M', 5)]
