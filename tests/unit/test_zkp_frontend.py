import pytest
from src.arc_integration import ZKPAttest

def test_zkp_frontend():
    zkp = ZKPAttest()
    assert zkp is not None
