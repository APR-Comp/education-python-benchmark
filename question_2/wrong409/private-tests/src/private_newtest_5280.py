from wrong_2_409 import *

import pytest
@pytest.mark.timeout(5)
def test_5280():
    assert contains_unique_day("June",[('November', 1), ('October', 17)]) == False
