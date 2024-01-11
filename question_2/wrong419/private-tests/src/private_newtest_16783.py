from wrong_2_419 import *

import pytest
@pytest.mark.timeout(5)
def test_16783():
    assert contains_unique_day("April",[('May', 15), ('January', 3), ('July', 4)]) == False
