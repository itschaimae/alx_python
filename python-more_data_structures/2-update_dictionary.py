def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value

def print_sorted_dictionary(my_dict):
    """ Print sorted dictionary """
    keys = sorted(my_dict.keys())
    for k in keys:
        print("{}: {}".format(k, my_dict[k]))



