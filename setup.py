from distutils.core import setup
from setuptools import find_packages

setup(
    name='pyesapi',
    version='0.2.3',
    description='A customized Python interface to Eclipse Scripting API',
    long_description='Leverages the pythonnet project to interface with dotnet CLI in real time. Helper functions and classes have been added to return numpy arrays and manage collections (of IEnumerable).'
    author='Michael M. Folkerts, PhD at Varian, a Siemens Healthineers Company',
    url='https://github.com/VarianAPIs/PyESAPI',
    author_email='Michael.Folkerts@varian.com',
    license='MIT',
    packages=find_packages(),
    python_requires=">=3.7, <4", # see up to date active releases here: https://www.python.org/downloads/ 
    install_requires=[
        'numpy',
        'scipy',
        'pythonnet',
        'pynetdicom'
    ],
)
