from pathlib import Path

import pypandoc
from setuptools import setup, find_packages

current_version = "0.0.2"
download_url = f"https://github.com/Myzel394/django-model-mixins/archieve/v_" \
               f"{current_version}.tar.gz"

dev_requires = [
    "flake8",
    "flake8-docstrings",
    "flake8-dunder-all",
    "flake8-quotes"
]


def get_long_description(name: str = "README.md"):
    try:
        return pypandoc.convert("README.md", "rst")
    except (IOError, ImportError):
        description=open('README.md').read()


def get_install_requires():
    return Path.cwd().joinpath("requirements.txt").read_text().splitlines()


setup(
    name="django-model-mixins",
    version=current_version,
    author="Myzel394 Xyllian",
    author_email="myzel394.xyllian@gmail.com",
    url="https://github.com/Myzel394/django-model-mixins",
    description="Mixins for Django models.",
    long_description=get_long_description(),
    platforms=['OS Independent'],
    license="MIT",
    download_url=download_url,
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Framework :: Django",
        "Intended Audience :: Developers",
    ],
    keywords=["django", "django-utils", "django-models"],
    install_requires=get_install_requires(),
    extra_require={
        "dev": dev_requires
    }
)
