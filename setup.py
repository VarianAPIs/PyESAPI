from distutils.core import setup

setup(
    name='pyesapi',
    version='0.2dev',
    description='Python interface to Eclipse Scripting API',
    author='Michael Folkerts, Varian Medical Systems',
    author_email='Michael.Folkerts@varian.com',
    license='MIT',
    packages=['pyesapi'],
    install_requires=[
        'pypiwin32',
        'numpy',
        'scipy',
        # 'pythonnet @ https://api.github.com/repos/pythonnet/pythonnet/tarball/d3ca2e8f9d221853f5c75fbb0ff4c7c85dafa70d', # some commit we know works
    ],
)
