import os

PATHS = [
    # | ESAPI 15.6 location
    'C:\\Program Files (x86)\\Varian\\RTM\\15.6\\esapi\\API',
    ]

ASSEMBLIES = [
    # | System
    'System',  # broken?
    # 'System.Drawing',
    'System.Windows',
    'System.Collections',
    'System.Runtime.InteropServices',

    # | ESAPI
    'VMS.TPS.Common.Model.API',
    'VMS.TPS.Common.Model.Types',
    ]

BUILTINS = [
    'clr',
    ]

ASSEMBLIES.extend(BUILTINS)
ASSEMBLIES.sort()

REVIT_ASSEMBLIES = [
    # | Revit
    'RevitAPI',
    'RevitAPIUI',
    'RevitServices',
    'RevitNodes',
    ]

# | If running inside Revit, Process Revit Assemblies Only
try:
    __revit__
except NameError:
    pass
else:
    ASSEMBLIES = REVIT_ASSEMBLIES
