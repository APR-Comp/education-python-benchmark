from wrong_4_274 import *

import pytest
@pytest.mark.timeout(5)
def test_7781():
    assert sort_age([('F', 5), ('F', 1), ('M', 2), ('F', 33), ('M', 4), ('F', 16), ('M', 1), ('F', 6), ('F', 19), ('F', 9)]) == [('F', 33), ('F', 19), ('F', 16), ('F', 9), ('F', 6), ('F', 5), ('M', 4), ('M', 2), ('M', 1), ('F', 1)]
