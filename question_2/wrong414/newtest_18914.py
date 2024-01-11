from wrong_2_414 import *

import pytest
@pytest.mark.timeout(5)
def test_18914():
    assert contains_unique_day("July",[('January', 1), ('November', 9)]) == False
