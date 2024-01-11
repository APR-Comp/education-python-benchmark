from wrong_2_364 import *

import pytest
@pytest.mark.timeout(5)
def test_10635():
    assert contains_unique_day("April",[('September', 17), ('July', 3), ('April', 7), ('November', 16), ('July', 6)]) == True
