from wrong_correct_2_058 import *

import pytest
@pytest.mark.timeout(5)
def test_9436():
    assert contains_unique_day("April",[('June', 3), ('July', 9)]) == False
