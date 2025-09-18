import pytest
from src.arc_integration import ARCSolver

def test_arc_zkp_integration():
    solver = ARCSolver()
    assert solver is not None
