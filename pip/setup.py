from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from os import path

here = path.abspath(path.dirname(__file__))
setup(
    name = "cucats",
    version = "2.0.0",
    packages=["cucats"],
#    packages=find_packages(),
    description = "A CUCaTS python course self check exercise module",
    author = "D. Low",
    author_email = "daniellowtw@gmail.com",
    url = "http://about.me/daniel.low",
    download_url = "http://cucats.org",
    keywords = ["CUCaTS"],
    install_requires = ['pygeocoder'],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Beginners",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Topic :: Learning",
        ],
    long_description = """\
CUCaTS exercise module
-------------------------------------
This includes exercises for a Beginners Python workshop.
"""
)