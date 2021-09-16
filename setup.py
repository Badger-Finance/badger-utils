from setuptools import setup


with open("requirements.txt", "r") as f:
    requirements = list(map(str.strip, f.read().split("\n")))[:-1]

setup(
    name="badger-utils",
    install_requires=requirements,
    author="Andrii Kulikov",
    author_email="blaynemono@gmail.com",
    url="https://github.com/SHAKOTN/badger-utils",
    python_requires=">=3.6,<4",
)
