# encoding: utf-8
# module VMS.TPS.Common.Model.Types calls itself Types
# from VMS.TPS.Common.Model.Types, Version=1.0.300.11, Culture=neutral, PublicKeyToken=305b81e210ec4b89
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ApplicationScriptApprovalStatus(Enum, IComparable, IFormattable, IConvertible):
    # type: (2), ApprovedForEvaluation (1), Retired (3), Unapproved (0), Undefined (-1)
    """ enum ApplicationScriptApprovalStatus, values: Approved (2), ApprovedForEvaluation (1), Retired (3), Unapproved (0), Undefined (-1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Approved = None
    ApprovedForEvaluation = None
    Retired = None
    Unapproved = None
    Undefined = None
    value__ = None


class ApplicationScriptType(Enum, IComparable, IFormattable, IConvertible):
    # type: (0), ESAPIActionPack (1), ESAPICustomExecutable (3), MIRS (2), Unknown (-1)
    """ enum ApplicationScriptType, values: ESAPI (0), ESAPIActionPack (1), ESAPICustomExecutable (3), MIRS (2), Unknown (-1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ESAPI = None
    ESAPIActionPack = None
    ESAPICustomExecutable = None
    MIRS = None
    Unknown = None
    value__ = None


class ApprovalHistoryEntry(object):
    # no doc
    ApprovalDateTime = None
    ApprovalStatus = None
    StatusComment = None
    UserDisplayName = None
    UserId = None


class AxisAlignedMargins(object):
    # type: (geometry: StructureMarginGeometry, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float)
    """ AxisAlignedMargins(geometry: StructureMarginGeometry, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) """
    def ToString(self):
        # type: (self: AxisAlignedMargins) -> str
        """ ToString(self: AxisAlignedMargins) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, geometry, x1, y1, z1, x2, y2, z2):
        """
        __new__[AxisAlignedMargins]() -> AxisAlignedMargins

        

        __new__(cls: type, geometry: StructureMarginGeometry, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float)
        """
        pass

    Geometry = None
    X1 = None
    X2 = None
    Y1 = None
    Y2 = None
    Z1 = None
    Z2 = None


class BeamNumber(object, IXmlSerializable, IEquatable[BeamNumber]):
    # type: (number: int)

    """
    BeamNumber(number: int)

    BeamNumber(other: BeamNumber)
    """
    def Equals(self, other):
        # type: (self: BeamNumber, other: object) -> bool

        """
        Equals(self: BeamNumber, other: object) -> bool

        Equals(self: BeamNumber, other: BeamNumber) -> bool
        """
        pass

    def GetHashCode(self):
        # type: (self: BeamNumber) -> int
        """ GetHashCode(self: BeamNumber) -> int """
        pass

    def GetSchema(self):
        # type: (self: BeamNumber) -> XmlSchema
        """ GetSchema(self: BeamNumber) -> XmlSchema """
        pass

    def ReadXml(self, reader):
        # type: (self: BeamNumber, reader: XmlReader)
        """ ReadXml(self: BeamNumber, reader: XmlReader) """
        pass

    def WriteXml(self, writer):
        # type: (self: BeamNumber, writer: XmlWriter)
        """ WriteXml(self: BeamNumber, writer: XmlWriter) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __int__(self, *args): #cannot find CLR method
        """ __int__(bn: BeamNumber) -> int """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __long__(self, *args): #cannot find CLR method
        """ __int__(bn: BeamNumber) -> int """
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[BeamNumber]() -> BeamNumber

        

        __new__(cls: type, number: int)

        __new__(cls: type, other: BeamNumber)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BeamNumber) -> bool
    """ Get: IsValid(self: BeamNumber) -> bool """

    Number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BeamNumber) -> int
    """ Get: Number(self: BeamNumber) -> int """


    NotABeamNumber = None


class BlockType(Enum, IComparable, IFormattable, IConvertible):
    # type: (0), SHIELDING (1)
    """ enum BlockType, values: APERTURE (0), SHIELDING (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    APERTURE = None
    SHIELDING = None
    value__ = None


class CalculationType(Enum, IComparable, IFormattable, IConvertible):
    # type: (6), PhotonIMRTOptimization (2), PhotonLeafMotions (4), PhotonSRSDose (1), PhotonVMATOptimization (3), PhotonVolumeDose (0), ProtonVolumeDose (5)
    """ enum CalculationType, values: DVHEstimation (6), PhotonIMRTOptimization (2), PhotonLeafMotions (4), PhotonSRSDose (1), PhotonVMATOptimization (3), PhotonVolumeDose (0), ProtonVolumeDose (5) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DVHEstimation = None
    PhotonIMRTOptimization = None
    PhotonLeafMotions = None
    PhotonSRSDose = None
    PhotonVMATOptimization = None
    PhotonVolumeDose = None
    ProtonVolumeDose = None
    value__ = None


