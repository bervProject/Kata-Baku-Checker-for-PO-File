import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kata-baku-checkr-po-file",
    version="0.0.1",
    author="Bervianto Leo Pratama",
    author_email="bervianto.leo@gmail.com",
    description="Checker for Kata Baku for PO File reader",
    long_description=long_description,
    url="https://github.com/bervProject/Kata-Baku-Checker-for-PO-File/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
)
