from wrong_correct_2_004 import *

import pytest
@pytest.mark.timeout(5)
def test_10071():
    assert contains_unique_day("April",[('November', 15), ('November', 18), ('March', 8)]) == False
