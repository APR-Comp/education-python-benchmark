from wrong_2_394 import *

import pytest
@pytest.mark.timeout(5)
def test_15981():
    assert contains_unique_day("September",[('February', 4), ('December', 10)]) == False
