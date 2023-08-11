import sys

def main():
    args = sys.argv[1:] 

    num_args = len(args)
    arg_plural = "argument" if num_args == 1 else "arguments"

    print("{} {}:".format(num_args, arg_plural))
    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))

if __name__ == "__main__":
    main()
