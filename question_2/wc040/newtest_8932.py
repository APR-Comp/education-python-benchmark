from wrong_correct_2_040 import *

import pytest
@pytest.mark.timeout(5)
def test_8932():
    assert contains_unique_day("June",[('November', 1), ('August', 1)]) == False