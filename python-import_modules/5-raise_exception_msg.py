def raise_exception_msg(message=""):
    raise NameError(message)

try:
    raise_exception_msg("This is a custom exception message")
except NameError as e:
    print("Caught exception:", e)

print("C is fun")
