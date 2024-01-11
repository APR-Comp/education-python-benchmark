from wrong_correct_2_058 import *

import pytest
@pytest.mark.timeout(5)
def test_19864():
    assert contains_unique_day("July",[('July', 7), ('September', 2)]) == True
