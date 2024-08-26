from setuptools import setup, find_packages

setup(
    name="blog_api",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "pydantic",
        "pytest",
        "httpx",
    ],
    entry_points={
        "console_scripts": [
            "blogapi=blog_api.main:run"
        ],
    },
    python_requires='>=3.11',
)
