# PyESAPI
"Pie-Sappy"

A passion project to help accelerate breakthroughs in medical physics research by bringing the power of Python into the Varian API ecosystem.

## Quickstart

* Access your Eclipse 15.5 (or later) TBOX desktop
* Install [Anaconda3](https://www.anaconda.com/download/?lang=en-us)
  * Choose to install for "Just Me" (unless you know what you are doing and have admin privlages on your machine)
  * Use defaults (don't add anaconda to path, but do set ananconda as your default python installation)
* Optionally install google chrome or chromium browser (for better Jupyter Notebook experience) and set it as your default browser
* Launch "Anaconda Prompt" by searching in Windows menu
* In the prompt, execute the command `pip install https://api.github.com/repos/VarianAPIs/PyESAPI/tarball`
  * TODO: get official pypy distribution set up
* Then execute the command `jupyter notebook`
* Create a new notebook and see below for examples.

## Examples
* [Developer Workshop 2018](examples/DeveloperWorkshop2018/README.md)
* Stand-alone python script: [standalone.py](examples/standalone.py)

## Development
Set custom ESAPI_PATH (to DLLs) before import (bypasses production directory path search)
```python
import os
os.environ['ESAPI_PATH'] = r'C:\Users\CoolKid\Source\Magic\Bin\Debug64'
import pyesapi
# ...
```

## Proxy and Git Considerations
* [Proxy for Anaconda](https://support.anaconda.com/customer/en/portal/articles/2921276-using-anaconda-behind-a-firewall-or-proxy)
* Install git in a conda env: `conda install -c anaconda git`
  * No admin privlages are arequired when installing git this way  
* Proxy for git: `git config --global https.proxy https://some.proxy.net:1234`

