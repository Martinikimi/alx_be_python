def  safe_divide(numerator, denominator):
    try:
        num=float(numerator)
        deno=float(denominator)
        
        results= numerator/denominator
        return f"Result:{results}"
    
    except ZeroDivisionError:
        return f"Error: Cannot divide by Zero"
    
    except ValueError:
        return "Error: Please enter valid numbers."
