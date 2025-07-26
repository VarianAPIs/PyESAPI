from typing import Any, Dict, Generic, List, Optional, Union, overload
from datetime import datetime
from System.Collections import IEnumerator
from Microsoft.Win32 import RegistryHive
from System.Collections import DictionaryBase
from System.Globalization import CultureInfo
from System.IO import FileStreamAsyncResult
from System.Reflection import Assembly, AssemblyName, MethodBase, MethodInfo
from System.Runtime.InteropServices import _Attribute, _Exception
from System.Runtime.Serialization import SerializationInfo, StreamingContext

class Action(MulticastDelegate):
    """Class docstring."""

    def __init__(self, object: Any, method: IntPtr) -> None:
        """Initialize instance."""
        ...

    @property
    def Method(self) -> MethodInfo:
        """MethodInfo: Property docstring."""
        ...

    @property
    def Target(self) -> Any:
        """Any: Property docstring."""
        ...

    def BeginInvoke(self, callback: AsyncCallback, object: Any) -> FileStreamAsyncResult:
        """Method docstring."""
        ...

    def Clone(self) -> Any:
        """Method docstring."""
        ...

    def DynamicInvoke(self, args: Array[Any]) -> Any:
        """Method docstring."""
        ...

    def EndInvoke(self, result: FileStreamAsyncResult) -> None:
        """Method docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetInvocationList(self) -> Array[Delegate]:
        """Method docstring."""
        ...

    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def Invoke(self) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...


class Action(Generic[T], MulticastDelegate):
    """Class docstring."""

    def __init__(self, object: Any, method: IntPtr) -> None:
        """Initialize instance."""
        ...

    @property
    def Method(self) -> MethodInfo:
        """MethodInfo: Property docstring."""
        ...

    @property
    def Target(self) -> Any:
        """Any: Property docstring."""
        ...

    def BeginInvoke(self, obj: T, callback: AsyncCallback, object: Any) -> FileStreamAsyncResult:
        """Method docstring."""
        ...

    def Clone(self) -> Any:
        """Method docstring."""
        ...

    def DynamicInvoke(self, args: Array[Any]) -> Any:
        """Method docstring."""
        ...

    def EndInvoke(self, result: FileStreamAsyncResult) -> None:
        """Method docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetInvocationList(self) -> Array[Delegate]:
        """Method docstring."""
        ...

    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def Invoke(self, obj: T) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...


class AggregateException(Exception):
    """Class docstring."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, message: str) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, innerExceptions: List[Exception]) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, innerExceptions: Array[Exception]) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, message: str, innerExceptions: List[Exception]) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, message: str, innerExceptions: Array[Exception]) -> None:
        """Initialize instance."""
        ...

    @property
    def Data(self) -> DictionaryBase:
        """DictionaryBase: Property docstring."""
        ...

    @property
    def HResult(self) -> int:
        """int: Property docstring."""
        ...

    @HResult.setter
    def HResult(self, value: int) -> None:
        """Set property value."""
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
    def InnerExceptions(self) -> ReadOnlyCollection[Exception]:
        """ReadOnlyCollection[Exception]: Property docstring."""
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

    def Flatten(self) -> AggregateException:
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

    @overload
    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def Handle(self, predicate: Func[Exception, bool]) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...


class ApplicationException(Exception):
    """Class docstring."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, message: str) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
        """Initialize instance."""
        ...

    @property
    def Data(self) -> DictionaryBase:
        """DictionaryBase: Property docstring."""
        ...

    @property
    def HResult(self) -> int:
        """int: Property docstring."""
        ...

    @HResult.setter
    def HResult(self, value: int) -> None:
        """Set property value."""
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

    @overload
    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...


