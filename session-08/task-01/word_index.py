#!/usr/bin/env python

#
# The One Description:
#
# - Existence of an abstraction to which values can be
# converted. 
# 
# - This abstraction provides operations to (1) wrap
#   around values, so that they become the abstraction; (2) bind
#   itself to functions, so to establish sequences of functions;
#   and (3) unwrap the value, so to examine the final result.
# 
# - Larger problem is solved as a pipeline of functions bound
#   together, with unwrapping happening at the end.
# 
# - Particularly for The One style, the bind operation simply
#   calls the given function, giving it the value that it holds, and holds
#   on to the returned value.
#


# Defining a main method makes testing easier
def main(file_path):
    pass

if __name__ == "__main__":
    main(sys.argv[1])
