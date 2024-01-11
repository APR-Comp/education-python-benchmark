from wrong_correct_5_022 import *

import pytest
@pytest.mark.timeout(5)
def test_19818():
    assert top_k([31, 4923, 4, 605, 283989],3) == [283989, 4923, 605]
