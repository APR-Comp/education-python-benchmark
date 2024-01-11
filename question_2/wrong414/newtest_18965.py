from wrong_2_414 import *

import pytest
@pytest.mark.timeout(5)
def test_18965():
    assert contains_unique_day("November",[('June', 9), ('March', 24)]) == False
