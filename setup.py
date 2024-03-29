# -*- coding: utf-8 -*-

import setuptools

setuptools.setup(
    name='hhdpy',
    version='1.0.8',
    description='hhd2002를 위한 파이썬 커맨드라인 유틸리티',
    author='hhd2002',
    author_email='h2d2002@naver.com',
    url='https://github.com/HyundongHwang/hhdpy',
    install_requires=[],
    packages=setuptools.find_packages(),
    keywords=['hhdpy', 'hhd2002', 'utility'],
    python_requires='>=3',
    package_data={},
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'hhdpy = hhdpy.__main__:main',
        ]
    },
)

# for linux
# rm -rf build dist *.egg-info;
# python3 setup.py bdist_wheel;
# twine upload dist/*.whl;
# ;
# pip3 install -U hhdpy;
# pip3 install -U hhdpy;
# pip3 show hhdpy;
# ;
# git add *;
# git commit -m m;
# git push origin master;