from wrong_2_419 import *

import pytest
@pytest.mark.timeout(5)
def test_15677():
    assert contains_unique_day("December",[('June', 4), ('June', 2)]) == False