class Array:
    """Class docstring."""

    def __init__(self) -> None:
        """Initialize instance."""
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
    def Length(self) -> int:
        """int: Property docstring."""
        ...

    @property
    def LongLength(self) -> int:
        """int: Property docstring."""
        ...

    @property
    def Rank(self) -> int:
        """int: Property docstring."""
        ...

    @property
    def SyncRoot(self) -> Any:
        """Any: Property docstring."""
        ...

    @staticmethod
    def AsReadOnly(array: Array[T]) -> ReadOnlyCollection[T]:
        """Method docstring."""
        ...

    @staticmethod
    def BinarySearch(array: Array, value: Any) -> int:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def BinarySearch(array: Array, index: int, length: int, value: Any) -> int:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def BinarySearch(array: Array, value: Any, comparer: StringComparer) -> int:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def BinarySearch(array: Array[T], value: T) -> int:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def BinarySearch(array: Array[T], value: T, comparer: IComparer[T]) -> int:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def BinarySearch(array: Array[T], index: int, length: int, value: T) -> int:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def BinarySearch(array: Array[T], index: int, length: int, value: T, comparer: IComparer[T]) -> int:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def BinarySearch(array: Array, index: int, length: int, value: Any, comparer: StringComparer) -> int:
        """Method docstring."""
        ...

    @staticmethod
    def Clear(array: Array, index: int, length: int) -> None:
        """Method docstring."""
        ...

    def Clone(self) -> Any:
        """Method docstring."""
        ...

    @staticmethod
    def ConstrainedCopy(sourceArray: Array, sourceIndex: int, destinationArray: Array, destinationIndex: int, length: int) -> None:
        """Method docstring."""
        ...

    @staticmethod
    def ConvertAll(array: Array[TInput], converter: Converter[TInput, TOutput]) -> Array[TOutput]:
        """Method docstring."""
        ...

    @staticmethod
    def Copy(sourceArray: Array, destinationArray: Array, length: int) -> None:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Copy(sourceArray: Array, sourceIndex: int, destinationArray: Array, destinationIndex: int, length: int) -> None:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Copy(sourceArray: Array, destinationArray: Array, length: int) -> None:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Copy(sourceArray: Array, sourceIndex: int, destinationArray: Array, destinationIndex: int, length: int) -> None:
        """Method docstring."""
        ...

    def CopyTo(self, array: Array, index: int) -> None:
        """Method docstring."""
        ...

    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """Method docstring."""
        ...

    @staticmethod
    def CreateInstance(elementType: Type, length: int) -> Array:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def CreateInstance(elementType: Type, length1: int, length2: int, length3: int) -> Array:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def CreateInstance(elementType: Type, lengths: Array[int]) -> Array:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def CreateInstance(elementType: Type, lengths: Array[int]) -> Array:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def CreateInstance(elementType: Type, lengths: Array[int], lowerBounds: Array[int]) -> Array:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def CreateInstance(elementType: Type, length1: int, length2: int) -> Array:
        """Method docstring."""
        ...

    @staticmethod
    def Empty() -> Array[T]:
        """Method docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    @staticmethod
    def Exists(array: Array[T], match: Predicate[T]) -> bool:
        """Method docstring."""
        ...

    @staticmethod
    def Find(array: Array[T], match: Predicate[T]) -> T:
        """Method docstring."""
        ...

    @staticmethod
    def FindAll(array: Array[T], match: Predicate[T]) -> Array[T]:
        """Method docstring."""
        ...

    @staticmethod
    def FindIndex(array: Array[T], match: Predicate[T]) -> int:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def FindIndex(array: Array[T], startIndex: int, match: Predicate[T]) -> int:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def FindIndex(array: Array[T], startIndex: int, count: int, match: Predicate[T]) -> int:
        """Method docstring."""
        ...

    @staticmethod
    def FindLast(array: Array[T], match: Predicate[T]) -> T:
        """Method docstring."""
        ...

    @staticmethod
    def FindLastIndex(array: Array[T], match: Predicate[T]) -> int:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def FindLastIndex(array: Array[T], startIndex: int, match: Predicate[T]) -> int:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def FindLastIndex(array: Array[T], startIndex: int, count: int, match: Predicate[T]) -> int:
        """Method docstring."""
        ...

    @staticmethod
    def ForEach(array: Array[T], action: Action[T]) -> None:
        """Method docstring."""
        ...

    def GetEnumerator(self) -> IEnumerator:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetLength(self, dimension: int) -> int:
        """Method docstring."""
        ...

    def GetLongLength(self, dimension: int) -> int:
        """Method docstring."""
        ...

    def GetLowerBound(self, dimension: int) -> int:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def GetUpperBound(self, dimension: int) -> int:
        """Method docstring."""
        ...

    def GetValue(self, indices: Array[int]) -> Any:
        """Method docstring."""
        ...

    @overload
    def GetValue(self, index: int) -> Any:
        """Method docstring."""
        ...

    @overload
    def GetValue(self, index1: int, index2: int) -> Any:
        """Method docstring."""
        ...

    @overload
    def GetValue(self, index1: int, index2: int, index3: int) -> Any:
        """Method docstring."""
        ...

    @overload
    def GetValue(self, index: int) -> Any:
        """Method docstring."""
        ...

    @overload
    def GetValue(self, index1: int, index2: int) -> Any:
        """Method docstring."""
        ...

    @overload
    def GetValue(self, index1: int, index2: int, index3: int) -> Any:
        """Method docstring."""
        ...

    @overload
    def GetValue(self, indices: Array[int]) -> Any:
        """Method docstring."""
        ...

    @staticmethod
    def IndexOf(array: Array, value: Any) -> int:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def IndexOf(array: Array, value: Any, startIndex: int) -> int:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def IndexOf(array: Array, value: Any, startIndex: int, count: int) -> int:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def IndexOf(array: Array[T], value: T) -> int:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def IndexOf(array: Array[T], value: T, startIndex: int) -> int:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def IndexOf(array: Array[T], value: T, startIndex: int, count: int) -> int:
        """Method docstring."""
        ...

    def Initialize(self) -> None:
        """Method docstring."""
        ...

    @staticmethod
    def LastIndexOf(array: Array, value: Any) -> int:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def LastIndexOf(array: Array, value: Any, startIndex: int) -> int:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def LastIndexOf(array: Array, value: Any, startIndex: int, count: int) -> int:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def LastIndexOf(array: Array[T], value: T) -> int:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def LastIndexOf(array: Array[T], value: T, startIndex: int) -> int:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def LastIndexOf(array: Array[T], value: T, startIndex: int, count: int) -> int:
        """Method docstring."""
        ...

    @staticmethod
    def Resize(array: Array[T], newSize: int) -> None:
        """Method docstring."""
        ...

    @staticmethod
    def Reverse(array: Array) -> None:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Reverse(array: Array, index: int, length: int) -> None:
        """Method docstring."""
        ...

    def SetValue(self, value: Any, index: int) -> None:
        """Method docstring."""
        ...

    @overload
    def SetValue(self, value: Any, index1: int, index2: int) -> None:
        """Method docstring."""
        ...

    @overload
    def SetValue(self, value: Any, index1: int, index2: int, index3: int) -> None:
        """Method docstring."""
        ...

    @overload
    def SetValue(self, value: Any, indices: Array[int]) -> None:
        """Method docstring."""
        ...

    @overload
    def SetValue(self, value: Any, index: int) -> None:
        """Method docstring."""
        ...

    @overload
    def SetValue(self, value: Any, index1: int, index2: int) -> None:
        """Method docstring."""
        ...

    @overload
    def SetValue(self, value: Any, index1: int, index2: int, index3: int) -> None:
        """Method docstring."""
        ...

    @overload
    def SetValue(self, value: Any, indices: Array[int]) -> None:
        """Method docstring."""
        ...

    @staticmethod
    def Sort(array: Array) -> None:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Sort(keys: Array, items: Array) -> None:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Sort(array: Array, index: int, length: int) -> None:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Sort(keys: Array, items: Array, index: int, length: int) -> None:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Sort(array: Array, comparer: StringComparer) -> None:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Sort(keys: Array, items: Array, comparer: StringComparer) -> None:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Sort(array: Array, index: int, length: int, comparer: StringComparer) -> None:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Sort(array: Array[T]) -> None:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Sort(keys: Array[TKey], items: Array[TValue]) -> None:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Sort(array: Array[T], index: int, length: int) -> None:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Sort(keys: Array[TKey], items: Array[TValue], index: int, length: int) -> None:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Sort(array: Array[T], comparer: IComparer[T]) -> None:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Sort(keys: Array[TKey], items: Array[TValue], comparer: IComparer[TKey]) -> None:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Sort(array: Array[T], index: int, length: int, comparer: IComparer[T]) -> None:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Sort(keys: Array[TKey], items: Array[TValue], index: int, length: int, comparer: IComparer[TKey]) -> None:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Sort(array: Array[T], comparison: Comparison[T]) -> None:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Sort(keys: Array, items: Array, index: int, length: int, comparer: StringComparer) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    @staticmethod
    def TrueForAll(array: Array[T], match: Predicate[T]) -> bool:
        """Method docstring."""
        ...


class AsyncCallback(MulticastDelegate):
    """Class docstring."""

    def __init__(self, object: Any, method: IntPtr) -> None:
        """Initialize instance."""
        ...

    @property
    def Method(self) -> MethodInfo:
        """MethodInfo: Property docstring."""
        ...

    @property
    def Target(self) -> Any:
        """Any: Property docstring."""
        ...

    def BeginInvoke(self, ar: FileStreamAsyncResult, callback: AsyncCallback, object: Any) -> FileStreamAsyncResult:
        """Method docstring."""
        ...

    def Clone(self) -> Any:
        """Method docstring."""
        ...

    def DynamicInvoke(self, args: Array[Any]) -> Any:
        """Method docstring."""
        ...

    def EndInvoke(self, result: FileStreamAsyncResult) -> None:
        """Method docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetInvocationList(self) -> Array[Delegate]:
        """Method docstring."""
        ...

    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def Invoke(self, ar: FileStreamAsyncResult) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...


