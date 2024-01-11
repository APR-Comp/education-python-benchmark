from wrong_4_354 import *

import pytest
@pytest.mark.timeout(5)
def test_338():
    assert sort_age([('M', 12)]) == [('M', 12)]
