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
        'numpy',
        'scipy',
        'pythonnet'
    ],
)
