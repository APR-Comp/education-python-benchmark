from wrong_3_264 import *

import pytest
@pytest.mark.timeout(5)
def test_18094():
    assert remove_extras([738]) == [738]
