from wrong_4_354 import *

import pytest
@pytest.mark.timeout(5)
def test_17163():
    assert sort_age([('F', 10), ('F', 31), ('F', 20), ('M', 9)]) == [('F', 31), ('F', 20), ('F', 10), ('M', 9)]
