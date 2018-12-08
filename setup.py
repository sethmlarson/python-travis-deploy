import io
import re
from setuptools import setup, find_packages

with io.open("src/python_travis_deploy/__init__.py", "rt", encoding="utf-8") as f:
    version = re.search(r"^__version__\s+=\s+[\"\']([\d.]+)[\"\']$", f.read()).group(1)


with io.open("README.rst", "rt", encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="python_travis_deploy",
    version=version,
    license="Apache-2.0",
    description="A test project for deploying to PyPI from Travis",
    long_description=long_description,
    author="Seth Michael Larson",
    author_email="sethmichaellarson@gmail.com",
    packages=find_packages("src/"),
    package_dir={"": "src/"},
    requires=["urllib3"],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
