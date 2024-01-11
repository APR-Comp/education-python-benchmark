from wrong_correct_2_040 import *

import pytest
@pytest.mark.timeout(5)
def test_2348():
    assert contains_unique_day("March",[('July', 1), ('August', 3), ('September', 5), ('July', 18)]) == False
