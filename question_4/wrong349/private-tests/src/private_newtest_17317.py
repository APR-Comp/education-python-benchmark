from wrong_4_349 import *

import pytest
@pytest.mark.timeout(5)
def test_17317():
    assert sort_age([('F', 2), ('F', 8)]) == [('F', 8), ('F', 2)]
