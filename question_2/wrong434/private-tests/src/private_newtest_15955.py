from wrong_2_434 import *

import pytest
@pytest.mark.timeout(5)
def test_15955():
    assert contains_unique_day("December",[('March', 7), ('March', 8), ('November', 6), ('February', 2), ('February', 12), ('March', 18)]) == False
