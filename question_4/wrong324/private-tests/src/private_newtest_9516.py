from wrong_4_324 import *

import pytest
@pytest.mark.timeout(5)
def test_9516():
    assert sort_age([('F', 5)]) == [('F', 5)]
