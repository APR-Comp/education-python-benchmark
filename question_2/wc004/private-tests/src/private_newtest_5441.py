from wrong_correct_2_004 import *

import pytest
@pytest.mark.timeout(5)
def test_5441():
    assert contains_unique_day("September",[('February', 16), ('June', 13)]) == False