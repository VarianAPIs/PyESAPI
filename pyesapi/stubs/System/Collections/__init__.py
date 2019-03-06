# encoding: utf-8
# module System.Collections calls itself Collections
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ArrayList(object, IList, ICollection, IEnumerable, ICloneable):
    """
    Implements the System.Collections.IList interface using an array whose size is dynamically increased as required.
    
    ArrayList()
    ArrayList(capacity: int)
    ArrayList(c: ICollection)
    """
    @staticmethod
    def Adapter(list):
        # type: (list: IList) -> ArrayList
        """
        Adapter(list: IList) -> ArrayList
        
            Creates an System.Collections.ArrayList wrapper for a specific System.Collections.IList.
        
            list: The System.Collections.IList to wrap.
            Returns: The System.Collections.ArrayList wrapper around the System.Collections.IList.
        """
        pass

    def Add(self, value):
        # type: (self: ArrayList, value: object) -> int
        """
        Add(self: ArrayList, value: object) -> int
        
            Adds an object to the end of the System.Collections.ArrayList.
        
            value: The System.Object to be added to the end of the System.Collections.ArrayList. The value can be null.
            Returns: The System.Collections.ArrayList index at which the value has been added.
        """
        pass

    def AddRange(self, c):
        # type: (self: ArrayList, c: ICollection)
        """
        AddRange(self: ArrayList, c: ICollection)
            Adds the elements of an System.Collections.ICollection to the end of the System.Collections.ArrayList.
        
            c: The System.Collections.ICollection whose elements should be added to the end of the System.Collections.ArrayList. The collection itself cannot be null, but it can contain elements that are null.
        """
        pass

    def BinarySearch(self, *__args):
        # type: (self: ArrayList, index: int, count: int, value: object, comparer: IComparer) -> int
        """
        BinarySearch(self: ArrayList, index: int, count: int, value: object, comparer: IComparer) -> int
        
            Searches a range of elements in the sorted System.Collections.ArrayList for an element using the specified comparer and returns the zero-based index of the element.
        
            index: The zero-based starting index of the range to search.
            count: The length of the range to search.
            value: The System.Object to locate. The value can be null.
            comparer: The System.Collections.IComparer implementation to use when comparing elements.-or- null to use the default comparer that is the System.IComparable implementation of each element.
            Returns: The zero-based index of value in the sorted System.Collections.ArrayList, if value is found; otherwise, a negative number, which is the bitwise complement of the index of the next element that is larger than value or, if there is no larger element, 
             the bitwise complement of System.Collections.ArrayList.Count.
        
        BinarySearch(self: ArrayList, value: object) -> int
        
            Searches the entire sorted System.Collections.ArrayList for an element using the default comparer and returns the zero-based index of the element.
        
            value: The System.Object to locate. The value can be null.
            Returns: The zero-based index of value in the sorted System.Collections.ArrayList, if value is found; otherwise, a negative number, which is the bitwise complement of the index of the next element that is larger than value or, if there is no larger element, 
             the bitwise complement of System.Collections.ArrayList.Count.
        
        BinarySearch(self: ArrayList, value: object, comparer: IComparer) -> int
        
            Searches the entire sorted System.Collections.ArrayList for an element using the specified comparer and returns the zero-based index of the element.
        
            value: The System.Object to locate. The value can be null.
            comparer: The System.Collections.IComparer implementation to use when comparing elements.-or- null to use the default comparer that is the System.IComparable implementation of each element.
            Returns: The zero-based index of value in the sorted System.Collections.ArrayList, if value is found; otherwise, a negative number, which is the bitwise complement of the index of the next element that is larger than value or, if there is no larger element, 
             the bitwise complement of System.Collections.ArrayList.Count.
        """
        pass

    def Clear(self):
        # type: (self: ArrayList)
        """
        Clear(self: ArrayList)
            Removes all elements from the System.Collections.ArrayList.
        """
        pass

    def Clone(self):
        # type: (self: ArrayList) -> object
        """
        Clone(self: ArrayList) -> object
        
            Creates a shallow copy of the System.Collections.ArrayList.
            Returns: A shallow copy of the System.Collections.ArrayList.
        """
        pass

    def Contains(self, item):
        # type: (self: ArrayList, item: object) -> bool
        """
        Contains(self: ArrayList, item: object) -> bool
        
            Determines whether an element is in the System.Collections.ArrayList.
        
            item: The System.Object to locate in the System.Collections.ArrayList. The value can be null.
            Returns: true if item is found in the System.Collections.ArrayList; otherwise, false.
        """
        pass

    def CopyTo(self, *__args):
        # type: (self: ArrayList, array: Array)
        """
        CopyTo(self: ArrayList, array: Array)
            Copies the entire System.Collections.ArrayList to a compatible one-dimensional System.Array, starting at the beginning of the target array.
        
            array: The one-dimensional System.Array that is the destination of the elements copied from System.Collections.ArrayList. The System.Array must have zero-based indexing.
        CopyTo(self: ArrayList, array: Array, arrayIndex: int)
            Copies the entire System.Collections.ArrayList to a compatible one-dimensional System.Array, starting at the specified index of the target array.
        
            array: The one-dimensional System.Array that is the destination of the elements copied from System.Collections.ArrayList. The System.Array must have zero-based indexing.
            arrayIndex: The zero-based index in array at which copying begins.
        CopyTo(self: ArrayList, index: int, array: Array, arrayIndex: int, count: int)
            Copies a range of elements from the System.Collections.ArrayList to a compatible one-dimensional System.Array, starting at the specified index of the target array.
        
            index: The zero-based index in the source System.Collections.ArrayList at which copying begins.
            array: The one-dimensional System.Array that is the destination of the elements copied from System.Collections.ArrayList. The System.Array must have zero-based indexing.
            arrayIndex: The zero-based index in array at which copying begins.
            count: The number of elements to copy.
        """
        pass

    @staticmethod
    def FixedSize(list):
        # type: (list: IList) -> IList
        """
        FixedSize(list: IList) -> IList
        
            Returns an System.Collections.IList wrapper with a fixed size.
        
            list: The System.Collections.IList to wrap.
            Returns: An System.Collections.IList wrapper with a fixed size.
        FixedSize(list: ArrayList) -> ArrayList
        
            Returns an System.Collections.ArrayList wrapper with a fixed size.
        
            list: The System.Collections.ArrayList to wrap.
            Returns: An System.Collections.ArrayList wrapper with a fixed size.
        """
        pass

    def GetEnumerator(self, index=None, count=None):
        # type: (self: ArrayList) -> IEnumerator
        """
        GetEnumerator(self: ArrayList) -> IEnumerator
        
            Returns an enumerator for the entire System.Collections.ArrayList.
            Returns: An System.Collections.IEnumerator for the entire System.Collections.ArrayList.
        GetEnumerator(self: ArrayList, index: int, count: int) -> IEnumerator
        
            Returns an enumerator for a range of elements in the System.Collections.ArrayList.
        
            index: The zero-based starting index of the System.Collections.ArrayList section that the enumerator should refer to.
            count: The number of elements in the System.Collections.ArrayList section that the enumerator should refer to.
            Returns: An System.Collections.IEnumerator for the specified range of elements in the System.Collections.ArrayList.
        """
        pass

    def GetRange(self, index, count):
        # type: (self: ArrayList, index: int, count: int) -> ArrayList
        """
        GetRange(self: ArrayList, index: int, count: int) -> ArrayList
        
            Returns an System.Collections.ArrayList which represents a subset of the elements in the source System.Collections.ArrayList.
        
            index: The zero-based System.Collections.ArrayList index at which the range starts.
            count: The number of elements in the range.
            Returns: An System.Collections.ArrayList which represents a subset of the elements in the source System.Collections.ArrayList.
        """
        pass

    def IndexOf(self, value, startIndex=None, count=None):
        # type: (self: ArrayList, value: object) -> int
        """
        IndexOf(self: ArrayList, value: object) -> int
        
            Searches for the specified System.Object and returns the zero-based index of the first occurrence within the entire System.Collections.ArrayList.
        
            value: The System.Object to locate in the System.Collections.ArrayList. The value can be null.
            Returns: The zero-based index of the first occurrence of value within the entire System.Collections.ArrayList, if found; otherwise, -1.
        IndexOf(self: ArrayList, value: object, startIndex: int) -> int
        
            Searches for the specified System.Object and returns the zero-based index of the first occurrence within the range of elements in the System.Collections.ArrayList that extends from the specified index to the last element.
        
            value: The System.Object to locate in the System.Collections.ArrayList. The value can be null.
            startIndex: The zero-based starting index of the search. 0 (zero) is valid in an empty list.
            Returns: The zero-based index of the first occurrence of value within the range of elements in the System.Collections.ArrayList that extends from startIndex to the last element, if found; otherwise, -1.
        IndexOf(self: ArrayList, value: object, startIndex: int, count: int) -> int
        
            Searches for the specified System.Object and returns the zero-based index of the first occurrence within the range of elements in the System.Collections.ArrayList that starts at the specified index and contains the specified number of elements.
        
            value: The System.Object to locate in the System.Collections.ArrayList. The value can be null.
            startIndex: The zero-based starting index of the search. 0 (zero) is valid in an empty list.
            count: The number of elements in the section to search.
            Returns: The zero-based index of the first occurrence of value within the range of elements in the System.Collections.ArrayList that starts at startIndex and contains count number of elements, if found; otherwise, -1.
        """
        pass

    def Insert(self, index, value):
        # type: (self: ArrayList, index: int, value: object)
        """
        Insert(self: ArrayList, index: int, value: object)
            Inserts an element into the System.Collections.ArrayList at the specified index.
        
            index: The zero-based index at which value should be inserted.
            value: The System.Object to insert. The value can be null.
        """
        pass

    def InsertRange(self, index, c):
        # type: (self: ArrayList, index: int, c: ICollection)
        """
        InsertRange(self: ArrayList, index: int, c: ICollection)
            Inserts the elements of a collection into the System.Collections.ArrayList at the specified index.
        
            index: The zero-based index at which the new elements should be inserted.
            c: The System.Collections.ICollection whose elements should be inserted into the System.Collections.ArrayList. The collection itself cannot be null, but it can contain elements that are null.
        """
        pass

    def LastIndexOf(self, value, startIndex=None, count=None):
        # type: (self: ArrayList, value: object) -> int
        """
        LastIndexOf(self: ArrayList, value: object) -> int
        
            Searches for the specified System.Object and returns the zero-based index of the last occurrence within the entire System.Collections.ArrayList.
        
            value: The System.Object to locate in the System.Collections.ArrayList. The value can be null.
            Returns: The zero-based index of the last occurrence of value within the entire the System.Collections.ArrayList, if found; otherwise, -1.
        LastIndexOf(self: ArrayList, value: object, startIndex: int) -> int
        
            Searches for the specified System.Object and returns the zero-based index of the last occurrence within the range of elements in the System.Collections.ArrayList that extends from the first element to the specified index.
        
            value: The System.Object to locate in the System.Collections.ArrayList. The value can be null.
            startIndex: The zero-based starting index of the backward search.
            Returns: The zero-based index of the last occurrence of value within the range of elements in the System.Collections.ArrayList that extends from the first element to startIndex, if found; otherwise, -1.
        LastIndexOf(self: ArrayList, value: object, startIndex: int, count: int) -> int
        
            Searches for the specified System.Object and returns the zero-based index of the last occurrence within the range of elements in the System.Collections.ArrayList that contains the specified number of elements and ends at the specified index.
        
            value: The System.Object to locate in the System.Collections.ArrayList. The value can be null.
            startIndex: The zero-based starting index of the backward search.
            count: The number of elements in the section to search.
            Returns: The zero-based index of the last occurrence of value within the range of elements in the System.Collections.ArrayList that contains count number of elements and ends at startIndex, if found; otherwise, -1.
        """
        pass

    @staticmethod
    def ReadOnly(list):
        # type: (list: IList) -> IList
        """
        ReadOnly(list: IList) -> IList
        
            Returns a read-only System.Collections.IList wrapper.
        
            list: The System.Collections.IList to wrap.
            Returns: A read-only System.Collections.IList wrapper around list.
        ReadOnly(list: ArrayList) -> ArrayList
        
            Returns a read-only System.Collections.ArrayList wrapper.
        
            list: The System.Collections.ArrayList to wrap.
            Returns: A read-only System.Collections.ArrayList wrapper around list.
        """
        pass

    def Remove(self, obj):
        # type: (self: ArrayList, obj: object)
        """
        Remove(self: ArrayList, obj: object)
            Removes the first occurrence of a specific object from the System.Collections.ArrayList.
        
            obj: The System.Object to remove from the System.Collections.ArrayList. The value can be null.
        """
        pass

    def RemoveAt(self, index):
        # type: (self: ArrayList, index: int)
        """
        RemoveAt(self: ArrayList, index: int)
            Removes the element at the specified index of the System.Collections.ArrayList.
        
            index: The zero-based index of the element to remove.
        """
        pass

    def RemoveRange(self, index, count):
        # type: (self: ArrayList, index: int, count: int)
        """
        RemoveRange(self: ArrayList, index: int, count: int)
            Removes a range of elements from the System.Collections.ArrayList.
        
            index: The zero-based starting index of the range of elements to remove.
            count: The number of elements to remove.
        """
        pass

    @staticmethod
    def Repeat(value, count):
        # type: (value: object, count: int) -> ArrayList
        """
        Repeat(value: object, count: int) -> ArrayList
        
            Returns an System.Collections.ArrayList whose elements are copies of the specified value.
        
            value: The System.Object to copy multiple times in the new System.Collections.ArrayList. The value can be null.
            count: The number of times value should be copied.
            Returns: An System.Collections.ArrayList with count number of elements, all of which are copies of value.
        """
        pass

    def Reverse(self, index=None, count=None):
        # type: (self: ArrayList)
        """
        Reverse(self: ArrayList)
            Reverses the order of the elements in the entire System.Collections.ArrayList.
        Reverse(self: ArrayList, index: int, count: int)
            Reverses the order of the elements in the specified range.
        
            index: The zero-based starting index of the range to reverse.
            count: The number of elements in the range to reverse.
        """
        pass

    def SetRange(self, index, c):
        # type: (self: ArrayList, index: int, c: ICollection)
        """
        SetRange(self: ArrayList, index: int, c: ICollection)
            Copies the elements of a collection over a range of elements in the System.Collections.ArrayList.
        
            index: The zero-based System.Collections.ArrayList index at which to start copying the elements of c.
            c: The System.Collections.ICollection whose elements to copy to the System.Collections.ArrayList. The collection itself cannot be null, but it can contain elements that are null.
        """
        pass

    def Sort(self, *__args):
        # type: (self: ArrayList)
        """
        Sort(self: ArrayList)
            Sorts the elements in the entire System.Collections.ArrayList.
        Sort(self: ArrayList, comparer: IComparer)
            Sorts the elements in the entire System.Collections.ArrayList using the specified comparer.
        
            comparer: The System.Collections.IComparer implementation to use when comparing elements.-or- A null reference (Nothing in Visual Basic) to use the System.IComparable implementation of each element.
        Sort(self: ArrayList, index: int, count: int, comparer: IComparer)
            Sorts the elements in a range of elements in System.Collections.ArrayList using the specified comparer.
        
            index: The zero-based starting index of the range to sort.
            count: The length of the range to sort.
            comparer: The System.Collections.IComparer implementation to use when comparing elements.-or- A null reference (Nothing in Visual Basic) to use the System.IComparable implementation of each element.
        """
        pass

    @staticmethod
    def Synchronized(list):
        # type: (list: IList) -> IList
        """
        Synchronized(list: IList) -> IList
        
            Returns an System.Collections.IList wrapper that is synchronized (thread safe).
        
            list: The System.Collections.IList to synchronize.
            Returns: An System.Collections.IList wrapper that is synchronized (thread safe).
        Synchronized(list: ArrayList) -> ArrayList
        
            Returns an System.Collections.ArrayList wrapper that is synchronized (thread safe).
        
            list: The System.Collections.ArrayList to synchronize.
            Returns: An System.Collections.ArrayList wrapper that is synchronized (thread safe).
        """
        pass

    def ToArray(self, type=None):
        # type: (self: ArrayList) -> Array[object]
        """
        ToArray(self: ArrayList) -> Array[object]
        
            Copies the elements of the System.Collections.ArrayList to a new System.Object array.
            Returns: An System.Object array containing copies of the elements of the System.Collections.ArrayList.
        ToArray(self: ArrayList, type: Type) -> Array
        
            Copies the elements of the System.Collections.ArrayList to a new array of the specified element type.
        
            type: The element System.Type of the destination array to create and copy elements to.
            Returns: An array of the specified element type containing copies of the elements of the System.Collections.ArrayList.
        """
        pass

    def TrimToSize(self):
        # type: (self: ArrayList)
        """
        TrimToSize(self: ArrayList)
            Sets the capacity to the actual number of elements in the System.Collections.ArrayList.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: IList, value: object) -> bool
        
            Determines whether the System.Collections.IList contains a specific value.
        
            value: The object to locate in the System.Collections.IList.
            Returns: true if the System.Object is found in the System.Collections.IList; otherwise, false.
        """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, capacity: int)
        __new__(cls: type, c: ICollection)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Capacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets or sets the number of elements that the System.Collections.ArrayList can contain.
    
    Get: Capacity(self: ArrayList) -> int
    
    Set: Capacity(self: ArrayList) = value
    """

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets the number of elements actually contained in the System.Collections.ArrayList.
    
    Get: Count(self: ArrayList) -> int
    """

    IsFixedSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets a value indicating whether the System.Collections.ArrayList has a fixed size.
    
    Get: IsFixedSize(self: ArrayList) -> bool
    """

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets a value indicating whether the System.Collections.ArrayList is read-only.
    
    Get: IsReadOnly(self: ArrayList) -> bool
    """

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (thread safe).
    """
    Gets a value indicating whether access to the System.Collections.ArrayList is synchronized (thread safe).
    
    Get: IsSynchronized(self: ArrayList) -> bool
    """

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets an object that can be used to synchronize access to the System.Collections.ArrayList.
    
    Get: SyncRoot(self: ArrayList) -> object
    """



class BitArray(object, ICollection, IEnumerable, ICloneable):
    # type: (1) and false indicates the bit is off (0).
    """
    Manages a compact array of bit values, which are represented as Booleans, where true indicates that the bit is on (1) and false indicates the bit is off (0).
    
    BitArray(length: int)
    BitArray(length: int, defaultValue: bool)
    BitArray(bytes: Array[Byte])
    BitArray(values: Array[bool])
    BitArray(values: Array[int])
    BitArray(bits: BitArray)
    """
    def And(self, value):
        # type: (self: BitArray, value: BitArray) -> BitArray
        """
        And(self: BitArray, value: BitArray) -> BitArray
        
            Performs the bitwise AND operation on the elements in the current System.Collections.BitArray against the corresponding elements in the specified System.Collections.BitArray.
        
            value: The System.Collections.BitArray with which to perform the bitwise AND operation.
            Returns: The current instance containing the result of the bitwise AND operation on the elements in the current System.Collections.BitArray against the corresponding elements in the specified System.Collections.BitArray.
        """
        pass

    def Clone(self):
        # type: (self: BitArray) -> object
        """
        Clone(self: BitArray) -> object
        
            Creates a shallow copy of the System.Collections.BitArray.
            Returns: A shallow copy of the System.Collections.BitArray.
        """
        pass

    def CopyTo(self, array, index):
        # type: (self: BitArray, array: Array, index: int)
        """
        CopyTo(self: BitArray, array: Array, index: int)
            Copies the entire System.Collections.BitArray to a compatible one-dimensional System.Array, starting at the specified index of the target array.
        
            array: The one-dimensional System.Array that is the destination of the elements copied from System.Collections.BitArray. The System.Array must have zero-based indexing.
            index: The zero-based index in array at which copying begins.
        """
        pass

    def Get(self, index):
        # type: (self: BitArray, index: int) -> bool
        """
        Get(self: BitArray, index: int) -> bool
        
            Gets the value of the bit at a specific position in the System.Collections.BitArray.
        
            index: The zero-based index of the value to get.
            Returns: The value of the bit at position index.
        """
        pass

    def GetEnumerator(self):
        # type: (self: BitArray) -> IEnumerator
        """
        GetEnumerator(self: BitArray) -> IEnumerator
        
            Returns an enumerator that iterates through the System.Collections.BitArray.
            Returns: An System.Collections.IEnumerator for the entire System.Collections.BitArray.
        """
        pass

    def Not(self):
        # type: (self: BitArray) -> BitArray
        """
        Not(self: BitArray) -> BitArray
        
            Inverts all the bit values in the current System.Collections.BitArray, so that elements set to true are changed to false, and elements set to false are changed to true.
            Returns: The current instance with inverted bit values.
        """
        pass

    def Or(self, value):
        # type: (self: BitArray, value: BitArray) -> BitArray
        """
        Or(self: BitArray, value: BitArray) -> BitArray
        
            Performs the bitwise OR operation on the elements in the current System.Collections.BitArray against the corresponding elements in the specified System.Collections.BitArray.
        
            value: The System.Collections.BitArray with which to perform the bitwise OR operation.
            Returns: The current instance containing the result of the bitwise OR operation on the elements in the current System.Collections.BitArray against the corresponding elements in the specified System.Collections.BitArray.
        """
        pass

    def Set(self, index, value):
        # type: (self: BitArray, index: int, value: bool)
        """
        Set(self: BitArray, index: int, value: bool)
            Sets the bit at a specific position in the System.Collections.BitArray to the specified value.
        
            index: The zero-based index of the bit to set.
            value: The Boolean value to assign to the bit.
        """
        pass

    def SetAll(self, value):
        # type: (self: BitArray, value: bool)
        """
        SetAll(self: BitArray, value: bool)
            Sets all bits in the System.Collections.BitArray to the specified value.
        
            value: The Boolean value to assign to all bits.
        """
        pass

    def Xor(self, value):
        # type: (self: BitArray, value: BitArray) -> BitArray
        """
        Xor(self: BitArray, value: BitArray) -> BitArray
        
            Performs the bitwise exclusive OR operation on the elements in the current System.Collections.BitArray against the corresponding elements in the specified System.Collections.BitArray.
        
            value: The System.Collections.BitArray with which to perform the bitwise exclusive OR operation.
            Returns: The current instance containing the result of the bitwise exclusive OR operation on the elements in the current System.Collections.BitArray against the corresponding elements in the specified System.Collections.BitArray.
        """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, length: int)
        __new__(cls: type, length: int, defaultValue: bool)
        __new__(cls: type, bytes: Array[Byte])
        __new__(cls: type, values: Array[bool])
        __new__(cls: type, values: Array[int])
        __new__(cls: type, bits: BitArray)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets the number of elements contained in the System.Collections.BitArray.
    
    Get: Count(self: BitArray) -> int
    """

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets a value indicating whether the System.Collections.BitArray is read-only.
    
    Get: IsReadOnly(self: BitArray) -> bool
    """

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (thread safe).
    """
    Gets a value indicating whether access to the System.Collections.BitArray is synchronized (thread safe).
    
    Get: IsSynchronized(self: BitArray) -> bool
    """

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets or sets the number of elements in the System.Collections.BitArray.
    
    Get: Length(self: BitArray) -> int
    
    Set: Length(self: BitArray) = value
    """

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets an object that can be used to synchronize access to the System.Collections.BitArray.
    
    Get: SyncRoot(self: BitArray) -> object
    """



class CaseInsensitiveComparer(object, IComparer):
    """
    Compares two objects for equivalence, ignoring the case of strings.
    
    CaseInsensitiveComparer()
    CaseInsensitiveComparer(culture: CultureInfo)
    """
    def Compare(self, a, b):
        # type: (self: CaseInsensitiveComparer, a: object, b: object) -> int
        """
        Compare(self: CaseInsensitiveComparer, a: object, b: object) -> int
        
            Performs a case-insensitive comparison of two objects of the same type and returns a value indicating whether one is less than, equal to, or greater than the other.
        
            a: The first object to compare.
            b: The second object to compare.
            Returns: A signed integer that indicates the relative values of a and b, as shown in the following table.Value Meaning Less than zero a is less than b, with casing ignored. Zero a equals b, with casing ignored. Greater than zero a is greater than b, with 
             casing ignored.
        """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, culture=None):
        """
        __new__(cls: type)
        __new__(cls: type, culture: CultureInfo)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Default = None
    DefaultInvariant = None


