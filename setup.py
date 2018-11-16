from __future__ import with_statement

from setuptools import setup


VERSION = '1.1.0'


def readme():
    try:
        with open('README.rst') as f:
            return f.read()
    except IOError:
        return ''


INSTALL_REQUIRES = [
    'Django>=1.11',
]

TESTS_REQUIRE = [
    'pytest>=3.0.0',
    'pytest-cov',
    'tox',
]


setup(
    name='cafe24-sms-Django',
    version=VERSION,
    description='Send SMS messages to mobile devices through Cafe24 SMS api.',
    long_description=readme(),
    author='Hyunwoo Shim',
    author_email='hyunwoo.shim@laziness.xyz',
    url='https://github.com/iumjjing/cafe24-sms-Django',
    download_url='https://github.com/iumjjing/cafe24-sms-Django/archive/master.zip',
    packages=('cafe24_sms',),
    install_requires=INSTALL_REQUIRES,
    tests_require=TESTS_REQUIRE,
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
