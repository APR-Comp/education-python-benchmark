from wrong_2_409 import *

import pytest
@pytest.mark.timeout(5)
def test_4850():
    assert contains_unique_day("October",[('May', 5), ('January', 26)]) == False
