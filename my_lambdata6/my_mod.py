# my_lambdata/my_mod.py

def enlarge(n):
    """[a function which enlarges a number by two orders of magnitude]

    Args:
        n ([int or float]): [any number]

    Returns:
        [int or float]: [n*100]
    """
    return n * 100

# this code breaks our ability to import enlarge from other files, if left in the global scope:
#


if __name__ == "__main__":

    y = int(input("Please choose a number"))
    print(y, enlarge(y))

# if __name__ == "__main__":
#     # only run the code below IF this script is invoked from the command-line

#     y = int(input("Please choose a number"))
#     print(y, enlarge(y))
