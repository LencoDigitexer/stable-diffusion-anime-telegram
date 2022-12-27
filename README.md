# Stable Diffusion Anime Telegram
**A Telegram bot for converting an image into an anime-style image based on the stable diffusion API.**
- Find it on Telegram as [Stable Diffusion Anime](https://t.me/stablediffusion_api_bot)


## Features
- [X] Simple image processing.

## ToDo 
- [ ] Choosing the image style.
- [ ] Re-converting an image.
- [ ] Viewing hints (what the neural network saw).

## Deploying

### Deploy on [Heroku](https://heroku.com)
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

### Installation
- Clone this git repository.
```sh 
git clone https://github.com/lencodigitexer/stable-diffusion-anime-telegram
```
- Change Directory
```sh 
cd stable-diffusion-anime-telegram
```
- Install requirements with pip3
```sh 
pip3 install -r requirements.txt
```

### Configuration
**There are two Ways for configuring this bot.**
1. Get a token from https://t.me/BotFather/
2. Rename config.py.example to config.py
2. Add bot token in [config.py](config.py)

### Deploy 
```sh 
python3 -m bot
```


## Copyright & License
- Copyright (©) 2023 by [LencoDigitexer](https://github.com/lencodigitexer)
- Licensed under the terms of the [GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007](./LICENSE)
