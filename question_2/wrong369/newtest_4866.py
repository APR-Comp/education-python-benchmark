from wrong_2_369 import *

import pytest
@pytest.mark.timeout(5)
def test_4866():
    assert contains_unique_day("April",[('May', 8), ('June', 15)]) == False
