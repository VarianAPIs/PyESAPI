#!/usr/bin/env python3
"""
DLL-First .NET Stub Generator

This version prioritizes DLL introspection using pythonnet reflection as the primary
source for all type information, with XML documentation only used for docstrings.

ARCHITECTURE:
1. Load DLL assemblies using pythonnet
2. Enumerate all types using .NET reflection
3. Extract complete type information (properties, methods, fields) from DLL
4. Parse XML documentation to match and enhance with docstrings
5. Generate Python stub files with accurate type annotations

CORE PRINCIPLES:
- DLL reflection is the source of truth for all type information
- XML provides documentation only (summary, remarks, examples, parameter descriptions)
- No hardcoded type mappings - use actual .NET reflection properties
- Direct conversion from .NET Type objects to Python type strings
- Preserve actual pythonnet runtime behavior in generated stubs

Usage:
    python dotnet_stubs.py <dll_folder> [output_folder]
    
Example:
    python dotnet_stubs.py "C:\Program Files\Varian\RTM\18.0\esapi\API" stubs
"""

import sys
import logging
import sys
import logging
import xml.etree.ElementTree as ET
import re
from pathlib import Path
from typing import Dict, List, Set, Optional, Any, Union
from dataclasses import dataclass, field
from collections import defaultdict
import xml.etree.ElementTree as ET

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

try:
    import clr
    import System
    from System import Type, Array
    from System.Reflection import Assembly, BindingFlags
    HAS_PYTHONNET = True
    logger.info("pythonnet available - DLL introspection enabled")
except ImportError:
    HAS_PYTHONNET = False
    logger.error("pythonnet not available - DLL introspection disabled")
    sys.exit(1)


# =============================================================================
# Data Structures
# =============================================================================

@dataclass
class TypeInfo:
    """Complete type information extracted from DLL"""
    full_name: str
    simple_name: str
    namespace: str
    is_class: bool = False
    is_interface: bool = False
    is_enum: bool = False
    is_struct: bool = False
    base_type: Optional[str] = None
    interfaces: List[str] = field(default_factory=list)
    properties: Dict[str, 'PropertyInfo'] = field(default_factory=dict)
    methods: Dict[str, List['MethodInfo']] = field(default_factory=dict)
    fields: Dict[str, 'FieldInfo'] = field(default_factory=dict)
    constructors: List['MethodInfo'] = field(default_factory=list)
    is_generic: bool = False
    generic_parameters: List[str] = field(default_factory=list)


@dataclass
class PropertyInfo:
    """Property information from DLL"""
    name: str
    type_str: str
    can_read: bool
    can_write: bool
    is_static: bool = False


@dataclass
class MethodInfo:
    """Method information from DLL"""
    name: str
    return_type_str: str
    parameters: List['ParameterInfo'] = field(default_factory=list)
    is_static: bool = False
    is_constructor: bool = False
    is_generic: bool = False
    generic_parameters: List[str] = field(default_factory=list)
    # Store original .NET parameter types for XML documentation lookup
    original_parameter_types: List[str] = field(default_factory=list)


@dataclass
class ParameterInfo:
    """Parameter information from DLL"""
    name: str
    type_str: str
    is_optional: bool = False
    default_value: Any = None


@dataclass
class FieldInfo:
    """Field information from DLL"""
    name: str
    type_str: str
    is_static: bool = False
    is_readonly: bool = False


@dataclass
class DocumentationInfo:
    """Documentation extracted from XML"""
    summary: str = ""
    remarks: str = ""
    returns_doc: str = ""
    example: str = ""
    param_descriptions: Dict[str, str] = field(default_factory=dict)
    exceptions: Dict[str, str] = field(default_factory=dict)


# =============================================================================
# .NET Type to Python Type Conversion
# =============================================================================

