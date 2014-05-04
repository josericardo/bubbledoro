from distutils.core import setup
from distutils.command.install import INSTALL_SCHEMES

for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

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
    data_files=[('bubbledoro', ['sounds/lets_play.wav', 'sounds/chewy.wav', 'sounds/available.wav'])],
    include_package_data=True,
    install_requires=[
    ],
)
