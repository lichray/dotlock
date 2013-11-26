import os
from setuptools import setup


setup(
    name='dotlock',
    version='0.1',
    description='Mandatory cross-process locking',
    author='Zhihao Yuan',
    author_email='zhihao.yuan@rackspace.com',
    packages=['dotlock'],
    zip_safe=True,
    license='BSD',
    keywords=['lockfile', 'multiprocessing'],
    url='https://github.com/lichray/dotlock',
    tests_require=open('tools/test-requires', 'rt').readlines(),
)