class NetTypeToPythonConverter:
    """Converts .NET Type objects directly to Python type strings using reflection"""
    
    # Cache for interface-to-implementation mappings
    _interface_implementations = {}
    _available_types = {}
    
    @classmethod
    def set_available_types(cls, available_types: Dict[str, Any]):
        """Set the available types for interface resolution"""
        cls._available_types = available_types
        cls._interface_implementations.clear()  # Clear cache when types change
    
    @classmethod
    def _find_implementation_for_interface(cls, interface_name: str) -> Optional[str]:
        """Find a concrete implementation for an interface type using reflection"""
        if not interface_name or not interface_name.startswith('I'):
            return None
        
        # Check cache first
        if interface_name in cls._interface_implementations:
            return cls._interface_implementations[interface_name]
        
        # Look for implementation by removing 'I' prefix
        impl_name = interface_name[1:]  # Remove 'I' prefix
        
        # Search in available types
        for full_name, net_type in cls._available_types.items():
            try:
                # Check if this type implements the interface
                if hasattr(net_type, 'GetInterfaces'):
                    for implemented_interface in net_type.GetInterfaces():
                        if hasattr(implemented_interface, 'Name') and implemented_interface.Name == interface_name:
                            # Found an implementation - prefer the one with matching name
                            if hasattr(net_type, 'Name') and net_type.Name == impl_name:
                                cls._interface_implementations[interface_name] = impl_name
                                return impl_name
                            # Fallback to any implementation
                            elif hasattr(net_type, 'Name'):
                                cls._interface_implementations[interface_name] = net_type.Name
                                return net_type.Name
                
                # Also check by simple name matching
                if hasattr(net_type, 'Name') and net_type.Name == impl_name:
                    # Verify it's not an interface itself
                    if hasattr(net_type, 'IsInterface') and not net_type.IsInterface:
                        cls._interface_implementations[interface_name] = impl_name
                        return impl_name
                        
            except Exception:
                continue
        
        # Cache negative result
        cls._interface_implementations[interface_name] = None
        return None
    
    # Basic type mappings for common .NET types
    BASIC_MAPPINGS = {
        'System.String': 'str',
        'System.Int32': 'int', 
        'System.Int64': 'int',
        'System.Int16': 'int',
        'System.UInt32': 'int',
        'System.UInt64': 'int', 
        'System.UInt16': 'int',
        'System.Byte': 'int',
        'System.SByte': 'int',
        'System.Double': 'float',
        'System.Single': 'float',
        'System.Decimal': 'float',
        'System.Boolean': 'bool',
        'System.DateTime': 'datetime',
        'System.TimeSpan': 'timedelta',
        'System.Guid': 'str',
        'System.Void': 'None',
        'System.Object': 'Any',
        'System.Collections.Generic.Dictionary': 'Dict',
        'System.Collections.Generic.List': 'List',
        'System.Collections.Generic.IEnumerable': 'Iterable',
        'System.Collections.Generic.IList': 'List',
        'System.Collections.Generic.IDictionary': 'Dict',
        'System.Collections.Generic.IReadOnlyList': 'List',
        'System.Collections.Generic.ICollection': 'List',
        # Keep System types as-is for pythonnet compatibility
        'System.Array': 'Array',
        'System.Type': 'Type',
        'System.ValueType': 'ValueType',
        'System.Enum': 'Enum',
        'System.MulticastDelegate': 'MulticastDelegate',
        'System.Xml.Schema.XmlSchema': 'XmlSchema',
        'System.Xml.XmlReader': 'XmlReader',
        'System.Xml.XmlWriter': 'XmlWriter',
        'System.Collections.BitArray': 'BitArray',
        'System.Collections.IEnumerator': 'IEnumerator',
        'Windows.Media.Color': 'Color',
        # Pointer types - convert to Any for Python compatibility
        'System.Void*': 'Any',
        'System.Int32*': 'Any',
        'System.Byte*': 'Any',
    }
    
    @classmethod
    def convert_type(cls, net_type) -> str:
        """Convert .NET Type object to Python type string using pure reflection"""
        if net_type is None:
            return 'Any'
        
        try:
            # Handle string representations that come from ToString() rather than actual Type objects
            if isinstance(net_type, str):
                return cls._convert_type_string(net_type)
            
            # Handle proper .NET Type objects
            # Check for reference types (ending with &)
            type_str = str(net_type)
            if type_str.endswith('&'):
                # Remove the & and process the underlying type
                underlying_type_str = type_str[:-1]
                return cls._convert_type_string(underlying_type_str)
            
            if hasattr(net_type, 'IsArray') and net_type.IsArray:
                element_type = net_type.GetElementType()
                element_python_type = cls.convert_type(element_type)
                return f'Array[{element_python_type}]'
            
            # Handle generic types using reflection
            if hasattr(net_type, 'IsGenericType') and net_type.IsGenericType:
                return cls._convert_generic_type(net_type)
            
            # Get full name using reflection
            full_name = net_type.FullName if hasattr(net_type, 'FullName') and net_type.FullName else str(net_type)
            
            # Handle nested types (replace + with .)
            if '+' in full_name:
                full_name = full_name.replace('+', '.')
            
            # Handle pointer types
            if full_name.endswith('*'):
                return 'Any'
            
            # Check basic mappings
            if full_name in cls.BASIC_MAPPINGS:
                return cls.BASIC_MAPPINGS[full_name]
            
            # Handle enums
            if hasattr(net_type, 'IsEnum') and net_type.IsEnum:
                return cls._get_simple_name(full_name)
            
            # For other types, return simple name and check for interface implementation
            simple_name = cls._get_simple_name(full_name)
            clean_name = cls._clean_assembly_references(simple_name)
            
            # Check if it's an interface and find implementation
            if hasattr(net_type, 'IsInterface') and net_type.IsInterface:
                impl_name = cls._find_implementation_for_interface(clean_name)
                if impl_name:
                    return impl_name
            
            return clean_name
            
        except Exception as e:
            logger.debug(f"Type conversion failed for {net_type}: {e}")
            return 'Any'
    
    @classmethod
    def _convert_type_string(cls, type_str: str) -> str:
        """Convert string representation of a type to Python type string"""
        if not type_str:
            return 'Any'
        
        # Handle array notation T[], T1[], etc.
        if type_str.endswith('[]'):
            element_type_name = type_str[:-2]
            # For generic type parameters like T, T1, just use Array[T]
            if element_type_name in {'T', 'T1', 'T2', 'T3', 'T4', 'TKey', 'TValue'}:
                return f'Array[{element_type_name}]'
            else:
                element_python_type = cls._convert_type_string(element_type_name)
                return f'Array[{element_python_type}]'
        
        # Handle pointer types
        if type_str.endswith('*'):
            return 'Any'
        
        # Check basic mappings
        if type_str in cls.BASIC_MAPPINGS:
            return cls.BASIC_MAPPINGS[type_str]
        
        # Handle generic notation T`1, T`2 etc by extracting base name
        if '`' in type_str:
            base_name = type_str.split('`')[0]
            simple_name = cls._get_simple_name(base_name)
            # Check for interface implementation
            impl_name = cls._find_implementation_for_interface(simple_name)
            return impl_name or simple_name
        
        # Get simple name and check for interface implementation
        simple_name = cls._get_simple_name(type_str)
        impl_name = cls._find_implementation_for_interface(simple_name)
        return impl_name or simple_name
    
    @classmethod
    def convert_type_string(cls, type_name: str) -> str:
        """Convert a type name string to Python type string"""
        if not type_name:
            return 'Any'
        
        # Check basic mappings
        if type_name in cls.BASIC_MAPPINGS:
            return cls.BASIC_MAPPINGS[type_name]
        
        # Get simple name and check for interface implementation
        simple_name = cls._get_simple_name(type_name)
        impl_name = cls._find_implementation_for_interface(simple_name)
        return impl_name or simple_name
    
    @classmethod
    def _clean_assembly_references(cls, type_str: str) -> str:
        """Clean assembly references from type strings as a final step"""
        if not type_str:
            return 'Any'  # Return Any for empty types
        
        import re
        
        # Remove assembly information patterns
        type_str = re.sub(r'\s*,\s*Culture=neutral,\s*PublicKeyToken=[a-f0-9]+\]\]&?', '', type_str)
        type_str = re.sub(r'\s*\[\[\s*', '', type_str) 
        type_str = re.sub(r'\s*\]\]\s*', '', type_str)
        type_str = re.sub(r'\s*&\s*$', '', type_str)
        
        # Clean up malformed patterns like "0, Culture=..."
        type_str = re.sub(r'^\s*\d+\s*,?\s*Culture=.*$', 'Any', type_str)
        
        # Clean up numbers that might be left from malformed conversions at the start
        type_str = re.sub(r'^\s*\d+\s*,?\s*', '', type_str)
        
        # If after cleaning we have nothing meaningful, return Any
        cleaned = type_str.strip()
        if not cleaned or cleaned in ['0', '194']:  # Common leftover numbers
            return 'Any'
        
        return cleaned
    
    @classmethod
    def _convert_generic_type(cls, net_type) -> str:
        """Convert generic .NET type using reflection"""
        try:
            # Get generic type definition and arguments
            generic_def = net_type.GetGenericTypeDefinition()
            generic_args = net_type.GetGenericArguments()
            
            # Get the base name
            def_name = generic_def.FullName if hasattr(generic_def, 'FullName') else str(generic_def)
            base_name = cls._get_simple_name(def_name).split('`')[0]  # Remove `1, `2 etc.
            
            # Convert arguments
            converted_args = [cls.convert_type(arg) for arg in generic_args]
            
            # Handle common generic types
            if 'Nullable' in base_name:
                if converted_args:
                    return f'Optional[{converted_args[0]}]'
                else:
                    return 'Optional[Any]'
            elif any(name in base_name for name in ['List', 'IList', 'IEnumerable', 'ICollection']):
                if converted_args:
                    return f'List[{converted_args[0]}]'
                else:
                    return 'List[Any]'
            elif any(name in base_name for name in ['Dictionary', 'IDictionary']):
                if len(converted_args) >= 2:
                    return f'Dict[{converted_args[0]}, {converted_args[1]}]'
                elif len(converted_args) == 1:
                    return f'Dict[str, {converted_args[0]}]'
                else:
                    return 'Dict[str, Any]'
            else:
                # Generic type we don't specifically handle
                if converted_args:
                    args_str = ', '.join(converted_args)
                    return f'{base_name}[{args_str}]'
                else:
                    return f'{base_name}[Any]'
                    
        except Exception as e:
            logger.debug(f"Generic type conversion failed for {net_type}: {e}")
            return 'Any'
    
    @classmethod
    def _get_simple_name(cls, full_name: str) -> str:
        """Extract simple class name from full name"""
        if '.' in full_name:
            return full_name.split('.')[-1]
        return full_name


# =============================================================================
# DLL Type Introspector
# =============================================================================

