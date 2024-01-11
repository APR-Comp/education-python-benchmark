from wrong_2_384 import *

import pytest
@pytest.mark.timeout(5)
def test_10262():
    assert contains_unique_day("November",[('July', 4), ('April', 8)]) == False
