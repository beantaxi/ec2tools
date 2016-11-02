# This handy function is used to flexibly return a lambda, when passed
# an argument, a callable, or None
#
# If passed an argument, it creates a simple '==' lambda comparing a parameter to the argument
# If passed None, it creates a lambda which always returns True
# If passed a callable, it just returns the callable as is.
#
# The main use case for this function, is for functions like justOne(). Just one selects a single
# element from a list, and fails if <>1 matches are found.
def createFn (fnOrArg=None):
	if not fnOrArg:
		fn = lambda x : True	
	elif callable(fnOrArg):
		fn = fnOrArg
	else:
		arg = fnOrArg
		fn = lambda x: x == arg
	return fn


def first (coll, fnOrArg=None):
	fn = createFn(fnOrArg)
	hits = [el for el in coll if fn(el)]
	if not hits:
		hit = None
	else:
		hit = hits[0]
	return hit
		

def flattenListOfLists (listOfLists):
	list = [val for sublist in listOfLists for val in sublist]
	return list


# Find exactly one element in a collection.
#
# fnOrArg can be None, or a Value, or a Callable.
#    None:     return the first argument in the collection (assuming it has one)
#    Value:    return the element equal to the value, if exactly 1 exists
#    Callable: return the one and only element, for which the callable returns true
#
# This function takes the place of a lot of nuisance code, eg getting an instance and 
# confirming there is only one instance with that name. AWS tends to name things via tags,
# which are key-value pairs, and usually uniqueness is not enforced, so many instances
# (or volumes, etc) can all share a name. Even though they shouldn't. justOne() takes
# care of validating possible multiple hits.
def justOne (coll, fnOrArg=None):
	if not coll:
		raise Exception("No match found (collection is empty)")
	fn = createFn(fnOrArg)
	hits = [el for el in coll if fn(el)]
	if not hits:
		raise Exception("No matches found")
	if len(hits) > 1:
		raise Exception("More than 1 hit found")
	hit = hits[0]
	return hit


# Same as justOne(), except this returns None if there are no hits, instead of failing.
def justOneOrNone (coll, fnOrArg=None):
	if not coll:
		hit = None
	else:
		fn = createFn(fnOrArg)
		hits = [el for el in coll if fn(el)]
		if not hits:
			hit = None
		elif len(hits) > 1:
			raise Exception("More than 1 hit found")
		else:
			hit = hits[0]
	return hit


def toList (*args):
    if not isinstance(args, list):
        args = list(args)
    if len(args) == 1 and isinstance(args[0], list):
        args = args[0]
    return args
