import pytest
from src.arc_integration import ZKPAttest

def test_zkp_sign():
    zkp = ZKPAttest()
    grids = [[[0,1],[1,0]]]
    signed = zkp.sign_grids(grids)
    assert len(signed) == 1
