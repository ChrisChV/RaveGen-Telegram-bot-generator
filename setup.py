import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ravegen",
    version="0.3.1",
    scripts=['ravegen/ravegen'],
    author="Christofer Chavez Carazas",
    author_email="xnpiochv@gmail.com",
    license='MIT',
    description="Program for generate, create and deploy telegram bots readable way.",
    long_description=long_description,
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
