# PyESAPI
"Pi-e-Sappy" for research use only.

A passion project to help accelerate breakthroughs in medical physics research by bringing the power of Python into the Varian API ecosystem.
PyESAPI combined with Jupyter Notebook gives you a "command line to Eclipse" allowing you to rapidly prototype your ESAPI scripts or research ideas.

## Quick Start (updated July 17th 2024)

* Access your Eclipse 15.5 (or later) TBOX desktop or Varian Innovation Center environment
* Install Python 3.10 or later from: https://www.python.org/downloads/
  * Be sure to check the option to "add python.exe to PATH" (unless you are already managing multiple versions of Python)
  * Note: If you use an older version of Python, your milage may vary.
* Launch "Command Prompt" by searching in Windows menu
* Navigate to a directory where you would like to store your first PyESAPI project using the `cd` command
* In the prompt, execute the commands:
  * `pip install pyesapi`
  * `pip install jupyter`
* Then execute the command `jupyter notebook`
* Create a new notebook and see below for examples (if you are using a python virtual environment, be sure not to select "root" kernel).

## Examples
### Jupyter Notebooks (from Developer Workshop 2018)
  * [Getting Started](http://nbviewer.jupyter.org/github/VarianAPIs/PyESAPI/blob/master/examples/DeveloperWorkshop2018/GettingStarted.ipynb)
  * [Data Mining](http://nbviewer.jupyter.org/github/VarianAPIs/PyESAPI/blob/master/examples/DeveloperWorkshop2018/DataMining.ipynb)
  * [10xResearch](http://nbviewer.jupyter.org/github/VarianAPIs/PyESAPI/blob/master/examples/DeveloperWorkshop2018/10xResearch.ipynb)
* Stand-alone python script: [standalone.py](examples/standalone.py)

## Known issues
* PyESAPI is not compatible with vscode-jupyter plugin which uses multithreading. ESAPI only allows for single-thread access to objects.
* Python 3.12 may require Microsoft Visual C++ 14.0 or greater. If you are using a VIC environment, you can get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
  * Note: anaconda provieds pre-built binaries for popular packages.

## Upgrading
* `pip install --upgrade pysapi`
  * This will check and upgrade PyESAPI if a newer version is available

## Recommended tooling:
Now that you've had a chance to explore the capabilities of PyESAPI, it's time to get more organized. Below are some recommendations on platforms and software to develop with.
  * Varian Innovation Center Eclipse environment (or local TBOX)
  * VisualStudio Code (lightweight IDE)
  * Google Chrome or Microsoft Edge set as default browser (for better Jupyter Notebook experience)
  * Git or GitHub Desktop (code repository and open source collaboration)

# Development Notes
For those wishing to contribute to PyESAPI or use PyESAPI with pre-released local builds of Eclipse.

## Custom ESAPI DLL path
Set custom ESAPI_PATH (to DLLs) before import (bypasses production directory path search)
```python
import os
os.environ['ESAPI_PATH'] = r'C:\Users\CoolKid\Source\Magic\Bin\Debug64'
import pyesapi
# ...
```

## Stub Gen (experimental/under construction)
To create lintable code and enable code completion (in Visual Studio Code at least) we can generate python stubs for ESAPI libs using IronPython...
1. [Download](https://ironpython.net/download/) and install IronPython (2.7.9 tested to work) in default location (C:\Program Files\IronPython 2.7\ipy.exe).
1. Load ironpython-stubs submodule `git submodule update --init` (ironstubs)
1. Move to stubgen folder `cd stubgen`
1. Execute script `stubgen.ps1` (if you hit a Pdb prompt, type continue)
1. Commit updates to stubs folder
