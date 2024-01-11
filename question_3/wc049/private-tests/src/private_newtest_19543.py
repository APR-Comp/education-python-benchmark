from wrong_correct_3_049 import *

import pytest
@pytest.mark.timeout(5)
def test_19543():
    assert remove_extras([68453, 979, 7, 52, 8]) == [68453, 979, 7, 52, 8]
