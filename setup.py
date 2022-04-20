# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

with open("README.md","r",encoding="utf-8-sig") as f:
    readme = f.read()
requirements=['pythainlp']

setup(
    name="IsanNLP",
    version="0.1.dev1",
    description="Isan Natural Language Processing library",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="wannaphong",
    author_email="wannaphong@kkumail.com",
    url="https://github.com/wannaphongcom/IsanNLP",
    packages=find_packages(),
    install_requires=requirements
)
