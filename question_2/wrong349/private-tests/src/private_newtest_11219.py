from wrong_2_349 import *

import pytest
@pytest.mark.timeout(5)
def test_11219():
    assert contains_unique_day("April",[('December', 7), ('February', 10), ('April', 6), ('May', 19), ('October', 6), ('February', 3), ('November', 9), ('July', 2), ('November', 3)]) == False
