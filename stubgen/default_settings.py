import os

PATHS = [
    # | ESAPI 15.6 location
    'C:\\Program Files (x86)\\Varian\\RTM\\15.6\\esapi\\API',
    ]

ASSEMBLIES = [
    # 'WindowsBase',
    # # | System
    # 'System',
    # 'System.Drawing',
    # 'System.Windows',
    # 'System.Windows.Forms',
    # 'System.Collections.Generic',
    # 'System.Runtime.InteropServices',
    # | ESAPI
    'VMS.TPS.Common.Model.API',
    'VMS.TPS.Common.Model.Types',
    ]

BUILTINS = [
    'clr',
    'wpf'
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
