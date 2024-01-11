from wrong_2_419 import *

import pytest
@pytest.mark.timeout(5)
def test_7359():
    assert contains_unique_day("June",[('April', 15), ('April', 7)]) == False
