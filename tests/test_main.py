import pytest
import os
from importlib import reload
from src.core_logic import calculate_supremacy
import src.config # Import config directly to reload it

def test_calculate_supremacy():
    """
    Verifies the deterministic nature of the supremacy calculation.
    """
    assert calculate_supremacy(base_value=100) == 10000
    assert calculate_supremacy(base_value=5) == 500

def test_calculate_supremacy_invalid_input():
    """
    Verifies that calculate_supremacy raises ValueError for invalid inputs.
    """
    with pytest.raises(ValueError, match="base_value must be a non-negative integer."):
        calculate_supremacy(base_value=-1)
    with pytest.raises(ValueError, match="base_value must be a non-negative integer."):
        calculate_supremacy(base_value=10.5)
    with pytest.raises(ValueError, match="base_value must be a non-negative integer."):
        calculate_supremacy(base_value="abc")

def test_calculate_supremacy_with_env_variable():
    """
    Verifies that SUPREMACY_MULTIPLIER can be overridden by an environment variable.
    """
    # Store original value and ensure config is reloaded to get default if env var not set
    reload(src.config)
    original_multiplier = src.config.SUPREMACY_MULTIPLIER
    
    os.environ["AXIOM_SUPREMACY_MULTIPLIER"] = "200"
    reload(src.config) # Reload config to pick up new env var
    
    assert src.config.SUPREMACY_MULTIPLIER == 200
    assert calculate_supremacy(base_value=10) == 2000
    
    del os.environ["AXIOM_SUPREMACY_MULTIPLIER"]
    reload(src.config) # Reload again to revert to default
    assert src.config.SUPREMACY_MULTIPLIER == original_multiplier
