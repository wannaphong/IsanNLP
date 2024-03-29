# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

with open("README.md","r",encoding="utf-8-sig") as f:
    readme = f.read()
requirements=[
    'pythainlp',
    'pandas'
]

setup(
    name="IsanNLP",
    version="0.1.dev2",
    description="Isan Natural Language Processing library",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="wannaphong",
    package_data={
        "isannlp": [
            "corpus/*",
        ]
    },
    author_email="wannaphong@yahoo.com",
    url="https://github.com/wannaphongcom/IsanNLP",
    packages=find_packages(),
    install_requires=requirements
)