class CaseInsensitiveHashCodeProvider(object, IHashCodeProvider):
    """
    Supplies a hash code for an object, using a hashing algorithm that ignores the case of strings.
    
    CaseInsensitiveHashCodeProvider()
    CaseInsensitiveHashCodeProvider(culture: CultureInfo)
    """
    def GetHashCode(self, obj=None):
        # type: (self: CaseInsensitiveHashCodeProvider, obj: object) -> int
        """
        GetHashCode(self: CaseInsensitiveHashCodeProvider, obj: object) -> int
        
            Returns a hash code for the given object, using a hashing algorithm that ignores the case of strings.
        
            obj: The System.Object for which a hash code is to be returned.
            Returns: A hash code for the given object, using a hashing algorithm that ignores the case of strings.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, culture=None):
        """
        __new__(cls: type)
        __new__(cls: type, culture: CultureInfo)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Default = None
    DefaultInvariant = None


class IEnumerable:
    """ Exposes the enumerator, which supports a simple iteration over a non-generic collection. """
    def GetEnumerator(self):
        # type: (self: IEnumerable) -> IEnumerator
        """
        GetEnumerator(self: IEnumerable) -> IEnumerator
        
            Returns an enumerator that iterates through a collection.
            Returns: An System.Collections.IEnumerator object that can be used to iterate through the collection.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class ICollection(IEnumerable):
    """ Defines size, enumerators, and synchronization methods for all nongeneric collections. """
    def CopyTo(self, array, index):
        # type: (self: ICollection, array: Array, index: int)
        """
        CopyTo(self: ICollection, array: Array, index: int)
            Copies the elements of the System.Collections.ICollection to an System.Array, starting at a particular System.Array index.
        
            array: The one-dimensional System.Array that is the destination of the elements copied from System.Collections.ICollection. The System.Array must have zero-based indexing.
            index: The zero-based index in array at which copying begins.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets the number of elements contained in the System.Collections.ICollection.
    
    Get: Count(self: ICollection) -> int
    """

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (thread safe).
    """
    Gets a value indicating whether access to the System.Collections.ICollection is synchronized (thread safe).
    
    Get: IsSynchronized(self: ICollection) -> bool
    """

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets an object that can be used to synchronize access to the System.Collections.ICollection.
    
    Get: SyncRoot(self: ICollection) -> object
    """



