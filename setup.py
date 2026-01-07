from setuptools import setup, find_packages

setup(
    name="vendas-cli",
    version="1.0.0",
    py_modules=["main"],
    entry_points={
        "console_scripts": [
            "vendas-cli=main:run",
        ],
    },
    install_requires=[],
    python_requires=">=3.11",
)