class Attribute:
    """Class docstring."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def TypeId(self) -> Any:
        """Any: Property docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    @staticmethod
    def GetCustomAttribute(element: MemberInfo, attributeType: Type) -> Attribute:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def GetCustomAttribute(element: MemberInfo, attributeType: Type, inherit: bool) -> Attribute:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def GetCustomAttribute(element: ParameterInfo, attributeType: Type) -> Attribute:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def GetCustomAttribute(element: ParameterInfo, attributeType: Type, inherit: bool) -> Attribute:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def GetCustomAttribute(element: Module, attributeType: Type) -> Attribute:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def GetCustomAttribute(element: Module, attributeType: Type, inherit: bool) -> Attribute:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def GetCustomAttribute(element: Assembly, attributeType: Type) -> Attribute:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def GetCustomAttribute(element: Assembly, attributeType: Type, inherit: bool) -> Attribute:
        """Method docstring."""
        ...

    @staticmethod
    def GetCustomAttributes(element: MemberInfo, type: Type) -> Array[Attribute]:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def GetCustomAttributes(element: MemberInfo, type: Type, inherit: bool) -> Array[Attribute]:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def GetCustomAttributes(element: MemberInfo) -> Array[Attribute]:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def GetCustomAttributes(element: MemberInfo, inherit: bool) -> Array[Attribute]:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def GetCustomAttributes(element: ParameterInfo) -> Array[Attribute]:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def GetCustomAttributes(element: ParameterInfo, attributeType: Type) -> Array[Attribute]:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def GetCustomAttributes(element: ParameterInfo, attributeType: Type, inherit: bool) -> Array[Attribute]:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def GetCustomAttributes(element: ParameterInfo, inherit: bool) -> Array[Attribute]:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def GetCustomAttributes(element: Module, attributeType: Type) -> Array[Attribute]:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def GetCustomAttributes(element: Module) -> Array[Attribute]:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def GetCustomAttributes(element: Module, inherit: bool) -> Array[Attribute]:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def GetCustomAttributes(element: Module, attributeType: Type, inherit: bool) -> Array[Attribute]:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def GetCustomAttributes(element: Assembly, attributeType: Type) -> Array[Attribute]:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def GetCustomAttributes(element: Assembly, attributeType: Type, inherit: bool) -> Array[Attribute]:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def GetCustomAttributes(element: Assembly) -> Array[Attribute]:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def GetCustomAttributes(element: Assembly, inherit: bool) -> Array[Attribute]:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def IsDefaultAttribute(self) -> bool:
        """Method docstring."""
        ...

    @staticmethod
    def IsDefined(element: MemberInfo, attributeType: Type) -> bool:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def IsDefined(element: MemberInfo, attributeType: Type, inherit: bool) -> bool:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def IsDefined(element: ParameterInfo, attributeType: Type) -> bool:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def IsDefined(element: ParameterInfo, attributeType: Type, inherit: bool) -> bool:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def IsDefined(element: Module, attributeType: Type) -> bool:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def IsDefined(element: Module, attributeType: Type, inherit: bool) -> bool:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def IsDefined(element: Assembly, attributeType: Type) -> bool:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def IsDefined(element: Assembly, attributeType: Type, inherit: bool) -> bool:
        """Method docstring."""
        ...

    def Match(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...


class Delegate:
    """Class docstring."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Method(self) -> MethodInfo:
        """MethodInfo: Property docstring."""
        ...

    @property
    def Target(self) -> Any:
        """Any: Property docstring."""
        ...

    def Clone(self) -> Any:
        """Method docstring."""
        ...

    @staticmethod
    def Combine(a: Delegate, b: Delegate) -> Delegate:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Combine(delegates: Array[Delegate]) -> Delegate:
        """Method docstring."""
        ...

    @staticmethod
    def CreateDelegate(type: Type, target: Any, method: str) -> Delegate:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def CreateDelegate(type: Type, target: Any, method: str, ignoreCase: bool) -> Delegate:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def CreateDelegate(type: Type, target: Any, method: str, ignoreCase: bool, throwOnBindFailure: bool) -> Delegate:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def CreateDelegate(type: Type, target: Type, method: str) -> Delegate:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def CreateDelegate(type: Type, target: Type, method: str, ignoreCase: bool) -> Delegate:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def CreateDelegate(type: Type, target: Type, method: str, ignoreCase: bool, throwOnBindFailure: bool) -> Delegate:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def CreateDelegate(type: Type, method: MethodInfo, throwOnBindFailure: bool) -> Delegate:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def CreateDelegate(type: Type, firstArgument: Any, method: MethodInfo, throwOnBindFailure: bool) -> Delegate:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def CreateDelegate(type: Type, method: MethodInfo) -> Delegate:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def CreateDelegate(type: Type, firstArgument: Any, method: MethodInfo) -> Delegate:
        """Method docstring."""
        ...

    def DynamicInvoke(self, args: Array[Any]) -> Any:
        """Method docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetInvocationList(self) -> Array[Delegate]:
        """Method docstring."""
        ...

    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    @staticmethod
    def Remove(source: Delegate, value: Delegate) -> Delegate:
        """Method docstring."""
        ...

    @staticmethod
    def RemoveAll(source: Delegate, value: Delegate) -> Delegate:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...


class Enum(ValueType):
    """Class docstring."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    def CompareTo(self, target: Any) -> int:
        """Method docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    @staticmethod
    def Format(enumType: Type, value: Any, format: str) -> str:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    @staticmethod
    def GetName(enumType: Type, value: Any) -> str:
        """Method docstring."""
        ...

    @staticmethod
    def GetNames(enumType: Type) -> Array[str]:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def GetTypeCode(self) -> TypeCode:
        """Method docstring."""
        ...

    @staticmethod
    def GetUnderlyingType(enumType: Type) -> Type:
        """Method docstring."""
        ...

    @staticmethod
    def GetValues(enumType: Type) -> Array:
        """Method docstring."""
        ...

    def HasFlag(self, flag: Enum) -> bool:
        """Method docstring."""
        ...

    @staticmethod
    def IsDefined(enumType: Type, value: Any) -> bool:
        """Method docstring."""
        ...

    @staticmethod
    def Parse(enumType: Type, value: str) -> Any:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Parse(enumType: Type, value: str, ignoreCase: bool) -> Any:
        """Method docstring."""
        ...

    @staticmethod
    def ToObject(enumType: Type, value: Any) -> Any:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def ToObject(enumType: Type, value: int) -> Any:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def ToObject(enumType: Type, value: int) -> Any:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def ToObject(enumType: Type, value: int) -> Any:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def ToObject(enumType: Type, value: int) -> Any:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def ToObject(enumType: Type, value: int) -> Any:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def ToObject(enumType: Type, value: int) -> Any:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def ToObject(enumType: Type, value: int) -> Any:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def ToObject(enumType: Type, value: int) -> Any:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    @overload
    def ToString(self, format: str, provider: CultureInfo) -> str:
        """Method docstring."""
        ...

    @overload
    def ToString(self, provider: CultureInfo) -> str:
        """Method docstring."""
        ...

    @overload
    def ToString(self, format: str) -> str:
        """Method docstring."""
        ...

    @staticmethod
    def TryParse(value: str, result: TEnum) -> bool:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def TryParse(value: str, ignoreCase: bool, result: TEnum) -> bool:
        """Method docstring."""
        ...


class Exception:
    """Class docstring."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, message: str) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
        """Initialize instance."""
        ...

    @property
    def Data(self) -> DictionaryBase:
        """DictionaryBase: Property docstring."""
        ...

    @property
    def HResult(self) -> int:
        """int: Property docstring."""
        ...

    @HResult.setter
    def HResult(self, value: int) -> None:
        """Set property value."""
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

    @overload
    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...


class IComparable:
    """Class docstring."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    def CompareTo(self, obj: Any) -> int:
        """Method docstring."""
        ...


class IntPtr(ValueType):
    """Class docstring."""

    def __init__(self, value: int) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, value: int) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, value: Any) -> None:
        """Initialize instance."""
        ...

    @classmethod
    @property
    def Size(cls) -> int:
        """int: Property docstring."""
        ...

    @staticmethod
    def Add(pointer: IntPtr, offset: int) -> IntPtr:
        """Method docstring."""
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

    @staticmethod
    def Subtract(pointer: IntPtr, offset: int) -> IntPtr:
        """Method docstring."""
        ...

    def ToInt32(self) -> int:
        """Method docstring."""
        ...

    def ToInt64(self) -> int:
        """Method docstring."""
        ...

    def ToPointer(self) -> Any:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    @overload
    def ToString(self, format: str) -> str:
        """Method docstring."""
        ...

    Zero: IntPtr

