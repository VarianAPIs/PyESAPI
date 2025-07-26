from typing import Any, Dict, Generic, List, Optional, Union, overload
from datetime import datetime
from System import Type
from System import Exception, IntPtr
from System.Reflection import MethodBase
from System.Runtime.Serialization import SerializationInfo, StreamingContext

class _Attribute:
    """Class docstring."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    def GetIDsOfNames(self, riid: str, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr) -> None:
        """Method docstring."""
        ...

    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """Method docstring."""
        ...

    def GetTypeInfoCount(self, pcTInfo: int) -> None:
        """Method docstring."""
        ...

    def Invoke(self, dispIdMember: int, riid: str, lcid: int, wFlags: int, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> None:
        """Method docstring."""
        ...


class _Exception:
    """Class docstring."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def HelpLink(self) -> str:
        """str: Property docstring."""
        ...

    @HelpLink.setter
    def HelpLink(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def InnerException(self) -> Exception:
        """Exception: Property docstring."""
        ...

    @property
    def Message(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Source(self) -> str:
        """str: Property docstring."""
        ...

    @Source.setter
    def Source(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def StackTrace(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def TargetSite(self) -> MethodBase:
        """MethodBase: Property docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetBaseException(self) -> Exception:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

