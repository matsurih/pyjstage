import os
from setuptools import setup, find_packages


def read_requirements():
    """Parse requirements from requirements.txt."""
    reqs_path = os.path.join('.', 'requirements.txt')
    with open(reqs_path, 'r') as f:
        requirements = [line.rstrip() for line in f]
    return requirements


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pyjstage',
    version='v0.0.1',
    description='J-STAGE API wrapper for Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='matsurih',
    author_email='pipikapu@gmail.com',
    url='https://github.com/matsurih/pyjstage',
    license='MIT',
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=read_requirements(),
)
