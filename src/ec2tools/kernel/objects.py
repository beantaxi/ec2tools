from . import misc, tags

def addNameProperty (o):
	misc.addProperty(o, 'name', getName, setName)


# ec2tools attempts to support using objects or object ids interchangeably.
#
# getId() is a little helper method to make that easy.
#
# If the argument is a string, return the argument.
# Else, return its id member.
#
# arg is not validated to make sure any of this works; if it doesn't, the normal
# Python exceptions will be raised.
def getId (arg):
	if isinstance(arg, str):
		id = arg
	else:
		id = arg.id
	return id


def getName (resource, tagsFieldName='tags'):
	name = tags.getTagValue(resource, 'Name')
	return name


def setName (resource, name):
	if not name == None:
		nameTag = {'Key': 'Name', 'Value': name}
		tags = [nameTag]
		resource.create_tags(Tags=tags)

