from wrong_2_394 import *

import pytest
@pytest.mark.timeout(5)
def test_18100():
    assert contains_unique_day("November",[('March', 5), ('July', 4), ('March', 22), ('July', 22), ('January', 3)]) == False
