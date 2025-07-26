from typing import Any, Dict, Generic, List, Optional, Union, overload
from datetime import datetime
from System import Array, Enum, MulticastDelegate, Type, ValueType
from System.Collections import BitArray, IEnumerator
from System.Xml import XmlReader, XmlWriter
from System.Xml.Schema import XmlSchema
from Windows.Media import Color
from Microsoft.Win32 import RegistryHive, RegistryKey
from System import Action, AggregateException, AsyncCallback, Attribute, Delegate, IntPtr, TypeCode
from System.Collections import ReadOnlyList
from System.Globalization import CultureInfo
from System.IO import FileStreamAsyncResult
from System.Reflection import Assembly, AssemblyName, MethodInfo
from System.Runtime.InteropServices import _Attribute
from System.Runtime.InteropServices.WindowsRuntime import Point
from System.Runtime.Serialization import SerializationInfo, StreamingContext
from System.Text import StringBuilder
from System.Threading import SendOrPostCallback, SynchronizationContext
from VMS.TPS.Common.Model.Types import ApplicationScriptApprovalStatus, ApplicationScriptType, ApprovalHistoryEntry, AxisAlignedMargins, BeamNumber, BeamTechnique, BlockType, BrachyTreatmentTechniqueType, CalculationType, ChangeBrachyTreatmentUnitResult, ClinicalGoal, ClosedLeavesMeetingPoint, CourseClinicalStatus, DRRCalculationParameters, DVHEstimateType, DVHEstimationStructureType, DVHPoint, DoseProfile, DoseValue, DoseValuePresentation, ExternalBeamMachineParameters, FitToStructureMargins, Fluence, GantryDirection, ImageApprovalHistoryEntry, ImageProfile, ImagingBeamSetupParameters, IonBeamScanMode, IonPlanNormalizationParameters, IonPlanOptimizationMode, JawFitting, LMCMSSOptions, LMCVOptions, LateralSpreadingDeviceType, LogSeverity, MLCPlanType, MeasureModifier, MeasureType, MetersetValue, OpenLeavesMeetingPoint, OptimizationAvoidanceSector, OptimizationIntermediateDoseOption, OptimizationObjectiveOperator, OptimizationOption, OptimizationOptionsIMPT, OptimizationOptionsIMRT, OptimizationOptionsVMAT, ParticleType, PatientOrientation, PatientSupportType, PlanSetupApprovalStatus, PlanSumOperation, PlanType, PlanUncertaintyType, PrescriptionModifier, PrescriptionType, ProtonBeamLineStatus, ProtonBeamMachineParameters, ProtonDeliveryTimeStatus, RTPrescriptionConstraintType, RTPrescriptionTargetType, RailPosition, RangeModulatorType, RangeShifterType, RegistrationApprovalStatus, SegmentProfile, SeriesModality, SetSourcePositionsResult, SetupTechnique, SmartLMCOptions, StructureApprovalHistoryEntry, StructureCodeInfo, TreatmentSessionStatus, UserIdentity, VRect, VVector, VolumePresentation

class ActiveStructureCodeDictionaries:
    """Provides access to the structure code dictionaries with the active structure codes."""

    def __init__(self, providerFunc: Func[str, Dict[str, StructureCode]]) -> None:
        """Initialize instance."""
        ...

    @property
    def Fma(self) -> StructureCodeDictionary:
        """StructureCodeDictionary: The Foundational Model of Anatomy Ontology structure scheme."""
        ...

    @property
    def RadLex(self) -> StructureCodeDictionary:
        """StructureCodeDictionary: The RSNA RadLex radiology lexicon structure scheme."""
        ...

    @property
    def Srt(self) -> StructureCodeDictionary:
        """StructureCodeDictionary: The SNOMED RT structure scheme."""
        ...

    @property
    def VmsStructCode(self) -> StructureCodeDictionary:
        """StructureCodeDictionary: The Varian 99VMS_STRUCTCODE structure scheme."""
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


class AddOn(ApiDataObject):
    """Represents an add-on, which is a beam modifying device that is inserted into a beam in an accessory slot of the external beam machine. An add-on is used to shape the beam or modulate its intensity or both. Add-ons are blocks, MLCs, wedges, compensators, applicators, a tray, and other devices or materials that can be fixed to a tray to be mounted into an accessory slot."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def CreationDateTime(self) -> Optional[datetime]:
        """Optional[datetime]: The date when this object was created."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class AddOnMaterial(ApiDataObject):
    """Add-on material describes the dosimetric and physical properties of the metal alloy or other substance used to create the add-on."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class Algorithm(ValueType):
    """Algorithm"""

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

    Name: str
    Version: str

class Algorithm(ValueType):
    """Algorithm"""

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

    Name: str
    Version: str

class ApiDataObject(SerializableObject):
    """The base class of objects in the Eclipse Scripting API."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: A comment about the object."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: The date when this object was last modified."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: The name of the last user who modified this object."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: The identifier of the last user who modified this object."""
        ...

    @property
    def Id(self) -> str:
        """str: The identifier of the object."""
        ...

    @property
    def Name(self) -> str:
        """str: The name of the object."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Serves as a hash function for this type.
        
        Returns:
            int: A hash code for the current Object."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def ReadXml(self, reader: XmlReader) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Returns a string that represents the current object.
        
        Returns:
            str: A string that represents the current object."""
        ...

    def WriteXml(self, writer: XmlWriter) -> None:
        """Method docstring."""
        ...


class ApiObjectFactory:
    """Class docstring."""

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


class Application(SerializableObject):
    """The main application interface."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Calculation(self) -> Calculation:
        """Calculation: Calculation related functions"""
        ...

    @property
    def CurrentUser(self) -> User:
        """User: The user who is currently logged on."""
        ...

    @property
    def Equipment(self) -> Equipment:
        """Equipment: Provides access to clinical devices and accessories."""
        ...

    @property
    def PatientSummaries(self) -> List[PatientSummary]:
        """List[PatientSummary]: Fetches patient summaries from the database."""
        ...

    @property
    def ScriptEnvironment(self) -> ScriptEnvironment:
        """ScriptEnvironment: Gets the script environment."""
        ...

    @property
    def StructureCodes(self) -> ActiveStructureCodeDictionaries:
        """ActiveStructureCodeDictionaries: Provides access to the structure code dictionaries with the active structure codes."""
        ...

    def ClosePatient(self) -> None:
        """Closes the current patient. If the script tries to access the data of a closed patient, an access violation exception occurs."""
        ...

    @staticmethod
    def CreateApplication(username: str, password: str) -> Application:
        """Creates an application instance for a standalone script and logs into the system.
        
        Code that uses ESAPI must run on a single-threaded apartment (STAThread). The Dispose method must be called before the program exits. Only one application instance may be created during the entire run of the program.
        
        Returns:
            Application: Application object that is the root of the data model."""
        ...

    @overload
    @staticmethod
    def CreateApplication() -> Application:
        """Creates an application instance for a standalone script and logs into the system.
        
        Code that uses ESAPI must run on a single-threaded apartment (STAThread). The Dispose method must be called before the program exits. Only one application instance may be created during the entire run of the program.
        
        Returns:
            Application: Application object that is the root of the data model."""
        ...

    def Dispose(self) -> None:
        """Releases all unmanaged resources of this object."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def OpenPatient(self, patientSummary: PatientSummary) -> Patient:
        """Method docstring."""
        ...

    def OpenPatientById(self, id: str) -> Patient:
        """Method docstring."""
        ...

    def ReadXml(self, reader: XmlReader) -> None:
        """Method docstring."""
        ...

    def SaveModifications(self) -> None:
        """[Availability of this method depends on your Eclipse Scripting API license] Saves data modifications to the database if saving is allowed. Note: Calling this method can cause a multi-user warning dialog box to appear if the same patient is modified by other parties."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    def WriteXml(self, writer: XmlWriter) -> None:
        """Method docstring."""
        ...


class ApplicationPackage(ApiDataObject):
    """Presents the application package information in the system. Note: not all methods are necessarily Published at the moment."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def ApprovalStatus(self) -> ApplicationScriptApprovalStatus:
        """ApplicationScriptApprovalStatus: The status of the application package. Possible values are defined by a lookup RT_APP_EXTENSION_STATUS."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Description(self) -> str:
        """str: Description of functionality provided by the package."""
        ...

    @property
    def ExpirationDate(self) -> Optional[datetime]:
        """Optional[datetime]: An optional expiration date of the package. The package cannot be executed after expiration date. The date is presented in UTC."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def PackageId(self) -> str:
        """str: Unique Package ID."""
        ...

    @property
    def PackageName(self) -> str:
        """str: The full name of the package."""
        ...

    @property
    def PackageVersion(self) -> str:
        """str: The version number of the package."""
        ...

    @property
    def PublisherData(self) -> str:
        """str: Optional JSON data that can be used by package internally, e.g. customer key."""
        ...

    @property
    def PublisherName(self) -> str:
        """str: The name of the organization or author that created the package. This is a free text that can be set by the approver."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class ApplicationScript(ApiDataObject):
    """Presents the application script information in the system. The location of the script file is not stored in the system."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def ApprovalStatus(self) -> ApplicationScriptApprovalStatus:
        """ApplicationScriptApprovalStatus: The status of the script."""
        ...

    @property
    def ApprovalStatusDisplayText(self) -> str:
        """str: The display text of the approval status."""
        ...

    @property
    def AssemblyName(self) -> AssemblyName:
        """AssemblyName: The full name of the script assembly."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def ExpirationDate(self) -> Optional[datetime]:
        """Optional[datetime]: An optional expiration date of the script. The script cannot be executed after expiration date. The date is presented in UTC."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def IsReadOnlyScript(self) -> bool:
        """bool: Returns true if the script is intended only to read patient data."""
        ...

    @property
    def IsWriteableScript(self) -> bool:
        """bool: Returns true if the script is intended to modify persistent data."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def PublisherName(self) -> str:
        """str: The name of the organization or author that created the script. This is a free text that can be set by the approver."""
        ...

    @property
    def ScriptType(self) -> ApplicationScriptType:
        """ApplicationScriptType: The type of the application script."""
        ...

    @property
    def StatusDate(self) -> Optional[datetime]:
        """Optional[datetime]: A timestamp of the last approval status modification."""
        ...

    @property
    def StatusUserIdentity(self) -> UserIdentity:
        """UserIdentity: The identity of the user who last modified the approval status."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class ApplicationScriptLog(ApiDataObject):
    """The log entry of the application script execution."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def CourseId(self) -> str:
        """str: The identifier of the course that was modified by the script."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def PatientId(self) -> str:
        """str: The identifier of the patient that was modified by the script."""
        ...

    @property
    def PlanSetupId(self) -> str:
        """str: The identifier of the plan that was modified by the script, or an empty string if the script did not modify the plan."""
        ...

    @property
    def PlanUID(self) -> str:
        """str: The DICOM UID of the plan that was modified by the script, or an empty string if the script did not modify the plan."""
        ...

    @property
    def Script(self) -> ApplicationScript:
        """ApplicationScript: The script that modified the plan or structure set."""
        ...

    @property
    def ScriptFullName(self) -> str:
        """str: The full name of the script assembly that modified the plan or structure set. A System.Reflection.AssemblyName object can be created from the string."""
        ...

    @property
    def StructureSetId(self) -> str:
        """str: The identifier of the structure set that was modified by the script, or an empty string if the script did not modify the structure set."""
        ...

    @property
    def StructureSetUID(self) -> str:
        """str: The DICOM UID of the structure set that was modified by the script, or an empty string if the script did not modify the structure set."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class Applicator(AddOn):
    """An applicator add-on, either an electron applicator or cone applicator."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def ApplicatorLengthInMM(self) -> float:
        """float: Applicator length in mm."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def CreationDateTime(self) -> Optional[datetime]:
        """Optional[datetime]: Property docstring."""
        ...

    @property
    def DiameterInMM(self) -> float:
        """float: Applicator Diameter in mm."""
        ...

    @property
    def FieldSizeX(self) -> float:
        """float: The field width in direction X (cm)."""
        ...

    @property
    def FieldSizeY(self) -> float:
        """float: The field width in direction Y (cm)."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def IsStereotactic(self) -> bool:
        """bool: Is stereotactic."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class AsyncPump:
    """Provides a pump that supports running asynchronous methods on the current thread."""

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


