import pytest
import json
from src.arc_integration import ARCSolver

@pytest.fixture
def mock_zkp():
    class MockZKP:
        def sign_grids(self, grids):
            return [grid for grid in grids]
    return MockZKP()

def test_solve_task(mock_zkp, monkeypatch):
    monkeypatch.setattr('src.arc_integration.ZKPAttest', lambda: mock_zkp)
    solver = ARCSolver()
    task = {'input': [[0,1],[1,0]]}
    pred = solver.solve_task(task)
    assert 'attempt_1' in pred and 'attempt_2' in pred
    assert len(pred['attempt_1']) == 2 and len(pred['attempt_2']) == 2
    assert json.dumps(pred)  # Serializable
