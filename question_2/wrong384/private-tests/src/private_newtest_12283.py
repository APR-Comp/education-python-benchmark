from wrong_2_384 import *

import pytest
@pytest.mark.timeout(5)
def test_12283():
    assert contains_unique_day("February",[('November', 15), ('March', 5)]) == False
