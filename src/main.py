# Genesis state: 0xDEADBEEF
# H(M)=0 locked.

import logging
from src.core_logic import calculate_supremacy

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    """
    Main function to initiate the void engine.
    """
    logger.info("Void engine initiated. Supremacy awaits.")
    try:
        initial_supremacy = calculate_supremacy(base_value=165) # Corresponds to $165M ARR
        logger.info(f"Initial Supremacy Value Calculated: {initial_supremacy}")
    except ValueError as e:
        logger.error(f"Error calculating initial supremacy: {e}")

if __name__ == "__main__":
    main()
