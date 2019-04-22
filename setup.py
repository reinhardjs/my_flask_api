from setuptools import setup, find_packages

setup(
	name='myproject', 
	version='1.0', 
	packages=find_packages(),
	install_requires=['flask-restplus==0.9.2', 'Flask-SQLAlchemy==2.1']
)
