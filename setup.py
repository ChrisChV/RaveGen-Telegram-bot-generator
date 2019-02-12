import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ravegen-dev",
    version="0.1.1",
    author="Christofer Chavez Carazas",
    author_email="xnpiochv@gmail.com",
    description="Program for generate basic telegram bots with python-telegram-bot and deploy it on Heroku ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ChrisChV/RaveGen-Telegram-bot-generator/tree/developing",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)