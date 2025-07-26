from typing import Any, Dict, Generic, List, Optional, Union, overload
from datetime import datetime
from System import Array, Enum, Type, ValueType
from System.Collections import BitArray, IEnumerator
from System.Xml import XmlReader, XmlWriter
from System.Xml.Schema import XmlSchema
from Microsoft.Win32 import RegistryHive
from System import AggregateException, ApplicationException, Exception, IComparable, TypeCode
from System.Collections import DictionaryBase
from System.Globalization import CultureInfo
from System.Reflection import MethodBase
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import SerializationInfo, StreamingContext
from VMS.TPS.Common.Model.API import AddOn

class ApplicationScriptApprovalStatus:
    """The approval statuses of the application script."""

    Approved: ApplicationScriptApprovalStatus
    ApprovedForEvaluation: ApplicationScriptApprovalStatus
    Retired: ApplicationScriptApprovalStatus
    Unapproved: ApplicationScriptApprovalStatus
    Undefined: ApplicationScriptApprovalStatus

class ApplicationScriptType:
    """The type of the application script."""

    ESAPI: ApplicationScriptType
    ESAPIActionPack: ApplicationScriptType
    ESAPIApprovalHook: ApplicationScriptType
    ESAPICustomExecutable: ApplicationScriptType
    MIRS: ApplicationScriptType
    Unknown: ApplicationScriptType

class ApprovalHistoryEntry(ValueType):
    """An entry in the plan approval history."""

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

    ApprovalDateTime: datetime
    ApprovalStatus: PlanSetupApprovalStatus
    StatusComment: str
    UserDisplayName: str
    UserId: str

class AxisAlignedMargins(ValueType):
    """Represents margins aligned to the axes of the image coordinate system, in mm. Negative margins are not allowed, but it is possible to specify whether the margins represent an inner or outer margin."""

    def __init__(self, geometry: StructureMarginGeometry, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> None:
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
        """A string that represents the current object.
        
        Returns:
            str: A string that represents the current object."""
        ...

    Geometry: StructureMarginGeometry
    X1: float
    X2: float
    Y1: float
    Y2: float
    Z1: float
    Z2: float

class BeamNumber(ValueType):
    """Represents a unique identifier for a beam of a plan. The identifier is unique within the scope of the plan."""

    def __init__(self, number: int) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, other: BeamNumber) -> None:
        """Initialize instance."""
        ...

    @property
    def IsValid(self) -> bool:
        """bool: Returns true if the given BeamNumber is valid. Otherwise false."""
        ...

    @property
    def Number(self) -> int:
        """int: The beam number."""
        ...

    def Equals(self, other: Any) -> bool:
        """Method docstring."""
        ...

    @overload
    def Equals(self, other: BeamNumber) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Provides a hash code for the item, see
        
        Returns:
            int: The hash code for this instance."""
        ...

    def GetSchema(self) -> XmlSchema:
        """This member is internal to the Eclipse Scripting API.
        
        Returns:
            XmlSchema: XmlSchema."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def ReadXml(self, reader: XmlReader) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    def WriteXml(self, writer: XmlWriter) -> None:
        """Method docstring."""
        ...

    NotABeamNumber: BeamNumber

class BeamTechnique:
    """An enumeration of beam techniques."""

    Arc: BeamTechnique
    ConformalArc: BeamTechnique
    Invalid: BeamTechnique
    MLC: BeamTechnique
    MLCArc: BeamTechnique
    MultipleStaticSegmentIMRT: BeamTechnique
    ScanningProton: BeamTechnique
    ScatteringProton: BeamTechnique
    SlidingWindowIMRT: BeamTechnique
    Static: BeamTechnique
    VMAT: BeamTechnique

class BlockType:
    """A type flag that tells whether a block is an aperture block or a shielding block. An aperture block is used to limit the radiated area while a shielding block is made to protect a sensitive organ."""

    APERTURE: BlockType
    SHIELDING: BlockType

class BrachyTreatmentTechniqueType:
    """The enumeration of Brachytherapy treatment techniques."""

    CONTACT: BrachyTreatmentTechniqueType
    INTERSTITIAL: BrachyTreatmentTechniqueType
    INTRACAVITARY: BrachyTreatmentTechniqueType
    INTRALUMENARY: BrachyTreatmentTechniqueType
    INTRAVASCULAR: BrachyTreatmentTechniqueType
    NONE: BrachyTreatmentTechniqueType
    PERMANENT: BrachyTreatmentTechniqueType

class CalculationType:
    """Calculation type."""

    DVHEstimation: CalculationType
    PhotonIMRTOptimization: CalculationType
    PhotonLeafMotions: CalculationType
    PhotonOptimization: CalculationType
    PhotonSRSDose: CalculationType
    PhotonVMATOptimization: CalculationType
    PhotonVolumeDose: CalculationType
    ProtonBeamDeliveryDynamics: CalculationType
    ProtonBeamLineModifiers: CalculationType
    ProtonDDC: CalculationType
    ProtonDVHEstimation: CalculationType
    ProtonMSPostProcessing: CalculationType
    ProtonOptimization: CalculationType
    ProtonVolumeDose: CalculationType

class ChangeBrachyTreatmentUnitResult:
    """Return value for"""

    Failed: ChangeBrachyTreatmentUnitResult
    FailedBecausePlanContainsSeedCollections: ChangeBrachyTreatmentUnitResult
    Success: ChangeBrachyTreatmentUnitResult
    SuccessButPdrDataMissing: ChangeBrachyTreatmentUnitResult

