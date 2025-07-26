import os

# Support multiple ESAPI versions - adjust these paths as needed
PATHS = [
    # | ESAPI 15.6 location
    'C:\\Program Files (x86)\\Varian\\RTM\\15.6\\esapi\\API',
    # | ESAPI 16.x location (uncomment and adjust if you have newer versions)
    # 'C:\\Program Files (x86)\\Varian\\RTM\\16.0\\esapi\\API',
    # 'C:\\Program Files (x86)\\Varian\\RTM\\16.1\\esapi\\API',
    ]

# Add any custom ESAPI_PATH from environment
if 'ESAPI_PATH' in os.environ:
    PATHS.insert(0, os.environ['ESAPI_PATH'])

ASSEMBLIES = [
    # | System assemblies
    'System',  # Note: may have issues, can comment out if problematic
    # 'System.Drawing',  # Uncomment if needed
    'System.Windows',
    'System.Collections',
    'System.Runtime.InteropServices',
    'System.Xml',  # Added for completeness

    # | ESAPI assemblies (core)
    'VMS.TPS.Common.Model.API',
    'VMS.TPS.Common.Model.Types',
    
    # | Additional ESAPI assemblies (uncomment if needed)
    # 'VMS.TPS.Common.Model',
    # 'VMS.TPS.Common.Interfaces',
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
