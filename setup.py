import setuptools


setuptools.setup(name='ec2tools',
                 version='0.4.1',
                 url='https://github.com/beantaxi/ec2tools',
                 install_requires=['boto3'],
                 packages=setuptools.find_packages('ec2tools'))
