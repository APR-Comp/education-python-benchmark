from wrong_4_294 import *

import pytest
@pytest.mark.timeout(5)
def test_8237():
    assert sort_age([('F', 28), ('F', 12), ('M', 3)]) == [('F', 28), ('F', 12), ('M', 3)]
