from wrong_2_354 import *

import pytest
@pytest.mark.timeout(5)
def test_17180():
    assert contains_unique_day("February",[('May', 14), ('September', 7)]) == False