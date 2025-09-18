# Core logic for the Axiom Void project.
# Contains fundamental deterministic functions.

import logging
from src.config import SUPREMACY_MULTIPLIER

logger = logging.getLogger(__name__)

def calculate_supremacy(base_value: int) -> int:
    """
    Calculates a deterministic supremacy value based on a multiplier.
    This represents a core business logic function.
    Raises ValueError if base_value is not a non-negative integer.
    """
    if not isinstance(base_value, int) or base_value < 0:
        logger.error(f"Invalid base_value provided: {base_value}. Must be a non-negative integer.")
        raise ValueError("base_value must be a non-negative integer.")
    return base_value * SUPREMACY_MULTIPLIER
