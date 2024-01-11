from wrong_2_359 import *

import pytest
@pytest.mark.timeout(5)
def test_5404():
    assert contains_unique_day("May",[('September', 7), ('April', 9), ('April', 14)]) == False
