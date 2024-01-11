from wrong_2_354 import *

import pytest
@pytest.mark.timeout(5)
def test_19460():
    assert contains_unique_day("August",[('January', 22), ('May', 4)]) == False
