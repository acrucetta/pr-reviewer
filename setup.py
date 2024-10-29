from setuptools import setup, find_packages

setup(
    # Basic package information
    name="git_pr_generator",     # The name pip uses to install your package
    version="0.2.0",            # Package version (semantic versioning recommended)
    description="A tool to make pull-requests",
    long_description=open("README.md").read(),  # Your README.md content
    long_description_content_type="text/markdown",
    
    # Package discovery
    packages=find_packages(),    # Automatically find all Python packages in your project
    
    # Dependencies
    install_requires=[          # List of required packages
        "anthropic>=0.3.0",     # >= means "this version or newer"
        "click>=8.0.0",
    ],
    
    # This is the magic that creates your command-line tool
    entry_points={
        "console_scripts": [
            "git-pr=git_pr_generator.cli:main",  # command=package.module:function
        ],
    },
    
    # Additional metadata for PyPI
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    
    # Python version requirement
    python_requires=">=3.7",
)