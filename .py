import traceback
import sys

# Error solution database (extendable)
ERROR_SOLUTIONS = {
    "ZeroDivisionError": "You tried to divide by zero. Check your denominator and ensure it's not zero.",
    "FileNotFoundError": "The file you're trying to access does not exist. Verify the file path and name.",
    "KeyError": "The key you're looking for doesn't exist in the dictionary. Check your key names or use 'dict.get(key)' to avoid errors.",
    "IndexError": "The index you're trying to access is out of range. Ensure your index is within the length of the list.",
    "TypeError": "There might be a mismatch in data types. Double-check the types of variables you're working with.",
    "ValueError": "The function received an argument of the correct type but inappropriate value. Validate the input values.",
}

def debugging_companion(func):
    """
    Decorator to wrap around functions for error monitoring and debugging assistance.
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            error_type = type(e).__name__
            print(f"\n🚨 Error Detected: {error_type}")
            print("Traceback:")
            traceback.print_exc()
            solution = ERROR_SOLUTIONS.get(error_type, "No solution found for this error.")
            print(f"\n💡 Suggested Fix: {solution}")
            if solution == "No solution found for this error.":
                print("🔗 Visit https://stackoverflow.com/ for further troubleshooting.")
            return None
    return wrapper

# Example function to demonstrate the debugging companion
@debugging_companion
def buggy_function():
    # Intentionally causing an error
    # Uncomment lines one by one to test different errors
    # x = 1 / 0  # ZeroDivisionError
    # open("non_existent_file.txt")  # FileNotFoundError
    # data = {"key": "value"}
    # print(data["nonexistent_key"])  # KeyError
    numbers = [1, 2, 3]
    print(numbers[5])  # IndexError

if __name__ == "__main__":
    print("Running the Debugging Companion Demo:")
    buggy_function()
