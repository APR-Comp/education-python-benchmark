from wrong_4_299 import *

import pytest
@pytest.mark.timeout(5)
def test_14584():
    assert sort_age([('F', 23), ('F', 24)]) == [('F', 24), ('F', 23)]
