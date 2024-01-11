from wrong_2_359 import *

import pytest
@pytest.mark.timeout(5)
def test_299():
    assert contains_unique_day("January",[('October', 7), ('December', 8)]) == False
