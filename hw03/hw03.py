from functools import lru_cache
memoize = lru_cache(None)

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    "*** YOUR CODE HERE ***"

    if n <= 3:
        return n
    else:
        return g(n-1) + 2*g(n-2) + 3*g(n-3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    "*** YOUR CODE HERE ***"


def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    "*** YOUR CODE HERE ***"
    if k == 0:
        return False

    if k % 10 == 7:
        return True
    else:
        return has_seven(k//10)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
    "*** YOUR CODE HERE ***"

    # Iterative
    # k = 1
    # pingpong_val = 1
    # direction = "increment"
    #
    # while k != n:
    #
    #     if k % 7 == 0 or has_seven(k):
    #         if direction == "increment":
    #             direction = "decrement"
    #         else:
    #             direction = "increment"
    #
    #     if direction == "increment":
    #         pingpong_val += 1
    #     else:
    #         pingpong_val -= 1
    #
    #     k += 1
    #
    # return pingpong_val

    # Recursive
    def pingpong_seq(k, val, direction):
        if k == n:
            return val

        if k%7 == 0 or has_seven(k):
            if direction == "increment":
                direction = "decrement"
            else:
                direction = "increment"

        if direction == "increment":
            return pingpong_seq(k+1, val+1, "increment")
        else:
            return pingpong_seq(k+1, val-1, "decrement")

    return pingpong_seq(1, 1, "increment")


@memoize
def count_partitions(m, n):
    if m == 1 or n == 1:    # 8, 1 / 1, 8
        return 1            # cases of 0, n are justified being counted here as they represent counting a power of 2
                            # in terms of itself

    # n is always > 0
    elif m < 0:
        return 0

    else:
        denominations = [2 ** x for x in range(get_denominations(n))]
        return sum([count_partitions(m - n, n) for n in denominations])


def get_denominations(n):
    if n == 1:
        return 1
    else:
        return get_denominations(n // 2) + 1


def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"

    if amount == 0:
        return 0
    else:

        # The logic behind this is, we take out one valid denomination and
        # then figure out the possible combinations for the leftover amount
        # in terms of the valid denominations upto it.
        # When we hit a 1 or 0, we've hit a valid combination and we increment
        # the count by 1

        denominations = [2 ** x for x in range(get_denominations(amount))]
        return sum([count_partitions(amount - n, n) for n in denominations])



def towers_of_hanoi(n, start, end):
    """Print the moves required to solve the towers of hanoi game, starting
    with n disks on the start pole and finishing on the end pole.

    The game is to assumed to have 3 poles.

    >>> towers_of_hanoi(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> towers_of_hanoi(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> towers_of_hanoi(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 0 < start <= 3 and 0 < end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"

    if n == 1:
        print("Move the top disk from rod {0} to rod {1}".format(start, end))
        return

    intermediate = 6 - (start + end)
    towers_of_hanoi(n-1, start, intermediate)
    towers_of_hanoi(1, start, end)
    towers_of_hanoi(n-1, intermediate, end)


from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    """
    # return (lambda a, b: a(a, b))(lambda a, b: b*a(a, b-1) if b > 0 else 1, b)

    # Fixed point combinator concept. Very difficult
    return (lambda f: lambda k: f(f, k))(lambda f, k: k * f(f, k - 1) if k > 0 else 1)