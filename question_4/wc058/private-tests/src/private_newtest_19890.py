from wrong_correct_4_058 import *

import pytest
@pytest.mark.timeout(5)
def test_19890():
    assert sort_age([('F', 5), ('M', 27), ('F', 39), ('M', 4)]) == [('F', 39), ('M', 27), ('F', 5), ('M', 4)]
