from wrong_4_309 import *

import pytest
@pytest.mark.timeout(5)
def test_13062():
    assert sort_age([('M', 5)]) == [('M', 5)]