class ClinicalGoal(ValueType):
    """Represents a clinical goal."""

    def __init__(self, measureType: MeasureType, structureId: str, objective: Objective, objAsString: str, priority: GoalPriority, tolerance: float, toleranceAsString: str, actual: float, actualAsString: str, evalResult: GoalEvalResult) -> None:
        """Initialize instance."""
        ...

    @property
    def ActualValue(self) -> float:
        """float: Clinical goal actual value"""
        ...

    @property
    def ActualValueAsString(self) -> str:
        """str: String representation of clinical goal actual value"""
        ...

    @property
    def EvaluationResult(self) -> GoalEvalResult:
        """GoalEvalResult: Evaluation result."""
        ...

    @property
    def MeasureType(self) -> MeasureType:
        """MeasureType: Clinical goal measure type"""
        ...

    @property
    def Objective(self) -> Objective:
        """Objective: Clinical goal objective"""
        ...

    @property
    def ObjectiveAsString(self) -> str:
        """str: String representation of clinical goal objective"""
        ...

    @property
    def Priority(self) -> GoalPriority:
        """GoalPriority: Goal priority (0-4), where 0 is Most Important"""
        ...

    @property
    def StructureId(self) -> str:
        """str: Clinical goal structure Id"""
        ...

    @property
    def VariationAcceptable(self) -> float:
        """float: Clinical goal Variation Acceptable (tolerance)"""
        ...

    @property
    def VariationAcceptableAsString(self) -> str:
        """str: String representation of clinical goal Variation Acceptable (tolerance)"""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """This member is internal to the Eclipse Scripting API.
        
        Returns:
            XmlSchema: XmlSchema."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def ReadXml(self, reader: XmlReader) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    def WriteXml(self, writer: XmlWriter) -> None:
        """Method docstring."""
        ...


class ClosedLeavesMeetingPoint:
    """Specifies where the closed MLC leaf pairs are parked in an MLC leaf fit operation. Bank_One: Varian = B, IEC MLCX = X1, IEC MLCY = Y1; Bank_Two: Varian = A, IEC MLCX = X2, IEC MLCY = Y2"""

    ClosedLeavesMeetingPoint_BankOne: ClosedLeavesMeetingPoint
    ClosedLeavesMeetingPoint_BankTwo: ClosedLeavesMeetingPoint
    ClosedLeavesMeetingPoint_Center: ClosedLeavesMeetingPoint

class Component:
    """VVector component indexing."""

    X: Component
    Y: Component
    Z: Component

class CourseClinicalStatus:
    """Clinical Status of Course"""

    Active: CourseClinicalStatus
    Completed: CourseClinicalStatus
    Null: CourseClinicalStatus
    Restored: CourseClinicalStatus

class DRRCalculationParameters:
    """Parameters for DRR calculation."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, drrSize: float) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, drrSize: float, weight: float, ctFrom: float, ctTo: float) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, drrSize: float, weight: float, ctFrom: float, ctTo: float, geoFrom: float, geoTo: float) -> None:
        """Initialize instance."""
        ...

    @property
    def DRRSize(self) -> float:
        """float: DRR size. Decreasing the size of the DRR effectively increases the resolution of the DRR. Value must be between 5 and 5120 mm."""
        ...

    @DRRSize.setter
    def DRRSize(self, value: float) -> None:
        """Set property value."""
        ...

    @property
    def FieldOutlines(self) -> bool:
        """bool: Defines if field outlines (MLC, CIAO etc.) are added as layers in the DRR."""
        ...

    @FieldOutlines.setter
    def FieldOutlines(self, value: bool) -> None:
        """Set property value."""
        ...

    @property
    def StructureOutlines(self) -> bool:
        """bool: Defines if structure outlines are added as layers in the DRR."""
        ...

    @StructureOutlines.setter
    def StructureOutlines(self, value: bool) -> None:
        """Set property value."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetLayerParameters(self, index: int) -> SingleLayerParameters:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def SetLayerParameters(self, index: int, weight: float, ctFrom: float, ctTo: float) -> None:
        """Method docstring."""
        ...

    @overload
    def SetLayerParameters(self, index: int, weight: float, ctFrom: float, ctTo: float, geoFrom: float, geoTo: float) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...


class DVHEstimateType:
    """Represents the type of a DVH estimate curve"""

    Lower: DVHEstimateType
    Undefined: DVHEstimateType
    Upper: DVHEstimateType

class DVHEstimationStructureType:
    """Structure type as defined in Planning Model Library: PTV or OAR"""

    AVOIDANCE: DVHEstimationStructureType
    Null: DVHEstimationStructureType
    PTV: DVHEstimationStructureType

class DVHPoint(ValueType):
    """Represents a value on a Dose Volume Histogram (DVH) curve."""

    def __init__(self, dose: DoseValue, volume: float, volumeUnit: str) -> None:
        """Initialize instance."""
        ...

    @property
    def DoseValue(self) -> DoseValue:
        """DoseValue: The dose value of the point."""
        ...

    @property
    def Volume(self) -> float:
        """float: The volume value of the point."""
        ...

    @property
    def VolumeUnit(self) -> str:
        """str: The volume unit of the point."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """This member is internal to the Eclipse Scripting API.
        
        Returns:
            XmlSchema: XmlSchema."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def ReadXml(self, reader: XmlReader) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    def WriteXml(self, writer: XmlWriter) -> None:
        """Method docstring."""
        ...


class DefaultDoseValueSettings:
    """Class docstring."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    def Decimals(self, unit: DoseUnit) -> int:
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

    def ToString(self) -> str:
        """Method docstring."""
        ...


class DefaultDoseValueSettings:
    """Class docstring."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    def Decimals(self, unit: DoseUnit) -> int:
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

    def ToString(self) -> str:
        """Method docstring."""
        ...


class DoseProfile(LineProfile):
    """Represents a dose profile."""

    def __init__(self, origin: VVector, step: VVector, data: Array[float], unit: DoseUnit) -> None:
        """Initialize instance."""
        ...

    @property
    def Count(self) -> int:
        """int: Property docstring."""
        ...

    @property
    def Item(self) -> ProfilePoint:
        """ProfilePoint: Property docstring."""
        ...

    @property
    def Unit(self) -> DoseUnit:
        """DoseUnit: The unit of the points on this dose profile."""
        ...

    @Unit.setter
    def Unit(self, value: DoseUnit) -> None:
        """Set property value."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetEnumerator(self) -> IEnumerator[ProfilePoint]:
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


class DoseUnit:
    """The unit of the dose value."""

    Gy: DoseUnit
    Percent: DoseUnit
    Unknown: DoseUnit
    cGy: DoseUnit

class DoseUnit:
    """The unit of the dose value."""

    Gy: DoseUnit
    Percent: DoseUnit
    Unknown: DoseUnit
    cGy: DoseUnit

class DoseValue(ValueType):
    """Represents a dose value. DoseValue semantics follows the semantics of System.Double, with DoseValue.Undefined corresponding to Double.NaN."""

    def __init__(self, value: float, unitName: str) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, value: float, unit: DoseUnit) -> None:
        """Initialize instance."""
        ...

    @property
    def Decimals(self) -> int:
        """int: The display precision of this value"""
        ...

    @property
    def Dose(self) -> float:
        """float: The value of this instance."""
        ...

    @property
    def IsAbsoluteDoseValue(self) -> bool:
        """bool: Returns true if the unit of the dose value is absolute (Gy or cGy)."""
        ...

    @property
    def IsRelativeDoseValue(self) -> bool:
        """bool: Returns true if the unit of the dose value is relative (%)."""
        ...

    @property
    def Unit(self) -> DoseUnit:
        """DoseUnit: The unit of this instance."""
        ...

    @property
    def UnitAsString(self) -> str:
        """str: The unit of this instance as a string."""
        ...

    @property
    def ValueAsString(self) -> str:
        """str: The value of this instance as a string."""
        ...

    def CompareTo(self, other: DoseValue) -> int:
        """Method docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    @overload
    def Equals(self, other: DoseValue) -> bool:
        """Method docstring."""
        ...

    @overload
    def Equals(self, other: DoseValue, epsilon: float) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """A hash code for the current object.
        
        Returns:
            int: A hash code for the current object."""
        ...

    def GetSchema(self) -> XmlSchema:
        """This member is internal to the Eclipse Scripting API.
        
        Returns:
            XmlSchema: XmlSchema."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    @staticmethod
    def IsAbsoluteDoseUnit(doseUnit: DoseUnit) -> bool:
        """Method docstring."""
        ...

    @staticmethod
    def IsRelativeDoseUnit(doseUnit: DoseUnit) -> bool:
        """Method docstring."""
        ...

    def IsUndefined(self) -> bool:
        """Returns true if this dose value is equal to DoseValue.Undefined, false otherwise.
        
        Returns:
            bool: True if this dose value is not defined, false otherwise."""
        ...

    def ReadXml(self, reader: XmlReader) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """A string that represents the current object.
        
        Returns:
            str: A string that represents the current object."""
        ...

    @staticmethod
    def UndefinedDose() -> DoseValue:
        """A dose value, for which the value is Double.NaN and the unit is unknown.
        
        Returns:
            DoseValue: Undefined dose value."""
        ...

    def WriteXml(self, writer: XmlWriter) -> None:
        """Method docstring."""
        ...

    Undefined: DoseValue

class DoseValueDisplayConfig:
    """Configure the settings related to the dose value display for the application. Defaults to the same settings as Eclipse."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @classmethod
    @property
    def DisplaySettings(cls) -> DefaultDoseValueSettings:
        """DefaultDoseValueSettings: Get and set current dosevalue display settings. Set settings controller to null reverts to default display settings."""
        ...

    @classmethod
    @DisplaySettings.setter
    def DisplaySettings(cls, value: DefaultDoseValueSettings) -> None:
        """Set property value."""
        ...

    @staticmethod
    def Decimals(unit: DoseUnit) -> int:
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

    def ToString(self) -> str:
        """Method docstring."""
        ...


