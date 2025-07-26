from typing import Any, Dict, Generic, List, Optional, Union, overload
from datetime import datetime
from System import Array, Type

class BitArray:
    """Class docstring."""

    def __init__(self, length: int) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, length: int, defaultValue: bool) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, bytes: Array[int]) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, values: Array[bool]) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, values: Array[int]) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, bits: BitArray) -> None:
        """Initialize instance."""
        ...

    @property
    def Count(self) -> int:
        """int: Property docstring."""
        ...

    @property
    def IsReadOnly(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsSynchronized(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def Item(self) -> bool:
        """bool: Property docstring."""
        ...

    @Item.setter
    def Item(self, value: bool) -> None:
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
    def SyncRoot(self) -> Any:
        """Any: Property docstring."""
        ...

    def And(self, value: BitArray) -> BitArray:
        """Method docstring."""
        ...

    def Clone(self) -> Any:
        """Method docstring."""
        ...

    def CopyTo(self, array: Array, index: int) -> None:
        """Method docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def Get(self, index: int) -> bool:
        """Method docstring."""
        ...

    def GetEnumerator(self) -> IEnumerator:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def Not(self) -> BitArray:
        """Method docstring."""
        ...

    def Or(self, value: BitArray) -> BitArray:
        """Method docstring."""
        ...

    def Set(self, index: int, value: bool) -> None:
        """Method docstring."""
        ...

    def SetAll(self, value: bool) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    def Xor(self, value: BitArray) -> BitArray:
        """Method docstring."""
        ...


class DictionaryBase:
    """Class docstring."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Count(self) -> int:
        """int: Property docstring."""
        ...

    def Clear(self) -> None:
        """Method docstring."""
        ...

    def CopyTo(self, array: Array, index: int) -> None:
        """Method docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetEnumerator(self) -> DictionaryEnumeratorByKeys:
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


class IEnumerator:
    """Class docstring."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Current(self) -> Any:
        """Any: Property docstring."""
        ...

    def MoveNext(self) -> bool:
        """Method docstring."""
        ...

    def Reset(self) -> None:
        """Method docstring."""
        ...


class ReadOnlyList:
    """Class docstring."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Count(self) -> int:
        """int: Property docstring."""
        ...

    @property
    def IsFixedSize(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsReadOnly(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsSynchronized(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def Item(self) -> Any:
        """Any: Property docstring."""
        ...

    @Item.setter
    def Item(self, value: Any) -> None:
        """Set property value."""
        ...

    @property
    def SyncRoot(self) -> Any:
        """Any: Property docstring."""
        ...

    def Add(self, obj: Any) -> int:
        """Method docstring."""
        ...

    def Clear(self) -> None:
        """Method docstring."""
        ...

    def Contains(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def CopyTo(self, array: Array, index: int) -> None:
        """Method docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetEnumerator(self) -> IEnumerator:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def IndexOf(self, value: Any) -> int:
        """Method docstring."""
        ...

    def Insert(self, index: int, obj: Any) -> None:
        """Method docstring."""
        ...

    def Remove(self, value: Any) -> None:
        """Method docstring."""
        ...

    def RemoveAt(self, index: int) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

