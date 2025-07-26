from typing import Any, Dict, Generic, List, Optional, Union, overload
from datetime import datetime
from System import Type

class FileStreamAsyncResult:
    """Class docstring."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def AsyncState(self) -> Any:
        """Any: Property docstring."""
        ...

    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """WaitHandle: Property docstring."""
        ...

    @property
    def CompletedSynchronously(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsCompleted(self) -> bool:
        """bool: Property docstring."""
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

