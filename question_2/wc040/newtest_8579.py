from wrong_correct_2_040 import *

import pytest
@pytest.mark.timeout(5)
def test_8579():
    assert contains_unique_day("April",[('November', 4), ('August', 13)]) == False
