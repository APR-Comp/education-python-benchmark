from wrong_correct_2_004 import *

import pytest
@pytest.mark.timeout(5)
def test_822():
    assert contains_unique_day("July",[('July', 6), ('March', 29), ('June', 29)]) == True
