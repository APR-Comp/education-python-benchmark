from wrong_correct_2_049 import *

import pytest
@pytest.mark.timeout(5)
def test_7713():
    assert contains_unique_day("March",[('February', 3), ('April', 6)]) == False