class DllIntrospector:
    """Introspects DLL assemblies to extract complete type information"""
    
    def __init__(self, dll_paths: List[str], docs: Optional[Dict[str, DocumentationInfo]] = None):
        self.dll_paths = dll_paths
        self.target_assemblies = []  # Only assemblies from input DLLs
        self.all_assemblies = []     # All loaded assemblies
        self.type_info_cache: Dict[str, TypeInfo] = {}
        self.referenced_types: Set[str] = set()  # All types referenced by target types
        self.available_types: Dict[str, Any] = {}  # All available .NET types by full name
        self.types_to_stub: Dict[str, TypeInfo] = {}  # All types that need stubs generated
        self.docs = docs or {}  # XML documentation for filtering
        
    def load_assemblies(self):
        """Load all DLL assemblies"""
        target_assembly_names = set()
        
        for dll_path in self.dll_paths:
            try:
                # Load assembly using pythonnet
                clr.AddReference(str(dll_path))
                
                # Extract assembly name from path for identification
                dll_name = Path(dll_path).stem
                target_assembly_names.add(dll_name)
                
                logger.info(f"Loaded assembly: {dll_path}")
            except Exception as e:
                logger.warning(f"Failed to load {dll_path}: {e}")
        
        # Get all loaded assemblies and identify target ones
        self.all_assemblies = list(System.AppDomain.CurrentDomain.GetAssemblies())
        
        # Build a map of all available types for dependency resolution
        self._build_available_types_map()
        
        # Filter to only target assemblies (those from input DLL files)
        for assembly in self.all_assemblies:
            try:
                assembly_name = assembly.GetName().Name
                if assembly_name in target_assembly_names:
                    self.target_assemblies.append(assembly)
                    logger.info(f"Target assembly identified: {assembly_name}")
            except Exception as e:
                logger.debug(f"Failed to get assembly name for {assembly}: {e}")
        
        logger.info(f"Total assemblies loaded: {len(self.all_assemblies)}")
        logger.info(f"Target assemblies for stub generation: {len(self.target_assemblies)}")
        logger.info(f"Available types for dependency resolution: {len(self.available_types)}")
    
    def _build_available_types_map(self):
        """Build a map of all available .NET types for dependency resolution"""
        for assembly in self.all_assemblies:
            try:
                for net_type in assembly.GetTypes():
                    if hasattr(net_type, 'FullName') and net_type.FullName:
                        self.available_types[net_type.FullName] = net_type
            except Exception as e:
                logger.debug(f"Failed to build type map for assembly {assembly}: {e}")
        
        # Pass available types to converter for interface resolution
        NetTypeToPythonConverter.set_available_types(self.available_types)
    
    def extract_all_types(self) -> Dict[str, TypeInfo]:
        """Extract type information from target assemblies and all their dependencies"""
        # Step 1: Extract target types from input DLLs
        target_types = {}
        
        for assembly in self.target_assemblies:
            try:
                assembly_types = self._extract_assembly_types(assembly)
                target_types.update(assembly_types)
                logger.info(f"Extracted {len(assembly_types)} types from {assembly.GetName().Name}")
            except Exception as e:
                logger.debug(f"Failed to extract types from assembly {assembly}: {e}")
        
        logger.info(f"Target types extracted from input DLLs: {len(target_types)}")
        
        # Step 2: Discover all referenced types
        self._discover_referenced_types(target_types)
        logger.info(f"Total referenced types discovered: {len(self.referenced_types)}")
        
        # Step 3: Generate stubs for all referenced types
        all_types_to_stub = {}
        
        # Add target types
        all_types_to_stub.update(target_types)
        
        # Add referenced types that we can resolve
        for referenced_type_name in self.referenced_types:
            if referenced_type_name not in all_types_to_stub and referenced_type_name in self.available_types:
                try:
                    net_type = self.available_types[referenced_type_name]
                    type_info = self._extract_type_info(net_type)
                    if type_info:
                        all_types_to_stub[referenced_type_name] = type_info
                        logger.debug(f"Added referenced type for stubbing: {referenced_type_name}")
                except Exception as e:
                    logger.debug(f"Failed to extract referenced type {referenced_type_name}: {e}")
        
        logger.info(f"Total types to generate stubs for: {len(all_types_to_stub)}")
        return all_types_to_stub
    
    def _discover_referenced_types(self, target_types: Dict[str, TypeInfo]):
        """Discover all types referenced by target types"""
        self.referenced_types.clear()
        
        for type_info in target_types.values():
            self._collect_type_references(type_info)
    
    def _collect_type_references(self, type_info: TypeInfo):
        """Recursively collect all type references from a type"""
        # Base type
        if type_info.base_type:
            self._add_type_reference(type_info.base_type)
        
        # Interfaces
        for interface in type_info.interfaces:
            self._add_type_reference(interface)
        
        # Properties
        for prop_info in type_info.properties.values():
            self._add_type_reference(prop_info.type_str)
        
        # Methods
        for method_overloads in type_info.methods.values():
            for method_info in method_overloads:
                self._add_type_reference(method_info.return_type_str)
                for param in method_info.parameters:
                    self._add_type_reference(param.type_str)
        
        # Fields
        for field_info in type_info.fields.values():
            self._add_type_reference(field_info.type_str)
        
        # Constructors
        for ctor_info in type_info.constructors:
            for param in ctor_info.parameters:
                self._add_type_reference(param.type_str)
    
    def _add_type_reference(self, type_str: str):
        """Add a type reference, extracting the actual type name"""
        if not type_str or type_str in {'Any', 'None', 'str', 'int', 'float', 'bool'}:
            return
        
        # Extract base type from generics like List[SomeType] -> SomeType
        import re
        
        # Handle generic types - extract both container and arguments
        generic_match = re.match(r'(\w+)\[(.*)\]', type_str)
        if generic_match:
            container_type = generic_match.group(1)
            args_str = generic_match.group(2)
            
            # Add container type if it's not a basic Python type
            if container_type not in {'List', 'Dict', 'Optional', 'Union', 'Iterable', 'Any', 'Callable', 'Tuple', 'Set'}:
                self._resolve_and_add_type(container_type)
            
            # Parse and add argument types
            if args_str:
                # Split by comma, but handle nested generics
                args = self._parse_generic_args(args_str)
                for arg in args:
                    self._add_type_reference(arg.strip())
        else:
            # Simple type
            self._resolve_and_add_type(type_str)
    
    def _parse_generic_args(self, args_str: str) -> List[str]:
        """Parse generic arguments, handling nested generics"""
        args = []
        current_arg = ""
        bracket_depth = 0
        
        for char in args_str:
            if char == ',' and bracket_depth == 0:
                args.append(current_arg.strip())
                current_arg = ""
            else:
                if char == '[':
                    bracket_depth += 1
                elif char == ']':
                    bracket_depth -= 1
                current_arg += char
        
        if current_arg.strip():
            args.append(current_arg.strip())
        
        return args
    
    def _resolve_and_add_type(self, type_name: str):
        """Resolve type name to full name and add to references"""
        if not type_name or type_name in self.referenced_types:
            return
        
        # Try exact match first
        if type_name in self.available_types:
            self.referenced_types.add(type_name)
            return
        
        # Try to find by simple name
        for full_name, net_type in self.available_types.items():
            try:
                if hasattr(net_type, 'Name') and net_type.Name == type_name:
                    self.referenced_types.add(full_name)
                    return
                # Also check simple name extraction
                if full_name.split('.')[-1] == type_name:
                    self.referenced_types.add(full_name)
                    return
            except:
                continue
    
    def _extract_assembly_types(self, assembly) -> Dict[str, TypeInfo]:
        """Extract types from a single assembly"""
        types = {}
        
        try:
            # Get all types from assembly
            assembly_types = assembly.GetTypes()
            logger.info(f"Found {len(assembly_types)} total types in assembly {assembly.GetName().Name}")
            
            public_count = 0
            skipped_count = 0
            extracted_count = 0
            
            for net_type in assembly_types:
                try:
                    # Check if type is public
                    if hasattr(net_type, 'IsPublic') and not net_type.IsPublic:
                        continue
                    
                    public_count += 1
                    
                    # Skip compiler-generated and private types
                    if self._should_skip_type(net_type):
                        skipped_count += 1
                        logger.debug(f"Skipping type: {net_type.FullName}")
                        continue
                    
                    type_info = self._extract_type_info(net_type)
                    if type_info:
                        types[type_info.full_name] = type_info
                        extracted_count += 1
                        logger.debug(f"Extracted type: {type_info.full_name}")
                    else:
                        logger.debug(f"Failed to extract type info for: {net_type.FullName}")
                        
                except Exception as e:
                    logger.debug(f"Failed to extract type info for {net_type}: {e}")
            
            logger.info(f"Assembly {assembly.GetName().Name}: {public_count} public types, {skipped_count} skipped, {extracted_count} extracted")
                    
        except Exception as e:
            logger.debug(f"Failed to get types from assembly {assembly}: {e}")
        
        return types
    
    def _clean_generic_type_name(self, simple_name: str, net_type) -> str:
        """Clean up generic type names by extracting actual generic type parameters from C# reflection"""
        if '`' not in simple_name:
            return simple_name
        
        # Split on backtick to get base name and parameter count
        parts = simple_name.split('`')
        base_name = parts[0]
        
        if len(parts) < 2:
            return simple_name
        
        try:
            param_count = int(parts[1])
        except ValueError:
            # If not a number, return as-is
            return simple_name
        
        # For zero parameters, just return base name
        if param_count == 0:
            return base_name
        
        # Extract actual generic type parameters from C# reflection
        if hasattr(net_type, 'IsGenericTypeDefinition') and net_type.IsGenericTypeDefinition:
            try:
                # For generic type definitions, get the generic parameters
                if hasattr(net_type, 'GetGenericArguments'):
                    generic_args = net_type.GetGenericArguments()
                    if generic_args and len(generic_args) > 0:
                        # Use actual parameter names from C# reflection
                        param_names = []
                        for arg in generic_args:
                            if hasattr(arg, 'Name'):
                                param_names.append(arg.Name)
                            else:
                                param_names.append(f'T{len(param_names)}')
                        
                        # Store the generic parameter info for later use in class generation
                        if not hasattr(net_type, '_extracted_generic_params'):
                            net_type._extracted_generic_params = param_names
                        
                        return base_name  # Return just base name for class definition
            except Exception as e:
                logger.debug(f"Failed to extract generic parameters for {net_type}: {e}")
        
        # For non-generic type definitions or if extraction fails, return just the base name
        return base_name
    
    def _should_skip_type(self, net_type) -> bool:
        """Determine if we should skip this type"""
        if not hasattr(net_type, 'FullName') or not net_type.FullName:
            return True
        
        full_name = net_type.FullName
        
        # Skip compiler-generated types
        if any(marker in full_name for marker in ['<', '>', '+<', 'c__DisplayClass', 'd__']):
            return True
        
        # Skip some system types that aren't useful in stubs
        if full_name.startswith('System.') and any(marker in full_name for marker in [
            'Runtime.CompilerServices', 'Diagnostics', 'ComponentModel'
        ]):
            return True
        
        return False
    
    def _extract_type_info(self, net_type) -> Optional[TypeInfo]:
        """Extract complete information for a single type"""
        try:
            full_name = net_type.FullName
            simple_name = net_type.Name
            namespace = net_type.Namespace or ""
            
            logger.debug(f"Processing type: {full_name}")
            
            # Handle nested types
            if '+' in full_name:
                full_name = full_name.replace('+', '.')
            
            # Clean up generic type names - remove backtick notation
            if '`' in simple_name:
                simple_name = self._clean_generic_type_name(simple_name, net_type)
            
            # Determine type category
            is_class = hasattr(net_type, 'IsClass') and net_type.IsClass
            is_interface = hasattr(net_type, 'IsInterface') and net_type.IsInterface  
            is_enum = hasattr(net_type, 'IsEnum') and net_type.IsEnum
            is_struct = hasattr(net_type, 'IsValueType') and net_type.IsValueType and not is_enum
            
            logger.debug(f"Type {full_name}: class={is_class}, interface={is_interface}, enum={is_enum}, struct={is_struct}")
            
            # Get base type
            base_type = None
            if hasattr(net_type, 'BaseType') and net_type.BaseType:
                base_type = NetTypeToPythonConverter.convert_type(net_type.BaseType)
            
            # Get interfaces
            interfaces = []
            if hasattr(net_type, 'GetInterfaces'):
                for interface in net_type.GetInterfaces():
                    interfaces.append(NetTypeToPythonConverter.convert_type(interface))
            
            # Handle generic types
            is_generic = hasattr(net_type, 'IsGenericType') and net_type.IsGenericType
            generic_parameters = []
            if is_generic and hasattr(net_type, 'GetGenericArguments'):
                for arg in net_type.GetGenericArguments():
                    generic_parameters.append(arg.Name if hasattr(arg, 'Name') else str(arg))
            
            type_info = TypeInfo(
                full_name=full_name,
                simple_name=simple_name,
                namespace=namespace,
                is_class=is_class,
                is_interface=is_interface,
                is_enum=is_enum,
                is_struct=is_struct,
                base_type=base_type,
                interfaces=interfaces,
                is_generic=is_generic,
                generic_parameters=generic_parameters
            )
            
            # Extract members
            self._extract_properties(net_type, type_info)
            self._extract_methods(net_type, type_info)
            self._extract_fields(net_type, type_info)
            self._extract_constructors(net_type, type_info)
            
            logger.debug(f"Successfully extracted type info for {full_name}")
            return type_info
            
        except Exception as e:
            logger.warning(f"Failed to extract type info for {net_type}: {e}")
            import traceback
            logger.debug(traceback.format_exc())
            return None
    
    def _extract_properties(self, net_type, type_info: TypeInfo):
        """Extract property information"""
        try:
            # Get all properties (public only, including inherited properties for complete API surface)
            binding_flags = BindingFlags.Public | BindingFlags.Instance | BindingFlags.Static
            properties = net_type.GetProperties(binding_flags)
            
            for prop in properties:
                try:
                    # Skip compiler-generated properties
                    if '<' in prop.Name or '>' in prop.Name:
                        continue
                    
                    # Skip explicit interface implementations (properties with dots in their names)
                    if '.' in prop.Name:
                        continue
                    
                    prop_info = PropertyInfo(
                        name=prop.Name,
                        type_str=NetTypeToPythonConverter.convert_type(prop.PropertyType),
                        can_read=prop.CanRead,
                        can_write=prop.CanWrite,
                        is_static=hasattr(prop, 'GetMethod') and prop.GetMethod and prop.GetMethod.IsStatic
                    )
                    
                    type_info.properties[prop.Name] = prop_info
                    
                except Exception as e:
                    logger.debug(f"Failed to extract property {prop.Name}: {e}")
                    
        except Exception as e:
            logger.debug(f"Failed to extract properties for {net_type}: {e}")
    
    def _should_include_method(self, method, type_info: TypeInfo, docs: Dict[str, DocumentationInfo]) -> bool:
        """Determine if a method should be included in the stub (simplified for public methods only)"""
        method_name = method.Name
        
        # Always skip special methods and property accessors
        if method.IsSpecialName or method_name.startswith('get_') or method_name.startswith('set_'):
            return False
        
        # Skip compiler-generated methods
        if '<' in method_name or '>' in method_name:
            return False
        
        # Skip explicit interface implementations (methods with dots in their names)
        if '.' in method_name and not method_name.startswith('op_'):
            return False
        
        if method_name.startswith('op_'):
            return True

        # Since we're only getting public methods now, include all remaining methods
        return not method.IsSpecialName

    def _extract_methods(self, net_type, type_info: TypeInfo):
        """Extract method information"""
        try:
            # Get all methods (public only, including inherited methods for complete API surface)
            binding_flags = BindingFlags.Public | BindingFlags.Instance | BindingFlags.Static
            methods = net_type.GetMethods(binding_flags)
            
            for method in methods:
                try:
                    logger.debug(f"Considering method: {method.Name}, IsSpecialName: {method.IsSpecialName}, IsPublic: {method.IsPublic}, IsStatic: {method.IsStatic}")
                    
                    # Use the filtering method to determine if this method should be included
                    if not self._should_include_method(method, type_info, self.docs):
                        continue
                    
                    method_info = MethodInfo(
                        name=method.Name,
                        return_type_str=NetTypeToPythonConverter.convert_type(method.ReturnType),
                        is_static=method.IsStatic,
                        is_generic=method.IsGenericMethod
                    )
                    
                    # Extract parameters
                    for param in method.GetParameters():
                        param_name = param.Name or f"param{param.Position}"
                        param_type = NetTypeToPythonConverter.convert_type(param.ParameterType)
                        
                        # Store original .NET type name for XML documentation lookup
                        original_type_name = param.ParameterType.FullName or str(param.ParameterType)
                        method_info.original_parameter_types.append(original_type_name)
                        
                        param_info = ParameterInfo(
                            name=self._sanitize_identifier(param_name),
                            type_str=param_type,
                            is_optional=param.IsOptional,
                            default_value=self._format_default_value(param.DefaultValue, param_type) if param.IsOptional else None
                        )
                        method_info.parameters.append(param_info)
                    
                    # Handle generic methods
                    if method_info.is_generic and hasattr(method, 'GetGenericArguments'):
                        for arg in method.GetGenericArguments():
                            method_info.generic_parameters.append(arg.Name if hasattr(arg, 'Name') else str(arg))
                    
                    # Group methods by name (for overloads)
                    if method.Name not in type_info.methods:
                        type_info.methods[method.Name] = []
                    type_info.methods[method.Name].append(method_info)
                    
                except Exception as e:
                    logger.debug(f"Failed to extract method {method.Name}: {e}")
                    
        except Exception as e:
            logger.debug(f"Failed to extract methods for {net_type}: {e}")
    
    def _extract_fields(self, net_type, type_info: TypeInfo):
        """Extract field information"""
        try:
            # Get all fields (public only, including inherited fields for complete API surface)
            binding_flags = BindingFlags.Public | BindingFlags.Instance | BindingFlags.Static
            fields = net_type.GetFields(binding_flags)
            
            for field in fields:
                try:
                    # Skip compiler-generated fields
                    if '<' in field.Name or '>' in field.Name or field.Name.startswith('k__BackingField'):
                        continue
                    
                    field_info = FieldInfo(
                        name=field.Name,
                        type_str=NetTypeToPythonConverter.convert_type(field.FieldType),
                        is_static=field.IsStatic,
                        is_readonly=field.IsInitOnly
                    )
                    
                    type_info.fields[field.Name] = field_info
                    
                except Exception as e:
                    logger.debug(f"Failed to extract field {field.Name}: {e}")
                    
        except Exception as e:
            logger.debug(f"Failed to extract fields for {net_type}: {e}")
    
    def _extract_constructors(self, net_type, type_info: TypeInfo):
        """Extract constructor information"""
        try:
            constructors = net_type.GetConstructors()
            
            for ctor in constructors:
                try:
                    ctor_info = MethodInfo(
                        name='__init__',
                        return_type_str='None',
                        is_constructor=True,
                        is_static=False
                    )
                    
                    # Extract parameters
                    for param in ctor.GetParameters():
                        param_info = ParameterInfo(
                            name=param.Name or f"param{param.Position}",
                            type_str=NetTypeToPythonConverter.convert_type(param.ParameterType),
                            is_optional=param.IsOptional,
                            default_value=param.DefaultValue if param.IsOptional else None
                        )
                        ctor_info.parameters.append(param_info)
                    
                    type_info.constructors.append(ctor_info)
                    
                except Exception as e:
                    logger.debug(f"Failed to extract constructor: {e}")
                    
        except Exception as e:
            logger.debug(f"Failed to extract constructors for {net_type}: {e}")

    def _sanitize_identifier(self, name: str) -> str:
        """Sanitize identifiers that conflict with Python reserved keywords"""
        # Python reserved keywords that cannot be used as identifiers
        PYTHON_KEYWORDS = {
            'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
            'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
            'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
            'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try',
            'while', 'with', 'yield'
        }
        
        # Add underscore suffix if it's a reserved keyword
        if name in PYTHON_KEYWORDS:
            return f"{name}_"
        
        return name

    def _format_default_value(self, default_value, param_type: str):
        """Format default values for Python stubs"""
        if default_value is None:
            return None
        
        # Handle enum values
        if hasattr(default_value, '__class__') and hasattr(default_value.__class__, '__name__'):
            class_name = default_value.__class__.__name__
            if hasattr(default_value, 'name'):  # It's an enum
                return f"{class_name}.{default_value.name}"
        
        # Handle basic types
        if isinstance(default_value, str):
            return repr(default_value)
        elif isinstance(default_value, bool):
            return str(default_value)
        elif isinstance(default_value, (int, float)):
            return str(default_value)
        else:
            # For complex types, just use None or a simple representation
            return None


