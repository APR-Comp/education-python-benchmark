from wrong_correct_2_031 import *

import pytest
@pytest.mark.timeout(5)
def test_17347():
    assert contains_unique_day("December",[('August', 8), ('November', 5)]) == False
