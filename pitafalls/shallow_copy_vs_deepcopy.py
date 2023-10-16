import copy

a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]


def assignment():
    """
    Normal assignment operations will simply point the new variable towards the existing object.
    """
    d = c
    assert id(d) == id(c)  # True - d is the same object as c
    assert id(d[0]) == id(c[0])  # True - d[0] is the same object as c[0]


def shallow_copy():
    """
    A shallow copy constructs a new compound object and then (to the extent possible)
    inserts references into it to the objects found in the original.
    """
    d = copy.copy(c)
    assert id(c) != id(d)  # False - d is now a new object
    assert id(c[0]) == id(d[0])  # True - d[0] is the same object as c[0]


def deep_copy():
    """
    A deep copy constructs a new compound object and then,
    recursively, inserts copies into it of the objects found in the original.
    """
    d = copy.deepcopy(c)
    assert id(c) != id(d)  # False - d is now a new object
    assert id(c[0]) != id(d[0])  # False - d[0] is now a new object


if __name__ == '__main__':
    assignment()
    shallow_copy()
    deep_copy()

