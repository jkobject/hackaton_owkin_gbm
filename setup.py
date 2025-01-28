"""Python setup.py for hackaton_owkin_gbm package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("hackaton_owkin_gbm", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="hackaton_owkin_gbm",
    version=read("hackaton_owkin_gbm", "VERSION"),
    description="Awesome hackaton_owkin_gbm created by jkobject",
    url="https://github.com/jkobject/hackaton_owkin_gbm/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="jkobject",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["hackaton_owkin_gbm = hackaton_owkin_gbm.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
