from wrong_correct_3_058 import *

import pytest
@pytest.mark.timeout(5)
def test_15045():
    assert remove_extras([26835, 77, 31, 199, 8, 724]) == [26835, 77, 31, 199, 8, 724]
