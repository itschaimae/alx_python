def is_same_class(obj, a_class):
    return type(obj) == a_class

# Test cases
if is_same_class(1, int):
    print("1 is an instance of the class int")
if is_same_class(1, float):
    print("1 is an instance of the class float")
if is_same_class(1, object):
    print("1 is an instance of the class object")

