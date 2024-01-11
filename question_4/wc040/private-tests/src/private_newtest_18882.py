from wrong_correct_4_040 import *

import pytest
@pytest.mark.timeout(5)
def test_18882():
    assert sort_age([('F', 5), ('F', 3)]) == [('F', 5), ('F', 3)]
