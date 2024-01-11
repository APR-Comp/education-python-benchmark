from collections import OrderedDict

from wrong_correct_3_031 import *
import pytest
@pytest.mark.timeout(5)
def test_003():
    assert remove_extras([]) == []
