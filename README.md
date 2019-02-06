# RaveGen: Telegram bot generator


Program for generate, create and deploy telegram bots using [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) for connect with [Telegram Bot API](https://core.telegram.org/bots/api) and Heroku for deploy the bot.

## Installing

### Requiremenst

- [python-telegram-bot:](https://github.com/python-telegram-bot/python-telegram-bot)

```shell
$ pip install python-telegram-bot --upgrade
```

- Heroku Cli:

```shell
$ sudo snap install heroku --classic
```

### RaveGen installation

Download the package:

- Deb Package (Wait! Compiling...)
- Rpm Package (Wait! Compiling...)

Install the package:

- Deb package:

```shell
$ sudo dpkg -i ravegen-{version}.deb
```

- Rpm Package:

```shell
$ sudo dnf install ravegen-{version}.rpm
```
**OR** clone this repository and run `sudo make install`

## Create and deploy a bot in three steps!


### Step 1

Get the Token from [@BotFather](https://telegram.me/BotFather). If you need help, you can read the [Tutorial for Create a Telegram Bot in BotFather](https://github.com/ChrisChV/RaveGen-Telegram-bot-generator/wiki/Tutorial:-Create-a-Telegram-Bot-in-BotFather)


### Step 2

Run the follow command and paste the Token:

```shell
$ ravegen init -m
```

### Step 3

Run this command and follow the indications:

```shell
$ ravegen deploy -d
```
### Eureka!

Now find your bot on Telegram and try to tell it something.

## Advanced usage

If you need help about the commands run:

```
$ ravegen help
```

Or if you want to know more see the [RaveGen Wiki](https://github.com/ChrisChV/RaveGen-Telegram-bot-generator/wiki)

