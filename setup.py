import os
from setuptools import setup
from pip._internal.network.session import PipSession
from pip._internal.req import parse_requirements


requirements = parse_requirements(
    os.path.join(
        os.path.dirname(__file__),
        'requirements.txt'
    ), session=PipSession()
)

if __name__ == '__main__':
    setup(
        name='colab-super',
        version='0.1.0',
        author='geekyrakshit',
        author_email='19soumik.rakshit96@gmail.com',
        packages=['colab_super'],
        url='http://pypi.python.org/pypi/PackageName/',
        description='A python package that provides various utilities for your adventures with Google Colab',
        long_description=open('README.md').read(),
        install_requires=[str(requirement.requirement) for requirement in requirements]
    )
