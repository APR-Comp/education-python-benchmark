from wrong_2_414 import *

import pytest
@pytest.mark.timeout(5)
def test_843():
    assert contains_unique_day("November",[('September', 1), ('August', 9)]) == False
