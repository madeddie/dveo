from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="dveo",
    version="0.2.1",
    description="DVEO REST API wrapper",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/madeddie/dveo",
    author="Edwin Hermans",
    author_email="edwin@madtech.cx",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="dveo video encoder api",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    install_requires=["requests", "xmltodict"],
    extras_require={"dev": ["black", "flake8", "rope", "pydocstyle", "sphinx"]},
    # package_data={"sample": ["package_data.dat"]},  # Optional
    # entry_points={"console_scripts": ["sample=sample:main"]},  # Optional
    project_urls={
        "Bug Reports": "https://github.com/madeddie/dveo/issues",
        "Source": "https://github.com/madeddie/dveo/",
    },
)
