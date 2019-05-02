# Pyrove
An alternative way to run tests/scripts. (Again, I have my reasons.)

## Concept
Consider a directory structure like this:

```
Project/
	Foo/
		bar.py # wants to import Baz/qux.py
		test.py
		tests/
			test_bar.py # wants to import Foo/bar.py
	Baz/
		qux.py
```

Where Foo and Baz are "independent-ish" projects or libraries or etc. Debates about repository theory or package-and-build techniques aside, I think this is pretty reasonable situation in which to to find oneself. 

Each one might have their own set of unit tests. It gets a bit tough when those tests want to import things above it. Generally speaking, you can do something like these:
	
	$ python -m unittest Foo/tests/test_bar.py
	$ python -m unittest Foo/tests/test_*.py 

Which is fine, although perhaps a bit less "elegant" looking. And you for sure can't do something like this (AFAIK):

	$ python -m unittest Foo/tests/test_bar.py arg
	$ python -m unittest Foo/tests/test_bar.py --arg
	$ python -m unittest discover

In the first two cases, `unittest` will interpret your args as a module or argument to itself, which will likely fail. And in the third case `unittest` will of course try to run more than you want, and probably will still have module issues.

So instead, this module tries to make things a little easier. Use it to run a set of tests like this:

	# Runs anything in `Foo/tests/` named like `test_*.py`
	$ python Foo/test.py 
	# ...same, but passing "safe" into each
	$ python Foo/test.py safe

Now, I grant that this is probably only useful in development--and specifically when you don't have paths set up or IDEs like Pycharm, or whatever. But it certainly allows me to write in a README for anyone coming across my Git to run `python Foo/test.py`, which is pretty simple. 

## Set up
For this to work, you need two things:

1. Ability to import `Pyrove.py` (probably from the `setup_jagpy.py` script)
2. A file that looks like `test.py` or similar. The one given here is so generic, you probably can just drop it anywhere and be done, so long as `Pyrove.py` is importable from it.

Once you have one, you can pretty much copy-drop it anywhere without changes.
