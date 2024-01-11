from wrong_2_379 import *

import pytest
@pytest.mark.timeout(5)
def test_14205():
    assert contains_unique_day("September",[('April', 25), ('November', 2)]) == False
