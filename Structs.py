
"""This is a bunch of sugar around Python collections."""


#
def lookup(collection, key, if_none=None):
    """Lookup key in collection; if not found return if_none (or None)"""
    if key in collection:
        return collection[key]
    else:
        return if_none
