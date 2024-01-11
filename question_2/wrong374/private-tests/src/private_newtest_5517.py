from wrong_2_374 import *

import pytest
@pytest.mark.timeout(5)
def test_5517():
    assert contains_unique_day("May",[('November', 13), ('June', 0)]) == False
