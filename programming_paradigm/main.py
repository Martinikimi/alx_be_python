<<<<<<< HEAD
@"
import sys
from robust_division_calculator import safe_divide
=======
import sys

def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        return f"Error: Cannot divide by zero."
>>>>>>> 35403f06c49c05279a6c386022c9c5890a69303b

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
<<<<<<< HEAD
        sys.exit(1)
    numerator = sys.argv[1]
    denominator = sys.argv[2]
    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
"@ | Set-Content main.py
=======
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
>>>>>>> 35403f06c49c05279a6c386022c9c5890a69303b
