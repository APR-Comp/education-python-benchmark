from wrong_2_379 import *

import pytest
@pytest.mark.timeout(5)
def test_12556():
    assert contains_unique_day("October",[('October', 1), ('May', 16)]) == True
