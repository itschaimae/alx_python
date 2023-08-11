import sys

args = sys.argv[1:] 

num_args = len(args)
arg_plural = "argument" if num_args == 1 else "arguments"

print("Number of {}{}:{}".format(" " if num_args > 0 else "", arg_plural, "." if num_args == 0 else ""))
for i, arg in enumerate(args, start=1):
    print("{}: {}".format(i, arg))
