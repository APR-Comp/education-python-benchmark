from wrong_4_279 import *

import pytest
@pytest.mark.timeout(5)
def test_10388():
    assert sort_age([('F', 16)]) == [('F', 16)]
