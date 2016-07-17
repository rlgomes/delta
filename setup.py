"""
setup.py
"""
from setuptools import setup, find_packages

__VERSION = '0.4.1'

setup(
    name='delta',
    version=__VERSION,
    author='Rodney Gomes',
    author_email='rodneygomes@gmail.com',
    url='https://github.com/rlgomes/delta',
    install_requires=[],
    tests_require=[
        'robber==1.0.1'
    ],
    test_suite='test',
    keywords=['date', 'durations', 'timedelta'],
    py_modules=['delta'],
    packages=find_packages(exclude=['test']),

    license='MIT',
    description='Human friendly context aware duration parsing library',
    long_description='https://github.com/rlgomes/delta',
)
