from wrong_2_384 import *

import pytest
@pytest.mark.timeout(5)
def test_18578():
    assert contains_unique_day("June",[('December', 1), ('July', 1), ('December', 6)]) == False
