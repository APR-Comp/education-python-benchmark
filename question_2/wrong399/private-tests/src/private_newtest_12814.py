from wrong_2_399 import *

import pytest
@pytest.mark.timeout(5)
def test_12814():
    assert contains_unique_day("January",[('November', 6), ('July', 11), ('January', 3)]) == True
