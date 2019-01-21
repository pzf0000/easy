import os
import re
from setuptools import setup, find_packages


def read(f):
    return open(f, 'r', encoding='utf-8').read()


def get_version(package):
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version('easy')

setup(
    name="easy",
    version=version,
    license="GPL-3.0",
    description="Easy Django MicroService Framework",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Leo Pan",
    author_email="pzf0000@foxmail.com",
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    install_requires=[
        "django",
        "bootstrap_admin",
    ],
    python_requires=">=3.5",
    zip_safe=False,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.1",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GPL License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Internet :: WWW/HTTP",
    ]
)
