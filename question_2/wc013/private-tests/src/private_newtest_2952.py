from wrong_correct_2_013 import *

import pytest
@pytest.mark.timeout(5)
def test_2952():
    assert contains_unique_day("January",[('October', 29), ('February', 9), ('February', 16)]) == False
