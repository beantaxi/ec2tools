from ec2tools.kernel.vars import iam

def getAccountId ():
	currentUser = iam.CurrentUser()
	arn = currentUser.arn
	ownerId = arn.split(':')[4]
	return ownerId



