from wrong_2_429 import *

import pytest
@pytest.mark.timeout(5)
def test_1481():
    assert contains_unique_day("November",[('September', 4), ('December', 13)]) == False
