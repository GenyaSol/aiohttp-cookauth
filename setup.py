from setuptools import setup, find_packages
import os
import re


with open(os.path.join(os.path.abspath(os.path.dirname(
        __file__)), 'aiohttp_cookauth', '__init__.py'), 'r', encoding='latin1') as fp:
    try:
        version = re.findall(r"^__version__ = '([^']+)'$", fp.read(), re.M)[0]
    except IndexError:
        raise RuntimeError('Unable to determine version.')


def read(f):
    return open(os.path.join(os.path.dirname(__file__), f)).read().strip()


install_requires = ['aiohttp>=3.2.0']
tests_require = install_requires + ['pytest']
extras_require = {
    'aioredis': ['aioredis>=1.0.0'],
}


setup(name='aiohttp-cookauth',
      version=version,
      description=("authorization via cookies for aiohttp.web"),
      long_description='\n\n'.join((read('README.md'))),
      classifiers=[
          'License :: OSI Approved :: Apache Software License',
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Topic :: Internet :: WWW/HTTP',
          'Framework :: AsyncIO',
      ],
      author='Evgeny Solomatin',
      author_email='solgenya@gmail.com',
      url='https://github.com/GenyaSol/aiohttp_cookauth/',
      license='Apache 2',
      packages=find_packages(),
      install_requires=install_requires,
      include_package_data=True,
      extras_require=extras_require)
