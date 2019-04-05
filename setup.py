import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ravegen",
    version="0.2.3",
    scripts=['ravegen/ravegen'],
    author="Christofer Chavez Carazas",
    author_email="xnpiochv@gmail.com",
    description="Program for generate basic telegram bots with python-telegram-bot and deploy it on Heroku ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'python-telegram-bot',
    ],
    package_data={'ravegen': ["LICENSE", "rave_compl.bash", "ravegen/commands", "ravegen/version"]},
    include_package_data=True,
    url="https://github.com/ChrisChV/RaveGen-Telegram-bot-generator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
    ],
)
