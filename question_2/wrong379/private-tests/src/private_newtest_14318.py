from wrong_2_379 import *

import pytest
@pytest.mark.timeout(5)
def test_14318():
    assert contains_unique_day("December",[('February', 4), ('May', 2), ('November', 7)]) == False
