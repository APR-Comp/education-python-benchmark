from wrong_2_369 import *

import pytest
@pytest.mark.timeout(5)
def test_1714():
    assert contains_unique_day("September",[('January', 2), ('July', 4)]) == False
