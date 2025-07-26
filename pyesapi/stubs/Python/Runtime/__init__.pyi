from typing import Any, Dict, Generic, List, Optional, Union, overload
from datetime import datetime
from System import Type, ValueType
from System import IntPtr

class Slot(ValueType):
    """Class docstring."""

    def __init__(self, id: TypeSlotID, value: IntPtr) -> None:
        """Initialize instance."""
        ...

    @property
    def ID(self) -> TypeSlotID:
        """TypeSlotID: Property docstring."""
        ...

    @property
    def Value(self) -> IntPtr:
        """IntPtr: Property docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