class ClosedLeavesMeetingPoint(Enum, IComparable, IFormattable, IConvertible):
    # type: (0), ClosedLeavesMeetingPoint_BankTwo (1), ClosedLeavesMeetingPoint_Center (2)
    """ enum ClosedLeavesMeetingPoint, values: ClosedLeavesMeetingPoint_BankOne (0), ClosedLeavesMeetingPoint_BankTwo (1), ClosedLeavesMeetingPoint_Center (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ClosedLeavesMeetingPoint_BankOne = None
    ClosedLeavesMeetingPoint_BankTwo = None
    ClosedLeavesMeetingPoint_Center = None
    value__ = None


class LineProfile(object, IEnumerable[ProfilePoint], IEnumerable):
    # type: (origin: VVector, step: VVector, data: Array[float])
    """ LineProfile(origin: VVector, step: VVector, data: Array[float]) """
    def GetEnumerator(self):
        # type: (self: LineProfile) -> IEnumerator[ProfilePoint]
        """ GetEnumerator(self: LineProfile) -> IEnumerator[ProfilePoint] """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ProfilePoint](enumerable: IEnumerable[ProfilePoint], value: ProfilePoint) -> bool """
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

    @staticmethod # known case of __new__
    def __new__(self, origin, step, data):
        """ __new__(cls: type, origin: VVector, step: VVector, data: Array[float]) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: LineProfile) -> int
    """ Get: Count(self: LineProfile) -> int """



class DoseProfile(LineProfile, IEnumerable[ProfilePoint], IEnumerable):
    # type: (origin: VVector, step: VVector, data: Array[float], unit: DoseUnit)
    """ DoseProfile(origin: VVector, step: VVector, data: Array[float], unit: DoseUnit) """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, origin, step, data, unit):
        """ __new__(cls: type, origin: VVector, step: VVector, data: Array[float], unit: DoseUnit) """
        pass

    Unit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: DoseProfile) -> DoseUnit
    """ Get: Unit(self: DoseProfile) -> DoseUnit """



class DoseValue(object, IXmlSerializable, IComparable[DoseValue], IEquatable[DoseValue]):
    # type: (value: float, unitName: str)

    """
    DoseValue(value: float, unitName: str)

    DoseValue(value: float, unit: DoseUnit)
    """
    def CompareTo(self, other):
        # type: (self: DoseValue, other: DoseValue) -> int
        """ CompareTo(self: DoseValue, other: DoseValue) -> int """
        pass

    def Equals(self, *__args):
        # type: (self: DoseValue, obj: object) -> bool

        """
        Equals(self: DoseValue, obj: object) -> bool

        Equals(self: DoseValue, other: DoseValue) -> bool

        Equals(self: DoseValue, other: DoseValue, epsilon: float) -> bool
        """
        pass

    def GetHashCode(self):
        # type: (self: DoseValue) -> int
        """ GetHashCode(self: DoseValue) -> int """
        pass

    def GetSchema(self):
        # type: (self: DoseValue) -> XmlSchema
        """ GetSchema(self: DoseValue) -> XmlSchema """
        pass

    @staticmethod
    def IsAbsoluteDoseUnit(doseUnit):
        # type: (doseUnit: DoseUnit) -> bool
        """ IsAbsoluteDoseUnit(doseUnit: DoseUnit) -> bool """
        pass

    @staticmethod
    def IsRelativeDoseUnit(doseUnit):
        # type: (doseUnit: DoseUnit) -> bool
        """ IsRelativeDoseUnit(doseUnit: DoseUnit) -> bool """
        pass

    def IsUndefined(self):
        # type: (self: DoseValue) -> bool
        """ IsUndefined(self: DoseValue) -> bool """
        pass

    def ReadXml(self, reader):
        # type: (self: DoseValue, reader: XmlReader)
        """ ReadXml(self: DoseValue, reader: XmlReader) """
        pass

    def ToString(self):
        # type: (self: DoseValue) -> str
        """ ToString(self: DoseValue) -> str """
        pass

    @staticmethod
    def UndefinedDose():
        # type: () -> DoseValue
        """ UndefinedDose() -> DoseValue """
        pass

    def WriteXml(self, writer):
        # type: (self: DoseValue, writer: XmlWriter)
        """ WriteXml(self: DoseValue, writer: XmlWriter) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/yx.__div__(y) <==> x/y """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, value, *__args):
        """
        __new__[DoseValue]() -> DoseValue

        

        __new__(cls: type, value: float, unitName: str)

        __new__(cls: type, value: float, unit: DoseUnit)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(dv1: DoseValue, dv2: DoseValue) -> DoseValue """
        pass

    def __rdiv__(self, *args): #cannot find CLR method
        """ __rdiv__(dv1: DoseValue, dv2: DoseValue) -> float """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(dbl: float, dv: DoseValue) -> DoseValue """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(dv1: DoseValue, dv2: DoseValue) -> DoseValue """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    Decimals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: DoseValue) -> int
    """ Get: Decimals(self: DoseValue) -> int """

    Dose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: DoseValue) -> float
    """ Get: Dose(self: DoseValue) -> float """

    IsAbsoluteDoseValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: DoseValue) -> bool
    """ Get: IsAbsoluteDoseValue(self: DoseValue) -> bool """

    IsRelativeDoseValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: DoseValue) -> bool
    """ Get: IsRelativeDoseValue(self: DoseValue) -> bool """

    Unit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: DoseValue) -> DoseUnit
    """ Get: Unit(self: DoseValue) -> DoseUnit """

    UnitAsString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: DoseValue) -> str
    """ Get: UnitAsString(self: DoseValue) -> str """

    ValueAsString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: DoseValue) -> str
    """ Get: ValueAsString(self: DoseValue) -> str """


    DoseUnit = None
    Undefined = None


class DoseValueDisplayConfig(object):
    # type: ()
    """ DoseValueDisplayConfig() """
    @staticmethod
    def Decimals(unit):
        # type: (unit: DoseUnit) -> int
        """ Decimals(unit: DoseUnit) -> int """
        pass

    DisplaySettings = None


class DoseValuePresentation(Enum, IComparable, IFormattable, IConvertible):
    # type: (1), Relative (0)
    """ enum DoseValuePresentation, values: Absolute (1), Relative (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Absolute = None
    Relative = None
    value__ = None


class DosimeterUnit(Enum, IComparable, IFormattable, IConvertible):
    # type: (2), MU (1), Null (0), Second (3)
    """ enum DosimeterUnit, values: Minute (2), MU (1), Null (0), Second (3) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Minute = None
    MU = None
    Null = None
    Second = None
    value__ = None


class DRRCalculationParameters(object):
    # type: ()

    """
    DRRCalculationParameters()

    DRRCalculationParameters(drrSize: float)

    DRRCalculationParameters(drrSize: float, weight: float, ctFrom: float, ctTo: float)

    DRRCalculationParameters(drrSize: float, weight: float, ctFrom: float, ctTo: float, geoFrom: float, geoTo: float)
    """
    def GetLayerParameters(self, index):
        # type: (self: DRRCalculationParameters, index: int) -> SingleLayerParameters
        """ GetLayerParameters(self: DRRCalculationParameters, index: int) -> SingleLayerParameters """
        pass

    def SetLayerParameters(self, index, weight, ctFrom, ctTo, geoFrom=None, geoTo=None):
        # type: (self: DRRCalculationParameters, index: int, weight: float, ctFrom: float, ctTo: float)SetLayerParameters(self: DRRCalculationParameters, index: int, weight: float, ctFrom: float, ctTo: float, geoFrom: float, geoTo: float)
        """ SetLayerParameters(self: DRRCalculationParameters, index: int, weight: float, ctFrom: float, ctTo: float)SetLayerParameters(self: DRRCalculationParameters, index: int, weight: float, ctFrom: float, ctTo: float, geoFrom: float, geoTo: float) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, drrSize=None, weight=None, ctFrom=None, ctTo=None, geoFrom=None, geoTo=None):
        """
        __new__(cls: type)

        __new__(cls: type, drrSize: float)

        __new__(cls: type, drrSize: float, weight: float, ctFrom: float, ctTo: float)

        __new__(cls: type, drrSize: float, weight: float, ctFrom: float, ctTo: float, geoFrom: float, geoTo: float)
        """
        pass

    DRRSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: DRRCalculationParameters) -> float

    """
    Get: DRRSize(self: DRRCalculationParameters) -> float

    

    Set: DRRSize(self: DRRCalculationParameters) = value
    """

    FieldOutlines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: DRRCalculationParameters) -> bool

    """
    Get: FieldOutlines(self: DRRCalculationParameters) -> bool

    

    Set: FieldOutlines(self: DRRCalculationParameters) = value
    """

    StructureOutlines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: DRRCalculationParameters) -> bool

    """
    Get: StructureOutlines(self: DRRCalculationParameters) -> bool

    

    Set: StructureOutlines(self: DRRCalculationParameters) = value
    """



