from wrong_2_419 import *

import pytest
@pytest.mark.timeout(5)
def test_13646():
    assert contains_unique_day("June",[('February', 14), ('February', 6), ('January', 4)]) == False
