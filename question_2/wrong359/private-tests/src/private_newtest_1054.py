from wrong_2_359 import *

import pytest
@pytest.mark.timeout(5)
def test_1054():
    assert contains_unique_day("November",[('January', 22), ('June', 8)]) == False
