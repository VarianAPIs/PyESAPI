# copy stubgen module locally
# cp -r ..\iroonpython-stubs\ironstubs .
cp -r C:\Users\blw8175\PycharmProjects\ironpython-stubs\ironstubs .

# overwirite default_settings.py with pyesapi repo version
cp .\default_settings.py .\ironstubs

# need logs dir else error
mkdir logs

# execute stubgen, add --debug if you get errors, add --overwrite to re-gen things from scratch
& 'C:\Program Files\IronPython 2.7\ipy.exe' -m ironstubs make --all --overwrite --output=..\..\pyesapi\stubs
& 'C:\Program Files\IronPython 2.7\ipy.exe' -m ironstubs make System.Xml --overwrite --output=..\..\pyesapi\stubs