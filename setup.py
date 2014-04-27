from distutils.core import setup

setup(
    name='bubbledoro',
    version='0.0.1',
    author='Jose Ricardo',
    author_email='root@josericardo.eti.br',
    packages=['bubbledoro'],
    scripts=['bin/bubbledoro'],
    url='http://pypi.python.org/pypi/bubbledoro/',
    license='LICENSE.txt',
    description='A command line pomodoro counter and goals tracker.',
    long_description=open('README.md').read(),
    install_requires=[
    ],
)
