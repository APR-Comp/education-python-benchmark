from wrong_correct_2_040 import *

import pytest
@pytest.mark.timeout(5)
def test_15440():
    assert contains_unique_day("June",[('September', 1), ('April', 9), ('January', 29)]) == False
