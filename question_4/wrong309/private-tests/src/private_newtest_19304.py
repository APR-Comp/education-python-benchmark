from wrong_4_309 import *

import pytest
@pytest.mark.timeout(5)
def test_19304():
    assert sort_age([('M', 5), ('F', 7), ('F', 13), ('M', 2)]) == [('F', 13), ('F', 7), ('M', 5), ('M', 2)]
