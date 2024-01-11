from wrong_2_434 import *

import pytest
@pytest.mark.timeout(5)
def test_9774():
    assert contains_unique_day("February",[('October', 7), ('March', 29), ('June', 28), ('January', 2), ('October', 4)]) == False
