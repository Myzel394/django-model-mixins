from pathlib import Path

from setuptools import setup, find_packages

current_version = "0.1.2"
download_url = f"https://github.com/Myzel394/django-model-mixins/archieve/v_" \
               f"{current_version}.tar.gz"

dev_requires = [
    "flake8",
    "flake8-docstrings",
    "flake8-dunder-all",
    "flake8-quotes"
]


def get_long_description(name: str = "README.md"):
    return Path.cwd().joinpath(name).read_text()

setup(
    name="django-model-mixins",
    version=current_version,
    author="Myzel394 Xyllian",
    author_email="myzel394.xyllian@gmail.com",
    url="https://github.com/Myzel394/django-model-mixins",
    description="Mixins for Django models.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
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
    install_requires=[
        "django"
    ],
    extra_require={
        "dev": dev_requires
    }
)