class DVHEstimateType(Enum, IComparable, IFormattable, IConvertible):
    # type: (1), Undefined (99), Upper (0)
    """ enum DVHEstimateType, values: Lower (1), Undefined (99), Upper (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Lower = None
    Undefined = None
    Upper = None
    value__ = None


class DVHPoint(object, IXmlSerializable):
    # type: (dose: DoseValue, volume: float, volumeUnit: str)
    """ DVHPoint(dose: DoseValue, volume: float, volumeUnit: str) """
    def GetSchema(self):
        # type: (self: DVHPoint) -> XmlSchema
        """ GetSchema(self: DVHPoint) -> XmlSchema """
        pass

    def ReadXml(self, reader):
        # type: (self: DVHPoint, reader: XmlReader)
        """ ReadXml(self: DVHPoint, reader: XmlReader) """
        pass

    def WriteXml(self, writer):
        # type: (self: DVHPoint, writer: XmlWriter)
        """ WriteXml(self: DVHPoint, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, dose, volume, volumeUnit):
        """
        __new__[DVHPoint]() -> DVHPoint

        

        __new__(cls: type, dose: DoseValue, volume: float, volumeUnit: str)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DoseValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: DVHPoint) -> DoseValue
    """ Get: DoseValue(self: DVHPoint) -> DoseValue """

    Volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: DVHPoint) -> float
    """ Get: Volume(self: DVHPoint) -> float """

    VolumeUnit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: DVHPoint) -> str
    """ Get: VolumeUnit(self: DVHPoint) -> str """



class ExternalBeamMachineParameters(object):
    # type: (machineId: str, energyModeId: str, doseRate: int, techniqueId: str, primaryFluenceModeId: str)
    """ ExternalBeamMachineParameters(machineId: str, energyModeId: str, doseRate: int, techniqueId: str, primaryFluenceModeId: str) """
    @staticmethod # known case of __new__
    def __new__(self, machineId, energyModeId, doseRate, techniqueId, primaryFluenceModeId):
        """ __new__(cls: type, machineId: str, energyModeId: str, doseRate: int, techniqueId: str, primaryFluenceModeId: str) """
        pass

    DoseRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ExternalBeamMachineParameters) -> int

    """
    Get: DoseRate(self: ExternalBeamMachineParameters) -> int

    

    Set: DoseRate(self: ExternalBeamMachineParameters) = value
    """

    EnergyModeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ExternalBeamMachineParameters) -> str

    """
    Get: EnergyModeId(self: ExternalBeamMachineParameters) -> str

    

    Set: EnergyModeId(self: ExternalBeamMachineParameters) = value
    """

    MachineId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ExternalBeamMachineParameters) -> str

    """
    Get: MachineId(self: ExternalBeamMachineParameters) -> str

    

    Set: MachineId(self: ExternalBeamMachineParameters) = value
    """

    PrimaryFluenceModeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ExternalBeamMachineParameters) -> str

    """
    Get: PrimaryFluenceModeId(self: ExternalBeamMachineParameters) -> str

    

    Set: PrimaryFluenceModeId(self: ExternalBeamMachineParameters) = value
    """

    TechniqueId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ExternalBeamMachineParameters) -> str

    """
    Get: TechniqueId(self: ExternalBeamMachineParameters) -> str

    

    Set: TechniqueId(self: ExternalBeamMachineParameters) = value
    """



class FitToStructureMargins(object):
    # type: (x1: float, y1: float, x2: float, y2: float)

    """
    FitToStructureMargins(x1: float, y1: float, x2: float, y2: float)

    FitToStructureMargins(margin: float)
    """
    def ToString(self):
        # type: (self: FitToStructureMargins) -> str
        """ ToString(self: FitToStructureMargins) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[FitToStructureMargins]() -> FitToStructureMargins

        

        __new__(cls: type, x1: float, y1: float, x2: float, y2: float)

        __new__(cls: type, margin: float)
        """
        pass

    Type = None
    X1 = None
    X2 = None
    Y1 = None
    Y2 = None


class FitToStructureMarginType(Enum, IComparable, IFormattable, IConvertible):
    # type: (0), Elliptical (1)
    """ enum FitToStructureMarginType, values: Circular (0), Elliptical (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Circular = None
    Elliptical = None
    value__ = None


class Fluence(object):
    # type: (fluenceMatrix: Array[Single], xOrigin: float, yOrigin: float)

    """
    Fluence(fluenceMatrix: Array[Single], xOrigin: float, yOrigin: float)

    Fluence(fluenceMatrix: Array[Single], xOrigin: float, yOrigin: float, mlcId: str)
    """
    def GetPixels(self):
        # type: (self: Fluence) -> Array[Single]
        """ GetPixels(self: Fluence) -> Array[Single] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, fluenceMatrix, xOrigin, yOrigin, mlcId=None):
        """
        __new__(cls: type, fluenceMatrix: Array[Single], xOrigin: float, yOrigin: float)

        __new__(cls: type, fluenceMatrix: Array[Single], xOrigin: float, yOrigin: float, mlcId: str)
        """
        pass

    MLCId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Fluence) -> str
    """ Get: MLCId(self: Fluence) -> str """

    XOrigin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Fluence) -> float
    """ Get: XOrigin(self: Fluence) -> float """

    XSizeMM = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Fluence) -> float
    """ Get: XSizeMM(self: Fluence) -> float """

    XSizePixel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Fluence) -> int
    """ Get: XSizePixel(self: Fluence) -> int """

    YOrigin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Fluence) -> float
    """ Get: YOrigin(self: Fluence) -> float """

    YSizeMM = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Fluence) -> float
    """ Get: YSizeMM(self: Fluence) -> float """

    YSizePixel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Fluence) -> int
    """ Get: YSizePixel(self: Fluence) -> int """


    MaxSizePixel = 1024


class GantryDirection(Enum, IComparable, IFormattable, IConvertible):
    # type: (1), CounterClockwise (2), None (0)
    """ enum GantryDirection, values: Clockwise (1), CounterClockwise (2), None (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Clockwise = None
    CounterClockwise = None
    # None = None
    value__ = None


class IDoseValueDisplaySettings:
    # no doc
    def Decimals(self, unit):
        # type: (self: IDoseValueDisplaySettings, unit: DoseUnit) -> int
        """ Decimals(self: IDoseValueDisplaySettings, unit: DoseUnit) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ImageApprovalHistoryEntry(object):
    # no doc
    ApprovalDateTime = None
    ApprovalStatus = None
    StatusComment = None
    UserDisplayName = None
    UserId = None


class ImageApprovalStatus(Enum, IComparable, IFormattable, IConvertible):
    # type: (3), Approved (2), Disposed (4), New (0), Reviewed (1)
    """ enum ImageApprovalStatus, values: ActionRequired (3), Approved (2), Disposed (4), New (0), Reviewed (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ActionRequired = None
    Approved = None
    Disposed = None
    New = None
    Reviewed = None
    value__ = None


class ImageProfile(LineProfile, IEnumerable[ProfilePoint], IEnumerable):
    # type: (origin: VVector, step: VVector, data: Array[float], unit: str)
    """ ImageProfile(origin: VVector, step: VVector, data: Array[float], unit: str) """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, origin, step, data, unit):
        """ __new__(cls: type, origin: VVector, step: VVector, data: Array[float], unit: str) """
        pass

    Unit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ImageProfile) -> str
    """ Get: Unit(self: ImageProfile) -> str """



class ImagingSetup(Enum, IComparable, IFormattable, IConvertible):
    # type: (4), MV_MV_High_Quality (2), MV_MV_Low_Dose (3), MVCBCT_High_Quality (0), MVCBCT_Low_Dose (1)
    """ enum ImagingSetup, values: kVCBCT (4), MV_MV_High_Quality (2), MV_MV_Low_Dose (3), MVCBCT_High_Quality (0), MVCBCT_Low_Dose (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    kVCBCT = None
    MVCBCT_High_Quality = None
    MVCBCT_Low_Dose = None
    MV_MV_High_Quality = None
    MV_MV_Low_Dose = None
    value__ = None


class IonBeamScanMode(Enum, IComparable, IFormattable, IConvertible):
    # type: (4), Modulated (2), None (0), Uniform (1), Unknown (999), Wobbling (3)
    """ enum IonBeamScanMode, values: Line (4), Modulated (2), None (0), Uniform (1), Unknown (999), Wobbling (3) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Line = None
    Modulated = None
    # None = None
    Uniform = None
    Unknown = None
    value__ = None
    Wobbling = None


class JawFitting(Enum, IComparable, IFormattable, IConvertible):
    # type: (1), FitToStructure (2), None (0)
    """ enum JawFitting, values: FitToRecommended (1), FitToStructure (2), None (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    FitToRecommended = None
    FitToStructure = None
    # None = None
    value__ = None


class LateralSpreadingDeviceType(Enum, IComparable, IFormattable, IConvertible):
    # type: (1), Scatterer (0)
    """ enum LateralSpreadingDeviceType, values: Magnet (1), Scatterer (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Magnet = None
    Scatterer = None
    value__ = None


class LMCMSSOptions(object):
    # type: (numberOfIterations: int)
    """ LMCMSSOptions(numberOfIterations: int) """
    @staticmethod # known case of __new__
    def __new__(self, numberOfIterations):
        """ __new__(cls: type, numberOfIterations: int) """
        pass

    NumberOfIterations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: LMCMSSOptions) -> int
    """ Get: NumberOfIterations(self: LMCMSSOptions) -> int """



class LMCVOptions(object):
    # type: (fixedJaws: bool)
    """ LMCVOptions(fixedJaws: bool) """
    @staticmethod # known case of __new__
    def __new__(self, fixedJaws):
        """ __new__(cls: type, fixedJaws: bool) """
        pass

    FixedJaws = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: LMCVOptions) -> bool
    """ Get: FixedJaws(self: LMCVOptions) -> bool """



