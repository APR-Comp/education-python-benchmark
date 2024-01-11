from wrong_2_379 import *

import pytest
@pytest.mark.timeout(5)
def test_1801():
    assert contains_unique_day("April",[('May', 30), ('October', 4), ('November', 7), ('November', 11), ('August', 0)]) == False
