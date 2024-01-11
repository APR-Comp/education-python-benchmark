from wrong_2_354 import *

import pytest
@pytest.mark.timeout(5)
def test_798():
    assert contains_unique_day("September",[('August', 4), ('May', 9), ('December', 7)]) == False
