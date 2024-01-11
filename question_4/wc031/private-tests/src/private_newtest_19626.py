from wrong_correct_4_031 import *

import pytest
@pytest.mark.timeout(5)
def test_19626():
    assert sort_age([('M', 31), ('F', 9)]) == [('M', 31), ('F', 9)]
