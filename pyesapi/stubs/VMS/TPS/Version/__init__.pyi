from typing import Any, Dict, Generic, List, Optional, Union, overload
from datetime import datetime
from System import Type

class VersionInfo:
    """This class is a set of constants that specify build version information. Generated automatically from TpsNetVersion.in - do not edit by hand. The logic is copied from the VFC equivalents in TpsVersion.in. Names and identifiers are kept exactly the same as in the original VFC version to help in maintenance."""

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

    CORE_BUILD_STRING: str
    CORE_CHANGESET: str
    CORE_COMPANY_NAME: str
    CORE_EDITION_STRING: str
    CORE_FILE_VERSION_STRING: str
    CORE_LEGAL_COPYRIGHT: str
    CORE_LEGAL_TRADEMARKS: str
    CORE_PRODUCT_NAME: str
    CORE_PRODUCT_VERSION_NUMERIC: str
    CORE_PRODUCT_VERSION_STRING: str
    CORE_TPSNET_INTERFACE_VERSION_STRING: str
    CORE_TPSNET_SERVICES_INTERFACE_VERSION_STRING: str
    CORE_VERSION_BUILD: str
    CORE_VERSION_MAJOR: str
    CORE_VERSION_MICRO: str
    CORE_VERSION_MINOR: str
    CORE_VERSION_STRING: str
    CORE_YEAR: str
    CORE_YEAR_STRING: str
