from typing import Any, Dict, Generic, List, Optional, Union, overload
from datetime import datetime
from System import Type, ValueType

class SerializationInfo:
    """Class docstring."""

    def __init__(self, type: Type, converter: FormatterConverter) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, type: Type, converter: FormatterConverter, requireSameTokenInPartialTrust: bool) -> None:
        """Initialize instance."""
        ...

    @property
    def AssemblyName(self) -> str:
        """str: Property docstring."""
        ...

    @AssemblyName.setter
    def AssemblyName(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def FullTypeName(self) -> str:
        """str: Property docstring."""
        ...

    @FullTypeName.setter
    def FullTypeName(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def IsAssemblyNameSetExplicit(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsFullTypeNameSetExplicit(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def MemberCount(self) -> int:
        """int: Property docstring."""
        ...

    @property
    def ObjectType(self) -> Type:
        """Type: Property docstring."""
        ...

    def AddValue(self, name: str, value: Any, type: Type) -> None:
        """Method docstring."""
        ...

    @overload
    def AddValue(self, name: str, value: Any) -> None:
        """Method docstring."""
        ...

    @overload
    def AddValue(self, name: str, value: bool) -> None:
        """Method docstring."""
        ...

    @overload
    def AddValue(self, name: str, value: Char) -> None:
        """Method docstring."""
        ...

    @overload
    def AddValue(self, name: str, value: int) -> None:
        """Method docstring."""
        ...

    @overload
    def AddValue(self, name: str, value: int) -> None:
        """Method docstring."""
        ...

    @overload
    def AddValue(self, name: str, value: int) -> None:
        """Method docstring."""
        ...

    @overload
    def AddValue(self, name: str, value: int) -> None:
        """Method docstring."""
        ...

    @overload
    def AddValue(self, name: str, value: int) -> None:
        """Method docstring."""
        ...

    @overload
    def AddValue(self, name: str, value: int) -> None:
        """Method docstring."""
        ...

    @overload
    def AddValue(self, name: str, value: int) -> None:
        """Method docstring."""
        ...

    @overload
    def AddValue(self, name: str, value: int) -> None:
        """Method docstring."""
        ...

    @overload
    def AddValue(self, name: str, value: float) -> None:
        """Method docstring."""
        ...

    @overload
    def AddValue(self, name: str, value: float) -> None:
        """Method docstring."""
        ...

    @overload
    def AddValue(self, name: str, value: float) -> None:
        """Method docstring."""
        ...

    @overload
    def AddValue(self, name: str, value: datetime) -> None:
        """Method docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetBoolean(self, name: str) -> bool:
        """Method docstring."""
        ...

    def GetByte(self, name: str) -> int:
        """Method docstring."""
        ...

    def GetChar(self, name: str) -> Char:
        """Method docstring."""
        ...

    def GetDateTime(self, name: str) -> datetime:
        """Method docstring."""
        ...

    def GetDecimal(self, name: str) -> float:
        """Method docstring."""
        ...

    def GetDouble(self, name: str) -> float:
        """Method docstring."""
        ...

    def GetEnumerator(self) -> SerializationInfoEnumerator:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetInt16(self, name: str) -> int:
        """Method docstring."""
        ...

    def GetInt32(self, name: str) -> int:
        """Method docstring."""
        ...

    def GetInt64(self, name: str) -> int:
        """Method docstring."""
        ...

    def GetSByte(self, name: str) -> int:
        """Method docstring."""
        ...

    def GetSingle(self, name: str) -> float:
        """Method docstring."""
        ...

    def GetString(self, name: str) -> str:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def GetUInt16(self, name: str) -> int:
        """Method docstring."""
        ...

    def GetUInt32(self, name: str) -> int:
        """Method docstring."""
        ...

    def GetUInt64(self, name: str) -> int:
        """Method docstring."""
        ...

    def GetValue(self, name: str, type: Type) -> Any:
        """Method docstring."""
        ...

    def SetType(self, type: Type) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...


class StreamingContext(ValueType):
    """Class docstring."""

    def __init__(self, state: StreamingContextStates) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, state: StreamingContextStates, additional: Any) -> None:
        """Initialize instance."""
        ...

    @property
    def Context(self) -> Any:
        """Any: Property docstring."""
        ...

    @property
    def State(self) -> StreamingContextStates:
        """StreamingContextStates: Property docstring."""
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

