from wrong_2_429 import *

import pytest
@pytest.mark.timeout(5)
def test_5913():
    assert contains_unique_day("April",[('October', 1), ('November', 6), ('December', 7)]) == False
