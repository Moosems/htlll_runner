from distutils.core import setup

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name="htlll_runner",
    version="0.0.1",
    description="A simple python package to run htlll",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Moosems",
    author_email="moosems.j@gmail.com",
    url="https://github.com/Moosems/htlll_runner",
    install_requires=["ply"],
    packages=["htlll_runner"],
    entry_points={
        "console_scripts": [
            "htlll_runner = htlll_runner.__main__:main"
        ]
    }
)
