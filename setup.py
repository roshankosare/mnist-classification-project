import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"
SRC_REPO = "mnistClassifier"



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)