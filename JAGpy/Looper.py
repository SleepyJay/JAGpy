
"""Generic looping"""

from collections import deque

#
def combos(start, stop, size):
    full = map(lambda x: [x], range(start, stop))

    for i in range(0, size - 1):
        full = combo_step(start, stop, full)

    return full


#
def combo_step(start, stop, items):
    my_step = []

    # [ [1,1], [0,1], ...]
    for item in items:
        # [1,1]
        for z in range(start, stop):
            cur = []
            # make copy of existing
            for x in item:
                cur.append(x)
            # add from the range
            cur.append(z)

            my_step.append(cur)

    return my_step


# Turn a number in to a list of "bits" of a given base.
def value_to_list(base, value, size=None):
    my_list = []
    high = base - 1

    it = value
    while it > high:
        res = divmod(it, base)
        it = res[0]
        my_list.append(res[1])

    my_list.append(it)

    if size:
        while len(my_list) < size:
            my_list.append(0)

    my_list.reverse()

    return my_list


#
def list_to_value(base, my_list):
    my_list.reverse()

    val = 0
    mul = 1

    for x in my_list:
        val += (x * mul)
        mul *= base

    return val


def permutations_from_list(ints):
    """Generate permutations of the given list of integers"""
    return _do_permutate_list(ints, False)


def permutations_from_list_rightward(ints):
    """Generate permutations of the given list of integers; rightward tries to build bigger sums first"""
    return _do_permutate_list(ints, True)


def yy_do_permutate_list(ints, rightward=False):
    queue = deque([[]])
    cnt = len(ints)
    while queue:
        if rightward:
            q = queue.pop()
        else:
            q = queue.popleft()

        if len(q):
            k = q[-1]
            j = cnt - len(q)
            m = None
            if j in ints:
                m = ints[j]
            print(f"k: {k}, j: {j}, m: {m}")

        else:
            k = 0

        for i in range(k, cnt):
            print(f"i: {i}")
            x = ints[i]
            cur = []
            cur.extend(q)
            cur.append(x)

            if len(cur) < cnt:
                queue.append(cur)

            yield cur


def _do_permutate_list(ints, rightward=False):
    queue = deque([[]])
    cnt = len(ints)
    while queue:
        if rightward:
            q = queue.pop()
        else:
            q = queue.popleft()

        if len(q):
            k = q[-1]+1
        else:
            k = 0

        for i in range(k, cnt):
            cur = list(q)
            cur.append(i)

            if len(cur) < cnt:
                queue.append(cur)

            yield list(map(lambda y: ints[y], cur))