class DoseValuePresentation:
    """Types of presentation for dose values."""

    Absolute: DoseValuePresentation
    Relative: DoseValuePresentation

class DosimeterUnit:
    """The dosimeter unit."""

    MU: DosimeterUnit
    Minute: DosimeterUnit
    Null: DosimeterUnit
    Second: DosimeterUnit

class ExternalBeamMachineParameters:
    """The parameters for the external beam treatment unit."""

    def __init__(self, machineId: str, energyModeId: str, doseRate: int, techniqueId: str, primaryFluenceModeId: str) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, machineId: str) -> None:
        """Initialize instance."""
        ...

    @property
    def DoseRate(self) -> int:
        """int: Dose rate value."""
        ...

    @DoseRate.setter
    def DoseRate(self, value: int) -> None:
        """Set property value."""
        ...

    @property
    def EnergyModeId(self) -> str:
        """str: The energy mode identifier. For example, "6X", or "18X"."""
        ...

    @EnergyModeId.setter
    def EnergyModeId(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def MLCId(self) -> str:
        """str: Optional MLC identifier. If null (which is the default) then the single MLC of the treatment unit is selected."""
        ...

    @MLCId.setter
    def MLCId(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def MachineId(self) -> str:
        """str: The treatment unit identifier."""
        ...

    @MachineId.setter
    def MachineId(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def PrimaryFluenceModeId(self) -> str:
        """str: Primary Fluence Mode identifier. Acceptable values are: null, empty string, "SRS","FFF"."""
        ...

    @PrimaryFluenceModeId.setter
    def PrimaryFluenceModeId(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def TechniqueId(self) -> str:
        """str: Technique identifier. Typically "STATIC" or "ARC"."""
        ...

    @TechniqueId.setter
    def TechniqueId(self, value: str) -> None:
        """Set property value."""
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


class FitToStructureMarginType:
    """Margin type"""

    Circular: FitToStructureMarginType
    Elliptical: FitToStructureMarginType

class FitToStructureMargins(ValueType):
    """Margins that are used when fitting a field device to a structure from the BEV perspective"""

    def __init__(self, x1: float, y1: float, x2: float, y2: float) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, margin: float) -> None:
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
        """A string that represents the current object.
        
        Returns:
            str: A string that represents the current object."""
        ...

    Type: FitToStructureMarginType
    X1: float
    X2: float
    Y1: float
    Y2: float

class Fluence:
    """Represents the fluence for a beam. The resolution in the fluence matrix is 2.5 mm in x and y directions. In the fluence matrix, x dimension is the number of columns, and y dimension is the number of rows."""

    def __init__(self, fluenceMatrix: Array[float], xOrigin: float, yOrigin: float) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, fluenceMatrix: Array[float], xOrigin: float, yOrigin: float, mlcId: str) -> None:
        """Initialize instance."""
        ...

    @property
    def MLCId(self) -> str:
        """str: The identifier of the MLC that is related to the fluence. The value can be empty or null."""
        ...

    @MLCId.setter
    def MLCId(self, value: str) -> None:
        """Set property value."""
        ...

    @classmethod
    @property
    def MaxSizePixel(cls) -> int:
        """int: The maximum size of pixels for x or y dimension in the fluence."""
        ...

    @property
    def XOrigin(self) -> float:
        """float: The x coordinate of the first pixel in a fluence map. The value is measured in millimeters from the field isocenter to the center of the first pixel. The coordinate axes are the same as in the IEC BEAM LIMITING DEVICE coordinate system."""
        ...

    @XOrigin.setter
    def XOrigin(self, value: float) -> None:
        """Set property value."""
        ...

    @property
    def XSizeMM(self) -> float:
        """float: The size of x dimension in mm for the fluence. The resolution is 2.5 mm in x and y directions."""
        ...

    @property
    def XSizePixel(self) -> int:
        """int: The size of x dimension in pixels for the fluence. This corresponds to the number of columns in the pixels matrix."""
        ...

    @property
    def YOrigin(self) -> float:
        """float: The y coordinate of the first pixel in a fluence map. The value is measured in millimeters from the field isocenter to the center of the first pixel. The coordinate axes are the same as in the IEC BEAM LIMITING DEVICE coordinate system."""
        ...

    @YOrigin.setter
    def YOrigin(self, value: float) -> None:
        """Set property value."""
        ...

    @property
    def YSizeMM(self) -> float:
        """float: The size of y dimension in mm for the fluence. The resolution is 2.5 mm in x and y directions."""
        ...

    @property
    def YSizePixel(self) -> int:
        """int: The size of y dimension in pixels for the fluence. This corresponds to the number of rows in the pixels matrix."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetPixels(self) -> Array[float]:
        """Returns the fluence matrix.
        
        Returns:
            Array[float]: The pixel values for the fluence as described in"""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...


class GantryDirection:
    """The enumeration of gantry rotation directions."""

    Clockwise: GantryDirection
    CounterClockwise: GantryDirection
    None_: GantryDirection

class GoalEvalResult:
    """Clinical Goal Evaluation Result"""

    Failed: GoalEvalResult
    NA: GoalEvalResult
    Passed: GoalEvalResult
    WithinVariationAcceptable: GoalEvalResult

class GoalPriority:
    """Clinical Goal Priority"""

    Important: GoalPriority
    LessImportant: GoalPriority
    MostImportant: GoalPriority
    ReportValueOnly: GoalPriority
    VeryImportant: GoalPriority

class IDoseValueDisplaySettings:
    """Application specific dose value display settings."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    def Decimals(self, unit: DoseUnit) -> int:
        """Method docstring."""
        ...


class ImageApprovalHistoryEntry(ValueType):
    """An entry in the image approval history."""

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

    ApprovalDateTime: datetime
    ApprovalStatus: ImageApprovalStatus
    StatusComment: str
    UserDisplayName: str
    UserId: str

class ImageApprovalStatus:
    """The enumeration of image approval statuses."""

    ActionRequired: ImageApprovalStatus
    Approved: ImageApprovalStatus
    Disposed: ImageApprovalStatus
    New: ImageApprovalStatus
    Reviewed: ImageApprovalStatus

class ImageProfile(LineProfile):
    """Represents an image line profile."""

    def __init__(self, origin: VVector, step: VVector, data: Array[float], unit: str) -> None:
        """Initialize instance."""
        ...

    @property
    def Count(self) -> int:
        """int: Property docstring."""
        ...

    @property
    def Item(self) -> ProfilePoint:
        """ProfilePoint: Property docstring."""
        ...

    @property
    def Unit(self) -> str:
        """str: The unit of the points on the image profile."""
        ...

    @Unit.setter
    def Unit(self, value: str) -> None:
        """Set property value."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetEnumerator(self) -> IEnumerator[ProfilePoint]:
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


class ImagingBeamSetupParameters:
    """Setup parameters for imaging fields."""

    def __init__(self, imagingSetup: ImagingSetup, fitMarginX1_mm: float, fitMarginX2_mm: float, fitMarginY1_mm: float, fitMarginY2_mm: float, fieldSizeX_mm: float, fieldSizeY_mm: float) -> None:
        """Initialize instance."""
        ...

    @property
    def FieldSizeX(self) -> float:
        """float: Field size in x-direction in mm."""
        ...

    @FieldSizeX.setter
    def FieldSizeX(self, value: float) -> None:
        """Set property value."""
        ...

    @property
    def FieldSizeY(self) -> float:
        """float: Field size in y-direction in mm."""
        ...

    @FieldSizeY.setter
    def FieldSizeY(self, value: float) -> None:
        """Set property value."""
        ...

    @property
    def FitMarginX1(self) -> float:
        """float: Fit margin in x-direction in mm."""
        ...

    @FitMarginX1.setter
    def FitMarginX1(self, value: float) -> None:
        """Set property value."""
        ...

    @property
    def FitMarginX2(self) -> float:
        """float: Fit margin in x-direction in mm."""
        ...

    @FitMarginX2.setter
    def FitMarginX2(self, value: float) -> None:
        """Set property value."""
        ...

    @property
    def FitMarginY1(self) -> float:
        """float: Fit margin in y-direction in mm."""
        ...

    @FitMarginY1.setter
    def FitMarginY1(self, value: float) -> None:
        """Set property value."""
        ...

    @property
    def FitMarginY2(self) -> float:
        """float: Fit margin in y-direction in mm."""
        ...

    @FitMarginY2.setter
    def FitMarginY2(self, value: float) -> None:
        """Set property value."""
        ...

    @property
    def ImagingSetup(self) -> ImagingSetup:
        """ImagingSetup: Identifier for the imaging setup."""
        ...

    @ImagingSetup.setter
    def ImagingSetup(self, value: ImagingSetup) -> None:
        """Set property value."""
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


class ImagingSetup:
    """Set of available imaging setups."""

    MVCBCT_High_Quality: ImagingSetup
    MVCBCT_Low_Dose: ImagingSetup
    MV_MV_High_Quality: ImagingSetup
    MV_MV_Low_Dose: ImagingSetup
    kVCBCT: ImagingSetup

class IonBeamScanMode:
    """The method of beam scanning to be used during treatment. Used with IonBeams."""

    Line: IonBeamScanMode
    Modulated: IonBeamScanMode
    None_: IonBeamScanMode
    Uniform: IonBeamScanMode
    Unknown: IonBeamScanMode
    Wobbling: IonBeamScanMode

class IonPlanNormalizationParameters:
    """The parameters for proton plan normalization."""

    def __init__(self, normalizationMode: PlanNormalizationMode, normalizationValue: float, volumePercentage: float) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, normalizationMode: PlanNormalizationMode, normalizationValue: float) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, normalizationMode: PlanNormalizationMode) -> None:
        """Initialize instance."""
        ...

    @property
    def NormalizationMode(self) -> PlanNormalizationMode:
        """PlanNormalizationMode: Normalization mode."""
        ...

    @property
    def NormalizationValue(self) -> float:
        """float: The treatment unit identifier."""
        ...

    @property
    def VolumePercentage(self) -> float:
        """float: Volume percentage factor."""
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


class IonPlanOptimizationMode:
    """Proton plan optimization mode."""

    MultiFieldOptimization: IonPlanOptimizationMode
    SingleFieldOptimization: IonPlanOptimizationMode

class JawFitting:
    """Specifies where collimator jaws are positioned in an MLC leaf fit operation."""

    FitToRecommended: JawFitting
    FitToStructure: JawFitting
    None_: JawFitting

class LMCMSSOptions:
    """Options for calculating leaf motions using the non-Varian MSS Leaf Motion Calculator (LMCMSS) algorithm."""

    def __init__(self, numberOfIterations: int) -> None:
        """Initialize instance."""
        ...

    @property
    def NumberOfIterations(self) -> int:
        """int: The number of calculation iterations."""
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


class LMCVOptions:
    """Options for calculating leaf motions using the Varian Leaf Motion Calculator (LMCV) algorithm."""

    def __init__(self, fixedJaws: bool) -> None:
        """Initialize instance."""
        ...

    @property
    def FixedJaws(self) -> bool:
        """bool: Use the Fixed jaws option."""
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


class LateralSpreadingDeviceType:
    """Type of the lateral spreading device."""

    Magnet: LateralSpreadingDeviceType
    Scatterer: LateralSpreadingDeviceType

class LineProfile:
    """Represents values along a line segment."""

    def __init__(self, origin: VVector, step: VVector, data: Array[float]) -> None:
        """Initialize instance."""
        ...

    @property
    def Count(self) -> int:
        """int: The number of points in the profile."""
        ...

    @property
    def Item(self) -> ProfilePoint:
        """ProfilePoint: Property docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetEnumerator(self) -> IEnumerator[ProfilePoint]:
        """An enumerator for the points in the profile.
        
        Returns:
            IEnumerator[ProfilePoint]: Enumerator for points in the profile."""
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


class LogSeverity:
    """The enumeration of log severities."""

    Alert: LogSeverity
    Debug: LogSeverity
    Emergency: LogSeverity
    Error: LogSeverity
    Info: LogSeverity
    Warning: LogSeverity

class MLCPlanType:
    """The enumeration of Multileaf Collimator (MLC) techniques."""

    ArcDynamic: MLCPlanType
    DoseDynamic: MLCPlanType
    NotDefined: MLCPlanType
    ProtonLayerStacking: MLCPlanType
    Static: MLCPlanType
    VMAT: MLCPlanType

class MeasureModifier:
    """Measure modifier"""

    MeasureModifierAtLeast: MeasureModifier
    MeasureModifierAtMost: MeasureModifier
    MeasureModifierNone: MeasureModifier
    MeasureModifierTarget: MeasureModifier

class MeasureType:
    """Enumeration of plan measure types."""

    MeasureTypeDQP_DXXX: MeasureType
    MeasureTypeDQP_DXXXcc: MeasureType
    MeasureTypeDQP_VXXX: MeasureType
    MeasureTypeDQP_VXXXGy: MeasureType
    MeasureTypeDoseConformity: MeasureType
    MeasureTypeDoseMax: MeasureType
    MeasureTypeDoseMean: MeasureType
    MeasureTypeDoseMin: MeasureType
    MeasureTypeGradient: MeasureType
    MeasureTypeNone: MeasureType

class MetersetValue(ValueType):
    """Represents a meterset value."""

    def __init__(self, value: float, unit: DosimeterUnit) -> None:
        """Initialize instance."""
        ...

    @property
    def Unit(self) -> DosimeterUnit:
        """DosimeterUnit: The unit of this instance."""
        ...

    @Unit.setter
    def Unit(self, value: DosimeterUnit) -> None:
        """Set property value."""
        ...

    @property
    def Value(self) -> float:
        """float: The value of this instance."""
        ...

    @Value.setter
    def Value(self, value: float) -> None:
        """Set property value."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """This member is internal to the Eclipse Scripting API.
        
        Returns:
            XmlSchema: XmlSchema."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def ReadXml(self, reader: XmlReader) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    def WriteXml(self, writer: XmlWriter) -> None:
        """Method docstring."""
        ...


class Objective(ValueType):
    """Represents a clinical goal objective."""

    def __init__(self, type: ObjectiveGoalType, value: float, valueUnit: ObjectiveUnit, oper: ObjectiveOperator, limit: float, limitUnit: ObjectiveUnit) -> None:
        """Initialize instance."""
        ...

    @property
    def Limit(self) -> float:
        """float: Objective limit"""
        ...

    @property
    def LimitUnit(self) -> ObjectiveUnit:
        """ObjectiveUnit: Objective limit unit"""
        ...

    @property
    def Operator(self) -> ObjectiveOperator:
        """ObjectiveOperator: Objective operator"""
        ...

    @property
    def Type(self) -> ObjectiveGoalType:
        """ObjectiveGoalType: Objective type"""
        ...

    @property
    def Value(self) -> float:
        """float: Objective value"""
        ...

    @property
    def ValueUnit(self) -> ObjectiveUnit:
        """ObjectiveUnit: Objective value"""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """This member is internal to the Eclipse Scripting API.
        
        Returns:
            XmlSchema: XmlSchema."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def ReadXml(self, reader: XmlReader) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    def WriteXml(self, writer: XmlWriter) -> None:
        """Method docstring."""
        ...


class ObjectiveGoalType:
    """Clinical goal Objective type"""

    ConformityIndex: ObjectiveGoalType
    Dose: ObjectiveGoalType
    GradientMeasure: ObjectiveGoalType
    Invalid: ObjectiveGoalType
    Maximum_Dose: ObjectiveGoalType
    Mean_Dose: ObjectiveGoalType
    Minimum_Dose: ObjectiveGoalType
    Prescription: ObjectiveGoalType
    Volume: ObjectiveGoalType

class ObjectiveOperator:
    """Clinical goal Objective operator"""

    Equals: ObjectiveOperator
    GreaterThan: ObjectiveOperator
    GreaterThanOrEqual: ObjectiveOperator
    LessThan: ObjectiveOperator
    LessThanOrEqual: ObjectiveOperator
    None_: ObjectiveOperator

class ObjectiveUnit:
    """Clinical goal Objective Unit"""

    Absolute: ObjectiveUnit
    None_: ObjectiveUnit
    Relative: ObjectiveUnit

class OpenLeavesMeetingPoint:
    """Specifies where the open MLC leaves meet the structure outline in an MLC leaf fit operation."""

    OpenLeavesMeetingPoint_Inside: OpenLeavesMeetingPoint
    OpenLeavesMeetingPoint_Middle: OpenLeavesMeetingPoint
    OpenLeavesMeetingPoint_Outside: OpenLeavesMeetingPoint

class OptimizationAvoidanceSector(ValueType):
    """Avoidance sector details."""

    def __init__(self, startAngle: float, stopAngle: float) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, startAngle: float, stopAngle: float, isValid: bool, validationError: str) -> None:
        """Initialize instance."""
        ...

    @property
    def IsDefined(self) -> bool:
        """bool: Is Avoidance Sector defined. True if either startAngle or stopAngle is defined."""
        ...

    @property
    def StartAngle(self) -> float:
        """float: Start angle."""
        ...

    @property
    def StopAngle(self) -> float:
        """float: Stop angle."""
        ...

    @property
    def Valid(self) -> bool:
        """bool: Is Avoidance Sector valid."""
        ...

    @property
    def ValidationError(self) -> str:
        """str: Validation error."""
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


class OptimizationConvergenceOption:
    """Options for terminating optimization upon convergence."""

    NoEarlyTermination: OptimizationConvergenceOption
    TerminateIfConverged: OptimizationConvergenceOption

class OptimizationIntermediateDoseOption:
    """Options for using intermediate dose in optimization."""

    NoIntermediateDose: OptimizationIntermediateDoseOption
    UseIntermediateDose: OptimizationIntermediateDoseOption

class OptimizationObjectiveOperator:
    """Optimization Objective Operator, which is used for setting the upper and lower optimization objectives."""

    Exact: OptimizationObjectiveOperator
    Lower: OptimizationObjectiveOperator
    None_: OptimizationObjectiveOperator
    Upper: OptimizationObjectiveOperator

class OptimizationOption:
    """Options for Optimization."""

    ContinueOptimization: OptimizationOption
    ContinueOptimizationWithPlanDoseAsIntermediateDose: OptimizationOption
    RestartOptimization: OptimizationOption

class OptimizationOptionsBase:
    """Abstract base class for IMRT and VMAT optimization options."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def IntermediateDoseOption(self) -> OptimizationIntermediateDoseOption:
        """OptimizationIntermediateDoseOption: Use of intermediate dose in optimization."""
        ...

    @property
    def MLC(self) -> str:
        """str: Identifier for the Multileaf Collimator (MLC). This can be left empty if there is exactly one MLC configured."""
        ...

    @property
    def StartOption(self) -> OptimizationOption:
        """OptimizationOption: The state at the beginning of the optimization."""
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


class OptimizationOptionsIMPT(OptimizationOptionsBase):
    """Options for IMPT optimization."""

    def __init__(self, maxIterations: int, initialState: OptimizationOption) -> None:
        """Initialize instance."""
        ...

    @property
    def IntermediateDoseOption(self) -> OptimizationIntermediateDoseOption:
        """OptimizationIntermediateDoseOption: Property docstring."""
        ...

    @property
    def MLC(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def MaximumNumberOfIterations(self) -> int:
        """int: Maximum number of iterations for the IMPT optimizer."""
        ...

    @property
    def StartOption(self) -> OptimizationOption:
        """OptimizationOption: Property docstring."""
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


class OptimizationOptionsIMRT(OptimizationOptionsBase):
    """Options for IMRT optimization."""

    def __init__(self, maxIterations: int, initialState: OptimizationOption, numberOfStepsBeforeIntermediateDose: int, convergenceOption: OptimizationConvergenceOption, mlcId: str) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, maxIterations: int, initialState: OptimizationOption, convergenceOption: OptimizationConvergenceOption, intermediateDoseOption: OptimizationIntermediateDoseOption, mlcId: str) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, maxIterations: int, initialState: OptimizationOption, convergenceOption: OptimizationConvergenceOption, mlcId: str) -> None:
        """Initialize instance."""
        ...

    @property
    def ConvergenceOption(self) -> OptimizationConvergenceOption:
        """OptimizationConvergenceOption: Terminate the optimization early if it is converged."""
        ...

    @property
    def IntermediateDoseOption(self) -> OptimizationIntermediateDoseOption:
        """OptimizationIntermediateDoseOption: Property docstring."""
        ...

    @property
    def MLC(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def MaximumNumberOfIterations(self) -> int:
        """int: Maximum number of iterations for the IMRT optimizer."""
        ...

    @property
    def NumberOfStepsBeforeIntermediateDose(self) -> int:
        """int: Number of steps before the intermediate dose is calculated."""
        ...

    @property
    def StartOption(self) -> OptimizationOption:
        """OptimizationOption: Property docstring."""
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


class OptimizationOptionsVMAT(OptimizationOptionsBase):
    """Options for VMAT optimization."""

    def __init__(self, startOption: OptimizationOption, mlcId: str) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, intermediateDoseOption: OptimizationIntermediateDoseOption, mlcId: str) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, numberOfCycles: int, mlcId: str) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, options: OptimizationOptionsVMAT) -> None:
        """Initialize instance."""
        ...

    @property
    def IntermediateDoseOption(self) -> OptimizationIntermediateDoseOption:
        """OptimizationIntermediateDoseOption: Property docstring."""
        ...

    @property
    def MLC(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def NumberOfOptimizationCycles(self) -> int:
        """int: Number of VMAT optimization cycles."""
        ...

    @property
    def StartOption(self) -> OptimizationOption:
        """OptimizationOption: Property docstring."""
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


class ParticleType:
    """Particle types"""

    Photon: ParticleType
    Proton: ParticleType

class PatientOrientation:
    """The enumeration of patient orientations."""

    FeetFirstDecubitusLeft: PatientOrientation
    FeetFirstDecubitusRight: PatientOrientation
    FeetFirstProne: PatientOrientation
    FeetFirstSupine: PatientOrientation
    HeadFirstDecubitusLeft: PatientOrientation
    HeadFirstDecubitusRight: PatientOrientation
    HeadFirstProne: PatientOrientation
    HeadFirstSupine: PatientOrientation
    NoOrientation: PatientOrientation
    Sitting: PatientOrientation

class PatientSupportType:
    """Patient support type."""

    Chair: PatientSupportType
    Table: PatientSupportType

class PlanNormalizationMode:
    """Plan normalization options for SetPlanNormalization"""

    NoNormalization: PlanNormalizationMode
    TargetDVH: PlanNormalizationMode
    TargetMax: PlanNormalizationMode
    TargetMean: PlanNormalizationMode
    TargetMin: PlanNormalizationMode
    UserDefined: PlanNormalizationMode

class PlanSetupApprovalStatus:
    """The enumeration of plan approval statuses."""

    Completed: PlanSetupApprovalStatus
    CompletedEarly: PlanSetupApprovalStatus
    ExternallyApproved: PlanSetupApprovalStatus
    PlanningApproved: PlanSetupApprovalStatus
    Rejected: PlanSetupApprovalStatus
    Retired: PlanSetupApprovalStatus
    Reviewed: PlanSetupApprovalStatus
    TreatmentApproved: PlanSetupApprovalStatus
    UnApproved: PlanSetupApprovalStatus
    UnPlannedTreatment: PlanSetupApprovalStatus
    Unknown: PlanSetupApprovalStatus

class PlanSumOperation:
    """PlanSum operation for PlanSetups in PlanSum. Indicates whether the plan is summed with (“+”) or subtracted from (“-”) the other plans in the sum."""

    Addition: PlanSumOperation
    Subtraction: PlanSumOperation
    Undefined: PlanSumOperation

class PlanType:
    """The enumeration of plan types."""

    Brachy: PlanType
    ExternalBeam: PlanType
    ExternalBeam_IRREG: PlanType
    ExternalBeam_Proton: PlanType

class PlanUncertaintyType:
    """Plan uncertainty type indicates the usage of associated uncertainty parameters, see"""

    BaselineShiftUncertainty: PlanUncertaintyType
    IsocenterShiftUncertainty: PlanUncertaintyType
    RangeUncertainty: PlanUncertaintyType
    RobustOptimizationUncertainty: PlanUncertaintyType
    UncertaintyTypeNotDefined: PlanUncertaintyType

class PlanValidationResult:
    """Represents plan validatation result"""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, details: List[PlanValidationResultDetail]) -> None:
        """Initialize instance."""
        ...

    @property
    def Details(self) -> List[PlanValidationResultDetail]:
        """List[PlanValidationResultDetail]: The validation details of this instance."""
        ...

    @Details.setter
    def Details(self, value: List[PlanValidationResultDetail]) -> None:
        """Set property value."""
        ...

    @property
    def ErrorCount(self) -> int:
        """int: The error count of this instance."""
        ...

    @ErrorCount.setter
    def ErrorCount(self, value: int) -> None:
        """Set property value."""
        ...

    @property
    def InfoCount(self) -> int:
        """int: The info count of this instance."""
        ...

    @InfoCount.setter
    def InfoCount(self, value: int) -> None:
        """Set property value."""
        ...

    @property
    def StringPresentation(self) -> str:
        """str: String representation of this instance."""
        ...

    @property
    def WarningCount(self) -> int:
        """int: The warning count of this instance."""
        ...

    @WarningCount.setter
    def WarningCount(self, value: int) -> None:
        """Set property value."""
        ...

    def Add(self, detail: PlanValidationResultDetail) -> None:
        """Method docstring."""
        ...

    @overload
    def Add(self, componentResult: PlanValidationResult) -> None:
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

    def ToString(self) -> str:
        """Method docstring."""
        ...


