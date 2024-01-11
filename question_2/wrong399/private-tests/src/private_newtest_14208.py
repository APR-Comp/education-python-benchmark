from wrong_2_399 import *

import pytest
@pytest.mark.timeout(5)
def test_14208():
    assert contains_unique_day("March",[('November', 20), ('January', 15), ('October', 12)]) == False
