from wrong_2_419 import *

import pytest
@pytest.mark.timeout(5)
def test_5157():
    assert contains_unique_day("December",[('May', 0), ('December', 17), ('March', 8)]) == True
