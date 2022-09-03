from setuptools import setup, Extension
from pybind11.setup_helpers import Pybind11Extension


with open("requirements.txt", "r") as file:
    requirements = file.read().splitlines()
    print(requirements)

with open("README.rst", "r") as file:
    readme = file.read()


extensions = [Pybind11Extension('zombies.zombies', ['zombies.cpp'])]


setup(
    name="zombies-speed",
    version="1.0.0a",
    author="The Master",
    license="MIT",
    description="A speedup for zombies.",
    long_description=readme,
    long_description_content_type="text/x-rst",
    ext_modules=extensions,
    install_requires=requirements,
)
