from codecs import open
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="datascraper",  # Updated to match README.md
    version="1.1.15",  # Increment version or verify latest
    description="A Smart, Automatic, Fast and Lightweight Web Scraper for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/muddasirrob/datascraper",  # Added correct repository URL
    author="Muddasir Rauf",  # Standardized author name
    author_email="muddasirrob@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",  # Added specific versions
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
    ],
    keywords="scraping scraper web-scraping",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    python_requires=">=3.8",  # Updated to a more recent minimum version
    install_requires=[
        "requests>=2.25.0,<3.0.0",  # Added version constraints
        "bs4>=4.9.0",
        "lxml>=4.6.0",
    ],
)
