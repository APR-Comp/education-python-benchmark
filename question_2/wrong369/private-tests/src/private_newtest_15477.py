from wrong_2_369 import *

import pytest
@pytest.mark.timeout(5)
def test_15477():
    assert contains_unique_day("April",[('January', 19), ('November', 9)]) == False
