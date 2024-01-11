from wrong_4_344 import *

import pytest
@pytest.mark.timeout(5)
def test_13197():
    assert sort_age([('F', 5), ('M', 6)]) == [('M', 6), ('F', 5)]
