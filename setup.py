from distutils.core import setup
setup(
  name = 'empath',
  packages = ['empath'], # this must be the same as the name above
  version = '0.01',
  description = 'A tool for text analysis',
  author = 'Ethan Fast',
  author_email = 'ejhfast@gmail.com',
  url = 'https://github.com/Ejhfast/empath-client', # use the URL to the github repo
  download_url = 'https://github.com/Ejhfast/meta/empath-client/0.48a',
  keywords = ['social science', 'lexicon', 'text analysis'], # arbitrary keywords
  classifiers = [],
  install_requires=[
          'requests'
  ]
)