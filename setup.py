import io
import os
import re

from setuptools import find_packages, setup


with io.open("fab_quickstart/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r"__version__ = \"(.*?)\"", f.read()).group(1)


def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)


def read(fname):
    return open(fpath(fname)).read()


def desc():
    return read("README.rst")


project_urls = {
  'FAB Quick Start Guide': 'https://github.com/valhuber/fab-quickstart/wiki'
}

setup(
    name="FAB-Quickstart",
    version=version,  
    url="https://github.com/valhuber/fab-quickstart",
    license="BSD",
    author="Val Huber",
    author_email="valjhuber@gmail.com",
    project_urls=project_urls,
    description=(
        "Creates FAB view from model, for an instant multi-page, multi-table app."
        "Apps are multi-page: 1 page per table, with page-page navigation for related data."
        "Pages are multi-table: includes related_views, predictive joins."
    ),
    long_description=desc(),
    long_description_content_type="text/x-rst",
    packages=find_packages(),
    package_data={"": ["LICENSE"]},
    entry_points={
        "console_scripts": ["fab-quickstart=fab_quickstart.cli:start"]
    },
    include_package_data=True,
    zip_safe=False,
    platforms="any",
    install_requires=[
        "apispec[yaml]>=3.3, <4",
        "colorama>=0.3.9, <1",
        "click>=6.7, <8",
        "email_validator>=1.0.5, <2",
        "Flask>=0.12, <3",
        "Flask-Babel>=1, <2",
        "Flask-Login>=0.3, <0.5",
        "Flask-OpenID>=1.2.5, <2",
        "Flask-SQLAlchemy>=2.4, <3",
        "Flask-WTF>=0.14.2, <1",
        "Flask-JWT-Extended>=3.18, <4",
        "jsonschema>=3.0.1, <4",
        "marshmallow>=3, <4",
        "marshmallow-enum>=1.5.1, <2",
        "marshmallow-sqlalchemy>=0.22.0, <1",
        "python-dateutil>=2.3, <3",
        "prison>=0.1.3, <1.0.0",
        "PyJWT>=1.7.1",
        "sqlalchemy-utils>=0.32.21, <1",
    ],
    extras_require={"jmespath": ["jmespath>=0.9.5"]},
    tests_require=["nose>=1.0", "mockldap>=0.3.0"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires="~=3.6"
)