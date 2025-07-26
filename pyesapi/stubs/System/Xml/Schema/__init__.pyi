from typing import Any, Dict, Generic, List, Optional, Union, overload
from datetime import datetime
from System import Array, Type
from System.Xml import XmlReader, XmlWriter

class XmlSchema(XmlSchemaObject):
    """Class docstring."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def AttributeFormDefault(self) -> XmlSchemaForm:
        """XmlSchemaForm: Property docstring."""
        ...

    @AttributeFormDefault.setter
    def AttributeFormDefault(self, value: XmlSchemaForm) -> None:
        """Set property value."""
        ...

    @property
    def AttributeGroups(self) -> XmlSchemaObjectTable:
        """XmlSchemaObjectTable: Property docstring."""
        ...

    @property
    def Attributes(self) -> XmlSchemaObjectTable:
        """XmlSchemaObjectTable: Property docstring."""
        ...

    @property
    def BlockDefault(self) -> XmlSchemaDerivationMethod:
        """XmlSchemaDerivationMethod: Property docstring."""
        ...

    @BlockDefault.setter
    def BlockDefault(self, value: XmlSchemaDerivationMethod) -> None:
        """Set property value."""
        ...

    @property
    def ElementFormDefault(self) -> XmlSchemaForm:
        """XmlSchemaForm: Property docstring."""
        ...

    @ElementFormDefault.setter
    def ElementFormDefault(self, value: XmlSchemaForm) -> None:
        """Set property value."""
        ...

    @property
    def Elements(self) -> XmlSchemaObjectTable:
        """XmlSchemaObjectTable: Property docstring."""
        ...

    @property
    def FinalDefault(self) -> XmlSchemaDerivationMethod:
        """XmlSchemaDerivationMethod: Property docstring."""
        ...

    @FinalDefault.setter
    def FinalDefault(self, value: XmlSchemaDerivationMethod) -> None:
        """Set property value."""
        ...

    @property
    def Groups(self) -> XmlSchemaObjectTable:
        """XmlSchemaObjectTable: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @Id.setter
    def Id(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def Includes(self) -> XmlSchemaObjectCollection:
        """XmlSchemaObjectCollection: Property docstring."""
        ...

    @property
    def IsCompiled(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def Items(self) -> XmlSchemaObjectCollection:
        """XmlSchemaObjectCollection: Property docstring."""
        ...

    @property
    def LineNumber(self) -> int:
        """int: Property docstring."""
        ...

    @LineNumber.setter
    def LineNumber(self, value: int) -> None:
        """Set property value."""
        ...

    @property
    def LinePosition(self) -> int:
        """int: Property docstring."""
        ...

    @LinePosition.setter
    def LinePosition(self, value: int) -> None:
        """Set property value."""
        ...

    @property
    def Namespaces(self) -> XmlSerializerNamespaces:
        """XmlSerializerNamespaces: Property docstring."""
        ...

    @Namespaces.setter
    def Namespaces(self, value: XmlSerializerNamespaces) -> None:
        """Set property value."""
        ...

    @property
    def Notations(self) -> XmlSchemaObjectTable:
        """XmlSchemaObjectTable: Property docstring."""
        ...

    @property
    def Parent(self) -> XmlSchemaObject:
        """XmlSchemaObject: Property docstring."""
        ...

    @Parent.setter
    def Parent(self, value: XmlSchemaObject) -> None:
        """Set property value."""
        ...

    @property
    def SchemaTypes(self) -> XmlSchemaObjectTable:
        """XmlSchemaObjectTable: Property docstring."""
        ...

    @property
    def SourceUri(self) -> str:
        """str: Property docstring."""
        ...

    @SourceUri.setter
    def SourceUri(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def TargetNamespace(self) -> str:
        """str: Property docstring."""
        ...

    @TargetNamespace.setter
    def TargetNamespace(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def UnhandledAttributes(self) -> Array[XmlAttribute]:
        """Array[XmlAttribute]: Property docstring."""
        ...

    @UnhandledAttributes.setter
    def UnhandledAttributes(self, value: Array[XmlAttribute]) -> None:
        """Set property value."""
        ...

    @property
    def Version(self) -> str:
        """str: Property docstring."""
        ...

    @Version.setter
    def Version(self, value: str) -> None:
        """Set property value."""
        ...

    def Compile(self, validationEventHandler: ValidationEventHandler, resolver: XmlResolver) -> None:
        """Method docstring."""
        ...

    @overload
    def Compile(self, validationEventHandler: ValidationEventHandler) -> None:
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
    def Read(reader: TextReader, validationEventHandler: ValidationEventHandler) -> XmlSchema:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Read(stream: Stream, validationEventHandler: ValidationEventHandler) -> XmlSchema:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Read(reader: XmlReader, validationEventHandler: ValidationEventHandler) -> XmlSchema:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    def Write(self, stream: Stream) -> None:
        """Method docstring."""
        ...

    @overload
    def Write(self, stream: Stream, namespaceManager: XmlNamespaceManager) -> None:
        """Method docstring."""
        ...

    @overload
    def Write(self, writer: TextWriter) -> None:
        """Method docstring."""
        ...

    @overload
    def Write(self, writer: TextWriter, namespaceManager: XmlNamespaceManager) -> None:
        """Method docstring."""
        ...

    @overload
    def Write(self, writer: XmlWriter) -> None:
        """Method docstring."""
        ...

    @overload
    def Write(self, writer: XmlWriter, namespaceManager: XmlNamespaceManager) -> None:
        """Method docstring."""
        ...

    InstanceNamespace: str
    Namespace: str
