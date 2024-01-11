from wrong_2_414 import *

import pytest
@pytest.mark.timeout(5)
def test_10461():
    assert contains_unique_day("June",[('November', 3), ('January', 6), ('May', 6)]) == False
