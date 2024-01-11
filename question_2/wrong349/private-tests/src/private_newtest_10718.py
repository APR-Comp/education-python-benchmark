from wrong_2_349 import *

import pytest
@pytest.mark.timeout(5)
def test_10718():
    assert contains_unique_day("May",[('August', 4), ('July', 8), ('May', 8), ('November', 28), ('July', 3), ('April', 6), ('April', 2), ('May', 2)]) == False