class MulticastDelegate(Delegate):
    """Class docstring."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Method(self) -> MethodInfo:
        """MethodInfo: Property docstring."""
        ...

    @property
    def Target(self) -> Any:
        """Any: Property docstring."""
        ...

    def Clone(self) -> Any:
        """Method docstring."""
        ...

    def DynamicInvoke(self, args: Array[Any]) -> Any:
        """Method docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetInvocationList(self) -> Array[Delegate]:
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


class Type(MemberInfo):
    """Class docstring."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Assembly(self) -> Assembly:
        """Assembly: Property docstring."""
        ...

    @property
    def AssemblyQualifiedName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Attributes(self) -> TypeAttributes:
        """TypeAttributes: Property docstring."""
        ...

    @property
    def BaseType(self) -> Type:
        """Type: Property docstring."""
        ...

    @property
    def ContainsGenericParameters(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def CustomAttributes(self) -> List[CustomAttributeData]:
        """List[CustomAttributeData]: Property docstring."""
        ...

    @property
    def DeclaringMethod(self) -> MethodBase:
        """MethodBase: Property docstring."""
        ...

    @property
    def DeclaringType(self) -> Type:
        """Type: Property docstring."""
        ...

    @classmethod
    @property
    def DefaultBinder(cls) -> Binder:
        """Binder: Property docstring."""
        ...

    @property
    def FullName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def GUID(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def GenericParameterAttributes(self) -> GenericParameterAttributes:
        """GenericParameterAttributes: Property docstring."""
        ...

    @property
    def GenericParameterPosition(self) -> int:
        """int: Property docstring."""
        ...

    @property
    def GenericTypeArguments(self) -> Array[Type]:
        """Array[Type]: Property docstring."""
        ...

    @property
    def HasElementType(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsAbstract(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsAnsiClass(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsArray(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsAutoClass(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsAutoLayout(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsByRef(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsCOMObject(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsClass(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsConstructedGenericType(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsContextful(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsEnum(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsExplicitLayout(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsGenericParameter(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsGenericType(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsGenericTypeDefinition(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsImport(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsInterface(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsLayoutSequential(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsMarshalByRef(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsNested(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsNestedAssembly(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsNestedFamANDAssem(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsNestedFamORAssem(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsNestedFamily(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsNestedPrivate(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsNestedPublic(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsNotPublic(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsPointer(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsPrimitive(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsPublic(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsSealed(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsSecurityCritical(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsSecuritySafeCritical(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsSecurityTransparent(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsSerializable(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsSpecialName(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsUnicodeClass(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsValueType(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsVisible(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def MemberType(self) -> MemberTypes:
        """MemberTypes: Property docstring."""
        ...

    @property
    def MetadataToken(self) -> int:
        """int: Property docstring."""
        ...

    @property
    def Module(self) -> Module:
        """Module: Property docstring."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Namespace(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def ReflectedType(self) -> Type:
        """Type: Property docstring."""
        ...

    @property
    def StructLayoutAttribute(self) -> StructLayoutAttribute:
        """StructLayoutAttribute: Property docstring."""
        ...

    @property
    def TypeHandle(self) -> RuntimeTypeHandle:
        """RuntimeTypeHandle: Property docstring."""
        ...

    @property
    def TypeInitializer(self) -> ConstructorInfo:
        """ConstructorInfo: Property docstring."""
        ...

    @property
    def UnderlyingSystemType(self) -> Type:
        """Type: Property docstring."""
        ...

    def Equals(self, o: Any) -> bool:
        """Method docstring."""
        ...

    @overload
    def Equals(self, o: Type) -> bool:
        """Method docstring."""
        ...

    def FindInterfaces(self, filter: TypeFilter, filterCriteria: Any) -> Array[Type]:
        """Method docstring."""
        ...

    def FindMembers(self, memberType: MemberTypes, bindingAttr: BindingFlags, filter: MemberFilter, filterCriteria: Any) -> Array[MemberInfo]:
        """Method docstring."""
        ...

    def GetArrayRank(self) -> int:
        """Method docstring."""
        ...

    def GetConstructor(self, bindingAttr: BindingFlags, binder: Binder, callConvention: CallingConventions, types: Array[Type], modifiers: Array[ParameterModifier]) -> ConstructorInfo:
        """Method docstring."""
        ...

    @overload
    def GetConstructor(self, bindingAttr: BindingFlags, binder: Binder, types: Array[Type], modifiers: Array[ParameterModifier]) -> ConstructorInfo:
        """Method docstring."""
        ...

    @overload
    def GetConstructor(self, types: Array[Type]) -> ConstructorInfo:
        """Method docstring."""
        ...

    def GetConstructors(self) -> Array[ConstructorInfo]:
        """Method docstring."""
        ...

    @overload
    def GetConstructors(self, bindingAttr: BindingFlags) -> Array[ConstructorInfo]:
        """Method docstring."""
        ...

    def GetCustomAttributes(self, inherit: bool) -> Array[Any]:
        """Method docstring."""
        ...

    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[Any]:
        """Method docstring."""
        ...

    def GetCustomAttributesData(self) -> List[CustomAttributeData]:
        """Method docstring."""
        ...

    def GetDefaultMembers(self) -> Array[MemberInfo]:
        """Method docstring."""
        ...

    def GetElementType(self) -> Type:
        """Method docstring."""
        ...

    def GetEnumName(self, value: Any) -> str:
        """Method docstring."""
        ...

    def GetEnumNames(self) -> Array[str]:
        """Method docstring."""
        ...

    def GetEnumUnderlyingType(self) -> Type:
        """Method docstring."""
        ...

    def GetEnumValues(self) -> Array:
        """Method docstring."""
        ...

    def GetEvent(self, name: str) -> EventInfo:
        """Method docstring."""
        ...

    @overload
    def GetEvent(self, name: str, bindingAttr: BindingFlags) -> EventInfo:
        """Method docstring."""
        ...

    def GetEvents(self) -> Array[EventInfo]:
        """Method docstring."""
        ...

    @overload
    def GetEvents(self, bindingAttr: BindingFlags) -> Array[EventInfo]:
        """Method docstring."""
        ...

    def GetField(self, name: str) -> FieldInfo:
        """Method docstring."""
        ...

    @overload
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """Method docstring."""
        ...

    def GetFields(self) -> Array[FieldInfo]:
        """Method docstring."""
        ...

    @overload
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """Method docstring."""
        ...

    def GetGenericArguments(self) -> Array[Type]:
        """Method docstring."""
        ...

    def GetGenericParameterConstraints(self) -> Array[Type]:
        """Method docstring."""
        ...

    def GetGenericTypeDefinition(self) -> Type:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetInterface(self, name: str) -> Type:
        """Method docstring."""
        ...

    @overload
    def GetInterface(self, name: str, ignoreCase: bool) -> Type:
        """Method docstring."""
        ...

    def GetInterfaceMap(self, interfaceType: Type) -> InterfaceMapping:
        """Method docstring."""
        ...

    def GetInterfaces(self) -> Array[Type]:
        """Method docstring."""
        ...

    def GetMember(self, name: str) -> Array[MemberInfo]:
        """Method docstring."""
        ...

    @overload
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """Method docstring."""
        ...

    @overload
    def GetMember(self, name: str, type: MemberTypes, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """Method docstring."""
        ...

    def GetMembers(self) -> Array[MemberInfo]:
        """Method docstring."""
        ...

    @overload
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """Method docstring."""
        ...

    def GetMethod(self, name: str, bindingAttr: BindingFlags, binder: Binder, callConvention: CallingConventions, types: Array[Type], modifiers: Array[ParameterModifier]) -> MethodInfo:
        """Method docstring."""
        ...

    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags, binder: Binder, types: Array[Type], modifiers: Array[ParameterModifier]) -> MethodInfo:
        """Method docstring."""
        ...

    @overload
    def GetMethod(self, name: str, types: Array[Type], modifiers: Array[ParameterModifier]) -> MethodInfo:
        """Method docstring."""
        ...

    @overload
    def GetMethod(self, name: str, types: Array[Type]) -> MethodInfo:
        """Method docstring."""
        ...

    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """Method docstring."""
        ...

    @overload
    def GetMethod(self, name: str) -> MethodInfo:
        """Method docstring."""
        ...

    def GetMethods(self) -> Array[MethodInfo]:
        """Method docstring."""
        ...

    @overload
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """Method docstring."""
        ...

    def GetNestedType(self, name: str) -> Type:
        """Method docstring."""
        ...

    @overload
    def GetNestedType(self, name: str, bindingAttr: BindingFlags) -> Type:
        """Method docstring."""
        ...

    def GetNestedTypes(self) -> Array[Type]:
        """Method docstring."""
        ...

    @overload
    def GetNestedTypes(self, bindingAttr: BindingFlags) -> Array[Type]:
        """Method docstring."""
        ...

    def GetProperties(self) -> Array[PropertyInfo]:
        """Method docstring."""
        ...

    @overload
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """Method docstring."""
        ...

    def GetProperty(self, name: str, bindingAttr: BindingFlags, binder: Binder, returnType: Type, types: Array[Type], modifiers: Array[ParameterModifier]) -> PropertyInfo:
        """Method docstring."""
        ...

    @overload
    def GetProperty(self, name: str, returnType: Type, types: Array[Type], modifiers: Array[ParameterModifier]) -> PropertyInfo:
        """Method docstring."""
        ...

    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """Method docstring."""
        ...

    @overload
    def GetProperty(self, name: str, returnType: Type, types: Array[Type]) -> PropertyInfo:
        """Method docstring."""
        ...

    @overload
    def GetProperty(self, name: str, types: Array[Type]) -> PropertyInfo:
        """Method docstring."""
        ...

    @overload
    def GetProperty(self, name: str, returnType: Type) -> PropertyInfo:
        """Method docstring."""
        ...

    @overload
    def GetProperty(self, name: str) -> PropertyInfo:
        """Method docstring."""
        ...

    @staticmethod
    def GetType(typeName: str, throwOnError: bool, ignoreCase: bool) -> Type:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def GetType(typeName: str, throwOnError: bool) -> Type:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def GetType(typeName: str) -> Type:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def GetType(typeName: str, assemblyResolver: Func[AssemblyName, Assembly], typeResolver: Func[Assembly, str, bool, Type]) -> Type:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def GetType(typeName: str, assemblyResolver: Func[AssemblyName, Assembly], typeResolver: Func[Assembly, str, bool, Type], throwOnError: bool) -> Type:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def GetType(typeName: str, assemblyResolver: Func[AssemblyName, Assembly], typeResolver: Func[Assembly, str, bool, Type], throwOnError: bool, ignoreCase: bool) -> Type:
        """Method docstring."""
        ...

    @overload
    def GetType(self) -> Type:
        """Method docstring."""
        ...

    @overload
    def GetType(self) -> Type:
        """Method docstring."""
        ...

    @staticmethod
    def GetTypeArray(args: Array[Any]) -> Array[Type]:
        """Method docstring."""
        ...

    @staticmethod
    def GetTypeCode(type: Type) -> TypeCode:
        """Method docstring."""
        ...

    @staticmethod
    def GetTypeFromCLSID(clsid: str) -> Type:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def GetTypeFromCLSID(clsid: str, throwOnError: bool) -> Type:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def GetTypeFromCLSID(clsid: str, server: str) -> Type:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def GetTypeFromCLSID(clsid: str, server: str, throwOnError: bool) -> Type:
        """Method docstring."""
        ...

    @staticmethod
    def GetTypeFromHandle(handle: RuntimeTypeHandle) -> Type:
        """Method docstring."""
        ...

    @staticmethod
    def GetTypeFromProgID(progID: str) -> Type:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def GetTypeFromProgID(progID: str, throwOnError: bool) -> Type:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def GetTypeFromProgID(progID: str, server: str) -> Type:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def GetTypeFromProgID(progID: str, server: str, throwOnError: bool) -> Type:
        """Method docstring."""
        ...

    @staticmethod
    def GetTypeHandle(o: Any) -> RuntimeTypeHandle:
        """Method docstring."""
        ...

    def InvokeMember(self, name: str, invokeAttr: BindingFlags, binder: Binder, target: Any, args: Array[Any], culture: CultureInfo) -> Any:
        """Method docstring."""
        ...

    @overload
    def InvokeMember(self, name: str, invokeAttr: BindingFlags, binder: Binder, target: Any, args: Array[Any]) -> Any:
        """Method docstring."""
        ...

    @overload
    def InvokeMember(self, name: str, invokeAttr: BindingFlags, binder: Binder, target: Any, args: Array[Any], modifiers: Array[ParameterModifier], culture: CultureInfo, namedParameters: Array[str]) -> Any:
        """Method docstring."""
        ...

    def IsAssignableFrom(self, c: Type) -> bool:
        """Method docstring."""
        ...

    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """Method docstring."""
        ...

    def IsEnumDefined(self, value: Any) -> bool:
        """Method docstring."""
        ...

    def IsEquivalentTo(self, other: Type) -> bool:
        """Method docstring."""
        ...

    def IsInstanceOfType(self, o: Any) -> bool:
        """Method docstring."""
        ...

    def IsSubclassOf(self, c: Type) -> bool:
        """Method docstring."""
        ...

    def MakeArrayType(self) -> Type:
        """Method docstring."""
        ...

    @overload
    def MakeArrayType(self, rank: int) -> Type:
        """Method docstring."""
        ...

    def MakeByRefType(self) -> Type:
        """Method docstring."""
        ...

    def MakeGenericType(self, typeArguments: Array[Type]) -> Type:
        """Method docstring."""
        ...

    def MakePointerType(self) -> Type:
        """Method docstring."""
        ...

    @staticmethod
    def ReflectionOnlyGetType(typeName: str, throwIfNotFound: bool, ignoreCase: bool) -> Type:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    Delimiter: Char
    EmptyTypes: Array[Type]
    FilterAttribute: MemberFilter
    FilterName: MemberFilter
    FilterNameIgnoreCase: MemberFilter
    Missing: Any

class TypeCode:
    """Class docstring."""

    Boolean: TypeCode
    Byte: TypeCode
    Char: TypeCode
    DBNull: TypeCode
    DateTime: TypeCode
    Decimal: TypeCode
    Double: TypeCode
    Empty: TypeCode
    Int16: TypeCode
    Int32: TypeCode
    Int64: TypeCode
    Object: TypeCode
    SByte: TypeCode
    Single: TypeCode
    String: TypeCode
    UInt16: TypeCode
    UInt32: TypeCode
    UInt64: TypeCode

class ValueType:
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

