from wrong_correct_2_049 import *

import pytest
@pytest.mark.timeout(5)
def test_12310():
    assert contains_unique_day("October",[('September', 13), ('January', 3)]) == False
