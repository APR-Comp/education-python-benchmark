from wrong_2_359 import *

import pytest
@pytest.mark.timeout(5)
def test_12962():
    assert contains_unique_day("January",[('February', 5), ('February', 12)]) == False
