from src.main import analyze_algorithm
import os

code = """
ALGORITMO Test(n)
    FOR i = 1 TO n DO
        x = x + 1
    ENDFOR
    RETURN x
FIN
"""

with open("temp_test_logs.txt", "w") as f:
    f.write(code)

result = analyze_algorithm("temp_test_logs.txt")
print("Logs:")
for log in result['line_by_line']:
    print(f"Line {log['line']}: {log['cost']}")

if any("OE:" in log['cost'] for log in result['line_by_line']):
    print("\nSUCCESS: OE tag found.")
else:
    print("\nFAILURE: OE tag not found.")
