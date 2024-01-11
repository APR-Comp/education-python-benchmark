from wrong_correct_3_049 import *

import pytest
@pytest.mark.timeout(5)
def test_12634():
    assert remove_extras([1, 3]) == [1, 3]
