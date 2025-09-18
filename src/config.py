# Configuration for the Axiom Void project.
# This module centralizes configurable parameters for deterministic operations.

import os

# SUPREMACY_MULTIPLIER can be overridden by an environment variable
SUPREMACY_MULTIPLIER = int(os.getenv("AXIOM_SUPREMACY_MULTIPLIER", "100"))