class IList(ICollection, IEnumerable):
    """ Represents a non-generic collection of objects that can be individually accessed by index. """
    def Add(self, value):
        # type: (self: IList, value: object) -> int
        """
        Add(self: IList, value: object) -> int
        
            Adds an item to the System.Collections.IList.
        
            value: The object to add to the System.Collections.IList.
            Returns: The position into which the new element was inserted, or -1 to indicate that the item was not inserted into the collection,
        """
        pass

    def Clear(self):
        # type: (self: IList)
        """
        Clear(self: IList)
            Removes all items from the System.Collections.IList.
        """
        pass

    def Contains(self, value):
        """
        __contains__(self: IList, value: object) -> bool
        
            Determines whether the System.Collections.IList contains a specific value.
        
            value: The object to locate in the System.Collections.IList.
            Returns: true if the System.Object is found in the System.Collections.IList; otherwise, false.
        """
        pass

    def IndexOf(self, value):
        # type: (self: IList, value: object) -> int
        """
        IndexOf(self: IList, value: object) -> int
        
            Determines the index of a specific item in the System.Collections.IList.
        
            value: The object to locate in the System.Collections.IList.
            Returns: The index of value if found in the list; otherwise, -1.
        """
        pass

    def Insert(self, index, value):
        # type: (self: IList, index: int, value: object)
        """
        Insert(self: IList, index: int, value: object)
            Inserts an item to the System.Collections.IList at the specified index.
        
            index: The zero-based index at which value should be inserted.
            value: The object to insert into the System.Collections.IList.
        """
        pass

    def Remove(self, value):
        # type: (self: IList, value: object)
        """
        Remove(self: IList, value: object)
            Removes the first occurrence of a specific object from the System.Collections.IList.
        
            value: The object to remove from the System.Collections.IList.
        """
        pass

    def RemoveAt(self, index):
        # type: (self: IList, index: int)
        """
        RemoveAt(self: IList, index: int)
            Removes the System.Collections.IList item at the specified index.
        
            index: The zero-based index of the item to remove.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    IsFixedSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets a value indicating whether the System.Collections.IList has a fixed size.
    
    Get: IsFixedSize(self: IList) -> bool
    """

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets a value indicating whether the System.Collections.IList is read-only.
    
    Get: IsReadOnly(self: IList) -> bool
    """



class CollectionBase(object, IList, ICollection, IEnumerable):
    """ Provides the abstract base class for a strongly typed collection. """
    def Clear(self):
        # type: (self: CollectionBase)
        """
        Clear(self: CollectionBase)
            Removes all objects from the System.Collections.CollectionBase instance. This method cannot be overridden.
        """
        pass

    def GetEnumerator(self):
        # type: (self: CollectionBase) -> IEnumerator
        """
        GetEnumerator(self: CollectionBase) -> IEnumerator
        
            Returns an enumerator that iterates through the System.Collections.CollectionBase instance.
            Returns: An System.Collections.IEnumerator for the System.Collections.CollectionBase instance.
        """
        pass

    def OnClear(self, *args): #cannot find CLR method
        # type: (self: CollectionBase)
        """
        OnClear(self: CollectionBase)
            Performs additional custom processes when clearing the contents of the System.Collections.CollectionBase instance.
        """
        pass

    def OnClearComplete(self, *args): #cannot find CLR method
        # type: (self: CollectionBase)
        """
        OnClearComplete(self: CollectionBase)
            Performs additional custom processes after clearing the contents of the System.Collections.CollectionBase instance.
        """
        pass

    def OnInsert(self, *args): #cannot find CLR method
        # type: (self: CollectionBase, index: int, value: object)
        """
        OnInsert(self: CollectionBase, index: int, value: object)
            Performs additional custom processes before inserting a new element into the System.Collections.CollectionBase instance.
        
            index: The zero-based index at which to insert value.
            value: The new value of the element at index.
        """
        pass

    def OnInsertComplete(self, *args): #cannot find CLR method
        # type: (self: CollectionBase, index: int, value: object)
        """
        OnInsertComplete(self: CollectionBase, index: int, value: object)
            Performs additional custom processes after inserting a new element into the System.Collections.CollectionBase instance.
        
            index: The zero-based index at which to insert value.
            value: The new value of the element at index.
        """
        pass

    def OnRemove(self, *args): #cannot find CLR method
        # type: (self: CollectionBase, index: int, value: object)
        """
        OnRemove(self: CollectionBase, index: int, value: object)
            Performs additional custom processes when removing an element from the System.Collections.CollectionBase instance.
        
            index: The zero-based index at which value can be found.
            value: The value of the element to remove from index.
        """
        pass

    def OnRemoveComplete(self, *args): #cannot find CLR method
        # type: (self: CollectionBase, index: int, value: object)
        """
        OnRemoveComplete(self: CollectionBase, index: int, value: object)
            Performs additional custom processes after removing an element from the System.Collections.CollectionBase instance.
        
            index: The zero-based index at which value can be found.
            value: The value of the element to remove from index.
        """
        pass

    def OnSet(self, *args): #cannot find CLR method
        # type: (self: CollectionBase, index: int, oldValue: object, newValue: object)
        """
        OnSet(self: CollectionBase, index: int, oldValue: object, newValue: object)
            Performs additional custom processes before setting a value in the System.Collections.CollectionBase instance.
        
            index: The zero-based index at which oldValue can be found.
            oldValue: The value to replace with newValue.
            newValue: The new value of the element at index.
        """
        pass

    def OnSetComplete(self, *args): #cannot find CLR method
        # type: (self: CollectionBase, index: int, oldValue: object, newValue: object)
        """
        OnSetComplete(self: CollectionBase, index: int, oldValue: object, newValue: object)
            Performs additional custom processes after setting a value in the System.Collections.CollectionBase instance.
        
            index: The zero-based index at which oldValue can be found.
            oldValue: The value to replace with newValue.
            newValue: The new value of the element at index.
        """
        pass

    def OnValidate(self, *args): #cannot find CLR method
        # type: (self: CollectionBase, value: object)
        """
        OnValidate(self: CollectionBase, value: object)
            Performs additional custom processes when validating a value.
        
            value: The object to validate.
        """
        pass

    def RemoveAt(self, index):
        # type: (self: CollectionBase, index: int)
        """
        RemoveAt(self: CollectionBase, index: int)
            Removes the element at the specified index of the System.Collections.CollectionBase instance. This method is not overridable.
        
            index: The zero-based index of the element to remove.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: IList, value: object) -> bool
        
            Determines whether the System.Collections.IList contains a specific value.
        
            value: The object to locate in the System.Collections.IList.
            Returns: true if the System.Object is found in the System.Collections.IList; otherwise, false.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, capacity: int)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Capacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets or sets the number of elements that the System.Collections.CollectionBase can contain.
    
    Get: Capacity(self: CollectionBase) -> int
    
    Set: Capacity(self: CollectionBase) = value
    """

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets the number of elements contained in the System.Collections.CollectionBase instance. This property cannot be overridden.
    
    Get: Count(self: CollectionBase) -> int
    """

    InnerList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance. """

    List = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance. """



