from distutils.core import setup

setup(
    name='pyesapi',
    version='0.3dev',
    description='Python interface to Eclipse Scripting API',
    author='Michael Folkerts, Varian Medical Systems',
    author_email='Michael.Folkerts@varian.com',
    license='MIT',
    packages=['pyesapi'],
    install_requires=[
        'pip @ git+https://github.com/pythonnet/pythonnet@d3ca2e8f9d221853f5c75fbb0ff4c7c85dafa70d#egg=pythonnet',
    ],
)
