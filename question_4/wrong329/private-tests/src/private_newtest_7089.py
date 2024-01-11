from wrong_4_329 import *

import pytest
@pytest.mark.timeout(5)
def test_7089():
    assert sort_age([('F', 5)]) == [('F', 5)]
