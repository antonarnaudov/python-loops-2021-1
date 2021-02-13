"""
    function name -> is_empty
    first parameter -> my_set
"""


def is_empty(my_set):
    # if list is empty -> return false
    if not my_set:
        return True
    return False
    # return false


def is_empty1(my_set):
    return True if not my_set else False

#
# print(is_empty([]))
# print(is_empty([1, 2]))
