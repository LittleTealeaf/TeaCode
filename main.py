import sys

from func import *

i = 0

"""
basic concepts:
    {} -> execute within executes
    (){} -> functions as objects
    {valname} 1 2 3 4 $awef
    first is the storing variable name, everything after is the "stack"
        operators such as  +-*/^%><= use it as a stack
        stacks can be put in a stack, multiplied, etc.
    ! indicates a command
"""

if __name__ == '__main__':
    file = open(sys.argv[1], "r").read().split("\n")
    while i < len(file):
        cmd = file[i].split(" ")
        if len(cmd) == 0 or (len(cmd[0]) > 0 and "#" in cmd[0]):
            print(file[i][1:])
        elif "!" in cmd[0]:
            functions[cmd[0][1:]](cmd)

        i += 1
