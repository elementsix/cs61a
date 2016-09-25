## Extra Linked Lists and Sets ##

from lab08 import *

# Set Practice

def add_up(n, lst):
    """Returns True if any two non identical elements in lst add up to any n.

    >>> add_up(100, [1, 2, 3, 4, 5])
    False
    >>> add_up(7, [1, 2, 3, 4, 2])
    True
    >>> add_up(10, [5, 5])
    False
    """
    "*** YOUR CODE HERE ***"

    lst = set(lst)

    while lst:
        a = lst.pop()
        if (n-a in lst):
            return True

    return False

def pow(n,k):
    """Computes n^k.

    >>> pow(2, 3)
    8
    >>> pow(4, 2)
    16
    """
    "*** YOUR CODE HERE ***"

    if k == 1:
        return n
    elif k%2 == 0:
        return pow(n*n, k//2)
    else:
        return n * pow(n, k-1)

def missing_no(lst):
    """lst contains all the numbers from 1 to n for some n except some
    number k. Find k.

    >>> missing_no([1, 0, 4, 5, 7, 9, 2, 6, 3])
    8
    >>> missing_no(list(filter(lambda x: x != 293, list(range(2000)))))
    293
    """
    "*** YOUR CODE HERE ***"

    numbers = set()
    count = 0

    for element in lst:
        numbers.add(element)
        count += 1

    full = set(list(range(count+1)))

    return list(set(full) - set(numbers))[0]



def find_duplicates_k(k, lst):
    """Returns True if there are any duplicates in lst that are within k
    indices apart.

    >>> find_duplicates_k(3, [1, 2, 3, 4, 1])
    False
    >>> find_duplicates_k(4, [1, 2, 3, 4, 1])
    True
    """
    "*** YOUR CODE HERE ***"

    prev_set = set()
    for i, elem in enumerate(lst):
        if elem in prev_set:
            return True
        prev_set.add(elem)
        if i - k >= 0:
            prev_set.remove(lst[i - k])
    return False


def find_duplicates_k_l(k, l, lst):
    """Returns True if there are any two values who in lst that are within k
    indices apart AND if the absolute value of their difference is less than
    or equal to l.

    >>> find_duplicates_k_l(4, 0, [1, 2, 3, 4, 5])
    False
    >>> find_duplicates_k_l(4, 1, [1, 2, 3, 4, 5])
    True
    >>> find_duplicates_k_l(4, 0, [1, 2, 3, 4, 1])
    True
    >>> find_duplicates_k_l(2, 0, [1, 2, 3, 4, 1])
    False
    >>> find_duplicates_k_l(1, 100, [100, 275, 320, 988, 27])
    True
    >>> find_duplicates_k_l(1, 100, [100, 199, 275, 320, 988, 27])
    True
    >>> find_duplicates_k_l(1, 100, [100, 23, 199, 275, 320, 988, 27])
    True
    >>> find_duplicates_k_l(2, 100, [100, 23, 199, 275, 320, 988, 27])
    True
    """