# =============================================================================
# XML Documentation Parser
# =============================================================================

class XmlDocParser:
    """Parses XML documentation files to extract docstrings"""
    
    def __init__(self):
        self.doc_cache: Dict[str, DocumentationInfo] = {}
    
    def parse_xml_files(self, xml_files: List[str]) -> Dict[str, DocumentationInfo]:
        """Parse all XML files and return documentation mapping"""
        docs = {}
        
        for xml_file in xml_files:
            try:
                file_docs = self._parse_xml_file(xml_file)
                docs.update(file_docs)
                logger.info(f"Parsed documentation from {xml_file}: {len(file_docs)} entries")
            except Exception as e:
                logger.error(f"Failed to parse {xml_file}: {e}")
        
        return docs
    
    def _parse_xml_file(self, xml_file: str) -> Dict[str, DocumentationInfo]:
        """Parse a single XML documentation file"""
        docs = {}
        
        try:
            tree = ET.parse(xml_file)
            root = tree.getroot()
            
            for member in root.findall('.//member'):
                name_attr = member.get('name', '')
                if not name_attr or len(name_attr) < 2:
                    continue
                
                # Extract member identifier (remove T:, M:, P:, F: prefix)
                member_id = name_attr[2:] if name_attr[1] == ':' else name_attr
                
                doc_info = self._extract_documentation(member)
                docs[member_id] = doc_info
                
        except ET.ParseError as e:
            logger.error(f"XML parsing error in {xml_file}: {e}")
        except Exception as e:
            logger.error(f"Unexpected error parsing {xml_file}: {e}")
        
        return docs
    
    def _extract_documentation(self, member_element) -> DocumentationInfo:
        """Extract documentation from a member element"""
        doc_info = DocumentationInfo()
        
        # Extract summary
        summary_elem = member_element.find('summary')
        if summary_elem is not None and summary_elem.text:
            doc_info.summary = self._clean_text(summary_elem.text)
        
        # Extract remarks
        remarks_elem = member_element.find('remarks')
        if remarks_elem is not None and remarks_elem.text:
            doc_info.remarks = self._clean_text(remarks_elem.text)
        
        # Extract returns documentation
        returns_elem = member_element.find('returns')
        if returns_elem is not None and returns_elem.text:
            doc_info.returns_doc = self._clean_text(returns_elem.text)
        
        # Extract example
        example_elem = member_element.find('example')
        if example_elem is not None and example_elem.text:
            doc_info.example = self._clean_text(example_elem.text)
        
        # Extract parameter descriptions
        for param_elem in member_element.findall('param'):
            param_name = param_elem.get('name', '')
            if param_name and param_elem.text:
                doc_info.param_descriptions[param_name] = self._clean_text(param_elem.text)
        
        # Extract exception documentation
        for exception_elem in member_element.findall('exception'):
            exception_type = exception_elem.get('cref', '')
            if exception_type and exception_elem.text:
                # Clean up the exception type (remove T: prefix if present)
                if exception_type.startswith('T:'):
                    exception_type = exception_type[2:]
                doc_info.exceptions[exception_type] = self._clean_text(exception_elem.text)
        
        return doc_info
    
    def _clean_text(self, text: str) -> str:
        """Clean up XML text content"""
        if not text:
            return ""
        
        # Remove excessive whitespace while preserving line breaks
        lines = text.strip().split('\n')
        cleaned_lines = [line.strip() for line in lines if line.strip()]
        return ' '.join(cleaned_lines)


