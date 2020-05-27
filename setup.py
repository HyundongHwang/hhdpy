# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name                = 'hhdpy',
    version             = '0.1',
    description         = 'hhdpy',
    author              = 'hhd2002',
    author_email        = 'h2d2002@naver.com',
    url                 = 'https://github.com/HyundongHwang/hhdpy',
    download_url        = 'https://github.com/HyundongHwang/hhdpy/archive/0.0.tar.gz',
    install_requires    =  [],
    packages            = find_packages(exclude = []),
    keywords            = ['hhdpy'],
    python_requires     = '>=3',
    package_data        = {},
    zip_safe            = False,
    classifiers         = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)