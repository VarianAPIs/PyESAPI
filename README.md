# PyESAPI
"Pie-Sappy" for research use only.

A passion project to help accelerate breakthroughs in medical physics research by bringing the power of Python into the Varian API ecosystem.

## Quickstart
To simpify the install process and to provide users with accelerated (pre-compiled) numerical libraries, Anaconda's python distribution and repos are recommended. As of this commit, pythonnet's pypi build only officailly supports python 3.6, therefore, we will provide a conda environment file to standardize a working environment for pyesapi until further notice. The following documents the quickest path to a "live" jupyter notebook:

* Access your Eclipse 15.5 (or later) TBOX desktop
* Install [Anaconda3](https://www.anaconda.com/download/?lang=en-us)
  * Choose to install for "Just Me" (unless you know what you are doing and have admin privlages on your machine)
  * Use defaults (don't add anaconda to path, but do set ananconda as your default python installation)
* Optionally install google chrome or chromium browser (for better Jupyter Notebook experience) and set it as your default browser
* Launch "Anaconda Prompt" by searching in Windows menu
* In the prompt, execute the command `curl -O https://raw.githubusercontent.com/VarianAPIs/PyESAPI/master/condaenv36.yml`
  * This command downloads the anaconda base environment definition file for use with pyesapi (used for all examples)
* In the prompt, execute the command `conda env create -f condaenv36.yml`
  * This command actually creates the anaconda environment
* In the prompt, execute the command `conda activate pyesapi36`
* Then execute the command `jupyter notebook`
* Create a new notebook and see below for examples (be sure not to select "root" kernel).

## Examples
* [Developer Workshop 2018](examples/DeveloperWorkshop2018/README.md)
* Stand-alone python script: [standalone.py](examples/standalone.py)

## Upgrading
* Inside your conda env, execute `pip install https://api.github.com/repos/VarianAPIs/PyESAPI/tarball --upgrade`
  * This will check and upgrade PyESAPI if a newer version is available

## Visual Studio Code
* Tested to work with new projects being built with pyesapi
* Install [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
* Select your pyesapi36 conda env (bottom bar, left side)
* Set path to conda in your *User* settings.json:
  * `"python.condaPath": "C:\\Example\\Path\\To\\anaconda3\\Scripts\\conda.exe"`
* Set cmd to default integrated terminal in *Workspace* settings.json file [(ref)](https://code.visualstudio.com/docs/editor/integrated-terminal#_configuration)
  * `"terminal.integrated.shell.windows": "C:\\Windows\\System32\\cmd.exe"`
* Linting is still experimental, but code completion seems to work, please report any issues you find
  * Flake8 is already included in the provided pyesapi36 conda env

## Proxy and Git Considerations
* [Proxy for Anaconda](https://support.anaconda.com/customer/en/portal/articles/2921276-using-anaconda-behind-a-firewall-or-proxy)
* Install git in a conda env: `conda install -c anaconda git`
  * No admin privlages are arequired when installing git this way  
* Proxy for git: `git config --global https.proxy https://some.proxy.net:1234`

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
- [*] PyESAPI Stubs V1 (2.7 style, incomplete)
- [ ] PyESAPI Stubs V2 (.pyi style, needs dev work)
- [ ] Official PyPi release
- [*] Visual Studio Code support
- [ ] Versioning of stubs
