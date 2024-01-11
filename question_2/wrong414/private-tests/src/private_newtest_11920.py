from wrong_2_414 import *

import pytest
@pytest.mark.timeout(5)
def test_11920():
    assert contains_unique_day("December",[('January', 21), ('April', 1), ('June', 1)]) == False
