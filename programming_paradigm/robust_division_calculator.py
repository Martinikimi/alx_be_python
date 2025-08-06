import sys

def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        return f"Error: Cannot divide by zero."

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        return
    
    try:
        numerator = float(sys.argv[1])
        denominator = float(sys.argv[2])
    except ValueError:
        return f"Error: Please enter numeric values only."
        return

    result = safe_divide(numerator, denominator)
    print("The result of the division is", result)

if __name__ == "__main__":
    main()

