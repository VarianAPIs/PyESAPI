from distutils.core import setup, find_packages

setup(
    name='pyesapi',
    version='0.5dev',
    description='Python interface to Eclipse Scripting API',
    author='Michael Folkerts, Varian Medical Systems',
    author_email='Michael.Folkerts@varian.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'pythonnet==2.3.0', # tested to work with python 3.6
    ],
)
