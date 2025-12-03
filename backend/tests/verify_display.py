from src.main import analyze_algorithm
res = analyze_algorithm('tests/FIBONACCI_USER.txt')
print(f"RESULT: {res.get('complexity_calculated')}")
