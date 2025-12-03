
import sys
import os

# Add root to path
sys.path.append(os.getcwd())

try:
    from src.analysis.CostCalculator import CostCalculator
    print("Import successful")
except Exception as e:
    print(f"Import failed: {e}")
    import traceback
    traceback.print_exc()