from setuptools import setup, find_packages

setup(
    name="llm-beginner-study",
    version="0.1.0",
    packages=find_packages(include=["projects.*"]),
    python_requires=">=3.8",
    install_requires=[],
)
