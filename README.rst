


.. image:: https://github.com/ChrisChV/RaveGen-Telegram-bot-generator/blob/developing/images/logo/logo.png
   :target: https://pypi.org/project/ravegen/
   :alt: RaveGen Logo
   
   

.. image:: https://img.shields.io/pypi/v/ravegen.svg
   :target: https://pypi.org/project/ravegen/
   :alt: Pypi version Badge

.. image:: https://api.codacy.com/project/badge/Grade/d29961acaea84b9baa6ad32f8e66b09c
   :target: https://app.codacy.com/app/ChrisChV/RaveGen-Telegram-bot-generator?utm_source=github.com&utm_medium=referral&utm_content=ChrisChV/RaveGen-Telegram-bot-generator&utm_campaign=Badge_Grade_Dashboard
   :alt: Codacy Badge

.. image:: https://www.codefactor.io/repository/github/chrischv/ravegen-telegram-bot-generator/badge
   :target: https://www.codefactor.io/repository/github/chrischv/ravegen-telegram-bot-generator
   :alt: CodeFactor

.. image:: https://img.shields.io/pypi/l/ravegen.svg
   :target: https://pypi.org/project/ravegen/
   :alt: Pypi license Badge

.. image:: https://travis-ci.com/ChrisChV/RaveGen-Telegram-bot-generator.svg?branch=master
   :target: https://travis-ci.com/ChrisChV/RaveGen-Telegram-bot-generator
   :alt: Build Status

.. image:: https://codecov.io/gh/ChrisChV/RaveGen-Telegram-bot-generator/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/ChrisChV/RaveGen-Telegram-bot-generator
   :alt: Codecov

==================================
RaveGen: Telegram bot generator
==================================


Program for generate, create and deploy telegram bots readable way. You do not need to know how the Telegram API works or how or where you are going to deploy the bot, you just have to worry about what the bot is going to reply.

RaveGen uses `python-telegram-bot <https://github.com/python-telegram-bot/python-telegram-bot>`_ for connect with `Telegram Bot API <https://core.telegram.org/bots/api>`_ and you can deploy the bot on Heroku or Google App Engine


===========
Installing
===========

------------------
Requirements
------------------

Depending on where you want to deploy the bot:

-   Heroku Cli:

.. code:: shell

    $ sudo snap install heroku --classic

-   Google App Engine:

    You need to follow the steps in `<https://cloud.google.com/sdk/docs/quickstart-debian-ubuntu>`_



-------------------------
RaveGen installation
-------------------------

You can install RaveGen with:

.. code:: shell

    $ sudo pip install ravegen --upgrade

**OR** clone this repository and run ``sudo make install``

==========================================
Create and deploy a bot in three steps!
==========================================

---------
Step 1
---------

Get the Token from `@BotFather <https://telegram.me/BotFather>`_. If you need help, you can read the `Tutorial for Create a Telegram Bot in BotFather <https://github.com/ChrisChV/RaveGen-Telegram-bot-generator/wiki/Tutorial:-Create-a-Telegram-Bot-in-BotFather>`_

---------
Step 2
---------

Run the follow command and paste the Token:

.. code:: shell

    $ ravegen init -m

--------
Step 3
--------

Run this command and follow the indications:

.. code:: shell

    $ ravegen deploy -d

---------
Eureka!
---------

Now find your bot on Telegram and try to tell it something.

=================
Advanced usage
=================

If you need help about the commands run:

.. code:: shell

    $ ravegen help

Or if you want to know more see the `RaveGen Wiki <https://github.com/ChrisChV/RaveGen-Telegram-bot-generator/wiki>`_
