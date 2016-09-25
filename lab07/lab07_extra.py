## Extra Recursive Objects ##

from lab07 import *

# Linked List Practice

def list_to_link(lst):
    """Takes a Python list and returns a Link with the same elements.

    >>> list_to_link([1, 2, 3])
    Link(1, Link(2, Link(3)))
    """
    "*** YOUR CODE HERE ***"

    if not lst:
        return Link.empty

    link = Link(lst[0])
    link.rest = list_to_link(lst[1:])

    return link


def link_to_list(link):
    """Takes a Link and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> link_to_list(link)
    [1, 2, 3, 4]
    >>> link_to_list(Link.empty)
    []
    """
    "*** YOUR CODE HERE ***"
    lst = []

    while link is not Link.empty:
        lst.append(link.first)
        link = link.rest

    return lst

def reverse(link):
    """Returns a Link that is the reverse of the original.

    >>> reverse(Link(1))
    Link(1)
    >>> link = Link(1, Link(2, Link(3)))
    >>> reverse(link)
    Link(3, Link(2, Link(1)))
    >>> link
    Link(1, Link(2, Link(3)))
    """
    "*** YOUR CODE HERE ***"

    new = Link(link.first)
    copy = link.rest

    while copy is not Link.empty:
        new = Link(copy.first, new)
        copy = copy.rest

    return new


def mutate_reverse(link):
    """Mutates the Link so that its elements are reversed.

    >>> link = Link(1)
    >>> mutate_reverse(link)
    >>> link
    Link(1)

    >>> link = Link(1, Link(2, Link(3)))
    >>> mutate_reverse(link)
    >>> link
    Link(3, Link(2, Link(1)))
    """
    "*** YOUR CODE HERE ***"

    if not link or not link.rest:
        return

    mutate_reverse(link.rest)

    while link.rest is not Link.empty:
        link.first, link.rest.first = link.rest.first, link.first
        link = link.rest



# Tree Practice

def leaves(t):
    """Returns a list of all the entries of the leaf nodes of the Tree t.

    >>> leaves(Tree(1))
    [1]
    >>> leaves(Tree(1, [Tree(2, [Tree(3)]), Tree(4)]))
    [3, 4]
    """
    "*** YOUR CODE HERE ***"

    if t.is_leaf():
        return [t.entry]
    else:
        l = sum([leaves(b) for b in t.branches], [])
        return l


def cumulative_sum(t):
    """Return a new Tree, where each entry is the sum of all entries in the
    corresponding subtree of t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative = cumulative_sum(t)
    >>> t
    Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative
    Tree(16, [Tree(8, [Tree(5)]), Tree(7)])
    >>> cumulative_sum(Tree(1))
    Tree(1)
    """
    "*** YOUR CODE HERE ***"

    if not t or t.is_leaf():
        return t

    else:
        cumulative_branches = [cumulative_sum(b) for b in t.branches]
        cumulative_entry = sum([cb.entry for cb in cumulative_branches]) + t.entry
        cumulative_tree = Tree(cumulative_entry, cumulative_branches)
        return cumulative_tree



def same_shape(t1, t2):
    """Returns whether two Trees t1, t2 have the same shape. Two trees have the
    same shape if they have the same number of branches and each of their
    children have the same shape.

    >>> t, s = Tree(1), Tree(3)
    >>> same_shape(t, t)
    True
    >>> same_shape(t, s)
    True
    >>> t = Tree(1, [Tree(2), Tree(3)])
    >>> same_shape(t, s)
    False
    >>> s = cumulative_sum(t)
    >>> same_shape(t, s)
    True
    """
    "*** YOUR CODE HERE ***"

    return len(t1.branches) == len(t2.branches) and \
        all(same_shape(st1, st2) for st1, st2 in zip(t1.branches, t2.branches))



# Folding Linked Lists

from operator import add, sub, mul

def foldl(link, fn, z):
    """ Left fold
    >>> lst = Link(3, Link(2, Link(1)))
    >>> foldl(lst, sub, 0) # (((0 - 3) - 2) - 1)
    -6
    >>> foldl(lst, add, 0) # (((0 + 3) + 2) + 1)
    6
    >>> foldl(lst, mul, 1) # (((1 * 3) * 2) * 1)
    6
    """
    if link is Link.empty:
        return z
    "*** YOUR CODE HERE ***"
    return foldl(link.rest, fn, fn(z, link.first))

def foldr(link, fn, z):
    """ Right fold
    >>> lst = Link(3, Link(2, Link(1)))
    >>> foldr(lst, sub, 0) # (3 - (2 - (1 - 0)))
    2
    >>> foldr(lst, add, 0) # (3 + (2 + (1 + 0)))
    6
    >>> foldr(lst, mul, 1) # (3 * (2 * (1 * 1)))
    6
    """
    "*** YOUR CODE HERE ***"
    if link is Link.empty:
        return z
    "*** YOUR CODE HERE ***"
    return foldr(link.rest, fn, fn(link.first, z))

identity = lambda x: x

def foldl2(link, fn, z):
    """ Write foldl using foldr
    >>> list = Link(3, Link(2, Link(1)))
    >>> foldl2(list, sub, 0) # (((0 - 3) - 2) - 1)
    -6
    >>> foldl2(list, add, 0) # (((0 + 3) + 2) + 1)
    6
    >>> foldl2(list, mul, 1) # (((1 * 3) * 2) * 1)
    6
    """
    def step(x, g):
        "*** YOUR CODE HERE ***"
        return lambda a: g(fn(a, x))    # Didn't get this
    return foldr(link, step, identity)(z)

