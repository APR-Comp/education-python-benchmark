from wrong_2_424 import *

import pytest
@pytest.mark.timeout(5)
def test_11042():
    assert contains_unique_day("January",[('January', 4), ('February', 20), ('December', 5), ('August', 22), ('October', 7), ('June', 4), ('May', 2)]) == False
