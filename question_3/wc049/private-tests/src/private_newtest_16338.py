from wrong_correct_3_049 import *

import pytest
@pytest.mark.timeout(5)
def test_16338():
    assert remove_extras([6, 9, 280]) == [6, 9, 280]
