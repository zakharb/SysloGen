![logo](logo.png)

## _Simple Log Generator_ 

![](https://img.shields.io/badge/version-1.0-blue)
![](https://img.shields.io/badge/python-3.9-blue)

## Content  
[Info](#info)  
[Install](#install)  
[Usage](#usage)  

<a name="info"/>

## Info
</a>  

> The software is designed to generate a Log from File  
> It uses Log example file,
> read random message from this file and generate new one

<a name="info"/>

## Install
</a>  

- download `.whl` file
- install via `pip`
```sh
pip install zgenerator-xxx.whl
```

<a name="usage"/>

## Usage
</a>  

```sh
Syslogen 1.0 Simple Syslog Generator
Copyright (C) 2021 Bengart Zakhar
This program comes with ABSOLUTELY NO WARRANTY
This is free software, and you are welcome to redistribute it
under certain conditions; type `--license` for details.

   _______  _______ __    ____  _____________   __
  / ___/\ \/ / ___// /   / __ \/ ____/ ____/ | / /
  \__ \  \  /\__ \/ /   / / / / / __/ __/ /  |/ / 
 ___/ /  / /___/ / /___/ /_/ / /_/ / /___/ /|  /  
/____/  /_//____/_____/\____/\____/_____/_/ |_/   

usage: syslogen [options] -i input_file -c count

optional arguments:
  -h, --help   show this help message and exit
  -i, --input  File used to generate messages
  -c, --count  Number of generated messages per second
```