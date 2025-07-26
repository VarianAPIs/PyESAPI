from typing import Any, Dict, Generic, List, Optional, Union, overload
from datetime import datetime
from System import Enum, Type
from Microsoft.Win32 import RegistryHive
from System import TypeCode
from System.Globalization import CultureInfo
from VMS.TPS.Common.Model.Types import BlockType

class BlockType:
    """Class docstring."""

    Dynamic: BlockType
    Static: BlockType
    Uncompressed: BlockType
