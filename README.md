# PyESAPI
"Pie-Sappy" for research use only.

A passion project to help accelerate breakthroughs in medical physics research by bringing the power of Python into the Varian API ecosystem.

## Quickstart (updated June 16th 2023)

* Access your Eclipse 15.5 (or later) TBOX desktop
* Install Python 3.10 or higher from: https://www.python.org/downloads/
* Optionally install google chrome or chromium browser (for better Jupyter Notebook experience) and set it as your default browser
* Launch "Command Prompt" by searching in Windows menu
* Navigate to a directory where you would like to store your first PyEsapi project using the `cd` command
* (optional) Create and activate a python virtual environment in this location using `python -m venv venv`
* In the prompt, execute the commands:
  * `pip install https://api.github.com/repos/VarianAPIs/PyESAPI/tarball`
  * `pip install jupyter`
* Then execute the command `jupyter notebook`
* Create a new notebook and see below for examples (be sure not to select "root" kernel).

## Examples
* [Developer Workshop 2018](examples/DeveloperWorkshop2018/README.md)
* Stand-alone python script: [standalone.py](examples/standalone.py)

## Upgrading
* Inside your project directory, execute `pip install https://api.github.com/repos/VarianAPIs/PyESAPI/tarball --upgrade`
  * This will check and upgrade PyESAPI if a newer version is available

# Development
For those wishing to contribute to PyESAPI

## Custom ESAPI DLL path
Set custom ESAPI_PATH (to DLLs) before import (bypasses production directory path search)
```python
import os
os.environ['ESAPI_PATH'] = r'C:\Users\CoolKid\Source\Magic\Bin\Debug64'
import pyesapi
# ...
```

## Stub Gen
To create lintable code and enable code completion (in Visual Studio Code at least) we generate python stubs for ESAPI libs...
1. [Download](https://ironpython.net/download/) and install IronPython (2.7.9 tested to work) in default location (C:\Program Files\IronPython 2.7\ipy.exe).
1. Load ironpython-stubs submodule `git submodule update --init` (ironstubs)
1. Move to stubgen folder `cd stubgen`
1. Execute script `stubgen.ps1` (if you hit a Pdb prompt, type continue)
1. Commit updates to stubs folder

## TODOs

