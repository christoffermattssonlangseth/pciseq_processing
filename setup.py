from setuptools import setup
import setuptools

setuptools.setup(
    name="pciseq_processing-christoffermattssonlangseth", 
    version="0.0.1",
    author="Christoffer Mattsson Langseth",
    author_email="christoffer.langseth@scilifelab.se",
    description="Package to process data for pciseq and the ouput from pciseq",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/christoffermattssonlangseth/pciseq_processing",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