class PlanValidationResultDetail:
    """Represents plan validation detail."""

    def __init__(self, plan: str, messageForUser: str, classification: ResultClassification, code: str) -> None:
        """Initialize instance."""
        ...

    @property
    def Classification(self) -> ResultClassification:
        """ResultClassification: Result classification of this instance."""
        ...

    @Classification.setter
    def Classification(self, value: ResultClassification) -> None:
        """Set property value."""
        ...

    @property
    def Code(self) -> str:
        """str: Unique validation detail code of this instance."""
        ...

    @Code.setter
    def Code(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def MessageForUser(self) -> str:
        """str: Localized message for user of this instance."""
        ...

    @MessageForUser.setter
    def MessageForUser(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def Plan(self) -> str:
        """str: Identifies the plan of this instance."""
        ...

    @Plan.setter
    def Plan(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def StringPresentation(self) -> str:
        """str: String representation of this instance."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    @staticmethod
    def GetClassification(detail: PlanValidationResultDetail) -> ResultClassification:
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


class PlanValidationResultEsapiDetail:
    """A class for detailed plan validation result"""

    def __init__(self, messageForUser: str, isError: bool, code: str) -> None:
        """Initialize instance."""
        ...

    @property
    def Code(self) -> str:
        """str: Detail code."""
        ...

    @Code.setter
    def Code(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def IsError(self) -> bool:
        """bool: Check if the result is a error (true) or a warning (false)."""
        ...

    @IsError.setter
    def IsError(self, value: bool) -> None:
        """Set property value."""
        ...

    @property
    def MessageForUser(self) -> str:
        """str: Message for the user about the validation result detail."""
        ...

    @MessageForUser.setter
    def MessageForUser(self, value: str) -> None:
        """Set property value."""
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


class PrescriptionModifier:
    """Prescription modifier."""

    PrescriptionModifierAtLeast: PrescriptionModifier
    PrescriptionModifierAtMost: PrescriptionModifier
    PrescriptionModifierDMax: PrescriptionModifier
    PrescriptionModifierEUD: PrescriptionModifier
    PrescriptionModifierIsodose: PrescriptionModifier
    PrescriptionModifierMaxDose: PrescriptionModifier
    PrescriptionModifierMaxDoseAtMost: PrescriptionModifier
    PrescriptionModifierMeanDose: PrescriptionModifier
    PrescriptionModifierMeanDoseAtLeast: PrescriptionModifier
    PrescriptionModifierMeanDoseAtMost: PrescriptionModifier
    PrescriptionModifierMidPoint: PrescriptionModifier
    PrescriptionModifierMinDose: PrescriptionModifier
    PrescriptionModifierMinDoseAtLeast: PrescriptionModifier
    PrescriptionModifierNone: PrescriptionModifier
    PrescriptionModifierRefPoint: PrescriptionModifier
    PrescriptionModifierUser: PrescriptionModifier

class PrescriptionType:
    """Enumeration of prescription types."""

    PrescriptionTypeDepth: PrescriptionType
    PrescriptionTypeIsodose: PrescriptionType
    PrescriptionTypeNone: PrescriptionType
    PrescriptionTypeVolume: PrescriptionType

class ProfilePoint(ValueType):
    """Represents a point of a line profile."""

    def __init__(self, position: VVector, value: float) -> None:
        """Initialize instance."""
        ...

    @property
    def Position(self) -> VVector:
        """VVector: The position of the point."""
        ...

    @Position.setter
    def Position(self, value: VVector) -> None:
        """Set property value."""
        ...

    @property
    def Value(self) -> float:
        """float: The value of the point."""
        ...

    @Value.setter
    def Value(self, value: float) -> None:
        """Set property value."""
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


class ProtonBeamLineStatus:
    """Status of proton beam line"""

    Invalid: ProtonBeamLineStatus
    Outdated: ProtonBeamLineStatus
    Valid: ProtonBeamLineStatus

class ProtonBeamMachineParameters:
    """The parameters for the proton beam treatment unit."""

    def __init__(self, machineId: str, techniqueId: str, toleranceId: str) -> None:
        """Initialize instance."""
        ...

    @property
    def MachineId(self) -> str:
        """str: The treatment unit identifier."""
        ...

    @MachineId.setter
    def MachineId(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def TechniqueId(self) -> str:
        """str: Technique identifier. For example, "MODULAT_SCANNING", or "UNIFORM_SCANNING"."""
        ...

    @TechniqueId.setter
    def TechniqueId(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def ToleranceId(self) -> str:
        """str: Tolerance identifier."""
        ...

    @ToleranceId.setter
    def ToleranceId(self, value: str) -> None:
        """Set property value."""
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


class ProtonDeliveryTimeStatus:
    """The enumeration of proton delivery time statuses."""

    Deliverable: ProtonDeliveryTimeStatus
    NotCalculated: ProtonDeliveryTimeStatus
    Undeliverable: ProtonDeliveryTimeStatus

class RTPrescriptionConstraintType:
    """Type of the RT prescription constraint."""

    FreeText: RTPrescriptionConstraintType
    MaximumDose: RTPrescriptionConstraintType
    MaximumDvhDose: RTPrescriptionConstraintType
    MaximumMeanDose: RTPrescriptionConstraintType
    MinimumDose: RTPrescriptionConstraintType
    MinimumDvhDose: RTPrescriptionConstraintType

class RTPrescriptionTargetType:
    """The type of the prescription target definition"""

    Depth: RTPrescriptionTargetType
    Isocenter: RTPrescriptionTargetType
    IsodoseLine: RTPrescriptionTargetType
    Undefined: RTPrescriptionTargetType
    Volume: RTPrescriptionTargetType

class RailPosition:
    """Setting for the moveable rail position (in or out) used for couch modeling in Eclipse."""

    In: RailPosition
    Out: RailPosition

class RangeModulatorType:
    """Type of the range modulator."""

    Fixed: RangeModulatorType
    Whl_FixedWeights: RangeModulatorType
    Whl_ModWeights: RangeModulatorType

class RangeShifterType:
    """Type of the range shifter."""

    Analog: RangeShifterType
    Binary: RangeShifterType

class RegistrationApprovalStatus:
    """The enumeration of registration approval statuses."""

    Approved: RegistrationApprovalStatus
    Retired: RegistrationApprovalStatus
    Reviewed: RegistrationApprovalStatus
    Unapproved: RegistrationApprovalStatus

class RendererStrings:
    """Class docstring."""

    Applicators: RendererStrings
    BrachyFractions: RendererStrings
    Catheters: RendererStrings
    CumulativeDVH: RendererStrings
    DoseZRes: RendererStrings
    FinalSpotList: RendererStrings
    Isodoses: RendererStrings
    LengthUnit: RendererStrings
    NormalizationInvalid: RendererStrings
    OrientationLabelAnterior: RendererStrings
    OrientationLabelFeet: RendererStrings
    OrientationLabelHead: RendererStrings
    OrientationLabelLeft: RendererStrings
    OrientationLabelPosterior: RendererStrings
    OrientationLabelRight: RendererStrings
    PlanInTreatment: RendererStrings
    Seeds: RendererStrings
    WarningAddOns: RendererStrings
    WarningArc: RendererStrings
    WarningCAXOnly: RendererStrings
    WarningConcurrency: RendererStrings
    WarningPlanWeights: RendererStrings

class ResetSourcePositionsResult:
    """Return value for"""

    NoSideEffects: ResetSourcePositionsResult
    TotalDwellTimeChanged: ResetSourcePositionsResult

class ResultClassification:
    """Classification of plan validation detail."""

    ValidationError: ResultClassification
    ValidationInfo: ResultClassification
    ValidationWarning: ResultClassification

class ResultClassification:
    """Classification of plan validation detail."""

    ValidationError: ResultClassification
    ValidationInfo: ResultClassification
    ValidationWarning: ResultClassification

class SegmentProfile:
    """Represents the segment values along a line segment."""

    def __init__(self, origin: VVector, step: VVector, data: BitArray) -> None:
        """Initialize instance."""
        ...

    @property
    def Count(self) -> int:
        """int: The number of points in the profile."""
        ...

    @property
    def EdgeCoordinates(self) -> List[VVector]:
        """List[VVector]: Returns the coordinates of the edges of the segment along the segment profile."""
        ...

    @property
    def Item(self) -> SegmentProfilePoint:
        """SegmentProfilePoint: Property docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetEnumerator(self) -> IEnumerator[SegmentProfilePoint]:
        """An enumerator for points in the profile.
        
        Returns:
            IEnumerator[SegmentProfilePoint]: Enumerator for points in the profile."""
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


class SegmentProfilePoint(ValueType):
    """Represents a point of a segment profile."""

    def __init__(self, position: VVector, value: bool) -> None:
        """Initialize instance."""
        ...

    @property
    def Position(self) -> VVector:
        """VVector: The position of the point."""
        ...

    @Position.setter
    def Position(self, value: VVector) -> None:
        """Set property value."""
        ...

    @property
    def Value(self) -> bool:
        """bool: The value of the point: true if the point is inside the segment, false otherwise."""
        ...

    @Value.setter
    def Value(self, value: bool) -> None:
        """Set property value."""
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


class SeriesModality:
    """The enumeration of series modalities."""

    CT: SeriesModality
    MR: SeriesModality
    Other: SeriesModality
    PT: SeriesModality
    REG: SeriesModality
    RTDOSE: SeriesModality
    RTIMAGE: SeriesModality
    RTPLAN: SeriesModality
    RTSTRUCT: SeriesModality

class SetSourcePositionsResult(ValueType):
    """Return value for"""

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

    InputRoundedToMachineResolution: bool
    SourcePositionsUpdated: bool
    TotalDwellTimeChanged: bool

class SetupTechnique:
    """The enumeration of setup techniques for a beam."""

    BreastBridge: SetupTechnique
    FixedSSD: SetupTechnique
    HyperArc: SetupTechnique
    Isocentric: SetupTechnique
    SkinApposition: SetupTechnique
    TBI: SetupTechnique
    Unknown: SetupTechnique

class SingleLayerParameters:
    """One layer or group of DRR calculation parameters."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def CTFrom(self) -> float:
        """float: Lower end of the CT window. Value must be between -1024.0 and 6000.0."""
        ...

    @CTFrom.setter
    def CTFrom(self, value: float) -> None:
        """Set property value."""
        ...

    @property
    def CTTo(self) -> float:
        """float: Upper end of the CT window. Value must be between -1024.0 and 6000.0."""
        ...

    @CTTo.setter
    def CTTo(self, value: float) -> None:
        """Set property value."""
        ...

    @property
    def GeoClipping(self) -> bool:
        """bool: Image volume type on which the DRR calculation is based. If calculation is based on partial image volume as specified by"""
        ...

    @GeoClipping.setter
    def GeoClipping(self, value: bool) -> None:
        """Set property value."""
        ...

    @property
    def GeoFrom(self) -> float:
        """float: Starting distance from the isocenter. Value must be between -10000 and 10000 mm."""
        ...

    @GeoFrom.setter
    def GeoFrom(self, value: float) -> None:
        """Set property value."""
        ...

    @property
    def GeoTo(self) -> float:
        """float: Ending distance from the isocenter. Value must be between -10000 and 10000 mm."""
        ...

    @GeoTo.setter
    def GeoTo(self, value: float) -> None:
        """Set property value."""
        ...

    @property
    def LayerOn(self) -> bool:
        """bool: Defines whether the layer of parameters are selected."""
        ...

    @LayerOn.setter
    def LayerOn(self, value: bool) -> None:
        """Set property value."""
        ...

    @property
    def Weight(self) -> float:
        """float: Weight factor of the DRR layer. Value must be between -100.0 and 100.0."""
        ...

    @Weight.setter
    def Weight(self, value: float) -> None:
        """Set property value."""
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


class SmartLMCOptions:
    """Options for calculating leaf motions using the Varian Smart LMC algorithm."""

    def __init__(self, fixedFieldBorders: bool, jawTracking: bool) -> None:
        """Initialize instance."""
        ...

    @property
    def FixedFieldBorders(self) -> bool:
        """bool: Use the Fixed field borders option. See details in Eclipse Photon and Electron Algorithms Reference Guide."""
        ...

    @property
    def JawTracking(self) -> bool:
        """bool: Use the Jaw tracking option. See details in Eclipse Photon and Electron Algorithms Reference Guide."""
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


class StructureApprovalHistoryEntry(ValueType):
    """An entry in the structure approval history."""

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

    ApprovalDateTime: datetime
    ApprovalStatus: StructureApprovalStatus
    StatusComment: str
    UserDisplayName: str
    UserId: str

class StructureApprovalStatus:
    """The enumeration of structure approval statuses."""

    Approved: StructureApprovalStatus
    Rejected: StructureApprovalStatus
    Reviewed: StructureApprovalStatus
    UnApproved: StructureApprovalStatus

class StructureCodeInfo(ValueType):
    """Represents structure code information."""

    def __init__(self, codingScheme: str, code: str) -> None:
        """Initialize instance."""
        ...

    @property
    def Code(self) -> str:
        """str: The structure code as defined in the associated coding scheme."""
        ...

    @property
    def CodingScheme(self) -> str:
        """str: The coding scheme of the structure code."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    @overload
    def Equals(self, other: StructureCodeInfo) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Returns the hash code for this instance. Overrides Object.GetHashCode.
        
        Returns:
            int: The hash code for this instance."""
        ...

    def GetSchema(self) -> XmlSchema:
        """This member is internal to the Eclipse Scripting API.
        
        Returns:
            XmlSchema: XmlSchema."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def ReadXml(self, reader: XmlReader) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """A string that represents the current object.
        
        Returns:
            str: A string that represents the current object."""
        ...

    def WriteXml(self, writer: XmlWriter) -> None:
        """Method docstring."""
        ...


class StructureMarginGeometry:
    """Specifies whether a margin operation expands (outer margin) or shrinks (inner margin) the volume."""

    Inner: StructureMarginGeometry
    Outer: StructureMarginGeometry

class TreatmentSessionStatus:
    """Status of the treatment session."""

    Completed: TreatmentSessionStatus
    CompletedPartially: TreatmentSessionStatus
    InActiveResume: TreatmentSessionStatus
    InActiveTreat: TreatmentSessionStatus
    Null: TreatmentSessionStatus
    Resume: TreatmentSessionStatus
    Treat: TreatmentSessionStatus

class UserIdentity(ValueType):
    """Represents the identity of an user, including the identifier (username) and the display name."""

    def __init__(self, id: str, displayName: str) -> None:
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

    DisplayName: str
    Id: str

class VRect(Generic[T], ValueType):
    """Represents a rectangle.
    
    Currently limited to value types."""

    def __init__(self, x1: T, y1: T, x2: T, y2: T) -> None:
        """Initialize instance."""
        ...

    @property
    def X1(self) -> T:
        """T: The X1-coordinate of the rectangle."""
        ...

    @property
    def X2(self) -> T:
        """T: The X2-coordinate of the rectangle."""
        ...

    @property
    def Y1(self) -> T:
        """T: The Y1-coordinate of the rectangle."""
        ...

    @property
    def Y2(self) -> T:
        """T: The Y2-coordinate of the rectangle."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    @overload
    def Equals(self, other: VRect[T]) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Returns the hash code for this instance. Overrides Object.GetHashCode.
        
        Returns:
            int: The hash code for this instance."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """A string that represents the current object.
        
        Returns:
            str: A string that represents the current object."""
        ...


class VVector(ValueType):
    """Represents a displacement in 3D space."""

    def __init__(self, xi: float, yi: float, zi: float) -> None:
        """Initialize instance."""
        ...

    @property
    def Item(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def Length(self) -> float:
        """float: The length of the VVector."""
        ...

    @property
    def LengthSquared(self) -> float:
        """float: The square of the length of the VVector."""
        ...

    @property
    def x(self) -> float:
        """float: The X component of the VVector."""
        ...

    @x.setter
    def x(self, value: float) -> None:
        """Set property value."""
        ...

    @property
    def y(self) -> float:
        """float: The Y component of the VVector."""
        ...

    @y.setter
    def y(self, value: float) -> None:
        """Set property value."""
        ...

    @property
    def z(self) -> float:
        """float: The Z component of the VVector."""
        ...

    @z.setter
    def z(self, value: float) -> None:
        """Set property value."""
        ...

    @staticmethod
    def Distance(left: VVector, right: VVector) -> float:
        """Method docstring."""
        ...

    def EpsilonEqual(self, other: VVector, epsilon: float) -> bool:
        """Method docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    @overload
    def Equals(self, other: VVector) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """A hash code for the current object.
        
        Returns:
            int: A hash code for the current object."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def GetUnitLengthScaledVector(self) -> VVector:
        """Scales this VVector so that its length becomes equal to unity."""
        ...

    def IsUndefined(self) -> bool:
        """Returns true if at least one of this vector components are equal to double.IsNaN or double.IsInfinity, false otherwise.
        
        Returns:
            bool: True if at least one of the vector component is not defined or is infinity, false otherwise."""
        ...

    def ScalarProduct(self, left: VVector) -> float:
        """Method docstring."""
        ...

    def ScaleToUnitLength(self) -> None:
        """Scales this VVector so that its length becomes equal to unity."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    def Update(self, vc: Component, value: float) -> VVector:
        """Method docstring."""
        ...

    DefaultEpsilon: float
    Undefined: VVector

class ValidationException(ApplicationException):
    """ValidationException."""

    def __init__(self, reason: str) -> None:
        """Initialize instance."""
        ...

    @property
    def Data(self) -> DictionaryBase:
        """DictionaryBase: Property docstring."""
        ...

    @property
    def HResult(self) -> int:
        """int: Property docstring."""
        ...

    @HResult.setter
    def HResult(self, value: int) -> None:
        """Set property value."""
        ...

    @property
    def HelpLink(self) -> str:
        """str: Property docstring."""
        ...

    @HelpLink.setter
    def HelpLink(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def InnerException(self) -> Exception:
        """Exception: Property docstring."""
        ...

    @property
    def Message(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Source(self) -> str:
        """str: Property docstring."""
        ...

    @Source.setter
    def Source(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def StackTrace(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def TargetSite(self) -> MethodBase:
        """MethodBase: Property docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetBaseException(self) -> Exception:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    @overload
    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...


class VolumePresentation:
    """Types of presentation for volume values."""

    AbsoluteCm3: VolumePresentation
    Relative: VolumePresentation
