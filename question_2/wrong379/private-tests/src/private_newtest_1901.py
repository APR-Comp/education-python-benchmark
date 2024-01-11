from wrong_2_379 import *

import pytest
@pytest.mark.timeout(5)
def test_1901():
    assert contains_unique_day("August",[('September', 7), ('February', 9), ('August', 4), ('October', 5), ('February', 8)]) == True
