__author__="samuel"
__date__ ="$Apr 2, 2011 2:02:41 PM$"

from setuptools import setup,find_packages

setup (
  name = 'collisions',
  version = '0.1',
  packages = find_packages(),

  # Declare your packages' dependencies here, for eg:
  install_requires=['foo>=3'],

  # Fill in these to make your Egg ready for upload to
  # PyPI
  author = 'samuel',
  author_email = '',

  summary = 'Just another Python package for the cheese shop',
  url = '',
  license = '',
  long_description= 'Long description of the package',

  # could also include long_description, download_url, classifiers, etc.

  
)