import pytest
from src.tda_viz import TDAVisualizer  # Assume exists

def test_tda_visualization():
    viz = TDAVisualizer()
    data = [[1,2],[3,4]]
    result = viz.visualize(data)
    assert 'betti' in result