# =============================================================================
# Docstring Generator
# =============================================================================

class DocstringGenerator:
    """Generates Google-style docstrings from documentation info"""
    
    @staticmethod
    def generate_class_docstring(type_info: TypeInfo, doc_info: Optional[DocumentationInfo] = None) -> str:
        """Generate docstring for a class"""
        if not doc_info or not doc_info.summary:
            return '"""Class docstring."""'
        
        lines = [doc_info.summary]
        
        if doc_info.remarks:
            lines.append("")
            lines.append(doc_info.remarks)
        
        if doc_info.example:
            lines.append("")
            lines.append("Example:")
            lines.append(f"    {doc_info.example}")
        
        if len(lines) == 1:
            return f'"""{lines[0]}"""'
        else:
            content = '\n    '.join(lines)
            return f'"""{content}"""'
    
    @staticmethod
    def generate_method_docstring(method_info: MethodInfo, doc_info: Optional[DocumentationInfo] = None) -> str:
        """Generate docstring for a method"""
        if not doc_info or not doc_info.summary:
            # For constructors, provide a basic but helpful docstring
            if method_info.is_constructor:
                return '"""Initialize instance."""'
            else:
                return '"""Method docstring."""'
        
        lines = [doc_info.summary]
        
        if doc_info.remarks:
            lines.append("")
            lines.append(doc_info.remarks)
        
        # Add Args section
        if method_info.parameters and doc_info.param_descriptions:
            lines.append("")
            lines.append("Args:")
            for param in method_info.parameters:
                param_doc = doc_info.param_descriptions.get(param.name, "")
                param_line = f"    {param.name} ({param.type_str}): {param_doc}"
                lines.append(param_line)
        
        # Add Returns section
        if method_info.return_type_str != 'None' and doc_info.returns_doc:
            lines.append("")
            lines.append(f"Returns:")
            lines.append(f"    {method_info.return_type_str}: {doc_info.returns_doc}")
        
        # Add Raises section
        if doc_info.exceptions:
            lines.append("")
            lines.append("Raises:")
            for exc_type, exc_desc in doc_info.exceptions.items():
                lines.append(f"    {exc_type}: {exc_desc}")
        
        if len(lines) == 1:
            return f'"""{lines[0]}"""'
        else:
            content = '\n        '.join(lines)
            return f'"""{content}"""'
    
    @staticmethod
    def generate_property_docstring(prop_info: PropertyInfo, doc_info: Optional[DocumentationInfo] = None) -> str:
        """Generate docstring for a property"""
        if not doc_info or not doc_info.summary:
            return f'"""{prop_info.type_str}: Property docstring."""'
        
        return f'"""{prop_info.type_str}: {doc_info.summary}"""'


# =============================================================================
# Import Tracking
# =============================================================================

