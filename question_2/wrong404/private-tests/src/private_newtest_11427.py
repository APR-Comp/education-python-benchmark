from wrong_2_404 import *

import pytest
@pytest.mark.timeout(5)
def test_11427():
    assert contains_unique_day("January",[('October', 5), ('September', 1)]) == False