class MeasureModifier(Enum, IComparable, IFormattable, IConvertible):
    # type: (0), MeasureModifierAtMost (1), MeasureModifierNone (99), MeasureModifierTarget (2)
    """ enum MeasureModifier, values: MeasureModifierAtLeast (0), MeasureModifierAtMost (1), MeasureModifierNone (99), MeasureModifierTarget (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    MeasureModifierAtLeast = None
    MeasureModifierAtMost = None
    MeasureModifierNone = None
    MeasureModifierTarget = None
    value__ = None


class MeasureType(Enum, IComparable, IFormattable, IConvertible):
    # type: (0), MeasureTypeDQP_DXXX (4), MeasureTypeDQP_DXXXcc (5), MeasureTypeDQP_VXXX (2), MeasureTypeDQP_VXXXGy (3), MeasureTypeGradient (1), MeasureTypeNone (99)
    """ enum MeasureType, values: MeasureTypeDoseConformity (0), MeasureTypeDQP_DXXX (4), MeasureTypeDQP_DXXXcc (5), MeasureTypeDQP_VXXX (2), MeasureTypeDQP_VXXXGy (3), MeasureTypeGradient (1), MeasureTypeNone (99) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    MeasureTypeDoseConformity = None
    MeasureTypeDQP_DXXX = None
    MeasureTypeDQP_DXXXcc = None
    MeasureTypeDQP_VXXX = None
    MeasureTypeDQP_VXXXGy = None
    MeasureTypeGradient = None
    MeasureTypeNone = None
    value__ = None


class MetersetValue(object, IXmlSerializable):
    # type: (value: float, unit: DosimeterUnit)
    """ MetersetValue(value: float, unit: DosimeterUnit) """
    def GetSchema(self):
        # type: (self: MetersetValue) -> XmlSchema
        """ GetSchema(self: MetersetValue) -> XmlSchema """
        pass

    def ReadXml(self, reader):
        # type: (self: MetersetValue, reader: XmlReader)
        """ ReadXml(self: MetersetValue, reader: XmlReader) """
        pass

    def WriteXml(self, writer):
        # type: (self: MetersetValue, writer: XmlWriter)
        """ WriteXml(self: MetersetValue, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, value, unit):
        """
        __new__[MetersetValue]() -> MetersetValue

        

        __new__(cls: type, value: float, unit: DosimeterUnit)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Unit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: MetersetValue) -> DosimeterUnit
    """ Get: Unit(self: MetersetValue) -> DosimeterUnit """

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: MetersetValue) -> float
    """ Get: Value(self: MetersetValue) -> float """



