from wrong_4_324 import *

import pytest
@pytest.mark.timeout(5)
def test_9018():
    assert sort_age([('M', 12)]) == [('M', 12)]