class Comparer(object, IComparer, ISerializable):
    """
    Compares two objects for equivalence, where string comparisons are case-sensitive.
    
    Comparer(culture: CultureInfo)
    """
    def Compare(self, a, b):
        # type: (self: Comparer, a: object, b: object) -> int
        """
        Compare(self: Comparer, a: object, b: object) -> int
        
            Performs a case-sensitive comparison of two objects of the same type and returns a value indicating whether one is less than, equal to, or greater than the other.
        
            a: The first object to compare.
            b: The second object to compare.
            Returns: A signed integer that indicates the relative values of a and b, as shown in the following table.Value Meaning Less than zero a is less than b. Zero a equals b. Greater than zero a is greater than b.
        """
        pass

    def GetObjectData(self, info, context):
        # type: (self: Comparer, info: SerializationInfo, context: StreamingContext)
        """
        GetObjectData(self: Comparer, info: SerializationInfo, context: StreamingContext)
            Populates a System.Runtime.Serialization.SerializationInfo object with the data required for serialization.
        
            info: The object to populate with data.
            context: The context information about the source or destination of the serialization.
        """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, culture):
        """ __new__(cls: type, culture: CultureInfo) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Default = None
    DefaultInvariant = None


class IDictionary(ICollection, IEnumerable):
    """ Represents a nongeneric collection of key/value pairs. """
    def Add(self, key, value):
        # type: (self: IDictionary, key: object, value: object)
        """
        Add(self: IDictionary, key: object, value: object)
            Adds an element with the provided key and value to the System.Collections.IDictionary object.
        
            key: The System.Object to use as the key of the element to add.
            value: The System.Object to use as the value of the element to add.
        """
        pass

    def Clear(self):
        # type: (self: IDictionary)
        """
        Clear(self: IDictionary)
            Removes all elements from the System.Collections.IDictionary object.
        """
        pass

    def Contains(self, key):
        """
        __contains__(self: IDictionary, key: object) -> bool
        
            Determines whether the System.Collections.IDictionary object contains an element with the specified key.
        
            key: The key to locate in the System.Collections.IDictionary object.
            Returns: true if the System.Collections.IDictionary contains an element with the key; otherwise, false.
        """
        pass

    def GetEnumerator(self):
        # type: (self: IDictionary) -> IDictionaryEnumerator
        """
        GetEnumerator(self: IDictionary) -> IDictionaryEnumerator
        
            Returns an System.Collections.IDictionaryEnumerator object for the System.Collections.IDictionary object.
            Returns: An System.Collections.IDictionaryEnumerator object for the System.Collections.IDictionary object.
        """
        pass

    def Remove(self, key):
        # type: (self: IDictionary, key: object)
        """
        Remove(self: IDictionary, key: object)
            Removes the element with the specified key from the System.Collections.IDictionary object.
        
            key: The key of the element to remove.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    IsFixedSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets a value indicating whether the System.Collections.IDictionary object has a fixed size.
    
    Get: IsFixedSize(self: IDictionary) -> bool
    """

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets a value indicating whether the System.Collections.IDictionary object is read-only.
    
    Get: IsReadOnly(self: IDictionary) -> bool
    """

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets an System.Collections.ICollection object containing the keys of the System.Collections.IDictionary object.
    
    Get: Keys(self: IDictionary) -> ICollection
    """

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets an System.Collections.ICollection object containing the values in the System.Collections.IDictionary object.
    
    Get: Values(self: IDictionary) -> ICollection
    """



