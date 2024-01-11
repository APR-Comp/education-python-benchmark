from wrong_2_349 import *

import pytest
@pytest.mark.timeout(5)
def test_10910():
    assert contains_unique_day("August",[('August', 22), ('January', 4), ('December', 16)]) == True
