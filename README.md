<p align="center">
  <img src="logo.png" alt="animated" />
</p>

<p align="center">
  The simplest syslog generator.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-1.1-blue" height="20"/>
  <img src="https://img.shields.io/badge/python-3.11-blue" height="20"/>
</p>

<p align="center">
  <img src="usage.gif" alt="animated" />
</p>


## Getting Started

[Syslogen](https://github.com/zakharb/syslogen) generates messages from file and send them to external Syslog server.  

### Prerequisites

No additional libraries are required.

### Installing

Git clone project, install package via `pip`
```
git clone git@github.com:zakharb/syslogen.git
python3 -m pip install dist/syslogen-*.whl
```
<p align="center">
  <img src="install.gif" alt="animated" />
</p>

## Usage

Choose server and port  
Set sending speed  
Specify file with logs examples  

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

Use virtual environment `venv` for isolating code

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/zakharb/syslogen/tags). 

## Authors

* **Zakhar Bengart** - *Initial work* - [Ze](https://github.com/zakharb)

See also the list of [contributors](https://github.com/zakharb/contributors) who participated in this project.

## License

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation - see the [LICENSE](LICENSE) file for details

