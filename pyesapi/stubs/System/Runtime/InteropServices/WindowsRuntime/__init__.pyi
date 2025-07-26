from typing import Any, Dict, Generic, List, Optional, Union, overload
from datetime import datetime
from System import Type, ValueType

class Point(ValueType):
    """Class docstring."""

    def __init__(self) -> None:
        """Initialize instance."""
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

