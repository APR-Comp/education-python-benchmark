from wrong_2_379 import *

import pytest
@pytest.mark.timeout(5)
def test_4132():
    assert contains_unique_day("September",[('March', 3), ('August', 6)]) == False
