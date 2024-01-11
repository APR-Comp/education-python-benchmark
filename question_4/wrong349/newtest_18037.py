from wrong_4_349 import *

import pytest
@pytest.mark.timeout(5)
def test_18037():
    assert sort_age([('F', 9), ('F', 32)]) == [('F', 32), ('F', 9)]
