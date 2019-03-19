from setuptools import setup, find_packages

setup(
    name='pypackage',
    version='0.1',
    packages=find_packages(exclude=['tets']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/sh3zaad/pypackage',
    author='Shezaad Essop Moosa',
    author_email='shezaadem@gmail.com'
)
