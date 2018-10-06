import sys, os
from setuptools import setup, find_packages

setup(name="PACKAGENAME", packages=find_packages())
sys.path.append(os.path.dirname(os.path.abspath(__file__)))