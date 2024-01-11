from wrong_4_334 import *

import pytest
@pytest.mark.timeout(5)
def test_11037():
    assert sort_age([('F', 27), ('F', 36), ('F', 26)]) == [('F', 36), ('F', 27), ('F', 26)]
