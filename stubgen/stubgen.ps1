# copy stubgen module locally
cp -r ..\iroonpython-stubs\ironstubs .

# overwirite default_settings.py with pyesapi repo version
cp .\default_settings.py .\ironstubs

# need logs dir else error
mkdir logs

# execute stubgen, add --debug if you get errors
& 'C:\Program Files\IronPython 2.7\ipy.exe' -m ironstubs make --all --overwrite --output=..\..\stubs