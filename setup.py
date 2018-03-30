from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

about = {}
with open(path.join(here, 'invain', '__version__.py'),
          'r', 'utf-8') as f:
    exec(f.read(), about)

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

packages=find_packages(exclude=['contrib', 'docs', 'tests*'])

setup(
  name=about['__title__'],
  version=about['__version__'],
  description=about['__description__'],
  long_description = long_description,
  author = 'Alan Arechiga',
  author_email = 'alan@macler.us',
  license=about['__license__'],
  url=about['__github_url__'],
  download_url = 'https://github.com/hailfire113/InVaIN/archive/0.1.tar.gz',
  keywords = ['invain', 'stocks', 'data','finance', 'yahoo','quotes'],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Financial and Insurance Industry',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Office/Business :: Financial',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
   ],
   packages=find_packages(exclude=['contrib', 'docs', 'tests']),
   install_requires=['requests'],
)
