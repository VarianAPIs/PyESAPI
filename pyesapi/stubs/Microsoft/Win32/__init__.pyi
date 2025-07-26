from typing import Any, Dict, Generic, List, Optional, Union, overload
from datetime import datetime
from System import Array, Enum, Type
from System import TypeCode
from System.Globalization import CultureInfo

class Color:
    """Class docstring."""

    BackgroundBlue: Color
    BackgroundGreen: Color
    BackgroundIntensity: Color
    BackgroundMask: Color
    BackgroundRed: Color
    BackgroundYellow: Color
    Black: Color
    ColorMask: Color
    ForegroundBlue: Color
    ForegroundGreen: Color
    ForegroundIntensity: Color
    ForegroundMask: Color
    ForegroundRed: Color
    ForegroundYellow: Color

class RegistryHive:
    """Class docstring."""

    ClassesRoot: RegistryHive
    CurrentConfig: RegistryHive
    CurrentUser: RegistryHive
    DynData: RegistryHive
    LocalMachine: RegistryHive
    PerformanceData: RegistryHive
    Users: RegistryHive

class RegistryKey(MarshalByRefObject):
    """Class docstring."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Handle(self) -> SafeRegistryHandle:
        """SafeRegistryHandle: Property docstring."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def SubKeyCount(self) -> int:
        """int: Property docstring."""
        ...

    @property
    def ValueCount(self) -> int:
        """int: Property docstring."""
        ...

    @property
    def View(self) -> RegistryView:
        """RegistryView: Property docstring."""
        ...

    def Close(self) -> None:
        """Method docstring."""
        ...

    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """Method docstring."""
        ...

    def CreateSubKey(self, subkey: str) -> RegistryKey:
        """Method docstring."""
        ...

    @overload
    def CreateSubKey(self, subkey: str, permissionCheck: RegistryKeyPermissionCheck) -> RegistryKey:
        """Method docstring."""
        ...

    @overload
    def CreateSubKey(self, subkey: str, permissionCheck: RegistryKeyPermissionCheck, options: RegistryOptions) -> RegistryKey:
        """Method docstring."""
        ...

    @overload
    def CreateSubKey(self, subkey: str, writable: bool) -> RegistryKey:
        """Method docstring."""
        ...

    @overload
    def CreateSubKey(self, subkey: str, writable: bool, options: RegistryOptions) -> RegistryKey:
        """Method docstring."""
        ...

    @overload
    def CreateSubKey(self, subkey: str, permissionCheck: RegistryKeyPermissionCheck, registrySecurity: RegistrySecurity) -> RegistryKey:
        """Method docstring."""
        ...

    @overload
    def CreateSubKey(self, subkey: str, permissionCheck: RegistryKeyPermissionCheck, registryOptions: RegistryOptions, registrySecurity: RegistrySecurity) -> RegistryKey:
        """Method docstring."""
        ...

    def DeleteSubKey(self, subkey: str) -> None:
        """Method docstring."""
        ...

    @overload
    def DeleteSubKey(self, subkey: str, throwOnMissingSubKey: bool) -> None:
        """Method docstring."""
        ...

    def DeleteSubKeyTree(self, subkey: str) -> None:
        """Method docstring."""
        ...

    @overload
    def DeleteSubKeyTree(self, subkey: str, throwOnMissingSubKey: bool) -> None:
        """Method docstring."""
        ...

    def DeleteValue(self, name: str) -> None:
        """Method docstring."""
        ...

    @overload
    def DeleteValue(self, name: str, throwOnMissingValue: bool) -> None:
        """Method docstring."""
        ...

    def Dispose(self) -> None:
        """Method docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def Flush(self) -> None:
        """Method docstring."""
        ...

    @staticmethod
    def FromHandle(handle: SafeRegistryHandle) -> RegistryKey:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def FromHandle(handle: SafeRegistryHandle, view: RegistryView) -> RegistryKey:
        """Method docstring."""
        ...

    def GetAccessControl(self) -> RegistrySecurity:
        """Method docstring."""
        ...

    @overload
    def GetAccessControl(self, includeSections: AccessControlSections) -> RegistrySecurity:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetLifetimeService(self) -> Any:
        """Method docstring."""
        ...

    def GetSubKeyNames(self) -> Array[str]:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def GetValue(self, name: str) -> Any:
        """Method docstring."""
        ...

    @overload
    def GetValue(self, name: str, defaultValue: Any) -> Any:
        """Method docstring."""
        ...

    @overload
    def GetValue(self, name: str, defaultValue: Any, options: RegistryValueOptions) -> Any:
        """Method docstring."""
        ...

    def GetValueKind(self, name: str) -> RegistryValueKind:
        """Method docstring."""
        ...

    def GetValueNames(self) -> Array[str]:
        """Method docstring."""
        ...

    def InitializeLifetimeService(self) -> Any:
        """Method docstring."""
        ...

    @staticmethod
    def OpenBaseKey(hKey: RegistryHive, view: RegistryView) -> RegistryKey:
        """Method docstring."""
        ...

    @staticmethod
    def OpenRemoteBaseKey(hKey: RegistryHive, machineName: str) -> RegistryKey:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def OpenRemoteBaseKey(hKey: RegistryHive, machineName: str, view: RegistryView) -> RegistryKey:
        """Method docstring."""
        ...

    def OpenSubKey(self, name: str, writable: bool) -> RegistryKey:
        """Method docstring."""
        ...

    @overload
    def OpenSubKey(self, name: str, permissionCheck: RegistryKeyPermissionCheck) -> RegistryKey:
        """Method docstring."""
        ...

    @overload
    def OpenSubKey(self, name: str, rights: RegistryRights) -> RegistryKey:
        """Method docstring."""
        ...

    @overload
    def OpenSubKey(self, name: str, permissionCheck: RegistryKeyPermissionCheck, rights: RegistryRights) -> RegistryKey:
        """Method docstring."""
        ...

    @overload
    def OpenSubKey(self, name: str) -> RegistryKey:
        """Method docstring."""
        ...

    def SetAccessControl(self, registrySecurity: RegistrySecurity) -> None:
        """Method docstring."""
        ...

    def SetValue(self, name: str, value: Any) -> None:
        """Method docstring."""
        ...

    @overload
    def SetValue(self, name: str, value: Any, valueKind: RegistryValueKind) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

