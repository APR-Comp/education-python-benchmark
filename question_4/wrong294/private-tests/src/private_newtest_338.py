from wrong_4_294 import *

import pytest
@pytest.mark.timeout(5)
def test_338():
    assert sort_age([('M', 12)]) == [('M', 12)]
