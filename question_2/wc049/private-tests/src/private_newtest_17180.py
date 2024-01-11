from wrong_correct_2_049 import *

import pytest
@pytest.mark.timeout(5)
def test_17180():
    assert contains_unique_day("February",[('May', 14), ('September', 7)]) == False
