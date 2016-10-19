import setuptools


setuptools.setup(name='ec2tools',
                 description='Handy tools for using boto as intended.',
                 keywords='boto boto3 awsi ec2',
                 version='0.4.2',
                 url='https://github.com/beantaxi/ec2tools',
                 author='Chris Lalos',
                 author_email='chris.lalos@gmail.com',
                 install_requires=['boto3'],
                 packages=['ec2tools', 'ec2tools.api'],
                 package_dir={'': '.'})
#                 packages=setuptools.find_packages(exclude=['tests']))
