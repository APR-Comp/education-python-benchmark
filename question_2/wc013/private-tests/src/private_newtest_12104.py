from wrong_correct_2_013 import *

import pytest
@pytest.mark.timeout(5)
def test_12104():
    assert contains_unique_day("July",[('February', 19), ('September', 2)]) == False
