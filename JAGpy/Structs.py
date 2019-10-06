
"""This is a bunch of sugar around Python collections."""

#
def lookup(collection, key, if_none=None):
    """Lookup key in collection; if not found return if_none (or None)"""
    
    if isinstance(collection, list) or isinstance(collection, tuple):
        try:
            val = collection[key] 
            return val
        except IndexError:
            return if_none
        
    elif key in collection:
        if isinstance(collection, set):
            return key
        else:
            return collection[key]
    else:
        return if_none


#
def has_item(collection, key, if_none=None):
    """Lookup key in collection; if not found return if_none (or None)"""
    if key in collection:
        return True
    else:
        return if_none


#
def lookup_any(collection, keys, if_none=None):
    for key in keys:
        val = lookup(collection, key)

        if val:
            return val

    return if_none


#
def lookup_all(collection, keys, if_none=None):
    values = []
    for key in keys:
        val = lookup(collection, key)

        if not val:
            return if_none

        values.append(val)

    return values


def list_to_set_without(collection, without):
    new_set = set()
    for item in collection:
        if item in without:
            continue
        new_set.add(item)
    return new_set

