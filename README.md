<p align="center">
  <img src="logo.png" alt="animated" />
</p>

<p align="center">

  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&pause=1000&color=0A7AFF&center=true&width=435&lines=+The+simplest+syslog+generator." alt="Typing SVG" />
  </a>

</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-1.1-blue" height="20"/>
  <img src="https://img.shields.io/badge/python-3.11-blue" height="20"/>
</p>

<p align="center">
  <img src="usage.gif" alt="animated" />
</p>


## Getting Started

[Syslogen](https://github.com/zakharb/syslogen) is the simple Syslog generator that creates messages from file and send them to external Syslog server.  

### Requirements

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)  
Only Python3, no additional libraries are required.

### Installing

Git clone project
```
git clone git@github.com:zakharb/syslogen.git
```

Install package via `pip`
```
python3 -m pip install dist/syslogen-*.whl
```
<p align="center">
  <img src="install.gif" alt="animated" />
</p>

## Usage

All parameters send via arguments. 
- set syslog server where to send logs
- change server port (optional) `--port` 
- set sending messages per second `--count`
- set input file with logs examples `--input`  

### Examples

Start with 2 msg/sec and standart port

```
python3 -m syslogen 192.168.1.1 -i examples_messages.txt -c 2
```

Start with 4 msg/sec and port 5514
```
python3 -m syslogen 192.168.1.1 -p 5514 -i examples_messages.txt -c 4
```

## Deployment

Edit Dockerfile and spicify server IP address

Build image
```
docker build --network host -t syslogen .
```

Run image
```
docker run syslogen
```
## Versioning

Using [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/zakharb/syslogen/tags). 

## Authors

* **Zakhar Bengart** - *Initial work* - [Ze](https://github.com/zakharb)

See also the list of [contributors](https://github.com/zakharb/syslogen/contributors) who participated in this project.

## License

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation - see the [LICENSE](LICENSE) file for details

