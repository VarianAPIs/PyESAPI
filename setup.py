from distutils.core import setup
from setuptools import find_packages

setup(
    name='pyesapi',
    version='0.2.1',
    description='Python interface to Eclipse Scripting API',
    author='Michael Folkerts, Varian Medical Systems',
    author_email='Michael.Folkerts@varian.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'pythonnet', #  v2.3.0 tested to work with python 3.6
    ],
)
