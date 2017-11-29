from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


packages=find_packages(exclude=['contrib', 'docs', 'tests*'])

setup(
  name = 'InVaIN',
  version = '0.1.3',
  description = 'A util to pull stock data',
  long_description = long_description,
  author = 'Alan Arechiga',
  author_email = 'alan@macler.us',
  license = 'MIT',
  url = 'https://github.com/hailfire113/InVaIN', # use the URL to the github repo
  download_url = 'https://github.com/hailfire113/InVaIN/archive/0.1.tar.gz', # I'll explain this in a second
  keywords = ['invain', 'stocks', 'data','finance', 'yahoo','quotes'], # arbitrary keywords
  classifiers=[
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Intended Audience :: Financial and Insurance Industry',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Office/Business :: Financial'

    # Pick your license as you wish (should match "license" above)
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
   ],
   packages=find_packages(exclude=['contrib', 'docs', 'tests']),
   install_requires=['requests'],
)