class DictionaryBase(object, IDictionary, ICollection, IEnumerable):
    """ Provides the abstract base class for a strongly typed collection of key/value pairs. """
    def Clear(self):
        # type: (self: DictionaryBase)
        """
        Clear(self: DictionaryBase)
            Clears the contents of the System.Collections.DictionaryBase instance.
        """
        pass

    def CopyTo(self, array, index):
        # type: (self: DictionaryBase, array: Array, index: int)
        """
        CopyTo(self: DictionaryBase, array: Array, index: int)
            Copies the System.Collections.DictionaryBase elements to a one-dimensional System.Array at the specified index.
        
            array: The one-dimensional System.Array that is the destination of the System.Collections.DictionaryEntry objects copied from the System.Collections.DictionaryBase instance. The System.Array must have zero-based indexing.
            index: The zero-based index in array at which copying begins.
        """
        pass

    def GetEnumerator(self):
        # type: (self: DictionaryBase) -> IDictionaryEnumerator
        """
        GetEnumerator(self: DictionaryBase) -> IDictionaryEnumerator
        
            Returns an System.Collections.IDictionaryEnumerator that iterates through the System.Collections.DictionaryBase instance.
            Returns: An System.Collections.IDictionaryEnumerator for the System.Collections.DictionaryBase instance.
        """
        pass

    def OnClear(self, *args): #cannot find CLR method
        # type: (self: DictionaryBase)
        """
        OnClear(self: DictionaryBase)
            Performs additional custom processes before clearing the contents of the System.Collections.DictionaryBase instance.
        """
        pass

    def OnClearComplete(self, *args): #cannot find CLR method
        # type: (self: DictionaryBase)
        """
        OnClearComplete(self: DictionaryBase)
            Performs additional custom processes after clearing the contents of the System.Collections.DictionaryBase instance.
        """
        pass

    def OnGet(self, *args): #cannot find CLR method
        # type: (self: DictionaryBase, key: object, currentValue: object) -> object
        """
        OnGet(self: DictionaryBase, key: object, currentValue: object) -> object
        
            Gets the element with the specified key and value in the System.Collections.DictionaryBase instance.
        
            key: The key of the element to get.
            currentValue: The current value of the element associated with key.
            Returns: An System.Object containing the element with the specified key and value.
        """
        pass

    def OnInsert(self, *args): #cannot find CLR method
        # type: (self: DictionaryBase, key: object, value: object)
        """
        OnInsert(self: DictionaryBase, key: object, value: object)
            Performs additional custom processes before inserting a new element into the System.Collections.DictionaryBase instance.
        
            key: The key of the element to insert.
            value: The value of the element to insert.
        """
        pass

    def OnInsertComplete(self, *args): #cannot find CLR method
        # type: (self: DictionaryBase, key: object, value: object)
        """
        OnInsertComplete(self: DictionaryBase, key: object, value: object)
            Performs additional custom processes after inserting a new element into the System.Collections.DictionaryBase instance.
        
            key: The key of the element to insert.
            value: The value of the element to insert.
        """
        pass

    def OnRemove(self, *args): #cannot find CLR method
        # type: (self: DictionaryBase, key: object, value: object)
        """
        OnRemove(self: DictionaryBase, key: object, value: object)
            Performs additional custom processes before removing an element from the System.Collections.DictionaryBase instance.
        
            key: The key of the element to remove.
            value: The value of the element to remove.
        """
        pass

    def OnRemoveComplete(self, *args): #cannot find CLR method
        # type: (self: DictionaryBase, key: object, value: object)
        """
        OnRemoveComplete(self: DictionaryBase, key: object, value: object)
            Performs additional custom processes after removing an element from the System.Collections.DictionaryBase instance.
        
            key: The key of the element to remove.
            value: The value of the element to remove.
        """
        pass

    def OnSet(self, *args): #cannot find CLR method
        # type: (self: DictionaryBase, key: object, oldValue: object, newValue: object)
        """
        OnSet(self: DictionaryBase, key: object, oldValue: object, newValue: object)
            Performs additional custom processes before setting a value in the System.Collections.DictionaryBase instance.
        
            key: The key of the element to locate.
            oldValue: The old value of the element associated with key.
            newValue: The new value of the element associated with key.
        """
        pass

    def OnSetComplete(self, *args): #cannot find CLR method
        # type: (self: DictionaryBase, key: object, oldValue: object, newValue: object)
        """
        OnSetComplete(self: DictionaryBase, key: object, oldValue: object, newValue: object)
            Performs additional custom processes after setting a value in the System.Collections.DictionaryBase instance.
        
            key: The key of the element to locate.
            oldValue: The old value of the element associated with key.
            newValue: The new value of the element associated with key.
        """
        pass

    def OnValidate(self, *args): #cannot find CLR method
        # type: (self: DictionaryBase, key: object, value: object)
        """
        OnValidate(self: DictionaryBase, key: object, value: object)
            Performs additional custom processes when validating the element with the specified key and value.
        
            key: The key of the element to validate.
            value: The value of the element to validate.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: IDictionary, key: object) -> bool
        
            Determines whether the System.Collections.IDictionary object contains an element with the specified key.
        
            key: The key to locate in the System.Collections.IDictionary object.
            Returns: true if the System.Collections.IDictionary contains an element with the key; otherwise, false.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets the number of elements contained in the System.Collections.DictionaryBase instance.
    
    Get: Count(self: DictionaryBase) -> int
    """

    Dictionary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ Gets the list of elements contained in the System.Collections.DictionaryBase instance. """

    InnerHashtable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ Gets the list of elements contained in the System.Collections.DictionaryBase instance. """



class DictionaryEntry(object):
    """
    Defines a dictionary key/value pair that can be set or retrieved.
    
    DictionaryEntry(key: object, value: object)
    """
    @staticmethod # known case of __new__
    def __new__(self, key, value):
        """
        __new__[DictionaryEntry]() -> DictionaryEntry
        
        __new__(cls: type, key: object, value: object)
        """
        pass

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets or sets the key in the key/value pair.
    
    Get: Key(self: DictionaryEntry) -> object
    
    Set: Key(self: DictionaryEntry) = value
    """

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets or sets the value in the key/value pair.
    
    Get: Value(self: DictionaryEntry) -> object
    
    Set: Value(self: DictionaryEntry) = value
    """



