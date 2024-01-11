from wrong_correct_2_040 import *

import pytest
@pytest.mark.timeout(5)
def test_14268():
    assert contains_unique_day("May",[('June', 7), ('August', 12)]) == False
