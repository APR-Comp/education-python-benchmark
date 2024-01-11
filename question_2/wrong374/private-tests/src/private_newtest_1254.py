from wrong_2_374 import *

import pytest
@pytest.mark.timeout(5)
def test_1254():
    assert contains_unique_day("October",[('October', 15), ('September', 5)]) == True
