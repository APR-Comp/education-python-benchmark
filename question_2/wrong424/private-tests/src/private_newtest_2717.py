from wrong_2_424 import *

import pytest
@pytest.mark.timeout(5)
def test_2717():
    assert contains_unique_day("January",[('July', 3), ('October', 9), ('April', 13)]) == False