class Hashtable(object, IDictionary, ICollection, IEnumerable, ISerializable, IDeserializationCallback, ICloneable):
    """
    Represents a collection of key/value pairs that are organized based on the hash code of the key.
    
    Hashtable()
    Hashtable(capacity: int)
    Hashtable(capacity: int, loadFactor: Single)
    Hashtable(capacity: int, loadFactor: Single, hcp: IHashCodeProvider, comparer: IComparer)
    Hashtable(capacity: int, loadFactor: Single, equalityComparer: IEqualityComparer)
    Hashtable(hcp: IHashCodeProvider, comparer: IComparer)
    Hashtable(equalityComparer: IEqualityComparer)
    Hashtable(capacity: int, hcp: IHashCodeProvider, comparer: IComparer)
    Hashtable(capacity: int, equalityComparer: IEqualityComparer)
    Hashtable(d: IDictionary)
    Hashtable(d: IDictionary, loadFactor: Single)
    Hashtable(d: IDictionary, hcp: IHashCodeProvider, comparer: IComparer)
    Hashtable(d: IDictionary, equalityComparer: IEqualityComparer)
    Hashtable(d: IDictionary, loadFactor: Single, hcp: IHashCodeProvider, comparer: IComparer)
    Hashtable(d: IDictionary, loadFactor: Single, equalityComparer: IEqualityComparer)
    """
    def Add(self, key, value):
        # type: (self: Hashtable, key: object, value: object)
        """
        Add(self: Hashtable, key: object, value: object)
            Adds an element with the specified key and value into the System.Collections.Hashtable.
        
            key: The key of the element to add.
            value: The value of the element to add. The value can be null.
        """
        pass

    def Clear(self):
        # type: (self: Hashtable)
        """
        Clear(self: Hashtable)
            Removes all elements from the System.Collections.Hashtable.
        """
        pass

    def Clone(self):
        # type: (self: Hashtable) -> object
        """
        Clone(self: Hashtable) -> object
        
            Creates a shallow copy of the System.Collections.Hashtable.
            Returns: A shallow copy of the System.Collections.Hashtable.
        """
        pass

    def Contains(self, key):
        # type: (self: Hashtable, key: object) -> bool
        """
        Contains(self: Hashtable, key: object) -> bool
        
            Determines whether the System.Collections.Hashtable contains a specific key.
        
            key: The key to locate in the System.Collections.Hashtable.
            Returns: true if the System.Collections.Hashtable contains an element with the specified key; otherwise, false.
        """
        pass

    def ContainsKey(self, key):
        # type: (self: Hashtable, key: object) -> bool
        """
        ContainsKey(self: Hashtable, key: object) -> bool
        
            Determines whether the System.Collections.Hashtable contains a specific key.
        
            key: The key to locate in the System.Collections.Hashtable.
            Returns: true if the System.Collections.Hashtable contains an element with the specified key; otherwise, false.
        """
        pass

    def ContainsValue(self, value):
        # type: (self: Hashtable, value: object) -> bool
        """
        ContainsValue(self: Hashtable, value: object) -> bool
        
            Determines whether the System.Collections.Hashtable contains a specific value.
        
            value: The value to locate in the System.Collections.Hashtable. The value can be null.
            Returns: true if the System.Collections.Hashtable contains an element with the specified value; otherwise, false.
        """
        pass

    def CopyTo(self, array, arrayIndex):
        # type: (self: Hashtable, array: Array, arrayIndex: int)
        """
        CopyTo(self: Hashtable, array: Array, arrayIndex: int)
            Copies the System.Collections.Hashtable elements to a one-dimensional System.Array instance at the specified index.
        
            array: The one-dimensional System.Array that is the destination of the System.Collections.DictionaryEntry objects copied from System.Collections.Hashtable. The System.Array must have zero-based indexing.
            arrayIndex: The zero-based index in array at which copying begins.
        """
        pass

    def GetEnumerator(self):
        # type: (self: Hashtable) -> IDictionaryEnumerator
        """
        GetEnumerator(self: Hashtable) -> IDictionaryEnumerator
        
            Returns an System.Collections.IDictionaryEnumerator that iterates through the System.Collections.Hashtable.
            Returns: An System.Collections.IDictionaryEnumerator for the System.Collections.Hashtable.
        """
        pass

    def GetHash(self, *args): #cannot find CLR method
        # type: (self: Hashtable, key: object) -> int
        """
        GetHash(self: Hashtable, key: object) -> int
        
            Returns the hash code for the specified key.
        
            key: The System.Object for which a hash code is to be returned.
            Returns: The hash code for key.
        """
        pass

    def GetObjectData(self, info, context):
        # type: (self: Hashtable, info: SerializationInfo, context: StreamingContext)
        """
        GetObjectData(self: Hashtable, info: SerializationInfo, context: StreamingContext)
            Implements the System.Runtime.Serialization.ISerializable interface and returns the data needed to serialize the System.Collections.Hashtable.
        
            info: A System.Runtime.Serialization.SerializationInfo object containing the information required to serialize the System.Collections.Hashtable.
            context: A System.Runtime.Serialization.StreamingContext object containing the source and destination of the serialized stream associated with the System.Collections.Hashtable.
        """
        pass

    def KeyEquals(self, *args): #cannot find CLR method
        # type: (self: Hashtable, item: object, key: object) -> bool
        """
        KeyEquals(self: Hashtable, item: object, key: object) -> bool
        
            Compares a specific System.Object with a specific key in the System.Collections.Hashtable.
        
            item: The System.Object to compare with key.
            key: The key in the System.Collections.Hashtable to compare with item.
            Returns: true if item and key are equal; otherwise, false.
        """
        pass

    def OnDeserialization(self, sender):
        # type: (self: Hashtable, sender: object)
        """
        OnDeserialization(self: Hashtable, sender: object)
            Implements the System.Runtime.Serialization.ISerializable interface and raises the deserialization event when the deserialization is complete.
        
            sender: The source of the deserialization event.
        """
        pass

    def Remove(self, key):
        # type: (self: Hashtable, key: object)
        """
        Remove(self: Hashtable, key: object)
            Removes the element with the specified key from the System.Collections.Hashtable.
        
            key: The key of the element to remove.
        """
        pass

    @staticmethod
    def Synchronized(table):
        # type: (table: Hashtable) -> Hashtable
        """
        Synchronized(table: Hashtable) -> Hashtable
        
            Returns a synchronized (thread-safe) wrapper for the System.Collections.Hashtable.
        
            table: The System.Collections.Hashtable to synchronize.
            Returns: A synchronized (thread-safe) wrapper for the System.Collections.Hashtable.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: IDictionary, key: object) -> bool
        
            Determines whether the System.Collections.IDictionary object contains an element with the specified key.
        
            key: The key to locate in the System.Collections.IDictionary object.
            Returns: true if the System.Collections.IDictionary contains an element with the key; otherwise, false.
        """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, capacity: int)
        __new__(cls: type, capacity: int, loadFactor: Single)
        __new__(cls: type, capacity: int, loadFactor: Single, hcp: IHashCodeProvider, comparer: IComparer)
        __new__(cls: type, capacity: int, loadFactor: Single, equalityComparer: IEqualityComparer)
        __new__(cls: type, hcp: IHashCodeProvider, comparer: IComparer)
        __new__(cls: type, equalityComparer: IEqualityComparer)
        __new__(cls: type, capacity: int, hcp: IHashCodeProvider, comparer: IComparer)
        __new__(cls: type, capacity: int, equalityComparer: IEqualityComparer)
        __new__(cls: type, d: IDictionary)
        __new__(cls: type, d: IDictionary, loadFactor: Single)
        __new__(cls: type, d: IDictionary, hcp: IHashCodeProvider, comparer: IComparer)
        __new__(cls: type, d: IDictionary, equalityComparer: IEqualityComparer)
        __new__(cls: type, d: IDictionary, loadFactor: Single, hcp: IHashCodeProvider, comparer: IComparer)
        __new__(cls: type, d: IDictionary, loadFactor: Single, equalityComparer: IEqualityComparer)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    comparer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ Gets or sets the System.Collections.IComparer to use for the System.Collections.Hashtable. """

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets the number of key/value pairs contained in the System.Collections.Hashtable.
    
    Get: Count(self: Hashtable) -> int
    """

    EqualityComparer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ Gets the System.Collections.IEqualityComparer to use for the System.Collections.Hashtable. """

    hcp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ Gets or sets the object that can dispense hash codes. """

    IsFixedSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets a value indicating whether the System.Collections.Hashtable has a fixed size.
    
    Get: IsFixedSize(self: Hashtable) -> bool
    """

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets a value indicating whether the System.Collections.Hashtable is read-only.
    
    Get: IsReadOnly(self: Hashtable) -> bool
    """

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (thread safe).
    """
    Gets a value indicating whether access to the System.Collections.Hashtable is synchronized (thread safe).
    
    Get: IsSynchronized(self: Hashtable) -> bool
    """

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets an System.Collections.ICollection containing the keys in the System.Collections.Hashtable.
    
    Get: Keys(self: Hashtable) -> ICollection
    """

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets an object that can be used to synchronize access to the System.Collections.Hashtable.
    
    Get: SyncRoot(self: Hashtable) -> object
    """

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets an System.Collections.ICollection containing the values in the System.Collections.Hashtable.
    
    Get: Values(self: Hashtable) -> ICollection
    """



class IComparer:
    """ Exposes a method that compares two objects. """
    def Compare(self, x, y):
        # type: (self: IComparer, x: object, y: object) -> int
        """
        Compare(self: IComparer, x: object, y: object) -> int
        
            Compares two objects and returns a value indicating whether one is less than, equal to, or greater than the other.
        
            x: The first object to compare.
            y: The second object to compare.
            Returns: A signed integer that indicates the relative values of x and y, as shown in the following table.Value Meaning Less than zero x is less than y. Zero x equals y. Greater than zero x is greater than y.
        """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IEnumerator:
    """ Supports a simple iteration over a nongeneric collection. """
    def MoveNext(self):
        # type: (self: IEnumerator) -> bool
        """
        MoveNext(self: IEnumerator) -> bool
        
            Advances the enumerator to the next element of the collection.
            Returns: true if the enumerator was successfully advanced to the next element; false if the enumerator has passed the end of the collection.
        """
        pass

    def next(self, *args): #cannot find CLR method
        # type: (self: object) -> object
        """ next(self: object) -> object """
        pass

    def Reset(self):
        # type: (self: IEnumerator)
        """
        Reset(self: IEnumerator)
            Sets the enumerator to its initial position, which is before the first element in the collection.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets the current element in the collection.
    
    Get: Current(self: IEnumerator) -> object
    """



class IDictionaryEnumerator(IEnumerator):
    """ Enumerates the elements of a nongeneric dictionary. """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Entry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets both the key and the value of the current dictionary entry.
    
    Get: Entry(self: IDictionaryEnumerator) -> DictionaryEntry
    """

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets the key of the current dictionary entry.
    
    Get: Key(self: IDictionaryEnumerator) -> object
    """

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets the value of the current dictionary entry.
    
    Get: Value(self: IDictionaryEnumerator) -> object
    """