class ImportTracker:
    """Tracks imports needed for a specific namespace during stub generation"""
    
    def __init__(self, current_namespace: str):
        self.current_namespace = current_namespace
        self.typing_imports = set()
        self.datetime_imports = set()
        self.system_imports = {}  # System namespace -> set of types
        self.external_namespaces = {}  # external namespace -> set of types
        
    def add_type_reference(self, type_str: str, available_types: Dict[str, TypeInfo]):
        """Add a type reference and track necessary imports"""
        if not type_str or type_str in {'None', 'str', 'int', 'float', 'bool'}:
            return
            
        # Handle typing imports
        if type_str in {'Any', 'List', 'Dict', 'Optional', 'Union', 'Generic', 'Callable', 'Tuple', 'Set', 'TypeVar'}:
            self.typing_imports.add(type_str)
            return
            
        # Handle generic type parameters (T, T1, T2, etc.)
        if re.match(r'^T\d*$', type_str):
            self.typing_imports.add('TypeVar')
            return
            
        # Handle datetime imports
        if type_str in {'datetime', 'timedelta'}:
            self.datetime_imports.add(type_str)
            return
            
        # Handle generic types
        import re
        generic_match = re.match(r'(\w+)\[(.*)\]', type_str)
        if generic_match:
            container_type = generic_match.group(1)
            args_str = generic_match.group(2)
            
            # Add container type
            self.add_type_reference(container_type, available_types)
            
            # Add argument types
            if args_str:
                args = self._parse_generic_args(args_str)
                for arg in args:
                    self.add_type_reference(arg.strip(), available_types)
            return
            
        # Find the type's namespace
        type_namespace = self._find_type_namespace(type_str, available_types)
        
        if type_namespace is None:
            # Unknown type, might be System type
            if type_str in {'Array', 'Type', 'ValueType', 'Enum', 'MulticastDelegate', 'Action', 'Func'}:
                self.system_imports.setdefault('System', set()).add(type_str)
            elif type_str in {'IEnumerable', 'IList', 'IDictionary', 'ICollection'}:
                self.system_imports.setdefault('System.Collections', set()).add(type_str)
            elif type_str in {'XmlReader', 'XmlWriter'}:
                self.system_imports.setdefault('System.Xml', set()).add(type_str)
            elif type_str in {'XmlSchema'}:
                self.system_imports.setdefault('System.Xml.Schema', set()).add(type_str)
            return
            
        # If it's from a different namespace, add to external imports
        if type_namespace != self.current_namespace:
            self.external_namespaces.setdefault(type_namespace, set()).add(type_str)
    
    def _parse_generic_args(self, args_str: str) -> List[str]:
        """Parse generic arguments, handling nested generics"""
        args = []
        current_arg = ""
        bracket_depth = 0
        
        for char in args_str:
            if char == ',' and bracket_depth == 0:
                args.append(current_arg.strip())
                current_arg = ""
            else:
                if char == '[':
                    bracket_depth += 1
                elif char == ']':
                    bracket_depth -= 1
                current_arg += char
        
        if current_arg.strip():
            args.append(current_arg.strip())
        
        return args
    
    def _find_type_namespace(self, type_name: str, available_types: Dict[str, TypeInfo]) -> Optional[str]:
        """Find which namespace a type belongs to"""
        for type_info in available_types.values():
            if type_info.simple_name == type_name:
                return type_info.namespace
        return None
    
    def generate_import_lines(self) -> List[str]:
        """Generate the import statements for this namespace"""
        lines = []
        
        # Always include essential typing imports for stubs
        essential_typing = {'Any', 'overload'}
        self.typing_imports.update(essential_typing)
        
        # Typing imports
        if self.typing_imports:
            lines.append(f"from typing import {', '.join(sorted(self.typing_imports))}")
        
        # Datetime imports
        if self.datetime_imports:
            lines.append(f"from datetime import {', '.join(sorted(self.datetime_imports))}")
        
        # System imports
        for sys_namespace, types in sorted(self.system_imports.items()):
            if types:
                lines.append(f"from {sys_namespace} import {', '.join(sorted(types))}")
        
        # External namespace imports
        for ext_namespace, types in sorted(self.external_namespaces.items()):
            if types:
                lines.append(f"from {ext_namespace} import {', '.join(sorted(types))}")
        
        return lines


# =============================================================================
# Python Stub Generator
# =============================================================================

