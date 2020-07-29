import setuptools

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="kata-baku-checkr-po-file",
    version="0.1.2",
    author="Bervianto Leo Pratama",
    author_email="bervianto.leo@gmail.com",
    description="Checker for Kata Baku for PO File reader",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/bervProject/Kata-Baku-Checker-for-PO-File/",
    packages=setuptools.find_packages(),
    install_requires=[
        'polib',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
)
