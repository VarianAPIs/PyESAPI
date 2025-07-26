from typing import Any, Dict, Generic, List, Optional, Union, overload
from datetime import datetime
from System import Array, Type
from System import AggregateException
from System.Globalization import CultureInfo

class StringBuilder:
    """Class docstring."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, capacity: int) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, value: str) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, value: str, capacity: int) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, value: str, startIndex: int, length: int, capacity: int) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, capacity: int, maxCapacity: int) -> None:
        """Initialize instance."""
        ...

    @property
    def Capacity(self) -> int:
        """int: Property docstring."""
        ...

    @Capacity.setter
    def Capacity(self, value: int) -> None:
        """Set property value."""
        ...

    @property
    def Chars(self) -> Char:
        """Char: Property docstring."""
        ...

    @Chars.setter
    def Chars(self, value: Char) -> None:
        """Set property value."""
        ...

    @property
    def Length(self) -> int:
        """int: Property docstring."""
        ...

    @Length.setter
    def Length(self, value: int) -> None:
        """Set property value."""
        ...

    @property
    def MaxCapacity(self) -> int:
        """int: Property docstring."""
        ...

    def Append(self, value: Char, repeatCount: int) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Append(self, value: Array[Char], startIndex: int, charCount: int) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Append(self, value: str) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Append(self, value: str, startIndex: int, count: int) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Append(self, value: int) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Append(self, value: int) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Append(self, value: Char) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Append(self, value: int) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Append(self, value: int) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Append(self, value: int) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Append(self, value: float) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Append(self, value: float) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Append(self, value: float) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Append(self, value: int) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Append(self, value: int) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Append(self, value: int) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Append(self, value: Any) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Append(self, value: Array[Char]) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Append(self, value: Any, valueCount: int) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Append(self, value: bool) -> StringBuilder:
        """Method docstring."""
        ...

    def AppendFormat(self, format: str, arg0: Any) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def AppendFormat(self, format: str, arg0: Any, arg1: Any) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def AppendFormat(self, format: str, arg0: Any, arg1: Any, arg2: Any) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def AppendFormat(self, provider: CultureInfo, format: str, arg0: Any) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def AppendFormat(self, provider: CultureInfo, format: str, arg0: Any, arg1: Any) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def AppendFormat(self, provider: CultureInfo, format: str, arg0: Any, arg1: Any, arg2: Any) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def AppendFormat(self, format: str, args: Array[Any]) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def AppendFormat(self, provider: CultureInfo, format: str, args: Array[Any]) -> StringBuilder:
        """Method docstring."""
        ...

    def AppendLine(self) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def AppendLine(self, value: str) -> StringBuilder:
        """Method docstring."""
        ...

    def Clear(self) -> StringBuilder:
        """Method docstring."""
        ...

    def CopyTo(self, sourceIndex: int, destination: Array[Char], destinationIndex: int, count: int) -> None:
        """Method docstring."""
        ...

    def EnsureCapacity(self, capacity: int) -> int:
        """Method docstring."""
        ...

    def Equals(self, sb: StringBuilder) -> bool:
        """Method docstring."""
        ...

    @overload
    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def Insert(self, index: int, value: str, count: int) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Insert(self, index: int, value: str) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Insert(self, index: int, value: int) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Insert(self, index: int, value: int) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Insert(self, index: int, value: int) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Insert(self, index: int, value: Char) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Insert(self, index: int, value: Array[Char]) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Insert(self, index: int, value: Array[Char], startIndex: int, charCount: int) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Insert(self, index: int, value: int) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Insert(self, index: int, value: int) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Insert(self, index: int, value: float) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Insert(self, index: int, value: float) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Insert(self, index: int, value: float) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Insert(self, index: int, value: int) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Insert(self, index: int, value: int) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Insert(self, index: int, value: int) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Insert(self, index: int, value: Any) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Insert(self, index: int, value: bool) -> StringBuilder:
        """Method docstring."""
        ...

    def Remove(self, startIndex: int, length: int) -> StringBuilder:
        """Method docstring."""
        ...

    def Replace(self, oldValue: str, newValue: str) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Replace(self, oldValue: str, newValue: str, startIndex: int, count: int) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Replace(self, oldChar: Char, newChar: Char) -> StringBuilder:
        """Method docstring."""
        ...

    @overload
    def Replace(self, oldChar: Char, newChar: Char, startIndex: int, count: int) -> StringBuilder:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    @overload
    def ToString(self, startIndex: int, length: int) -> str:
        """Method docstring."""
        ...