class IEqualityComparer:
    """ Defines methods to support the comparison of objects for equality. """
    def Equals(self, x, y):
        # type: (self: IEqualityComparer, x: object, y: object) -> bool
        """
        Equals(self: IEqualityComparer, x: object, y: object) -> bool
        
            Determines whether the specified objects are equal.
        
            x: The first object to compare.
            y: The second object to compare.
            Returns: true if the specified objects are equal; otherwise, false.
        """
        pass

    def GetHashCode(self, obj):
        # type: (self: IEqualityComparer, obj: object) -> int
        """
        GetHashCode(self: IEqualityComparer, obj: object) -> int
        
            Returns a hash code for the specified object.
        
            obj: The System.Object for which a hash code is to be returned.
            Returns: A hash code for the specified object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IHashCodeProvider:
    """ Supplies a hash code for an object, using a custom hash function. """
    def GetHashCode(self, obj):
        # type: (self: IHashCodeProvider, obj: object) -> int
        """
        GetHashCode(self: IHashCodeProvider, obj: object) -> int
        
            Returns a hash code for the specified object.
        
            obj: The System.Object for which a hash code is to be returned.
            Returns: A hash code for the specified object.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IStructuralComparable:
    """ Supports the structural comparison of collection objects. """
    def CompareTo(self, other, comparer):
        # type: (self: IStructuralComparable, other: object, comparer: IComparer) -> int
        """
        CompareTo(self: IStructuralComparable, other: object, comparer: IComparer) -> int
        
            Determines whether the current collection object precedes, occurs in the same position as, or follows another object in the sort order.
        
            other: The object to compare with the current instance.
            comparer: An object that compares members of the current collection object with the corresponding members of other.
            Returns: An integer that indicates the relationship of the current collection object to other, as shown in the following table.Return valueDescription-1The current instance precedes other.0The current instance and other are equal.1The current instance follows 
             other.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass


class IStructuralEquatable:
    """ Defines methods to support the comparison of objects for structural equality. """
    def Equals(self, other, comparer):
        # type: (self: IStructuralEquatable, other: object, comparer: IEqualityComparer) -> bool
        """
        Equals(self: IStructuralEquatable, other: object, comparer: IEqualityComparer) -> bool
        
            Determines whether an object is structurally equal to the current instance.
        
            other: The object to compare with the current instance.
            comparer: An object that determines whether the current instance and other are equal.
            Returns: true if the two objects are equal; otherwise, false.
        """
        pass

    def GetHashCode(self, comparer):
        # type: (self: IStructuralEquatable, comparer: IEqualityComparer) -> int
        """
        GetHashCode(self: IStructuralEquatable, comparer: IEqualityComparer) -> int
        
            Returns a hash code for the current instance.
        
            comparer: An object that computes the hash code of the current object.
            Returns: The hash code for the current instance.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass


class Queue(object, ICollection, IEnumerable, ICloneable):
    """
    Represents a first-in, first-out collection of objects.
    
    Queue()
    Queue(capacity: int)
    Queue(capacity: int, growFactor: Single)
    Queue(col: ICollection)
    """
    def Clear(self):
        # type: (self: Queue)
        """
        Clear(self: Queue)
            Removes all objects from the System.Collections.Queue.
        """
        pass

    def Clone(self):
        # type: (self: Queue) -> object
        """
        Clone(self: Queue) -> object
        
            Creates a shallow copy of the System.Collections.Queue.
            Returns: A shallow copy of the System.Collections.Queue.
        """
        pass

    def Contains(self, obj):
        # type: (self: Queue, obj: object) -> bool
        """
        Contains(self: Queue, obj: object) -> bool
        
            Determines whether an element is in the System.Collections.Queue.
        
            obj: The System.Object to locate in the System.Collections.Queue. The value can be null.
            Returns: true if obj is found in the System.Collections.Queue; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        # type: (self: Queue, array: Array, index: int)
        """
        CopyTo(self: Queue, array: Array, index: int)
            Copies the System.Collections.Queue elements to an existing one-dimensional System.Array, starting at the specified array index.
        
            array: The one-dimensional System.Array that is the destination of the elements copied from System.Collections.Queue. The System.Array must have zero-based indexing.
            index: The zero-based index in array at which copying begins.
        """
        pass

    def Dequeue(self):
        # type: (self: Queue) -> object
        """
        Dequeue(self: Queue) -> object
        
            Removes and returns the object at the beginning of the System.Collections.Queue.
            Returns: The object that is removed from the beginning of the System.Collections.Queue.
        """
        pass

    def Enqueue(self, obj):
        # type: (self: Queue, obj: object)
        """
        Enqueue(self: Queue, obj: object)
            Adds an object to the end of the System.Collections.Queue.
        
            obj: The object to add to the System.Collections.Queue. The value can be null.
        """
        pass

    def GetEnumerator(self):
        # type: (self: Queue) -> IEnumerator
        """
        GetEnumerator(self: Queue) -> IEnumerator
        
            Returns an enumerator that iterates through the System.Collections.Queue.
            Returns: An System.Collections.IEnumerator for the System.Collections.Queue.
        """
        pass

    def Peek(self):
        # type: (self: Queue) -> object
        """
        Peek(self: Queue) -> object
        
            Returns the object at the beginning of the System.Collections.Queue without removing it.
            Returns: The object at the beginning of the System.Collections.Queue.
        """
        pass

    @staticmethod
    def Synchronized(queue):
        # type: (queue: Queue) -> Queue
        """
        Synchronized(queue: Queue) -> Queue
        
            Returns a System.Collections.Queue wrapper that is synchronized (thread safe).
        
            queue: The System.Collections.Queue to synchronize.
            Returns: A System.Collections.Queue wrapper that is synchronized (thread safe).
        """
        pass

    def ToArray(self):
        # type: (self: Queue) -> Array[object]
        """
        ToArray(self: Queue) -> Array[object]
        
            Copies the System.Collections.Queue elements to a new array.
            Returns: A new array containing elements copied from the System.Collections.Queue.
        """
        pass

    def TrimToSize(self):
        # type: (self: Queue)
        """
        TrimToSize(self: Queue)
            Sets the capacity to the actual number of elements in the System.Collections.Queue.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, capacity: int)
        __new__(cls: type, capacity: int, growFactor: Single)
        __new__(cls: type, col: ICollection)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets the number of elements contained in the System.Collections.Queue.
    
    Get: Count(self: Queue) -> int
    """

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (thread safe).
    """
    Gets a value indicating whether access to the System.Collections.Queue is synchronized (thread safe).
    
    Get: IsSynchronized(self: Queue) -> bool
    """

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets an object that can be used to synchronize access to the System.Collections.Queue.
    
    Get: SyncRoot(self: Queue) -> object
    """



