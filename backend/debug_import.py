
try:
    from src.analysis.CostCalculator import CostCalculator
    print("Successfully imported CostCalculator")
except Exception as e:
    with open("error.log", "w") as f:
        import traceback
        traceback.print_exc(file=f)
    print("Error logged to error.log")