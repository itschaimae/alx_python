def raise_exception_msg(message=""):
    raise NameError(message)

raise_exception_msg = __import__('5-raise_exception_msg').raise_exception_msg

try:
    raise_exception_msg("This is a custom exception message")
except NameError as ne:
    print("Caught exception:", ne)

print("C is fun")