class MLCPlanType(Enum, IComparable, IFormattable, IConvertible):
    # type: (2), DoseDynamic (1), NotDefined (999), ProtonLayerStacking (4), Static (0), VMAT (3)
    """ enum MLCPlanType, values: ArcDynamic (2), DoseDynamic (1), NotDefined (999), ProtonLayerStacking (4), Static (0), VMAT (3) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ArcDynamic = None
    DoseDynamic = None
    NotDefined = None
    ProtonLayerStacking = None
    Static = None
    value__ = None
    VMAT = None


class OpenLeavesMeetingPoint(Enum, IComparable, IFormattable, IConvertible):
    # type: (0), OpenLeavesMeetingPoint_Middle (2), OpenLeavesMeetingPoint_Outside (1)
    """ enum OpenLeavesMeetingPoint, values: OpenLeavesMeetingPoint_Inside (0), OpenLeavesMeetingPoint_Middle (2), OpenLeavesMeetingPoint_Outside (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    OpenLeavesMeetingPoint_Inside = None
    OpenLeavesMeetingPoint_Middle = None
    OpenLeavesMeetingPoint_Outside = None
    value__ = None


class OptimizationConvergenceOption(Enum, IComparable, IFormattable, IConvertible):
    # type: (0), TerminateIfConverged (1)
    """ enum OptimizationConvergenceOption, values: NoEarlyTermination (0), TerminateIfConverged (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    NoEarlyTermination = None
    TerminateIfConverged = None
    value__ = None


class OptimizationIntermediateDoseOption(Enum, IComparable, IFormattable, IConvertible):
    # type: (0), UseIntermediateDose (1)
    """ enum OptimizationIntermediateDoseOption, values: NoIntermediateDose (0), UseIntermediateDose (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    NoIntermediateDose = None
    UseIntermediateDose = None
    value__ = None


class OptimizationObjectiveOperator(Enum, IComparable, IFormattable, IConvertible):
    # type: (2), Lower (1), None (99), Upper (0)
    """ enum OptimizationObjectiveOperator, values: Exact (2), Lower (1), None (99), Upper (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Exact = None
    Lower = None
    # None = None
    Upper = None
    value__ = None


class OptimizationOption(Enum, IComparable, IFormattable, IConvertible):
    # type: (1), ContinueOptimizationWithPlanDoseAsIntermediateDose (2), RestartOptimization (0)
    """ enum OptimizationOption, values: ContinueOptimization (1), ContinueOptimizationWithPlanDoseAsIntermediateDose (2), RestartOptimization (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ContinueOptimization = None
    ContinueOptimizationWithPlanDoseAsIntermediateDose = None
    RestartOptimization = None
    value__ = None


class OptimizationOptionsBase(object):
    # no doc
    IntermediateDoseOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizationOptionsBase) -> OptimizationIntermediateDoseOption
    """ Get: IntermediateDoseOption(self: OptimizationOptionsBase) -> OptimizationIntermediateDoseOption """

    MLC = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizationOptionsBase) -> str
    """ Get: MLC(self: OptimizationOptionsBase) -> str """

    StartOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizationOptionsBase) -> OptimizationOption
    """ Get: StartOption(self: OptimizationOptionsBase) -> OptimizationOption """



class OptimizationOptionsIMRT(OptimizationOptionsBase):
    # type: (maxIterations: int, initialState: OptimizationOption, numberOfStepsBeforeIntermediateDose: int, convergenceOption: OptimizationConvergenceOption, mlcId: str)

    """
    OptimizationOptionsIMRT(maxIterations: int, initialState: OptimizationOption, numberOfStepsBeforeIntermediateDose: int, convergenceOption: OptimizationConvergenceOption, mlcId: str)

    OptimizationOptionsIMRT(maxIterations: int, initialState: OptimizationOption, convergenceOption: OptimizationConvergenceOption, intermediateDoseOption: OptimizationIntermediateDoseOption, mlcId: str)

    OptimizationOptionsIMRT(maxIterations: int, initialState: OptimizationOption, convergenceOption: OptimizationConvergenceOption, mlcId: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, maxIterations, initialState, *__args):
        """
        __new__(cls: type, maxIterations: int, initialState: OptimizationOption, numberOfStepsBeforeIntermediateDose: int, convergenceOption: OptimizationConvergenceOption, mlcId: str)

        __new__(cls: type, maxIterations: int, initialState: OptimizationOption, convergenceOption: OptimizationConvergenceOption, intermediateDoseOption: OptimizationIntermediateDoseOption, mlcId: str)

        __new__(cls: type, maxIterations: int, initialState: OptimizationOption, convergenceOption: OptimizationConvergenceOption, mlcId: str)
        """
        pass

    ConvergenceOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizationOptionsIMRT) -> OptimizationConvergenceOption
    """ Get: ConvergenceOption(self: OptimizationOptionsIMRT) -> OptimizationConvergenceOption """

    MaximumNumberOfIterations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizationOptionsIMRT) -> int
    """ Get: MaximumNumberOfIterations(self: OptimizationOptionsIMRT) -> int """

    NumberOfStepsBeforeIntermediateDose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizationOptionsIMRT) -> int
    """ Get: NumberOfStepsBeforeIntermediateDose(self: OptimizationOptionsIMRT) -> int """



class OptimizationOptionsVMAT(OptimizationOptionsBase):
    # type: (startOption: OptimizationOption, mlcId: str)

    """
    OptimizationOptionsVMAT(startOption: OptimizationOption, mlcId: str)

    OptimizationOptionsVMAT(intermediateDoseOption: OptimizationIntermediateDoseOption, mlcId: str)

    OptimizationOptionsVMAT(numberOfCycles: int, mlcId: str)

    OptimizationOptionsVMAT(options: OptimizationOptionsVMAT)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, startOption: OptimizationOption, mlcId: str)

        __new__(cls: type, intermediateDoseOption: OptimizationIntermediateDoseOption, mlcId: str)

        __new__(cls: type, numberOfCycles: int, mlcId: str)

        __new__(cls: type, startOption: OptimizationOption, intermediateDoseOption: OptimizationIntermediateDoseOption, numberOfCycles: int, mlcId: str)

        __new__(cls: type, options: OptimizationOptionsVMAT)
        """
        pass

    NumberOfOptimizationCycles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizationOptionsVMAT) -> int
    """ Get: NumberOfOptimizationCycles(self: OptimizationOptionsVMAT) -> int """



class PatientOrientation(Enum, IComparable, IFormattable, IConvertible):
    # type: (8), FeetFirstDecubitusRight (7), FeetFirstProne (6), FeetFirstSupine (5), HeadFirstDecubitusLeft (4), HeadFirstDecubitusRight (3), HeadFirstProne (2), HeadFirstSupine (1), NoOrientation (0), Sitting (9)
    """ enum PatientOrientation, values: FeetFirstDecubitusLeft (8), FeetFirstDecubitusRight (7), FeetFirstProne (6), FeetFirstSupine (5), HeadFirstDecubitusLeft (4), HeadFirstDecubitusRight (3), HeadFirstProne (2), HeadFirstSupine (1), NoOrientation (0), Sitting (9) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    FeetFirstDecubitusLeft = None
    FeetFirstDecubitusRight = None
    FeetFirstProne = None
    FeetFirstSupine = None
    HeadFirstDecubitusLeft = None
    HeadFirstDecubitusRight = None
    HeadFirstProne = None
    HeadFirstSupine = None
    NoOrientation = None
    Sitting = None
    value__ = None


class PatientSupportType(Enum, IComparable, IFormattable, IConvertible):
    # type: (1), Table (0)
    """ enum PatientSupportType, values: Chair (1), Table (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Chair = None
    Table = None
    value__ = None


class PlanSetupApprovalStatus(Enum, IComparable, IFormattable, IConvertible):
    # type: (6), CompletedEarly (5), ExternallyApproved (9), PlanningApproved (3), Rejected (0), Retired (7), Reviewed (2), TreatmentApproved (4), UnApproved (1), Unknown (999), UnPlannedTreatment (8)
    """ enum PlanSetupApprovalStatus, values: Completed (6), CompletedEarly (5), ExternallyApproved (9), PlanningApproved (3), Rejected (0), Retired (7), Reviewed (2), TreatmentApproved (4), UnApproved (1), Unknown (999), UnPlannedTreatment (8) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Completed = None
    CompletedEarly = None
    ExternallyApproved = None
    PlanningApproved = None
    Rejected = None
    Retired = None
    Reviewed = None
    TreatmentApproved = None
    UnApproved = None
    Unknown = None
    UnPlannedTreatment = None
    value__ = None


