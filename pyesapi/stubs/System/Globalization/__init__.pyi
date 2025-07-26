from typing import Any, Dict, Generic, List, Optional, Union, overload
from datetime import datetime
from System import Array, Type

class CultureInfo:
    """Class docstring."""

    def __init__(self, name: str) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, name: str, useUserOverride: bool) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, culture: int) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, culture: int, useUserOverride: bool) -> None:
        """Initialize instance."""
        ...

    @property
    def Calendar(self) -> Calendar:
        """Calendar: Property docstring."""
        ...

    @property
    def CompareInfo(self) -> CompareInfo:
        """CompareInfo: Property docstring."""
        ...

    @property
    def CultureTypes(self) -> CultureTypes:
        """CultureTypes: Property docstring."""
        ...

    @classmethod
    @property
    def CurrentCulture(cls) -> CultureInfo:
        """CultureInfo: Property docstring."""
        ...

    @classmethod
    @CurrentCulture.setter
    def CurrentCulture(cls, value: CultureInfo) -> None:
        """Set property value."""
        ...

    @classmethod
    @property
    def CurrentUICulture(cls) -> CultureInfo:
        """CultureInfo: Property docstring."""
        ...

    @classmethod
    @CurrentUICulture.setter
    def CurrentUICulture(cls, value: CultureInfo) -> None:
        """Set property value."""
        ...

    @property
    def DateTimeFormat(self) -> DateTimeFormatInfo:
        """DateTimeFormatInfo: Property docstring."""
        ...

    @DateTimeFormat.setter
    def DateTimeFormat(self, value: DateTimeFormatInfo) -> None:
        """Set property value."""
        ...

    @classmethod
    @property
    def DefaultThreadCurrentCulture(cls) -> CultureInfo:
        """CultureInfo: Property docstring."""
        ...

    @classmethod
    @DefaultThreadCurrentCulture.setter
    def DefaultThreadCurrentCulture(cls, value: CultureInfo) -> None:
        """Set property value."""
        ...

    @classmethod
    @property
    def DefaultThreadCurrentUICulture(cls) -> CultureInfo:
        """CultureInfo: Property docstring."""
        ...

    @classmethod
    @DefaultThreadCurrentUICulture.setter
    def DefaultThreadCurrentUICulture(cls, value: CultureInfo) -> None:
        """Set property value."""
        ...

    @property
    def DisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def EnglishName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def IetfLanguageTag(self) -> str:
        """str: Property docstring."""
        ...

    @classmethod
    @property
    def InstalledUICulture(cls) -> CultureInfo:
        """CultureInfo: Property docstring."""
        ...

    @classmethod
    @property
    def InvariantCulture(cls) -> CultureInfo:
        """CultureInfo: Property docstring."""
        ...

    @property
    def IsNeutralCulture(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsReadOnly(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def KeyboardLayoutId(self) -> int:
        """int: Property docstring."""
        ...

    @property
    def LCID(self) -> int:
        """int: Property docstring."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def NativeName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def NumberFormat(self) -> NumberFormatInfo:
        """NumberFormatInfo: Property docstring."""
        ...

    @NumberFormat.setter
    def NumberFormat(self, value: NumberFormatInfo) -> None:
        """Set property value."""
        ...

    @property
    def OptionalCalendars(self) -> Array[Calendar]:
        """Array[Calendar]: Property docstring."""
        ...

    @property
    def Parent(self) -> CultureInfo:
        """CultureInfo: Property docstring."""
        ...

    @property
    def TextInfo(self) -> TextInfo:
        """TextInfo: Property docstring."""
        ...

    @property
    def ThreeLetterISOLanguageName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def ThreeLetterWindowsLanguageName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def TwoLetterISOLanguageName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def UseUserOverride(self) -> bool:
        """bool: Property docstring."""
        ...

    def ClearCachedData(self) -> None:
        """Method docstring."""
        ...

    def Clone(self) -> Any:
        """Method docstring."""
        ...

    @staticmethod
    def CreateSpecificCulture(name: str) -> CultureInfo:
        """Method docstring."""
        ...

    def Equals(self, value: Any) -> bool:
        """Method docstring."""
        ...

    def GetConsoleFallbackUICulture(self) -> CultureInfo:
        """Method docstring."""
        ...

    @staticmethod
    def GetCultureInfo(culture: int) -> CultureInfo:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def GetCultureInfo(name: str) -> CultureInfo:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def GetCultureInfo(name: str, altName: str) -> CultureInfo:
        """Method docstring."""
        ...

    @staticmethod
    def GetCultureInfoByIetfLanguageTag(name: str) -> CultureInfo:
        """Method docstring."""
        ...

    @staticmethod
    def GetCultures(types: CultureTypes) -> Array[CultureInfo]:
        """Method docstring."""
        ...

    def GetFormat(self, formatType: Type) -> Any:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    @staticmethod
    def ReadOnly(ci: CultureInfo) -> CultureInfo:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

