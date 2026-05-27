from setuptools import setup, find_packages

setup(
    name="code-formatter-pro-rust-20260526_181748",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'code=code:main',
        ],
    },
)
