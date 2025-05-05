from setuptools import setup, find_packages

setup(
    name='phasesync',
    version='0.1.0',
    author='ADLS Consulting',
    author_email='limited.adls@gmail.com',
    description='A symbolic compression and architectural phase-weighting tool for intelligent codebase management.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/adlsconsulting/phasesync',
    packages=find_packages(),
    install_requires=[
        'click>=8.0.0'
    ],
    entry_points={
        'console_scripts': [
            'phasesync=PhaseSync:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
