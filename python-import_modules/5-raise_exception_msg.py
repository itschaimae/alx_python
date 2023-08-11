def raise_exception_msg(message=""):
    raise NameError(message)

# Example usage
try:
    raise_exception_msg("This is a custom exception message")
except NameError as e:
    print("Caught exception:", e)
