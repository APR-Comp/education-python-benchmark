from wrong_correct_2_031 import *

import pytest
@pytest.mark.timeout(5)
def test_17216():
    assert contains_unique_day("January",[('October', 30), ('November', 3)]) == False
