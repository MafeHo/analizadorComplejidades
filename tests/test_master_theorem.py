
import sys
import os

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from analysis.MathEngine import MathEngine
from sympy import symbols, sympify

def test_master_theorem():
    engine = MathEngine()
    n = engine.n
    T = engine.T
    
    test_cases = [
        {
            "name": "Binary Search",
            "expr": T(n/2) + 1,
            "expected_case": 2,
            "expected_a": 1,
            "expected_b": 2
        },
        {
            "name": "Merge Sort",
            "expr": 2*T(n/2) + n,
            "expected_case": 2,
            "expected_a": 2,
            "expected_b": 2
        },
        {
            "name": "Case 1 Example",
            "expr": 2*T(n/2) + 1,
            "expected_case": 1,
            "expected_a": 2,
            "expected_b": 2
        },
        {
            "name": "Case 3 Example",
            "expr": T(n/2) + n,
            "expected_case": 3,
            "expected_a": 1,
            "expected_b": 2
        }
    ]
    
    print("Running Master Theorem Tests...")
    print("="*40)
    
    for case in test_cases:
        print(f"Testing: {case['name']}")
        print(f"Expression: {case['expr']}")
        
        result = engine.solve_recurrence(case['expr'])
        
        if isinstance(result, dict):
            details = result.get('details')
            complexity = result.get('complexity')
            
            res_str = engine.format_complexity(complexity)
            # Fix for Windows console encoding
            res_str = res_str.replace('\u0398', 'Theta').replace('\u03a9', 'Omega')
            print(f"Result: {res_str}")
            if details:
                print(f"Details: {details}")
                if details.get('case') == case['expected_case']:
                    print("[PASS] Case Match")
                else:
                    print(f"[FAIL] Case Mismatch: Expected {case['expected_case']}, Got {details.get('case')}")
                
                if details.get('a') == case['expected_a']:
                    print("[PASS] 'a' Match")
                else:
                    print(f"[FAIL] 'a' Mismatch: Expected {case['expected_a']}, Got {details.get('a')}")

                if details.get('b') == case['expected_b']:
                    print("[PASS] 'b' Match")
                else:
                    print(f"[FAIL] 'b' Mismatch: Expected {case['expected_b']}, Got {details.get('b')}")
            else:
                print("[FAIL] No details returned")
        else:
            print(f"❌ Returned expression instead of dict: {result}")
        
        print("-" * 40)

if __name__ == "__main__":
    test_master_theorem()
