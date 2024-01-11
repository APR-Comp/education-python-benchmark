from wrong_2_374 import *

import pytest
@pytest.mark.timeout(5)
def test_14905():
    assert contains_unique_day("November",[('July', 1), ('July', 17)]) == False
