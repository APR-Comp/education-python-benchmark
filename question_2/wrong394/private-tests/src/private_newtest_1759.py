from wrong_2_394 import *

import pytest
@pytest.mark.timeout(5)
def test_1759():
    assert contains_unique_day("April",[('December', 7), ('November', 4)]) == False
