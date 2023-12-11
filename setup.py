# coding: utf-8
from codecs import open
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="pypinyin-dict",
    version="0.7.0",
    author="mozillazg",
    author_email="mozillazg101@gmail.com",
    description="使用 pinyin-data 和 phrase-pinyin-data 中的拼音数据文件覆盖 pypinyin 中的自带拼音数据，实现只使用某个或某些拼音数据文件中的拼音数据的需求",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mozillazg/pypinyin-dict",
    project_urls={
        "Bug Tracker": "https://github.com/mozillazg/pypinyin-dict/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    install_requires=['pypinyin'],
    packages=setuptools.find_packages(where="src"),
    python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*, <4',
)
