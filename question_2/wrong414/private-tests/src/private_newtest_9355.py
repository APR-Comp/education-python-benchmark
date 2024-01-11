from wrong_2_414 import *

import pytest
@pytest.mark.timeout(5)
def test_9355():
    assert contains_unique_day("August",[('April', 3), ('July', 5)]) == False
