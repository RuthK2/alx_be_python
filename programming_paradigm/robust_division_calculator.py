def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
        result = num / den
        return f"Result: {result}"
    
    except ZeroDivisionError:
       print("Error:Cannot divide by zero.")
    except ValueError:
       print("Error:Please enter numeric values only.")


    