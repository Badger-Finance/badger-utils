import pathlib

from setuptools import setup
from setuptools import find_packages


with open("requirements.txt", "r") as f:
    requirements = list(map(str.strip, f.read().split("\n")))[:-1]

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()


setup(
    name="badger-utils",
    install_requires=requirements,
    author="Andrii Kulikov",
    author_email="blaynemono@gmail.com",
    description="Badger utils and shared code",
    long_description=README,
    keywords=["badger-utils"],
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    version="0.2.2",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ],
    license="MIT",
    url="https://github.com/SHAKOTN/badger-utils",
    python_requires=">=3.7,<4",
)
