import setuptools

from os import path


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="py-time-between",
    version="0.1.1",
    author="Allan Silva",
    author_email="allan.tavares@allantavares.com.br",
    description="Ordinary package to say if a time variable falls between two given times.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MicroarrayTecnologia/py-time-between",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        ],
)
