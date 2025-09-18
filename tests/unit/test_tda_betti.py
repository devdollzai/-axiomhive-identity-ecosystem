import pytest
from src.tda_viz import TDAVisualizer

def test_tda_betti():
    viz = TDAVisualizer()
    result = viz.compute_betti([[1,2],[3,4]])
    assert 'betti_0' in result
