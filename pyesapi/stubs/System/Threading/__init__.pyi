from typing import Any, Dict, Generic, List, Optional, Union, overload
from datetime import datetime
from System import Array, MulticastDelegate, Type
from System import AggregateException, AsyncCallback, Delegate, IntPtr
from System.IO import FileStreamAsyncResult
from System.Reflection import MethodInfo
from System.Runtime.Serialization import SerializationInfo, StreamingContext

class SendOrPostCallback(MulticastDelegate):
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

    def BeginInvoke(self, state: Any, callback: AsyncCallback, object: Any) -> FileStreamAsyncResult:
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

    def Invoke(self, state: Any) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...


class SynchronizationContext:
    """Class docstring."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @classmethod
    @property
    def Current(cls) -> SynchronizationContext:
        """SynchronizationContext: Property docstring."""
        ...

    def CreateCopy(self) -> SynchronizationContext:
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

    def IsWaitNotificationRequired(self) -> bool:
        """Method docstring."""
        ...

    def OperationCompleted(self) -> None:
        """Method docstring."""
        ...

    def OperationStarted(self) -> None:
        """Method docstring."""
        ...

    def Post(self, d: SendOrPostCallback, state: Any) -> None:
        """Method docstring."""
        ...

    def Send(self, d: SendOrPostCallback, state: Any) -> None:
        """Method docstring."""
        ...

    @staticmethod
    def SetSynchronizationContext(syncContext: SynchronizationContext) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    def Wait(self, waitHandles: Array[IntPtr], waitAll: bool, millisecondsTimeout: int) -> int:
        """Method docstring."""
        ...

