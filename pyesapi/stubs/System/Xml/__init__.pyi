from typing import Any, Dict, Generic, List, Optional, Union, overload
from datetime import datetime
from System import Array, Type
from Microsoft.Win32 import RegistryKey
from System.Text import StringBuilder

class XmlReader:
    """Class docstring."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def AttributeCount(self) -> int:
        """int: Property docstring."""
        ...

    @property
    def BaseURI(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def CanReadBinaryContent(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def CanReadValueChunk(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def CanResolveEntity(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def Depth(self) -> int:
        """int: Property docstring."""
        ...

    @property
    def EOF(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def HasAttributes(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def HasValue(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsDefault(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsEmptyElement(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def Item(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def LocalName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def NameTable(self) -> XmlNameTable:
        """XmlNameTable: Property docstring."""
        ...

    @property
    def NamespaceURI(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def NodeType(self) -> XmlNodeType:
        """XmlNodeType: Property docstring."""
        ...

    @property
    def Prefix(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def QuoteChar(self) -> Char:
        """Char: Property docstring."""
        ...

    @property
    def ReadState(self) -> ReadState:
        """ReadState: Property docstring."""
        ...

    @property
    def SchemaInfo(self) -> XmlAsyncCheckReaderWithLineInfoNSSchema:
        """XmlAsyncCheckReaderWithLineInfoNSSchema: Property docstring."""
        ...

    @property
    def Settings(self) -> XmlReaderSettings:
        """XmlReaderSettings: Property docstring."""
        ...

    @property
    def Value(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def ValueType(self) -> Type:
        """Type: Property docstring."""
        ...

    @property
    def XmlLang(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def XmlSpace(self) -> XmlSpace:
        """XmlSpace: Property docstring."""
        ...

    def Close(self) -> None:
        """Method docstring."""
        ...

    @staticmethod
    def Create(inputUri: str) -> XmlReader:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Create(inputUri: str, settings: XmlReaderSettings) -> XmlReader:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Create(inputUri: str, settings: XmlReaderSettings, inputContext: XmlParserContext) -> XmlReader:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Create(input: Stream) -> XmlReader:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Create(input: Stream, settings: XmlReaderSettings) -> XmlReader:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Create(input: Stream, settings: XmlReaderSettings, baseUri: str) -> XmlReader:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Create(input: Stream, settings: XmlReaderSettings, inputContext: XmlParserContext) -> XmlReader:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Create(input: TextReader) -> XmlReader:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Create(input: TextReader, settings: XmlReaderSettings) -> XmlReader:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Create(input: TextReader, settings: XmlReaderSettings, baseUri: str) -> XmlReader:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Create(input: TextReader, settings: XmlReaderSettings, inputContext: XmlParserContext) -> XmlReader:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Create(reader: XmlReader, settings: XmlReaderSettings) -> XmlReader:
        """Method docstring."""
        ...

    def Dispose(self) -> None:
        """Method docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetAttribute(self, name: str) -> str:
        """Method docstring."""
        ...

    @overload
    def GetAttribute(self, name: str, namespaceURI: str) -> str:
        """Method docstring."""
        ...

    @overload
    def GetAttribute(self, i: int) -> str:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def GetValueAsync(self) -> Task[str]:
        """Method docstring."""
        ...

    @staticmethod
    def IsName(str: str) -> bool:
        """Method docstring."""
        ...

    @staticmethod
    def IsNameToken(str: str) -> bool:
        """Method docstring."""
        ...

    def IsStartElement(self) -> bool:
        """Method docstring."""
        ...

    @overload
    def IsStartElement(self, name: str) -> bool:
        """Method docstring."""
        ...

    @overload
    def IsStartElement(self, localname: str, ns: str) -> bool:
        """Method docstring."""
        ...

    def LookupNamespace(self, prefix: str) -> str:
        """Method docstring."""
        ...

    def MoveToAttribute(self, i: int) -> None:
        """Method docstring."""
        ...

    @overload
    def MoveToAttribute(self, name: str) -> bool:
        """Method docstring."""
        ...

    @overload
    def MoveToAttribute(self, name: str, ns: str) -> bool:
        """Method docstring."""
        ...

    def MoveToContent(self) -> XmlNodeType:
        """Method docstring."""
        ...

    def MoveToContentAsync(self) -> Task[XmlNodeType]:
        """Method docstring."""
        ...

    def MoveToElement(self) -> bool:
        """Method docstring."""
        ...

    def MoveToFirstAttribute(self) -> bool:
        """Method docstring."""
        ...

    def MoveToNextAttribute(self) -> bool:
        """Method docstring."""
        ...

    def Read(self) -> bool:
        """Method docstring."""
        ...

    def ReadAsync(self) -> Task[bool]:
        """Method docstring."""
        ...

    def ReadAttributeValue(self) -> bool:
        """Method docstring."""
        ...

    def ReadContentAs(self, returnType: Type, namespaceResolver: ConfigXmlReader) -> Any:
        """Method docstring."""
        ...

    def ReadContentAsAsync(self, returnType: Type, namespaceResolver: ConfigXmlReader) -> Task[Any]:
        """Method docstring."""
        ...

    def ReadContentAsBase64(self, buffer: Array[int], index: int, count: int) -> int:
        """Method docstring."""
        ...

    def ReadContentAsBase64Async(self, buffer: Array[int], index: int, count: int) -> Task[int]:
        """Method docstring."""
        ...

    def ReadContentAsBinHex(self, buffer: Array[int], index: int, count: int) -> int:
        """Method docstring."""
        ...

    def ReadContentAsBinHexAsync(self, buffer: Array[int], index: int, count: int) -> Task[int]:
        """Method docstring."""
        ...

    def ReadContentAsBoolean(self) -> bool:
        """Method docstring."""
        ...

    def ReadContentAsDateTime(self) -> datetime:
        """Method docstring."""
        ...

    def ReadContentAsDateTimeOffset(self) -> DateTimeOffset:
        """Method docstring."""
        ...

    def ReadContentAsDecimal(self) -> float:
        """Method docstring."""
        ...

    def ReadContentAsDouble(self) -> float:
        """Method docstring."""
        ...

    def ReadContentAsFloat(self) -> float:
        """Method docstring."""
        ...

    def ReadContentAsInt(self) -> int:
        """Method docstring."""
        ...

    def ReadContentAsLong(self) -> int:
        """Method docstring."""
        ...

    def ReadContentAsObject(self) -> Any:
        """Method docstring."""
        ...

    def ReadContentAsObjectAsync(self) -> Task[Any]:
        """Method docstring."""
        ...

    def ReadContentAsString(self) -> str:
        """Method docstring."""
        ...

    def ReadContentAsStringAsync(self) -> Task[str]:
        """Method docstring."""
        ...

    def ReadElementContentAs(self, returnType: Type, namespaceResolver: ConfigXmlReader, localName: str, namespaceURI: str) -> Any:
        """Method docstring."""
        ...

    @overload
    def ReadElementContentAs(self, returnType: Type, namespaceResolver: ConfigXmlReader) -> Any:
        """Method docstring."""
        ...

    def ReadElementContentAsAsync(self, returnType: Type, namespaceResolver: ConfigXmlReader) -> Task[Any]:
        """Method docstring."""
        ...

    def ReadElementContentAsBase64(self, buffer: Array[int], index: int, count: int) -> int:
        """Method docstring."""
        ...

    def ReadElementContentAsBase64Async(self, buffer: Array[int], index: int, count: int) -> Task[int]:
        """Method docstring."""
        ...

    def ReadElementContentAsBinHex(self, buffer: Array[int], index: int, count: int) -> int:
        """Method docstring."""
        ...

    def ReadElementContentAsBinHexAsync(self, buffer: Array[int], index: int, count: int) -> Task[int]:
        """Method docstring."""
        ...

    def ReadElementContentAsBoolean(self, localName: str, namespaceURI: str) -> bool:
        """Method docstring."""
        ...

    @overload
    def ReadElementContentAsBoolean(self) -> bool:
        """Method docstring."""
        ...

    def ReadElementContentAsDateTime(self, localName: str, namespaceURI: str) -> datetime:
        """Method docstring."""
        ...

    @overload
    def ReadElementContentAsDateTime(self) -> datetime:
        """Method docstring."""
        ...

    def ReadElementContentAsDecimal(self, localName: str, namespaceURI: str) -> float:
        """Method docstring."""
        ...

    @overload
    def ReadElementContentAsDecimal(self) -> float:
        """Method docstring."""
        ...

    def ReadElementContentAsDouble(self, localName: str, namespaceURI: str) -> float:
        """Method docstring."""
        ...

    @overload
    def ReadElementContentAsDouble(self) -> float:
        """Method docstring."""
        ...

    def ReadElementContentAsFloat(self, localName: str, namespaceURI: str) -> float:
        """Method docstring."""
        ...

    @overload
    def ReadElementContentAsFloat(self) -> float:
        """Method docstring."""
        ...

    def ReadElementContentAsInt(self, localName: str, namespaceURI: str) -> int:
        """Method docstring."""
        ...

    @overload
    def ReadElementContentAsInt(self) -> int:
        """Method docstring."""
        ...

    def ReadElementContentAsLong(self, localName: str, namespaceURI: str) -> int:
        """Method docstring."""
        ...

    @overload
    def ReadElementContentAsLong(self) -> int:
        """Method docstring."""
        ...

    def ReadElementContentAsObject(self, localName: str, namespaceURI: str) -> Any:
        """Method docstring."""
        ...

    @overload
    def ReadElementContentAsObject(self) -> Any:
        """Method docstring."""
        ...

    def ReadElementContentAsObjectAsync(self) -> Task[Any]:
        """Method docstring."""
        ...

    def ReadElementContentAsString(self, localName: str, namespaceURI: str) -> str:
        """Method docstring."""
        ...

    @overload
    def ReadElementContentAsString(self) -> str:
        """Method docstring."""
        ...

    def ReadElementContentAsStringAsync(self) -> Task[str]:
        """Method docstring."""
        ...

    def ReadElementString(self, name: str) -> str:
        """Method docstring."""
        ...

    @overload
    def ReadElementString(self) -> str:
        """Method docstring."""
        ...

    @overload
    def ReadElementString(self, localname: str, ns: str) -> str:
        """Method docstring."""
        ...

    def ReadEndElement(self) -> None:
        """Method docstring."""
        ...

    def ReadInnerXml(self) -> str:
        """Method docstring."""
        ...

    def ReadInnerXmlAsync(self) -> Task[str]:
        """Method docstring."""
        ...

    def ReadOuterXml(self) -> str:
        """Method docstring."""
        ...

    def ReadOuterXmlAsync(self) -> Task[str]:
        """Method docstring."""
        ...

    def ReadStartElement(self) -> None:
        """Method docstring."""
        ...

    @overload
    def ReadStartElement(self, name: str) -> None:
        """Method docstring."""
        ...

    @overload
    def ReadStartElement(self, localname: str, ns: str) -> None:
        """Method docstring."""
        ...

    def ReadString(self) -> str:
        """Method docstring."""
        ...

    def ReadSubtree(self) -> XmlReader:
        """Method docstring."""
        ...

    def ReadToDescendant(self, name: str) -> bool:
        """Method docstring."""
        ...

    @overload
    def ReadToDescendant(self, localName: str, namespaceURI: str) -> bool:
        """Method docstring."""
        ...

    def ReadToFollowing(self, name: str) -> bool:
        """Method docstring."""
        ...

    @overload
    def ReadToFollowing(self, localName: str, namespaceURI: str) -> bool:
        """Method docstring."""
        ...

    def ReadToNextSibling(self, name: str) -> bool:
        """Method docstring."""
        ...

    @overload
    def ReadToNextSibling(self, localName: str, namespaceURI: str) -> bool:
        """Method docstring."""
        ...

    def ReadValueChunk(self, buffer: Array[Char], index: int, count: int) -> int:
        """Method docstring."""
        ...

    def ReadValueChunkAsync(self, buffer: Array[Char], index: int, count: int) -> Task[int]:
        """Method docstring."""
        ...

    def ResolveEntity(self) -> None:
        """Method docstring."""
        ...

    def Skip(self) -> None:
        """Method docstring."""
        ...

    def SkipAsync(self) -> Task:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...


