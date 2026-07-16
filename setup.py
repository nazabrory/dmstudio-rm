from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

exec(open('dmstudio/version.py').read())

version = __version__


setup(name='dmstudio',
      version=version,
      description='Python module for Datamine Studio RM scripting with AI agent capabilities',
      url='https://github.com/nazabrory/dmstudio',
      download_url='https://github.com/nazabrory/dmstudio/archive/' + version + '.tar.gz',
      license='MIT',
      packages=['dmstudio'],
      include_package_data=True,
      package_data={'': ['LICENSE.txt', 'README.md']},
      zip_safe=False)
