from wrong_2_419 import *

import pytest
@pytest.mark.timeout(5)
def test_13658():
    assert contains_unique_day("July",[('January', 27), ('October', 2), ('May', 4)]) == False