class XmlWriter:
    """Class docstring."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Settings(self) -> XmlWriterSettings:
        """XmlWriterSettings: Property docstring."""
        ...

    @property
    def WriteState(self) -> WriteState:
        """WriteState: Property docstring."""
        ...

    @property
    def XmlLang(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def XmlSpace(self) -> XmlSpace:
        """XmlSpace: Property docstring."""
        ...

    def Close(self) -> None:
        """Method docstring."""
        ...

    @staticmethod
    def Create(outputFileName: str) -> XmlWriter:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Create(outputFileName: str, settings: XmlWriterSettings) -> XmlWriter:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Create(output: Stream) -> XmlWriter:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Create(output: Stream, settings: XmlWriterSettings) -> XmlWriter:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Create(output: TextWriter) -> XmlWriter:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Create(output: TextWriter, settings: XmlWriterSettings) -> XmlWriter:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Create(output: StringBuilder) -> XmlWriter:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Create(output: StringBuilder, settings: XmlWriterSettings) -> XmlWriter:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Create(output: XmlWriter) -> XmlWriter:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Create(output: XmlWriter, settings: XmlWriterSettings) -> XmlWriter:
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

    def FlushAsync(self) -> Task:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def LookupPrefix(self, ns: str) -> str:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    def WriteAttributeString(self, localName: str, ns: str, value: str) -> None:
        """Method docstring."""
        ...

    @overload
    def WriteAttributeString(self, localName: str, value: str) -> None:
        """Method docstring."""
        ...

    @overload
    def WriteAttributeString(self, prefix: str, localName: str, ns: str, value: str) -> None:
        """Method docstring."""
        ...

    def WriteAttributeStringAsync(self, prefix: str, localName: str, ns: str, value: str) -> Task:
        """Method docstring."""
        ...

    def WriteAttributes(self, reader: XmlReader, defattr: bool) -> None:
        """Method docstring."""
        ...

    def WriteAttributesAsync(self, reader: XmlReader, defattr: bool) -> Task:
        """Method docstring."""
        ...

    def WriteBase64(self, buffer: Array[int], index: int, count: int) -> None:
        """Method docstring."""
        ...

    def WriteBase64Async(self, buffer: Array[int], index: int, count: int) -> Task:
        """Method docstring."""
        ...

    def WriteBinHex(self, buffer: Array[int], index: int, count: int) -> None:
        """Method docstring."""
        ...

    def WriteBinHexAsync(self, buffer: Array[int], index: int, count: int) -> Task:
        """Method docstring."""
        ...

    def WriteCData(self, text: str) -> None:
        """Method docstring."""
        ...

    def WriteCDataAsync(self, text: str) -> Task:
        """Method docstring."""
        ...

    def WriteCharEntity(self, ch: Char) -> None:
        """Method docstring."""
        ...

    def WriteCharEntityAsync(self, ch: Char) -> Task:
        """Method docstring."""
        ...

    def WriteChars(self, buffer: Array[Char], index: int, count: int) -> None:
        """Method docstring."""
        ...

    def WriteCharsAsync(self, buffer: Array[Char], index: int, count: int) -> Task:
        """Method docstring."""
        ...

    def WriteComment(self, text: str) -> None:
        """Method docstring."""
        ...

    def WriteCommentAsync(self, text: str) -> Task:
        """Method docstring."""
        ...

    def WriteDocType(self, name: str, pubid: str, sysid: str, subset: str) -> None:
        """Method docstring."""
        ...

    def WriteDocTypeAsync(self, name: str, pubid: str, sysid: str, subset: str) -> Task:
        """Method docstring."""
        ...

    def WriteElementString(self, localName: str, value: str) -> None:
        """Method docstring."""
        ...

    @overload
    def WriteElementString(self, localName: str, ns: str, value: str) -> None:
        """Method docstring."""
        ...

    @overload
    def WriteElementString(self, prefix: str, localName: str, ns: str, value: str) -> None:
        """Method docstring."""
        ...

    def WriteElementStringAsync(self, prefix: str, localName: str, ns: str, value: str) -> Task:
        """Method docstring."""
        ...

    def WriteEndAttribute(self) -> None:
        """Method docstring."""
        ...

    def WriteEndDocument(self) -> None:
        """Method docstring."""
        ...

    def WriteEndDocumentAsync(self) -> Task:
        """Method docstring."""
        ...

    def WriteEndElement(self) -> None:
        """Method docstring."""
        ...

    def WriteEndElementAsync(self) -> Task:
        """Method docstring."""
        ...

    def WriteEntityRef(self, name: str) -> None:
        """Method docstring."""
        ...

    def WriteEntityRefAsync(self, name: str) -> Task:
        """Method docstring."""
        ...

    def WriteFullEndElement(self) -> None:
        """Method docstring."""
        ...

    def WriteFullEndElementAsync(self) -> Task:
        """Method docstring."""
        ...

    def WriteName(self, name: str) -> None:
        """Method docstring."""
        ...

    def WriteNameAsync(self, name: str) -> Task:
        """Method docstring."""
        ...

    def WriteNmToken(self, name: str) -> None:
        """Method docstring."""
        ...

    def WriteNmTokenAsync(self, name: str) -> Task:
        """Method docstring."""
        ...

    def WriteNode(self, navigator: XPathNavigator, defattr: bool) -> None:
        """Method docstring."""
        ...

    @overload
    def WriteNode(self, reader: XmlReader, defattr: bool) -> None:
        """Method docstring."""
        ...

    def WriteNodeAsync(self, reader: XmlReader, defattr: bool) -> Task:
        """Method docstring."""
        ...

    @overload
    def WriteNodeAsync(self, navigator: XPathNavigator, defattr: bool) -> Task:
        """Method docstring."""
        ...

    def WriteProcessingInstruction(self, name: str, text: str) -> None:
        """Method docstring."""
        ...

    def WriteProcessingInstructionAsync(self, name: str, text: str) -> Task:
        """Method docstring."""
        ...

    def WriteQualifiedName(self, localName: str, ns: str) -> None:
        """Method docstring."""
        ...

    def WriteQualifiedNameAsync(self, localName: str, ns: str) -> Task:
        """Method docstring."""
        ...

    def WriteRaw(self, buffer: Array[Char], index: int, count: int) -> None:
        """Method docstring."""
        ...

    @overload
    def WriteRaw(self, data: str) -> None:
        """Method docstring."""
        ...

    def WriteRawAsync(self, buffer: Array[Char], index: int, count: int) -> Task:
        """Method docstring."""
        ...

    @overload
    def WriteRawAsync(self, data: str) -> Task:
        """Method docstring."""
        ...

    def WriteStartAttribute(self, localName: str, ns: str) -> None:
        """Method docstring."""
        ...

    @overload
    def WriteStartAttribute(self, localName: str) -> None:
        """Method docstring."""
        ...

    @overload
    def WriteStartAttribute(self, prefix: str, localName: str, ns: str) -> None:
        """Method docstring."""
        ...

    def WriteStartDocument(self) -> None:
        """Method docstring."""
        ...

    @overload
    def WriteStartDocument(self, standalone: bool) -> None:
        """Method docstring."""
        ...

    def WriteStartDocumentAsync(self) -> Task:
        """Method docstring."""
        ...

    @overload
    def WriteStartDocumentAsync(self, standalone: bool) -> Task:
        """Method docstring."""
        ...

    def WriteStartElement(self, localName: str, ns: str) -> None:
        """Method docstring."""
        ...

    @overload
    def WriteStartElement(self, localName: str) -> None:
        """Method docstring."""
        ...

    @overload
    def WriteStartElement(self, prefix: str, localName: str, ns: str) -> None:
        """Method docstring."""
        ...

    def WriteStartElementAsync(self, prefix: str, localName: str, ns: str) -> Task:
        """Method docstring."""
        ...

    def WriteString(self, text: str) -> None:
        """Method docstring."""
        ...

    def WriteStringAsync(self, text: str) -> Task:
        """Method docstring."""
        ...

    def WriteSurrogateCharEntity(self, lowChar: Char, highChar: Char) -> None:
        """Method docstring."""
        ...

    def WriteSurrogateCharEntityAsync(self, lowChar: Char, highChar: Char) -> Task:
        """Method docstring."""
        ...

    def WriteValue(self, value: Any) -> None:
        """Method docstring."""
        ...

    @overload
    def WriteValue(self, value: str) -> None:
        """Method docstring."""
        ...

    @overload
    def WriteValue(self, value: datetime) -> None:
        """Method docstring."""
        ...

    @overload
    def WriteValue(self, value: DateTimeOffset) -> None:
        """Method docstring."""
        ...

    @overload
    def WriteValue(self, value: float) -> None:
        """Method docstring."""
        ...

    @overload
    def WriteValue(self, value: float) -> None:
        """Method docstring."""
        ...

    @overload
    def WriteValue(self, value: float) -> None:
        """Method docstring."""
        ...

    @overload
    def WriteValue(self, value: int) -> None:
        """Method docstring."""
        ...

    @overload
    def WriteValue(self, value: int) -> None:
        """Method docstring."""
        ...

    @overload
    def WriteValue(self, value: bool) -> None:
        """Method docstring."""
        ...

    def WriteWhitespace(self, ws: str) -> None:
        """Method docstring."""
        ...

    def WriteWhitespaceAsync(self, ws: str) -> Task:
        """Method docstring."""
        ...

