from setuptools import setup, find_packages

setup(
    name="CustomAPI",
    version="0.1",
    description="A package for string manipulation functions",
    packages=find_packages(),
    install_requires=[],  # No external dependencies
    author="Ramis H., Yucheng A., Bex A.",
    url="https://github.com/yourname/string_package",  # Update this with your repo
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