class PlanSumOperation(Enum, IComparable, IFormattable, IConvertible):
    # type: (0), Subtraction (1), Undefined (-1)
    """ enum PlanSumOperation, values: Addition (0), Subtraction (1), Undefined (-1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Addition = None
    Subtraction = None
    Undefined = None
    value__ = None


class PlanType(Enum, IComparable, IFormattable, IConvertible):
    # type: (3), ExternalBeam (0), ExternalBeam_IRREG (1), ExternalBeam_Proton (2)
    """ enum PlanType, values: Brachy (3), ExternalBeam (0), ExternalBeam_IRREG (1), ExternalBeam_Proton (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Brachy = None
    ExternalBeam = None
    ExternalBeam_IRREG = None
    ExternalBeam_Proton = None
    value__ = None


class PlanUncertaintyType(Enum, IComparable, IFormattable, IConvertible):
    # type: (3), IsocenterShiftUncertainty (2), RangeUncertainty (1), RobustOptimizationUncertainty (4), UncertaintyTypeNotDefined (0)
    """ enum PlanUncertaintyType, values: BaselineShiftUncertainty (3), IsocenterShiftUncertainty (2), RangeUncertainty (1), RobustOptimizationUncertainty (4), UncertaintyTypeNotDefined (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BaselineShiftUncertainty = None
    IsocenterShiftUncertainty = None
    RangeUncertainty = None
    RobustOptimizationUncertainty = None
    UncertaintyTypeNotDefined = None
    value__ = None


class PrescriptionModifier(Enum, IComparable, IFormattable, IConvertible):
    # type: (0), PrescriptionModifierAtMost (1), PrescriptionModifierDMax (20), PrescriptionModifierEUD (6), PrescriptionModifierIsodose (40), PrescriptionModifierMaxDose (3), PrescriptionModifierMaxDoseAtMost (10), PrescriptionModifierMeanDose (2), PrescriptionModifierMeanDoseAtLeast (7), PrescriptionModifierMeanDoseAtMost (8), PrescriptionModifierMidPoint (21), PrescriptionModifierMinDose (4), PrescriptionModifierMinDoseAtLeast (9), PrescriptionModifierNone (99), PrescriptionModifierRefPoint (5), PrescriptionModifierUser (22)
    """ enum PrescriptionModifier, values: PrescriptionModifierAtLeast (0), PrescriptionModifierAtMost (1), PrescriptionModifierDMax (20), PrescriptionModifierEUD (6), PrescriptionModifierIsodose (40), PrescriptionModifierMaxDose (3), PrescriptionModifierMaxDoseAtMost (10), PrescriptionModifierMeanDose (2), PrescriptionModifierMeanDoseAtLeast (7), PrescriptionModifierMeanDoseAtMost (8), PrescriptionModifierMidPoint (21), PrescriptionModifierMinDose (4), PrescriptionModifierMinDoseAtLeast (9), PrescriptionModifierNone (99), PrescriptionModifierRefPoint (5), PrescriptionModifierUser (22) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    PrescriptionModifierAtLeast = None
    PrescriptionModifierAtMost = None
    PrescriptionModifierDMax = None
    PrescriptionModifierEUD = None
    PrescriptionModifierIsodose = None
    PrescriptionModifierMaxDose = None
    PrescriptionModifierMaxDoseAtMost = None
    PrescriptionModifierMeanDose = None
    PrescriptionModifierMeanDoseAtLeast = None
    PrescriptionModifierMeanDoseAtMost = None
    PrescriptionModifierMidPoint = None
    PrescriptionModifierMinDose = None
    PrescriptionModifierMinDoseAtLeast = None
    PrescriptionModifierNone = None
    PrescriptionModifierRefPoint = None
    PrescriptionModifierUser = None
    value__ = None


class PrescriptionType(Enum, IComparable, IFormattable, IConvertible):
    # type: (1), PrescriptionTypeIsodose (2), PrescriptionTypeNone (99), PrescriptionTypeVolume (0)
    """ enum PrescriptionType, values: PrescriptionTypeDepth (1), PrescriptionTypeIsodose (2), PrescriptionTypeNone (99), PrescriptionTypeVolume (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    PrescriptionTypeDepth = None
    PrescriptionTypeIsodose = None
    PrescriptionTypeNone = None
    PrescriptionTypeVolume = None
    value__ = None


class ProfilePoint(object):
    # type: (position: VVector, value: float)
    """ ProfilePoint(position: VVector, value: float) """
    @staticmethod # known case of __new__
    def __new__(self, position, value):
        """
        __new__[ProfilePoint]() -> ProfilePoint

        

        __new__(cls: type, position: VVector, value: float)
        """
        pass

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ProfilePoint) -> VVector
    """ Get: Position(self: ProfilePoint) -> VVector """

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ProfilePoint) -> float
    """ Get: Value(self: ProfilePoint) -> float """



class RangeModulatorType(Enum, IComparable, IFormattable, IConvertible):
    # type: (0), Whl_FixedWeights (1), Whl_ModWeights (2)
    """ enum RangeModulatorType, values: Fixed (0), Whl_FixedWeights (1), Whl_ModWeights (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Fixed = None
    value__ = None
    Whl_FixedWeights = None
    Whl_ModWeights = None


class RangeShifterType(Enum, IComparable, IFormattable, IConvertible):
    # type: (0), Binary (1)
    """ enum RangeShifterType, values: Analog (0), Binary (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Analog = None
    Binary = None
    value__ = None


class RegistrationApprovalStatus(Enum, IComparable, IFormattable, IConvertible):
    # type: (1), Retired (2), Reviewed (3), Unapproved (0)
    """ enum RegistrationApprovalStatus, values: Approved (1), Retired (2), Reviewed (3), Unapproved (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Approved = None
    Retired = None
    Reviewed = None
    Unapproved = None
    value__ = None


class RendererStrings(Enum, IComparable, IFormattable, IConvertible):
    # type: (20), BrachyFractions (11), Catheters (18), CumulativeDVH (13), DoseZRes (21), FinalSpotList (10), Isodoses (7), LengthUnit (6), NormalizationInvalid (12), OrientationLabelAnterior (2), OrientationLabelFeet (5), OrientationLabelHead (4), OrientationLabelLeft (0), OrientationLabelPosterior (3), OrientationLabelRight (1), PlanInTreatment (15), Seeds (19), WarningAddOns (8), WarningArc (9), WarningCAXOnly (14), WarningConcurrency (16), WarningPlanWeights (17)
    """ enum RendererStrings, values: Applicators (20), BrachyFractions (11), Catheters (18), CumulativeDVH (13), DoseZRes (21), FinalSpotList (10), Isodoses (7), LengthUnit (6), NormalizationInvalid (12), OrientationLabelAnterior (2), OrientationLabelFeet (5), OrientationLabelHead (4), OrientationLabelLeft (0), OrientationLabelPosterior (3), OrientationLabelRight (1), PlanInTreatment (15), Seeds (19), WarningAddOns (8), WarningArc (9), WarningCAXOnly (14), WarningConcurrency (16), WarningPlanWeights (17) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Applicators = None
    BrachyFractions = None
    Catheters = None
    CumulativeDVH = None
    DoseZRes = None
    FinalSpotList = None
    Isodoses = None
    LengthUnit = None
    NormalizationInvalid = None
    OrientationLabelAnterior = None
    OrientationLabelFeet = None
    OrientationLabelHead = None
    OrientationLabelLeft = None
    OrientationLabelPosterior = None
    OrientationLabelRight = None
    PlanInTreatment = None
    Seeds = None
    value__ = None
    WarningAddOns = None
    WarningArc = None
    WarningCAXOnly = None
    WarningConcurrency = None
    WarningPlanWeights = None


class RTPrescriptionConstraintType(Enum, IComparable, IFormattable, IConvertible):
    # type: (5), MaximumDose (1), MaximumDvhDose (3), MaximumMeanDose (4), MinimumDose (0), MinimumDvhDose (2)
    """ enum RTPrescriptionConstraintType, values: FreeText (5), MaximumDose (1), MaximumDvhDose (3), MaximumMeanDose (4), MinimumDose (0), MinimumDvhDose (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    FreeText = None
    MaximumDose = None
    MaximumDvhDose = None
    MaximumMeanDose = None
    MinimumDose = None
    MinimumDvhDose = None
    value__ = None


class RTPrescriptionTargetType(Enum, IComparable, IFormattable, IConvertible):
    # type: (1), Isocenter (2), IsodoseLine (3), Undefined (99), Volume (0)
    """ enum RTPrescriptionTargetType, values: Depth (1), Isocenter (2), IsodoseLine (3), Undefined (99), Volume (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Depth = None
    Isocenter = None
    IsodoseLine = None
    Undefined = None
    value__ = None
    Volume = None


class SegmentProfile(object, IEnumerable[SegmentProfilePoint], IEnumerable):
    # type: (origin: VVector, step: VVector, data: BitArray)
    """ SegmentProfile(origin: VVector, step: VVector, data: BitArray) """
    def GetEnumerator(self):
        # type: (self: SegmentProfile) -> IEnumerator[SegmentProfilePoint]
        """ GetEnumerator(self: SegmentProfile) -> IEnumerator[SegmentProfilePoint] """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[SegmentProfilePoint](enumerable: IEnumerable[SegmentProfilePoint], value: SegmentProfilePoint) -> bool """
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

    @staticmethod # known case of __new__
    def __new__(self, origin, step, data):
        """ __new__(cls: type, origin: VVector, step: VVector, data: BitArray) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: SegmentProfile) -> int
    """ Get: Count(self: SegmentProfile) -> int """

    EdgeCoordinates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: SegmentProfile) -> IList[VVector]
    """ Get: EdgeCoordinates(self: SegmentProfile) -> IList[VVector] """



class SegmentProfilePoint(object):
    # type: (position: VVector, value: bool)
    """ SegmentProfilePoint(position: VVector, value: bool) """
    @staticmethod # known case of __new__
    def __new__(self, position, value):
        """
        __new__[SegmentProfilePoint]() -> SegmentProfilePoint

        

        __new__(cls: type, position: VVector, value: bool)
        """
        pass

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: SegmentProfilePoint) -> VVector
    """ Get: Position(self: SegmentProfilePoint) -> VVector """

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: SegmentProfilePoint) -> bool
    """ Get: Value(self: SegmentProfilePoint) -> bool """



class SeriesModality(Enum, IComparable, IFormattable, IConvertible):
    # type: (0), MR (1), Other (8), PT (2), REG (7), RTDOSE (6), RTIMAGE (3), RTPLAN (5), RTSTRUCT (4)
    """ enum SeriesModality, values: CT (0), MR (1), Other (8), PT (2), REG (7), RTDOSE (6), RTIMAGE (3), RTPLAN (5), RTSTRUCT (4) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CT = None
    MR = None
    Other = None
    PT = None
    REG = None
    RTDOSE = None
    RTIMAGE = None
    RTPLAN = None
    RTSTRUCT = None
    value__ = None


class SetupTechnique(Enum, IComparable, IFormattable, IConvertible):
    # type: (4), FixedSSD (2), Isocentric (1), SkinApposition (5), TBI (3), Unknown (0)
    """ enum SetupTechnique, values: BreastBridge (4), FixedSSD (2), Isocentric (1), SkinApposition (5), TBI (3), Unknown (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BreastBridge = None
    FixedSSD = None
    Isocentric = None
    SkinApposition = None
    TBI = None
    Unknown = None
    value__ = None


class SingleLayerParameters(object):
    # no doc
    CTFrom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: SingleLayerParameters) -> float

    """
    Get: CTFrom(self: SingleLayerParameters) -> float

    

    Set: CTFrom(self: SingleLayerParameters) = value
    """

    CTTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: SingleLayerParameters) -> float

    """
    Get: CTTo(self: SingleLayerParameters) -> float

    

    Set: CTTo(self: SingleLayerParameters) = value
    """

    GeoClipping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: SingleLayerParameters) -> bool

    """
    Get: GeoClipping(self: SingleLayerParameters) -> bool

    

    Set: GeoClipping(self: SingleLayerParameters) = value
    """

    GeoFrom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: SingleLayerParameters) -> float

    """
    Get: GeoFrom(self: SingleLayerParameters) -> float

    

    Set: GeoFrom(self: SingleLayerParameters) = value
    """

    GeoTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: SingleLayerParameters) -> float

    """
    Get: GeoTo(self: SingleLayerParameters) -> float

    

    Set: GeoTo(self: SingleLayerParameters) = value
    """

    LayerOn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: SingleLayerParameters) -> bool

    """
    Get: LayerOn(self: SingleLayerParameters) -> bool

    

    Set: LayerOn(self: SingleLayerParameters) = value
    """

    Weight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: SingleLayerParameters) -> float

    """
    Get: Weight(self: SingleLayerParameters) -> float

    

    Set: Weight(self: SingleLayerParameters) = value
    """



class SmartLMCOptions(object):
    # type: (fixedFieldBorders: bool, jawTracking: bool)
    """ SmartLMCOptions(fixedFieldBorders: bool, jawTracking: bool) """
    @staticmethod # known case of __new__
    def __new__(self, fixedFieldBorders, jawTracking):
        """ __new__(cls: type, fixedFieldBorders: bool, jawTracking: bool) """
        pass

    FixedFieldBorders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: SmartLMCOptions) -> bool
    """ Get: FixedFieldBorders(self: SmartLMCOptions) -> bool """

    JawTracking = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: SmartLMCOptions) -> bool
    """ Get: JawTracking(self: SmartLMCOptions) -> bool """



class StructureApprovalHistoryEntry(object):
    # no doc
    ApprovalDateTime = None
    ApprovalStatus = None
    StatusComment = None
    UserDisplayName = None
    UserId = None


class StructureApprovalStatus(Enum, IComparable, IFormattable, IConvertible):
    # type: (1), Rejected (2), Reviewed (3), UnApproved (0)
    """ enum StructureApprovalStatus, values: Approved (1), Rejected (2), Reviewed (3), UnApproved (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Approved = None
    Rejected = None
    Reviewed = None
    UnApproved = None
    value__ = None


class StructureCodeInfo(object, IXmlSerializable, IEquatable[StructureCodeInfo]):
    # type: (codingScheme: str, code: str)
    """ StructureCodeInfo(codingScheme: str, code: str) """
    def Equals(self, *__args):
        # type: (self: StructureCodeInfo, obj: object) -> bool

        """
        Equals(self: StructureCodeInfo, obj: object) -> bool

        Equals(self: StructureCodeInfo, other: StructureCodeInfo) -> bool
        """
        pass

    def GetHashCode(self):
        # type: (self: StructureCodeInfo) -> int
        """ GetHashCode(self: StructureCodeInfo) -> int """
        pass

    def GetSchema(self):
        # type: (self: StructureCodeInfo) -> XmlSchema
        """ GetSchema(self: StructureCodeInfo) -> XmlSchema """
        pass

    def ReadXml(self, reader):
        # type: (self: StructureCodeInfo, reader: XmlReader)
        """ ReadXml(self: StructureCodeInfo, reader: XmlReader) """
        pass

    def ToString(self):
        # type: (self: StructureCodeInfo) -> str
        """ ToString(self: StructureCodeInfo) -> str """
        pass

    def WriteXml(self, writer):
        # type: (self: StructureCodeInfo, writer: XmlWriter)
        """ WriteXml(self: StructureCodeInfo, writer: XmlWriter) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, codingScheme, code):
        """
        __new__[StructureCodeInfo]() -> StructureCodeInfo

        

        __new__(cls: type, codingScheme: str, code: str)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: StructureCodeInfo) -> str
    """ Get: Code(self: StructureCodeInfo) -> str """

    CodingScheme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: StructureCodeInfo) -> str
    """ Get: CodingScheme(self: StructureCodeInfo) -> str """



class StructureMarginGeometry(Enum, IComparable, IFormattable, IConvertible):
    # type: (1), Outer (0)
    """ enum StructureMarginGeometry, values: Inner (1), Outer (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Inner = None
    Outer = None
    value__ = None


class TreatmentSessionStatus(Enum, IComparable, IFormattable, IConvertible):
    # type: (3), CompletedPartially (4), InActiveResume (6), InActiveTreat (5), Null (0), Resume (2), Treat (1)
    """ enum TreatmentSessionStatus, values: Completed (3), CompletedPartially (4), InActiveResume (6), InActiveTreat (5), Null (0), Resume (2), Treat (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Completed = None
    CompletedPartially = None
    InActiveResume = None
    InActiveTreat = None
    Null = None
    Resume = None
    Treat = None
    value__ = None


class UserIdentity(object):
    # type: (id: str, displayName: str)
    """ UserIdentity(id: str, displayName: str) """
    @staticmethod # known case of __new__
    def __new__(self, id, displayName):
        """
        __new__[UserIdentity]() -> UserIdentity

        

        __new__(cls: type, id: str, displayName: str)
        """
        pass

    DisplayName = None
    Id = None


class ValidationException(ApplicationException, ISerializable, _Exception):
    # type: (reason: str)
    """ ValidationException(reason: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, reason):
        """ __new__(cls: type, reason: str) """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SerializeObjectState = None


class VolumePresentation(Enum, IComparable, IFormattable, IConvertible):
    # type: (1), Relative (0)
    """ enum VolumePresentation, values: AbsoluteCm3 (1), Relative (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AbsoluteCm3 = None
    Relative = None
    value__ = None


class VRect(object):
    # type: (x1: T, y1: T, x2: T, y2: T)
    """ VRect[T](x1: T, y1: T, x2: T, y2: T) """
    def Equals(self, *__args):
        # type: (self: VRect[T], obj: object) -> bool

        """
        Equals(self: VRect[T], obj: object) -> bool

        Equals(self: VRect[T], other: VRect[T]) -> bool
        """
        pass

    def GetHashCode(self):
        # type: (self: VRect[T]) -> int
        """ GetHashCode(self: VRect[T]) -> int """
        pass

    def ToString(self):
        # type: (self: VRect[T]) -> str
        """ ToString(self: VRect[T]) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, x1, y1, x2, y2):
        """
        __new__[VRect`1]() -> VRect[T]

        

        __new__(cls: type, x1: T, y1: T, x2: T, y2: T)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    X1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: VRect[T]) -> T
    """ Get: X1(self: VRect[T]) -> T """

    X2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: VRect[T]) -> T
    """ Get: X2(self: VRect[T]) -> T """

    Y1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: VRect[T]) -> T
    """ Get: Y1(self: VRect[T]) -> T """

    Y2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: VRect[T]) -> T
    """ Get: Y2(self: VRect[T]) -> T """



class VVector(object):
    # type: (xi: float, yi: float, zi: float)
    """ VVector(xi: float, yi: float, zi: float) """
    @staticmethod
    def Distance(left, right):
        # type: (left: VVector, right: VVector) -> float
        """ Distance(left: VVector, right: VVector) -> float """
        pass

    def ScalarProduct(self, left):
        # type: (self: VVector, left: VVector) -> float
        """ ScalarProduct(self: VVector, left: VVector) -> float """
        pass

    def ScaleToUnitLength(self):
        # type: (self: VVector)
        """ ScaleToUnitLength(self: VVector) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, xi, yi, zi):
        """
        __new__[VVector]() -> VVector

        

        __new__(cls: type, xi: float, yi: float, zi: float)
        """
        pass

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(left: VVector, right: VVector) -> VVector """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(mul: float, val: VVector) -> VVector """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(left: VVector, right: VVector) -> VVector """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: VVector) -> float
    """ Get: Length(self: VVector) -> float """

    LengthSquared = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: VVector) -> float
    """ Get: LengthSquared(self: VVector) -> float """

    x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: VVector) -> float

    """
    Get: x(self: VVector) -> float

    

    Set: x(self: VVector) = value
    """

    y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: VVector) -> float

    """
    Get: y(self: VVector) -> float

    

    Set: y(self: VVector) = value
    """

    z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: VVector) -> float

    """
    Get: z(self: VVector) -> float

    

    Set: z(self: VVector) = value
    """



