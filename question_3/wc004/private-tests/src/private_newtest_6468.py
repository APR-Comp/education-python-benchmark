from wrong_correct_3_004 import *

import pytest
@pytest.mark.timeout(5)
def test_6468():
    assert remove_extras([5, 770, 7]) == [5, 770, 7]
