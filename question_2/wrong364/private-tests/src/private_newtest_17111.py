from wrong_2_364 import *

import pytest
@pytest.mark.timeout(5)
def test_17111():
    assert contains_unique_day("February",[('July', 8), ('December', 9), ('January', 9)]) == False
