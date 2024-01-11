from wrong_4_354 import *

import pytest
@pytest.mark.timeout(5)
def test_14383():
    assert sort_age([('F', 0)]) == [('F', 0)]
