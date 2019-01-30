# PyESAPI
"Pie-Sappy"

A passion project to help accelerate breakthroughs in medical physics research by bringing the power of Python into the Varian API ecosystem.

## Quickstart

* Access your Eclipse 15.5 (or later) TBOX desktop
* Install [Anaconda3](https://www.anaconda.com/download/?lang=en-us) for "Just Me" (unless you know what you are doing)
  * Use defaults (don't add anaconda to path, but do set ananconda as your default python installation)
* Optionally install google chrome or chromium browser (for better Jupyter Notebook experience) and set it as your default browser
* Launch "Anaconda Prompt" by searching in Windows menu
* Execute the command `conda install -c anaconda git`
* If you are behind a proxy do `git config --global https.proxy https://some.proxy.net:1234`
* Execute the command `pip install git+https://github.com/VarianAPIs/PyESAPI`
* Execute the command `jupyter notebook`
* Create a new notebook and see below for examples.

## Examples
* [Developer Workshop 2018](examples/DeveloperWorkshop2018/README.md)
* Stand-alone python script: [standalone.py](examples/standalone.py)

## Development
Set custom ESAPI_PATH (to DLLs) before import (bypasses production directory path search)
```python
import os
os.environ['ESAPI_PATH'] = "C:\\Users\\CoolKid\\Source\\Magic\\Bin\\Debug64"
import pyesapi
# ...
```
