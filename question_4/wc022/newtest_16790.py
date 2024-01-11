from wrong_correct_4_022 import *

import pytest
@pytest.mark.timeout(5)
def test_16790():
    assert sort_age([('M', 13), ('F', 14), ('F', 33), ('F', 29), ('F', 25)]) == [('F', 33), ('F', 29), ('F', 25), ('F', 14), ('M', 13)]
