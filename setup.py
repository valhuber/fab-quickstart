from setuptools import setup, find_packages

setup(
      # mandatory
      name='fab_quickstart',
      # mandatory
      version='0.1',
      # mandatory
      author_email='valjhuber@gmail.com',
      packages=['fab_quickstart'],
      package_data={},
      install_requires=['click'],
      entry_points={
        'console_scripts': ['fab_quickstart_cli:start']
      }
)