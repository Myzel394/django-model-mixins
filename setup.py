from setuptools import setup, find_packages

current_version = "0.0.2"
download_url = f"https://github.com/Myzel394/django-model-mixins/archieve/v_" \
               f"{current_version}.tar.gz"

setup(
    name="django-model-mixins",
    version=current_version,
    author="Myzel394 Xyllian",
    author_email="myzel394.xyllian@gmail.com",
    url="https://github.com/Myzel394/django-model-mixins",
    description="Mixins for Django models.",
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
    install_requires=["django", "pytz"],
)
