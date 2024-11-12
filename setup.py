from setuptools import setup
from setuptools import find_packages

PROJECT_NAME = "sensor"
__version__ = '0.0.1'

with open(file='README.md',mode='r',encoding='utf-8') as file:
    long_description_content = file.read()

setup(
    name = PROJECT_NAME,
    version = __version__,
    author = "shrikanth",
    author_email= "shrikanthp04@gmail.com",
    description = "Air Pressure system (APS) sensor system",
    long_description = long_description_content,
    packages = find_packages(),
)
