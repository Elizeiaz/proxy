import os

from setuptools import setup, find_packages


def read(*names, **kwargs):
    with open(os.path.join(os.path.dirname(__file__), *names),
              encoding='utf8') as fp:
        return fp.read()


setup(
    name="proxy",
    version="1.0",
    author="Trubin Vitaly",
    author_email="my_mail@example.com",
    description="Proxy-client",
    long_description=read('README.md'),
    packages=find_packages(),
    # install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
