"""
PhaseSync - A semantic compression tool for development phases and AI collaboration.
"""

from setuptools import setup, find_packages

setup(
    name="phasesync",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "click>=8.0.0",
    ],
    entry_points={
        'console_scripts': [
            'phasesync=PhaseSync:main',
        ],
    },
    author="Donald Watts",
    author_email="limited.adls@gmail.com",
    description="A tool for managing and tracking codebases using the Symbolic Weight Protocol (SWP)",
    long_description=open("PhaseSync/README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/phasesync",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
)
