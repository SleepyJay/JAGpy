# JAGpy
This is a collection of small utilities common to multiple projects. 

## Installation
Any project that needs one of these will likely have a `setup_jagpy.py` script. Generally, you just run it. As of this writing, any JAGpy modules will be usually be copied into a local JAGpy folder at the root of the repo using it. (I have my reasons.) 

This is typically just for my development needs, and is NOT intended to be some kind of universal solution (very much NOT). 

## Bits Provided

### Looper
Looper is a way to make n-size loops generically (and with only 3 loops internally and no regression). Like if you wanted to consider all combinations of 5 items, you might need 5 `for` loops... or just stick it into Looper. ;)

Also does basic decimal-to-binary type stuff. 

### MMDDYYYY
These are some simple sugar code for using dates in the MM/DD/YYYY format.
I had a project using a lot of dates and this made things simpler. 'Nuff said. 
(Tests not provided.)

### Structs
I wrote this to simplify lookups in a structure. Consider that the two Pythonic ways are something like either of:

```
if key in collection:
    return collection[key]
else:
    return None
```
or (ick)

```
try:
    return collection[key]
except KeyError:
    return None
```

Given that I might do a lot of lookups, I wanted to make that much eaiser, like say:
```lookup(collection, key)```. So I did.

(Tests not provided.)

### Numbers
Some generic number functions. Again, something like `is_int(value)` feels a lot better to me when I want to write it a few times than this (the actual body of `is_int` function):

```
try:
    int(val)
except TypeError:
    return False
else:
    return True

```

(Tests not provided.)

### Pyrove
An alternative way to run tests/scripts. (Again, I have my reasons.) See Pyrove_Notes.md for more. 



