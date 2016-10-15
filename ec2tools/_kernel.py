import boto3

# Shared variables
cli = boto3.client("ec2")
factory = boto3.resource("ec2")
glacier = boto3.resource("glacier")
iam = boto3.resource("iam")


def createFn (fnOrArg):
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
		

def getAccountId ():
	currentUser = iam.CurrentUser()
	arn = currentUser.arn
	ownerId = arn.split(':')[4]
	return ownerId


def getId (arg):
	if isinstance(arg, str):
		id = str(arg)
	else:
		id = arg.id
	return id


def justOne (coll, fnOrArg=None):
	fn = createFn(fnOrArg)
	hits = [el for el in coll if fn(el)]
	if not hits:
		raise Exception("No matches found")
	if len(hits) > 1:
		raise Exception("More than 1 hit found")
	hit = hits[0]
	return hit


def toList (*args):
    if not isinstance(args, list):
        args = list(args)
    if len(args) == 1 and isinstance(args[0], list):
        args = args[0]
    return args
