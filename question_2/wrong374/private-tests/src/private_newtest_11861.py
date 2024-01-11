from wrong_2_374 import *

import pytest
@pytest.mark.timeout(5)
def test_11861():
    assert contains_unique_day("September",[('November', 22), ('March', 26)]) == False
