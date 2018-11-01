﻿# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

with open("README-pypi.md", "r", encoding="utf-8") as readme_file:
    readme = readme_file.read()
readme_file.close()
with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="pythainlp",
    version="1.7.0.1",
    description="Thai natural language processing library",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="PyThaiNLP",
    author_email="wannaphong@kkumail.com",
    url="https://github.com/PyThaiNLP/pythainlp",
    packages=find_packages(),
    test_suite="tests",
    package_data={
        "pythainlp.corpus": [
            "corpus_license.md",
            "countries_th.txt",
            "pos_th.json",
            "pt_tagger_1.dill",
            "stopwords_th.txt",
            "syllables_th.txt",
            "tha-wn.db",
            "thailand_provinces_th.csv",
            "thailand_provinces_th.txt",
            "ud_thai-pud_pt_tagger.dill",
            "ud_thai-pud_unigram_tagger.dill",
            "unigram_tagger.dill",
            "words_th.txt",
            "words_th_frozen_201810.txt",
        ],
        "pythainlp.sentiment": ["vocabulary.data", "sentiment.data"],
    },
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords="pythainlp",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: Thai",
        "Topic :: Text Processing :: Linguistic",
    ],
)