class PythonStubGenerator:
    """Generates Python stub files from type information"""
    
    OPERATOR_TO_MAGIC_METHOD = {
        'op_Addition': '__add__',
        'op_Subtraction': '__sub__',
        'op_Multiply': '__mul__',
        'op_Division': '__truediv__',
        'op_Modulus': '__mod__',
        'op_Equality': '__eq__',
        'op_Inequality': '__ne__',
        'op_LessThan': '__lt__',
        'op_GreaterThan': '__gt__',
        'op_LessThanOrEqual': '__le__',
        'op_GreaterThanOrEqual': '__ge__',
        'op_BitwiseAnd': '__and__',
        'op_BitwiseOr': '__or__',
        'op_ExclusiveOr': '__xor__',
        'op_UnaryNegation': '__neg__',
        'op_UnaryPlus': '__pos__',
        'op_Increment': '__inc__',
        'op_Decrement': '__dec__',
        'op_LogicalNot': '__not__',
        'op_LeftShift': '__lshift__',
        'op_RightShift': '__rshift__',
    }

    def __init__(self, type_infos: Dict[str, TypeInfo], docs: Dict[str, DocumentationInfo]):
        self.type_infos = type_infos
        self.docs = docs
        self.output_dir = None
        # Per-namespace import tracking
        self.namespace_imports = {}  # namespace -> ImportTracker
        self.namespace_to_types: Dict[str, Set[str]] = {}  # namespace -> set of type names in that namespace
        self.cross_references: Dict[str, Set[str]] = {}  # namespace -> set of external types it references
        
    def _build_namespace_maps(self):
        """Build maps of which types are in which namespaces and what they reference"""
        self.namespace_to_types.clear()
        self.cross_references.clear()
        
        # Build namespace -> types map
        for type_info in self.type_infos.values():
            namespace = type_info.namespace or ""
            if namespace not in self.namespace_to_types:
                self.namespace_to_types[namespace] = set()
            self.namespace_to_types[namespace].add(type_info.simple_name)
        
        # Build cross-reference map
        for type_info in self.type_infos.values():
            namespace = type_info.namespace or ""
            if namespace not in self.cross_references:
                self.cross_references[namespace] = set()
            
            # Collect all referenced types
            referenced_types = set()
            self._collect_referenced_types_from_type_info(type_info, referenced_types)
            
            # Filter to external references (not in same namespace)
            for ref_type in referenced_types:
                # Find which namespace this referenced type belongs to
                ref_namespace = self._find_type_namespace(ref_type)
                if ref_namespace != namespace and ref_namespace is not None:
                    # This is a cross-reference
                    self.cross_references[namespace].add(ref_type)
    
    def _collect_referenced_types_from_type_info(self, type_info: TypeInfo, referenced_types: set):
        """Collect all types referenced by this type info"""
        # Base type
        if type_info.base_type:
            self._extract_type_names_from_string(type_info.base_type, referenced_types)
        
        # Interfaces
        for interface in type_info.interfaces:
            self._extract_type_names_from_string(interface, referenced_types)
        
        # Properties
        for prop_info in type_info.properties.values():
            self._extract_type_names_from_string(prop_info.type_str, referenced_types)
        
        # Methods
        for method_overloads in type_info.methods.values():
            for method_info in method_overloads:
                self._extract_type_names_from_string(method_info.return_type_str, referenced_types)
                for param in method_info.parameters:
                    self._extract_type_names_from_string(param.type_str, referenced_types)
        
        # Fields
        for field_info in type_info.fields.values():
            self._extract_type_names_from_string(field_info.type_str, referenced_types)
        
        # Constructors
        for ctor_info in type_info.constructors:
            for param in ctor_info.parameters:
                self._extract_type_names_from_string(param.type_str, referenced_types)
    
    def _extract_type_names_from_string(self, type_str: str, type_names: set):
        """Extract all type names from a type string"""
        if not type_str:
            return
        
        import re
        
        # Skip basic Python types
        if type_str in {'Any', 'None', 'str', 'int', 'float', 'bool', 'object'}:
            return
        
        # Handle generic types
        generic_match = re.match(r'(\w+)\[(.*)\]', type_str)
        if generic_match:
            container_type = generic_match.group(1)
            args_str = generic_match.group(2)
            
            # Add container if it's not a basic typing type
            if container_type not in {'List', 'Dict', 'Optional', 'Union', 'Iterable', 'Callable', 'Tuple', 'Set', 'Generic'}:
                type_names.add(container_type)
            
            # Recursively parse arguments
            if args_str:
                args = self._parse_generic_args(args_str)
                for arg in args:
                    self._extract_type_names_from_string(arg.strip(), type_names)
        else:
            # Simple type
            type_names.add(type_str)
    
    def _parse_generic_args(self, args_str: str) -> List[str]:
        """Parse generic arguments, handling nested generics"""
        args = []
        current_arg = ""
        bracket_depth = 0
        
        for char in args_str:
            if char == ',' and bracket_depth == 0:
                args.append(current_arg.strip())
                current_arg = ""
            else:
                if char == '[':
                    bracket_depth += 1
                elif char == ']':
                    bracket_depth -= 1
                current_arg += char
        
        if current_arg.strip():
            args.append(current_arg.strip())
        
        return args
    
    def _find_type_namespace(self, type_name: str) -> Optional[str]:
        """Find which namespace a type belongs to"""
        for namespace, types in self.namespace_to_types.items():
            if type_name in types:
                return namespace
        
        # Check if it's a full type name that we have info for
        for full_name, type_info in self.type_infos.items():
            if type_info.simple_name == type_name:
                return type_info.namespace
        
        return None
    
    def _generate_imports_for_namespace(self, namespace: str, types: List[TypeInfo]) -> List[str]:
        """Generate import statements for a specific namespace based on actual dependencies"""
        lines = []
        
        # Comprehensive typing imports needed for stubs
        typing_imports = {'Any', 'List', 'Dict', 'Optional', 'Union', 'Generic', 'overload'}
        
        # Check if any types in this namespace are generic and need TypeVar
        has_generic_types = any(type_info.is_generic and type_info.generic_parameters for type_info in types)
        if has_generic_types:
            typing_imports.add('TypeVar')
        
        datetime_imports = {'datetime'}
        system_imports = {}  # namespace -> set of types
        cross_namespace_imports = {}  # namespace -> set of types
        
        # Always include essential typing imports
        lines.append(f"from typing import {', '.join(sorted(typing_imports))}")
        lines.append(f"from datetime import {', '.join(sorted(datetime_imports))}")
        
        # Get cross-references for this namespace
        cross_refs = self.cross_references.get(namespace, set())
        
        # Analyze what we actually need from cross-references
        for ref_type in cross_refs:
            # Check if it's a System type
            if ref_type in {'Array', 'Type', 'ValueType', 'Enum', 'MulticastDelegate'}:
                system_imports.setdefault('System', set()).add(ref_type)
            elif ref_type in {'XmlSchema'}:
                system_imports.setdefault('System.Xml.Schema', set()).add(ref_type)
            elif ref_type in {'XmlReader', 'XmlWriter'}:
                system_imports.setdefault('System.Xml', set()).add(ref_type)
            elif ref_type in {'BitArray', 'IEnumerator'}:
                system_imports.setdefault('System.Collections', set()).add(ref_type)
            elif ref_type in {'Color'}:
                system_imports.setdefault('Windows.Media', set()).add(ref_type)
            else:
                # Check if it's a cross-namespace reference
                ref_namespace = self._find_type_namespace(ref_type)
                if ref_namespace and ref_namespace != namespace:
                    # Map interfaces to implementations where available
                    mapped_type = self._map_interface_to_implementation(ref_type)
                    cross_namespace_imports.setdefault(ref_namespace, set()).add(mapped_type)
        
        # Generate import lines for System types
        for sys_namespace, sys_types in sorted(system_imports.items()):
            lines.append(f"from {sys_namespace} import {', '.join(sorted(sys_types))}")
        
        # Generate import lines for cross-namespace types
        for cross_namespace, cross_types in sorted(cross_namespace_imports.items()):
            # Convert namespace to import path
            import_path = cross_namespace.replace('.', '.')
            lines.append(f"from {import_path} import {', '.join(sorted(cross_types))}")
        
        return lines
    
    def _map_interface_to_implementation(self, type_name: str) -> str:
        """Map interface types to their implementation equivalents where available"""
        interface_mappings = {
            'IStructureCode': 'StructureCode',
            'IExternalPlanSetup': 'ExternalPlanSetup',
            'IPhotonCalculation': 'Calculation',
            'IPhotonOptimizationClient': 'OptimizationClient',
            'IProtonPlanSetup': 'IonPlanSetup',
            'IProtonCalculation': 'Calculation',
            'IProtonOptimizationClient': 'OptimizationClient',
            # Add more mappings as needed
        }
        return interface_mappings.get(type_name, type_name)
    
    def generate_stubs(self, output_dir: str):
        """Generate all stub files"""
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Build namespace relationship maps
        self._build_namespace_maps()
        
        # Organize types by namespace
        types_by_namespace = defaultdict(list)
        for type_info in self.type_infos.values():
            types_by_namespace[type_info.namespace].append(type_info)
        
        # Generate stub files per namespace
        for namespace, types in types_by_namespace.items():
            if namespace:  # Skip empty namespace for now
                self._generate_namespace_stub(namespace, types)
        
        logger.info(f"Generated stubs in {output_dir}")
    
    def _generate_namespace_stub(self, namespace: str, types: List[TypeInfo]):
        """Generate stub file for a namespace"""
        # Create module path
        module_parts = namespace.split('.')
        current_dir = self.output_dir
        
        for part in module_parts:
            current_dir = current_dir / part
            current_dir.mkdir(exist_ok=True)
            
            # Create __init__.py if it doesn't exist
            init_file = current_dir / '__init__.py'
            if not init_file.exists():
                init_file.write_text("")
        
        # Generate stub file
        stub_file = current_dir / '__init__.pyi'
        content = self._generate_module_content(namespace, types)
        stub_file.write_text(content, encoding='utf-8')
        
        logger.info(f"Generated stub: {stub_file}")
    
    def _generate_module_content(self, namespace: str, types: List[TypeInfo]) -> str:
        """Generate content for a module stub file"""
        lines = []
        
        # Add imports dynamically based on actual dependencies
        import_lines = self._generate_imports_for_namespace(namespace, types)
        lines.extend(import_lines)
        lines.append("")
        
        # Collect all generic type parameters used in this module
        type_vars_needed = set()
        for type_info in types:
            if type_info.is_generic and type_info.generic_parameters:
                for i, param in enumerate(type_info.generic_parameters):
                    if i == 0:
                        type_vars_needed.add('T')
                    else:
                        type_vars_needed.add(f'T{i}')
        
        # Generate TypeVar declarations if needed
        if type_vars_needed:
            for type_var in sorted(type_vars_needed):
                lines.append(f"{type_var} = TypeVar('{type_var}')")
            lines.append("")
        
        # Generate type stubs
        for type_info in sorted(types, key=lambda t: t.simple_name):
            if type_info.is_class:
                lines.extend(self._generate_class_stub(type_info))
            elif type_info.is_interface:
                lines.extend(self._generate_interface_stub(type_info))
            elif type_info.is_enum:
                lines.extend(self._generate_enum_stub(type_info))
            elif type_info.is_struct:
                lines.extend(self._generate_struct_stub(type_info))
            
            lines.append("")
        
        return '\n'.join(lines)
    
    def _generate_class_stub(self, type_info: TypeInfo) -> List[str]:
        """Generate stub for a class"""
        lines = []
        
        # Class definition
        class_def = f"class {type_info.simple_name}"
        
        # Handle inheritance
        base_classes = []
        if type_info.base_type and type_info.base_type != 'Any':
            base_classes.append(type_info.base_type)
        
        # Add Generic for generic types
        if type_info.is_generic and type_info.generic_parameters:
            # Create type parameter list
            type_params = []
            for i, param in enumerate(type_info.generic_parameters):
                if i == 0:
                    type_params.append('T')
                else:
                    type_params.append(f'T{i}')
            base_classes.insert(0, f"Generic[{', '.join(type_params)}]")
        
        if base_classes:
            class_def += f"({', '.join(base_classes)})"
        class_def += ":"
        
        lines.append(class_def)
        
        # Class docstring
        class_doc_key = type_info.full_name
        doc_info = self.docs.get(class_doc_key)
        docstring = DocstringGenerator.generate_class_docstring(type_info, doc_info)
        lines.append(f"    {docstring}")
        lines.append("")
        
        # Generate constructors
        if type_info.constructors:
            for i, ctor in enumerate(type_info.constructors):
                lines.extend(self._generate_constructor_stub(ctor, i > 0))
                lines.append("")
        else:
            # Default constructor
            lines.append("    def __init__(self) -> None:")
            lines.append("        \"\"\"Initialize instance.\"\"\"")
            lines.append("        ...")
            lines.append("")
        
        # Generate properties
        for prop_name, prop_info in sorted(type_info.properties.items()):
            lines.extend(self._generate_property_stub(type_info, prop_info))
            lines.append("")
        
        # Generate methods
        for method_name, method_overloads in sorted(type_info.methods.items()):
            for i, method_info in enumerate(method_overloads):
                lines.extend(self._generate_method_stub(type_info, method_info, i > 0))
                lines.append("")
        
        # Generate fields as class variables
        for field_name, field_info in sorted(type_info.fields.items()):
            lines.extend(self._generate_field_stub(type_info, field_info))
        
        # Ensure class has at least one member
        if len(lines) <= 3:  # Just class def, docstring, and empty line
            lines.append("    pass")
        
        return lines
    
    def _generate_interface_stub(self, type_info: TypeInfo) -> List[str]:
        """Generate stub for an interface (same as class for now)"""
        return self._generate_class_stub(type_info)
    
    def _generate_enum_stub(self, type_info: TypeInfo) -> List[str]:
        """Generate stub for an enum"""
        lines = []
        
        lines.append(f"class {type_info.simple_name}:")
        
        # Enum docstring
        enum_doc_key = type_info.full_name
        doc_info = self.docs.get(enum_doc_key)
        docstring = DocstringGenerator.generate_class_docstring(type_info, doc_info)
        lines.append(f"    {docstring}")
        lines.append("")
        
        # Generate enum values as class variables
        for field_name, field_info in sorted(type_info.fields.items()):
            if field_info.is_static:
                sanitized_field_name = self._sanitize_identifier(field_name)
                
                # Look up field documentation for enum values
                field_doc_key = f"{type_info.full_name}.{field_info.name}"
                doc_info = self.docs.get(field_doc_key)
                
                # Add documentation comment if available
                if doc_info and doc_info.summary:
                    lines.append(f"    # {doc_info.summary}")
                
                lines.append(f"    {sanitized_field_name}: {type_info.simple_name}")
        
        if not type_info.fields:
            lines.append("    pass")
        
        return lines
    
    def _generate_struct_stub(self, type_info: TypeInfo) -> List[str]:
        """Generate stub for a struct (same as class for now)"""
        return self._generate_class_stub(type_info)
    
    def _generate_constructor_stub(self, ctor_info: MethodInfo, is_overload: bool) -> List[str]:
        """Generate constructor stub"""
        lines = []
        
        if is_overload:
            lines.append("    @overload")
        
        # Build parameter list
        params = ["self"]
        for param in ctor_info.parameters:
            param_name = self._sanitize_identifier(param.name)
            param_str = f"{param_name}: {param.type_str}"
            if param.is_optional and param.default_value is not None:
                param_str += f" = {repr(param.default_value)}"
            params.append(param_str)
        
        params_str = ", ".join(params)
        lines.append(f"    def __init__({params_str}) -> None:")
        
        # Constructor docstring
        doc_key = f"{ctor_info.name}"  # Constructor docs are usually on the type
        doc_info = self.docs.get(doc_key)
        docstring = DocstringGenerator.generate_method_docstring(ctor_info, doc_info)
        lines.append(f"        {docstring}")
        lines.append("        ...")
        
        return lines
    
    def _generate_property_stub(self, type_info: TypeInfo, prop_info: PropertyInfo) -> List[str]:
        """Generate property stub"""
        lines = []
        
        # Sanitize property name for Python keywords
        prop_name = self._sanitize_identifier(prop_info.name)
        
        if prop_info.is_static:
            lines.append("    @classmethod")
            lines.append("    @property")
            lines.append(f"    def {prop_name}(cls) -> {prop_info.type_str}:")
        else:
            lines.append("    @property")
            lines.append(f"    def {prop_name}(self) -> {prop_info.type_str}:")
        
        # Property docstring
        prop_doc_key = f"{type_info.full_name}.{prop_info.name}"
        doc_info = self.docs.get(prop_doc_key)
        docstring = DocstringGenerator.generate_property_docstring(prop_info, doc_info)
        lines.append(f"        {docstring}")
        lines.append("        ...")
        
        # Add setter if writable
        if prop_info.can_write:
            lines.append("")
            if prop_info.is_static:
                lines.append("    @classmethod")
            lines.append(f"    @{prop_name}.setter")
            if prop_info.is_static:
                lines.append(f"    def {prop_name}(cls, value: {prop_info.type_str}) -> None:")
            else:
                lines.append(f"    def {prop_name}(self, value: {prop_info.type_str}) -> None:")
            
            # Use the same documentation for setter as getter, but modify it slightly
            if doc_info and doc_info.summary:
                setter_docstring = f'"""Set {prop_info.type_str}: {doc_info.summary}"""'
            else:
                setter_docstring = f'"""Set {prop_info.type_str}: Property setter."""'
            lines.append(f"        {setter_docstring}")
            lines.append("        ...")
        
        return lines
    
    def _sanitize_identifier(self, name: str) -> str:
        """Sanitize identifiers that conflict with Python reserved keywords"""
        # Python reserved keywords that cannot be used as identifiers
        PYTHON_KEYWORDS = {
            'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
            'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
            'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
            'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try',
            'while', 'with', 'yield'
        }
        
        # Add underscore suffix if it's a reserved keyword
        if name in PYTHON_KEYWORDS:
            return f"{name}_"
        
        return name
    
    def _generate_method_stub(self, type_info: TypeInfo, method_info: MethodInfo, is_overload: bool) -> List[str]:
        """Generate method stub"""
        lines = []
        
        if is_overload:
            lines.append("    @overload")
        
        if method_info.is_static:
            lines.append("    @staticmethod")
        
        # Sanitize method name
        method_name = self.OPERATOR_TO_MAGIC_METHOD.get(method_info.name, method_info.name)
        method_name = self._sanitize_identifier(method_info.name)
        
        # Build parameter list
        params = [] if method_info.is_static else ["self"]
        for param in method_info.parameters:
            param_name = self._sanitize_identifier(param.name)
            param_str = f"{param_name}: {param.type_str}"
            if param.is_optional and param.default_value is not None:
                param_str += f" = {repr(param.default_value)}"
            params.append(param_str)
        
        params_str = ", ".join(params)
        lines.append(f"    def {method_name}({params_str}) -> {method_info.return_type_str}:")
        
        # Method docstring - build documentation key with parameter types for overload support
        if method_info.original_parameter_types:
            # Build full method signature for XML documentation lookup (like XML format)
            param_types_str = ",".join(method_info.original_parameter_types)
            method_doc_key = f"{type_info.full_name}.{method_info.name}({param_types_str})"
        else:
            # Fallback to simple key for parameterless methods
            method_doc_key = f"{type_info.full_name}.{method_info.name}"
        
        doc_info = self.docs.get(method_doc_key)
        
        # If no exact match found, try simple key as fallback
        if not doc_info:
            simple_key = f"{type_info.full_name}.{method_info.name}"
            doc_info = self.docs.get(simple_key)
        
        docstring = DocstringGenerator.generate_method_docstring(method_info, doc_info)
        lines.append(f"        {docstring}")
        lines.append("        ...")
        
        return lines
    
    def _generate_field_stub(self, type_info: TypeInfo, field_info: FieldInfo) -> List[str]:
        """Generate field stub as class variable with documentation"""
        lines = []
        
        field_name = self._sanitize_identifier(field_info.name)
        
        # Look up field documentation
        field_doc_key = f"{type_info.full_name}.{field_info.name}"
        doc_info = self.docs.get(field_doc_key)
        
        # Add documentation comment if available
        if doc_info and doc_info.summary:
            # Add docstring comment above the field annotation
            lines.append(f"    # {doc_info.summary}")
        
        if field_info.is_static:
            lines.append(f"    {field_name}: {field_info.type_str}")
        else:
            # Instance fields become annotations
            lines.append(f"    {field_name}: {field_info.type_str}")
        
        return lines


