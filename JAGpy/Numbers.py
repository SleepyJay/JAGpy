
"""Some easy number functions"""


#
def has_sign(val):
    if val < 0:
        return '-'
    elif val > 0:
        return '+'
    else:
        return 0


# While it may be Pythonic to check for an int by using Exception, it's a bit...unweildly. So, compromise?
def is_int(val):
    try:
        int(val)
    except TypeError:
        return False
    else:
        return True


def intify(val):
    """When passed a number-like string, give me back a real number"""
    try:
        num = int(val)
        return num

    except TypeError:
        return val

    except ValueError:
        return val


def bin_to_int(b):
    digits = list(b)

    i = 0
    val = 0
    while digits:
        d = int(digits.pop())

        val += d * pow(2, i)
        i += 1

    return val

