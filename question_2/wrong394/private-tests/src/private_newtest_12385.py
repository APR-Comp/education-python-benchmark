from wrong_2_394 import *

import pytest
@pytest.mark.timeout(5)
def test_12385():
    assert contains_unique_day("July",[('November', 15), ('July', 13), ('June', 2), ('February', 3), ('January', 8)]) == True