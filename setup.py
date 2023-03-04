import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="appcode",
    version="0.0.1",
    author="Max Rodriguez Guell",
    author_email="rodriguezguell.max@gmail.com",
    description="An useful package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MaxMasterCOder/AppMaker",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)