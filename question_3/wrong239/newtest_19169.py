from wrong_3_239 import *

import pytest
@pytest.mark.timeout(5)
def test_19169():
    assert remove_extras([93]) == [93]
