from wrong_4_284 import *

import pytest
@pytest.mark.timeout(5)
def test_5873():
    assert sort_age([('M', 1), ('M', 19)]) == [('M', 19), ('M', 1)]