class ReadOnlyCollectionBase(object, ICollection, IEnumerable):
    """ Provides the abstract base class for a strongly typed non-generic read-only collection. """
    def GetEnumerator(self):
        # type: (self: ReadOnlyCollectionBase) -> IEnumerator
        """
        GetEnumerator(self: ReadOnlyCollectionBase) -> IEnumerator
        
            Returns an enumerator that iterates through the System.Collections.ReadOnlyCollectionBase instance.
            Returns: An System.Collections.IEnumerator for the System.Collections.ReadOnlyCollectionBase instance.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets the number of elements contained in the System.Collections.ReadOnlyCollectionBase instance.
    
    Get: Count(self: ReadOnlyCollectionBase) -> int
    """

    InnerList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ Gets the list of elements contained in the System.Collections.ReadOnlyCollectionBase instance. """



class SortedList(object, IDictionary, ICollection, IEnumerable, ICloneable):
    """
    Represents a collection of key/value pairs that are sorted by the keys and are accessible by key and by index.
    
    SortedList()
    SortedList(initialCapacity: int)
    SortedList(comparer: IComparer)
    SortedList(comparer: IComparer, capacity: int)
    SortedList(d: IDictionary)
    SortedList(d: IDictionary, comparer: IComparer)
    """
    def Add(self, key, value):
        # type: (self: SortedList, key: object, value: object)
        """
        Add(self: SortedList, key: object, value: object)
            Adds an element with the specified key and value to a System.Collections.SortedList object.
        
            key: The key of the element to add.
            value: The value of the element to add. The value can be null.
        """
        pass

    def Clear(self):
        # type: (self: SortedList)
        """
        Clear(self: SortedList)
            Removes all elements from a System.Collections.SortedList object.
        """
        pass

    def Clone(self):
        # type: (self: SortedList) -> object
        """
        Clone(self: SortedList) -> object
        
            Creates a shallow copy of a System.Collections.SortedList object.
            Returns: A shallow copy of the System.Collections.SortedList object.
        """
        pass

    def Contains(self, key):
        # type: (self: SortedList, key: object) -> bool
        """
        Contains(self: SortedList, key: object) -> bool
        
            Determines whether a System.Collections.SortedList object contains a specific key.
        
            key: The key to locate in the System.Collections.SortedList object.
            Returns: true if the System.Collections.SortedList object contains an element with the specified key; otherwise, false.
        """
        pass

    def ContainsKey(self, key):
        # type: (self: SortedList, key: object) -> bool
        """
        ContainsKey(self: SortedList, key: object) -> bool
        
            Determines whether a System.Collections.SortedList object contains a specific key.
        
            key: The key to locate in the System.Collections.SortedList object.
            Returns: true if the System.Collections.SortedList object contains an element with the specified key; otherwise, false.
        """
        pass

    def ContainsValue(self, value):
        # type: (self: SortedList, value: object) -> bool
        """
        ContainsValue(self: SortedList, value: object) -> bool
        
            Determines whether a System.Collections.SortedList object contains a specific value.
        
            value: The value to locate in the System.Collections.SortedList object. The value can be null.
            Returns: true if the System.Collections.SortedList object contains an element with the specified value; otherwise, false.
        """
        pass

    def CopyTo(self, array, arrayIndex):
        # type: (self: SortedList, array: Array, arrayIndex: int)
        """
        CopyTo(self: SortedList, array: Array, arrayIndex: int)
            Copies System.Collections.SortedList elements to a one-dimensional System.Array object, starting at the specified index in the array.
        
            array: The one-dimensional System.Array object that is the destination of the System.Collections.DictionaryEntry objects copied from System.Collections.SortedList. The System.Array must have zero-based indexing.
            arrayIndex: The zero-based index in array at which copying begins.
        """
        pass

    def GetByIndex(self, index):
        # type: (self: SortedList, index: int) -> object
        """
        GetByIndex(self: SortedList, index: int) -> object
        
            Gets the value at the specified index of a System.Collections.SortedList object.
        
            index: The zero-based index of the value to get.
            Returns: The value at the specified index of the System.Collections.SortedList object.
        """
        pass

    def GetEnumerator(self):
        # type: (self: SortedList) -> IDictionaryEnumerator
        """
        GetEnumerator(self: SortedList) -> IDictionaryEnumerator
        
            Returns an System.Collections.IDictionaryEnumerator object that iterates through a System.Collections.SortedList object.
            Returns: An System.Collections.IDictionaryEnumerator object for the System.Collections.SortedList object.
        """
        pass

    def GetKey(self, index):
        # type: (self: SortedList, index: int) -> object
        """
        GetKey(self: SortedList, index: int) -> object
        
            Gets the key at the specified index of a System.Collections.SortedList object.
        
            index: The zero-based index of the key to get.
            Returns: The key at the specified index of the System.Collections.SortedList object.
        """
        pass

    def GetKeyList(self):
        # type: (self: SortedList) -> IList
        """
        GetKeyList(self: SortedList) -> IList
        
            Gets the keys in a System.Collections.SortedList object.
            Returns: An System.Collections.IList object containing the keys in the System.Collections.SortedList object.
        """
        pass

    def GetValueList(self):
        # type: (self: SortedList) -> IList
        """
        GetValueList(self: SortedList) -> IList
        
            Gets the values in a System.Collections.SortedList object.
            Returns: An System.Collections.IList object containing the values in the System.Collections.SortedList object.
        """
        pass

    def IndexOfKey(self, key):
        # type: (self: SortedList, key: object) -> int
        """
        IndexOfKey(self: SortedList, key: object) -> int
        
            Returns the zero-based index of the specified key in a System.Collections.SortedList object.
        
            key: The key to locate in the System.Collections.SortedList object.
            Returns: The zero-based index of the key parameter, if key is found in the System.Collections.SortedList object; otherwise, -1.
        """
        pass

    def IndexOfValue(self, value):
        # type: (self: SortedList, value: object) -> int
        """
        IndexOfValue(self: SortedList, value: object) -> int
        
            Returns the zero-based index of the first occurrence of the specified value in a System.Collections.SortedList object.
        
            value: The value to locate in the System.Collections.SortedList object. The value can be null.
            Returns: The zero-based index of the first occurrence of the value parameter, if value is found in the System.Collections.SortedList object; otherwise, -1.
        """
        pass

    def Remove(self, key):
        # type: (self: SortedList, key: object)
        """
        Remove(self: SortedList, key: object)
            Removes the element with the specified key from a System.Collections.SortedList object.
        
            key: The key of the element to remove.
        """
        pass

    def RemoveAt(self, index):
        # type: (self: SortedList, index: int)
        """
        RemoveAt(self: SortedList, index: int)
            Removes the element at the specified index of a System.Collections.SortedList object.
        
            index: The zero-based index of the element to remove.
        """
        pass

    def SetByIndex(self, index, value):
        # type: (self: SortedList, index: int, value: object)
        """
        SetByIndex(self: SortedList, index: int, value: object)
            Replaces the value at a specific index in a System.Collections.SortedList object.
        
            index: The zero-based index at which to save value.
            value: The System.Object to save into the System.Collections.SortedList object. The value can be null.
        """
        pass

    @staticmethod
    def Synchronized(list):
        # type: (list: SortedList) -> SortedList
        """
        Synchronized(list: SortedList) -> SortedList
        
            Returns a synchronized (thread-safe) wrapper for a System.Collections.SortedList object.
        
            list: The System.Collections.SortedList object to synchronize.
            Returns: A synchronized (thread-safe) wrapper for the System.Collections.SortedList object.
        """
        pass

    def TrimToSize(self):
        # type: (self: SortedList)
        """
        TrimToSize(self: SortedList)
            Sets the capacity to the actual number of elements in a System.Collections.SortedList object.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: IDictionary, key: object) -> bool
        
            Determines whether the System.Collections.IDictionary object contains an element with the specified key.
        
            key: The key to locate in the System.Collections.IDictionary object.
            Returns: true if the System.Collections.IDictionary contains an element with the key; otherwise, false.
        """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, initialCapacity: int)
        __new__(cls: type, comparer: IComparer)
        __new__(cls: type, comparer: IComparer, capacity: int)
        __new__(cls: type, d: IDictionary)
        __new__(cls: type, d: IDictionary, comparer: IComparer)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Capacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets or sets the capacity of a System.Collections.SortedList object.
    
    Get: Capacity(self: SortedList) -> int
    
    Set: Capacity(self: SortedList) = value
    """

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets the number of elements contained in a System.Collections.SortedList object.
    
    Get: Count(self: SortedList) -> int
    """

    IsFixedSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets a value indicating whether a System.Collections.SortedList object has a fixed size.
    
    Get: IsFixedSize(self: SortedList) -> bool
    """

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets a value indicating whether a System.Collections.SortedList object is read-only.
    
    Get: IsReadOnly(self: SortedList) -> bool
    """

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (thread safe).
    """
    Gets a value indicating whether access to a System.Collections.SortedList object is synchronized (thread safe).
    
    Get: IsSynchronized(self: SortedList) -> bool
    """

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets the keys in a System.Collections.SortedList object.
    
    Get: Keys(self: SortedList) -> ICollection
    """

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets an object that can be used to synchronize access to a System.Collections.SortedList object.
    
    Get: SyncRoot(self: SortedList) -> object
    """

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets the values in a System.Collections.SortedList object.
    
    Get: Values(self: SortedList) -> ICollection
    """



class Stack(object, ICollection, IEnumerable, ICloneable):
    # type: (LIFO) non-generic collection of objects.
    """
    Represents a simple last-in-first-out (LIFO) non-generic collection of objects.
    
    Stack()
    Stack(initialCapacity: int)
    Stack(col: ICollection)
    """
    def Clear(self):
        # type: (self: Stack)
        """
        Clear(self: Stack)
            Removes all objects from the System.Collections.Stack.
        """
        pass

    def Clone(self):
        # type: (self: Stack) -> object
        """
        Clone(self: Stack) -> object
        
            Creates a shallow copy of the System.Collections.Stack.
            Returns: A shallow copy of the System.Collections.Stack.
        """
        pass

    def Contains(self, obj):
        # type: (self: Stack, obj: object) -> bool
        """
        Contains(self: Stack, obj: object) -> bool
        
            Determines whether an element is in the System.Collections.Stack.
        
            obj: The System.Object to locate in the System.Collections.Stack. The value can be null.
            Returns: true, if obj is found in the System.Collections.Stack; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        # type: (self: Stack, array: Array, index: int)
        """
        CopyTo(self: Stack, array: Array, index: int)
            Copies the System.Collections.Stack to an existing one-dimensional System.Array, starting at the specified array index.
        
            array: The one-dimensional System.Array that is the destination of the elements copied from System.Collections.Stack. The System.Array must have zero-based indexing.
            index: The zero-based index in array at which copying begins.
        """
        pass

    def GetEnumerator(self):
        # type: (self: Stack) -> IEnumerator
        """
        GetEnumerator(self: Stack) -> IEnumerator
        
            Returns an System.Collections.IEnumerator for the System.Collections.Stack.
            Returns: An System.Collections.IEnumerator for the System.Collections.Stack.
        """
        pass

    def Peek(self):
        # type: (self: Stack) -> object
        """
        Peek(self: Stack) -> object
        
            Returns the object at the top of the System.Collections.Stack without removing it.
            Returns: The System.Object at the top of the System.Collections.Stack.
        """
        pass

    def Pop(self):
        # type: (self: Stack) -> object
        """
        Pop(self: Stack) -> object
        
            Removes and returns the object at the top of the System.Collections.Stack.
            Returns: The System.Object removed from the top of the System.Collections.Stack.
        """
        pass

    def Push(self, obj):
        # type: (self: Stack, obj: object)
        """
        Push(self: Stack, obj: object)
            Inserts an object at the top of the System.Collections.Stack.
        
            obj: The System.Object to push onto the System.Collections.Stack. The value can be null.
        """
        pass

    @staticmethod
    def Synchronized(stack):
        # type: (stack: Stack) -> Stack
        """
        Synchronized(stack: Stack) -> Stack
        
            Returns a synchronized (thread safe) wrapper for the System.Collections.Stack.
        
            stack: The System.Collections.Stack to synchronize.
            Returns: A synchronized wrapper around the System.Collections.Stack.
        """
        pass

    def ToArray(self):
        # type: (self: Stack) -> Array[object]
        """
        ToArray(self: Stack) -> Array[object]
        
            Copies the System.Collections.Stack to a new array.
            Returns: A new array containing copies of the elements of the System.Collections.Stack.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, initialCapacity: int)
        __new__(cls: type, col: ICollection)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets the number of elements contained in the System.Collections.Stack.
    
    Get: Count(self: Stack) -> int
    """

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (thread safe).
    """
    Gets a value indicating whether access to the System.Collections.Stack is synchronized (thread safe).
    
    Get: IsSynchronized(self: Stack) -> bool
    """

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Gets an object that can be used to synchronize access to the System.Collections.Stack.
    
    Get: SyncRoot(self: Stack) -> object
    """



class StructuralComparisons(object):
    """ Provides objects for performing a structural comparison of two collection objects. """
    StructuralComparer = None
    StructuralEqualityComparer = None
    __all__ = []


# variables with complex values

