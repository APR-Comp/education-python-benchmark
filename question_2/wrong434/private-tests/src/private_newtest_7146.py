from wrong_2_434 import *

import pytest
@pytest.mark.timeout(5)
def test_7146():
    assert contains_unique_day("May",[('June', 17), ('November', 6), ('June', 1)]) == False
