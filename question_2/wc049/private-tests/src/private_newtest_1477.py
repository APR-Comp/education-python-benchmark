from wrong_correct_2_049 import *

import pytest
@pytest.mark.timeout(5)
def test_1477():
    assert contains_unique_day("June",[('September', 2), ('August', 0)]) == False
