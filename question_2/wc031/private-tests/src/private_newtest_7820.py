from wrong_correct_2_031 import *

import pytest
@pytest.mark.timeout(5)
def test_7820():
    assert contains_unique_day("April",[('February', 1), ('October', 6)]) == False
