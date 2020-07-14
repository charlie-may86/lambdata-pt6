

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata6",  # the name that you will install via pip
    version="1.1",
    author="Charlie May",
    author_email="camiv95@gmail.com",
    description="contains a function that enlarges a number by 100x",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # required if using a md file for long desc
    license="MIT",
    url="https://github.com/charlie-may86/lambdata-pt6",
    # keywords="",
    packages=find_packages()  # ["my_lambdata"]
)
