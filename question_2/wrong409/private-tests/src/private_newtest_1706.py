from wrong_2_409 import *

import pytest
@pytest.mark.timeout(5)
def test_1706():
    assert contains_unique_day("January",[('June', 28), ('December', 4)]) == False
