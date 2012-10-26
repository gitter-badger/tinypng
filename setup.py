from setuptools import setup
from os.path import join, dirname
from tinypng import __version__


def read(fname):
    return open(join(dirname(__file__), fname)).read()


setup(
    name='tinypng',
    version=__version__,
    description='Access api.tinypng.org from the shell and python scripts',
    long_description=read('README.markdown'),
    author='Manuel Barkhau',
    author_email='mbarkhau@gmail.com',
    url='http://bitbucket.org/mbarkhau/tinypng/',
    license="MIT",
    packages=['tinypng'],
    install_requires=['docopt'],
    scripts=['scripts/tinypng'],
    keywords="png image compression tinypng shrink",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],

)
