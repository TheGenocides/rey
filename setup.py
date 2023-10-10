from distutils.core import setup

with open("README.md", "r") as f:
    readme = f.read()

setup(
    name = "reyline",         
    packages = ["rey", "rey.models"],   
    version = "0.1",      
    license="MIT",    
    description = "An API wrapper designed to simplify the process of integrating Line Messaging API",
    long_description=readme,
    long_description_content_type="text/markdown",
    author = "TheGenocide",
    author_email = "luke.genesis.hyder@gmail.com",
    url = "https://github.com/TheGenocides/rey",
    download_url = "https://github.com/TheGenocides/rey/archive/refs/tags/v0.1.tar.gz",
    python_requires=">=3.7.0",
    keywords = ["line-bot", "apiwrapper", "line", "api"],
    install_requires=[
        "aiohttp"
    ],
    classifiers=[
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",      
    "Topic :: Software Development :: Build Tools",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11"

    ],
)