from wrong_2_399 import *

import pytest
@pytest.mark.timeout(5)
def test_9775():
    assert contains_unique_day("April",[('December', 6), ('April', 6)]) == False