class Beam(ApiDataObject):
    """Represents one beam (also referred to as "field") of an external beam treatment plan. See the definition of DICOM RT Beam for more details."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Applicator(self) -> Applicator:
        """Applicator: An applicator is a specific add-on used in the beam."""
        ...

    @property
    def ArcLength(self) -> float:
        """float: The arc length."""
        ...

    @property
    def AreControlPointJawsMoving(self) -> bool:
        """bool: Checks if jaws are moving."""
        ...

    @property
    def AverageSSD(self) -> float:
        """float: The average Source-to-Skin Distance (SSD) of an arc beam."""
        ...

    @property
    def BeamNumber(self) -> int:
        """int: DICOM RT Beam Number. The value is unique within the plan in which it is created."""
        ...

    @property
    def BeamTechnique(self) -> BeamTechnique:
        """BeamTechnique: Returns an enumeration that describes the type of the treatment field."""
        ...

    @property
    def Blocks(self) -> List[Block]:
        """List[Block]: A collection of installed blocks."""
        ...

    @property
    def Boluses(self) -> List[Bolus]:
        """List[Bolus]: A collection of beam boluses."""
        ...

    @property
    def CalculationLogs(self) -> List[BeamCalculationLog]:
        """List[BeamCalculationLog]: A collection of beam calculation logs."""
        ...

    @property
    def CollimatorRotation(self) -> float:
        """float: Collimator rotation"""
        ...

    @property
    def Comment(self) -> str:
        """str: [Availability of this property depends on your Eclipse Scripting API license] The Beam comment."""
        ...

    @Comment.setter
    def Comment(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def Compensator(self) -> Compensator:
        """Compensator: The compensator."""
        ...

    @property
    def ControlPoints(self) -> ControlPointCollection:
        """ControlPointCollection: An enumerable sequence of machine parameters that describe the planned treatment beam."""
        ...

    @property
    def CreationDateTime(self) -> Optional[datetime]:
        """Optional[datetime]: The date when this object was created."""
        ...

    @property
    def Dose(self) -> BeamDose:
        """BeamDose: The dose for the beam. Returns null if the dose is not calculated."""
        ...

    @property
    def DoseRate(self) -> int:
        """int: The dose rate of the treatment machine in MU/min."""
        ...

    @property
    def DosimetricLeafGap(self) -> float:
        """float: The dosimetric leaf gap that has been configured for the Dynamic Multileaf Collimator (DMLC) beams in the system. The dosimetric leaf gap is used for accounting for dose transmission through rounded MLC leaves."""
        ...

    @property
    def EnergyMode(self) -> EnergyMode:
        """EnergyMode: Energy mode of the treatment machine."""
        ...

    @property
    def EnergyModeDisplayName(self) -> str:
        """str: The display name of the energy mode. For example '18E' or '6X-SRS'."""
        ...

    @property
    def FieldReferencePoints(self) -> List[FieldReferencePoint]:
        """List[FieldReferencePoint]: A collection of field reference points."""
        ...

    @property
    def GantryDirection(self) -> GantryDirection:
        """GantryDirection: The gantry rotation direction: clockwise (CW), counterclockwise (CCW), or none."""
        ...

    @property
    def HasAllMLCLeavesClosed(self) -> bool:
        """bool: Returns true if all MLC leaves are closed."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: [Availability of this property depends on your Eclipse Scripting API license] The identifier of the Beam."""
        ...

    @Id.setter
    def Id(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def IsGantryExtended(self) -> bool:
        """bool: Checks if the gantry rotation is extended. For arc beams, checks if the gantry rotation is extended at the start angle."""
        ...

    @property
    def IsGantryExtendedAtStopAngle(self) -> bool:
        """bool: Checks if the gantry rotation is extended at the stop angle of an arc beam."""
        ...

    @property
    def IsIMRT(self) -> bool:
        """bool: Checks if a beam is IMRT."""
        ...

    @property
    def IsImagingTreatmentField(self) -> bool:
        """bool: Checks if a beam is an Imaging Treatment Beam, i.e., a beam that is used to take an MV image and whose dose is calculated and taken into account in treatment planning."""
        ...

    @property
    def IsSetupField(self) -> bool:
        """bool: Checks if a beam is a setup field."""
        ...

    @property
    def IsocenterPosition(self) -> VVector:
        """VVector: The position of the isocenter."""
        ...

    @property
    def MLC(self) -> MLC:
        """MLC: Returns a hardware description of the Multileaf Collimator (MLC) used in an MLC plan, or null if no MLC exists."""
        ...

    @property
    def MLCPlanType(self) -> MLCPlanType:
        """MLCPlanType: The type of the Multileaf Collimator (MLC) plan."""
        ...

    @property
    def MLCTransmissionFactor(self) -> float:
        """float: The transmission factor of the Multileaf Collimator (MLC) material."""
        ...

    @property
    def Meterset(self) -> MetersetValue:
        """MetersetValue: The meterset value of the beam."""
        ...

    @property
    def MetersetPerGy(self) -> float:
        """float: The calculated meterset/Gy value for the beam."""
        ...

    @property
    def MotionCompensationTechnique(self) -> str:
        """str: DICOM (respiratory) motion compensation technique. Returns an empty string if motion compensation technique is not used."""
        ...

    @property
    def MotionSignalSource(self) -> str:
        """str: DICOM (respiratory) signal source. Returns an empty string if motion compensation technique is not used."""
        ...

    @property
    def Name(self) -> str:
        """str: [Availability of this property depends on your Eclipse Scripting API license] The name of the Beam."""
        ...

    @Name.setter
    def Name(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def NormalizationFactor(self) -> float:
        """float: The beam normalization factor."""
        ...

    @property
    def NormalizationMethod(self) -> str:
        """str: The beam normalization method."""
        ...

    @property
    def Plan(self) -> PlanSetup:
        """PlanSetup: Used for navigating to parent Plan"""
        ...

    @property
    def PlannedSSD(self) -> float:
        """float: The Source-to-Skin Distance (SSD) value defined by the user."""
        ...

    @property
    def ReferenceImage(self) -> Image:
        """Image: The reference image of the beam."""
        ...

    @property
    def SSD(self) -> float:
        """float: The Source-to-Skin Distance (SSD). For arc beams, the SSD at the start angle. This value is calculated from the geometrical setup of the beam."""
        ...

    @property
    def SSDAtStopAngle(self) -> float:
        """float: The Source-to-Skin Distance (SSD) at the stop angle of an arc beam. This value is calculated from the geometrical setup of the beam."""
        ...

    @property
    def SetupNote(self) -> str:
        """str: The setup note of the field."""
        ...

    @SetupNote.setter
    def SetupNote(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def SetupTechnique(self) -> SetupTechnique:
        """SetupTechnique: The setup technique."""
        ...

    @property
    def Technique(self) -> Technique:
        """Technique: The technique used in the planning beam."""
        ...

    @property
    def ToleranceTableLabel(self) -> str:
        """str: User-defined label for the referenced tolerance table, or an empty string if there is no reference to a tolerance table."""
        ...

    @property
    def Trays(self) -> List[Tray]:
        """List[Tray]: A collection of installed trays."""
        ...

    @property
    def TreatmentTime(self) -> float:
        """float: The treatment time set for the beam in seconds. Plan Approval wizard sets this value by default."""
        ...

    @property
    def TreatmentUnit(self) -> ExternalBeamTreatmentUnit:
        """ExternalBeamTreatmentUnit: The external beam treatment unit associated with this beam."""
        ...

    @property
    def Wedges(self) -> List[Wedge]:
        """List[Wedge]: A collection of installed wedges."""
        ...

    @property
    def WeightFactor(self) -> float:
        """float: The weight factor of the beam."""
        ...

    def AddBolus(self, bolus: Bolus) -> None:
        """Method docstring."""
        ...

    @overload
    def AddBolus(self, bolusId: str) -> None:
        """Method docstring."""
        ...

    def AddFlatteningSequence(self) -> bool:
        """[Availability of this method depends on your Eclipse Scripting API license] Adds a flattening sequence to a static Halcyon field. Throws an exception if the field is not a Halcyon field.
        
        Returns:
            bool: True if flattening sequence was added."""
        ...

    def ApplyParameters(self, beamParams: BeamParameters) -> None:
        """Method docstring."""
        ...

    def CalculateAverageLeafPairOpenings(self) -> Dict[int, float]:
        """Calculate and get Average Leaf Pair Opening values. ALPO values are calculated on the fly (not serialized). Returns a Dictionary. Key element is the index of carriage group in the field and value element is the ALPO value for that carriage group."""
        ...

    def CanSetOptimalFluence(self, fluence: Fluence, message: str) -> bool:
        """Method docstring."""
        ...

    def CollimatorAngleToUser(self, val: float) -> float:
        """Method docstring."""
        ...

    def CountSubfields(self) -> int:
        """Counts and returns Subfield count."""
        ...

    def CreateOrReplaceDRR(self, parameters: DRRCalculationParameters) -> Image:
        """Method docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def FitCollimatorToStructure(self, margins: FitToStructureMargins, structure: Structure, useAsymmetricXJaws: bool, useAsymmetricYJaws: bool, optimizeCollimatorRotation: bool) -> None:
        """Method docstring."""
        ...

    def FitMLCToOutline(self, outline: Array[Array[Point]]) -> None:
        """Method docstring."""
        ...

    @overload
    def FitMLCToOutline(self, outline: Array[Array[Point]], optimizeCollimatorRotation: bool, jawFit: JawFitting, olmp: OpenLeavesMeetingPoint, clmp: ClosedLeavesMeetingPoint) -> None:
        """Method docstring."""
        ...

    def FitMLCToStructure(self, structure: Structure) -> None:
        """Method docstring."""
        ...

    @overload
    def FitMLCToStructure(self, margins: FitToStructureMargins, structure: Structure, optimizeCollimatorRotation: bool, jawFit: JawFitting, olmp: OpenLeavesMeetingPoint, clmp: ClosedLeavesMeetingPoint) -> None:
        """Method docstring."""
        ...

    def GantryAngleToUser(self, val: float) -> float:
        """Method docstring."""
        ...

    def GetCAXPathLengthInBolus(self, bolus: Bolus) -> float:
        """Method docstring."""
        ...

    def GetEditableParameters(self) -> BeamParameters:
        """Returns an editable copy of the beam parameters. The returned BeamParameters object is not updated if the beam parameters in the data model are changed, for example, by using another BeamParameters object.
        
        Returns:
            BeamParameters: Returns a new parameters object. Its values are copied from the corresponding properties of this object."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetOptimalFluence(self) -> Fluence:
        """Gets the optimal fluence for this beam. Returns null if optimal fluence does not exist.
        
        Returns:
            Fluence: Returns the optimized fluence, if it exists. Otherwise null."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
        ...

    def GetSourceLocation(self, gantryAngle: float) -> VVector:
        """Method docstring."""
        ...

    def GetSourceToBolusDistance(self, bolus: Bolus) -> float:
        """Method docstring."""
        ...

    def GetStructureOutlines(self, structure: Structure, inBEV: bool) -> Array[Array[Point]]:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def JawPositionsToUserString(self, val: VRect[float]) -> str:
        """Method docstring."""
        ...

    def PatientSupportAngleToUser(self, val: float) -> float:
        """Method docstring."""
        ...

    def ReadXml(self, reader: XmlReader) -> None:
        """Method docstring."""
        ...

    def RemoveBolus(self, bolus: Bolus) -> bool:
        """Method docstring."""
        ...

    @overload
    def RemoveBolus(self, bolusId: str) -> bool:
        """Method docstring."""
        ...

    def RemoveFlatteningSequence(self) -> bool:
        """[Availability of this method depends on your Eclipse Scripting API license] Removes the flattening sequence from a Halcyon field. Throws an exception if the field is not a Halcyon field.
        
        Returns:
            bool: True if flattening sequence was removed."""
        ...

    def SetOptimalFluence(self, fluence: Fluence) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    def WriteXml(self, writer: XmlWriter) -> None:
        """Method docstring."""
        ...


class BeamCalculationLog(SerializableObject):
    """Represents a beam calculation log."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Beam(self) -> Beam:
        """Beam: Used for navigating to parent Beam"""
        ...

    @property
    def Category(self) -> str:
        """str: The log category, for example, "Dose", or "Optimization"."""
        ...

    @property
    def MessageLines(self) -> List[str]:
        """List[str]: The log as an array of lines."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class BeamDose(Dose):
    """Represents a dose that is connected to a Beam."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def DoseMax3D(self) -> DoseValue:
        """DoseValue: Property docstring."""
        ...

    @property
    def DoseMax3DLocation(self) -> VVector:
        """VVector: Property docstring."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Isodoses(self) -> List[Isodose]:
        """List[Isodose]: Property docstring."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Origin(self) -> VVector:
        """VVector: Property docstring."""
        ...

    @property
    def Series(self) -> Series:
        """Series: Property docstring."""
        ...

    @property
    def SeriesUID(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def UID(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def XDirection(self) -> VVector:
        """VVector: Property docstring."""
        ...

    @property
    def XRes(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def XSize(self) -> int:
        """int: Property docstring."""
        ...

    @property
    def YDirection(self) -> VVector:
        """VVector: Property docstring."""
        ...

    @property
    def YRes(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def YSize(self) -> int:
        """int: Property docstring."""
        ...

    @property
    def ZDirection(self) -> VVector:
        """VVector: Property docstring."""
        ...

    @property
    def ZRes(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def ZSize(self) -> int:
        """int: Property docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetAbsoluteBeamDoseValue(self, relative: DoseValue) -> DoseValue:
        """Method docstring."""
        ...

    def GetDoseProfile(self, start: VVector, stop: VVector, preallocatedBuffer: Array[float]) -> DoseProfile:
        """Method docstring."""
        ...

    def GetDoseToPoint(self, at: VVector) -> DoseValue:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def GetVoxels(self, planeIndex: int, preallocatedBuffer: Array[int]) -> None:
        """Method docstring."""
        ...

    def ReadXml(self, reader: XmlReader) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    def VoxelToDoseValue(self, voxelValue: int) -> DoseValue:
        """Method docstring."""
        ...

    def WriteXml(self, writer: XmlWriter) -> None:
        """Method docstring."""
        ...


class BeamParameters:
    """An editable copy of the parameters of a treatment beam.
    
    To apply the parameters, call the"""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def ControlPoints(self) -> List[ControlPointParameters]:
        """List[ControlPointParameters]: Editable control point parameters copied from the treatment beam."""
        ...

    @property
    def GantryDirection(self) -> GantryDirection:
        """GantryDirection: The direction of gantry rotation (clockwise or counterclockwise)."""
        ...

    @property
    def Isocenter(self) -> VVector:
        """VVector: A copy of the isocenter position, in millimeters."""
        ...

    @Isocenter.setter
    def Isocenter(self, value: VVector) -> None:
        """Set property value."""
        ...

    @property
    def WeightFactor(self) -> float:
        """float: The weight factor of the beam."""
        ...

    @WeightFactor.setter
    def WeightFactor(self, value: float) -> None:
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

    def SetAllLeafPositions(self, leafPositions: Array[float]) -> None:
        """Method docstring."""
        ...

    def SetJawPositions(self, positions: VRect[float]) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...


class BeamUncertainty(ApiDataObject):
    """Access to beam uncertainty."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Beam(self) -> Beam:
        """Beam: The beam to which this uncertainty is linked."""
        ...

    @property
    def BeamNumber(self) -> BeamNumber:
        """BeamNumber: Beam number of the related beam."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Dose(self) -> Dose:
        """Dose: Dose of this beam uncertainty."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class Block(ApiDataObject):
    """Represents a block add-on, a custom-made beam collimating material fixed to a tray, used to shape the beam."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def AddOnMaterial(self) -> AddOnMaterial:
        """AddOnMaterial: The dosimetric material of the block."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def IsDiverging(self) -> bool:
        """bool: Checks if the block cut is diverging."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Outline(self) -> Array[Array[Point]]:
        """Array[Array[Point]]: The block outline points in field coordinates."""
        ...

    @Outline.setter
    def Outline(self, value: Array[Array[Point]]) -> None:
        """Set property value."""
        ...

    @property
    def TransmissionFactor(self) -> float:
        """float: The transmission factor of the selected material."""
        ...

    @property
    def Tray(self) -> Tray:
        """Tray: The tray on which the block is installed."""
        ...

    @property
    def TrayTransmissionFactor(self) -> float:
        """float: The transmission factor of the selected tray."""
        ...

    @property
    def Type(self) -> BlockType:
        """BlockType: The type of the block: shielding or aperture."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class Bolus(SerializableObject):
    """Represents a bolus, which is custom-made material that is usually fixed to the patient's skin for treatment. The bolus is used to modulate the depth dose profile of a beam."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Id(self) -> str:
        """str: The identifier of the bolus."""
        ...

    @property
    def MaterialCTValue(self) -> float:
        """float: The CT value of the bolus material (HU)."""
        ...

    @property
    def Name(self) -> str:
        """str: The name of the bolus."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class BrachyFieldReferencePoint(ApiDataObject):
    """This object links a Brachy field to a reference point."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def FieldDose(self) -> DoseValue:
        """DoseValue: The field dose."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def IsFieldDoseNominal(self) -> bool:
        """bool: Checks if the field dose is nominal (the real calculated field dose is not known). If the field doses at a reference point are nominal, they alone cannot be used to verify MU calculation."""
        ...

    @property
    def IsPrimaryReferencePoint(self) -> bool:
        """bool: Checks if the reference point is primary."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def RefPointLocation(self) -> VVector:
        """VVector: The location of the reference point."""
        ...

    @property
    def ReferencePoint(self) -> ReferencePoint:
        """ReferencePoint: Used for navigating to an underlying reference point."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class BrachyPlanSetup(PlanSetup):
    """Represents a brachytherapy treatment plan."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def ApplicationScriptLogs(self) -> List[ApplicationScriptLog]:
        """List[ApplicationScriptLog]: Property docstring."""
        ...

    @property
    def ApplicationSetupType(self) -> str:
        """str: The application setup type of this brachytherapy plan. Possible types are: "FLETCHER_SUIT", "DELCLOS", "BLOEDORN", "JOSLIN_FLYNN", "CHANDIGARH", "MANCHESTER", "HENSCHKE", "NASOPHARYNGEAL", "OESOPHAGEAL", "ENDOBRONCHIAL", "SYED_NEBLETT", "ENDORECTAL", "PERINEAL",  "HAM_FLAB", "EYE_PLAQUE", and "OTHER"."""
        ...

    @property
    def ApprovalHistory(self) -> List[ApprovalHistoryEntry]:
        """List[ApprovalHistoryEntry]: Property docstring."""
        ...

    @property
    def ApprovalStatus(self) -> PlanSetupApprovalStatus:
        """PlanSetupApprovalStatus: Property docstring."""
        ...

    @property
    def ApprovalStatusAsString(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def BaseDosePlanningItem(self) -> PlanningItem:
        """PlanningItem: Property docstring."""
        ...

    @BaseDosePlanningItem.setter
    def BaseDosePlanningItem(self, value: PlanningItem) -> None:
        """Set property value."""
        ...

    @property
    def Beams(self) -> List[Beam]:
        """List[Beam]: Property docstring."""
        ...

    @property
    def BeamsInTreatmentOrder(self) -> List[Beam]:
        """List[Beam]: Property docstring."""
        ...

    @property
    def BrachyTreatmentTechnique(self) -> BrachyTreatmentTechniqueType:
        """BrachyTreatmentTechniqueType: The treatment technique of this brachytherapy plan. Possible techniques are "INTRALUMENARY", "INTRACAVITARY", "INTERSTITIAL", "CONTACT", "INTRAVASCULAR", and "PERMANENT"."""
        ...

    @BrachyTreatmentTechnique.setter
    def BrachyTreatmentTechnique(self, value: BrachyTreatmentTechniqueType) -> None:
        """Set property value."""
        ...

    @property
    def Catheters(self) -> List[Catheter]:
        """List[Catheter]: The catheters or applicator channel centerlines of this brachytherapy plan, including any catheters associated with"""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @Comment.setter
    def Comment(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def Course(self) -> Course:
        """Course: Property docstring."""
        ...

    @property
    def CreationDateTime(self) -> Optional[datetime]:
        """Optional[datetime]: Property docstring."""
        ...

    @property
    def CreationUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def DVHEstimates(self) -> List[EstimatedDVH]:
        """List[EstimatedDVH]: Property docstring."""
        ...

    @property
    def Dose(self) -> PlanningItemDose:
        """PlanningItemDose: Property docstring."""
        ...

    @property
    def DosePerFraction(self) -> DoseValue:
        """DoseValue: Property docstring."""
        ...

    @property
    def DosePerFractionInPrimaryRefPoint(self) -> DoseValue:
        """DoseValue: Property docstring."""
        ...

    @property
    def DoseValuePresentation(self) -> DoseValuePresentation:
        """DoseValuePresentation: Property docstring."""
        ...

    @DoseValuePresentation.setter
    def DoseValuePresentation(self, value: DoseValuePresentation) -> None:
        """Set property value."""
        ...

    @property
    def ElectronCalculationModel(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def ElectronCalculationOptions(self) -> Dict[str, str]:
        """Dict[str, str]: Property docstring."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
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
    def IntegrityHash(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def IsDoseValid(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsTreated(self) -> bool:
        """bool: Property docstring."""
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
    def NumberOfFractions(self) -> Optional[int]:
        """Optional[int]: Property docstring."""
        ...

    @property
    def NumberOfPdrPulses(self) -> Optional[int]:
        """Optional[int]: The number of pulses in a brachytherapy Pulse Dose Rate (PDR) treatment. Null if the plan is not for a PDR treatment."""
        ...

    @property
    def OptimizationSetup(self) -> OptimizationSetup:
        """OptimizationSetup: Property docstring."""
        ...

    @property
    def PatientSupportDevice(self) -> PatientSupportDevice:
        """PatientSupportDevice: Property docstring."""
        ...

    @property
    def PdrPulseInterval(self) -> Optional[float]:
        """Optional[float]: The pulse interval in a brachytherapy Pulse Dose Rate (PDR) treatment in seconds. Null if the plan is not for a PDR treatment."""
        ...

    @property
    def PhotonCalculationModel(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def PhotonCalculationOptions(self) -> Dict[str, str]:
        """Dict[str, str]: Property docstring."""
        ...

    @property
    def PlanIntent(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def PlanIsInTreatment(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def PlanNormalizationMethod(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def PlanNormalizationPoint(self) -> VVector:
        """VVector: Property docstring."""
        ...

    @property
    def PlanNormalizationValue(self) -> float:
        """float: Property docstring."""
        ...

    @PlanNormalizationValue.setter
    def PlanNormalizationValue(self, value: float) -> None:
        """Set property value."""
        ...

    @property
    def PlanObjectiveStructures(self) -> List[str]:
        """List[str]: Property docstring."""
        ...

    @property
    def PlanType(self) -> PlanType:
        """PlanType: Property docstring."""
        ...

    @property
    def PlanUncertainties(self) -> List[PlanUncertainty]:
        """List[PlanUncertainty]: Property docstring."""
        ...

    @property
    def PlannedDosePerFraction(self) -> DoseValue:
        """DoseValue: Property docstring."""
        ...

    @property
    def PlanningApprovalDate(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def PlanningApprover(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def PlanningApproverDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def PredecessorPlan(self) -> PlanSetup:
        """PlanSetup: Property docstring."""
        ...

    @property
    def PredecessorPlanUID(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def PrescribedDosePerFraction(self) -> DoseValue:
        """DoseValue: Property docstring."""
        ...

    @property
    def PrescribedPercentage(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def PrimaryReferencePoint(self) -> ReferencePoint:
        """ReferencePoint: Property docstring."""
        ...

    @property
    def ProtocolID(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def ProtocolPhaseID(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def ProtonCalculationModel(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def ProtonCalculationOptions(self) -> Dict[str, str]:
        """Dict[str, str]: Property docstring."""
        ...

    @property
    def RTPrescription(self) -> RTPrescription:
        """RTPrescription: Property docstring."""
        ...

    @property
    def ReferenceLines(self) -> List[Structure]:
        """List[Structure]: Collection of reference lines in the plan."""
        ...

    @property
    def ReferencePoints(self) -> List[ReferencePoint]:
        """List[ReferencePoint]: Property docstring."""
        ...

    @property
    def SeedCollections(self) -> List[SeedCollection]:
        """List[SeedCollection]: The seed collections of this brachytherapy plan."""
        ...

    @property
    def Series(self) -> Series:
        """Series: Property docstring."""
        ...

    @property
    def SeriesUID(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def SolidApplicators(self) -> List[BrachySolidApplicator]:
        """List[BrachySolidApplicator]: The solid applicator parts of this brachytherapy plan."""
        ...

    @property
    def StructureSet(self) -> StructureSet:
        """StructureSet: Property docstring."""
        ...

    @property
    def StructuresSelectedForDvh(self) -> List[Structure]:
        """List[Structure]: Property docstring."""
        ...

    @property
    def TargetVolumeID(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def TotalDose(self) -> DoseValue:
        """DoseValue: Property docstring."""
        ...

    @property
    def TotalPrescribedDose(self) -> DoseValue:
        """DoseValue: Property docstring."""
        ...

    @property
    def TreatmentApprovalDate(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def TreatmentApprover(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def TreatmentApproverDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def TreatmentDateTime(self) -> Optional[datetime]:
        """Optional[datetime]: The treatment date of this brachytherapy plan."""
        ...

    @TreatmentDateTime.setter
    def TreatmentDateTime(self, value: Optional[datetime]) -> None:
        """Set property value."""
        ...

    @property
    def TreatmentOrientation(self) -> PatientOrientation:
        """PatientOrientation: Property docstring."""
        ...

    @property
    def TreatmentOrientationAsString(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def TreatmentPercentage(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def TreatmentSessions(self) -> List[PlanTreatmentSession]:
        """List[PlanTreatmentSession]: Property docstring."""
        ...

    @property
    def TreatmentTechnique(self) -> str:
        """str: The treatment technique of this brachytherapy plan. Possible techniques are "INTRALUMENARY", "INTRACAVITARY", "INTERSTITIAL", "CONTACT", "INTRAVASCULAR", and "PERMANENT"."""
        ...

    @property
    def UID(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def UseGating(self) -> bool:
        """bool: Property docstring."""
        ...

    @UseGating.setter
    def UseGating(self, value: bool) -> None:
        """Set property value."""
        ...

    @property
    def VerifiedPlan(self) -> PlanSetup:
        """PlanSetup: Property docstring."""
        ...

    def AddCatheter(self, catheterId: str, treatmentUnit: BrachyTreatmentUnit, outputDiagnostics: StringBuilder, appendChannelNumToId: bool, channelNum: int) -> Catheter:
        """Method docstring."""
        ...

    def AddLocationToExistingReferencePoint(self, location: VVector, referencePoint: ReferencePoint) -> None:
        """Method docstring."""
        ...

    def AddPlanUncertaintyWithParameters(self, uncertaintyType: PlanUncertaintyType, planSpecificUncertainty: bool, HUConversionError: float, isocenterShift: VVector) -> PlanUncertainty:
        """Method docstring."""
        ...

    def AddReferencePoint(self, target: bool, id: str) -> ReferencePoint:
        """Method docstring."""
        ...

    @overload
    def AddReferencePoint(self, target: bool, location: Optional[VVector], id: str) -> ReferencePoint:
        """Method docstring."""
        ...

    @overload
    def AddReferencePoint(self, refPoint: ReferencePoint) -> None:
        """Method docstring."""
        ...

    def CalculateAccurateTG43DoseProfile(self, start: VVector, stop: VVector, preallocatedBuffer: Array[float]) -> DoseProfile:
        """Method docstring."""
        ...

    def CalculateTG43Dose(self) -> CalculateBrachy3DDoseResult:
        """Calculates 3D dose using the TG-43 brachy calculator."""
        ...

    def ChangeTreatmentUnit(self, treatmentUnit: BrachyTreatmentUnit, keepDoseIntact: bool, messages: List) -> ChangeBrachyTreatmentUnitResult:
        """Method docstring."""
        ...

    def ClearCalculationModel(self, calculationType: CalculationType) -> None:
        """Method docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetCalculationModel(self, calculationType: CalculationType) -> str:
        """Method docstring."""
        ...

    def GetCalculationOption(self, calculationModel: str, optionName: str, optionValue: str) -> bool:
        """Method docstring."""
        ...

    def GetCalculationOptions(self, calculationModel: str) -> Dict[str, str]:
        """Method docstring."""
        ...

    def GetClinicalGoals(self) -> List[ClinicalGoal]:
        """Method docstring."""
        ...

    def GetDVHCumulativeData(self, structure: Structure, dosePresentation: DoseValuePresentation, volumePresentation: VolumePresentation, binWidth: float) -> DVHData:
        """Method docstring."""
        ...

    def GetDoseAtVolume(self, structure: Structure, volume: float, volumePresentation: VolumePresentation, requestedDosePresentation: DoseValuePresentation) -> DoseValue:
        """Method docstring."""
        ...

    def GetDvhEstimationModelName(self) -> str:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetProtocolPrescriptionsAndMeasures(self, prescriptions: List, measures: List) -> None:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def GetVolumeAtDose(self, structure: Structure, dose: DoseValue, requestedVolumePresentation: VolumePresentation) -> float:
        """Method docstring."""
        ...

    def IsEntireBodyAndBolusesCoveredByCalculationArea(self) -> bool:
        """Method docstring."""
        ...

    def IsValidForPlanApproval(self, validationResults: List) -> bool:
        """Method docstring."""
        ...

    def MoveToCourse(self, destinationCourse: Course) -> None:
        """Method docstring."""
        ...

    def ReadXml(self, reader: XmlReader) -> None:
        """Method docstring."""
        ...

    def RemoveReferencePoint(self, refPoint: ReferencePoint) -> None:
        """Method docstring."""
        ...

    def SetCalculationModel(self, calculationType: CalculationType, model: str) -> None:
        """Method docstring."""
        ...

    def SetCalculationOption(self, calculationModel: str, optionName: str, optionValue: str) -> bool:
        """Method docstring."""
        ...

    def SetPrescription(self, numberOfFractions: int, dosePerFraction: DoseValue, treatmentPercentage: float) -> None:
        """Method docstring."""
        ...

    def SetTargetStructureIfNoDose(self, newTargetStructure: Structure, errorHint: StringBuilder) -> bool:
        """Method docstring."""
        ...

    def SetTreatmentOrder(self, orderedBeams: List[Beam]) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    def WriteXml(self, writer: XmlWriter) -> None:
        """Method docstring."""
        ...


class BrachySolidApplicator(ApiDataObject):
    """Represents a brachytherapy solid applicator part, such as a tandem or ovoid in a Fletcher Suit Delclos (FSD) applicator set. This class holds only the metadata related to the solid applicator part, and links to the"""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def ApplicatorSetName(self) -> str:
        """str: The name of the solid applicator set to which this part belongs."""
        ...

    @property
    def ApplicatorSetType(self) -> str:
        """str: The type of the solid applicator set to which this part belongs."""
        ...

    @property
    def Category(self) -> str:
        """str: The category of the solid applicator set to which this part belongs."""
        ...

    @property
    def Catheters(self) -> List[Catheter]:
        """List[Catheter]: The channel(s) of this solid applicator part."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def GroupNumber(self) -> int:
        """int: Applicator Group number."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Note(self) -> str:
        """str: A note or short description of the solid applicator part."""
        ...

    @property
    def PartName(self) -> str:
        """str: The name of the solid applicator part."""
        ...

    @property
    def PartNumber(self) -> str:
        """str: The part number of the solid applicator."""
        ...

    @property
    def Summary(self) -> str:
        """str: A summary of the solid applicator set to which this part belongs."""
        ...

    @property
    def UID(self) -> str:
        """str: The unique identifier of the solid applicator part."""
        ...

    @property
    def Vendor(self) -> str:
        """str: The vendor of the solid applicator set to which this part belongs."""
        ...

    @property
    def Version(self) -> str:
        """str: The version of the solid applicator part."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class BrachyTreatmentUnit(ApiDataObject):
    """Represents a brachytherapy afterloader."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def DoseRateMode(self) -> str:
        """str: The dose rate mode of this treatment unit. Supported modes are "HDR", "PDR", "MDR", and "LDR"."""
        ...

    @property
    def DwellTimeResolution(self) -> float:
        """float: The dwell time resolution supported by this treatment unit in seconds."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def MachineInterface(self) -> str:
        """str: The interface type for communicating with this brachytherapy treatment unit. Possible types are "GammaMed12i", "GammaMedPlus", "VariSource", "Other", and "Omnitron" (obsolete type)."""
        ...

    @property
    def MachineModel(self) -> str:
        """str: The model identifier for this treatment unit. Possible models are "VariSource_5", "VariSource_10", "Remote_Afterloading", "Manual_Loading", "GammaMed12i", and "GammaMedPlus"."""
        ...

    @property
    def MaxDwellTimePerChannel(self) -> float:
        """float: The maximum combined dwell time in a single channel in seconds."""
        ...

    @property
    def MaxDwellTimePerPos(self) -> float:
        """float: The maximum dwell time in a single dwell position in seconds."""
        ...

    @property
    def MaxDwellTimePerTreatment(self) -> float:
        """float: The maximum combined dwell time in all the channels during a single treatment session. The value is in seconds."""
        ...

    @property
    def MaximumChannelLength(self) -> float:
        """float: The maximum channel length supported by this treatment unit in millimeters."""
        ...

    @property
    def MaximumDwellPositionsPerChannel(self) -> int:
        """int: The maximum number of dwell positions per channel supported by this treatment unit."""
        ...

    @property
    def MaximumStepSize(self) -> float:
        """float: The maximum distance between adjacent source positions in millimeters."""
        ...

    @property
    def MinAllowedSourcePos(self) -> float:
        """float: The minimum allowed distance (in millimeters) from the tip of the inner lumen of the applicator to the center of the first dwell position. In other words, no source positions should be placed within this distance from the tip of the inner lumen."""
        ...

    @property
    def MinimumChannelLength(self) -> float:
        """float: The minimum channel length supported by this treatment unit in millimeters."""
        ...

    @property
    def MinimumStepSize(self) -> float:
        """float: The minimum distance between adjacent source positions in millimeters."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def NumberOfChannels(self) -> int:
        """int: The number of channels in this treatment unit."""
        ...

    @property
    def SourceCenterOffsetFromTip(self) -> float:
        """float: The offset distance (in millimeters) from the tip of the applicator to the center of the source at its first possible dwell position. In other words, the offset accounts for half of the active source length and encapsulation."""
        ...

    @property
    def SourceMovementType(self) -> str:
        """str: The source movement type as defined in DICOM. Possible types are "STEPWISE", "FIXED", and "OSCILLATING"."""
        ...

    @property
    def StepSizeResolution(self) -> float:
        """float: The default step size resolution for this treatment unit in millimeters."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetActiveRadioactiveSource(self) -> RadioactiveSource:
        """Returns the active radioactive source of this treatment unit.
        
        Returns:
            RadioactiveSource: A RadioactiveSource object if the treatment unit has a source installed. Otherwise null."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class CalculateBrachy3DDoseResult(SerializableObject):
    """Brachy 3D dose calculation result"""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Errors(self) -> List[str]:
        """List[str]: Error messages if "Success" is false."""
        ...

    @property
    def RoundedDwellTimeAdjustRatio(self) -> float:
        """float: The ratio with which the dwell times were adjusted to meet the resolution of the treatment unit. A value of zero (0.0) means no adjustment to dwell times was made. Value is undefined if "Success" is false"""
        ...

    @property
    def Success(self) -> bool:
        """bool: Was the dose calculation successful?"""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class Calculation:
    """Contains a calculation specific functions"""

    def __init__(self, dvhEstimationModelLibrary: IDVHEstimationModelLibrary) -> None:
        """Initialize instance."""
        ...

    @property
    def AlgorithmsRootPath(self) -> str:
        """str: Algorithms Root Path"""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetCalculationModels(self) -> List[CalculationModel]:
        """Retrieves calculation models"""
        ...

    def GetDvhEstimationModelStructures(self, modelId: str) -> List[DVHEstimationModelStructure]:
        """Method docstring."""
        ...

    def GetDvhEstimationModelSummaries(self) -> List[DVHEstimationModelSummary]:
        """List of DVH Estimation Model summaries."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetInstalledAlgorithms(self) -> List[Algorithm]:
        """Installed Algorithms"""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...


class CalculationModel(ValueType):
    """Calculation Model"""

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

    AlgorithmName: str
    AlgorithmVersion: str
    BeamDataDirectory: str
    DefaultOptionsFilePath: str
    EnabledFlag: bool
    ModelName: str

class CalculationModel(ValueType):
    """Calculation Model"""

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

    AlgorithmName: str
    AlgorithmVersion: str
    BeamDataDirectory: str
    DefaultOptionsFilePath: str
    EnabledFlag: bool
    ModelName: str

class CalculationResult:
    """Holds the result of the calculation (pass/fail)."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Success(self) -> bool:
        """bool: Returns true if calculation did not return any errors. Otherwise returns false."""
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


class Catheter(ApiDataObject):
    """Represents a brachytherapy catheter or an applicator channel centerline. Catheters are associated with a"""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def ApplicatorLength(self) -> float:
        """float: The total length from the tip of the catheter to the treatment unit in millimeters."""
        ...

    @ApplicatorLength.setter
    def ApplicatorLength(self, value: float) -> None:
        """Set property value."""
        ...

    @property
    def BrachyFieldReferencePoints(self) -> List[BrachyFieldReferencePoint]:
        """List[BrachyFieldReferencePoint]: A collection of brachy field reference points."""
        ...

    @property
    def BrachySolidApplicatorPartID(self) -> int:
        """int: The unique identifier of the"""
        ...

    @property
    def ChannelNumber(self) -> int:
        """int: The channel number of this catheter."""
        ...

    @ChannelNumber.setter
    def ChannelNumber(self, value: int) -> None:
        """Set property value."""
        ...

    @property
    def Color(self) -> Color:
        """Color: The color of the catheter in 2D views."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def DeadSpaceLength(self) -> float:
        """float: The total length from the tip of the catheter to the start of the inner lumen in millimeters."""
        ...

    @DeadSpaceLength.setter
    def DeadSpaceLength(self, value: float) -> None:
        """Set property value."""
        ...

    @property
    def FirstSourcePosition(self) -> float:
        """float: The first source position in millimeters in this catheter. This is the source position closest to the tip of the catheter."""
        ...

    @property
    def GroupNumber(self) -> int:
        """int: Catheter Group number."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def LastSourcePosition(self) -> float:
        """float: The last source position in millimeters in this catheter. This is the source position furthest away from the tip of the catheter."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Shape(self) -> Array[VVector]:
        """Array[VVector]: The DICOM coordinates of the applicator shape starting from the tip."""
        ...

    @Shape.setter
    def Shape(self, value: Array[VVector]) -> None:
        """Set property value."""
        ...

    @property
    def SourcePositions(self) -> List[SourcePosition]:
        """List[SourcePosition]: The source positions in the catheter starting from the tip."""
        ...

    @property
    def StepSize(self) -> float:
        """float: The step size of the catheter in millimeters."""
        ...

    @property
    def TreatmentUnit(self) -> BrachyTreatmentUnit:
        """BrachyTreatmentUnit: The brachytherapy treatment unit associated with this catheter."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
        ...

    def GetSourcePosCenterDistanceFromTip(self, sourcePosition: SourcePosition) -> float:
        """Method docstring."""
        ...

    def GetTotalDwellTime(self) -> float:
        """The total dwell time in this catheter in seconds.
        
        Returns:
            float: The total dwell time in this catheter in seconds."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def LinkRefLine(self, refLine: Structure) -> None:
        """Method docstring."""
        ...

    def LinkRefPoint(self, refPoint: ReferencePoint) -> None:
        """Method docstring."""
        ...

    def ReadXml(self, reader: XmlReader) -> None:
        """Method docstring."""
        ...

    def SetId(self, id: str, message: str) -> bool:
        """Method docstring."""
        ...

    def SetSourcePositions(self, stepSize: float, firstSourcePosition: float, lastSourcePosition: float) -> SetSourcePositionsResult:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    def UnlinkRefLine(self, refLine: Structure) -> None:
        """Method docstring."""
        ...

    def UnlinkRefPoint(self, refPoint: ReferencePoint) -> None:
        """Method docstring."""
        ...

    def WriteXml(self, writer: XmlWriter) -> None:
        """Method docstring."""
        ...


class Compensator(ApiDataObject):
    """Represents a beam compensator add-on, a custom-made beam modulating material fixed to a tray, used to modulate the beam's intensity."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Material(self) -> AddOnMaterial:
        """AddOnMaterial: The dosimetric material used in the compensator."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Slot(self) -> Slot:
        """Slot: The slot into which the tray is inserted."""
        ...

    @property
    def Tray(self) -> Tray:
        """Tray: The tray to which the compensator is connected."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class ConsoleEventHandlerDelegate(MulticastDelegate):
    """Class docstring."""

    def __init__(self, object: Any, method: IntPtr) -> None:
        """Initialize instance."""
        ...

    @property
    def Method(self) -> MethodInfo:
        """MethodInfo: Property docstring."""
        ...

    @property
    def Target(self) -> Any:
        """Any: Property docstring."""
        ...

    def BeginInvoke(self, eventCode: ConsoleHandlerEventCode, callback: AsyncCallback, object: Any) -> FileStreamAsyncResult:
        """Method docstring."""
        ...

    def Clone(self) -> Any:
        """Method docstring."""
        ...

    def DynamicInvoke(self, args: Array[Any]) -> Any:
        """Method docstring."""
        ...

    def EndInvoke(self, result: FileStreamAsyncResult) -> bool:
        """Method docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetInvocationList(self) -> Array[Delegate]:
        """Method docstring."""
        ...

    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def Invoke(self, eventCode: ConsoleHandlerEventCode) -> bool:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...


class ConsoleHandlerEventCode:
    """Class docstring."""

    CTRL_BREAK_EVENT: ConsoleHandlerEventCode
    CTRL_CLOSE_EVENT: ConsoleHandlerEventCode
    CTRL_C_EVENT: ConsoleHandlerEventCode
    CTRL_LOGOFF_EVENT: ConsoleHandlerEventCode
    CTRL_SHUTDOWN_EVENT: ConsoleHandlerEventCode

class ConsoleHandlerEventCode:
    """Class docstring."""

    CTRL_BREAK_EVENT: ConsoleHandlerEventCode
    CTRL_CLOSE_EVENT: ConsoleHandlerEventCode
    CTRL_C_EVENT: ConsoleHandlerEventCode
    CTRL_LOGOFF_EVENT: ConsoleHandlerEventCode
    CTRL_SHUTDOWN_EVENT: ConsoleHandlerEventCode

class ControlPoint(SerializableObject):
    """Represents a point in a planned sequence of treatment beam parameters. See the definition of control points in a DICOM RT Beam.
    
    Control points are discussed in DICOM PS 3.3 C.8.8.14. All beams have at least two control points. Note that some values may be NaN if they are not applicable to the treatment plan in question."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Beam(self) -> Beam:
        """Beam: Used for navigating to parent beam"""
        ...

    @property
    def CollimatorAngle(self) -> float:
        """float: The orientation of the IEC BEAM LIMITING DEVICE coordinate system with respect to the IEC GANTRY coordinate system (in degrees)."""
        ...

    @property
    def GantryAngle(self) -> float:
        """float: The gantry angle of the radiation source. In other words, the orientation of the IEC GANTRY coordinate system with respect to the IEC FIXED REFERENCE coordinate system (in degrees)."""
        ...

    @property
    def Index(self) -> int:
        """int: Control point index starting with zero. Even numbers represent start control points, and odd numbers represent stop control points."""
        ...

    @property
    def JawPositions(self) -> VRect[float]:
        """VRect[float]: The positions of the beam collimator jaws (in mm) in the IEC BEAM LIMITING DEVICE coordinates."""
        ...

    @property
    def LeafPositions(self) -> Array[float]:
        """Array[float]: The positions of the beam collimator leaf pairs (in mm) in the IEC BEAMLIMITING DEVICE coordinate axis appropriate to the device type. For example, the X-axis for MLCX and the Y-axis for MLCY. The two-dimensional array is indexed [bank, leaf] where the bank is either 0 or 1. Bank 0 represents the leaf bank to the negative MLC X direction, and bank 1 to the positive MLC X direction. If there is no MLC, a (0,0)-length array is returned."""
        ...

    @property
    def MetersetWeight(self) -> float:
        """float: The cumulative meterset weight to this control point. The cumulative meterset weight for the first item in a control point sequence is zero."""
        ...

    @property
    def PatientSupportAngle(self) -> float:
        """float: The patient support angle. In other words, the orientation of the IEC PATIENT SUPPORT (turntable) coordinate system with respect to the IEC FIXED REFERENCE coordinate system (in degrees)."""
        ...

    @property
    def TableTopLateralPosition(self) -> float:
        """float: Table top lateral position in millimeters, in the IEC TABLE TOP coordinate system."""
        ...

    @property
    def TableTopLongitudinalPosition(self) -> float:
        """float: Table top longitudinal position in millimeters, in the IEC TABLE TOP coordinate system."""
        ...

    @property
    def TableTopVerticalPosition(self) -> float:
        """float: Table top vertical position in millimeters, in the IEC TABLE TOP coordinate system."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class ControlPointCollection(SerializableObject):
    """Represents a collection of machine parameters that describe the planned treatment beam."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Count(self) -> int:
        """int: The number of control points in the collection."""
        ...

    @property
    def Item(self) -> ControlPoint:
        """ControlPoint: Property docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetEnumerator(self) -> IEnumerator[ControlPoint]:
        """Retrieves enumerator for ControlPoints in the collection.
        
        Returns:
            IEnumerator[ControlPoint]: Enumerator for ControlPoints in the collection."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class ControlPointParameters:
    """An editable copy of the parameters of a control point.
    
    To apply the parameters, call the ApplyParameters method of the Beam class. Because the parameters are simple copies, they do not reflect the current state of the data model."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def CollimatorAngle(self) -> float:
        """float: A copy of the collimator angle at this control point, in degrees, in the range [0, 360[. It is defined as the orientation of the IEC BEAM LIMITING DEVICE coordinate system with respect to the IEC GANTRY coordinate system (in degrees)."""
        ...

    @property
    def GantryAngle(self) -> float:
        """float: A copy of the gantry angle at this control point, in degrees, in the range [0, 360[. It is defined as the orientation of the IEC GANTRY coordinate system with respect to the IEC FIXED REFERENCE coordinate system (in degrees)."""
        ...

    @GantryAngle.setter
    def GantryAngle(self, value: float) -> None:
        """Set property value."""
        ...

    @property
    def Index(self) -> int:
        """int: Control point index starting with zero. Even numbers represent start control points, and odd numbers represent stop control points."""
        ...

    @property
    def JawPositions(self) -> VRect[float]:
        """VRect[float]: A copy of the jaw positions of the treatment beams at this control point in millimeters, and in IEC BEAM LIMITING DEVICE coordinates."""
        ...

    @JawPositions.setter
    def JawPositions(self, value: VRect[float]) -> None:
        """Set property value."""
        ...

    @property
    def LeafPositions(self) -> Array[float]:
        """Array[float]: A copy of the positions of the MLC leaf pairs (in millimeters) in the IEC BEAMLIMITING DEVICE coordinate axis appropriate to the MLC device type: the X-axis for MLCX and the Y-axis for MLCY. The two-dimensional array is indexed [bank, leaf], where the bank is either 0 or 1. Bank 0 represents the leaf bank to the negative MLC X direction, and bank 1 to the positive MLC X direction. If no MLC exists, a (0,0)-length array is returned."""
        ...

    @LeafPositions.setter
    def LeafPositions(self, value: Array[float]) -> None:
        """Set property value."""
        ...

    @property
    def MetersetWeight(self) -> float:
        """float: A copy of the cumulative meterset weight to this control point."""
        ...

    @MetersetWeight.setter
    def MetersetWeight(self, value: float) -> None:
        """Set property value."""
        ...

    @property
    def PatientSupportAngle(self) -> float:
        """float: A copy of the patient support angle at this control point, in degrees, in the range [0, 360[. It is defined as the orientation of the IEC PATIENT SUPPORT (turntable) coordinate system with respect to the IEC FIXED REFERENCE coordinate system (in degrees)."""
        ...

    @property
    def TableTopLateralPosition(self) -> float:
        """float: Table top lateral position in millimeters, in the IEC TABLE TOP coordinate system."""
        ...

    @property
    def TableTopLongitudinalPosition(self) -> float:
        """float: Table top longitudinal position in millimeters, in the IEC TABLE TOP coordinate system."""
        ...

    @property
    def TableTopVerticalPosition(self) -> float:
        """float: Table top vertical position in millimeters, in the IEC TABLE TOP coordinate system."""
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


class Course(ApiDataObject):
    """A course represents the course of treatment that a patient will be given. Every patient must have a course, and all plans always belong to a course."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def BrachyPlanSetups(self) -> List[BrachyPlanSetup]:
        """List[BrachyPlanSetup]: A collection of brachytherapy plans for the course."""
        ...

    @property
    def ClinicalStatus(self) -> CourseClinicalStatus:
        """CourseClinicalStatus: Clinical Status of Course."""
        ...

    @property
    def Comment(self) -> str:
        """str: [Availability of this property depends on your Eclipse Scripting API license] A comment about the Course."""
        ...

    @Comment.setter
    def Comment(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def CompletedDateTime(self) -> Optional[datetime]:
        """Optional[datetime]: The date and time when the course was completed."""
        ...

    @property
    def Diagnoses(self) -> List[Diagnosis]:
        """List[Diagnosis]: The diagnoses that are attached to the course."""
        ...

    @property
    def ExternalPlanSetups(self) -> List[ExternalPlanSetup]:
        """List[ExternalPlanSetup]: A collection of external beam plans for the course."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: [Availability of this property depends on your Eclipse Scripting API license] The identifier of the Course."""
        ...

    @Id.setter
    def Id(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def Intent(self) -> str:
        """str: The intent of the course."""
        ...

    @property
    def IonPlanSetups(self) -> List[IonPlanSetup]:
        """List[IonPlanSetup]: A collection of proton plans for the course."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Patient(self) -> Patient:
        """Patient: Patient in which the course is defined."""
        ...

    @property
    def PlanSetups(self) -> List[PlanSetup]:
        """List[PlanSetup]: A collection of plans for the course. The plans can be of any type (external beam or brachytherapy)."""
        ...

    @property
    def PlanSums(self) -> List[PlanSum]:
        """List[PlanSum]: A collection of plan sums for the course."""
        ...

    @property
    def StartDateTime(self) -> Optional[datetime]:
        """Optional[datetime]: The date and time when the course was started."""
        ...

    @property
    def TreatmentPhases(self) -> List[TreatmentPhase]:
        """List[TreatmentPhase]: All treatment phases in the course."""
        ...

    @property
    def TreatmentSessions(self) -> List[TreatmentSession]:
        """List[TreatmentSession]: Treatment sessions of the course."""
        ...

    def AddBrachyPlanSetup(self, structureSet: StructureSet, targetStructure: Structure, primaryReferencePoint: ReferencePoint, dosePerFraction: DoseValue, brachyTreatmentTechnique: BrachyTreatmentTechniqueType, additionalReferencePoints: List[ReferencePoint]) -> BrachyPlanSetup:
        """Method docstring."""
        ...

    @overload
    def AddBrachyPlanSetup(self, structureSet: StructureSet, dosePerFraction: DoseValue, brachyTreatmentTechnique: BrachyTreatmentTechniqueType) -> BrachyPlanSetup:
        """Method docstring."""
        ...

    def AddExternalPlanSetup(self, structureSet: StructureSet, targetStructure: Structure, primaryReferencePoint: ReferencePoint, additionalReferencePoints: List[ReferencePoint]) -> ExternalPlanSetup:
        """Method docstring."""
        ...

    @overload
    def AddExternalPlanSetup(self, structureSet: StructureSet) -> ExternalPlanSetup:
        """Method docstring."""
        ...

    def AddExternalPlanSetupAsVerificationPlan(self, structureSet: StructureSet, verifiedPlan: ExternalPlanSetup) -> ExternalPlanSetup:
        """Method docstring."""
        ...

    def AddIonPlanSetup(self, structureSet: StructureSet, targetStructure: Structure, primaryReferencePoint: ReferencePoint, patientSupportDeviceId: str, additionalReferencePoints: List[ReferencePoint]) -> IonPlanSetup:
        """Method docstring."""
        ...

    @overload
    def AddIonPlanSetup(self, structureSet: StructureSet, patientSupportDeviceId: str) -> IonPlanSetup:
        """Method docstring."""
        ...

    def AddIonPlanSetupAsVerificationPlan(self, structureSet: StructureSet, patientSupportDeviceId: str, verifiedPlan: IonPlanSetup) -> IonPlanSetup:
        """Method docstring."""
        ...

    def CanAddPlanSetup(self, structureSet: StructureSet) -> bool:
        """Method docstring."""
        ...

    def CanRemovePlanSetup(self, planSetup: PlanSetup) -> bool:
        """Method docstring."""
        ...

    def CopyBrachyPlanSetup(self, sourcePlan: BrachyPlanSetup, outputDiagnostics: StringBuilder) -> BrachyPlanSetup:
        """Method docstring."""
        ...

    @overload
    def CopyBrachyPlanSetup(self, sourcePlan: BrachyPlanSetup, structureset: StructureSet, outputDiagnostics: StringBuilder) -> BrachyPlanSetup:
        """Method docstring."""
        ...

    def CopyPlanSetup(self, sourcePlan: PlanSetup) -> PlanSetup:
        """Method docstring."""
        ...

    @overload
    def CopyPlanSetup(self, sourcePlan: PlanSetup, targetImage: Image, outputDiagnostics: StringBuilder) -> PlanSetup:
        """Method docstring."""
        ...

    @overload
    def CopyPlanSetup(self, sourcePlan: PlanSetup, targetImage: Image, registration: Registration, outputDiagnostics: StringBuilder) -> PlanSetup:
        """Method docstring."""
        ...

    @overload
    def CopyPlanSetup(self, sourcePlan: PlanSetup, structureset: StructureSet, outputDiagnostics: StringBuilder) -> PlanSetup:
        """Method docstring."""
        ...

    def CreatePlanSum(self, planningItems: List[PlanningItem], image: Image) -> PlanSum:
        """Method docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def IsCompleted(self) -> bool:
        """Checks if the clinical status of the course is completed or restored.
        
        Returns:
            bool: true if the clinical status of the course is completed or restored."""
        ...

    def ReadXml(self, reader: XmlReader) -> None:
        """Method docstring."""
        ...

    def RemovePlanSetup(self, planSetup: PlanSetup) -> None:
        """Method docstring."""
        ...

    def RemovePlanSum(self, planSum: PlanSum) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    def WriteXml(self, writer: XmlWriter) -> None:
        """Method docstring."""
        ...


class CustomScriptExecutable:
    """A factory class for creating an application object for a custom script executable."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @staticmethod
    def CreateApplication(scriptName: str) -> Application:
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


class DVHData(SerializableObject):
    """Represents Dose Volume Histogram (DVH) data."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Coverage(self) -> float:
        """float: The dose coverage of the target, normalized to 0.0 .. 1.0."""
        ...

    @property
    def CurveData(self) -> Array[DVHPoint]:
        """Array[DVHPoint]: The points of the Dose Volume Histogram (DVH) curve."""
        ...

    @property
    def MaxDose(self) -> DoseValue:
        """DoseValue: The maximum dose."""
        ...

    @property
    def MaxDosePosition(self) -> VVector:
        """VVector: The position of the maximum dose."""
        ...

    @property
    def MeanDose(self) -> DoseValue:
        """DoseValue: The mean dose."""
        ...

    @property
    def MedianDose(self) -> DoseValue:
        """DoseValue: The median dose."""
        ...

    @property
    def MinDose(self) -> DoseValue:
        """DoseValue: The minimum dose."""
        ...

    @property
    def MinDosePosition(self) -> VVector:
        """VVector: The position of the minimum dose."""
        ...

    @property
    def SamplingCoverage(self) -> float:
        """float: The sampling coverage."""
        ...

    @property
    def StdDev(self) -> float:
        """float: The standard deviation."""
        ...

    @property
    def Volume(self) -> float:
        """float: The volume of the structure in cubic centimeters."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class DVHEstimationModelStructure(SerializableObject):
    """Structure of a DVH estimation model in Planning Model Library"""

    def __init__(self, impl: DVHEstimationModelStructure) -> None:
        """Initialize instance."""
        ...

    @property
    def Id(self) -> str:
        """str: Id of the structure"""
        ...

    @property
    def IsValid(self) -> bool:
        """bool: Is Valid"""
        ...

    @property
    def ModelStructureGuid(self) -> str:
        """str: Model Id"""
        ...

    @property
    def StructureCodes(self) -> List[StructureCode]:
        """List[StructureCode]: List of structure codes associated with the structure"""
        ...

    @property
    def StructureType(self) -> DVHEstimationStructureType:
        """DVHEstimationStructureType: Structure type: PTV or OAR"""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class DVHEstimationModelSummary(SerializableObject):
    """A summary of an DVH Estimation Model. Contains the needed information for selecting a model."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Description(self) -> str:
        """str: Model Description"""
        ...

    @property
    def IsPublished(self) -> bool:
        """bool: True if set to published state. Only published models are available for optimizing."""
        ...

    @property
    def IsTrained(self) -> bool:
        """bool: True if the model contains data."""
        ...

    @property
    def ModelDataVersion(self) -> str:
        """str: Version"""
        ...

    @property
    def ModelParticleType(self) -> ParticleType:
        """ParticleType: Returns particle type for the model. Either ParticleType.Proton or ParticleType.Photon."""
        ...

    @property
    def ModelUID(self) -> str:
        """str: Model UID. To be used for the Load command."""
        ...

    @property
    def Name(self) -> str:
        """str: Display Name"""
        ...

    @property
    def Revision(self) -> int:
        """int: Publish revision of the model"""
        ...

    @property
    def TreatmentSite(self) -> str:
        """str: Indicating the treatment site the model was created for"""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class DefaultApplicationContext:
    """Class docstring."""

    def __init__(self, appName: str, taskName: str, versionString: str) -> None:
        """Initialize instance."""
        ...

    @property
    def ApprovesWorkflowSupportedPlans(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def AutomaticFieldOrdering(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def CanEditBrachyPlans(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def EditsTreatmentMachines(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def LoadsPatientsWithoutOpening(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def RequireConeInEachField(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def WantsToCalculateOnTheFly(self) -> bool:
        """bool: Property docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetAppEdition(self) -> str:
        """Method docstring."""
        ...

    def GetAppName(self) -> str:
        """Method docstring."""
        ...

    def GetAppVersion(self) -> str:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetTaskEdition(self) -> str:
        """Method docstring."""
        ...

    def GetTaskName(self) -> str:
        """Method docstring."""
        ...

    def GetTaskVersion(self) -> str:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def GetWorkspaceName(self) -> str:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...


class Diagnosis(ApiDataObject):
    """Represents a diagnosis of the patient."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def ClinicalDescription(self) -> str:
        """str: User-defined clinical description of the diagnosis."""
        ...

    @property
    def Code(self) -> str:
        """str: The disease code from the specified code table."""
        ...

    @property
    def CodeTable(self) -> str:
        """str: Identifies the coding system table, for example, ICD-9-CM."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class Dose(ApiDataObject):
    """Represents a 3D dose grid."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def DoseMax3D(self) -> DoseValue:
        """DoseValue: The maximum dose."""
        ...

    @property
    def DoseMax3DLocation(self) -> VVector:
        """VVector: The location of the maximum dose."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Isodoses(self) -> List[Isodose]:
        """List[Isodose]: A collection of isodoses."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Origin(self) -> VVector:
        """VVector: The origin of the dose matrix. In other words, the DICOM coordinates of the center point of the upper-left hand corner voxel of the first dose plane."""
        ...

    @property
    def Series(self) -> Series:
        """Series: Returns the series that contains the dose, or null if the dose is not connected to a series."""
        ...

    @property
    def SeriesUID(self) -> str:
        """str: Returns the DICOM UID of the series that contains the dose, or an empty string if the dose is not connected to a series."""
        ...

    @property
    def UID(self) -> str:
        """str: The DICOM UID of the dose."""
        ...

    @property
    def XDirection(self) -> VVector:
        """VVector: The direction of the x-axis in the dose matrix."""
        ...

    @property
    def XRes(self) -> float:
        """float: The dose matrix resolution in X-direction in millimeters."""
        ...

    @property
    def XSize(self) -> int:
        """int: The dose matrix size in X-direction in voxels."""
        ...

    @property
    def YDirection(self) -> VVector:
        """VVector: The direction of the y-axis in the dose matrix."""
        ...

    @property
    def YRes(self) -> float:
        """float: The dose matrix resolution in Y-direction in millimeters."""
        ...

    @property
    def YSize(self) -> int:
        """int: The dose matrix size in Y-direction in voxels."""
        ...

    @property
    def ZDirection(self) -> VVector:
        """VVector: The direction of the z-axis in the dose matrix."""
        ...

    @property
    def ZRes(self) -> float:
        """float: The dose matrix resolution in Z-direction in millimeters."""
        ...

    @property
    def ZSize(self) -> int:
        """int: The dose matrix size in Z-direction in voxels."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetDoseProfile(self, start: VVector, stop: VVector, preallocatedBuffer: Array[float]) -> DoseProfile:
        """Method docstring."""
        ...

    def GetDoseToPoint(self, at: VVector) -> DoseValue:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def GetVoxels(self, planeIndex: int, preallocatedBuffer: Array[int]) -> None:
        """Method docstring."""
        ...

    def ReadXml(self, reader: XmlReader) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    def VoxelToDoseValue(self, voxelValue: int) -> DoseValue:
        """Method docstring."""
        ...

    def WriteXml(self, writer: XmlWriter) -> None:
        """Method docstring."""
        ...


class DynamicWedge(Wedge):
    """A Dynamic Wedge is formed by a moving jaw of a standard collimator during irradiation."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def CreationDateTime(self) -> Optional[datetime]:
        """Optional[datetime]: Property docstring."""
        ...

    @property
    def Direction(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def WedgeAngle(self) -> float:
        """float: Property docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class ESAPIActionPackAttribute(Attribute):
    """Specifies the assembly as an Eclipse visual scripting action pack. Action packs are ESAPI scripts that are used by visual scripts."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def IsWriteable(self) -> bool:
        """bool: Returns true if the action pack can modify patient data."""
        ...

    @IsWriteable.setter
    def IsWriteable(self, value: bool) -> None:
        """Set property value."""
        ...

    @property
    def TypeId(self) -> Any:
        """Any: Property docstring."""
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

    def IsDefaultAttribute(self) -> bool:
        """Method docstring."""
        ...

    def Match(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...


class ESAPIScriptAttribute(Attribute):
    """Specifies the assembly as an Eclipse Scripting API (ESAPI) script."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def IsWriteable(self) -> bool:
        """bool: Returns true if the script can modify patient data."""
        ...

    @IsWriteable.setter
    def IsWriteable(self, value: bool) -> None:
        """Set property value."""
        ...

    @property
    def TypeId(self) -> Any:
        """Any: Property docstring."""
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

    def IsDefaultAttribute(self) -> bool:
        """Method docstring."""
        ...

    def Match(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...


class EnergyMode(ApiDataObject):
    """Represents an energy mode."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def IsElectron(self) -> bool:
        """bool: Checks if the mode is electron."""
        ...

    @property
    def IsPhoton(self) -> bool:
        """bool: Checks if the mode is photon."""
        ...

    @property
    def IsProton(self) -> bool:
        """bool: Checks if the mode is proton."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class EnhancedDynamicWedge(DynamicWedge):
    """An Enhanced Dynamic Wedge is similar to a Dynamic Wedge, but it features more wedge angles than a simple Dynamic Wedge."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def CreationDateTime(self) -> Optional[datetime]:
        """Optional[datetime]: Property docstring."""
        ...

    @property
    def Direction(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def WedgeAngle(self) -> float:
        """float: Property docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class Equipment:
    """Provides access to clinical devices and accessories."""

    def __init__(self, admin: IAdmin) -> None:
        """Initialize instance."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetBrachyTreatmentUnits(self) -> List[BrachyTreatmentUnit]:
        """Returns the available brachy treatment units. Excludes virtual and deleted ones.
        
        Returns:
            List[BrachyTreatmentUnit]: The available brachy treatment units."""
        ...

    def GetExternalBeamTreatmentUnits(self) -> List[ExternalBeamTreatmentUnit]:
        """Returns the available External Beam treatment units. Excludes virtual and deleted ones.
        
        Returns:
            List[ExternalBeamTreatmentUnit]: The available brachy treatment units."""
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


class EstimatedDVH(ApiDataObject):
    """Represents an estimated Dose Volume Histogram (DVH) curve."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def CurveData(self) -> Array[DVHPoint]:
        """Array[DVHPoint]: The points of the estimated DVH curve."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def PlanSetup(self) -> PlanSetup:
        """PlanSetup: Parent plan."""
        ...

    @property
    def PlanSetupId(self) -> str:
        """str: ID of the parent plan."""
        ...

    @property
    def Structure(self) -> Structure:
        """Structure: Parent structure."""
        ...

    @property
    def StructureId(self) -> str:
        """str: ID of the parent structure."""
        ...

    @property
    def TargetDoseLevel(self) -> DoseValue:
        """DoseValue: Dose level of the associated target structure."""
        ...

    @property
    def Type(self) -> DVHEstimateType:
        """DVHEstimateType: Type of DVH estimate curve."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class EvaluationDose(Dose):
    """Represents an evaluation dose that is connected to a plan that has no beams."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def DoseMax3D(self) -> DoseValue:
        """DoseValue: Property docstring."""
        ...

    @property
    def DoseMax3DLocation(self) -> VVector:
        """VVector: Property docstring."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Isodoses(self) -> List[Isodose]:
        """List[Isodose]: Property docstring."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Origin(self) -> VVector:
        """VVector: Property docstring."""
        ...

    @property
    def Series(self) -> Series:
        """Series: Property docstring."""
        ...

    @property
    def SeriesUID(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def UID(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def XDirection(self) -> VVector:
        """VVector: Property docstring."""
        ...

    @property
    def XRes(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def XSize(self) -> int:
        """int: Property docstring."""
        ...

    @property
    def YDirection(self) -> VVector:
        """VVector: Property docstring."""
        ...

    @property
    def YRes(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def YSize(self) -> int:
        """int: Property docstring."""
        ...

    @property
    def ZDirection(self) -> VVector:
        """VVector: Property docstring."""
        ...

    @property
    def ZRes(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def ZSize(self) -> int:
        """int: Property docstring."""
        ...

    def DoseValueToVoxel(self, doseValue: DoseValue) -> int:
        """Method docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetDoseProfile(self, start: VVector, stop: VVector, preallocatedBuffer: Array[float]) -> DoseProfile:
        """Method docstring."""
        ...

    def GetDoseToPoint(self, at: VVector) -> DoseValue:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def GetVoxels(self, planeIndex: int, preallocatedBuffer: Array[int]) -> None:
        """Method docstring."""
        ...

    def ReadXml(self, reader: XmlReader) -> None:
        """Method docstring."""
        ...

    def SetVoxels(self, planeIndex: int, values: Array[int]) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    def VoxelToDoseValue(self, voxelValue: int) -> DoseValue:
        """Method docstring."""
        ...

    def WriteXml(self, writer: XmlWriter) -> None:
        """Method docstring."""
        ...


class ExternalBeamTreatmentUnit(ApiDataObject):
    """Represents a treatment machine used for delivering external beam radiotherapy."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def MachineDepartmentName(self) -> str:
        """str: Default department associated with the machine."""
        ...

    @property
    def MachineModel(self) -> str:
        """str: The model of the treatment unit."""
        ...

    @property
    def MachineModelName(self) -> str:
        """str: The displayed name of the treatment unit model."""
        ...

    @property
    def MachineScaleDisplayName(self) -> str:
        """str: The name of the scale used in the treatment unit."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def OperatingLimits(self) -> TreatmentUnitOperatingLimits:
        """TreatmentUnitOperatingLimits: Information about operating limits for a set of treatment unit parameters."""
        ...

    @property
    def SourceAxisDistance(self) -> float:
        """float: The Source to Axis Distance (SAD)."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class ExternalPlanSetup(PlanSetup):
    """Represents an external beam plan. For more information, see the definition of the DICOM RT Plan."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def ApplicationScriptLogs(self) -> List[ApplicationScriptLog]:
        """List[ApplicationScriptLog]: Property docstring."""
        ...

    @property
    def ApprovalHistory(self) -> List[ApprovalHistoryEntry]:
        """List[ApprovalHistoryEntry]: Property docstring."""
        ...

    @property
    def ApprovalStatus(self) -> PlanSetupApprovalStatus:
        """PlanSetupApprovalStatus: Property docstring."""
        ...

    @property
    def ApprovalStatusAsString(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def BaseDosePlanningItem(self) -> PlanningItem:
        """PlanningItem: Property docstring."""
        ...

    @BaseDosePlanningItem.setter
    def BaseDosePlanningItem(self, value: PlanningItem) -> None:
        """Set property value."""
        ...

    @property
    def Beams(self) -> List[Beam]:
        """List[Beam]: Property docstring."""
        ...

    @property
    def BeamsInTreatmentOrder(self) -> List[Beam]:
        """List[Beam]: Property docstring."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @Comment.setter
    def Comment(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def Course(self) -> Course:
        """Course: Property docstring."""
        ...

    @property
    def CreationDateTime(self) -> Optional[datetime]:
        """Optional[datetime]: Property docstring."""
        ...

    @property
    def CreationUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def DVHEstimates(self) -> List[EstimatedDVH]:
        """List[EstimatedDVH]: Property docstring."""
        ...

    @property
    def Dose(self) -> PlanningItemDose:
        """PlanningItemDose: Property docstring."""
        ...

    @property
    def DoseAsEvaluationDose(self) -> EvaluationDose:
        """EvaluationDose: The evaluation dose is connected to the plan and contains voxels that are set by"""
        ...

    @property
    def DosePerFraction(self) -> DoseValue:
        """DoseValue: Property docstring."""
        ...

    @property
    def DosePerFractionInPrimaryRefPoint(self) -> DoseValue:
        """DoseValue: Property docstring."""
        ...

    @property
    def DoseValuePresentation(self) -> DoseValuePresentation:
        """DoseValuePresentation: Property docstring."""
        ...

    @DoseValuePresentation.setter
    def DoseValuePresentation(self, value: DoseValuePresentation) -> None:
        """Set property value."""
        ...

    @property
    def ElectronCalculationModel(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def ElectronCalculationOptions(self) -> Dict[str, str]:
        """Dict[str, str]: Property docstring."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
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
    def IntegrityHash(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def IsDoseValid(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsTreated(self) -> bool:
        """bool: Property docstring."""
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
    def NumberOfFractions(self) -> Optional[int]:
        """Optional[int]: Property docstring."""
        ...

    @property
    def OptimizationSetup(self) -> OptimizationSetup:
        """OptimizationSetup: Property docstring."""
        ...

    @property
    def PatientSupportDevice(self) -> PatientSupportDevice:
        """PatientSupportDevice: Property docstring."""
        ...

    @property
    def PhotonCalculationModel(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def PhotonCalculationOptions(self) -> Dict[str, str]:
        """Dict[str, str]: Property docstring."""
        ...

    @property
    def PlanIntent(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def PlanIsInTreatment(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def PlanNormalizationMethod(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def PlanNormalizationPoint(self) -> VVector:
        """VVector: Property docstring."""
        ...

    @property
    def PlanNormalizationValue(self) -> float:
        """float: Property docstring."""
        ...

    @PlanNormalizationValue.setter
    def PlanNormalizationValue(self, value: float) -> None:
        """Set property value."""
        ...

    @property
    def PlanObjectiveStructures(self) -> List[str]:
        """List[str]: Property docstring."""
        ...

    @property
    def PlanType(self) -> PlanType:
        """PlanType: Property docstring."""
        ...

    @property
    def PlanUncertainties(self) -> List[PlanUncertainty]:
        """List[PlanUncertainty]: Property docstring."""
        ...

    @property
    def PlannedDosePerFraction(self) -> DoseValue:
        """DoseValue: Property docstring."""
        ...

    @property
    def PlanningApprovalDate(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def PlanningApprover(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def PlanningApproverDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def PredecessorPlan(self) -> PlanSetup:
        """PlanSetup: Property docstring."""
        ...

    @property
    def PredecessorPlanUID(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def PrescribedDosePerFraction(self) -> DoseValue:
        """DoseValue: Property docstring."""
        ...

    @property
    def PrescribedPercentage(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def PrimaryReferencePoint(self) -> ReferencePoint:
        """ReferencePoint: Property docstring."""
        ...

    @property
    def ProtocolID(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def ProtocolPhaseID(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def ProtonCalculationModel(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def ProtonCalculationOptions(self) -> Dict[str, str]:
        """Dict[str, str]: Property docstring."""
        ...

    @property
    def RTPrescription(self) -> RTPrescription:
        """RTPrescription: Property docstring."""
        ...

    @property
    def ReferencePoints(self) -> List[ReferencePoint]:
        """List[ReferencePoint]: Property docstring."""
        ...

    @property
    def Series(self) -> Series:
        """Series: Property docstring."""
        ...

    @property
    def SeriesUID(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def StructureSet(self) -> StructureSet:
        """StructureSet: Property docstring."""
        ...

    @property
    def StructuresSelectedForDvh(self) -> List[Structure]:
        """List[Structure]: Property docstring."""
        ...

    @property
    def TargetVolumeID(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def TotalDose(self) -> DoseValue:
        """DoseValue: Property docstring."""
        ...

    @property
    def TotalPrescribedDose(self) -> DoseValue:
        """DoseValue: Property docstring."""
        ...

    @property
    def TradeoffExplorationContext(self) -> TradeoffExplorationContext:
        """TradeoffExplorationContext: [Availability of this property depends on your Eclipse Scripting API license] Gets the"""
        ...

    @property
    def TreatmentApprovalDate(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def TreatmentApprover(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def TreatmentApproverDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def TreatmentOrientation(self) -> PatientOrientation:
        """PatientOrientation: Property docstring."""
        ...

    @property
    def TreatmentOrientationAsString(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def TreatmentPercentage(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def TreatmentSessions(self) -> List[PlanTreatmentSession]:
        """List[PlanTreatmentSession]: Property docstring."""
        ...

    @property
    def UID(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def UseGating(self) -> bool:
        """bool: Property docstring."""
        ...

    @UseGating.setter
    def UseGating(self, value: bool) -> None:
        """Set property value."""
        ...

    @property
    def VerifiedPlan(self) -> PlanSetup:
        """PlanSetup: Property docstring."""
        ...

    def AddArcBeam(self, machineParameters: ExternalBeamMachineParameters, jawPositions: VRect[float], collimatorAngle: float, gantryAngle: float, gantryStop: float, gantryDirection: GantryDirection, patientSupportAngle: float, isocenter: VVector) -> Beam:
        """Method docstring."""
        ...

    def AddConformalArcBeam(self, machineParameters: ExternalBeamMachineParameters, collimatorAngle: float, controlPointCount: int, gantryAngle: float, gantryStop: float, gantryDirection: GantryDirection, patientSupportAngle: float, isocenter: VVector) -> Beam:
        """Method docstring."""
        ...

    def AddFixedSequenceBeam(self, machineParameters: ExternalBeamMachineParameters, collimatorAngle: float, gantryAngle: float, isocenter: VVector) -> Beam:
        """Method docstring."""
        ...

    def AddImagingSetup(self, machineParameters: ExternalBeamMachineParameters, setupParameters: ImagingBeamSetupParameters, targetStructure: Structure) -> bool:
        """Method docstring."""
        ...

    def AddMLCArcBeam(self, machineParameters: ExternalBeamMachineParameters, leafPositions: Array[float], jawPositions: VRect[float], collimatorAngle: float, gantryAngle: float, gantryStop: float, gantryDirection: GantryDirection, patientSupportAngle: float, isocenter: VVector) -> Beam:
        """Method docstring."""
        ...

    def AddMLCBeam(self, machineParameters: ExternalBeamMachineParameters, leafPositions: Array[float], jawPositions: VRect[float], collimatorAngle: float, gantryAngle: float, patientSupportAngle: float, isocenter: VVector) -> Beam:
        """Method docstring."""
        ...

    def AddMLCSetupBeam(self, machineParameters: ExternalBeamMachineParameters, leafPositions: Array[float], jawPositions: VRect[float], collimatorAngle: float, gantryAngle: float, patientSupportAngle: float, isocenter: VVector) -> Beam:
        """Method docstring."""
        ...

    def AddMultipleStaticSegmentBeam(self, machineParameters: ExternalBeamMachineParameters, metersetWeights: List[float], collimatorAngle: float, gantryAngle: float, patientSupportAngle: float, isocenter: VVector) -> Beam:
        """Method docstring."""
        ...

    def AddPlanUncertaintyWithParameters(self, uncertaintyType: PlanUncertaintyType, planSpecificUncertainty: bool, HUConversionError: float, isocenterShift: VVector) -> PlanUncertainty:
        """Method docstring."""
        ...

    def AddReferencePoint(self, target: bool, location: Optional[VVector], id: str) -> ReferencePoint:
        """Method docstring."""
        ...

    @overload
    def AddReferencePoint(self, refPoint: ReferencePoint) -> None:
        """Method docstring."""
        ...

    def AddSetupBeam(self, machineParameters: ExternalBeamMachineParameters, jawPositions: VRect[float], collimatorAngle: float, gantryAngle: float, patientSupportAngle: float, isocenter: VVector) -> Beam:
        """Method docstring."""
        ...

    def AddSlidingWindowBeam(self, machineParameters: ExternalBeamMachineParameters, metersetWeights: List[float], collimatorAngle: float, gantryAngle: float, patientSupportAngle: float, isocenter: VVector) -> Beam:
        """Method docstring."""
        ...

    def AddSlidingWindowBeamForFixedJaws(self, machineParameters: ExternalBeamMachineParameters, metersetWeights: List[float], collimatorAngle: float, gantryAngle: float, patientSupportAngle: float, isocenter: VVector) -> Beam:
        """Method docstring."""
        ...

    def AddStaticBeam(self, machineParameters: ExternalBeamMachineParameters, jawPositions: VRect[float], collimatorAngle: float, gantryAngle: float, patientSupportAngle: float, isocenter: VVector) -> Beam:
        """Method docstring."""
        ...

    def AddVMATBeam(self, machineParameters: ExternalBeamMachineParameters, metersetWeights: List[float], collimatorAngle: float, gantryAngle: float, gantryStop: float, gantryDirection: GantryDirection, patientSupportAngle: float, isocenter: VVector) -> Beam:
        """Method docstring."""
        ...

    def AddVMATBeamForFixedJaws(self, machineParameters: ExternalBeamMachineParameters, metersetWeights: List[float], collimatorAngle: float, gantryStartAngle: float, gantryStopAngle: float, gantryDir: GantryDirection, patientSupportAngle: float, isocenter: VVector) -> Beam:
        """Method docstring."""
        ...

    def CalculateDVHEstimates(self, modelId: str, targetDoseLevels: Dict[str, DoseValue], structureMatches: Dict[str, str]) -> CalculationResult:
        """Method docstring."""
        ...

    def CalculateDose(self) -> CalculationResult:
        """[Availability of this method depends on your Eclipse Scripting API license] Calculates the dose for the plan.
        
        Returns:
            CalculationResult: The calculation result. See calculation details from"""
        ...

    def CalculateDoseWithPresetValues(self, presetValues: List[KeyValuePair[str, MetersetValue]]) -> CalculationResult:
        """Method docstring."""
        ...

    def CalculateLeafMotions(self) -> CalculationResult:
        """[Availability of this method depends on your Eclipse Scripting API license] Calculates leaf motions using the calculation options of the plan setup. Before calling this method, set the calculation models for leaf motions and dose calculation.
        
        Returns:
            CalculationResult: The calculation result. See calculation details from"""
        ...

    @overload
    def CalculateLeafMotions(self, options: LMCVOptions) -> CalculationResult:
        """[Availability of this method depends on your Eclipse Scripting API license] Calculates leaf motions using the calculation options of the plan setup. Before calling this method, set the calculation models for leaf motions and dose calculation.
        
        Returns:
            CalculationResult: The calculation result. See calculation details from"""
        ...

    @overload
    def CalculateLeafMotions(self, options: SmartLMCOptions) -> CalculationResult:
        """[Availability of this method depends on your Eclipse Scripting API license] Calculates leaf motions using the calculation options of the plan setup. Before calling this method, set the calculation models for leaf motions and dose calculation.
        
        Returns:
            CalculationResult: The calculation result. See calculation details from"""
        ...

    @overload
    def CalculateLeafMotions(self, options: LMCMSSOptions) -> CalculationResult:
        """[Availability of this method depends on your Eclipse Scripting API license] Calculates leaf motions using the calculation options of the plan setup. Before calling this method, set the calculation models for leaf motions and dose calculation.
        
        Returns:
            CalculationResult: The calculation result. See calculation details from"""
        ...

    def CalculateLeafMotionsAndDose(self) -> CalculationResult:
        """Calculate leaf motions and dose using the calculation models defined in the plan setup.
        
        Returns:
            CalculationResult: Result of the intermediate dose calculation."""
        ...

    def CalculatePlanUncertaintyDoses(self) -> CalculationResult:
        """[Availability of this method depends on your Eclipse Scripting API license] Calculates the plan uncertainty dose for the photon plan.
        
        Returns:
            CalculationResult: The calculation result. See calculation details in"""
        ...

    def ClearCalculationModel(self, calculationType: CalculationType) -> None:
        """Method docstring."""
        ...

    def CopyEvaluationDose(self, existing: Dose) -> EvaluationDose:
        """Method docstring."""
        ...

    def CreateEvaluationDose(self) -> EvaluationDose:
        """[Availability of this method depends on your Eclipse Scripting API license] Creates an evaluation dose for the plan. The voxels in an evaluation dose can be set using the Eclipse Scripting API instead of a dose calculation algorithm. To create an evaluation dose, the plan must not contain any beams. To set the evaluation dose voxels, retrieve the dose matrix using the
        
        Saving modifications to the database is not possible if the evaluation dose has been created but voxels have not been set.
        
        Returns:
            EvaluationDose: A new evaluation dose object."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetCalculationModel(self, calculationType: CalculationType) -> str:
        """Method docstring."""
        ...

    def GetCalculationOption(self, calculationModel: str, optionName: str, optionValue: str) -> bool:
        """Method docstring."""
        ...

    def GetCalculationOptions(self, calculationModel: str) -> Dict[str, str]:
        """Method docstring."""
        ...

    def GetClinicalGoals(self) -> List[ClinicalGoal]:
        """Method docstring."""
        ...

    def GetDVHCumulativeData(self, structure: Structure, dosePresentation: DoseValuePresentation, volumePresentation: VolumePresentation, binWidth: float) -> DVHData:
        """Method docstring."""
        ...

    def GetDoseAtVolume(self, structure: Structure, volume: float, volumePresentation: VolumePresentation, requestedDosePresentation: DoseValuePresentation) -> DoseValue:
        """Method docstring."""
        ...

    def GetDvhEstimationModelName(self) -> str:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetModelsForCalculationType(self, calculationType: CalculationType) -> List[str]:
        """Method docstring."""
        ...

    def GetProtocolPrescriptionsAndMeasures(self, prescriptions: List, measures: List) -> None:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def GetVolumeAtDose(self, structure: Structure, dose: DoseValue, requestedVolumePresentation: VolumePresentation) -> float:
        """Method docstring."""
        ...

    def IsEntireBodyAndBolusesCoveredByCalculationArea(self) -> bool:
        """Method docstring."""
        ...

    def IsValidForPlanApproval(self, validationResults: List) -> bool:
        """Method docstring."""
        ...

    def MoveToCourse(self, destinationCourse: Course) -> None:
        """Method docstring."""
        ...

    def Optimize(self, maxIterations: int) -> OptimizerResult:
        """Runs IMRT optimization for the plan setup. The Multileaf Collimator (MLC) is determined automatically. If there are more than one MLC or no MLC at all, an exception is thrown. Plan normalization method is changed to 'No plan normalization' after successful optimization.
        
        Returns:
            OptimizerResult: The result of the optimization."""
        ...

    @overload
    def Optimize(self, maxIterations: int, optimizationOption: OptimizationOption) -> OptimizerResult:
        """Runs IMRT optimization for the plan setup. The Multileaf Collimator (MLC) is determined automatically. If there are more than one MLC or no MLC at all, an exception is thrown. Plan normalization method is changed to 'No plan normalization' after successful optimization.
        
        Returns:
            OptimizerResult: The result of the optimization."""
        ...

    @overload
    def Optimize(self, maxIterations: int, optimizationOption: OptimizationOption, mlcId: str) -> OptimizerResult:
        """Runs IMRT optimization for the plan setup. The Multileaf Collimator (MLC) is determined automatically. If there are more than one MLC or no MLC at all, an exception is thrown. Plan normalization method is changed to 'No plan normalization' after successful optimization.
        
        Returns:
            OptimizerResult: The result of the optimization."""
        ...

    @overload
    def Optimize(self) -> OptimizerResult:
        """Runs IMRT optimization for the plan setup. The Multileaf Collimator (MLC) is determined automatically. If there are more than one MLC or no MLC at all, an exception is thrown. Plan normalization method is changed to 'No plan normalization' after successful optimization.
        
        Returns:
            OptimizerResult: The result of the optimization."""
        ...

    @overload
    def Optimize(self, options: OptimizationOptionsIMRT) -> OptimizerResult:
        """Runs IMRT optimization for the plan setup. The Multileaf Collimator (MLC) is determined automatically. If there are more than one MLC or no MLC at all, an exception is thrown. Plan normalization method is changed to 'No plan normalization' after successful optimization.
        
        Returns:
            OptimizerResult: The result of the optimization."""
        ...

    def OptimizeVMAT(self, mlcId: str) -> OptimizerResult:
        """[Availability of this method depends on your Eclipse Scripting API license] Runs VMAT optimization for the plan setup. The Multileaf Collimator (MLC) is determined automatically. If there are more than one MLC or no MLC at all, an exception is thrown. Plan normalization method is changed to 'No plan normalization' after successful optimization.
        
        Returns:
            OptimizerResult: The result of the optimization."""
        ...

    @overload
    def OptimizeVMAT(self) -> OptimizerResult:
        """[Availability of this method depends on your Eclipse Scripting API license] Runs VMAT optimization for the plan setup. The Multileaf Collimator (MLC) is determined automatically. If there are more than one MLC or no MLC at all, an exception is thrown. Plan normalization method is changed to 'No plan normalization' after successful optimization.
        
        Returns:
            OptimizerResult: The result of the optimization."""
        ...

    @overload
    def OptimizeVMAT(self, options: OptimizationOptionsVMAT) -> OptimizerResult:
        """[Availability of this method depends on your Eclipse Scripting API license] Runs VMAT optimization for the plan setup. The Multileaf Collimator (MLC) is determined automatically. If there are more than one MLC or no MLC at all, an exception is thrown. Plan normalization method is changed to 'No plan normalization' after successful optimization.
        
        Returns:
            OptimizerResult: The result of the optimization."""
        ...

    def ReadXml(self, reader: XmlReader) -> None:
        """Method docstring."""
        ...

    def RemoveBeam(self, beam: Beam) -> None:
        """Method docstring."""
        ...

    def RemoveReferencePoint(self, refPoint: ReferencePoint) -> None:
        """Method docstring."""
        ...

    def SetCalculationModel(self, calculationType: CalculationType, model: str) -> None:
        """Method docstring."""
        ...

    def SetCalculationOption(self, calculationModel: str, optionName: str, optionValue: str) -> bool:
        """Method docstring."""
        ...

    def SetPrescription(self, numberOfFractions: int, dosePerFraction: DoseValue, treatmentPercentage: float) -> None:
        """Method docstring."""
        ...

    def SetTargetStructureIfNoDose(self, newTargetStructure: Structure, errorHint: StringBuilder) -> bool:
        """Method docstring."""
        ...

    def SetTreatmentOrder(self, orderedBeams: List[Beam]) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    def WriteXml(self, writer: XmlWriter) -> None:
        """Method docstring."""
        ...


class FieldReferencePoint(ApiDataObject):
    """This object links a treatment beam to a reference point."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def EffectiveDepth(self) -> float:
        """float: The effective depth of the field reference point. For arc fields this is the average value over the span of the arc."""
        ...

    @property
    def FieldDose(self) -> DoseValue:
        """DoseValue: The field dose."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def IsFieldDoseNominal(self) -> bool:
        """bool: Checks if the field dose is nominal (the real calculated field dose is not known). If the field doses at a reference point are nominal, they alone cannot be used to verify MU calculation."""
        ...

    @property
    def IsPrimaryReferencePoint(self) -> bool:
        """bool: Checks if the reference point is primary."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def RefPointLocation(self) -> VVector:
        """VVector: The location of the reference point."""
        ...

    @property
    def ReferencePoint(self) -> ReferencePoint:
        """ReferencePoint: Used for navigating to an underlying reference point."""
        ...

    @property
    def SSD(self) -> float:
        """float: The Source-to-Skin Distance (SSD) of the reference point. For arc fields this is the average value over the span of the arc."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class Globals:
    """This class is internal to the Eclipse Scripting API."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @classmethod
    @property
    def AbortNow(cls) -> bool:
        """bool: The flag that aborts script execution the next time any property or method of the Eclipse Scripting API is accessed."""
        ...

    @classmethod
    @AbortNow.setter
    def AbortNow(cls, value: bool) -> None:
        """Set property value."""
        ...

    @classmethod
    @property
    def DefaultMaximumNumberOfLoggedApiCalls(cls) -> int:
        """int: The default maximum number of API calls that are saved in the script execution log."""
        ...

    @staticmethod
    def AddCustomLogEntry(message: str, logSeverity: LogSeverity) -> None:
        """Method docstring."""
        ...

    @staticmethod
    def DisableApiAccessTrace() -> None:
        """Disables the getting of access information for API members through .NET trace listener."""
        ...

    @staticmethod
    def EnableApiAccessTrace() -> None:
        """Enables the getting of access information for API members through .NET trace listener."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    @staticmethod
    def GetLoggedApiCalls() -> List[str]:
        """Returns the last called properties and methods. The oldest cached call is the first. The maximum number of logged calls is set by calling SetMaximumNumberOfLoggedApiCalls.
        
        Returns:
            List[str]: The called API properties and methods as saved in the cache."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    @staticmethod
    def Initialize(logger: ILogger, executingAssemblyName: AssemblyName) -> None:
        """Method docstring."""
        ...

    @staticmethod
    def SetMaximumNumberOfLoggedApiCalls(apiLogCacheSize: int) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...


class Hospital(ApiDataObject):
    """Represents a hospital."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def CreationDateTime(self) -> Optional[datetime]:
        """Optional[datetime]: The date when this object was created."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Location(self) -> str:
        """str: The location of the hospital."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class IDVHEstimationCalculator:
    """Interface to the calculation of the DVH Estimates"""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    def CalculateDVHEstimates(self, modelId: str, targetDoseLevels: Dict[str, DoseValue], structureMatches: Dict[str, str]) -> CalculationResult:
        """Method docstring."""
        ...


class Image(ApiDataObject):
    """Represents a 2D or 3D image, which can be a DRR, a CT, MR, or other volumetric dataset."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def ApprovalHistory(self) -> List[ImageApprovalHistoryEntry]:
        """List[ImageApprovalHistoryEntry]: Returns the approval history of the image."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def ContrastBolusAgentIngredientName(self) -> str:
        """str: The name of the contrast bolus agent ingredient that is used in the image. If the value has not been specified, returns null."""
        ...

    @property
    def CreationDateTime(self) -> Optional[datetime]:
        """Optional[datetime]: The date when this object was created."""
        ...

    @property
    def DisplayUnit(self) -> str:
        """str: The name of the display unit in which the voxels of the image are shown in the user interface."""
        ...

    @property
    def FOR(self) -> str:
        """str: The UID of the frame of reference."""
        ...

    @property
    def HasUserOrigin(self) -> bool:
        """bool: Defines if a user origin has been specified for the image."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: [Availability of this property depends on your Eclipse Scripting API license] The identifier of the image."""
        ...

    @Id.setter
    def Id(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def ImageType(self) -> str:
        """str: The type of the image as indicated in the properties of the image slices."""
        ...

    @property
    def ImagingDeviceId(self) -> str:
        """str: Identification of the device that is used to scan the images into the system."""
        ...

    @property
    def ImagingOrientation(self) -> PatientOrientation:
        """PatientOrientation: The orientation of the patient."""
        ...

    @property
    def ImagingOrientationAsString(self) -> str:
        """str: The orientation of the patient as a string (localized)"""
        ...

    @property
    def IsProcessed(self) -> bool:
        """bool: Returns the value true if an image processing filter is in use for the image."""
        ...

    @property
    def Level(self) -> int:
        """int: The level setting. The value is given in the internal voxel scale."""
        ...

    @property
    def Modality(self) -> SeriesModality:
        """SeriesModality: The modality of the image as indicated in the properties of the image slices."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Origin(self) -> VVector:
        """VVector: The origin of the image. In other words, the DICOM coordinates of the center point of the upper-left hand corner voxel of the first image plane. Supported only for volume images. For other types of images, the return value is a vector of Double.NaNs."""
        ...

    @property
    def Series(self) -> Series:
        """Series: Used for navigating to parent series."""
        ...

    @property
    def UID(self) -> str:
        """str: Return UID of the first (and the only) slice in case of a 2D Image. Return null in case of a 3D Image."""
        ...

    @property
    def UserOrigin(self) -> VVector:
        """VVector: The user origin in DICOM coordinates in millimeter."""
        ...

    @UserOrigin.setter
    def UserOrigin(self, value: VVector) -> None:
        """Set property value."""
        ...

    @property
    def UserOriginComments(self) -> str:
        """str: The text typed on the Origin tab in the Image Properties dialog box."""
        ...

    @property
    def Window(self) -> int:
        """int: The window setting. The value is given in the internal voxel scale."""
        ...

    @property
    def XDirection(self) -> VVector:
        """VVector: The direction of the x-axis in the image. Supported only for volume images. For other types of images, the return value is a vector of Double.NaNs."""
        ...

    @property
    def XRes(self) -> float:
        """float: The image resolution in X-direction in millimeters."""
        ...

    @property
    def XSize(self) -> int:
        """int: The image size in X-direction in voxels."""
        ...

    @property
    def YDirection(self) -> VVector:
        """VVector: The direction of the y-axis in the image. Supported only for volume images. For other types of images, the return value is a vector of Double.NaNs."""
        ...

    @property
    def YRes(self) -> float:
        """float: The image resolution in Y-direction in millimeters."""
        ...

    @property
    def YSize(self) -> int:
        """int: The image size in Y-direction in voxels."""
        ...

    @property
    def ZDirection(self) -> VVector:
        """VVector: The direction of the z-axis in the image. Supported only for volume images. For other types of images, the return value is a vector of Double.NaNs."""
        ...

    @property
    def ZRes(self) -> float:
        """float: The image resolution in Z-direction in millimeters."""
        ...

    @property
    def ZSize(self) -> int:
        """int: The image size in Z-direction in voxels."""
        ...

    def CalculateDectProtonStoppingPowers(self, rhoImage: Image, zImage: Image, planeIndex: int, preallocatedBuffer: Array[float]) -> None:
        """Method docstring."""
        ...

    def CreateNewStructureSet(self) -> StructureSet:
        """[Availability of this method depends on your Eclipse Scripting API license] Creates a new structure set. If the image does not yet have a structure set, the new structure set will be assigned directly to it. If the image already has a structure set, a copy of this image is made, and the new structure set is assigned to the copy. The image must be a 3D image.
        
        Returns:
            StructureSet: New structure set."""
        ...

    def DicomToUser(self, dicom: VVector, planSetup: PlanSetup) -> VVector:
        """Method docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetImageProfile(self, start: VVector, stop: VVector, preallocatedBuffer: Array[float]) -> ImageProfile:
        """Method docstring."""
        ...

    def GetProtonStoppingPowerCurve(self, protonStoppingPowerCurve: List[float]) -> bool:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def GetVoxels(self, planeIndex: int, preallocatedBuffer: Array[int]) -> None:
        """Method docstring."""
        ...

    def ReadXml(self, reader: XmlReader) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    def UserToDicom(self, user: VVector, planSetup: PlanSetup) -> VVector:
        """Method docstring."""
        ...

    def VoxelToDisplayValue(self, voxelValue: int) -> float:
        """Method docstring."""
        ...

    def WriteXml(self, writer: XmlWriter) -> None:
        """Method docstring."""
        ...


class IonBeam(Beam):
    """Proton beam interface."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def AirGap(self) -> float:
        """float: The user-defined air gap in mm."""
        ...

    @property
    def Applicator(self) -> Applicator:
        """Applicator: Property docstring."""
        ...

    @property
    def ArcLength(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def AreControlPointJawsMoving(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def AverageSSD(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def BeamLineStatus(self) -> ProtonBeamLineStatus:
        """ProtonBeamLineStatus: Determine beamline's status"""
        ...

    @property
    def BeamNumber(self) -> int:
        """int: Property docstring."""
        ...

    @property
    def BeamTechnique(self) -> BeamTechnique:
        """BeamTechnique: Property docstring."""
        ...

    @property
    def Blocks(self) -> List[Block]:
        """List[Block]: Property docstring."""
        ...

    @property
    def Boluses(self) -> List[Bolus]:
        """List[Bolus]: Property docstring."""
        ...

    @property
    def CalculationLogs(self) -> List[BeamCalculationLog]:
        """List[BeamCalculationLog]: Property docstring."""
        ...

    @property
    def CollimatorRotation(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @Comment.setter
    def Comment(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def Compensator(self) -> Compensator:
        """Compensator: Property docstring."""
        ...

    @property
    def ControlPoints(self) -> ControlPointCollection:
        """ControlPointCollection: Property docstring."""
        ...

    @property
    def CreationDateTime(self) -> Optional[datetime]:
        """Optional[datetime]: Property docstring."""
        ...

    @property
    def DistalTargetMargin(self) -> float:
        """float: Distal end margin, in mm."""
        ...

    @DistalTargetMargin.setter
    def DistalTargetMargin(self, value: float) -> None:
        """Set property value."""
        ...

    @property
    def Dose(self) -> BeamDose:
        """BeamDose: Property docstring."""
        ...

    @property
    def DoseRate(self) -> int:
        """int: Property docstring."""
        ...

    @property
    def DosimetricLeafGap(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def EnergyMode(self) -> EnergyMode:
        """EnergyMode: Property docstring."""
        ...

    @property
    def EnergyModeDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def FieldReferencePoints(self) -> List[FieldReferencePoint]:
        """List[FieldReferencePoint]: Property docstring."""
        ...

    @property
    def GantryDirection(self) -> GantryDirection:
        """GantryDirection: Property docstring."""
        ...

    @property
    def HasAllMLCLeavesClosed(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
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
    def IonControlPoints(self) -> IonControlPointCollection:
        """IonControlPointCollection: Gets the proton control points."""
        ...

    @property
    def IsGantryExtended(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsGantryExtendedAtStopAngle(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsIMRT(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsImagingTreatmentField(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsSetupField(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsocenterPosition(self) -> VVector:
        """VVector: Property docstring."""
        ...

    @property
    def LateralMargins(self) -> VRect[float]:
        """VRect[float]: The lateral margins of this field, in mm."""
        ...

    @LateralMargins.setter
    def LateralMargins(self, value: VRect[float]) -> None:
        """Set property value."""
        ...

    @property
    def LateralSpreadingDevices(self) -> List[LateralSpreadingDevice]:
        """List[LateralSpreadingDevice]: The lateral spreading devices in this beam."""
        ...

    @property
    def MLC(self) -> MLC:
        """MLC: Property docstring."""
        ...

    @property
    def MLCPlanType(self) -> MLCPlanType:
        """MLCPlanType: Property docstring."""
        ...

    @property
    def MLCTransmissionFactor(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def Meterset(self) -> MetersetValue:
        """MetersetValue: Property docstring."""
        ...

    @property
    def MetersetPerGy(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def MotionCompensationTechnique(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def MotionSignalSource(self) -> str:
        """str: Property docstring."""
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
    def NominalRange(self) -> float:
        """float: The nominal range of the beam line, in mm."""
        ...

    @property
    def NominalSOBPWidth(self) -> float:
        """float: The nominal width of the Spread Out Bragg Peak, in mm."""
        ...

    @property
    def NormalizationFactor(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def NormalizationMethod(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def OptionId(self) -> str:
        """str: The identifier of the selected beam-line setting for proton beams. For a typical double scattering system, for example, an option is a combination of range modulator, second scatterer, and nominal energy that correspond to a broad proton beam with a certain range in patient and field size. Returns null if the option is undefined."""
        ...

    @property
    def PatientSupportId(self) -> str:
        """str: Patient support identifier. Returns null if undefined."""
        ...

    @property
    def PatientSupportType(self) -> PatientSupportType:
        """PatientSupportType: Patient support type."""
        ...

    @property
    def Plan(self) -> PlanSetup:
        """PlanSetup: Property docstring."""
        ...

    @property
    def PlannedSSD(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def ProximalTargetMargin(self) -> float:
        """float: Proximal end margin, in mm."""
        ...

    @ProximalTargetMargin.setter
    def ProximalTargetMargin(self, value: float) -> None:
        """Set property value."""
        ...

    @property
    def RangeModulators(self) -> List[RangeModulator]:
        """List[RangeModulator]: The range modulator devices in this beam."""
        ...

    @property
    def RangeShifters(self) -> List[RangeShifter]:
        """List[RangeShifter]: The range shifter devices in this beam."""
        ...

    @property
    def ReferenceImage(self) -> Image:
        """Image: Property docstring."""
        ...

    @property
    def SSD(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def SSDAtStopAngle(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def ScanMode(self) -> IonBeamScanMode:
        """IonBeamScanMode: The method of beam scanning to be used during treatment."""
        ...

    @property
    def SetupNote(self) -> str:
        """str: Property docstring."""
        ...

    @SetupNote.setter
    def SetupNote(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def SetupTechnique(self) -> SetupTechnique:
        """SetupTechnique: Property docstring."""
        ...

    @property
    def SnoutId(self) -> str:
        """str: The Snout identifier. Returns null if undefined."""
        ...

    @property
    def SnoutPosition(self) -> float:
        """float: The snout position in cm. Returns System::Double::NaN if undefined."""
        ...

    @property
    def TargetStructure(self) -> Structure:
        """Structure: Returns the field target structure. Null if the field target is not defined (and axial margins are defined around the isocenter level)."""
        ...

    @property
    def Technique(self) -> Technique:
        """Technique: Property docstring."""
        ...

    @property
    def ToleranceTableLabel(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Trays(self) -> List[Tray]:
        """List[Tray]: Property docstring."""
        ...

    @property
    def TreatmentTime(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def TreatmentUnit(self) -> ExternalBeamTreatmentUnit:
        """ExternalBeamTreatmentUnit: Property docstring."""
        ...

    @property
    def VirtualSADX(self) -> float:
        """float: Virtual Source-to-Axis Distance X, in mm."""
        ...

    @property
    def VirtualSADY(self) -> float:
        """float: Virtual Source-to-Axis Distance Y, in mm."""
        ...

    @property
    def Wedges(self) -> List[Wedge]:
        """List[Wedge]: Property docstring."""
        ...

    @property
    def WeightFactor(self) -> float:
        """float: Property docstring."""
        ...

    def AddBolus(self, bolus: Bolus) -> None:
        """Method docstring."""
        ...

    @overload
    def AddBolus(self, bolusId: str) -> None:
        """Method docstring."""
        ...

    def AddFlatteningSequence(self) -> bool:
        """Method docstring."""
        ...

    def ApplyParameters(self, beamParams: BeamParameters) -> None:
        """Method docstring."""
        ...

    @overload
    def ApplyParameters(self, beamParams: BeamParameters) -> None:
        """Method docstring."""
        ...

    def CalculateAverageLeafPairOpenings(self) -> Dict[int, float]:
        """Method docstring."""
        ...

    def CanSetOptimalFluence(self, fluence: Fluence, message: str) -> bool:
        """Method docstring."""
        ...

    def CollimatorAngleToUser(self, val: float) -> float:
        """Method docstring."""
        ...

    def CountSubfields(self) -> int:
        """Method docstring."""
        ...

    def CreateOrReplaceDRR(self, parameters: DRRCalculationParameters) -> Image:
        """Method docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def FitCollimatorToStructure(self, margins: FitToStructureMargins, structure: Structure, useAsymmetricXJaws: bool, useAsymmetricYJaws: bool, optimizeCollimatorRotation: bool) -> None:
        """Method docstring."""
        ...

    def FitMLCToOutline(self, outline: Array[Array[Point]]) -> None:
        """Method docstring."""
        ...

    @overload
    def FitMLCToOutline(self, outline: Array[Array[Point]], optimizeCollimatorRotation: bool, jawFit: JawFitting, olmp: OpenLeavesMeetingPoint, clmp: ClosedLeavesMeetingPoint) -> None:
        """Method docstring."""
        ...

    def FitMLCToStructure(self, structure: Structure) -> None:
        """Method docstring."""
        ...

    @overload
    def FitMLCToStructure(self, margins: FitToStructureMargins, structure: Structure, optimizeCollimatorRotation: bool, jawFit: JawFitting, olmp: OpenLeavesMeetingPoint, clmp: ClosedLeavesMeetingPoint) -> None:
        """Method docstring."""
        ...

    def GantryAngleToUser(self, val: float) -> float:
        """Method docstring."""
        ...

    def GetCAXPathLengthInBolus(self, bolus: Bolus) -> float:
        """Method docstring."""
        ...

    def GetDeliveryTimeStatusByRoomId(self, roomId: str) -> ProtonDeliveryTimeStatus:
        """Method docstring."""
        ...

    def GetEditableParameters(self) -> IonBeamParameters:
        """Returns a new editable copy of the ion beam parameters. The returned IonBeamParameters object is not updated if the beam parameters in the data model are changed, for example, by using another IonBeamParameters object.
        
        Returns:
            IonBeamParameters: Returns a new parameters object. Its values are copied from the corresponding properties of this object."""
        ...

    @overload
    def GetEditableParameters(self) -> BeamParameters:
        """Returns a new editable copy of the ion beam parameters. The returned IonBeamParameters object is not updated if the beam parameters in the data model are changed, for example, by using another IonBeamParameters object.
        
        Returns:
            BeamParameters: Returns a new parameters object. Its values are copied from the corresponding properties of this object."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetOptimalFluence(self) -> Fluence:
        """Method docstring."""
        ...

    def GetProtonDeliveryTimeByRoomIdAsNumber(self, roomId: str) -> float:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
        ...

    def GetSourceLocation(self, gantryAngle: float) -> VVector:
        """Method docstring."""
        ...

    def GetSourceToBolusDistance(self, bolus: Bolus) -> float:
        """Method docstring."""
        ...

    def GetStructureOutlines(self, structure: Structure, inBEV: bool) -> Array[Array[Point]]:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def JawPositionsToUserString(self, val: VRect[float]) -> str:
        """Method docstring."""
        ...

    def PatientSupportAngleToUser(self, val: float) -> float:
        """Method docstring."""
        ...

    def ReadXml(self, reader: XmlReader) -> None:
        """Method docstring."""
        ...

    def RemoveBolus(self, bolus: Bolus) -> bool:
        """Method docstring."""
        ...

    @overload
    def RemoveBolus(self, bolusId: str) -> bool:
        """Method docstring."""
        ...

    def RemoveFlatteningSequence(self) -> bool:
        """Method docstring."""
        ...

    def SetOptimalFluence(self, fluence: Fluence) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    def WriteXml(self, writer: XmlWriter) -> None:
        """Method docstring."""
        ...


class IonBeamParameters(BeamParameters):
    """An editable copy of the parameters of a proton beam.
    
    To apply the parameters, call the"""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def ControlPoints(self) -> List[ControlPointParameters]:
        """List[ControlPointParameters]: Editable control point parameters copied from the treatment beam."""
        ...

    @property
    def GantryDirection(self) -> GantryDirection:
        """GantryDirection: Property docstring."""
        ...

    @property
    def IonControlPointPairs(self) -> IonControlPointPairCollection:
        """IonControlPointPairCollection: A copy of editable control point pairs."""
        ...

    @property
    def Isocenter(self) -> VVector:
        """VVector: Property docstring."""
        ...

    @Isocenter.setter
    def Isocenter(self, value: VVector) -> None:
        """Set property value."""
        ...

    @property
    def PreSelectedRangeShifter1Id(self) -> str:
        """str: ID of the pre-selected range shifter 1 in the field."""
        ...

    @PreSelectedRangeShifter1Id.setter
    def PreSelectedRangeShifter1Id(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def PreSelectedRangeShifter1Setting(self) -> str:
        """str: Setting of the pre-selected range shifter 1 in the field."""
        ...

    @PreSelectedRangeShifter1Setting.setter
    def PreSelectedRangeShifter1Setting(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def PreSelectedRangeShifter2Id(self) -> str:
        """str: ID of the pre-selected range shifter 2 in the field."""
        ...

    @PreSelectedRangeShifter2Id.setter
    def PreSelectedRangeShifter2Id(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def PreSelectedRangeShifter2Setting(self) -> str:
        """str: Setting of the pre-selected range shifter 2 in the field."""
        ...

    @PreSelectedRangeShifter2Setting.setter
    def PreSelectedRangeShifter2Setting(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def SnoutId(self) -> str:
        """str: The snout identifier. Returns null if undefined."""
        ...

    @property
    def SnoutPosition(self) -> float:
        """float: Snout position in centimeters."""
        ...

    @property
    def TargetStructure(self) -> Structure:
        """Structure: Target structure of the field."""
        ...

    @TargetStructure.setter
    def TargetStructure(self, value: Structure) -> None:
        """Set property value."""
        ...

    @property
    def WeightFactor(self) -> float:
        """float: Property docstring."""
        ...

    @WeightFactor.setter
    def WeightFactor(self, value: float) -> None:
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

    def SetAllLeafPositions(self, leafPositions: Array[float]) -> None:
        """Method docstring."""
        ...

    def SetJawPositions(self, positions: VRect[float]) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...


class IonControlPoint(ControlPoint):
    """Proton control point interface."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Beam(self) -> Beam:
        """Beam: Property docstring."""
        ...

    @property
    def CollimatorAngle(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def FinalSpotList(self) -> IonSpotCollection:
        """IonSpotCollection: Gets a cached copy of the post-processed final spot list."""
        ...

    @property
    def GantryAngle(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def Index(self) -> int:
        """int: Property docstring."""
        ...

    @property
    def JawPositions(self) -> VRect[float]:
        """VRect[float]: Property docstring."""
        ...

    @property
    def LateralSpreadingDeviceSettings(self) -> List[LateralSpreadingDeviceSettings]:
        """List[LateralSpreadingDeviceSettings]: The lateral spreading device settings."""
        ...

    @property
    def LeafPositions(self) -> Array[float]:
        """Array[float]: Property docstring."""
        ...

    @property
    def MetersetWeight(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def NominalBeamEnergy(self) -> float:
        """float: Nominal beam energy, in megavolts."""
        ...

    @property
    def NumberOfPaintings(self) -> int:
        """int: The number of times the scan pattern shall be applied at the current control point."""
        ...

    @property
    def PatientSupportAngle(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def RangeModulatorSettings(self) -> List[RangeModulatorSettings]:
        """List[RangeModulatorSettings]: The range modulator settings."""
        ...

    @property
    def RangeShifterSettings(self) -> List[RangeShifterSettings]:
        """List[RangeShifterSettings]: The range shifter settings."""
        ...

    @property
    def RawSpotList(self) -> IonSpotCollection:
        """IonSpotCollection: Gets a cached copy of the raw spot list."""
        ...

    @property
    def ScanSpotTuneId(self) -> str:
        """str: User-supplied or machine code identifier for machine configuration to produce beam spot. This may be the nominal spot size or some other machine-specific value. Returns null if undefined."""
        ...

    @property
    def ScanningSpotSizeX(self) -> float:
        """float: The scanning spot size as calculated using the Full Width HalfMaximum (FWHM). The size is measured in air at isocenter in IEC GANTRY X direction (mm)."""
        ...

    @property
    def ScanningSpotSizeY(self) -> float:
        """float: The scanning spot size as calculated using the Full Width HalfMaximum (FWHM). The size is measured in air at isocenter in IEC GANTRY Y direction (mm)."""
        ...

    @property
    def SnoutPosition(self) -> float:
        """float: The snout position, in mm."""
        ...

    @property
    def TableTopLateralPosition(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def TableTopLongitudinalPosition(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def TableTopVerticalPosition(self) -> float:
        """float: Property docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class IonControlPointCollection(SerializableObject):
    """Represents a collection of machine parameters that describe the planned proton beam."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Count(self) -> int:
        """int: The number of control points in the collection."""
        ...

    @property
    def Item(self) -> IonControlPoint:
        """IonControlPoint: Property docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetEnumerator(self) -> IEnumerator[IonControlPoint]:
        """Retrieves enumerator for IonControlPoints in the collection.
        
        Returns:
            IEnumerator[IonControlPoint]: Enumerator for IonControlPoints in the collection."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class IonControlPointPair:
    """An editable copy of a control point pair (the pair of the start control point with an even index, and the end control point with an odd index).
    
    To apply the parameters, call the"""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def EndControlPoint(self) -> IonControlPointParameters:
        """IonControlPointParameters: The end control point in the pair, with an odd index."""
        ...

    @property
    def FinalSpotList(self) -> IonSpotParametersCollection:
        """IonSpotParametersCollection: Gets a cached copy of the editable post-processed final spot list."""
        ...

    @property
    def NominalBeamEnergy(self) -> float:
        """float: Nominal beam energy in megavolts."""
        ...

    @property
    def RawSpotList(self) -> IonSpotParametersCollection:
        """IonSpotParametersCollection: Gets a cached copy of the editable raw spot list"""
        ...

    @property
    def StartControlPoint(self) -> IonControlPointParameters:
        """IonControlPointParameters: Start control point in the pair, with an even index from zero."""
        ...

    @property
    def StartIndex(self) -> int:
        """int: The index of the start control point in the pair. The index should be an even number starting from zero."""
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

    def ResizeFinalSpotList(self, count: int) -> None:
        """Method docstring."""
        ...

    def ResizeRawSpotList(self, count: int) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...


class IonControlPointPairCollection:
    """A collection of editable copies of control point pairs that describe the planned proton beam.
    
    To apply the parameters, call the"""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Count(self) -> int:
        """int: The number of control point pairs in the collection."""
        ...

    @property
    def Item(self) -> IonControlPointPair:
        """IonControlPointPair: Property docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetEnumerator(self) -> IEnumerator[IonControlPointPair]:
        """Retrieves enumerator for IonControlPointPairs in the collection.
        
        Returns:
            IEnumerator[IonControlPointPair]: Enumerator for IonControlPointPairs in the collection."""
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


class IonControlPointParameters(ControlPointParameters):
    """An editable copy of the parameters of a proton control point.
    
    To apply the parameters, call the ApplyParameters method of the Beam class. Because the parameters are simple copies, they do not reflect the current state of the data model."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def CollimatorAngle(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def FinalSpotList(self) -> IonSpotParametersCollection:
        """IonSpotParametersCollection: Gets a cached copy of the post-processed final spot list."""
        ...

    @property
    def GantryAngle(self) -> float:
        """float: Property docstring."""
        ...

    @GantryAngle.setter
    def GantryAngle(self, value: float) -> None:
        """Set property value."""
        ...

    @property
    def Index(self) -> int:
        """int: Property docstring."""
        ...

    @property
    def JawPositions(self) -> VRect[float]:
        """VRect[float]: Property docstring."""
        ...

    @JawPositions.setter
    def JawPositions(self, value: VRect[float]) -> None:
        """Set property value."""
        ...

    @property
    def LeafPositions(self) -> Array[float]:
        """Array[float]: Property docstring."""
        ...

    @LeafPositions.setter
    def LeafPositions(self, value: Array[float]) -> None:
        """Set property value."""
        ...

    @property
    def MetersetWeight(self) -> float:
        """float: Property docstring."""
        ...

    @MetersetWeight.setter
    def MetersetWeight(self, value: float) -> None:
        """Set property value."""
        ...

    @property
    def PatientSupportAngle(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def RawSpotList(self) -> IonSpotParametersCollection:
        """IonSpotParametersCollection: Gets a cached copy of the raw spot list."""
        ...

    @property
    def SnoutPosition(self) -> float:
        """float: Snout position in centimeters."""
        ...

    @SnoutPosition.setter
    def SnoutPosition(self, value: float) -> None:
        """Set property value."""
        ...

    @property
    def TableTopLateralPosition(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def TableTopLongitudinalPosition(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def TableTopVerticalPosition(self) -> float:
        """float: Property docstring."""
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


class IonPlanSetup(PlanSetup):
    """Represents a proton treatment plan."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def ApplicationScriptLogs(self) -> List[ApplicationScriptLog]:
        """List[ApplicationScriptLog]: Property docstring."""
        ...

    @property
    def ApprovalHistory(self) -> List[ApprovalHistoryEntry]:
        """List[ApprovalHistoryEntry]: Property docstring."""
        ...

    @property
    def ApprovalStatus(self) -> PlanSetupApprovalStatus:
        """PlanSetupApprovalStatus: Property docstring."""
        ...

    @property
    def ApprovalStatusAsString(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def BaseDosePlanningItem(self) -> PlanningItem:
        """PlanningItem: Property docstring."""
        ...

    @BaseDosePlanningItem.setter
    def BaseDosePlanningItem(self, value: PlanningItem) -> None:
        """Set property value."""
        ...

    @property
    def Beams(self) -> List[Beam]:
        """List[Beam]: Property docstring."""
        ...

    @property
    def BeamsInTreatmentOrder(self) -> List[Beam]:
        """List[Beam]: Property docstring."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @Comment.setter
    def Comment(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def Course(self) -> Course:
        """Course: Property docstring."""
        ...

    @property
    def CreationDateTime(self) -> Optional[datetime]:
        """Optional[datetime]: Property docstring."""
        ...

    @property
    def CreationUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def DVHEstimates(self) -> List[EstimatedDVH]:
        """List[EstimatedDVH]: Property docstring."""
        ...

    @property
    def Dose(self) -> PlanningItemDose:
        """PlanningItemDose: Property docstring."""
        ...

    @property
    def DoseAsEvaluationDose(self) -> EvaluationDose:
        """EvaluationDose: The evaluation dose is connected to the plan and contains voxels that are set by"""
        ...

    @property
    def DosePerFraction(self) -> DoseValue:
        """DoseValue: Property docstring."""
        ...

    @property
    def DosePerFractionInPrimaryRefPoint(self) -> DoseValue:
        """DoseValue: Property docstring."""
        ...

    @property
    def DoseValuePresentation(self) -> DoseValuePresentation:
        """DoseValuePresentation: Property docstring."""
        ...

    @DoseValuePresentation.setter
    def DoseValuePresentation(self, value: DoseValuePresentation) -> None:
        """Set property value."""
        ...

    @property
    def ElectronCalculationModel(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def ElectronCalculationOptions(self) -> Dict[str, str]:
        """Dict[str, str]: Property docstring."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
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
    def IntegrityHash(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def IonBeams(self) -> List[IonBeam]:
        """List[IonBeam]: Gets the proton beams of the plan."""
        ...

    @property
    def IsDoseValid(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def IsPostProcessingNeeded(self) -> bool:
        """bool: Instructs whether to include the post-processing of scanning spots in proton dose calculation."""
        ...

    @IsPostProcessingNeeded.setter
    def IsPostProcessingNeeded(self, value: bool) -> None:
        """Set property value."""
        ...

    @property
    def IsTreated(self) -> bool:
        """bool: Property docstring."""
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
    def NumberOfFractions(self) -> Optional[int]:
        """Optional[int]: Property docstring."""
        ...

    @property
    def OptimizationSetup(self) -> OptimizationSetup:
        """OptimizationSetup: Property docstring."""
        ...

    @property
    def PatientSupportDevice(self) -> PatientSupportDevice:
        """PatientSupportDevice: Property docstring."""
        ...

    @property
    def PhotonCalculationModel(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def PhotonCalculationOptions(self) -> Dict[str, str]:
        """Dict[str, str]: Property docstring."""
        ...

    @property
    def PlanIntent(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def PlanIsInTreatment(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def PlanNormalizationMethod(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def PlanNormalizationPoint(self) -> VVector:
        """VVector: Property docstring."""
        ...

    @property
    def PlanNormalizationValue(self) -> float:
        """float: Property docstring."""
        ...

    @PlanNormalizationValue.setter
    def PlanNormalizationValue(self, value: float) -> None:
        """Set property value."""
        ...

    @property
    def PlanObjectiveStructures(self) -> List[str]:
        """List[str]: Property docstring."""
        ...

    @property
    def PlanType(self) -> PlanType:
        """PlanType: Property docstring."""
        ...

    @property
    def PlanUncertainties(self) -> List[PlanUncertainty]:
        """List[PlanUncertainty]: Property docstring."""
        ...

    @property
    def PlannedDosePerFraction(self) -> DoseValue:
        """DoseValue: Property docstring."""
        ...

    @property
    def PlanningApprovalDate(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def PlanningApprover(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def PlanningApproverDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def PredecessorPlan(self) -> PlanSetup:
        """PlanSetup: Property docstring."""
        ...

    @property
    def PredecessorPlanUID(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def PrescribedDosePerFraction(self) -> DoseValue:
        """DoseValue: Property docstring."""
        ...

    @property
    def PrescribedPercentage(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def PrimaryReferencePoint(self) -> ReferencePoint:
        """ReferencePoint: Property docstring."""
        ...

    @property
    def ProtocolID(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def ProtocolPhaseID(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def ProtonCalculationModel(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def ProtonCalculationOptions(self) -> Dict[str, str]:
        """Dict[str, str]: Property docstring."""
        ...

    @property
    def RTPrescription(self) -> RTPrescription:
        """RTPrescription: Property docstring."""
        ...

    @property
    def ReferencePoints(self) -> List[ReferencePoint]:
        """List[ReferencePoint]: Property docstring."""
        ...

    @property
    def Series(self) -> Series:
        """Series: Property docstring."""
        ...

    @property
    def SeriesUID(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def StructureSet(self) -> StructureSet:
        """StructureSet: Property docstring."""
        ...

    @property
    def StructuresSelectedForDvh(self) -> List[Structure]:
        """List[Structure]: Property docstring."""
        ...

    @property
    def TargetVolumeID(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def TotalDose(self) -> DoseValue:
        """DoseValue: Property docstring."""
        ...

    @property
    def TotalPrescribedDose(self) -> DoseValue:
        """DoseValue: Property docstring."""
        ...

    @property
    def TreatmentApprovalDate(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def TreatmentApprover(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def TreatmentApproverDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def TreatmentOrientation(self) -> PatientOrientation:
        """PatientOrientation: Property docstring."""
        ...

    @property
    def TreatmentOrientationAsString(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def TreatmentPercentage(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def TreatmentSessions(self) -> List[PlanTreatmentSession]:
        """List[PlanTreatmentSession]: Property docstring."""
        ...

    @property
    def UID(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def UseGating(self) -> bool:
        """bool: Property docstring."""
        ...

    @UseGating.setter
    def UseGating(self, value: bool) -> None:
        """Set property value."""
        ...

    @property
    def VerifiedPlan(self) -> PlanSetup:
        """PlanSetup: Property docstring."""
        ...

    def AddModulatedScanningBeam(self, machineParameters: ProtonBeamMachineParameters, snoutId: str, snoutPosition: float, gantryAngle: float, patientSupportAngle: float, isocenter: VVector) -> Beam:
        """Method docstring."""
        ...

    def AddPlanUncertaintyWithParameters(self, uncertaintyType: PlanUncertaintyType, planSpecificUncertainty: bool, HUConversionError: float, isocenterShift: VVector) -> PlanUncertainty:
        """Method docstring."""
        ...

    def AddReferencePoint(self, target: bool, location: Optional[VVector], id: str) -> ReferencePoint:
        """Method docstring."""
        ...

    @overload
    def AddReferencePoint(self, refPoint: ReferencePoint) -> None:
        """Method docstring."""
        ...

    def CalculateBeamDeliveryDynamics(self) -> CalculationResult:
        """[Availability of this method depends on your Eclipse Scripting API license] Calculates the beam delivery dynamics for the final spot list of a proton plan."""
        ...

    def CalculateBeamLine(self) -> CalculationResult:
        """[Availability of this method depends on your Eclipse Scripting API license] Calculates the beam line for the proton plan.
        
        Returns:
            CalculationResult: The calculation result. See calculation details from"""
        ...

    def CalculateDVHEstimates(self, modelId: str, targetDoseLevels: Dict[str, DoseValue], structureMatches: Dict[str, str]) -> CalculationResult:
        """Method docstring."""
        ...

    def CalculateDose(self) -> CalculationResult:
        """[Availability of this method depends on your Eclipse Scripting API license] Calculates the dose for the proton plan.
        
        Returns:
            CalculationResult: The calculation result. See calculation details from"""
        ...

    def CalculateDoseWithoutPostProcessing(self) -> CalculationResult:
        """Calculates the dose for a proton plan without post-processing. The existing final spot list is used, and no new list is created during the calculation.
        
        Returns:
            CalculationResult: The calculation result. See calculation details from"""
        ...

    def CalculatePlanUncertaintyDoses(self) -> CalculationResult:
        """[Availability of this method depends on your Eclipse Scripting API license] Calculates the plan uncertainty dose for the proton plan.
        
        Returns:
            CalculationResult: The calculation result. See calculation details in"""
        ...

    def ClearCalculationModel(self, calculationType: CalculationType) -> None:
        """Method docstring."""
        ...

    def CopyEvaluationDose(self, existing: Dose) -> EvaluationDose:
        """Method docstring."""
        ...

    def CreateDectVerificationPlan(self, rhoImage: Image, zImage: Image) -> IonPlanSetup:
        """Method docstring."""
        ...

    def CreateEvaluationDose(self) -> EvaluationDose:
        """[Availability of this method depends on your Eclipse Scripting API license] Creates an evaluation dose for the plan. The voxels in an evaluation dose can be set using the Eclipse Scripting API instead of a dose calculation algorithm. To create an evaluation dose, the plan must not contain any beams. To set the evaluation dose voxels, retrieve the dose matrix using the
        
        Saving modifications to the database is not possible if the evaluation dose has been created but voxels have not been set.
        
        Returns:
            EvaluationDose: A new evaluation dose object."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetCalculationModel(self, calculationType: CalculationType) -> str:
        """Method docstring."""
        ...

    def GetCalculationOption(self, calculationModel: str, optionName: str, optionValue: str) -> bool:
        """Method docstring."""
        ...

    def GetCalculationOptions(self, calculationModel: str) -> Dict[str, str]:
        """Method docstring."""
        ...

    def GetClinicalGoals(self) -> List[ClinicalGoal]:
        """Method docstring."""
        ...

    def GetDVHCumulativeData(self, structure: Structure, dosePresentation: DoseValuePresentation, volumePresentation: VolumePresentation, binWidth: float) -> DVHData:
        """Method docstring."""
        ...

    def GetDoseAtVolume(self, structure: Structure, volume: float, volumePresentation: VolumePresentation, requestedDosePresentation: DoseValuePresentation) -> DoseValue:
        """Method docstring."""
        ...

    def GetDvhEstimationModelName(self) -> str:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetModelsForCalculationType(self, calculationType: CalculationType) -> List[str]:
        """Method docstring."""
        ...

    def GetOptimizationMode(self) -> IonPlanOptimizationMode:
        """Get information on whether the plan is optimized using multi-field optimization or single-field optimization.
        
        Returns:
            IonPlanOptimizationMode: MultiFieldOptimization if the plan uses multi-field proton optimization and returns SingleFieldOptimization if the plan uses single-field proton optimization."""
        ...

    def GetProtocolPrescriptionsAndMeasures(self, prescriptions: List, measures: List) -> None:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def GetVolumeAtDose(self, structure: Structure, dose: DoseValue, requestedVolumePresentation: VolumePresentation) -> float:
        """Method docstring."""
        ...

    def IsEntireBodyAndBolusesCoveredByCalculationArea(self) -> bool:
        """Method docstring."""
        ...

    def IsValidForPlanApproval(self, validationResults: List) -> bool:
        """Method docstring."""
        ...

    def MoveToCourse(self, destinationCourse: Course) -> None:
        """Method docstring."""
        ...

    def OptimizeIMPT(self, options: OptimizationOptionsIMPT) -> OptimizerResult:
        """Method docstring."""
        ...

    def PostProcessAndCalculateDose(self) -> CalculationResult:
        """Post-processes the proton plan by creating a final spot list, and calculates the dose.
        
        Returns:
            CalculationResult: The calculation result. See calculation details from"""
        ...

    def ReadXml(self, reader: XmlReader) -> None:
        """Method docstring."""
        ...

    def RemoveReferencePoint(self, refPoint: ReferencePoint) -> None:
        """Method docstring."""
        ...

    def SetCalculationModel(self, calculationType: CalculationType, model: str) -> None:
        """Method docstring."""
        ...

    def SetCalculationOption(self, calculationModel: str, optionName: str, optionValue: str) -> bool:
        """Method docstring."""
        ...

    def SetNormalization(self, normalizationParameters: IonPlanNormalizationParameters) -> None:
        """Method docstring."""
        ...

    def SetOptimizationMode(self, mode: IonPlanOptimizationMode) -> None:
        """Method docstring."""
        ...

    def SetPrescription(self, numberOfFractions: int, dosePerFraction: DoseValue, treatmentPercentage: float) -> None:
        """Method docstring."""
        ...

    def SetTargetStructureIfNoDose(self, newTargetStructure: Structure, errorHint: StringBuilder) -> bool:
        """Method docstring."""
        ...

    def SetTreatmentOrder(self, orderedBeams: List[Beam]) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    def WriteXml(self, writer: XmlWriter) -> None:
        """Method docstring."""
        ...


class IonSpot(SerializableObject):
    """The proton scanning spot interface that contains the 3D spot position and spot weight."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Position(self) -> VVector:
        """VVector: Read-only spot position in X, Y, and Z directions."""
        ...

    @property
    def Weight(self) -> float:
        """float: Read-only spot weight."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class IonSpotCollection(SerializableObject):
    """Interface for the proton scanning spot list."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Count(self) -> int:
        """int: The number of scanning spots in this collection (spot list)."""
        ...

    @property
    def Item(self) -> IonSpot:
        """IonSpot: Property docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetEnumerator(self) -> IEnumerator[IonSpot]:
        """Retrieves enumerator for IonSpots in the collection.
        
        Returns:
            IEnumerator[IonSpot]: Enumerator for IonSpots in the collection."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class IonSpotParameters(SerializableObject):
    """Interface for the proton scanning spot that contains the 3D spot position and spot weight."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Weight(self) -> float:
        """float: Editable spot weight."""
        ...

    @Weight.setter
    def Weight(self, value: float) -> None:
        """Set property value."""
        ...

    @property
    def X(self) -> float:
        """float: Editable X position."""
        ...

    @X.setter
    def X(self, value: float) -> None:
        """Set property value."""
        ...

    @property
    def Y(self) -> float:
        """float: Editable Y position."""
        ...

    @Y.setter
    def Y(self, value: float) -> None:
        """Set property value."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class IonSpotParametersCollection(SerializableObject):
    """Interface for the editable proton scanning spot list."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Count(self) -> int:
        """int: The number of editable scanning spots in this collection (spot list)."""
        ...

    @property
    def Item(self) -> IonSpotParameters:
        """IonSpotParameters: Property docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetEnumerator(self) -> IEnumerator[IonSpotParameters]:
        """Retrieves enumerator for IonSpotParameterss in the collection.
        
        Returns:
            IEnumerator[IonSpotParameters]: Enumerator for IonSpotParameterss in the collection."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class Isodose(SerializableObject):
    """Represents an isodose level for a fixed absolute or relative dose value."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Color(self) -> Color:
        """Color: The color of the isodose."""
        ...

    @property
    def Level(self) -> DoseValue:
        """DoseValue: The dose value of the isodose level."""
        ...

    @property
    def MeshGeometry(self) -> MeshGeometry3D:
        """MeshGeometry3D: The triangle mesh of the isodose. Returned for those isodose levels that are rendered in 3D in Eclipse."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class LMCMSSProgressHandler:
    """Class docstring."""

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

    def HandleProgressUntilDone(self, progress: ILMCMSSProgress) -> None:
        """Method docstring."""
        ...

    def HandleVeryLowMinMUOperatingLimit(self, machine: str, minMu: float, precision: int, canContinue: bool) -> None:
        """Method docstring."""
        ...

    def ShowDetailedError(self, message: str, details: str) -> None:
        """Method docstring."""
        ...

    def ShowDetailedWarning(self, message: str, details: str) -> None:
        """Method docstring."""
        ...

    def ShowError(self, message: str) -> None:
        """Method docstring."""
        ...

    def ShowMessage(self, message: str) -> None:
        """Method docstring."""
        ...

    def ShowWarning(self, message: str) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...


class LateralSpreadingDevice(AddOn):
    """The lateral spreading device."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def CreationDateTime(self) -> Optional[datetime]:
        """Optional[datetime]: Property docstring."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Type(self) -> LateralSpreadingDeviceType:
        """LateralSpreadingDeviceType: The type of the device."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class LateralSpreadingDeviceSettings(SerializableObject):
    """Settings for the lateral spreading device."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def IsocenterToLateralSpreadingDeviceDistance(self) -> float:
        """float: Distance from the isocenter to the downstream edge of the lateral spreading device (mm) at the current control point."""
        ...

    @property
    def LateralSpreadingDeviceSetting(self) -> str:
        """str: Machine-specific setting."""
        ...

    @property
    def LateralSpreadingDeviceWaterEquivalentThickness(self) -> float:
        """float: Water equivalent thickness (in mm) of the lateral spreading device at the central axis for the beam energy incident upon the device."""
        ...

    @property
    def ReferencedLateralSpreadingDevice(self) -> LateralSpreadingDevice:
        """LateralSpreadingDevice: The referenced lateral spreading device."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class LoggingMessageHandler:
    """Class docstring."""

    def __init__(self, onMessageHandler: OnMessageHandler) -> None:
        """Initialize instance."""
        ...

    @property
    def LogFileDelegate(self) -> Func[ILogFile]:
        """Func[ILogFile]: Property docstring."""
        ...

    @LogFileDelegate.setter
    def LogFileDelegate(self, value: Func[ILogFile]) -> None:
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

    def OnMessage(self, args: MessageArgs) -> DialogResult:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...


class MLC(AddOn):
    """Represents a Multileaf Collimator (MLC) add-on."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def CreationDateTime(self) -> Optional[datetime]:
        """Optional[datetime]: Property docstring."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def ManufacturerName(self) -> str:
        """str: The name of the manufacturer of the Multileaf Collimator (MLC)."""
        ...

    @property
    def MinDoseDynamicLeafGap(self) -> float:
        """float: For dose-dynamic treatments, the minimum gap (mm) between moving, open leaf pairs that the Multileaf Collimator (MLC) hardware can handle."""
        ...

    @property
    def Model(self) -> str:
        """str: The number or name of the Multileaf Collimator (MLC) model."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def SerialNumber(self) -> str:
        """str: The serial number given to the Multileaf Collimator (MLC) by the factory."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class McoContextState:
    """Class docstring."""

    BalancedPlanReset: McoContextState
    LoadingSavedNavigationSpace: McoContextState
    NavigationObjectivesUpdated: McoContextState
    PlanLibraryUpdated: McoContextState
    ResettingToBalancedPlan: McoContextState
    SavedNavigationSpaceLoaded: McoContextState
    Undefined: McoContextState
    UpdatingNavigationObjectives: McoContextState
    UpdatingPlanLibrary: McoContextState

class MotorizedWedge(Wedge):
    """A motorized wedge is a standard wedge placed in the beam for a user-defined fraction of the total treatment time."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def CreationDateTime(self) -> Optional[datetime]:
        """Optional[datetime]: Property docstring."""
        ...

    @property
    def Direction(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def WedgeAngle(self) -> float:
        """float: Property docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class OmniWedge(Wedge):
    """An OmniWedge is a special type of wedge that combines an open field, a motorized wedge, and a virtual wedge to create the desired wedge effect."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def CreationDateTime(self) -> Optional[datetime]:
        """Optional[datetime]: Property docstring."""
        ...

    @property
    def Direction(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def WedgeAngle(self) -> float:
        """float: Property docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class OptimizationControllerBase(Generic[T, T1, T2]):
    """Class docstring."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    def Dispose(self) -> None:
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


class OptimizationControllerIMPT(OptimizationControllerBase[IProtonPlanSetup, IProtonCalculation, IProtonOptimizationClient]):
    """Controls the IMPT optimization from the Script"""

    def __init__(self, calculation: IProtonCalculation, planSetup: IProtonPlanSetup) -> None:
        """Initialize instance."""
        ...

    def Dispose(self) -> None:
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

    def Run(self, options: OptimizationOptionsIMPT) -> OptimizerResult:
        """Method docstring."""
        ...

    @overload
    def Run(self, maxIterations: int, optimizationOption: OptimizationOption) -> OptimizerResult:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...


class OptimizationControllerIMRT(OptimizationControllerBase[ExternalPlanSetup, IPhotonCalculation, IPhotonOptimizationClient]):
    """Controls the IMRT optimization from the Script"""

    def __init__(self, calculation: IPhotonCalculation, planSetup: ExternalPlanSetup) -> None:
        """Initialize instance."""
        ...

    def Dispose(self) -> None:
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

    def Run(self, maxIterations: int, options: OptimizationOptionsIMRT, intermediateDose: Dose) -> OptimizerResult:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...


class OptimizationControllerVMAT(OptimizationControllerBase[ExternalPlanSetup, IPhotonCalculation, IPhotonOptimizationClient]):
    """Controls the VMAT optimization from the Script"""

    def __init__(self, calculation: IPhotonCalculation, planSetup: ExternalPlanSetup) -> None:
        """Initialize instance."""
        ...

    def Dispose(self) -> None:
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

    def Run(self, options: OptimizationOptionsVMAT, intermediateDose: Dose) -> OptimizerResult:
        """Method docstring."""
        ...

    @overload
    def Run(self, mlcIdOrEmpty: str) -> OptimizerResult:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...


class OptimizationEUDObjective(OptimizationObjective):
    """A gEUD objective is an exact, upper or lower objective. An exact gEUD objective defines an exact dose value that a target structure should receive. An upper gEUD objective defines the maximum dose value that a structure should receive. A lower gEUD objective defines the minimum dose value that a target structure should receive. Generalized Equivalent Uniform Dose (gEUD) is a uniform dose that, if delivered over the same number of fractions, yields the same radiobiological effect as the non-uniform dose distribution of interest."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Dose(self) -> DoseValue:
        """DoseValue: The dose value for the objective."""
        ...

    @property
    def Operator(self) -> OptimizationObjectiveOperator:
        """OptimizationObjectiveOperator: Property docstring."""
        ...

    @property
    def ParameterA(self) -> float:
        """float: A tissue-specific parameter that illustrates the effect of the volume on the dose."""
        ...

    @property
    def Priority(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def Structure(self) -> Structure:
        """Structure: Property docstring."""
        ...

    @property
    def StructureId(self) -> str:
        """str: Property docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class OptimizationExcludeStructureParameter(OptimizationParameter):
    """Structures that have this parameter are excluded from the optimization."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Structure(self) -> Structure:
        """Structure: The structure to be excluded."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class OptimizationIMRTBeamParameter(OptimizationParameter):
    """Beam-specific optimization parameter for IMRT optimization."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Beam(self) -> Beam:
        """Beam: The beam to which this parameter belongs."""
        ...

    @property
    def BeamId(self) -> str:
        """str: The identifier of the beam."""
        ...

    @property
    def Excluded(self) -> bool:
        """bool: True if the beam is excluded from the optimization."""
        ...

    @property
    def FixedJaws(self) -> bool:
        """bool: If true, the collimator jaw positions of the beam remain the same during the optimization."""
        ...

    @property
    def SmoothX(self) -> float:
        """float: A smoothing parameter that controls the fluence profiles. A high value smoothes the fluence more than a low value."""
        ...

    @property
    def SmoothY(self) -> float:
        """float: A smoothing parameter that controls the fluence profiles. A high value smoothes the fluence more than a low value."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class OptimizationJawTrackingUsedParameter(OptimizationParameter):
    """An optimization parameter for using jaw tracking in VMAT optimization. The parameter exists if OptimizationSetup.UseJawTracking has been set to true."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class OptimizationLineObjective(OptimizationObjective):
    """A line objective is a collection of point objectives that have the same priority. It is used to limit the dose in a given structure."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def CurveData(self) -> Array[DVHPoint]:
        """Array[DVHPoint]: The points in the line objective."""
        ...

    @property
    def Operator(self) -> OptimizationObjectiveOperator:
        """OptimizationObjectiveOperator: Property docstring."""
        ...

    @property
    def Priority(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def Structure(self) -> Structure:
        """Structure: Property docstring."""
        ...

    @property
    def StructureId(self) -> str:
        """str: Property docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class OptimizationMeanDoseObjective(OptimizationObjective):
    """A mean objective defines the mean dose that should not be exceeded. The mean objective is used to decrease the dose that a structure receives."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Dose(self) -> DoseValue:
        """DoseValue: The dose value for the objective."""
        ...

    @property
    def Operator(self) -> OptimizationObjectiveOperator:
        """OptimizationObjectiveOperator: Property docstring."""
        ...

    @property
    def Priority(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def Structure(self) -> Structure:
        """Structure: Property docstring."""
        ...

    @property
    def StructureId(self) -> str:
        """str: Property docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class OptimizationNormalTissueParameter(OptimizationParameter):
    """An optimization parameter for the normal tissue objective."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def DistanceFromTargetBorderInMM(self) -> float:
        """float: Determines the distance in millimeters from the target border where the evaluation of the normal tissue objective dose begins."""
        ...

    @property
    def EndDosePercentage(self) -> float:
        """float: Determines the relative dose level in the normal tissue objective in the area furthest from the target border. Expressed in percentage. The value is positive. 100% is specified as 100."""
        ...

    @property
    def FallOff(self) -> float:
        """float: Determines the steepness of the normal tissue objective fall-off. The value is positive."""
        ...

    @property
    def IsAutomatic(self) -> bool:
        """bool: Returns True if an automatic normal tissue objective (NTO) is used.  The automatic NTO adapts to the patient anatomy and the optimization objectives, and automatically determines the dose fall-off criteria. When an automatic NTO is used, the other properties of this object, except Priority, are not used."""
        ...

    @property
    def IsAutomaticSbrt(self) -> bool:
        """bool: Returns True if an automatic SBRT normal tissue objective (NTO) is used. When an automatic SBRT NTO is used, the other properties of this object, except Priority, are not used."""
        ...

    @property
    def IsAutomaticSrs(self) -> bool:
        """bool: Returns True if an automatic SRS normal tissue objective (NTO) is used. When an automatic SRS NTO is used, the other properties of this object, except Priority, are not used."""
        ...

    @property
    def Priority(self) -> float:
        """float: Determines the relative importance of the normal tissue objective in relation to other optimization objectives. The value is positive."""
        ...

    @property
    def StartDosePercentage(self) -> float:
        """float: Determines the relative dose level in the normal tissue objective at the target border, expressed in percentage of the upper objective for the target. The value is positive. 100% is specified as 100."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class OptimizationObjective(SerializableObject):
    """Provides a common base type for all structure-specific optimization objectives."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Operator(self) -> OptimizationObjectiveOperator:
        """OptimizationObjectiveOperator: Specifies the type of the objective (upper, lower, exact)."""
        ...

    @property
    def Priority(self) -> float:
        """float: The priority of the objective as a positive double."""
        ...

    @property
    def Structure(self) -> Structure:
        """Structure: The structure to which this optimization objective belongs."""
        ...

    @property
    def StructureId(self) -> str:
        """str: The identifier of the structure."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Serves as a hash function for a particular type.
        
        Returns:
            int: A hash code for the current object."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class OptimizationOptionsVMATInternal(OptimizationOptionsVMAT):
    """Class docstring."""

    def __init__(self) -> None:
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
        """int: Property docstring."""
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


class OptimizationParameter(SerializableObject):
    """Provides a common base type for all optimization parameters."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Serves as a hash function for a particular type.
        
        Returns:
            int: A hash code for the current object."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class OptimizationPointCloudParameter(OptimizationParameter):
    """Structure-specific parameter for point cloud optimization. Relevant if the optimization algorithm uses a point cloud. The point cloud parameters are automatically created with default values when you add other structure-specific parameters or objectives in the optimization setup."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def PointResolutionInMM(self) -> float:
        """float: The point cloud resolution."""
        ...

    @property
    def Structure(self) -> Structure:
        """Structure: The structure whose parameters these are."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class OptimizationPointObjective(OptimizationObjective):
    """A point objective is either an upper or lower objective. An upper objective is used to limit the dose in a given structure. A lower objective is used to define the desired dose levels in target structures."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Dose(self) -> DoseValue:
        """DoseValue: The dose value for the objective."""
        ...

    @property
    def Operator(self) -> OptimizationObjectiveOperator:
        """OptimizationObjectiveOperator: Property docstring."""
        ...

    @property
    def Priority(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def Structure(self) -> Structure:
        """Structure: Property docstring."""
        ...

    @property
    def StructureId(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Volume(self) -> float:
        """float: Percentage of the structure volume (0-100 %) to receive the dose."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class OptimizationSetup(SerializableObject):
    """Gives access to the optimization parameters and objectives."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Objectives(self) -> List[OptimizationObjective]:
        """List[OptimizationObjective]: A collection of optimization objectives."""
        ...

    @property
    def Parameters(self) -> List[OptimizationParameter]:
        """List[OptimizationParameter]: A collection of optimization parameters."""
        ...

    @property
    def UseJawTracking(self) -> bool:
        """bool: [Availability of this property depends on your Eclipse Scripting API license] Jaw tracking parameter for VMAT optimization. The parameter can only be set for plans to be delivered with a treatment machine that supports jaw tracking."""
        ...

    @UseJawTracking.setter
    def UseJawTracking(self, value: bool) -> None:
        """Set property value."""
        ...

    def AddAutomaticNormalTissueObjective(self, priority: float) -> OptimizationNormalTissueParameter:
        """Method docstring."""
        ...

    def AddAutomaticSbrtNormalTissueObjective(self, priority: float) -> OptimizationNormalTissueParameter:
        """Method docstring."""
        ...

    def AddBeamSpecificParameter(self, beam: Beam, smoothX: float, smoothY: float, fixedJaws: bool) -> OptimizationIMRTBeamParameter:
        """Method docstring."""
        ...

    def AddEUDObjective(self, structure: Structure, objectiveOperator: OptimizationObjectiveOperator, dose: DoseValue, parameterA: float, priority: float) -> OptimizationEUDObjective:
        """Method docstring."""
        ...

    def AddMeanDoseObjective(self, structure: Structure, dose: DoseValue, priority: float) -> OptimizationMeanDoseObjective:
        """Method docstring."""
        ...

    def AddNormalTissueObjective(self, priority: float, distanceFromTargetBorderInMM: float, startDosePercentage: float, endDosePercentage: float, fallOff: float) -> OptimizationNormalTissueParameter:
        """Method docstring."""
        ...

    def AddPointObjective(self, structure: Structure, objectiveOperator: OptimizationObjectiveOperator, dose: DoseValue, volume: float, priority: float) -> OptimizationPointObjective:
        """Method docstring."""
        ...

    def AddProtonNormalTissueObjective(self, priority: float, distanceFromTargetBorderInMM: float, startDosePercentage: float, endDosePercentage: float) -> OptimizationNormalTissueParameter:
        """Method docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def ReadXml(self, reader: XmlReader) -> None:
        """Method docstring."""
        ...

    def RemoveObjective(self, objective: OptimizationObjective) -> None:
        """Method docstring."""
        ...

    def RemoveParameter(self, parameter: OptimizationParameter) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    def WriteXml(self, writer: XmlWriter) -> None:
        """Method docstring."""
        ...


class OptimizationVMATAvoidanceSectors(OptimizationParameter):
    """Beam-specific optimization parameter for VMAT Avoidance sectors."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def AvoidanceSector1(self) -> OptimizationAvoidanceSector:
        """OptimizationAvoidanceSector: Avoidance Sector 1."""
        ...

    @property
    def AvoidanceSector2(self) -> OptimizationAvoidanceSector:
        """OptimizationAvoidanceSector: Avoidance Sector 2."""
        ...

    @property
    def Beam(self) -> Beam:
        """Beam: The beam to which this parameter belongs."""
        ...

    @property
    def IsValid(self) -> bool:
        """bool: Is Avoidance Sectors valid."""
        ...

    @property
    def ValidationError(self) -> str:
        """str: Validation error if any."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class OptimizerDVH:
    """Contains a structure-specific Dose Volume Histogram (DVH) curve generated in optimization."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def CurveData(self) -> Array[DVHPoint]:
        """Array[DVHPoint]: An array of DVH points representing the DVH curve data."""
        ...

    @property
    def Structure(self) -> Structure:
        """Structure: The corresponding structure for the DVH curve data."""
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


class OptimizerObjectiveValue:
    """The optimizer objective function value for the structure."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Structure(self) -> Structure:
        """Structure: The corresponding structure for the objective function value."""
        ...

    @property
    def Value(self) -> float:
        """float: The objective function value."""
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


class OptimizerResult(CalculationResult):
    """Holds the result of the optimization (pass/fail)."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def NumberOfIMRTOptimizerIterations(self) -> int:
        """int: The number of iterations taken by the IMRT optimizer."""
        ...

    @NumberOfIMRTOptimizerIterations.setter
    def NumberOfIMRTOptimizerIterations(self, value: int) -> None:
        """Set property value."""
        ...

    @property
    def StructureDVHs(self) -> List[OptimizerDVH]:
        """List[OptimizerDVH]: A list of Dose Volume Histogram (DVH) curves for structures."""
        ...

    @property
    def StructureObjectiveValues(self) -> List[OptimizerObjectiveValue]:
        """List[OptimizerObjectiveValue]: The list of objective function values per structure."""
        ...

    @property
    def Success(self) -> bool:
        """bool: Property docstring."""
        ...

    @property
    def TotalObjectiveFunctionValue(self) -> float:
        """float: The total objective function value for the optimization."""
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


class Patient(ApiDataObject):
    """Represents a patient."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Courses(self) -> List[Course]:
        """List[Course]: A collection of the patient's courses."""
        ...

    @property
    def CreationDateTime(self) -> Optional[datetime]:
        """Optional[datetime]: The date when this object was created."""
        ...

    @property
    def DateOfBirth(self) -> Optional[datetime]:
        """Optional[datetime]: The date of birth of the patient."""
        ...

    @property
    def DefaultDepartment(self) -> str:
        """str: The default department name."""
        ...

    @property
    def FirstName(self) -> str:
        """str: The first name of the patient."""
        ...

    @FirstName.setter
    def FirstName(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def HasModifiedData(self) -> bool:
        """bool: Returns true if the patient object tree has been modified."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Hospital(self) -> Hospital:
        """Hospital: The hospital."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id2(self) -> str:
        """str: The patient ID2."""
        ...

    @property
    def LastName(self) -> str:
        """str: The last name of the patient."""
        ...

    @LastName.setter
    def LastName(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def MiddleName(self) -> str:
        """str: The middle name of the patient."""
        ...

    @MiddleName.setter
    def MiddleName(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def PrimaryOncologistId(self) -> str:
        """str: The identifier of the primary oncologist."""
        ...

    @property
    def PrimaryOncologistName(self) -> str:
        """str: The primary oncologist name."""
        ...

    @property
    def ReferencePoints(self) -> List[ReferencePoint]:
        """List[ReferencePoint]: Collection of all reference points for the patient."""
        ...

    @property
    def Registrations(self) -> List[Registration]:
        """List[Registration]: A collection of registrations."""
        ...

    @property
    def SSN(self) -> str:
        """str: The Social Security Account Number (SSN) of the patient."""
        ...

    @property
    def Sex(self) -> str:
        """str: The gender of the patient."""
        ...

    @property
    def StructureSets(self) -> List[StructureSet]:
        """List[StructureSet]: A collection of structure sets."""
        ...

    @property
    def Studies(self) -> List[Study]:
        """List[Study]: A collection of studies."""
        ...

    def AddCourse(self) -> Course:
        """[Availability of this method depends on your Eclipse Scripting API license] Attaches a new course to this patient.
        
        Returns:
            Course: The new course."""
        ...

    def AddEmptyPhantom(self, imageId: str, orientation: PatientOrientation, xSizePixel: int, ySizePixel: int, widthMM: float, heightMM: float, nrOfPlanes: int, planeSepMM: float) -> StructureSet:
        """Method docstring."""
        ...

    def AddReferencePoint(self, target: bool, id: str) -> ReferencePoint:
        """Method docstring."""
        ...

    def BeginModifications(self) -> None:
        """Enables write-access to the data model from the Scripting API. This function must be called for each patient the script modifies. If this function is not called, the data in the database cannot be modified.
        
        The method"""
        ...

    def CanAddCourse(self) -> bool:
        """Checks if a new course can be added to the patient.
        
        Returns:
            bool: true if a new course can be added to the patient."""
        ...

    def CanAddEmptyPhantom(self, errorMessage: str) -> bool:
        """Method docstring."""
        ...

    def CanCopyImageFromOtherPatient(self, targetStudy: Study, otherPatientId: str, otherPatientStudyId: str, otherPatient3DImageId: str, errorMessage: str) -> bool:
        """Method docstring."""
        ...

    def CanModifyData(self) -> bool:
        """Returns true if the script can modify patient data in the database.
        
        Returns:
            bool: true if the script can modify patient data in the database. Otherwise false."""
        ...

    def CanRemoveCourse(self, course: Course) -> bool:
        """Method docstring."""
        ...

    def CanRemoveEmptyPhantom(self, structureset: StructureSet, errorMessage: str) -> bool:
        """Method docstring."""
        ...

    def CopyImageFromOtherPatient(self, otherPatientId: str, otherPatientStudyId: str, otherPatient3DImageId: str) -> StructureSet:
        """Method docstring."""
        ...

    @overload
    def CopyImageFromOtherPatient(self, targetStudy: Study, otherPatientId: str, otherPatientStudyId: str, otherPatient3DImageId: str) -> StructureSet:
        """Method docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def ReadXml(self, reader: XmlReader) -> None:
        """Method docstring."""
        ...

    def RemoveCourse(self, course: Course) -> None:
        """Method docstring."""
        ...

    def RemoveEmptyPhantom(self, structureset: StructureSet) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    def WriteXml(self, writer: XmlWriter) -> None:
        """Method docstring."""
        ...


class PatientSummary(SerializableObject):
    """Basic information about the patient."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def CreationDateTime(self) -> Optional[datetime]:
        """Optional[datetime]: The date when the patient object was created."""
        ...

    @property
    def DateOfBirth(self) -> Optional[datetime]:
        """Optional[datetime]: The date of birth of the patient."""
        ...

    @property
    def FirstName(self) -> str:
        """str: The first name of the patient."""
        ...

    @property
    def Id(self) -> str:
        """str: The patient ID."""
        ...

    @property
    def Id2(self) -> str:
        """str: The patient ID2."""
        ...

    @property
    def LastName(self) -> str:
        """str: The last name of the patient."""
        ...

    @property
    def MiddleName(self) -> str:
        """str: The middle name of the patient."""
        ...

    @property
    def SSN(self) -> str:
        """str: The Social Security Account Number (SSN) of the patient."""
        ...

    @property
    def Sex(self) -> str:
        """str: The gender of the patient."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class PatientSupportDevice(ApiDataObject):
    """Represents a proton patient support device."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def PatientSupportAccessoryCode(self) -> str:
        """str: Patient support device accessory code."""
        ...

    @property
    def PatientSupportDeviceType(self) -> str:
        """str: Type of the patient support device."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class PlanSetup(PlanningItem):
    """Represents a treatment plan. See the definition of a DICOM RT Plan for more information."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def ApplicationScriptLogs(self) -> List[ApplicationScriptLog]:
        """List[ApplicationScriptLog]: The log entries of the script executions that have modified the plan."""
        ...

    @property
    def ApprovalHistory(self) -> List[ApprovalHistoryEntry]:
        """List[ApprovalHistoryEntry]: Returns the approval history of the plan setup."""
        ...

    @property
    def ApprovalStatus(self) -> PlanSetupApprovalStatus:
        """PlanSetupApprovalStatus: The approval status."""
        ...

    @property
    def ApprovalStatusAsString(self) -> str:
        """str: Returns the approval status as a string (localized)."""
        ...

    @property
    def BaseDosePlanningItem(self) -> PlanningItem:
        """PlanningItem: BaseDose for the optimization, can be either plan or plan sum."""
        ...

    @BaseDosePlanningItem.setter
    def BaseDosePlanningItem(self, value: PlanningItem) -> None:
        """Set property value."""
        ...

    @property
    def Beams(self) -> List[Beam]:
        """List[Beam]: A collection of all the beams in the plan (including setup beams). Returns an empty collection if not applicable for the plan, for example, if the plan is a brachytherapy plan."""
        ...

    @property
    def BeamsInTreatmentOrder(self) -> List[Beam]:
        """List[Beam]: A collection of all the beams in the plan (including setup beams) in treatment order. Returns an empty collection if not applicable for the plan, for example, if the plan is a brachytherapy plan."""
        ...

    @property
    def Comment(self) -> str:
        """str: [Availability of this property depends on your Eclipse Scripting API license] A comment about the Plan."""
        ...

    @Comment.setter
    def Comment(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def Course(self) -> Course:
        """Course: Property docstring."""
        ...

    @property
    def CreationDateTime(self) -> Optional[datetime]:
        """Optional[datetime]: Property docstring."""
        ...

    @property
    def CreationUserName(self) -> str:
        """str: The name of the user who saved the plan for the first time."""
        ...

    @property
    def DVHEstimates(self) -> List[EstimatedDVH]:
        """List[EstimatedDVH]: Returns a list of DVH estimate objects for this plan"""
        ...

    @property
    def Dose(self) -> PlanningItemDose:
        """PlanningItemDose: Property docstring."""
        ...

    @property
    def DosePerFraction(self) -> DoseValue:
        """DoseValue: The dose per fraction."""
        ...

    @property
    def DosePerFractionInPrimaryRefPoint(self) -> DoseValue:
        """DoseValue: The calculated fraction dose in the primary reference point."""
        ...

    @property
    def DoseValuePresentation(self) -> DoseValuePresentation:
        """DoseValuePresentation: Property docstring."""
        ...

    @DoseValuePresentation.setter
    def DoseValuePresentation(self, value: DoseValuePresentation) -> None:
        """Set property value."""
        ...

    @property
    def ElectronCalculationModel(self) -> str:
        """str: The name of the electron calculation model. Not applicable to brachytherapy plans."""
        ...

    @property
    def ElectronCalculationOptions(self) -> Dict[str, str]:
        """Dict[str, str]: The electron calculation options. Not applicable to brachytherapy plans."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: [Availability of this property depends on your Eclipse Scripting API license] The identifier of the PlanSetup."""
        ...

    @Id.setter
    def Id(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def IntegrityHash(self) -> str:
        """str: Returns the plan's integrity hash. Returns null if the plan's integrity hash has not been set."""
        ...

    @property
    def IsDoseValid(self) -> bool:
        """bool: Returns the value true if the plan dose is valid. This implies that the dose object returned from the dose property is not null and can therefore be used to query dose values."""
        ...

    @property
    def IsTreated(self) -> bool:
        """bool: Checks if the treatment plan has been delivered."""
        ...

    @property
    def Name(self) -> str:
        """str: [Availability of this property depends on your Eclipse Scripting API license] The name of the Plan."""
        ...

    @Name.setter
    def Name(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def NumberOfFractions(self) -> Optional[int]:
        """Optional[int]: The number of fractions."""
        ...

    @property
    def OptimizationSetup(self) -> OptimizationSetup:
        """OptimizationSetup: Provides access to optimization objectives and parameters."""
        ...

    @property
    def PatientSupportDevice(self) -> PatientSupportDevice:
        """PatientSupportDevice: Patient support device."""
        ...

    @property
    def PhotonCalculationModel(self) -> str:
        """str: The name of the photon calculation model. Not applicable to brachytherapy plans."""
        ...

    @property
    def PhotonCalculationOptions(self) -> Dict[str, str]:
        """Dict[str, str]: The photon calculation options. Not applicable to brachytherapy plans."""
        ...

    @property
    def PlanIntent(self) -> str:
        """str: The plan intent as in DICOM, or an empty string. The defined terms are "CURATIVE", "PALLIATIVE", "PROPHYLACTIC", "VERIFICATION", "MACHINE_QA", "RESEARCH" and "SERVICE", but the value can be different for imported plans."""
        ...

    @property
    def PlanIsInTreatment(self) -> bool:
        """bool: Checks if plan is loaded into console."""
        ...

    @property
    def PlanNormalizationMethod(self) -> str:
        """str: The user interface name for the current normalization method."""
        ...

    @property
    def PlanNormalizationPoint(self) -> VVector:
        """VVector: The plan normalization point."""
        ...

    @property
    def PlanNormalizationValue(self) -> float:
        """float: [Availability of this property depends on your Eclipse Scripting API license] The plan normalization value in percentage. The plan is normalized according to the plan normalization value, for instance, 200%. The value is Double.NaN if it is not defined."""
        ...

    @PlanNormalizationValue.setter
    def PlanNormalizationValue(self, value: float) -> None:
        """Set property value."""
        ...

    @property
    def PlanObjectiveStructures(self) -> List[str]:
        """List[str]: The list of structure IDs that are present in the plan objectives (prescriptions and indices)."""
        ...

    @property
    def PlanType(self) -> PlanType:
        """PlanType: The plan type."""
        ...

    @property
    def PlanUncertainties(self) -> List[PlanUncertainty]:
        """List[PlanUncertainty]: Plan uncertainties defined for the plan."""
        ...

    @property
    def PlannedDosePerFraction(self) -> DoseValue:
        """DoseValue: The calculated fraction dose in the primary reference point."""
        ...

    @property
    def PlanningApprovalDate(self) -> str:
        """str: The date when the plan was approved for planning."""
        ...

    @property
    def PlanningApprover(self) -> str:
        """str: The identifier of the user who approved the plan for planning."""
        ...

    @property
    def PlanningApproverDisplayName(self) -> str:
        """str: The display name of the user who approved the plan for planning."""
        ...

    @property
    def PredecessorPlan(self) -> PlanSetup:
        """PlanSetup: The prior revision of the plan"""
        ...

    @property
    def PredecessorPlanUID(self) -> str:
        """str: The UID of the predecessor plan."""
        ...

    @property
    def PrescribedDosePerFraction(self) -> DoseValue:
        """DoseValue: The prescribed fraction dose."""
        ...

    @property
    def PrescribedPercentage(self) -> float:
        """float: The prescribed dose percentage as a decimal number. For example, if the prescribed dose percentage shown in the Eclipse user interface is 80 %, returns 0.8"""
        ...

    @property
    def PrimaryReferencePoint(self) -> ReferencePoint:
        """ReferencePoint: The primary reference point."""
        ...

    @property
    def ProtocolID(self) -> str:
        """str: The protocol identifier."""
        ...

    @property
    def ProtocolPhaseID(self) -> str:
        """str: The protocol phase identifier."""
        ...

    @property
    def ProtonCalculationModel(self) -> str:
        """str: The name of the proton calculation model. Not applicable to brachytherapy plans."""
        ...

    @property
    def ProtonCalculationOptions(self) -> Dict[str, str]:
        """Dict[str, str]: The proton calculation options. Not applicable to brachytherapy plans."""
        ...

    @property
    def RTPrescription(self) -> RTPrescription:
        """RTPrescription: Used for navigating to the linked prescription."""
        ...

    @property
    def ReferencePoints(self) -> List[ReferencePoint]:
        """List[ReferencePoint]: Collection of reference points in the plan."""
        ...

    @property
    def Series(self) -> Series:
        """Series: The series that contains this plan. Null if the plan is not connected to a series."""
        ...

    @property
    def SeriesUID(self) -> str:
        """str: The DICOM UID of the series that contains this plan. Empty string if the plan is not connected to a series."""
        ...

    @property
    def StructureSet(self) -> StructureSet:
        """StructureSet: Property docstring."""
        ...

    @property
    def StructuresSelectedForDvh(self) -> List[Structure]:
        """List[Structure]: Property docstring."""
        ...

    @property
    def TargetVolumeID(self) -> str:
        """str: The target volume identifier."""
        ...

    @property
    def TotalDose(self) -> DoseValue:
        """DoseValue: Planned total dose."""
        ...

    @property
    def TotalPrescribedDose(self) -> DoseValue:
        """DoseValue: The total prescribed dose."""
        ...

    @property
    def TreatmentApprovalDate(self) -> str:
        """str: The date when the plan was approved for treatment."""
        ...

    @property
    def TreatmentApprover(self) -> str:
        """str: The identifier of the user who approved the plan for treatment."""
        ...

    @property
    def TreatmentApproverDisplayName(self) -> str:
        """str: The display name of the user who approved the plan for treatment."""
        ...

    @property
    def TreatmentOrientation(self) -> PatientOrientation:
        """PatientOrientation: The orientation of the treatment."""
        ...

    @property
    def TreatmentOrientationAsString(self) -> str:
        """str: The orientation of the treatment as a string (localized)."""
        ...

    @property
    def TreatmentPercentage(self) -> float:
        """float: The treatment percentage as a decimal number. For example, if the treatment percentage shown in the Eclipse user interface is 80%, returns 0.8."""
        ...

    @property
    def TreatmentSessions(self) -> List[PlanTreatmentSession]:
        """List[PlanTreatmentSession]: Treatment sessions for the plan, either scheduled sessions or treated sessions."""
        ...

    @property
    def UID(self) -> str:
        """str: The DICOM UID of the plan."""
        ...

    @property
    def UseGating(self) -> bool:
        """bool: Boolean to mark if gating is used in the plan."""
        ...

    @UseGating.setter
    def UseGating(self, value: bool) -> None:
        """Set property value."""
        ...

    @property
    def VerifiedPlan(self) -> PlanSetup:
        """PlanSetup: Returns the verified plan if this is a verification plan, otherwise returns null. The verified plan is the clinical plan that was used to create the verification plan."""
        ...

    def AddPlanUncertaintyWithParameters(self, uncertaintyType: PlanUncertaintyType, planSpecificUncertainty: bool, HUConversionError: float, isocenterShift: VVector) -> PlanUncertainty:
        """Method docstring."""
        ...

    def AddReferencePoint(self, target: bool, location: Optional[VVector], id: str) -> ReferencePoint:
        """Method docstring."""
        ...

    @overload
    def AddReferencePoint(self, refPoint: ReferencePoint) -> None:
        """Method docstring."""
        ...

    def ClearCalculationModel(self, calculationType: CalculationType) -> None:
        """Method docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetCalculationModel(self, calculationType: CalculationType) -> str:
        """Method docstring."""
        ...

    def GetCalculationOption(self, calculationModel: str, optionName: str, optionValue: str) -> bool:
        """Method docstring."""
        ...

    def GetCalculationOptions(self, calculationModel: str) -> Dict[str, str]:
        """Method docstring."""
        ...

    def GetClinicalGoals(self) -> List[ClinicalGoal]:
        """Method docstring."""
        ...

    def GetDVHCumulativeData(self, structure: Structure, dosePresentation: DoseValuePresentation, volumePresentation: VolumePresentation, binWidth: float) -> DVHData:
        """Method docstring."""
        ...

    def GetDoseAtVolume(self, structure: Structure, volume: float, volumePresentation: VolumePresentation, requestedDosePresentation: DoseValuePresentation) -> DoseValue:
        """Method docstring."""
        ...

    def GetDvhEstimationModelName(self) -> str:
        """Retrieves the name of DVH Estimation Model."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetProtocolPrescriptionsAndMeasures(self, prescriptions: List, measures: List) -> None:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def GetVolumeAtDose(self, structure: Structure, dose: DoseValue, requestedVolumePresentation: VolumePresentation) -> float:
        """Method docstring."""
        ...

    def IsEntireBodyAndBolusesCoveredByCalculationArea(self) -> bool:
        """Checks the limits of the current calculation area.
        
        Returns:
            bool: True if calculation area covers entire body or, if no body defined, image."""
        ...

    def IsValidForPlanApproval(self, validationResults: List) -> bool:
        """Method docstring."""
        ...

    def MoveToCourse(self, destinationCourse: Course) -> None:
        """Method docstring."""
        ...

    def ReadXml(self, reader: XmlReader) -> None:
        """Method docstring."""
        ...

    def RemoveReferencePoint(self, refPoint: ReferencePoint) -> None:
        """Method docstring."""
        ...

    def SetCalculationModel(self, calculationType: CalculationType, model: str) -> None:
        """Method docstring."""
        ...

    def SetCalculationOption(self, calculationModel: str, optionName: str, optionValue: str) -> bool:
        """Method docstring."""
        ...

    def SetPrescription(self, numberOfFractions: int, dosePerFraction: DoseValue, treatmentPercentage: float) -> None:
        """Method docstring."""
        ...

    def SetTargetStructureIfNoDose(self, newTargetStructure: Structure, errorHint: StringBuilder) -> bool:
        """Method docstring."""
        ...

    def SetTreatmentOrder(self, orderedBeams: List[Beam]) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    def WriteXml(self, writer: XmlWriter) -> None:
        """Method docstring."""
        ...


class PlanSum(PlanningItem):
    """A plan sum describes the cumulative dose summation of several treatment plans. It can be used, for example, to evaluate the dose the patient received from a treatment plan and boost plan together."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Course(self) -> Course:
        """Course: Property docstring."""
        ...

    @property
    def CreationDateTime(self) -> Optional[datetime]:
        """Optional[datetime]: Property docstring."""
        ...

    @property
    def Dose(self) -> PlanningItemDose:
        """PlanningItemDose: Property docstring."""
        ...

    @property
    def DoseValuePresentation(self) -> DoseValuePresentation:
        """DoseValuePresentation: Property docstring."""
        ...

    @DoseValuePresentation.setter
    def DoseValuePresentation(self, value: DoseValuePresentation) -> None:
        """Set property value."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: [Availability of this property depends on your Eclipse Scripting API license] The identifier of the PlanSum."""
        ...

    @Id.setter
    def Id(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def Name(self) -> str:
        """str: [Availability of this property depends on your Eclipse Scripting API license] The name of the PlanSum."""
        ...

    @Name.setter
    def Name(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def PlanSetups(self) -> List[PlanSetup]:
        """List[PlanSetup]: A collection of plan setups."""
        ...

    @property
    def PlanSumComponents(self) -> List[PlanSumComponent]:
        """List[PlanSumComponent]: A collection of plans in a plan sum."""
        ...

    @property
    def StructureSet(self) -> StructureSet:
        """StructureSet: Property docstring."""
        ...

    @property
    def StructuresSelectedForDvh(self) -> List[Structure]:
        """List[Structure]: Property docstring."""
        ...

    def AddItem(self, pi: PlanningItem) -> None:
        """Method docstring."""
        ...

    @overload
    def AddItem(self, pi: PlanningItem, operation: PlanSumOperation, planWeight: float) -> None:
        """Method docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetClinicalGoals(self) -> List[ClinicalGoal]:
        """Method docstring."""
        ...

    def GetDVHCumulativeData(self, structure: Structure, dosePresentation: DoseValuePresentation, volumePresentation: VolumePresentation, binWidth: float) -> DVHData:
        """Method docstring."""
        ...

    def GetDoseAtVolume(self, structure: Structure, volume: float, volumePresentation: VolumePresentation, requestedDosePresentation: DoseValuePresentation) -> DoseValue:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetPlanSumOperation(self, planSetupInPlanSum: PlanSetup) -> PlanSumOperation:
        """Method docstring."""
        ...

    def GetPlanWeight(self, planSetupInPlanSum: PlanSetup) -> float:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def GetVolumeAtDose(self, structure: Structure, dose: DoseValue, requestedVolumePresentation: VolumePresentation) -> float:
        """Method docstring."""
        ...

    def ReadXml(self, reader: XmlReader) -> None:
        """Method docstring."""
        ...

    def RemoveItem(self, pi: PlanningItem) -> None:
        """Method docstring."""
        ...

    def SetPlanSumOperation(self, planSetupInPlanSum: PlanSetup, operation: PlanSumOperation) -> None:
        """Method docstring."""
        ...

    def SetPlanWeight(self, planSetupInPlanSum: PlanSetup, weight: float) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    def WriteXml(self, writer: XmlWriter) -> None:
        """Method docstring."""
        ...


class PlanSumComponent(ApiDataObject):
    """Represents a component plan of a plan sum."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def PlanSetupId(self) -> str:
        """str: The unique identification of the plan within the course."""
        ...

    @property
    def PlanSumOperation(self) -> PlanSumOperation:
        """PlanSumOperation: The summing operation (+ or -) that defines how the dose of a component plan contributes to the plan sum."""
        ...

    @property
    def PlanWeight(self) -> float:
        """float: The weight of a component plan included in the plan sum."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class PlanTreatmentSession(ApiDataObject):
    """Plan in the treatment session."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def PlanSetup(self) -> PlanSetup:
        """PlanSetup: Scheduled or treated plan."""
        ...

    @property
    def Status(self) -> TreatmentSessionStatus:
        """TreatmentSessionStatus: Plan status in the treatment session."""
        ...

    @property
    def TreatmentSession(self) -> TreatmentSession:
        """TreatmentSession: Treatment session."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class PlanUncertainty(ApiDataObject):
    """Provides access to Plan Uncertainty parameters. For more information, see Eclipse Photon and Electron Instructions for Use."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def BeamUncertainties(self) -> List[BeamUncertainty]:
        """List[BeamUncertainty]: Collection of beam uncertainty doses."""
        ...

    @property
    def CalibrationCurveError(self) -> float:
        """float: The calibration curve error of the plan uncertainty in percentage. Returns 100 for 100%. NaN if not defined."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def DisplayName(self) -> str:
        """str: The display name of the plan variation, including the parameter values."""
        ...

    @property
    def Dose(self) -> Dose:
        """Dose: The dose of this plan variation."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def IsocenterShift(self) -> VVector:
        """VVector: The isocenter shift of the plan uncertainty."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def UncertaintyType(self) -> PlanUncertaintyType:
        """PlanUncertaintyType: Type of uncertainty, which determines how and in what context the defined parameters are to be used."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetDVHCumulativeData(self, structure: Structure, dosePresentation: DoseValuePresentation, volumePresentation: VolumePresentation, binWidth: float) -> DVHData:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class PlanningItem(ApiDataObject):
    """Common properties of a treatment plan and a plan sum."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Course(self) -> Course:
        """Course: Used for navigating to parent course."""
        ...

    @property
    def CreationDateTime(self) -> Optional[datetime]:
        """Optional[datetime]: The date when this object was created."""
        ...

    @property
    def Dose(self) -> PlanningItemDose:
        """PlanningItemDose: The total dose. The total dose is the dose of all planned fractions together."""
        ...

    @property
    def DoseValuePresentation(self) -> DoseValuePresentation:
        """DoseValuePresentation: The presentation of the dose as absolute or relative."""
        ...

    @DoseValuePresentation.setter
    def DoseValuePresentation(self, value: DoseValuePresentation) -> None:
        """Set property value."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def StructureSet(self) -> StructureSet:
        """StructureSet: The structure set."""
        ...

    @property
    def StructuresSelectedForDvh(self) -> List[Structure]:
        """List[Structure]: The collection of the structures that have been selected for DVH evaluation in Eclipse."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetClinicalGoals(self) -> List[ClinicalGoal]:
        """Get the list of clinical goals assigned to a planning item.
        
        Returns:
            List[ClinicalGoal]: The list of clinical goals attached to the plan."""
        ...

    def GetDVHCumulativeData(self, structure: Structure, dosePresentation: DoseValuePresentation, volumePresentation: VolumePresentation, binWidth: float) -> DVHData:
        """Method docstring."""
        ...

    def GetDoseAtVolume(self, structure: Structure, volume: float, volumePresentation: VolumePresentation, requestedDosePresentation: DoseValuePresentation) -> DoseValue:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def GetVolumeAtDose(self, structure: Structure, dose: DoseValue, requestedVolumePresentation: VolumePresentation) -> float:
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


class PlanningItemDose(Dose):
    """Represents a dose that is connected to a plan setup or a plan sum."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def DoseMax3D(self) -> DoseValue:
        """DoseValue: Property docstring."""
        ...

    @property
    def DoseMax3DLocation(self) -> VVector:
        """VVector: Property docstring."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Isodoses(self) -> List[Isodose]:
        """List[Isodose]: Property docstring."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Origin(self) -> VVector:
        """VVector: Property docstring."""
        ...

    @property
    def Series(self) -> Series:
        """Series: Property docstring."""
        ...

    @property
    def SeriesUID(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def UID(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def XDirection(self) -> VVector:
        """VVector: Property docstring."""
        ...

    @property
    def XRes(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def XSize(self) -> int:
        """int: Property docstring."""
        ...

    @property
    def YDirection(self) -> VVector:
        """VVector: Property docstring."""
        ...

    @property
    def YRes(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def YSize(self) -> int:
        """int: Property docstring."""
        ...

    @property
    def ZDirection(self) -> VVector:
        """VVector: Property docstring."""
        ...

    @property
    def ZRes(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def ZSize(self) -> int:
        """int: Property docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetDoseProfile(self, start: VVector, stop: VVector, preallocatedBuffer: Array[float]) -> DoseProfile:
        """Method docstring."""
        ...

    def GetDoseToPoint(self, at: VVector) -> DoseValue:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def GetVoxels(self, planeIndex: int, preallocatedBuffer: Array[int]) -> None:
        """Method docstring."""
        ...

    def ReadXml(self, reader: XmlReader) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    def VoxelToDoseValue(self, voxelValue: int) -> DoseValue:
        """Method docstring."""
        ...

    def WriteXml(self, writer: XmlWriter) -> None:
        """Method docstring."""
        ...


class ProtocolPhaseMeasure(SerializableObject):
    """Represents the plan measures (quality indices) of the clinical protocol."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def ActualValue(self) -> float:
        """float: The calculated actual value of this plan measure."""
        ...

    @property
    def Modifier(self) -> MeasureModifier:
        """MeasureModifier: Measure Modifier."""
        ...

    @property
    def StructureId(self) -> str:
        """str: ID of the structure to which this measure is applied."""
        ...

    @property
    def TargetIsMet(self) -> Optional[bool]:
        """Optional[bool]: Indicates whether the target is met. If this cannot be evaluated, the value is null."""
        ...

    @property
    def TargetValue(self) -> float:
        """float: The target value of this plan measure."""
        ...

    @property
    def Type(self) -> MeasureType:
        """MeasureType: Measure Type."""
        ...

    @property
    def TypeText(self) -> str:
        """str: Measure type as text, for instance, 'Conformity Index' in 'Conformity Index is more than 10.0'."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class ProtocolPhasePrescription(SerializableObject):
    """Represents the prescriptions (plan objectives) of the clinical protocol."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def ActualTotalDose(self) -> DoseValue:
        """DoseValue: Actual total dose for this prescription"""
        ...

    @property
    def PrescModifier(self) -> PrescriptionModifier:
        """PrescriptionModifier: Prescription Modifier."""
        ...

    @property
    def PrescParameter(self) -> float:
        """float: Value of the prescription parameter, for instance, '80' in 'At least 80% receives more than 2 Gy'."""
        ...

    @property
    def PrescType(self) -> PrescriptionType:
        """PrescriptionType: Prescription Type."""
        ...

    @property
    def StructureId(self) -> str:
        """str: ID of structure to which this prescription is applied."""
        ...

    @property
    def TargetFractionDose(self) -> DoseValue:
        """DoseValue: Fraction dose in absolute units specified for this prescription."""
        ...

    @property
    def TargetIsMet(self) -> Optional[bool]:
        """Optional[bool]: Indicates whether the target is met. If this cannot be evaluated, the value is null."""
        ...

    @property
    def TargetTotalDose(self) -> DoseValue:
        """DoseValue: Total dose in absolute units specified for this prescription."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class RTPrescription(ApiDataObject):
    """Represents a prescription."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def BolusFrequency(self) -> str:
        """str: Bolus frequency (how often the bolus is present in the field). For example, daily."""
        ...

    @property
    def BolusThickness(self) -> str:
        """str: Thickness of the bolus to be used."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Energies(self) -> List[str]:
        """List[str]: The energies in the prescription."""
        ...

    @property
    def EnergyModes(self) -> List[str]:
        """List[str]: The energy modes in the prescription."""
        ...

    @property
    def Gating(self) -> str:
        """str: Gating information."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def LatestRevision(self) -> RTPrescription:
        """RTPrescription: Gets the latest revision of the current RT prescription."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Notes(self) -> str:
        """str: Additional notes."""
        ...

    @property
    def NumberOfFractions(self) -> Optional[int]:
        """Optional[int]: Number of fractions, optional."""
        ...

    @property
    def OrgansAtRisk(self) -> List[RTPrescriptionOrganAtRisk]:
        """List[RTPrescriptionOrganAtRisk]: Gets the organs at risk of the current RT prescription."""
        ...

    @property
    def PhaseType(self) -> str:
        """str: Type of the phase (primary/boost)."""
        ...

    @property
    def PredecessorPrescription(self) -> RTPrescription:
        """RTPrescription: Gets the previous version of the RT prescription if it exists."""
        ...

    @property
    def RevisionNumber(self) -> int:
        """int: Revision number of the prescription."""
        ...

    @property
    def SimulationNeeded(self) -> Optional[bool]:
        """Optional[bool]: Indicates if simulations need to be done before treatment planning."""
        ...

    @property
    def Site(self) -> str:
        """str: The treatment site in the prescription."""
        ...

    @property
    def Status(self) -> str:
        """str: Prescription status."""
        ...

    @property
    def TargetConstraintsWithoutTargetLevel(self) -> List[RTPrescriptionTargetConstraints]:
        """List[RTPrescriptionTargetConstraints]: Coverage constraints for targets with no prescribed dose."""
        ...

    @property
    def Targets(self) -> List[RTPrescriptionTarget]:
        """List[RTPrescriptionTarget]: Gets the targets of the current prescription."""
        ...

    @property
    def Technique(self) -> str:
        """str: Treatment technique to be used."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class RTPrescriptionConstraint(SerializableObject):
    """Represents a coverage constraint for an RT prescription."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def ConstraintType(self) -> RTPrescriptionConstraintType:
        """RTPrescriptionConstraintType: Type of the constraint."""
        ...

    @property
    def Unit1(self) -> str:
        """str: Gy, %, or null"""
        ...

    @property
    def Unit2(self) -> str:
        """str: Gy, %, or null"""
        ...

    @property
    def Value1(self) -> str:
        """str: First numerical (or free text) part of the constraint."""
        ...

    @property
    def Value2(self) -> str:
        """str: Second numerical (or free text) part of the constraint."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class RTPrescriptionOrganAtRisk(SerializableObject):
    """Represents an organ at risk structure."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Constraints(self) -> List[RTPrescriptionConstraint]:
        """List[RTPrescriptionConstraint]: Constraints."""
        ...

    @property
    def OrganAtRiskId(self) -> str:
        """str: Structure identifier of the organ at risk."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class RTPrescriptionTarget(ApiDataObject):
    """Represents a prescription target."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Constraints(self) -> List[RTPrescriptionConstraint]:
        """List[RTPrescriptionConstraint]: Coverage constraints."""
        ...

    @property
    def DosePerFraction(self) -> DoseValue:
        """DoseValue: Dose per fraction for this target."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def NumberOfFractions(self) -> int:
        """int: The number of fractions in the prescription."""
        ...

    @property
    def TargetId(self) -> str:
        """str: The ID of the target volume."""
        ...

    @property
    def Type(self) -> RTPrescriptionTargetType:
        """RTPrescriptionTargetType: Type of the prescription target. It can be Isocenter, IsodoseLine, Volume or Depth."""
        ...

    @property
    def Value(self) -> float:
        """float: Defined when the target type is IsodoseLine or Depth. Unit is % for IsodoseLine or mm for Depth. Not defined for other prescription types."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class RTPrescriptionTargetConstraints(SerializableObject):
    """Represents target structure constraints."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Constraints(self) -> List[RTPrescriptionConstraint]:
        """List[RTPrescriptionConstraint]: Constraints."""
        ...

    @property
    def TargetId(self) -> str:
        """str: Identifier of the target structure."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class RadioactiveSource(ApiDataObject):
    """Represents a radioactive source installed into a"""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def CalibrationDate(self) -> Optional[datetime]:
        """Optional[datetime]: The calibration date for the strength of this radioactive source."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def NominalActivity(self) -> bool:
        """bool: Defines whether source decay is accounted for in treatment planning. If the value is true, the dose calculation uses the source at its calibration activity (nominal activity). If the value is false, the source strength is decayed to the treatment activity based on the treatment date of the plan where the source is used."""
        ...

    @property
    def RadioactiveSourceModel(self) -> RadioactiveSourceModel:
        """RadioactiveSourceModel: The brachytherapy radioactive source model associated with this radioactive source."""
        ...

    @property
    def SerialNumber(self) -> str:
        """str: The serial number of this radioactive source."""
        ...

    @property
    def Strength(self) -> float:
        """float: The source strength for the radioactive source on the calibration date in cGy cm^2/h."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class RadioactiveSourceModel(ApiDataObject):
    """The radioactive source model represents the details of the radioactive source used in brachytherapy. It encapsulates the source isotope, dimensions, and dose calculation parameters."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def ActiveSize(self) -> VVector:
        """VVector: The active size of the modeled radioactive source in x, y, and z dimensions in millimeters. x represents the source width, y represents the source height, and z the source length."""
        ...

    @property
    def ActivityConversionFactor(self) -> float:
        """float: The activity-kerma conversion factor is used for converting activity (in mCi) to air-kerma strength (in U = cGy cm^2 / h). The unit of the factor is [U / mCi]."""
        ...

    @property
    def CalculationModel(self) -> str:
        """str: The dose calculation type used with this source model. Possible values are "Point source" and "Linear source"."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def DoseRateConstant(self) -> float:
        """float: A conversion factor from the air-kerma strength to the dose rate in tissue. The unit of the dose rate constant is cGy / (h U)."""
        ...

    @property
    def HalfLife(self) -> float:
        """float: The half life of the isotope in seconds."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def LiteratureReference(self) -> str:
        """str: The reference to the scientific publications on which the source model is based."""
        ...

    @property
    def Manufacturer(self) -> str:
        """str: The manufacturer of the modeled radioactive source."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def SourceType(self) -> str:
        """str: The DICOM source type. Possible values are "Point", "Line", "Cylinder", and "Sphere"."""
        ...

    @property
    def Status(self) -> str:
        """str: The status of this source model. The status can be either "Unapproved", "Commissioning", "Approved", or "Retired"."""
        ...

    @property
    def StatusDate(self) -> Optional[datetime]:
        """Optional[datetime]: The time when the status of the source model was set."""
        ...

    @property
    def StatusUserName(self) -> str:
        """str: The name of the user who last set the status of the source model."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class RangeModulator(AddOn):
    """The range modulator device."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def CreationDateTime(self) -> Optional[datetime]:
        """Optional[datetime]: Property docstring."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Type(self) -> RangeModulatorType:
        """RangeModulatorType: The type of the device."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class RangeModulatorSettings(SerializableObject):
    """Range modulator settings."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def IsocenterToRangeModulatorDistance(self) -> float:
        """float: Distance from the isocenter to the downstream edge of the range modulator (mm) at the current control point."""
        ...

    @property
    def RangeModulatorGatingStarWaterEquivalentThickness(self) -> float:
        """float: Water equivalent thickness (in mm) of the range modulator at the position specified by Range Modulator Gating Start Value."""
        ...

    @property
    def RangeModulatorGatingStartValue(self) -> float:
        """float: Start position defines the range modulator position at which the beam is switched on."""
        ...

    @property
    def RangeModulatorGatingStopValue(self) -> float:
        """float: Stop position defines the range modulator position at which the beam is switched off."""
        ...

    @property
    def RangeModulatorGatingStopWaterEquivalentThickness(self) -> float:
        """float: Water equivalent thickness (in mm) of the range modulator at the position specified by Range Modulator Gating Stop Value."""
        ...

    @property
    def ReferencedRangeModulator(self) -> RangeModulator:
        """RangeModulator: The referenced range modulator."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class RangeShifter(AddOn):
    """The range shifter device."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def CreationDateTime(self) -> Optional[datetime]:
        """Optional[datetime]: Property docstring."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Type(self) -> RangeShifterType:
        """RangeShifterType: The type of the device."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class RangeShifterSettings(SerializableObject):
    """Range shifter settings."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def IsocenterToRangeShifterDistance(self) -> float:
        """float: Distance from the isocenter to the downstream edge of the range shifter (mm) at the current control point."""
        ...

    @property
    def RangeShifterSetting(self) -> str:
        """str: Machine-specific setting."""
        ...

    @property
    def RangeShifterWaterEquivalentThickness(self) -> float:
        """float: Water equivalent thickness (in mm) of the range shifter at the central axis for the beam energy incident upon the device."""
        ...

    @property
    def ReferencedRangeShifter(self) -> RangeShifter:
        """RangeShifter: The referenced range shifter."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class ReferencePoint(ApiDataObject):
    """A reference point associated with a patient."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def DailyDoseLimit(self) -> DoseValue:
        """DoseValue: Daily dose limit of this reference point."""
        ...

    @DailyDoseLimit.setter
    def DailyDoseLimit(self, value: DoseValue) -> None:
        """Set property value."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: [Availability of this property depends on your Eclipse Scripting API license] The identifier of the Reference Point."""
        ...

    @Id.setter
    def Id(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def SessionDoseLimit(self) -> DoseValue:
        """DoseValue: Session dose limit of this reference point."""
        ...

    @SessionDoseLimit.setter
    def SessionDoseLimit(self, value: DoseValue) -> None:
        """Set property value."""
        ...

    @property
    def TotalDoseLimit(self) -> DoseValue:
        """DoseValue: Total dose limit of this reference point."""
        ...

    @TotalDoseLimit.setter
    def TotalDoseLimit(self, value: DoseValue) -> None:
        """Set property value."""
        ...

    def AddLocation(self, Image: Image, x: float, y: float, z: float, errorHint: StringBuilder) -> bool:
        """Method docstring."""
        ...

    def ChangeLocation(self, Image: Image, x: float, y: float, z: float, errorHint: StringBuilder) -> bool:
        """Method docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetReferencePointLocation(self, Image: Image) -> VVector:
        """Method docstring."""
        ...

    @overload
    def GetReferencePointLocation(self, planSetup: PlanSetup) -> VVector:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def HasLocation(self, planSetup: PlanSetup) -> bool:
        """Method docstring."""
        ...

    def ReadXml(self, reader: XmlReader) -> None:
        """Method docstring."""
        ...

    def RemoveLocation(self, Image: Image, errorHint: StringBuilder) -> bool:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    def WriteXml(self, writer: XmlWriter) -> None:
        """Method docstring."""
        ...


class Registration(ApiDataObject):
    """Represents the spatial registration matrix between two frames of reference."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def CreationDateTime(self) -> Optional[datetime]:
        """Optional[datetime]: The date when this object was created."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def RegisteredFOR(self) -> str:
        """str: The frame of reference UID of the registered coordinate system."""
        ...

    @property
    def SourceFOR(self) -> str:
        """str: The frame of reference UID of the source coordinate system."""
        ...

    @property
    def Status(self) -> RegistrationApprovalStatus:
        """RegistrationApprovalStatus: The current approval status of the registration."""
        ...

    @property
    def StatusDateTime(self) -> Optional[datetime]:
        """Optional[datetime]: The approval status date and time."""
        ...

    @property
    def StatusUserDisplayName(self) -> str:
        """str: Full user name of user who changed the approval status."""
        ...

    @property
    def StatusUserName(self) -> str:
        """str: User ID of the user who changed the approval status."""
        ...

    @property
    def TransformationMatrix(self) -> Array[float]:
        """Array[float]: The elements of the 4x4 transformation matrix."""
        ...

    @property
    def UID(self) -> str:
        """str: The SOP Instance UID of this registration object."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def InverseTransformPoint(self, pt: VVector) -> VVector:
        """Method docstring."""
        ...

    def ReadXml(self, reader: XmlReader) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    def TransformPoint(self, pt: VVector) -> VVector:
        """Method docstring."""
        ...

    def WriteXml(self, writer: XmlWriter) -> None:
        """Method docstring."""
        ...


class ScriptContext:
    """Contains the runtime context information of the active application for the script."""

    def __init__(self, context: Any, user: Any, dvhEstimation: Any, appName: str) -> None:
        """Initialize instance."""
        ...

    @property
    def ApplicationName(self) -> str:
        """str: The name of the active application."""
        ...

    @property
    def BrachyPlanSetup(self) -> BrachyPlanSetup:
        """BrachyPlanSetup: The active brachytherapy plan setup. The value is null if the active object is not a brachytherapy plan setup."""
        ...

    @property
    def BrachyPlansInScope(self) -> List[BrachyPlanSetup]:
        """List[BrachyPlanSetup]: Retrieves a list of all brachytherapy plans in the Scope window."""
        ...

    @property
    def Calculation(self) -> Calculation:
        """Calculation: Calculation related functions"""
        ...

    @property
    def Course(self) -> Course:
        """Course: The course. The value may be null if the context has no course."""
        ...

    @property
    def CurrentUser(self) -> User:
        """User: The current user of the application."""
        ...

    @property
    def Equipment(self) -> Equipment:
        """Equipment: Provides access to clinical devices and accessories."""
        ...

    @Equipment.setter
    def Equipment(self, value: Equipment) -> None:
        """Set property value."""
        ...

    @property
    def ExternalPlanSetup(self) -> ExternalPlanSetup:
        """ExternalPlanSetup: The active external beam plan setup. The value is null if the active object is not an external beam plan setup."""
        ...

    @property
    def ExternalPlansInScope(self) -> List[ExternalPlanSetup]:
        """List[ExternalPlanSetup]: Retrieves a list of all external beam plans in the Scope window."""
        ...

    @property
    def Image(self) -> Image:
        """Image: The 3D image. The value may be null if the context has no image."""
        ...

    @property
    def IonPlanSetup(self) -> IonPlanSetup:
        """IonPlanSetup: The active proton plan setup. The value is null if the active object is not a proton plan setup."""
        ...

    @property
    def IonPlansInScope(self) -> List[IonPlanSetup]:
        """List[IonPlanSetup]: Retrieves a list of all proton plans in the Scope window."""
        ...

    @property
    def Patient(self) -> Patient:
        """Patient: The patient. The value may be null if the context has no patient."""
        ...

    @property
    def PlanSetup(self) -> PlanSetup:
        """PlanSetup: The plan setup. The value may be null if the context has no plan setup."""
        ...

    @property
    def PlanSum(self) -> PlanSum:
        """PlanSum: Retrieves the active plan sum."""
        ...

    @property
    def PlanSumsInScope(self) -> List[PlanSum]:
        """List[PlanSum]: Retrieves a list of all plan sums in the Scope window."""
        ...

    @property
    def PlansInScope(self) -> List[PlanSetup]:
        """List[PlanSetup]: Retrieves a list of all plans in the Scope window."""
        ...

    @property
    def StructureCodes(self) -> ActiveStructureCodeDictionaries:
        """ActiveStructureCodeDictionaries: Provides access to the structure code dictionaries with the active structure codes."""
        ...

    @StructureCodes.setter
    def StructureCodes(self, value: ActiveStructureCodeDictionaries) -> None:
        """Set property value."""
        ...

    @property
    def StructureSet(self) -> StructureSet:
        """StructureSet: The structure set. The value may be null if the context has no structure set."""
        ...

    @property
    def VersionInfo(self) -> str:
        """str: The version number of Eclipse."""
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


class ScriptEnvironment:
    """Contains the runtime information of the application environment for the script."""

    def __init__(self, appName: str, scripts: List[ApplicationScript], scriptExecutionEngine: Action[Assembly, Any, Window, Any]) -> None:
        """Initialize instance."""
        ...

    @overload
    def __init__(self, appName: str, scripts: List[ApplicationScript], packages: List[ApplicationPackage], scriptExecutionEngine: Action[Assembly, Any, Window, Any]) -> None:
        """Initialize instance."""
        ...

    @property
    def ApiVersionInfo(self) -> str:
        """str: The version number of Eclipse Scripting API."""
        ...

    @property
    def ApplicationName(self) -> str:
        """str: The name of the active application."""
        ...

    @property
    def Packages(self) -> List[ApplicationPackage]:
        """List[ApplicationPackage]: Retrieves a list of all packages known by the application."""
        ...

    @property
    def Scripts(self) -> List[ApplicationScript]:
        """List[ApplicationScript]: Retrieves a list of all scripts known by the application."""
        ...

    @property
    def VersionInfo(self) -> str:
        """str: The version number of Eclipse."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def ExecuteScript(self, scriptAssembly: Assembly, scriptContext: ScriptContext, window: Window) -> None:
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


class SearchBodyParameters(SerializableObject):
    """Parameters for the Search Body feature."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def FillAllCavities(self) -> bool:
        """bool: Defines whether all cavities are filled."""
        ...

    @FillAllCavities.setter
    def FillAllCavities(self, value: bool) -> None:
        """Set property value."""
        ...

    @property
    def KeepLargestParts(self) -> bool:
        """bool: Defines whether the largest part(s) of the Body structure are kept."""
        ...

    @KeepLargestParts.setter
    def KeepLargestParts(self, value: bool) -> None:
        """Set property value."""
        ...

    @property
    def LowerHUThreshold(self) -> int:
        """int: The lower threshold of the Hounsfield Unit value in the CT for the Search Body feature."""
        ...

    @LowerHUThreshold.setter
    def LowerHUThreshold(self, value: int) -> None:
        """Set property value."""
        ...

    @property
    def MREdgeThresholdHigh(self) -> int:
        """int: Higher edge threshold for MR images."""
        ...

    @MREdgeThresholdHigh.setter
    def MREdgeThresholdHigh(self, value: int) -> None:
        """Set property value."""
        ...

    @property
    def MREdgeThresholdLow(self) -> int:
        """int: Lower edge threshold for MR images."""
        ...

    @MREdgeThresholdLow.setter
    def MREdgeThresholdLow(self, value: int) -> None:
        """Set property value."""
        ...

    @property
    def NumberOfLargestPartsToKeep(self) -> int:
        """int: The number of the largest parts in the Body structure that are kept."""
        ...

    @NumberOfLargestPartsToKeep.setter
    def NumberOfLargestPartsToKeep(self, value: int) -> None:
        """Set property value."""
        ...

    @property
    def PreCloseOpenings(self) -> bool:
        """bool: Defines whether to connect structure parts before extraction."""
        ...

    @PreCloseOpenings.setter
    def PreCloseOpenings(self, value: bool) -> None:
        """Set property value."""
        ...

    @property
    def PreCloseOpeningsRadius(self) -> float:
        """float: Radius setting for PreCloseOpenings."""
        ...

    @PreCloseOpeningsRadius.setter
    def PreCloseOpeningsRadius(self, value: float) -> None:
        """Set property value."""
        ...

    @property
    def PreDisconnect(self) -> bool:
        """bool: Defines whether to disconnect structure parts before extraction."""
        ...

    @PreDisconnect.setter
    def PreDisconnect(self, value: bool) -> None:
        """Set property value."""
        ...

    @property
    def PreDisconnectRadius(self) -> float:
        """float: Radius setting for PreDisconnect."""
        ...

    @PreDisconnectRadius.setter
    def PreDisconnectRadius(self, value: float) -> None:
        """Set property value."""
        ...

    @property
    def Smoothing(self) -> bool:
        """bool: Whether to do smoothing."""
        ...

    @Smoothing.setter
    def Smoothing(self, value: bool) -> None:
        """Set property value."""
        ...

    @property
    def SmoothingLevel(self) -> int:
        """int: Smoothing levels."""
        ...

    @SmoothingLevel.setter
    def SmoothingLevel(self, value: int) -> None:
        """Set property value."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def LoadDefaults(self) -> None:
        """Loads the default values of the Search Body parameters."""
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


class SeedCollection(ApiDataObject):
    """Represents a collection of brachytherapy"""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def BrachyFieldReferencePoints(self) -> List[BrachyFieldReferencePoint]:
        """List[BrachyFieldReferencePoint]: Obsolete."""
        ...

    @property
    def Color(self) -> Color:
        """Color: The color of the seeds in the seed collection in the views."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def SourcePositions(self) -> List[SourcePosition]:
        """List[SourcePosition]: The source positions in this collection in creation order."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class SegmentVolume(SerializableObject):
    """The volumetric representation of a structure. This object is used  when defining margins for structures, or when performing Boolean operations on structures."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    def And(self, other: SegmentVolume) -> SegmentVolume:
        """Method docstring."""
        ...

    def AsymmetricMargin(self, margins: AxisAlignedMargins) -> SegmentVolume:
        """Method docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def Margin(self, marginInMM: float) -> SegmentVolume:
        """Method docstring."""
        ...

    def Not(self) -> SegmentVolume:
        """Creates a combination of segment volumes. Does not modify this segment volume. The combination includes the area that covers everything else but this segment volume.
        
        Returns:
            SegmentVolume: A new combined segment volume."""
        ...

    def Or(self, other: SegmentVolume) -> SegmentVolume:
        """Method docstring."""
        ...

    def ReadXml(self, reader: XmlReader) -> None:
        """Method docstring."""
        ...

    def Sub(self, other: SegmentVolume) -> SegmentVolume:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    def WriteXml(self, writer: XmlWriter) -> None:
        """Method docstring."""
        ...

    def Xor(self, other: SegmentVolume) -> SegmentVolume:
        """Method docstring."""
        ...


class SerializableObject:
    """Base class for objects that can be serialized."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @staticmethod
    def ClearSerializationHistory() -> None:
        """This member is internal to the Eclipse Scripting API."""
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
            XmlSchema: XmlSchema"""
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


class Series(ApiDataObject):
    """A series is a collection of radiation therapy objects of a patient. The series is part of a study. See the definition of a DICOM Series for more information."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def FOR(self) -> str:
        """str: The UID of the frame of reference."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Images(self) -> List[Image]:
        """List[Image]: A collection of images that belong to the series."""
        ...

    @property
    def ImagingDeviceDepartment(self) -> str:
        """str: The assigned department of the device that is used to scan the images into the system. Returns an empty string if the imaging device is not unique or the device department is not defined."""
        ...

    @property
    def ImagingDeviceId(self) -> str:
        """str: The identifier of the device that is used to scan the images into the system. Returns an empty string if the imaging device is not unique or the device identifier is not defined."""
        ...

    @property
    def ImagingDeviceManufacturer(self) -> str:
        """str: The manufacturer of the device that is used to scan the images into the system. Returns an empty string if the imaging device is not unique or the device manufacturer is not defined."""
        ...

    @property
    def ImagingDeviceModel(self) -> str:
        """str: The model of the device that is used to scan the images into the system. Returns an empty string if the imaging device is not unique or the device model is not defined."""
        ...

    @property
    def ImagingDeviceSerialNo(self) -> str:
        """str: The serial number of the device that is used to scan the images into the system. Returns an empty string if the imaging device is not unique or the device serial number is not defined."""
        ...

    @property
    def Modality(self) -> SeriesModality:
        """SeriesModality: The modality of the series."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Study(self) -> Study:
        """Study: Used for navigating to parent study."""
        ...

    @property
    def UID(self) -> str:
        """str: The DICOM UID."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def ReadXml(self, reader: XmlReader) -> None:
        """Method docstring."""
        ...

    def SetImagingDevice(self, imagingDeviceId: str) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    def WriteXml(self, writer: XmlWriter) -> None:
        """Method docstring."""
        ...


class SingleThreadSynchronizationContext(SynchronizationContext):
    """Provides a SynchronizationContext object that is single-threaded."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    def Complete(self) -> None:
        """Notifies the context that no more work will arrive."""
        ...

    def CreateCopy(self) -> SynchronizationContext:
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

    def IsWaitNotificationRequired(self) -> bool:
        """Method docstring."""
        ...

    def OperationCompleted(self) -> None:
        """Method docstring."""
        ...

    def OperationStarted(self) -> None:
        """Method docstring."""
        ...

    def Post(self, d: SendOrPostCallback, state: Any) -> None:
        """Method docstring."""
        ...

    def RunOnCurrentThread(self) -> None:
        """Runs an loop to process all queued work items."""
        ...

    def Send(self, d: SendOrPostCallback, state: Any) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    def Wait(self, waitHandles: Array[IntPtr], waitAll: bool, millisecondsTimeout: int) -> int:
        """Method docstring."""
        ...


class SingleThreadSynchronizationContextSetter:
    """Provides a temporary single-threaded environment until the diposal of this object ("""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    def Complete(self) -> None:
        """Method docstring."""
        ...

    def Dispose(self) -> None:
        """Resets the SynchronizationContext."""
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

    def Run(self) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...


class Slot(ApiDataObject):
    """A slot is the location (typically on the collimator head of the gantry) where an add-on, such as a wedge or block, is mounted."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Number(self) -> int:
        """int: The slot number is unique within an instance of a treatment machine."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class SourcePosition(ApiDataObject):
    """Represents a brachytherapy source dwell position in a"""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def DwellTime(self) -> float:
        """float: Dwell time."""
        ...

    @property
    def DwellTimeLock(self) -> Optional[bool]:
        """Optional[bool]: Identifies if the dwell time is locked. Set dwell time either locked = true, or unlocked = false. Locked when not allowed to change the dwell time. If unlocked, the dwell time can be changed."""
        ...

    @DwellTimeLock.setter
    def DwellTimeLock(self, value: Optional[bool]) -> None:
        """Set property value."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def NominalDwellTime(self) -> float:
        """float: The nominal dwell time associated with this source position in seconds."""
        ...

    @NominalDwellTime.setter
    def NominalDwellTime(self, value: float) -> None:
        """Set property value."""
        ...

    @property
    def RadioactiveSource(self) -> RadioactiveSource:
        """RadioactiveSource: The radioactive source associated with this dwell position."""
        ...

    @property
    def Transform(self) -> Array[float]:
        """Array[float]: The 4x4 transformation matrix represents the orientation and location of the source position in space. The matrix is composed of a 4x3 rotation submatrix and a 4x1 translation vector. Its bottom row indicates scaling and is always [0 0 0 1]. The translation vector indicates the coordinates of the source position center, in millimeters. The third column of the rotation matrix indicates the source axis direction."""
        ...

    @property
    def Translation(self) -> VVector:
        """VVector: The translation of this source position."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class StandardWedge(Wedge):
    """A standard wedge is a physical piece of material with an angle that is static during treatment."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def CreationDateTime(self) -> Optional[datetime]:
        """Optional[datetime]: Property docstring."""
        ...

    @property
    def Direction(self) -> float:
        """float: Property docstring."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def WedgeAngle(self) -> float:
        """float: Property docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class Structure(ApiDataObject):
    """A structure is a geometrical representation of an anatomical organ, a treatment volume, a marker, or a support structure. See the definition of a DICOM Structure for more information."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def ApprovalHistory(self) -> List[StructureApprovalHistoryEntry]:
        """List[StructureApprovalHistoryEntry]: Returns the approval history of the structure."""
        ...

    @property
    def CenterPoint(self) -> VVector:
        """VVector: The center point of the structure."""
        ...

    @property
    def Color(self) -> Color:
        """Color: The color of the structure."""
        ...

    @Color.setter
    def Color(self, value: Color) -> None:
        """Set property value."""
        ...

    @property
    def Comment(self) -> str:
        """str: [Availability of this property depends on your Eclipse Scripting API license] A comment about the Structure."""
        ...

    @Comment.setter
    def Comment(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def DicomType(self) -> str:
        """str: The DICOM type of the structure, for example, PTV, MARKER, or ORGAN."""
        ...

    @property
    def HasCalculatedPlans(self) -> bool:
        """bool: Checks if a calculated plan exists for the structure"""
        ...

    @property
    def HasSegment(self) -> bool:
        """bool: Checks if the structure has a segment."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: [Availability of this property depends on your Eclipse Scripting API license] The identifier of the Structure."""
        ...

    @Id.setter
    def Id(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def IsApproved(self) -> bool:
        """bool: Checks if the structure is approved"""
        ...

    @property
    def IsEmpty(self) -> bool:
        """bool: Checks if the structure is empty."""
        ...

    @property
    def IsHighResolution(self) -> bool:
        """bool: true if this structure is a high-resolution structure. Otherwise false."""
        ...

    @property
    def IsTarget(self) -> bool:
        """bool: Checks if the structure is PTV, CTV or GTV"""
        ...

    @property
    def MeshGeometry(self) -> MeshGeometry3D:
        """MeshGeometry3D: The mesh geometry."""
        ...

    @property
    def Name(self) -> str:
        """str: [Availability of this property depends on your Eclipse Scripting API license] The name of the Structure."""
        ...

    @Name.setter
    def Name(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def ROINumber(self) -> int:
        """int: The DICOM ROI Number of the structure."""
        ...

    @property
    def SegmentVolume(self) -> SegmentVolume:
        """SegmentVolume: Provides access to the segment volume of the structure."""
        ...

    @SegmentVolume.setter
    def SegmentVolume(self, value: SegmentVolume) -> None:
        """Set property value."""
        ...

    @property
    def StructureCode(self) -> StructureCode:
        """StructureCode: The structure code that identifies this structure."""
        ...

    @StructureCode.setter
    def StructureCode(self, value: StructureCode) -> None:
        """Set property value."""
        ...

    @property
    def StructureCodeInfos(self) -> List[StructureCodeInfo]:
        """List[StructureCodeInfo]: Property docstring."""
        ...

    @property
    def Volume(self) -> float:
        """float: The calculated volume."""
        ...

    def AddContourOnImagePlane(self, contour: Array[VVector], z: int) -> None:
        """Method docstring."""
        ...

    def And(self, other: SegmentVolume) -> SegmentVolume:
        """Method docstring."""
        ...

    def AsymmetricMargin(self, margins: AxisAlignedMargins) -> SegmentVolume:
        """Method docstring."""
        ...

    def CanConvertToHighResolution(self) -> bool:
        """Returns true if this structure can be converted to a high-resolution structure.
        
        Returns:
            bool: true if this structure can be converted to a high-resolution structure."""
        ...

    def CanEditSegmentVolume(self, errorMessage: str) -> bool:
        """Method docstring."""
        ...

    def CanSetAssignedHU(self, errorMessage: str) -> bool:
        """Method docstring."""
        ...

    def ClearAllContoursOnImagePlane(self, z: int) -> None:
        """Method docstring."""
        ...

    def ConvertDoseLevelToStructure(self, dose: Dose, doseLevel: DoseValue) -> None:
        """Method docstring."""
        ...

    def ConvertToHighResolution(self) -> None:
        """[Availability of this method depends on your Eclipse Scripting API license] Converts this structure to a high-resolution structure. Increases the resolution of the segment volume in cases where the image size is larger than 256x256 voxels.
        
        Raises:
            System.InvalidOperationException: Can not convert this structure."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetAssignedHU(self, huValue: float) -> bool:
        """Method docstring."""
        ...

    def GetContoursOnImagePlane(self, z: int) -> Array[Array[VVector]]:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetNumberOfSeparateParts(self) -> int:
        """If the structure has a segment, returns the number of separate parts.
        
        Returns:
            int: Returns the number of separate parts in this structure"""
        ...

    def GetReferenceLinePoints(self) -> Array[VVector]:
        """If the structure is a reference line, gets its points.
        
        Returns:
            Array[VVector]: An array that holds the points defining the reference line. If no reference line exists, the array is empty."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
        ...

    def GetSegmentProfile(self, start: VVector, stop: VVector, preallocatedBuffer: BitArray) -> SegmentProfile:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def IsPointInsideSegment(self, point: VVector) -> bool:
        """Method docstring."""
        ...

    def Margin(self, marginInMM: float) -> SegmentVolume:
        """Method docstring."""
        ...

    def Not(self) -> SegmentVolume:
        """Boolean Not operation for structures that have a segment model. Provided here for convenience.
        
        Returns:
            SegmentVolume: A new combined segment volume."""
        ...

    def Or(self, other: SegmentVolume) -> SegmentVolume:
        """Method docstring."""
        ...

    def ReadXml(self, reader: XmlReader) -> None:
        """Method docstring."""
        ...

    def ResetAssignedHU(self) -> bool:
        """[Availability of this method depends on your Eclipse Scripting API license] Resets the HU value of the material to "undefined".
        
        Returns:
            bool: Returns true if the HU value was set to "undefined". Returns false, if the value could not be reset. This can happen if the material has been set to a structure."""
        ...

    def SetAssignedHU(self, huValue: float) -> None:
        """Method docstring."""
        ...

    def Sub(self, other: SegmentVolume) -> SegmentVolume:
        """Method docstring."""
        ...

    def SubtractContourOnImagePlane(self, contour: Array[VVector], z: int) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    def WriteXml(self, writer: XmlWriter) -> None:
        """Method docstring."""
        ...

    def Xor(self, other: SegmentVolume) -> SegmentVolume:
        """Method docstring."""
        ...


class StructureCode(SerializableObject):
    """Represents a structure code and its coding scheme."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Code(self) -> str:
        """str: The structure code as defined in the associated coding scheme."""
        ...

    @property
    def CodeMeaning(self) -> str:
        """str: The meaning of the structure code."""
        ...

    @property
    def CodingScheme(self) -> str:
        """str: The coding scheme of the structure code."""
        ...

    @property
    def DisplayName(self) -> str:
        """str: The display name of the code."""
        ...

    @property
    def IsEncompassStructureCode(self) -> bool:
        """bool: Indicates whether the structure code is an encompass structure code."""
        ...

    def Equals(self, other: StructureCode) -> bool:
        """Method docstring."""
        ...

    @overload
    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Returns the hash code for this structure code."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def ReadXml(self, reader: XmlReader) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Returns a string that represents this object.
        
        Returns:
            str: A string that represents this object."""
        ...

    def ToStructureCodeInfo(self) -> StructureCodeInfo:
        """Returns a StructureCodeInfo object with the same coding scheme and code as in the current structure code object."""
        ...

    def WriteXml(self, writer: XmlWriter) -> None:
        """Method docstring."""
        ...


class StructureCodeDictionary:
    """Represents a set of structure codes as defined by a structure code scheme. The class exposes the structure codes that are available through the implemented"""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Count(self) -> int:
        """int: Gets the number of structure code object key/value pairs in this structure code dictionary."""
        ...

    @property
    def Item(self) -> StructureCode:
        """StructureCode: Property docstring."""
        ...

    @property
    def Keys(self) -> List[str]:
        """List[str]: Gets a collection containing the structure code identifiers in this structure code dictionary."""
        ...

    @property
    def Name(self) -> str:
        """str: The name of the structure code scheme."""
        ...

    @property
    def Values(self) -> List[StructureCode]:
        """List[StructureCode]: Gets a collection containing the structure codes in this structure code dictionary."""
        ...

    @property
    def Version(self) -> str:
        """str: The version of the structure code scheme. May be an empty string, if not applicable to the scheme."""
        ...

    def ContainsKey(self, key: str) -> bool:
        """Method docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetEnumerator(self) -> IEnumerator[KeyValuePair[str, StructureCode]]:
        """Returns an enumerator that iterates through the collection."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Returns a string that represents this object.
        
        Returns:
            str: A string that represents this object."""
        ...

    def TryGetValue(self, key: str, value: StructureCode) -> bool:
        """Method docstring."""
        ...

    SchemeNameFma: str
    SchemeNameRadLex: str
    SchemeNameSrt: str
    SchemeNameVmsStructCode: str

class StructureSet(ApiDataObject):
    """A structure set is a container for structures of a patient, including anatomical organs, treatment volumes and markers, and support structures."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def ApplicationScriptLogs(self) -> List[ApplicationScriptLog]:
        """List[ApplicationScriptLog]: The log entries of the script executions that have modified the structure set."""
        ...

    @property
    def Comment(self) -> str:
        """str: [Availability of this property depends on your Eclipse Scripting API license] A comment about the structure set."""
        ...

    @Comment.setter
    def Comment(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: [Availability of this property depends on your Eclipse Scripting API license] The identifier of the structure set."""
        ...

    @Id.setter
    def Id(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def Image(self) -> Image:
        """Image: Used for navigating to the image."""
        ...

    @property
    def Name(self) -> str:
        """str: [Availability of this property depends on your Eclipse Scripting API license] The name of the structure set."""
        ...

    @Name.setter
    def Name(self, value: str) -> None:
        """Set property value."""
        ...

    @property
    def Patient(self) -> Patient:
        """Patient: Used for navigating to the patient."""
        ...

    @property
    def Series(self) -> Series:
        """Series: The series that contains this plan. Null if the plan is not connected to a series."""
        ...

    @property
    def SeriesUID(self) -> str:
        """str: The DICOM UID of the series that contains this structure set. Empty string if the structure set is not connected to a series."""
        ...

    @property
    def Structures(self) -> List[Structure]:
        """List[Structure]: Used for navigating to the child structures."""
        ...

    @property
    def UID(self) -> str:
        """str: DICOM UID."""
        ...

    def AddCouchStructures(self, couchModel: str, orientation: PatientOrientation, railA: RailPosition, railB: RailPosition, surfaceHU: Optional[float], interiorHU: Optional[float], railHU: Optional[float], addedStructures: ReadOnlyList, imageResized: bool, error: str) -> bool:
        """Method docstring."""
        ...

    def AddReferenceLine(self, name: str, id: str, referenceLinePoints: Array[VVector]) -> Structure:
        """Method docstring."""
        ...

    def AddStructure(self, dicomType: str, id: str) -> Structure:
        """Method docstring."""
        ...

    @overload
    def AddStructure(self, code: StructureCodeInfo) -> Structure:
        """Method docstring."""
        ...

    def CanAddCouchStructures(self, error: str) -> bool:
        """Method docstring."""
        ...

    def CanAddStructure(self, dicomType: str, id: str) -> bool:
        """Method docstring."""
        ...

    def CanRemoveCouchStructures(self, error: str) -> bool:
        """Method docstring."""
        ...

    def CanRemoveStructure(self, structure: Structure) -> bool:
        """Method docstring."""
        ...

    def Copy(self) -> StructureSet:
        """[Availability of this method depends on your Eclipse Scripting API license] Creates a copy of this structure set.
        
        Returns:
            StructureSet: The newly created copy of the structure set."""
        ...

    def CreateAndSearchBody(self, parameters: SearchBodyParameters) -> Structure:
        """Method docstring."""
        ...

    def Delete(self) -> None:
        """[Availability of this method depends on your Eclipse Scripting API license] Deletes this structure set."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetDefaultSearchBodyParameters(self) -> SearchBodyParameters:
        """Gets a default set of Search Body parameters.
        
        Returns:
            SearchBodyParameters: Parameters for the Search Body feature."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def ReadXml(self, reader: XmlReader) -> None:
        """Method docstring."""
        ...

    def RemoveCouchStructures(self, removedStructureIds: ReadOnlyList, error: str) -> bool:
        """Method docstring."""
        ...

    def RemoveStructure(self, structure: Structure) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...

    def WriteXml(self, writer: XmlWriter) -> None:
        """Method docstring."""
        ...


class Study(ApiDataObject):
    """A study is a collection of series."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def CreationDateTime(self) -> Optional[datetime]:
        """Optional[datetime]: The date when this object was created."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Images3D(self) -> List[Image]:
        """List[Image]: A collection of 3D images in a study."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Series(self) -> List[Series]:
        """List[Series]: A collection of series."""
        ...

    @property
    def UID(self) -> str:
        """str: The DICOM UID."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class Technique(ApiDataObject):
    """Treatment technique used for a beam. Can be, for example, static or arc, or (for proton beams) modulated scanning."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def IsArc(self) -> bool:
        """bool: Returns the value true if the beam technique is 'ARC' or 'SRS ARC'."""
        ...

    @property
    def IsModulatedScanning(self) -> bool:
        """bool: Returns the value true if the beam technique is 'MODULAT_SCANNING'."""
        ...

    @property
    def IsProton(self) -> bool:
        """bool: Returns the value true if it is a proton beam."""
        ...

    @property
    def IsScanning(self) -> bool:
        """bool: Returns the value true if the beam technique is 'MODULAT_SCANNING' or 'UNIFORM_SCANNING'."""
        ...

    @property
    def IsStatic(self) -> bool:
        """bool: Returns the value true if the beam technique is 'STATIC' or 'SRS STATIC'."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class TradeoffExplorationContext:
    """Class docstring."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def CanCreatePlanCollection(self) -> bool:
        """bool: True if a plan collection can be created."""
        ...

    @property
    def CanLoadSavedPlanCollection(self) -> bool:
        """bool: True if a previously saved plan collection can be loaded."""
        ...

    @property
    def CanUseHybridOptimizationInPlanGeneration(self) -> bool:
        """bool: True if VMAT-IMRT hybrid optimization can be used in"""
        ...

    @property
    def CanUsePlanDoseAsIntermediateDose(self) -> bool:
        """bool: True if plan dose can be used as intermediate dose in"""
        ...

    @property
    def CurrentDose(self) -> Dose:
        """Dose: Dose at the current location on the Pareto surface (the current trade-offs). Returns null if no valid dose exists."""
        ...

    @property
    def HasPlanCollection(self) -> bool:
        """bool: True if the trade-off exploration context has a plan collection, so that the trade-offs can be explored using the"""
        ...

    @HasPlanCollection.setter
    def HasPlanCollection(self, value: bool) -> None:
        """Set property value."""
        ...

    @property
    def TargetStructures(self) -> List[Structure]:
        """List[Structure]: Target structures in trade-off exploration. These structures cannot be selected for trade-off exploration at the structure level. Homogeneity indices only apply to the target structures."""
        ...

    @property
    def TradeoffObjectiveCandidates(self) -> List[OptimizationObjective]:
        """List[OptimizationObjective]: Available optimization objectives that can be selected for trade-off exploration in multi-criteria optimization."""
        ...

    @property
    def TradeoffObjectives(self) -> IReadOnlyCollection[TradeoffObjective]:
        """IReadOnlyCollection[TradeoffObjective]: Trade-off objectives. If"""
        ...

    @property
    def TradeoffStructureCandidates(self) -> List[Structure]:
        """List[Structure]: Available structures that can be selected for trade-off exploration in multi-criteria optimization. Only organs at risk can be used for trade-off exploration at the structure level."""
        ...

    def AddTargetHomogeneityObjective(self, targetStructure: Structure) -> bool:
        """Method docstring."""
        ...

    def AddTradeoffObjective(self, structure: Structure) -> bool:
        """Method docstring."""
        ...

    @overload
    def AddTradeoffObjective(self, objective: OptimizationObjective) -> bool:
        """Method docstring."""
        ...

    def ApplyTradeoffExplorationResult(self) -> None:
        """[Availability of this method depends on your Eclipse Scripting API license] Saves the trade-off exploration result. Also applies the trade-off exploration result to the plan setup for IMRT plans. For VMAT plans, to apply the results to the plan setup, an additional call to the"""
        ...

    def CreateDeliverableVmatPlan(self, useIntermediateDose: bool) -> bool:
        """Method docstring."""
        ...

    def CreatePlanCollection(self, continueOptimization: bool, intermediateDoseMode: TradeoffPlanGenerationIntermediateDoseMode, useHybridOptimizationForVmat: bool = 'False') -> bool:
        """Method docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetObjectiveCost(self, objective: TradeoffObjective) -> float:
        """Method docstring."""
        ...

    def GetObjectiveLowerLimit(self, objective: TradeoffObjective) -> float:
        """Method docstring."""
        ...

    def GetObjectiveUpperLimit(self, objective: TradeoffObjective) -> float:
        """Method docstring."""
        ...

    def GetObjectiveUpperRestrictor(self, objective: TradeoffObjective) -> float:
        """Method docstring."""
        ...

    def GetStructureDvh(self, structure: Structure) -> DVHData:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def LoadSavedPlanCollection(self) -> bool:
        """Loads a previously saved plan collection and sets
        
        Returns:
            bool: True if the plan collection was successfully loaded from the database."""
        ...

    def RemoveAllTradeoffObjectives(self) -> None:
        """[Availability of this method depends on your Eclipse Scripting API license] Removes all the trade-off objectives of the current plan collection. Removing all trade-off objectives invalidates the current plan collection and sets"""
        ...

    def RemovePlanCollection(self) -> None:
        """[Availability of this method depends on your Eclipse Scripting API license] Removes the plan collection from the plan setup and database. Removing the plan collection sets"""
        ...

    def RemoveTargetHomogeneityObjective(self, targetStructure: Structure) -> bool:
        """Method docstring."""
        ...

    def RemoveTradeoffObjective(self, tradeoffObjective: TradeoffObjective) -> bool:
        """Method docstring."""
        ...

    @overload
    def RemoveTradeoffObjective(self, structure: Structure) -> bool:
        """Method docstring."""
        ...

    def ResetToBalancedPlan(self) -> None:
        """[Availability of this method depends on your Eclipse Scripting API license] Resets the costs of a trade-off objective to correspond to the balanced plan. If"""
        ...

    def SetObjectiveCost(self, tradeoffObjective: TradeoffObjective, cost: float) -> None:
        """Method docstring."""
        ...

    def SetObjectiveUpperRestrictor(self, tradeoffObjective: TradeoffObjective, restrictorValue: float) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...


class TradeoffObjective:
    """Trade-off objective interface that consists of a set of optimization objectives."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Id(self) -> int:
        """int: Identifier of the trade-off objective."""
        ...

    @property
    def OptimizationObjectives(self) -> List[OptimizationObjective]:
        """List[OptimizationObjective]: The collection of objectives that this trade-off objective represents."""
        ...

    @property
    def Structure(self) -> Structure:
        """Structure: Structure that this trade-off objective represents."""
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


class TradeoffPlanGenerationIntermediateDoseMode:
    """Enumeration that specifies the use of intermediate dose when optimizing a plan collection for trade-off exploring."""

    Calculate: TradeoffPlanGenerationIntermediateDoseMode
    NotUsed: TradeoffPlanGenerationIntermediateDoseMode
    UsePlanDose: TradeoffPlanGenerationIntermediateDoseMode

class Tray(AddOn):
    """A tray add-on is a plate where blocks, compensators, and other beam modifying materials can be fixed to. The tray is inserted into a slot during the treatment of a beam."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def CreationDateTime(self) -> Optional[datetime]:
        """Optional[datetime]: Property docstring."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class TreatmentPhase(ApiDataObject):
    """Treatment phase."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def OtherInfo(self) -> str:
        """str: Other info (notes)."""
        ...

    @property
    def PhaseGapNumberOfDays(self) -> int:
        """int: Number of days between phases."""
        ...

    @property
    def Prescriptions(self) -> List[RTPrescription]:
        """List[RTPrescription]: A collection of RT prescriptions in the course."""
        ...

    @property
    def TimeGapType(self) -> str:
        """str: Type of the time gap."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class TreatmentSession(ApiDataObject):
    """Treatment session."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def SessionNumber(self) -> int:
        """int: Treatment session number."""
        ...

    @property
    def SessionPlans(self) -> List[PlanTreatmentSession]:
        """List[PlanTreatmentSession]: Plans in this treatment session."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class TreatmentUnitOperatingLimit(ApiDataObject):
    """Describes the limits of a treatment unit parameter and provides descriptive information related to it."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Label(self) -> str:
        """str: Gets the descriptive name of the operating limit parameter."""
        ...

    @property
    def MaxValue(self) -> float:
        """float: Gets the maximum allowed value for the operating limit parameter."""
        ...

    @property
    def MinValue(self) -> float:
        """float: Gets the minimum allowed value for the operating limit parameter."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Precision(self) -> Optional[int]:
        """Optional[int]: Gets the number of decimal places to display for the operating limit parameter."""
        ...

    @property
    def UnitString(self) -> str:
        """str: Gets the string that describes the unit of the operating limit parameter."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class TreatmentUnitOperatingLimits(SerializableObject):
    """Provides operating limit information for treatment unit parameters."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def CollimatorAngle(self) -> TreatmentUnitOperatingLimit:
        """TreatmentUnitOperatingLimit: Gets the operating limit information for the collimator angle parameter."""
        ...

    @property
    def GantryAngle(self) -> TreatmentUnitOperatingLimit:
        """TreatmentUnitOperatingLimit: Gets the operating limit information for the gantry angle parameter."""
        ...

    @property
    def MU(self) -> TreatmentUnitOperatingLimit:
        """TreatmentUnitOperatingLimit: Gets the operating limit information for the monitor unit (MU) parameter."""
        ...

    @property
    def PatientSupportAngle(self) -> TreatmentUnitOperatingLimit:
        """TreatmentUnitOperatingLimit: Gets the operating limit information for the patient support angle parameter."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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


class TypeBasedIdValidator:
    """A utility class for validating the data object identifier."""

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

    @staticmethod
    def IsValidId(id: str, dataObject: ApiDataObject, errorHint: StringBuilder) -> bool:
        """Method docstring."""
        ...

    @staticmethod
    def ThrowIfNotValidId(id: str, dataObject: ApiDataObject) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Method docstring."""
        ...


class User(SerializableObject):
    """Represents a user."""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Id(self) -> str:
        """str: The identifier of the user."""
        ...

    @property
    def Language(self) -> str:
        """str: The language of the user."""
        ...

    @property
    def Name(self) -> str:
        """str: The display name of the user."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Serves as a hash function for this type.
        
        Returns:
            int: A hash code for the current Object."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
        ...

    def GetType(self) -> Type:
        """Method docstring."""
        ...

    def ReadXml(self, reader: XmlReader) -> None:
        """Method docstring."""
        ...

    def ToString(self) -> str:
        """Returns a string that represents the current object.
        
        Returns:
            str: A string that represents the current object."""
        ...

    def WriteXml(self, writer: XmlWriter) -> None:
        """Method docstring."""
        ...


class VMATProgressStatus(ValueType):
    """Class docstring."""

    def __init__(self, status: str, iteration: int, progress: int) -> None:
        """Initialize instance."""
        ...

    @property
    def Iteration(self) -> int:
        """int: Property docstring."""
        ...

    @property
    def Progress(self) -> int:
        """int: Property docstring."""
        ...

    @property
    def Status(self) -> str:
        """str: Property docstring."""
        ...

    def Equals(self, other: VMATProgressStatus) -> bool:
        """Method docstring."""
        ...

    @overload
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


class Wedge(AddOn):
    """A wedge is a beam modulating add-on that modifies the dose intensity over all or a part of a treatment beam.
    
    Use run-time type information via operator"""

    def __init__(self) -> None:
        """Initialize instance."""
        ...

    @property
    def Comment(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def CreationDateTime(self) -> Optional[datetime]:
        """Optional[datetime]: Property docstring."""
        ...

    @property
    def Direction(self) -> float:
        """float: The wedge orientation with respect to the beam orientation, in degrees."""
        ...

    @property
    def HistoryDateTime(self) -> datetime:
        """datetime: Property docstring."""
        ...

    @property
    def HistoryUserDisplayName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def HistoryUserName(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Id(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def Name(self) -> str:
        """str: Property docstring."""
        ...

    @property
    def WedgeAngle(self) -> float:
        """float: The wedge angle."""
        ...

    def Equals(self, obj: Any) -> bool:
        """Method docstring."""
        ...

    def GetHashCode(self) -> int:
        """Method docstring."""
        ...

    def GetSchema(self) -> XmlSchema:
        """Method docstring."""
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

