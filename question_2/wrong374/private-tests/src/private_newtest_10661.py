from wrong_2_374 import *

import pytest
@pytest.mark.timeout(5)
def test_10661():
    assert contains_unique_day("October",[('June', 18), ('March', 7), ('October', 17)]) == True
