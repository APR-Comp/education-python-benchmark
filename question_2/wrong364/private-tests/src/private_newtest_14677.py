from wrong_2_364 import *

import pytest
@pytest.mark.timeout(5)
def test_14677():
    assert contains_unique_day("August",[('June', 23), ('July', 12)]) == False
