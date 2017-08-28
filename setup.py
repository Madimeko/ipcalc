import os

try:
    from setuptools import setup
    from setuptools import find_packages
except Exception as e:
    print("Requires 'setuptools'")
    print(" pip install setuptools")
    exit()

config = {
    "name": "ipcalc",
    "version": "0.0.0",
    "author": "christiaan F Rademan",
    "author_email": "chris@fwiw.co.za",
    "description": "MyProject Package Example",
    "license": "BSD 3-Clause",
    "keywords": "another example",
    "url": "http://www.fwiw.co.za",
    "packages": find_packages(),
    "include_package_data": True,
    "classifiers": [
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Environment :: Other Environment",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7"
        ]
    }

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

if os.path.exists(os.path.join(os.path.dirname(__file__),
                               'requirements.txt')):
    with open(os.path.join(os.path.dirname(__file__),
                           'requirements.txt')) as x:
        requirements = x.read().splitlines()
else:
    requirements = []

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as x:
    readme = x.read()

print("%s\n" % (config['name']))

setup(
    install_requires=requirements,
    long_description=readme,
    **config
)
