from .misc import justOneOrNone


def createTag (resource, key, value):
	tag = {'Key': key, 'Value': value}
	tags = [tag]
	resp = resource.create_tags(Tags=tags)
	return resp


def getTag (resource, tagName, tagFieldName='tags'):
	tags = resource.__getattribute__(tagFieldName)
	f = lambda x: x['Key'] == tagName
	tag = justOneOrNone(tags, f)
	return tag


def getTagValue (resource, tagName, tagFieldName='tags'):
	tag = getTag(resource, tagName, tagFieldName)
	value = tag['Value'] if tag else None
	return value