# =============================================================================
# Main Application
# =============================================================================

def find_dll_files(folder: str) -> List[str]:
    """Find all DLL files in the folder"""
    dll_files = []
    folder_path = Path(folder)
    
    if folder_path.is_dir():
        for dll_file in folder_path.glob("*.dll"):
            dll_files.append(str(dll_file))
    
    return dll_files


def find_xml_files(folder: str) -> List[str]:
    """Find all XML files in the folder"""
    xml_files = []
    folder_path = Path(folder)
    
    if folder_path.is_dir():
        for xml_file in folder_path.glob("*.xml"):
            xml_files.append(str(xml_file))
    
    return xml_files


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: python dotnet_stubsv3.py <dll_folder> [output_folder]")
        sys.exit(1)
    
    dll_folder = sys.argv[1]
    output_folder = sys.argv[2] if len(sys.argv) > 2 else "stubs_v3"
    
    if not Path(dll_folder).exists():
        logger.error(f"DLL folder not found: {dll_folder}")
        sys.exit(1)
    
    # Find DLL and XML files
    dll_files = find_dll_files(dll_folder)
    xml_files = find_xml_files(dll_folder)
    
    logger.info(f"Found {len(dll_files)} DLL files and {len(xml_files)} XML files")
    
    if not dll_files:
        logger.error("No DLL files found")
        sys.exit(1)

    # Step 1: Parse XML documentation first (needed for method filtering)
    logger.info("Step 1: Parsing XML documentation...")
    xml_parser = XmlDocParser()
    docs = xml_parser.parse_xml_files(xml_files)

    # Step 2: Load DLLs and extract type information (with documentation-based filtering)
    logger.info("Step 2: Loading DLLs and extracting type information...")
    introspector = DllIntrospector(dll_files, docs)
    introspector.load_assemblies()
    type_infos = introspector.extract_all_types()

    # Step 3: Generate Python stubs
    logger.info("Step 3: Generating Python stub files...")
    stub_generator = PythonStubGenerator(type_infos, docs)
    stub_generator.generate_stubs(output_folder)
    
    logger.info(f"Stub generation completed. Output: {output_folder}")


if __name__ == "__main__":
    main()
