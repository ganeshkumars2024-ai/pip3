import sys

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def run_tests():
    print("--- Running Application Tests ---")
    
    # Test Addition
    assert add(2, 3) == 5, "Addition test failed"
    print("✓ Addition test passed")
    
    # Test Multiplication
    assert multiply(3, 4) == 12, "Multiplication test failed"
    print("✓ Multiplication test passed")
    
    print("--- All tests completed successfully ---")

if __name__ == "__main__":
    print("Starting Python Application...")
    run_tests()
    sys.exit(0)