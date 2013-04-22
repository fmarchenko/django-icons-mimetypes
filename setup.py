# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(name="django-icons-mimetypes",
      description="Mimetypes icons from the Tango project and template tag",
      version="1.0",
      author="Bors Ltd",
      author_email="icons_mimetypes@bors-ltd.fr",
      license="GPL3",
      long_description=open("README.txt").read(),
      url="https://github.com/bors-ltd/django-icons-mimetypes",
      packages=find_packages(),
      include_package_data=True,
      setup_requires=['distribute'],
      install_requires=open('requirements.txt').read())
