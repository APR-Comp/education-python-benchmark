from wrong_correct_2_058 import *

import pytest
@pytest.mark.timeout(5)
def test_1427():
    assert contains_unique_day("April",[('September', 3), ('February', 23)]) == False
