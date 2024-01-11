from wrong_correct_2_049 import *

import pytest
@pytest.mark.timeout(5)
def test_375():
    assert contains_unique_day("March",[('September', 2), ('September', 2), ('January', 7), ('May', 6), ('March', 4)]) == True
