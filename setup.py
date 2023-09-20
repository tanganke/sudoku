from setuptools import setup, find_packages

setup(
    name="sudoku",
    version="1.0.0",
    author="Anke Tang",
    author_email="tang.anke@foxmail.com",
    description="A Sudoku solver package",
    packages=find_packages(),
    install_requires=[
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "sudoku-solver=sudoku.cli:main",
        ],
    },
)
