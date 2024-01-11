from wrong_2_434 import *

import pytest
@pytest.mark.timeout(5)
def test_5520():
    assert contains_unique_day("November",[('February', 16), ('October', 13)]) == False
