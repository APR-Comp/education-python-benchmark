from wrong_2_354 import *

import pytest
@pytest.mark.timeout(5)
def test_7441():
    assert contains_unique_day("January",[('May', 9), ('March', 27), ('September', 15), ('August', 18), ('July', 7)]) == False
