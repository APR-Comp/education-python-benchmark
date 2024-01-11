from wrong_2_364 import *

import pytest
@pytest.mark.timeout(5)
def test_18871():
    assert contains_unique_day("August",[('December', 2), ('June', 6)]) == False
