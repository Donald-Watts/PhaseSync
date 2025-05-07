"""
PhaseSync - A semantic compression tool for development phases and AI collaboration.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="PhaseSync",
    version="0.1.0",
    author="Donald Watts",
    author_email="limited.adls@gmail.com",
    description="A semantic compression tool for development phases and AI collaboration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Donald-Watts/PhaseSync",
    project_urls={
        "Bug Tracker": "https://github.com/Donald-Watts/PhaseSync/issues",
        "Documentation": "https://github.com/Donald-Watts/PhaseSync#readme",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "typing-extensions>=4.0.0",
    ],
    entry_points={
        "console_scripts": [
            "phasesync=PhaseSync.__main__:main",
        ],
    },
)
