from distutils.core import setup

setup(
    name='pyesapi',
    version='0.4dev',
    description='Python interface to Eclipse Scripting API',
    author='Michael Folkerts, Varian Medical Systems',
    author_email='Michael.Folkerts@varian.com',
    license='MIT',
    packages=['pyesapi'],
    install_requires=[
        'git+https://github.com/pythonnet/pythonnet@master#egg=pythonnet',
    ],
)
