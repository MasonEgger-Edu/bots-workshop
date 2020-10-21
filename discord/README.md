# Build Your First Discord Bot

This tutorial has you build *Randombot*, a fun little bot with the following commands:

When the bot "hears" the following phrases in any discord channel, it will do
the following

* "roll a die" or "roll a dice" - Roll a 6 sided die and give you the result
* "roll a d<X>" - Roll a die with the specified amount of sides and give you the result
* "flip a coin" - Flip a coin and give you the result
* "pick a card" - Choose a random card from a standard 52 card deck and give you the result


## Prerequisites
* A developer environment setup with your favorite IDE/Text Editor
* Python3 installed
* A discord server that you are the administrator of and can add bots to

## Instructions

1. Create your discord bot in the [Discord Developer Portal](https://realpython.com/how-to-make-a-discord-bot-python/#how-to-make-a-discord-bot-in-the-developer-portal)
1. Create a folder for virtual environments if you don't already have one 
    1. `mkdir ~/.venvs`
1. Install a python virtual environment 
    1. `python -m venv ~/.venvs/discord`
1. Activate your python virtual environment
    1. `source ~/.venvs/discord/bin/activate`
1. Install `discord.py`
    1. **NOTE** Due to discord API changes, it is currently necessary to install
    a version that is < 1.5
    1. `pip install "discord.py>=1.4,<1.5"`
    1. This will only work until Discord kills the v6 gateway. Then we'll actually
    have to learn the new API
1. Run `pip freeze > requirements.txt` so it can be uploaded to GitHub and installed
in App Platform
1. Write the code.
    1. See provided randombot.py
1. If using `doctl`, use the specfile provided. Otherwise deploy a random 
static site
1. Create a new github repo and upload your code, requirements, and spec file
1. Enable GitHub access to the repository in the create new app workflow
1. Either deploy a static site and then, after it is done deploy the bot as a
worker 
1. Or run `doctl apps create --spec spec.yaml`