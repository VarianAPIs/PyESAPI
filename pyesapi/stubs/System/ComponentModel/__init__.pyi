from typing import Any, Dict, Generic, List, Optional, Union, overload
from datetime import datetime
from System import Type
from Microsoft.Win32 import RegistryKey

class Component(MarshalByRefObject):
    """Class docstring."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Container(self) -> Container:
        """Container: Property docstring."""
        ...

    @property
    def Site(self) -> Site:
        """Site: Property docstring."""
        ...

    @Site.setter
    def Site(self, value: Site) -> None:
        """Set property value."""
        ...

    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """Method docstring."""
        ...

    def Dispose(self) -> None:
        """Method docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetLifetimeService(self) -> Any:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def InitializeLifetimeService(self) -> Any:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

