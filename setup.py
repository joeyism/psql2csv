# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('psql2csv/__init__.py').read(),
    re.M
    ).group(1)


with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")

with open("requirements.txt", "rb") as f:
    req = f.read().decode("utf-8")


setup(
    name = "psql2csv",
    packages = ["psql2csv"],
    entry_points = {
        "console_scripts": ['psql2csv = psql2csv.cli:main']
        },
    version = version,
    description = "A library and a CLI to download PostgreSQL schemas and tables",
    long_description = long_descr,
    author = "Joey Sham",
    author_email = "sham.joey@gmail.com",
    url = "http://www.joeyism.com",
    install_requires=req
    )
