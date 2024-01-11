from wrong_correct_2_031 import *

import pytest
@pytest.mark.timeout(5)
def test_17007():
    assert contains_unique_day("January",[('July', 8), ('August', 29)]) == False
