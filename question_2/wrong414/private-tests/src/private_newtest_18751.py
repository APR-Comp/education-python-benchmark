from wrong_2_414 import *

import pytest
@pytest.mark.timeout(5)
def test_18751():
    assert contains_unique_day("December",[('October', 26), ('March', 30)]) == False
