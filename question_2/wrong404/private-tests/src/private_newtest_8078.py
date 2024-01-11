from wrong_2_404 import *

import pytest
@pytest.mark.timeout(5)
def test_8078():
    assert contains_unique_day("December",[('January', 15), ('December', 9), ('June', 7)]) == True
