from ec2tools._kernel import factory

def createTag (resource, key, value):
	tag = {'Key': key, 'Value': value}
	tags = [tag]
	resp = resource.create_tags(Tags=tags)
	return resp


def getName (resource, tagsFieldName='tags'):
	nameTag = getTag(resource, "Name", tagsFieldName)
	name = nameTag['Value'] if nameTag else None
	return name


def getTag (resource, tagName, tagFieldName='tags'):
	tags = resource.__getattribute__(tagFieldName)
	matches = [tag for tag in tags if tag['Key'] == tagName] if tags else []
	if len(matches) > 1:
		raise(Exception("More than one matching tag"))
	tag = matches[0] if matches else None
	return tag


def nameInstance (idInstance, name):
	instance = factory.Instance(idInstance)
	resp = createTag(instance, 'Name', name)


def nameVolume (idVolume, name):
	volume = factory.Volume(idVolume)
	resp = createTag(volume, 'Name', name)
	return resp


