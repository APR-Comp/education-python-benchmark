from wrong_correct_2_058 import *

import pytest
@pytest.mark.timeout(5)
def test_3022():
    assert contains_unique_day("April",[('March', 5), ('January', 17)]) == False
