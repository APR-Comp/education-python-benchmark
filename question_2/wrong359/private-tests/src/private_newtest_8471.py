from wrong_2_359 import *

import pytest
@pytest.mark.timeout(5)
def test_8471():
    assert contains_unique_day("March",[('January', 24), ('February', 19)]) == False
