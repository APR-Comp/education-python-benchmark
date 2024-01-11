from wrong_2_379 import *

import pytest
@pytest.mark.timeout(5)
def test_9564():
    assert contains_unique_day("January",[('December', 24), ('August', 6), ('February', 10)]) == False
