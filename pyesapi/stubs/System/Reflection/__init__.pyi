from typing import Any, Dict, Generic, List, Optional, Union, overload
from datetime import datetime
from System import Array, Type
from System import AggregateException, Delegate
from System.Globalization import CultureInfo
from System.Runtime.Serialization import SerializationInfo, StreamingContext

class Assembly:
    """Class docstring."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def CodeBase(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def CustomAttributes(self) -> List[CustomAttributeData]:
        """List[CustomAttributeData]: Property docstring."""
        ...

    @property
    def DefinedTypes(self) -> List[TypeInfo]:
        """List[TypeInfo]: Property docstring."""
        ...

    @property
    def EntryPoint(self) -> MethodInfo:
        """MethodInfo: Property docstring."""
        ...

    @property
    def EscapedCodeBase(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Evidence(self) -> Evidence:
        """Evidence: Property docstring."""
        ...

    @property
    def ExportedTypes(self) -> List[Type]:
        """List[Type]: Property docstring."""
        ...

    @property
    def FullName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def GlobalAssemblyCache(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def HostContext(self) -> int:
        """int: Property docstring."""
        ...

    @property
    def ImageRuntimeVersion(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def IsDynamic(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsFullyTrusted(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def Location(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def ManifestModule(self) -> Module:
        """Module: Property docstring."""
        ...

    @property
    def Modules(self) -> List[Module]:
        """List[Module]: Property docstring."""
        ...

    @property
    def PermissionSet(self) -> PermissionSet:
        """PermissionSet: Property docstring."""
        ...

    @property
    def ReflectionOnly(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def SecurityRuleSet(self) -> SecurityRuleSet:
        """SecurityRuleSet: Property docstring."""
        ...

    def CreateInstance(self, typeName: str) -> Any:
        """Method docstring."""
        ...

    @overload
    def CreateInstance(self, typeName: str, ignoreCase: bool) -> Any:
        """Method docstring."""
        ...

    @overload
    def CreateInstance(self, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array[Any], culture: CultureInfo, activationAttributes: Array[Any]) -> Any:
        """Method docstring."""
        ...

    @staticmethod
    def CreateQualifiedName(assemblyName: str, typeName: str) -> str:
        """Method docstring."""
        ...

    def Equals(self, o: Any) -> bool:
        """Method docstring."""
        ...

    @staticmethod
    def GetAssembly(type: Type) -> Assembly:
        """Method docstring."""
        ...

    @staticmethod
    def GetCallingAssembly() -> Assembly:
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

    @staticmethod
    def GetEntryAssembly() -> Assembly:
        """Method docstring."""
        ...

    @staticmethod
    def GetExecutingAssembly() -> Assembly:
        """Method docstring."""
        ...

    def GetExportedTypes(self) -> Array[Type]:
        """Method docstring."""
        ...

    def GetFile(self, name: str) -> FileStream:
        """Method docstring."""
        ...

    def GetFiles(self) -> Array[FileStream]:
        """Method docstring."""
        ...

    @overload
    def GetFiles(self, getResourceModules: bool) -> Array[FileStream]:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetLoadedModules(self) -> Array[Module]:
        """Method docstring."""
        ...

    @overload
    def GetLoadedModules(self, getResourceModules: bool) -> Array[Module]:
        """Method docstring."""
        ...

    def GetManifestResourceInfo(self, resourceName: str) -> ManifestResourceInfo:
        """Method docstring."""
        ...

    def GetManifestResourceNames(self) -> Array[str]:
        """Method docstring."""
        ...

    def GetManifestResourceStream(self, type: Type, name: str) -> Stream:
        """Method docstring."""
        ...

    @overload
    def GetManifestResourceStream(self, name: str) -> Stream:
        """Method docstring."""
        ...

    def GetModule(self, name: str) -> Module:
        """Method docstring."""
        ...

    def GetModules(self) -> Array[Module]:
        """Method docstring."""
        ...

    @overload
    def GetModules(self, getResourceModules: bool) -> Array[Module]:
        """Method docstring."""
        ...

    def GetName(self) -> AssemblyName:
        """Method docstring."""
        ...

    @overload
    def GetName(self, copiedName: bool) -> AssemblyName:
        """Method docstring."""
        ...

    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """Method docstring."""
        ...

    def GetReferencedAssemblies(self) -> Array[AssemblyName]:
        """Method docstring."""
        ...

    def GetSatelliteAssembly(self, culture: CultureInfo) -> Assembly:
        """Method docstring."""
        ...

    @overload
    def GetSatelliteAssembly(self, culture: CultureInfo, version: Version) -> Assembly:
        """Method docstring."""
        ...

    def GetType(self, name: str) -> Type:
        """Method docstring."""
        ...

    @overload
    def GetType(self, name: str, throwOnError: bool) -> Type:
        """Method docstring."""
        ...

    @overload
    def GetType(self, name: str, throwOnError: bool, ignoreCase: bool) -> Type:
        """Method docstring."""
        ...

    @overload
    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def GetTypes(self) -> Array[Type]:
        """Method docstring."""
        ...

    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """Method docstring."""
        ...

    @staticmethod
    def Load(assemblyString: str) -> Assembly:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Load(assemblyString: str, assemblySecurity: Evidence) -> Assembly:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Load(assemblyRef: AssemblyName) -> Assembly:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Load(assemblyRef: AssemblyName, assemblySecurity: Evidence) -> Assembly:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Load(rawAssembly: Array[int]) -> Assembly:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Load(rawAssembly: Array[int], rawSymbolStore: Array[int]) -> Assembly:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Load(rawAssembly: Array[int], rawSymbolStore: Array[int], securityContextSource: SecurityContextSource) -> Assembly:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def Load(rawAssembly: Array[int], rawSymbolStore: Array[int], securityEvidence: Evidence) -> Assembly:
        """Method docstring."""
        ...

    @staticmethod
    def LoadFile(path: str) -> Assembly:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def LoadFile(path: str, securityEvidence: Evidence) -> Assembly:
        """Method docstring."""
        ...

    @staticmethod
    def LoadFrom(assemblyFile: str) -> Assembly:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def LoadFrom(assemblyFile: str, securityEvidence: Evidence) -> Assembly:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def LoadFrom(assemblyFile: str, securityEvidence: Evidence, hashValue: Array[int], hashAlgorithm: AssemblyHashAlgorithm) -> Assembly:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def LoadFrom(assemblyFile: str, hashValue: Array[int], hashAlgorithm: AssemblyHashAlgorithm) -> Assembly:
        """Method docstring."""
        ...

    def LoadModule(self, moduleName: str, rawModule: Array[int]) -> Module:
        """Method docstring."""
        ...

    @overload
    def LoadModule(self, moduleName: str, rawModule: Array[int], rawSymbolStore: Array[int]) -> Module:
        """Method docstring."""
        ...

    @staticmethod
    def LoadWithPartialName(partialName: str) -> Assembly:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def LoadWithPartialName(partialName: str, securityEvidence: Evidence) -> Assembly:
        """Method docstring."""
        ...

    @staticmethod
    def ReflectionOnlyLoad(assemblyString: str) -> Assembly:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def ReflectionOnlyLoad(rawAssembly: Array[int]) -> Assembly:
        """Method docstring."""
        ...

    @staticmethod
    def ReflectionOnlyLoadFrom(assemblyFile: str) -> Assembly:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    @staticmethod
    def UnsafeLoadFrom(assemblyFile: str) -> Assembly:
        """Method docstring."""
        ...


class AssemblyName:
    """Class docstring."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, assemblyName: str) -> None:
        """Initialize instance."""
        ...

    @property
    def CodeBase(self) -> str:
        """str: Property docstring."""
        ...

    @CodeBase.setter
    def CodeBase(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def ContentType(self) -> AssemblyContentType:
        """AssemblyContentType: Property docstring."""
        ...

    @ContentType.setter
    def ContentType(self, value: AssemblyContentType) -> None:
        """Set property value."""
        ...

    @property
    def CultureInfo(self) -> CultureInfo:
        """CultureInfo: Property docstring."""
        ...

    @CultureInfo.setter
    def CultureInfo(self, value: CultureInfo) -> None:
        """Set property value."""
        ...

    @property
    def CultureName(self) -> str:
        """str: Property docstring."""
        ...

    @CultureName.setter
    def CultureName(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def EscapedCodeBase(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Flags(self) -> AssemblyNameFlags:
        """AssemblyNameFlags: Property docstring."""
        ...

    @Flags.setter
    def Flags(self, value: AssemblyNameFlags) -> None:
        """Set property value."""
        ...

    @property
    def FullName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HashAlgorithm(self) -> AssemblyHashAlgorithm:
        """AssemblyHashAlgorithm: Property docstring."""
        ...

    @HashAlgorithm.setter
    def HashAlgorithm(self, value: AssemblyHashAlgorithm) -> None:
        """Set property value."""
        ...

    @property
    def KeyPair(self) -> StrongNameKeyPair:
        """StrongNameKeyPair: Property docstring."""
        ...

    @KeyPair.setter
    def KeyPair(self, value: StrongNameKeyPair) -> None:
        """Set property value."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @Name.setter
    def Name(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def ProcessorArchitecture(self) -> ProcessorArchitecture:
        """ProcessorArchitecture: Property docstring."""
        ...

    @ProcessorArchitecture.setter
    def ProcessorArchitecture(self, value: ProcessorArchitecture) -> None:
        """Set property value."""
        ...

    @property
    def Version(self) -> Version:
        """Version: Property docstring."""
        ...

    @Version.setter
    def Version(self, value: Version) -> None:
        """Set property value."""
        ...

    @property
    def VersionCompatibility(self) -> AssemblyVersionCompatibility:
        """AssemblyVersionCompatibility: Property docstring."""
        ...

    @VersionCompatibility.setter
    def VersionCompatibility(self, value: AssemblyVersionCompatibility) -> None:
        """Set property value."""
        ...

    def Clone(self) -> Any:
        """Method docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    @staticmethod
    def GetAssemblyName(assemblyFile: str) -> AssemblyName:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """Method docstring."""
        ...

    def GetPublicKey(self) -> Array[int]:
        """Method docstring."""
        ...

    def GetPublicKeyToken(self) -> Array[int]:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def OnDeserialization(self, sender: Any) -> None:
        """Method docstring."""
        ...

    @staticmethod
    def ReferenceMatchesDefinition(reference: AssemblyName, definition: AssemblyName) -> bool:
        """Method docstring."""
        ...

    def SetPublicKey(self, publicKey: Array[int]) -> None:
        """Method docstring."""
        ...

    def SetPublicKeyToken(self, publicKeyToken: Array[int]) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...


class MethodBase(MemberInfo):
    """Class docstring."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Attributes(self) -> MethodAttributes:
        """MethodAttributes: Property docstring."""
        ...

    @property
    def CallingConvention(self) -> CallingConventions:
        """CallingConventions: Property docstring."""
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
    def DeclaringType(self) -> Type:
        """Type: Property docstring."""
        ...

    @property
    def IsAbstract(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsAssembly(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsConstructor(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsFamily(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsFamilyAndAssembly(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsFamilyOrAssembly(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsFinal(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsGenericMethod(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsGenericMethodDefinition(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsHideBySig(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsPrivate(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsPublic(self) -> bool:
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
    def IsSpecialName(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsStatic(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsVirtual(self) -> bool:
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
    def MethodHandle(self) -> RuntimeMethodHandle:
        """RuntimeMethodHandle: Property docstring."""
        ...

    @property
    def MethodImplementationFlags(self) -> MethodImplAttributes:
        """MethodImplAttributes: Property docstring."""
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
    def ReflectedType(self) -> Type:
        """Type: Property docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    @staticmethod
    def GetCurrentMethod() -> MethodBase:
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

    def GetGenericArguments(self) -> Array[Type]:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetMethodBody(self) -> MethodBody:
        """Method docstring."""
        ...

    @staticmethod
    def GetMethodFromHandle(handle: RuntimeMethodHandle) -> MethodBase:
        """Method docstring."""
        ...

    @overload
    @staticmethod
    def GetMethodFromHandle(handle: RuntimeMethodHandle, declaringType: RuntimeTypeHandle) -> MethodBase:
        """Method docstring."""
        ...

    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """Method docstring."""
        ...

    def GetParameters(self) -> Array[ParameterInfo]:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def Invoke(self, obj: Any, parameters: Array[Any]) -> Any:
        """Method docstring."""
        ...

    @overload
    def Invoke(self, obj: Any, invokeAttr: BindingFlags, binder: Binder, parameters: Array[Any], culture: CultureInfo) -> Any:
        """Method docstring."""
        ...

    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...


class MethodInfo(MethodBase):
    """Class docstring."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Attributes(self) -> MethodAttributes:
        """MethodAttributes: Property docstring."""
        ...

    @property
    def CallingConvention(self) -> CallingConventions:
        """CallingConventions: Property docstring."""
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
    def DeclaringType(self) -> Type:
        """Type: Property docstring."""
        ...

    @property
    def IsAbstract(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsAssembly(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsConstructor(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsFamily(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsFamilyAndAssembly(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsFamilyOrAssembly(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsFinal(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsGenericMethod(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsGenericMethodDefinition(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsHideBySig(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsPrivate(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsPublic(self) -> bool:
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
    def IsSpecialName(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsStatic(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsVirtual(self) -> bool:
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
    def MethodHandle(self) -> RuntimeMethodHandle:
        """RuntimeMethodHandle: Property docstring."""
        ...

    @property
    def MethodImplementationFlags(self) -> MethodImplAttributes:
        """MethodImplAttributes: Property docstring."""
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
    def ReflectedType(self) -> Type:
        """Type: Property docstring."""
        ...

    @property
    def ReturnParameter(self) -> ParameterInfo:
        """ParameterInfo: Property docstring."""
        ...

    @property
    def ReturnType(self) -> Type:
        """Type: Property docstring."""
        ...

    @property
    def ReturnTypeCustomAttributes(self) -> RuntimeType:
        """RuntimeType: Property docstring."""
        ...

    def CreateDelegate(self, delegateType: Type) -> Delegate:
        """Method docstring."""
        ...

    @overload
    def CreateDelegate(self, delegateType: Type, target: Any) -> Delegate:
        """Method docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetBaseDefinition(self) -> MethodInfo:
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

    def GetGenericArguments(self) -> Array[Type]:
        """Method docstring."""
        ...

    def GetGenericMethodDefinition(self) -> MethodInfo:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetMethodBody(self) -> MethodBody:
        """Method docstring."""
        ...

    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """Method docstring."""
        ...

    def GetParameters(self) -> Array[ParameterInfo]:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def Invoke(self, obj: Any, parameters: Array[Any]) -> Any:
        """Method docstring."""
        ...

    @overload
    def Invoke(self, obj: Any, invokeAttr: BindingFlags, binder: Binder, parameters: Array[Any], culture: CultureInfo) -> Any:
        """Method docstring."""
        ...

    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """Method docstring."""
        ...

    def MakeGenericMethod(self, typeArguments: Array[Type]) -> MethodInfo:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

