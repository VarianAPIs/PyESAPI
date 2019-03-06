# encoding: utf-8
# module VMS.TPS.Common.Model.API calls itself API
# from VMS.TPS.Common.Model.API, Version=1.0.300.11, Culture=neutral, PublicKeyToken=305b81e210ec4b89
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class SerializableObject(object, IXmlSerializable):
    # no doc
    @staticmethod
    def ClearSerializationHistory():
        """ ClearSerializationHistory() """
        pass

    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetSchema(self):
        """ GetSchema(self: SerializableObject) -> XmlSchema """
        pass

    def ReadXml(self, reader):
        """ ReadXml(self: SerializableObject, reader: XmlReader) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: SerializableObject, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class ApiDataObject(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def Equals(self, obj):
        """ Equals(self: ApiDataObject, obj: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: ApiDataObject) -> int """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def ToString(self):
        """ ToString(self: ApiDataObject) -> str """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: ApiDataObject, writer: XmlWriter) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Comment(self: ApiDataObject) -> str

"""

    HistoryDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HistoryDateTime(self: ApiDataObject) -> DateTime

"""

    HistoryUserDisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HistoryUserDisplayName(self: ApiDataObject) -> str

"""

    HistoryUserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HistoryUserName(self: ApiDataObject) -> str

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: ApiDataObject) -> str

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ApiDataObject) -> str

"""



class AddOn(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: AddOn, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CreationDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreationDateTime(self: AddOn) -> Nullable[DateTime]

"""



class AddOnMaterial(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: AddOnMaterial, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class Application(SerializableObject, IXmlSerializable, IDisposable):
    # no doc
    def ClosePatient(self):
        """ ClosePatient(self: Application) """
        pass

    @staticmethod
    def CreateApplication(username=None, password=None):
        """
        CreateApplication(username: str, password: str) -> Application
        CreateApplication() -> Application
        """
        pass

    def Dispose(self):
        """ Dispose(self: Application) """
        pass

    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def OpenPatient(self, patientSummary):
        """ OpenPatient(self: Application, patientSummary: PatientSummary) -> Patient """
        pass

    def OpenPatientById(self, id):
        """ OpenPatientById(self: Application, id: str) -> Patient """
        pass

    def SaveModifications(self):
        """ SaveModifications(self: Application) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: Application, writer: XmlWriter) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    CurrentUser = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentUser(self: Application) -> User

"""

    PatientSummaries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PatientSummaries(self: Application) -> IEnumerable[PatientSummary]

"""

    ScriptEnvironment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScriptEnvironment(self: Application) -> ScriptEnvironment

"""



class ApplicationScript(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: ApplicationScript, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ApprovalStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApprovalStatus(self: ApplicationScript) -> ApplicationScriptApprovalStatus

"""

    ApprovalStatusDisplayText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApprovalStatusDisplayText(self: ApplicationScript) -> str

"""

    AssemblyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AssemblyName(self: ApplicationScript) -> AssemblyName

"""

    ExpirationDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExpirationDate(self: ApplicationScript) -> Nullable[DateTime]

"""

    IsReadOnlyScript = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnlyScript(self: ApplicationScript) -> bool

"""

    IsWriteableScript = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsWriteableScript(self: ApplicationScript) -> bool

"""

    PublisherName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PublisherName(self: ApplicationScript) -> str

"""

    ScriptType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScriptType(self: ApplicationScript) -> ApplicationScriptType

"""

    StatusDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StatusDate(self: ApplicationScript) -> Nullable[DateTime]

"""

    StatusUserIdentity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StatusUserIdentity(self: ApplicationScript) -> UserIdentity

"""



class ApplicationScriptLog(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: ApplicationScriptLog, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CourseId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CourseId(self: ApplicationScriptLog) -> str

"""

    PatientId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PatientId(self: ApplicationScriptLog) -> str

"""

    PlanSetupId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlanSetupId(self: ApplicationScriptLog) -> str

"""

    PlanUID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlanUID(self: ApplicationScriptLog) -> str

"""

    Script = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Script(self: ApplicationScriptLog) -> ApplicationScript

"""

    ScriptFullName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScriptFullName(self: ApplicationScriptLog) -> str

"""

    StructureSetId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StructureSetId(self: ApplicationScriptLog) -> str

"""

    StructureSetUID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StructureSetUID(self: ApplicationScriptLog) -> str

"""



class Applicator(AddOn, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: Applicator, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class Beam(ApiDataObject, IXmlSerializable):
    # no doc
    def ApplyParameters(self, beamParams):
        """ ApplyParameters(self: Beam, beamParams: BeamParameters) """
        pass

    def CanSetOptimalFluence(self, fluence, message):
        """ CanSetOptimalFluence(self: Beam, fluence: Fluence) -> (bool, str) """
        pass

    def CollimatorAngleToUser(self, val):
        """ CollimatorAngleToUser(self: Beam, val: float) -> float """
        pass

    def CreateOrReplaceDRR(self, parameters):
        """ CreateOrReplaceDRR(self: Beam, parameters: DRRCalculationParameters) -> Image """
        pass

    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def FitCollimatorToStructure(self, margins, structure, useAsymmetricXJaws, useAsymmetricYJaws, optimizeCollimatorRotation):
        """ FitCollimatorToStructure(self: Beam, margins: FitToStructureMargins, structure: Structure, useAsymmetricXJaws: bool, useAsymmetricYJaws: bool, optimizeCollimatorRotation: bool) """
        pass

    def FitMLCToOutline(self, outline, optimizeCollimatorRotation=None, jawFit=None, olmp=None, clmp=None):
        """ FitMLCToOutline(self: Beam, outline: Array[Array[Point]])FitMLCToOutline(self: Beam, outline: Array[Array[Point]], optimizeCollimatorRotation: bool, jawFit: JawFitting, olmp: OpenLeavesMeetingPoint, clmp: ClosedLeavesMeetingPoint) """
        pass

    def FitMLCToStructure(self, *__args):
        """ FitMLCToStructure(self: Beam, structure: Structure)FitMLCToStructure(self: Beam, margins: FitToStructureMargins, structure: Structure, optimizeCollimatorRotation: bool, jawFit: JawFitting, olmp: OpenLeavesMeetingPoint, clmp: ClosedLeavesMeetingPoint) """
        pass

    def GantryAngleToUser(self, val):
        """ GantryAngleToUser(self: Beam, val: float) -> float """
        pass

    def GetEditableParameters(self):
        """ GetEditableParameters(self: Beam) -> BeamParameters """
        pass

    def GetOptimalFluence(self):
        """ GetOptimalFluence(self: Beam) -> Fluence """
        pass

    def GetSourceLocation(self, gantryAngle):
        """ GetSourceLocation(self: Beam, gantryAngle: float) -> VVector """
        pass

    def GetStructureOutlines(self, structure, inBEV):
        """ GetStructureOutlines(self: Beam, structure: Structure, inBEV: bool) -> Array[Array[Point]] """
        pass

    def JawPositionsToUserString(self, val):
        """ JawPositionsToUserString(self: Beam, val: VRect[float]) -> str """
        pass

    def PatientSupportAngleToUser(self, val):
        """ PatientSupportAngleToUser(self: Beam, val: float) -> float """
        pass

    def SetOptimalFluence(self, fluence):
        """ SetOptimalFluence(self: Beam, fluence: Fluence) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: Beam, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Applicator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Applicator(self: Beam) -> Applicator

"""

    ArcLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ArcLength(self: Beam) -> float

"""

    AverageSSD = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AverageSSD(self: Beam) -> float

"""

    BeamNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BeamNumber(self: Beam) -> int

"""

    Blocks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Blocks(self: Beam) -> IEnumerable[Block]

"""

    Boluses = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Boluses(self: Beam) -> IEnumerable[Bolus]

"""

    CalculationLogs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CalculationLogs(self: Beam) -> IEnumerable[BeamCalculationLog]

"""

    Compensator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Compensator(self: Beam) -> Compensator

"""

    ControlPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ControlPoints(self: Beam) -> ControlPointCollection

"""

    CreationDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreationDateTime(self: Beam) -> Nullable[DateTime]

"""

    Dose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dose(self: Beam) -> BeamDose

"""

    DoseRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DoseRate(self: Beam) -> int

"""

    DosimetricLeafGap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DosimetricLeafGap(self: Beam) -> float

"""

    EnergyModeDisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EnergyModeDisplayName(self: Beam) -> str

"""

    FieldReferencePoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FieldReferencePoints(self: Beam) -> IEnumerable[FieldReferencePoint]

"""

    GantryDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GantryDirection(self: Beam) -> GantryDirection

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: Beam) -> str

Set: Id(self: Beam) = value
"""

    IsocenterPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsocenterPosition(self: Beam) -> VVector

"""

    IsSetupField = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSetupField(self: Beam) -> bool

"""

    Meterset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Meterset(self: Beam) -> MetersetValue

"""

    MetersetPerGy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MetersetPerGy(self: Beam) -> float

"""

    MLC = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MLC(self: Beam) -> MLC

"""

    MLCPlanType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MLCPlanType(self: Beam) -> MLCPlanType

"""

    MLCTransmissionFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MLCTransmissionFactor(self: Beam) -> float

"""

    MotionCompensationTechnique = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MotionCompensationTechnique(self: Beam) -> str

"""

    MotionSignalSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MotionSignalSource(self: Beam) -> str

"""

    NormalizationFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NormalizationFactor(self: Beam) -> float

"""

    NormalizationMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NormalizationMethod(self: Beam) -> str

"""

    Plan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plan(self: Beam) -> PlanSetup

"""

    PlannedSSD = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlannedSSD(self: Beam) -> float

"""

    ReferenceImage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceImage(self: Beam) -> Image

"""

    SetupTechnique = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SetupTechnique(self: Beam) -> SetupTechnique

"""

    SSD = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SSD(self: Beam) -> float

"""

    SSDAtStopAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SSDAtStopAngle(self: Beam) -> float

"""

    Technique = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Technique(self: Beam) -> Technique

"""

    ToleranceTableLabel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToleranceTableLabel(self: Beam) -> str

"""

    Trays = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Trays(self: Beam) -> IEnumerable[Tray]

"""

    TreatmentTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TreatmentTime(self: Beam) -> float

"""

    TreatmentUnit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TreatmentUnit(self: Beam) -> ExternalBeamTreatmentUnit

"""

    Wedges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Wedges(self: Beam) -> IEnumerable[Wedge]

"""

    WeightFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WeightFactor(self: Beam) -> float

"""



class BeamCalculationLog(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: BeamCalculationLog, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Beam = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Beam(self: BeamCalculationLog) -> Beam

"""

    Category = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Category(self: BeamCalculationLog) -> str

"""

    MessageLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MessageLines(self: BeamCalculationLog) -> IEnumerable[str]

"""



class Dose(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetDoseProfile(self, start, stop, preallocatedBuffer):
        """ GetDoseProfile(self: Dose, start: VVector, stop: VVector, preallocatedBuffer: Array[float]) -> DoseProfile """
        pass

    def GetDoseToPoint(self, at):
        """ GetDoseToPoint(self: Dose, at: VVector) -> DoseValue """
        pass

    def GetVoxels(self, planeIndex, preallocatedBuffer):
        """ GetVoxels(self: Dose, planeIndex: int, preallocatedBuffer: Array[int]) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def VoxelToDoseValue(self, voxelValue):
        """ VoxelToDoseValue(self: Dose, voxelValue: int) -> DoseValue """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: Dose, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DoseMax3D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DoseMax3D(self: Dose) -> DoseValue

"""

    DoseMax3DLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DoseMax3DLocation(self: Dose) -> VVector

"""

    Isodoses = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Isodoses(self: Dose) -> IEnumerable[Isodose]

"""

    Origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Origin(self: Dose) -> VVector

"""

    Series = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Series(self: Dose) -> Series

"""

    SeriesUID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SeriesUID(self: Dose) -> str

"""

    UID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UID(self: Dose) -> str

"""

    XDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XDirection(self: Dose) -> VVector

"""

    XRes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XRes(self: Dose) -> float

"""

    XSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XSize(self: Dose) -> int

"""

    YDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YDirection(self: Dose) -> VVector

"""

    YRes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YRes(self: Dose) -> float

"""

    YSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YSize(self: Dose) -> int

"""

    ZDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ZDirection(self: Dose) -> VVector

"""

    ZRes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ZRes(self: Dose) -> float

"""

    ZSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ZSize(self: Dose) -> int

"""



class BeamDose(Dose, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetAbsoluteBeamDoseValue(self, relative):
        """ GetAbsoluteBeamDoseValue(self: BeamDose, relative: DoseValue) -> DoseValue """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: BeamDose, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class BeamParameters(object):
    # no doc
    def SetAllLeafPositions(self, leafPositions):
        """ SetAllLeafPositions(self: BeamParameters, leafPositions: Array[Single]) """
        pass

    def SetJawPositions(self, positions):
        """ SetJawPositions(self: BeamParameters, positions: VRect[float]) """
        pass

    ControlPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ControlPoints(self: BeamParameters) -> IEnumerable[ControlPointParameters]

"""

    GantryDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GantryDirection(self: BeamParameters) -> GantryDirection

"""

    Isocenter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Isocenter(self: BeamParameters) -> VVector

Set: Isocenter(self: BeamParameters) = value
"""

    WeightFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WeightFactor(self: BeamParameters) -> float

Set: WeightFactor(self: BeamParameters) = value
"""



class BeamUncertainty(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: BeamUncertainty, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Beam = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Beam(self: BeamUncertainty) -> Beam

"""

    BeamNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BeamNumber(self: BeamUncertainty) -> BeamNumber

"""

    Dose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dose(self: BeamUncertainty) -> Dose

"""



class Block(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: Block, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AddOnMaterial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AddOnMaterial(self: Block) -> AddOnMaterial

"""

    IsDiverging = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDiverging(self: Block) -> bool

"""

    Outline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Outline(self: Block) -> Array[Array[Point]]

"""

    TransmissionFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransmissionFactor(self: Block) -> float

"""

    Tray = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Tray(self: Block) -> Tray

"""

    TrayTransmissionFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TrayTransmissionFactor(self: Block) -> float

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: Block) -> BlockType

"""



class Bolus(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: Bolus, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: Bolus) -> str

"""

    MaterialCTValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialCTValue(self: Bolus) -> float

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Bolus) -> str

"""



class BrachyFieldReferencePoint(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: BrachyFieldReferencePoint, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    FieldDose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FieldDose(self: BrachyFieldReferencePoint) -> DoseValue

"""

    IsFieldDoseNominal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFieldDoseNominal(self: BrachyFieldReferencePoint) -> bool

"""

    IsPrimaryReferencePoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPrimaryReferencePoint(self: BrachyFieldReferencePoint) -> bool

"""

    ReferencePoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferencePoint(self: BrachyFieldReferencePoint) -> ReferencePoint

"""

    RefPointLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RefPointLocation(self: BrachyFieldReferencePoint) -> VVector

"""



class PlanningItem(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetDoseAtVolume(self, structure, volume, volumePresentation, requestedDosePresentation):
        """ GetDoseAtVolume(self: PlanningItem, structure: Structure, volume: float, volumePresentation: VolumePresentation, requestedDosePresentation: DoseValuePresentation) -> DoseValue """
        pass

    def GetDVHCumulativeData(self, structure, dosePresentation, volumePresentation, binWidth):
        """ GetDVHCumulativeData(self: PlanningItem, structure: Structure, dosePresentation: DoseValuePresentation, volumePresentation: VolumePresentation, binWidth: float) -> DVHData """
        pass

    def GetVolumeAtDose(self, structure, dose, requestedVolumePresentation):
        """ GetVolumeAtDose(self: PlanningItem, structure: Structure, dose: DoseValue, requestedVolumePresentation: VolumePresentation) -> float """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: PlanningItem, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CreationDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreationDateTime(self: PlanningItem) -> Nullable[DateTime]

"""

    Dose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dose(self: PlanningItem) -> PlanningItemDose

"""

    DoseValuePresentation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DoseValuePresentation(self: PlanningItem) -> DoseValuePresentation

Set: DoseValuePresentation(self: PlanningItem) = value
"""

    StructureSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StructureSet(self: PlanningItem) -> StructureSet

"""

    StructuresSelectedForDvh = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StructuresSelectedForDvh(self: PlanningItem) -> IEnumerable[Structure]

"""



class PlanSetup(PlanningItem, IXmlSerializable):
    # no doc
    def AddReferencePoint(self, structure, location, id, name):
        """ AddReferencePoint(self: PlanSetup, structure: Structure, location: Nullable[VVector], id: str, name: str) -> ReferencePoint """
        pass

    def AttachToCalcClient(self, *args): #cannot find CLR method
        """ AttachToCalcClient(self: PlanSetup, doseCalcClient: ICalculationClient) """
        pass

    def ClearCalculationModel(self, calculationType):
        """ ClearCalculationModel(self: PlanSetup, calculationType: CalculationType) """
        pass

    def DetachFromCalcClient(self, *args): #cannot find CLR method
        """ DetachFromCalcClient(self: PlanSetup, doseCalcClient: ICalculationClient) """
        pass

    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetCalculationModel(self, calculationType):
        """ GetCalculationModel(self: PlanSetup, calculationType: CalculationType) -> str """
        pass

    def GetCalculationOption(self, calculationModel, optionName, optionValue):
        """ GetCalculationOption(self: PlanSetup, calculationModel: str, optionName: str) -> (bool, str) """
        pass

    def GetCalculationOptions(self, calculationModel):
        """ GetCalculationOptions(self: PlanSetup, calculationModel: str) -> Dictionary[str, str] """
        pass

    def GetProtocolPrescriptionsAndMeasures(self, prescriptions, measures):
        """ GetProtocolPrescriptionsAndMeasures(self: PlanSetup, prescriptions: List[ProtocolPhasePrescription], measures: List[ProtocolPhaseMeasure]) -> (List[ProtocolPhasePrescription], List[ProtocolPhaseMeasure]) """
        pass

    def Report(self, *args): #cannot find CLR method
        """ Report(self: PlanSetup, str: str) """
        pass

    def SetCalculationModel(self, calculationType, model):
        """ SetCalculationModel(self: PlanSetup, calculationType: CalculationType, model: str) """
        pass

    def SetCalculationOption(self, calculationModel, optionName, optionValue):
        """ SetCalculationOption(self: PlanSetup, calculationModel: str, optionName: str, optionValue: str) -> bool """
        pass

    def SetPrescription(self, numberOfFractions, dosePerFraction, treatmentPercentage):
        """ SetPrescription(self: PlanSetup, numberOfFractions: int, dosePerFraction: DoseValue, treatmentPercentage: float) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: PlanSetup, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ApplicationScriptLogs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplicationScriptLogs(self: PlanSetup) -> IEnumerable[ApplicationScriptLog]

"""

    ApprovalHistory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApprovalHistory(self: PlanSetup) -> IEnumerable[ApprovalHistoryEntry]

"""

    ApprovalStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApprovalStatus(self: PlanSetup) -> PlanSetupApprovalStatus

"""

    Beams = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Beams(self: PlanSetup) -> IEnumerable[Beam]

"""

    Course = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Course(self: PlanSetup) -> Course

"""

    CreationUserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreationUserName(self: PlanSetup) -> str

"""

    DosePerFraction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DosePerFraction(self: PlanSetup) -> DoseValue

"""

    DosePerFractionInPrimaryRefPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DosePerFractionInPrimaryRefPoint(self: PlanSetup) -> DoseValue

"""

    DVHEstimates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DVHEstimates(self: PlanSetup) -> IEnumerable[EstimatedDVH]

"""

    ElectronCalculationModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElectronCalculationModel(self: PlanSetup) -> str

"""

    ElectronCalculationOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElectronCalculationOptions(self: PlanSetup) -> Dictionary[str, str]

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: PlanSetup) -> str

Set: Id(self: PlanSetup) = value
"""

    IsDoseValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDoseValid(self: PlanSetup) -> bool

"""

    IsTreated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsTreated(self: PlanSetup) -> bool

"""

    NumberOfFractions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfFractions(self: PlanSetup) -> Nullable[int]

"""

    OptimizationSetup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OptimizationSetup(self: PlanSetup) -> OptimizationSetup

"""

    PhotonCalculationModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PhotonCalculationModel(self: PlanSetup) -> str

"""

    PhotonCalculationOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PhotonCalculationOptions(self: PlanSetup) -> Dictionary[str, str]

"""

    PlanIntent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlanIntent(self: PlanSetup) -> str

"""

    PlannedDosePerFraction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlannedDosePerFraction(self: PlanSetup) -> DoseValue

"""

    PlanningApprovalDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlanningApprovalDate(self: PlanSetup) -> str

"""

    PlanningApprover = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlanningApprover(self: PlanSetup) -> str

"""

    PlanningApproverDisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlanningApproverDisplayName(self: PlanSetup) -> str

"""

    PlanNormalizationMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlanNormalizationMethod(self: PlanSetup) -> str

"""

    PlanNormalizationPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlanNormalizationPoint(self: PlanSetup) -> VVector

"""

    PlanNormalizationValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlanNormalizationValue(self: PlanSetup) -> float

Set: PlanNormalizationValue(self: PlanSetup) = value
"""

    PlanObjectiveStructures = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlanObjectiveStructures(self: PlanSetup) -> IEnumerable[str]

"""

    PlanType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlanType(self: PlanSetup) -> PlanType

"""

    PlanUncertainties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlanUncertainties(self: PlanSetup) -> IEnumerable[PlanUncertainty]

"""

    PredecessorPlan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PredecessorPlan(self: PlanSetup) -> PlanSetup

"""

    PrescribedDosePerFraction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrescribedDosePerFraction(self: PlanSetup) -> DoseValue

"""

    PrescribedPercentage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrescribedPercentage(self: PlanSetup) -> float

"""

    PrimaryReferencePoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrimaryReferencePoint(self: PlanSetup) -> ReferencePoint

"""

    ProtocolID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProtocolID(self: PlanSetup) -> str

"""

    ProtocolPhaseID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProtocolPhaseID(self: PlanSetup) -> str

"""

    ProtonCalculationModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProtonCalculationModel(self: PlanSetup) -> str

"""

    ProtonCalculationOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProtonCalculationOptions(self: PlanSetup) -> Dictionary[str, str]

"""

    ReferencePoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferencePoints(self: PlanSetup) -> IEnumerable[ReferencePoint]

"""

    RTPrescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RTPrescription(self: PlanSetup) -> RTPrescription

"""

    Series = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Series(self: PlanSetup) -> Series

"""

    SeriesUID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SeriesUID(self: PlanSetup) -> str

"""

    TargetVolumeID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TargetVolumeID(self: PlanSetup) -> str

"""

    TotalDose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalDose(self: PlanSetup) -> DoseValue

"""

    TotalPrescribedDose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalPrescribedDose(self: PlanSetup) -> DoseValue

"""

    TreatmentApprovalDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TreatmentApprovalDate(self: PlanSetup) -> str

"""

    TreatmentApprover = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TreatmentApprover(self: PlanSetup) -> str

"""

    TreatmentApproverDisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TreatmentApproverDisplayName(self: PlanSetup) -> str

"""

    TreatmentOrientation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TreatmentOrientation(self: PlanSetup) -> PatientOrientation

"""

    TreatmentPercentage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TreatmentPercentage(self: PlanSetup) -> float

"""

    TreatmentSessions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TreatmentSessions(self: PlanSetup) -> IEnumerable[PlanTreatmentSession]

"""

    UID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UID(self: PlanSetup) -> str

"""

    UseGating = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseGating(self: PlanSetup) -> bool

Set: UseGating(self: PlanSetup) = value
"""

    VerifiedPlan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VerifiedPlan(self: PlanSetup) -> PlanSetup

"""


    m_errorsOnCalculationCompleted = None


class BrachyPlanSetup(PlanSetup, IXmlSerializable):
    # no doc
    def AttachToCalcClient(self, *args): #cannot find CLR method
        """ AttachToCalcClient(self: PlanSetup, doseCalcClient: ICalculationClient) """
        pass

    def CalculateAccurateTG43DoseProfile(self, start, stop, preallocatedBuffer):
        """ CalculateAccurateTG43DoseProfile(self: BrachyPlanSetup, start: VVector, stop: VVector, preallocatedBuffer: Array[float]) -> DoseProfile """
        pass

    def DetachFromCalcClient(self, *args): #cannot find CLR method
        """ DetachFromCalcClient(self: PlanSetup, doseCalcClient: ICalculationClient) """
        pass

    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def Report(self, *args): #cannot find CLR method
        """ Report(self: PlanSetup, str: str) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: BrachyPlanSetup, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ApplicationSetupType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplicationSetupType(self: BrachyPlanSetup) -> str

"""

    Catheters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Catheters(self: BrachyPlanSetup) -> IEnumerable[Catheter]

"""

    NumberOfPdrPulses = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfPdrPulses(self: BrachyPlanSetup) -> Nullable[int]

"""

    PdrPulseInterval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PdrPulseInterval(self: BrachyPlanSetup) -> Nullable[float]

"""

    SeedCollections = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SeedCollections(self: BrachyPlanSetup) -> IEnumerable[SeedCollection]

"""

    SolidApplicators = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SolidApplicators(self: BrachyPlanSetup) -> IEnumerable[BrachySolidApplicator]

"""

    TreatmentDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TreatmentDateTime(self: BrachyPlanSetup) -> Nullable[DateTime]

"""

    TreatmentTechnique = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TreatmentTechnique(self: BrachyPlanSetup) -> str

"""


    m_errorsOnCalculationCompleted = None


class BrachySolidApplicator(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: BrachySolidApplicator, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ApplicatorSetName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplicatorSetName(self: BrachySolidApplicator) -> str

"""

    ApplicatorSetType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplicatorSetType(self: BrachySolidApplicator) -> str

"""

    Category = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Category(self: BrachySolidApplicator) -> str

"""

    Catheters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Catheters(self: BrachySolidApplicator) -> IEnumerable[Catheter]

"""

    Note = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Note(self: BrachySolidApplicator) -> str

"""

    PartName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartName(self: BrachySolidApplicator) -> str

"""

    PartNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartNumber(self: BrachySolidApplicator) -> str

"""

    Summary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Summary(self: BrachySolidApplicator) -> str

"""

    UID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UID(self: BrachySolidApplicator) -> str

"""

    Vendor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vendor(self: BrachySolidApplicator) -> str

"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Version(self: BrachySolidApplicator) -> str

"""



class BrachyTreatmentUnit(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetActiveRadioactiveSource(self):
        """ GetActiveRadioactiveSource(self: BrachyTreatmentUnit) -> RadioactiveSource """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: BrachyTreatmentUnit, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DoseRateMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DoseRateMode(self: BrachyTreatmentUnit) -> str

"""

    DwellTimeResolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DwellTimeResolution(self: BrachyTreatmentUnit) -> float

"""

    MachineInterface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MachineInterface(self: BrachyTreatmentUnit) -> str

"""

    MachineModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MachineModel(self: BrachyTreatmentUnit) -> str

"""

    MaxDwellTimePerChannel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxDwellTimePerChannel(self: BrachyTreatmentUnit) -> float

"""

    MaxDwellTimePerPos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxDwellTimePerPos(self: BrachyTreatmentUnit) -> float

"""

    MaxDwellTimePerTreatment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxDwellTimePerTreatment(self: BrachyTreatmentUnit) -> float

"""

    MaximumChannelLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumChannelLength(self: BrachyTreatmentUnit) -> float

"""

    MaximumDwellPositionsPerChannel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumDwellPositionsPerChannel(self: BrachyTreatmentUnit) -> int

"""

    MaximumStepSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumStepSize(self: BrachyTreatmentUnit) -> float

"""

    MinimumChannelLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumChannelLength(self: BrachyTreatmentUnit) -> float

"""

    MinimumStepSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumStepSize(self: BrachyTreatmentUnit) -> float

"""

    NumberOfChannels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfChannels(self: BrachyTreatmentUnit) -> int

"""

    SourceCenterOffsetFromTip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SourceCenterOffsetFromTip(self: BrachyTreatmentUnit) -> float

"""

    SourceMovementType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SourceMovementType(self: BrachyTreatmentUnit) -> str

"""

    StepSizeResolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StepSizeResolution(self: BrachyTreatmentUnit) -> float

"""



class CalculationResult(object):
    # no doc
    Success = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Success(self: CalculationResult) -> bool

"""



class Catheter(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetSourcePosCenterDistanceFromTip(self, sourcePosition):
        """ GetSourcePosCenterDistanceFromTip(self: Catheter, sourcePosition: SourcePosition) -> float """
        pass

    def GetTotalDwellTime(self):
        """ GetTotalDwellTime(self: Catheter) -> float """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: Catheter, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ApplicatorLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplicatorLength(self: Catheter) -> float

"""

    BrachyFieldReferencePoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BrachyFieldReferencePoints(self: Catheter) -> IEnumerable[BrachyFieldReferencePoint]

"""

    BrachySolidApplicatorPartID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BrachySolidApplicatorPartID(self: Catheter) -> int

"""

    ChannelNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ChannelNumber(self: Catheter) -> int

"""

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Color(self: Catheter) -> Color

"""

    DeadSpaceLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeadSpaceLength(self: Catheter) -> float

"""

    Shape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Shape(self: Catheter) -> Array[VVector]

"""

    SourcePositions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SourcePositions(self: Catheter) -> IEnumerable[SourcePosition]

"""

    StepSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StepSize(self: Catheter) -> float

"""

    TreatmentUnit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TreatmentUnit(self: Catheter) -> BrachyTreatmentUnit

"""



class Compensator(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: Compensator, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Material = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Material(self: Compensator) -> AddOnMaterial

"""

    Slot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Slot(self: Compensator) -> Slot

"""

    Tray = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Tray(self: Compensator) -> Tray

"""



class ControlPoint(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: ControlPoint, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Beam = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Beam(self: ControlPoint) -> Beam

"""

    CollimatorAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CollimatorAngle(self: ControlPoint) -> float

"""

    GantryAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GantryAngle(self: ControlPoint) -> float

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: ControlPoint) -> int

"""

    JawPositions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: JawPositions(self: ControlPoint) -> VRect[float]

"""

    LeafPositions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeafPositions(self: ControlPoint) -> Array[Single]

"""

    MetersetWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MetersetWeight(self: ControlPoint) -> float

"""

    PatientSupportAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PatientSupportAngle(self: ControlPoint) -> float

"""

    TableTopLateralPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TableTopLateralPosition(self: ControlPoint) -> float

"""

    TableTopLongitudinalPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TableTopLongitudinalPosition(self: ControlPoint) -> float

"""

    TableTopVerticalPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TableTopVerticalPosition(self: ControlPoint) -> float

"""



class ControlPointCollection(SerializableObject, IXmlSerializable, IEnumerable[ControlPoint], IEnumerable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: ControlPointCollection) -> IEnumerator[ControlPoint] """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: ControlPointCollection, writer: XmlWriter) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ControlPoint](enumerable: IEnumerable[ControlPoint], value: ControlPoint) -> bool """
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

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: ControlPointCollection) -> int

"""



class ControlPointParameters(object):
    # no doc
    CollimatorAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CollimatorAngle(self: ControlPointParameters) -> float

"""

    GantryAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GantryAngle(self: ControlPointParameters) -> float

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: ControlPointParameters) -> int

"""

    JawPositions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: JawPositions(self: ControlPointParameters) -> VRect[float]

Set: JawPositions(self: ControlPointParameters) = value
"""

    LeafPositions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeafPositions(self: ControlPointParameters) -> Array[Single]

Set: LeafPositions(self: ControlPointParameters) = value
"""

    MetersetWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MetersetWeight(self: ControlPointParameters) -> float

"""

    PatientSupportAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PatientSupportAngle(self: ControlPointParameters) -> float

"""

    TableTopLateralPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TableTopLateralPosition(self: ControlPointParameters) -> float

"""

    TableTopLongitudinalPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TableTopLongitudinalPosition(self: ControlPointParameters) -> float

"""

    TableTopVerticalPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TableTopVerticalPosition(self: ControlPointParameters) -> float

"""



class Course(ApiDataObject, IXmlSerializable):
    # no doc
    def AddExternalPlanSetup(self, structureSet):
        """ AddExternalPlanSetup(self: Course, structureSet: StructureSet) -> ExternalPlanSetup """
        pass

    def AddExternalPlanSetupAsVerificationPlan(self, structureSet, verifiedPlan):
        """ AddExternalPlanSetupAsVerificationPlan(self: Course, structureSet: StructureSet, verifiedPlan: ExternalPlanSetup) -> ExternalPlanSetup """
        pass

    def AddIonPlanSetup(self, structureSet, patientSupportDeviceId):
        """ AddIonPlanSetup(self: Course, structureSet: StructureSet, patientSupportDeviceId: str) -> IonPlanSetup """
        pass

    def AddIonPlanSetupAsVerificationPlan(self, structureSet, patientSupportDeviceId, verifiedPlan):
        """ AddIonPlanSetupAsVerificationPlan(self: Course, structureSet: StructureSet, patientSupportDeviceId: str, verifiedPlan: IonPlanSetup) -> IonPlanSetup """
        pass

    def CanAddPlanSetup(self, structureSet):
        """ CanAddPlanSetup(self: Course, structureSet: StructureSet) -> bool """
        pass

    def CanRemovePlanSetup(self, planSetup):
        """ CanRemovePlanSetup(self: Course, planSetup: PlanSetup) -> bool """
        pass

    def CopyPlanSetup(self, sourcePlan, structureset=None, outputDiagnostics=None):
        """
        CopyPlanSetup(self: Course, sourcePlan: PlanSetup) -> PlanSetup
        CopyPlanSetup(self: Course, sourcePlan: PlanSetup, structureset: StructureSet, outputDiagnostics: StringBuilder) -> PlanSetup
        """
        pass

    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def RemovePlanSetup(self, planSetup):
        """ RemovePlanSetup(self: Course, planSetup: PlanSetup) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: Course, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BrachyPlanSetups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BrachyPlanSetups(self: Course) -> IEnumerable[BrachyPlanSetup]

"""

    CompletedDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CompletedDateTime(self: Course) -> Nullable[DateTime]

"""

    Diagnoses = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Diagnoses(self: Course) -> IEnumerable[Diagnosis]

"""

    ExternalPlanSetups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExternalPlanSetups(self: Course) -> IEnumerable[ExternalPlanSetup]

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: Course) -> str

Set: Id(self: Course) = value
"""

    Intent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Intent(self: Course) -> str

"""

    IonPlanSetups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IonPlanSetups(self: Course) -> IEnumerable[IonPlanSetup]

"""

    Patient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Patient(self: Course) -> Patient

"""

    PlanSetups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlanSetups(self: Course) -> IEnumerable[PlanSetup]

"""

    PlanSums = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlanSums(self: Course) -> IEnumerable[PlanSum]

"""

    StartDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartDateTime(self: Course) -> Nullable[DateTime]

"""

    TreatmentPhases = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TreatmentPhases(self: Course) -> IEnumerable[TreatmentPhase]

"""

    TreatmentSessions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TreatmentSessions(self: Course) -> IEnumerable[TreatmentSession]

"""



class CustomScriptExecutable(object):
    # no doc
    @staticmethod
    def CreateApplication(scriptName):
        """ CreateApplication(scriptName: str) -> Application """
        pass

    __all__ = [
        'CreateApplication',
    ]


class Diagnosis(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: Diagnosis, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ClinicalDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClinicalDescription(self: Diagnosis) -> str

"""

    Code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Code(self: Diagnosis) -> str

"""

    CodeTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CodeTable(self: Diagnosis) -> str

"""



class DVHData(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: DVHData, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Coverage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Coverage(self: DVHData) -> float

"""

    CurveData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurveData(self: DVHData) -> Array[DVHPoint]

"""

    MaxDose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxDose(self: DVHData) -> DoseValue

"""

    MeanDose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MeanDose(self: DVHData) -> DoseValue

"""

    MedianDose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MedianDose(self: DVHData) -> DoseValue

"""

    MinDose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinDose(self: DVHData) -> DoseValue

"""

    SamplingCoverage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SamplingCoverage(self: DVHData) -> float

"""

    StdDev = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StdDev(self: DVHData) -> float

"""

    Volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Volume(self: DVHData) -> float

"""



class Wedge(AddOn, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: Wedge, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Direction(self: Wedge) -> float

"""

    WedgeAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WedgeAngle(self: Wedge) -> float

"""



class DynamicWedge(Wedge, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: DynamicWedge, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class EnhancedDynamicWedge(DynamicWedge, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: EnhancedDynamicWedge, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class ESAPIActionPackAttribute(Attribute, _Attribute):
    """ ESAPIActionPackAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    IsWriteable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsWriteable(self: ESAPIActionPackAttribute) -> bool

Set: IsWriteable(self: ESAPIActionPackAttribute) = value
"""



class ESAPIScriptAttribute(Attribute, _Attribute):
    """ ESAPIScriptAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    IsWriteable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsWriteable(self: ESAPIScriptAttribute) -> bool

Set: IsWriteable(self: ESAPIScriptAttribute) = value
"""



class EstimatedDVH(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: EstimatedDVH, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CurveData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurveData(self: EstimatedDVH) -> Array[DVHPoint]

"""

    PlanSetup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlanSetup(self: EstimatedDVH) -> PlanSetup

"""

    PlanSetupId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlanSetupId(self: EstimatedDVH) -> str

"""

    Structure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Structure(self: EstimatedDVH) -> Structure

"""

    StructureId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StructureId(self: EstimatedDVH) -> str

"""

    TargetDoseLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TargetDoseLevel(self: EstimatedDVH) -> DoseValue

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: EstimatedDVH) -> DVHEstimateType

"""



class EvaluationDose(Dose, IXmlSerializable):
    # no doc
    def DoseValueToVoxel(self, doseValue):
        """ DoseValueToVoxel(self: EvaluationDose, doseValue: DoseValue) -> int """
        pass

    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def SetVoxels(self, planeIndex, values):
        """ SetVoxels(self: EvaluationDose, planeIndex: int, values: Array[int]) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: EvaluationDose, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class ExternalBeamTreatmentUnit(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: ExternalBeamTreatmentUnit, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    MachineModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MachineModel(self: ExternalBeamTreatmentUnit) -> str

"""

    MachineModelName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MachineModelName(self: ExternalBeamTreatmentUnit) -> str

"""

    MachineScaleDisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MachineScaleDisplayName(self: ExternalBeamTreatmentUnit) -> str

"""

    OperatingLimits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OperatingLimits(self: ExternalBeamTreatmentUnit) -> TreatmentUnitOperatingLimits

"""

    SourceAxisDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SourceAxisDistance(self: ExternalBeamTreatmentUnit) -> float

"""



class ExternalPlanSetup(PlanSetup, IXmlSerializable):
    # no doc
    def AddArcBeam(self, machineParameters, jawPositions, collimatorAngle, gantryAngle, gantryStop, gantryDirection, patientSupportAngle, isocenter):
        """ AddArcBeam(self: ExternalPlanSetup, machineParameters: ExternalBeamMachineParameters, jawPositions: VRect[float], collimatorAngle: float, gantryAngle: float, gantryStop: float, gantryDirection: GantryDirection, patientSupportAngle: float, isocenter: VVector) -> Beam """
        pass

    def AddConformalArcBeam(self, machineParameters, collimatorAngle, controlPointCount, gantryAngle, gantryStop, gantryDirection, patientSupportAngle, isocenter):
        """ AddConformalArcBeam(self: ExternalPlanSetup, machineParameters: ExternalBeamMachineParameters, collimatorAngle: float, controlPointCount: int, gantryAngle: float, gantryStop: float, gantryDirection: GantryDirection, patientSupportAngle: float, isocenter: VVector) -> Beam """
        pass

    def AddMLCArcBeam(self, machineParameters, leafPositions, jawPositions, collimatorAngle, gantryAngle, gantryStop, gantryDirection, patientSupportAngle, isocenter):
        """ AddMLCArcBeam(self: ExternalPlanSetup, machineParameters: ExternalBeamMachineParameters, leafPositions: Array[Single], jawPositions: VRect[float], collimatorAngle: float, gantryAngle: float, gantryStop: float, gantryDirection: GantryDirection, patientSupportAngle: float, isocenter: VVector) -> Beam """
        pass

    def AddMLCBeam(self, machineParameters, leafPositions, jawPositions, collimatorAngle, gantryAngle, patientSupportAngle, isocenter):
        """ AddMLCBeam(self: ExternalPlanSetup, machineParameters: ExternalBeamMachineParameters, leafPositions: Array[Single], jawPositions: VRect[float], collimatorAngle: float, gantryAngle: float, patientSupportAngle: float, isocenter: VVector) -> Beam """
        pass

    def AddMultipleStaticSegmentBeam(self, machineParameters, metersetWeights, collimatorAngle, gantryAngle, patientSupportAngle, isocenter):
        """ AddMultipleStaticSegmentBeam(self: ExternalPlanSetup, machineParameters: ExternalBeamMachineParameters, metersetWeights: IEnumerable[float], collimatorAngle: float, gantryAngle: float, patientSupportAngle: float, isocenter: VVector) -> Beam """
        pass

    def AddSlidingWindowBeam(self, machineParameters, metersetWeights, collimatorAngle, gantryAngle, patientSupportAngle, isocenter):
        """ AddSlidingWindowBeam(self: ExternalPlanSetup, machineParameters: ExternalBeamMachineParameters, metersetWeights: IEnumerable[float], collimatorAngle: float, gantryAngle: float, patientSupportAngle: float, isocenter: VVector) -> Beam """
        pass

    def AddStaticBeam(self, machineParameters, jawPositions, collimatorAngle, gantryAngle, patientSupportAngle, isocenter):
        """ AddStaticBeam(self: ExternalPlanSetup, machineParameters: ExternalBeamMachineParameters, jawPositions: VRect[float], collimatorAngle: float, gantryAngle: float, patientSupportAngle: float, isocenter: VVector) -> Beam """
        pass

    def AddVMATBeam(self, machineParameters, metersetWeights, collimatorAngle, gantryAngle, gantryStop, gantryDirection, patientSupportAngle, isocenter):
        """ AddVMATBeam(self: ExternalPlanSetup, machineParameters: ExternalBeamMachineParameters, metersetWeights: IEnumerable[float], collimatorAngle: float, gantryAngle: float, gantryStop: float, gantryDirection: GantryDirection, patientSupportAngle: float, isocenter: VVector) -> Beam """
        pass

    def AttachToCalcClient(self, *args): #cannot find CLR method
        """ AttachToCalcClient(self: PlanSetup, doseCalcClient: ICalculationClient) """
        pass

    def CalculateDose(self):
        """ CalculateDose(self: ExternalPlanSetup) -> CalculationResult """
        pass

    def CalculateDoseWithPresetValues(self, presetValues):
        """ CalculateDoseWithPresetValues(self: ExternalPlanSetup, presetValues: List[KeyValuePair[str, MetersetValue]]) -> CalculationResult """
        pass

    def CalculateDVHEstimates(self, modelId, targetDoseLevels, structureMatches):
        """ CalculateDVHEstimates(self: ExternalPlanSetup, modelId: str, targetDoseLevels: Dictionary[str, DoseValue], structureMatches: Dictionary[str, str]) -> CalculationResult """
        pass

    def CalculateLeafMotions(self, options=None):
        """
        CalculateLeafMotions(self: ExternalPlanSetup) -> CalculationResult
        CalculateLeafMotions(self: ExternalPlanSetup, options: LMCVOptions) -> CalculationResult
        CalculateLeafMotions(self: ExternalPlanSetup, options: SmartLMCOptions) -> CalculationResult
        CalculateLeafMotions(self: ExternalPlanSetup, options: LMCMSSOptions) -> CalculationResult
        """
        pass

    def CalculateLeafMotionsAndDose(self):
        """ CalculateLeafMotionsAndDose(self: ExternalPlanSetup) -> CalculationResult """
        pass

    def CopyEvaluationDose(self, existing):
        """ CopyEvaluationDose(self: ExternalPlanSetup, existing: Dose) -> EvaluationDose """
        pass

    def CreateEvaluationDose(self):
        """ CreateEvaluationDose(self: ExternalPlanSetup) -> EvaluationDose """
        pass

    def DetachFromCalcClient(self, *args): #cannot find CLR method
        """ DetachFromCalcClient(self: PlanSetup, doseCalcClient: ICalculationClient) """
        pass

    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetModelsForCalculationType(self, calculationType):
        """ GetModelsForCalculationType(self: ExternalPlanSetup, calculationType: CalculationType) -> IEnumerable[str] """
        pass

    def Optimize(self, *__args):
        """
        Optimize(self: ExternalPlanSetup, maxIterations: int) -> OptimizerResult
        Optimize(self: ExternalPlanSetup, maxIterations: int, optimizationOption: OptimizationOption) -> OptimizerResult
        Optimize(self: ExternalPlanSetup, maxIterations: int, optimizationOption: OptimizationOption, mlcId: str) -> OptimizerResult
        Optimize(self: ExternalPlanSetup) -> OptimizerResult
        Optimize(self: ExternalPlanSetup, options: OptimizationOptionsIMRT) -> OptimizerResult
        """
        pass

    def OptimizeVMAT(self, *__args):
        """
        OptimizeVMAT(self: ExternalPlanSetup, mlcId: str) -> OptimizerResult
        OptimizeVMAT(self: ExternalPlanSetup) -> OptimizerResult
        OptimizeVMAT(self: ExternalPlanSetup, options: OptimizationOptionsVMAT) -> OptimizerResult
        """
        pass

    def RemoveBeam(self, beam):
        """ RemoveBeam(self: ExternalPlanSetup, beam: Beam) """
        pass

    def Report(self, *args): #cannot find CLR method
        """ Report(self: PlanSetup, str: str) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: ExternalPlanSetup, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DoseAsEvaluationDose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DoseAsEvaluationDose(self: ExternalPlanSetup) -> EvaluationDose

"""

    TradeoffExplorationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TradeoffExplorationContext(self: ExternalPlanSetup) -> TradeoffExplorationContext

"""


    m_errorsOnCalculationCompleted = None


class FieldReferencePoint(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: FieldReferencePoint, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    EffectiveDepth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EffectiveDepth(self: FieldReferencePoint) -> float

"""

    FieldDose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FieldDose(self: FieldReferencePoint) -> DoseValue

"""

    IsFieldDoseNominal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFieldDoseNominal(self: FieldReferencePoint) -> bool

"""

    IsPrimaryReferencePoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPrimaryReferencePoint(self: FieldReferencePoint) -> bool

"""

    ReferencePoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferencePoint(self: FieldReferencePoint) -> ReferencePoint

"""

    RefPointLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RefPointLocation(self: FieldReferencePoint) -> VVector

"""

    SSD = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SSD(self: FieldReferencePoint) -> float

"""



class Globals(object):
    """ Globals() """
    @staticmethod
    def DisableApiAccessTrace():
        """ DisableApiAccessTrace() """
        pass

    @staticmethod
    def EnableApiAccessTrace():
        """ EnableApiAccessTrace() """
        pass

    @staticmethod
    def GetLoggedApiCalls():
        """ GetLoggedApiCalls() -> IEnumerable[str] """
        pass

    @staticmethod
    def SetMaximumNumberOfLoggedApiCalls(apiLogCacheSize):
        """ SetMaximumNumberOfLoggedApiCalls(apiLogCacheSize: int) """
        pass

    AbortNow = False
    DefaultMaximumNumberOfLoggedApiCalls = 200


class Hospital(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: Hospital, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CreationDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreationDateTime(self: Hospital) -> Nullable[DateTime]

"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: Hospital) -> str

"""



class Image(ApiDataObject, IXmlSerializable):
    # no doc
    def CreateNewStructureSet(self):
        """ CreateNewStructureSet(self: Image) -> StructureSet """
        pass

    def DicomToUser(self, dicom, planSetup):
        """ DicomToUser(self: Image, dicom: VVector, planSetup: PlanSetup) -> VVector """
        pass

    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetImageProfile(self, start, stop, preallocatedBuffer):
        """ GetImageProfile(self: Image, start: VVector, stop: VVector, preallocatedBuffer: Array[float]) -> ImageProfile """
        pass

    def GetVoxels(self, planeIndex, preallocatedBuffer):
        """ GetVoxels(self: Image, planeIndex: int, preallocatedBuffer: Array[int]) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def UserToDicom(self, user, planSetup):
        """ UserToDicom(self: Image, user: VVector, planSetup: PlanSetup) -> VVector """
        pass

    def VoxelToDisplayValue(self, voxelValue):
        """ VoxelToDisplayValue(self: Image, voxelValue: int) -> float """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: Image, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ApprovalHistory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApprovalHistory(self: Image) -> IEnumerable[ImageApprovalHistoryEntry]

"""

    ContrastBolusAgentIngredientName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContrastBolusAgentIngredientName(self: Image) -> str

"""

    CreationDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreationDateTime(self: Image) -> Nullable[DateTime]

"""

    DisplayUnit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayUnit(self: Image) -> str

"""

    FOR = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FOR(self: Image) -> str

"""

    HasUserOrigin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasUserOrigin(self: Image) -> bool

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: Image) -> str

Set: Id(self: Image) = value
"""

    ImagingOrientation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ImagingOrientation(self: Image) -> PatientOrientation

"""

    IsProcessed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsProcessed(self: Image) -> bool

"""

    Level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Level(self: Image) -> int

"""

    Origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Origin(self: Image) -> VVector

"""

    Series = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Series(self: Image) -> Series

"""

    UserOrigin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserOrigin(self: Image) -> VVector

Set: UserOrigin(self: Image) = value
"""

    UserOriginComments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserOriginComments(self: Image) -> str

"""

    Window = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Window(self: Image) -> int

"""

    XDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XDirection(self: Image) -> VVector

"""

    XRes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XRes(self: Image) -> float

"""

    XSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XSize(self: Image) -> int

"""

    YDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YDirection(self: Image) -> VVector

"""

    YRes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YRes(self: Image) -> float

"""

    YSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YSize(self: Image) -> int

"""

    ZDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ZDirection(self: Image) -> VVector

"""

    ZRes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ZRes(self: Image) -> float

"""

    ZSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ZSize(self: Image) -> int

"""



class IonBeam(Beam, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetEditableParameters(self):
        """ GetEditableParameters(self: IonBeam) -> IonBeamParameters """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: IonBeam, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AirGap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AirGap(self: IonBeam) -> float

"""

    DistalTargetMargin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DistalTargetMargin(self: IonBeam) -> float

"""

    IonControlPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IonControlPoints(self: IonBeam) -> IonControlPointCollection

"""

    LateralMargins = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LateralMargins(self: IonBeam) -> VRect[float]

"""

    LateralSpreadingDevices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LateralSpreadingDevices(self: IonBeam) -> IEnumerable[LateralSpreadingDevice]

"""

    NominalRange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NominalRange(self: IonBeam) -> float

"""

    NominalSOBPWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NominalSOBPWidth(self: IonBeam) -> float

"""

    OptionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OptionId(self: IonBeam) -> str

"""

    PatientSupportId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PatientSupportId(self: IonBeam) -> str

"""

    PatientSupportType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PatientSupportType(self: IonBeam) -> PatientSupportType

"""

    ProximalTargetMargin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProximalTargetMargin(self: IonBeam) -> float

"""

    RangeModulators = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RangeModulators(self: IonBeam) -> IEnumerable[RangeModulator]

"""

    RangeShifters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RangeShifters(self: IonBeam) -> IEnumerable[RangeShifter]

"""

    ScanMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScanMode(self: IonBeam) -> IonBeamScanMode

"""

    SnoutId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SnoutId(self: IonBeam) -> str

"""

    TargetStructure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TargetStructure(self: IonBeam) -> Structure

"""

    VirtualSADX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VirtualSADX(self: IonBeam) -> float

"""

    VirtualSADY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VirtualSADY(self: IonBeam) -> float

"""



class IonBeamParameters(BeamParameters):
    # no doc
    ControlPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ControlPoints(self: IonBeamParameters) -> IEnumerable[IonControlPointParameters]

"""

    IonControlPointPairs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IonControlPointPairs(self: IonBeamParameters) -> IonControlPointPairCollection

"""



class IonControlPoint(ControlPoint, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: IonControlPoint, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    FinalSpotList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FinalSpotList(self: IonControlPoint) -> IonSpotCollection

"""

    LateralSpreadingDeviceSettings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LateralSpreadingDeviceSettings(self: IonControlPoint) -> IEnumerable[LateralSpreadingDeviceSettings]

"""

    NominalBeamEnergy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NominalBeamEnergy(self: IonControlPoint) -> float

"""

    NumberOfPaintings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfPaintings(self: IonControlPoint) -> int

"""

    RangeModulatorSettings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RangeModulatorSettings(self: IonControlPoint) -> IEnumerable[RangeModulatorSettings]

"""

    RangeShifterSettings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RangeShifterSettings(self: IonControlPoint) -> IEnumerable[RangeShifterSettings]

"""

    RawSpotList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RawSpotList(self: IonControlPoint) -> IonSpotCollection

"""

    ScanningSpotSizeX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScanningSpotSizeX(self: IonControlPoint) -> float

"""

    ScanningSpotSizeY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScanningSpotSizeY(self: IonControlPoint) -> float

"""

    ScanSpotTuneId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScanSpotTuneId(self: IonControlPoint) -> str

"""

    SnoutPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SnoutPosition(self: IonControlPoint) -> float

"""



class IonControlPointCollection(SerializableObject, IXmlSerializable, IEnumerable[IonControlPoint], IEnumerable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: IonControlPointCollection) -> IEnumerator[IonControlPoint] """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: IonControlPointCollection, writer: XmlWriter) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[IonControlPoint](enumerable: IEnumerable[IonControlPoint], value: IonControlPoint) -> bool """
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

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: IonControlPointCollection) -> int

"""



class IonControlPointPair(object):
    # no doc
    def ResizeFinalSpotList(self, count):
        """ ResizeFinalSpotList(self: IonControlPointPair, count: int) """
        pass

    def ResizeRawSpotList(self, count):
        """ ResizeRawSpotList(self: IonControlPointPair, count: int) """
        pass

    EndControlPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndControlPoint(self: IonControlPointPair) -> IonControlPointParameters

"""

    FinalSpotList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FinalSpotList(self: IonControlPointPair) -> IonSpotParametersCollection

"""

    NominalBeamEnergy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NominalBeamEnergy(self: IonControlPointPair) -> float

"""

    RawSpotList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RawSpotList(self: IonControlPointPair) -> IonSpotParametersCollection

"""

    StartControlPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartControlPoint(self: IonControlPointPair) -> IonControlPointParameters

"""

    StartIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartIndex(self: IonControlPointPair) -> int

"""



class IonControlPointPairCollection(object, IEnumerable[IonControlPointPair], IEnumerable):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: IonControlPointPairCollection) -> IEnumerator[IonControlPointPair] """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[IonControlPointPair](enumerable: IEnumerable[IonControlPointPair], value: IonControlPointPair) -> bool """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: IonControlPointPairCollection) -> int

"""



class IonControlPointParameters(ControlPointParameters):
    # no doc
    FinalSpotList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FinalSpotList(self: IonControlPointParameters) -> IonSpotParametersCollection

"""

    RawSpotList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RawSpotList(self: IonControlPointParameters) -> IonSpotParametersCollection

"""



class IonPlanSetup(PlanSetup, IXmlSerializable):
    # no doc
    def AttachToCalcClient(self, *args): #cannot find CLR method
        """ AttachToCalcClient(self: PlanSetup, doseCalcClient: ICalculationClient) """
        pass

    def CalculateDose(self):
        """ CalculateDose(self: IonPlanSetup) -> CalculationResult """
        pass

    def CalculateDoseWithoutPostProcessing(self):
        """ CalculateDoseWithoutPostProcessing(self: IonPlanSetup) -> CalculationResult """
        pass

    def CopyEvaluationDose(self, existing):
        """ CopyEvaluationDose(self: IonPlanSetup, existing: Dose) -> EvaluationDose """
        pass

    def CreateEvaluationDose(self):
        """ CreateEvaluationDose(self: IonPlanSetup) -> EvaluationDose """
        pass

    def DetachFromCalcClient(self, *args): #cannot find CLR method
        """ DetachFromCalcClient(self: PlanSetup, doseCalcClient: ICalculationClient) """
        pass

    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetModelsForCalculationType(self, calculationType):
        """ GetModelsForCalculationType(self: IonPlanSetup, calculationType: CalculationType) -> IEnumerable[str] """
        pass

    def PostProcessAndCalculateDose(self):
        """ PostProcessAndCalculateDose(self: IonPlanSetup) -> CalculationResult """
        pass

    def Report(self, *args): #cannot find CLR method
        """ Report(self: PlanSetup, str: str) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: IonPlanSetup, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DoseAsEvaluationDose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DoseAsEvaluationDose(self: IonPlanSetup) -> EvaluationDose

"""

    IonBeams = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IonBeams(self: IonPlanSetup) -> IEnumerable[IonBeam]

"""

    IsPostProcessingNeeded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPostProcessingNeeded(self: IonPlanSetup) -> bool

Set: IsPostProcessingNeeded(self: IonPlanSetup) = value
"""


    m_errorsOnCalculationCompleted = None


class IonSpot(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: IonSpot, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: IonSpot) -> VVector

"""

    Weight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Weight(self: IonSpot) -> Single

"""



class IonSpotCollection(SerializableObject, IXmlSerializable, IEnumerable[IonSpot], IEnumerable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: IonSpotCollection) -> IEnumerator[IonSpot] """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: IonSpotCollection, writer: XmlWriter) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[IonSpot](enumerable: IEnumerable[IonSpot], value: IonSpot) -> bool """
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

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: IonSpotCollection) -> int

"""



class IonSpotParameters(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: IonSpotParameters, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Weight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Weight(self: IonSpotParameters) -> Single

Set: Weight(self: IonSpotParameters) = value
"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: IonSpotParameters) -> Single

Set: X(self: IonSpotParameters) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: IonSpotParameters) -> Single

Set: Y(self: IonSpotParameters) = value
"""



class IonSpotParametersCollection(SerializableObject, IXmlSerializable, IEnumerable[IonSpotParameters], IEnumerable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: IonSpotParametersCollection) -> IEnumerator[IonSpotParameters] """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: IonSpotParametersCollection, writer: XmlWriter) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[IonSpotParameters](enumerable: IEnumerable[IonSpotParameters], value: IonSpotParameters) -> bool """
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

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: IonSpotParametersCollection) -> int

"""



class Isodose(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: Isodose, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Color(self: Isodose) -> Color

"""

    Level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Level(self: Isodose) -> DoseValue

"""

    MeshGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MeshGeometry(self: Isodose) -> MeshGeometry3D

"""



class LateralSpreadingDevice(AddOn, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: LateralSpreadingDevice, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: LateralSpreadingDevice) -> LateralSpreadingDeviceType

"""



class LateralSpreadingDeviceSettings(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: LateralSpreadingDeviceSettings, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    IsocenterToLateralSpreadingDeviceDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsocenterToLateralSpreadingDeviceDistance(self: LateralSpreadingDeviceSettings) -> float

"""

    LateralSpreadingDeviceSetting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LateralSpreadingDeviceSetting(self: LateralSpreadingDeviceSettings) -> str

"""

    LateralSpreadingDeviceWaterEquivalentThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LateralSpreadingDeviceWaterEquivalentThickness(self: LateralSpreadingDeviceSettings) -> float

"""

    ReferencedLateralSpreadingDevice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferencedLateralSpreadingDevice(self: LateralSpreadingDeviceSettings) -> LateralSpreadingDevice

"""



class MLC(AddOn, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: MLC, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ManufacturerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ManufacturerName(self: MLC) -> str

"""

    MinDoseDynamicLeafGap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinDoseDynamicLeafGap(self: MLC) -> float

"""

    Model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Model(self: MLC) -> str

"""

    SerialNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SerialNumber(self: MLC) -> str

"""



class MotorizedWedge(Wedge, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: MotorizedWedge, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class OmniWedge(Wedge, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: OmniWedge, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class OptimizationObjective(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def Equals(self, obj):
        """ Equals(self: OptimizationObjective, obj: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: OptimizationObjective) -> int """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: OptimizationObjective, writer: XmlWriter) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Operator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Operator(self: OptimizationObjective) -> OptimizationObjectiveOperator

"""

    Priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Priority(self: OptimizationObjective) -> float

"""

    Structure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Structure(self: OptimizationObjective) -> Structure

"""

    StructureId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StructureId(self: OptimizationObjective) -> str

"""



class OptimizationEUDObjective(OptimizationObjective, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: OptimizationEUDObjective, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Dose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dose(self: OptimizationEUDObjective) -> DoseValue

"""

    ParameterA = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParameterA(self: OptimizationEUDObjective) -> float

"""



class OptimizationParameter(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def Equals(self, obj):
        """ Equals(self: OptimizationParameter, obj: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: OptimizationParameter) -> int """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: OptimizationParameter, writer: XmlWriter) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass


class OptimizationExcludeStructureParameter(OptimizationParameter, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: OptimizationExcludeStructureParameter, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Structure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Structure(self: OptimizationExcludeStructureParameter) -> Structure

"""



class OptimizationIMRTBeamParameter(OptimizationParameter, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: OptimizationIMRTBeamParameter, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Beam = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Beam(self: OptimizationIMRTBeamParameter) -> Beam

"""

    BeamId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BeamId(self: OptimizationIMRTBeamParameter) -> str

"""

    Excluded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Excluded(self: OptimizationIMRTBeamParameter) -> bool

"""

    FixedJaws = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FixedJaws(self: OptimizationIMRTBeamParameter) -> bool

"""

    SmoothX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmoothX(self: OptimizationIMRTBeamParameter) -> float

"""

    SmoothY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmoothY(self: OptimizationIMRTBeamParameter) -> float

"""



class OptimizationJawTrackingUsedParameter(OptimizationParameter, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: OptimizationJawTrackingUsedParameter, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class OptimizationLineObjective(OptimizationObjective, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: OptimizationLineObjective, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    CurveData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurveData(self: OptimizationLineObjective) -> Array[DVHPoint]

"""



class OptimizationMeanDoseObjective(OptimizationObjective, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: OptimizationMeanDoseObjective, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Dose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dose(self: OptimizationMeanDoseObjective) -> DoseValue

"""



class OptimizationNormalTissueParameter(OptimizationParameter, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: OptimizationNormalTissueParameter, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DistanceFromTargetBorderInMM = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DistanceFromTargetBorderInMM(self: OptimizationNormalTissueParameter) -> float

"""

    EndDosePercentage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndDosePercentage(self: OptimizationNormalTissueParameter) -> float

"""

    FallOff = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FallOff(self: OptimizationNormalTissueParameter) -> float

"""

    IsAutomatic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAutomatic(self: OptimizationNormalTissueParameter) -> bool

"""

    Priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Priority(self: OptimizationNormalTissueParameter) -> float

"""

    StartDosePercentage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartDosePercentage(self: OptimizationNormalTissueParameter) -> float

"""



class OptimizationPointCloudParameter(OptimizationParameter, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: OptimizationPointCloudParameter, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    PointResolutionInMM = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointResolutionInMM(self: OptimizationPointCloudParameter) -> float

"""

    Structure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Structure(self: OptimizationPointCloudParameter) -> Structure

"""



class OptimizationPointObjective(OptimizationObjective, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: OptimizationPointObjective, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Dose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dose(self: OptimizationPointObjective) -> DoseValue

"""

    Volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Volume(self: OptimizationPointObjective) -> float

"""



class OptimizationSetup(SerializableObject, IXmlSerializable):
    # no doc
    def AddAutomaticNormalTissueObjective(self, priority):
        """ AddAutomaticNormalTissueObjective(self: OptimizationSetup, priority: float) -> OptimizationNormalTissueParameter """
        pass

    def AddBeamSpecificParameter(self, beam, smoothX, smoothY, fixedJaws):
        """ AddBeamSpecificParameter(self: OptimizationSetup, beam: Beam, smoothX: float, smoothY: float, fixedJaws: bool) -> OptimizationIMRTBeamParameter """
        pass

    def AddEUDObjective(self, structure, objectiveOperator, dose, parameterA, priority):
        """ AddEUDObjective(self: OptimizationSetup, structure: Structure, objectiveOperator: OptimizationObjectiveOperator, dose: DoseValue, parameterA: float, priority: float) -> OptimizationEUDObjective """
        pass

    def AddMeanDoseObjective(self, structure, dose, priority):
        """ AddMeanDoseObjective(self: OptimizationSetup, structure: Structure, dose: DoseValue, priority: float) -> OptimizationMeanDoseObjective """
        pass

    def AddNormalTissueObjective(self, priority, distanceFromTargetBorderInMM, startDosePercentage, endDosePercentage, fallOff):
        """ AddNormalTissueObjective(self: OptimizationSetup, priority: float, distanceFromTargetBorderInMM: float, startDosePercentage: float, endDosePercentage: float, fallOff: float) -> OptimizationNormalTissueParameter """
        pass

    def AddPointObjective(self, structure, objectiveOperator, dose, volume, priority):
        """ AddPointObjective(self: OptimizationSetup, structure: Structure, objectiveOperator: OptimizationObjectiveOperator, dose: DoseValue, volume: float, priority: float) -> OptimizationPointObjective """
        pass

    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def RemoveObjective(self, objective):
        """ RemoveObjective(self: OptimizationSetup, objective: OptimizationObjective) """
        pass

    def RemoveParameter(self, parameter):
        """ RemoveParameter(self: OptimizationSetup, parameter: OptimizationParameter) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: OptimizationSetup, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Objectives = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Objectives(self: OptimizationSetup) -> IEnumerable[OptimizationObjective]

"""

    Parameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parameters(self: OptimizationSetup) -> IEnumerable[OptimizationParameter]

"""

    UseJawTracking = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseJawTracking(self: OptimizationSetup) -> bool

Set: UseJawTracking(self: OptimizationSetup) = value
"""



class OptimizerDVH(object):
    # no doc
    CurveData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurveData(self: OptimizerDVH) -> Array[DVHPoint]

"""

    Structure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Structure(self: OptimizerDVH) -> Structure

"""



class OptimizerObjectiveValue(object):
    # no doc
    Structure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Structure(self: OptimizerObjectiveValue) -> Structure

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: OptimizerObjectiveValue) -> float

"""



class OptimizerResult(CalculationResult):
    # no doc
    NumberOfIMRTOptimizerIterations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfIMRTOptimizerIterations(self: OptimizerResult) -> int

"""

    StructureDVHs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StructureDVHs(self: OptimizerResult) -> IEnumerable[OptimizerDVH]

"""

    StructureObjectiveValues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StructureObjectiveValues(self: OptimizerResult) -> IEnumerable[OptimizerObjectiveValue]

"""

    TotalObjectiveFunctionValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalObjectiveFunctionValue(self: OptimizerResult) -> float

"""



class Patient(ApiDataObject, IXmlSerializable):
    # no doc
    def AddCourse(self):
        """ AddCourse(self: Patient) -> Course """
        pass

    def AddEmptyPhantom(self, imageId, orientation, xSizePixel, ySizePixel, widthMM, heightMM, nrOfPlanes, planeSepMM):
        """ AddEmptyPhantom(self: Patient, imageId: str, orientation: PatientOrientation, xSizePixel: int, ySizePixel: int, widthMM: float, heightMM: float, nrOfPlanes: int, planeSepMM: float) -> StructureSet """
        pass

    def BeginModifications(self):
        """ BeginModifications(self: Patient) """
        pass

    def CanAddCourse(self):
        """ CanAddCourse(self: Patient) -> bool """
        pass

    def CanAddEmptyPhantom(self, errorMessage):
        """ CanAddEmptyPhantom(self: Patient) -> (bool, str) """
        pass

    def CanCopyImageFromOtherPatient(self, targetStudy, otherPatientId, otherPatientStudyId, otherPatient3DImageId, errorMessage):
        """ CanCopyImageFromOtherPatient(self: Patient, targetStudy: Study, otherPatientId: str, otherPatientStudyId: str, otherPatient3DImageId: str) -> (bool, str) """
        pass

    def CanModifyData(self):
        """ CanModifyData(self: Patient) -> bool """
        pass

    def CanRemoveCourse(self, course):
        """ CanRemoveCourse(self: Patient, course: Course) -> bool """
        pass

    def CanRemoveEmptyPhantom(self, structureset, errorMessage):
        """ CanRemoveEmptyPhantom(self: Patient, structureset: StructureSet) -> (bool, str) """
        pass

    def CopyImageFromOtherPatient(self, *__args):
        """
        CopyImageFromOtherPatient(self: Patient, otherPatientId: str, otherPatientStudyId: str, otherPatient3DImageId: str) -> StructureSet
        CopyImageFromOtherPatient(self: Patient, targetStudy: Study, otherPatientId: str, otherPatientStudyId: str, otherPatient3DImageId: str) -> StructureSet
        """
        pass

    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def RemoveCourse(self, course):
        """ RemoveCourse(self: Patient, course: Course) """
        pass

    def RemoveEmptyPhantom(self, structureset):
        """ RemoveEmptyPhantom(self: Patient, structureset: StructureSet) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: Patient, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Courses = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Courses(self: Patient) -> IEnumerable[Course]

"""

    CreationDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreationDateTime(self: Patient) -> Nullable[DateTime]

"""

    DateOfBirth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DateOfBirth(self: Patient) -> Nullable[DateTime]

"""

    FirstName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FirstName(self: Patient) -> str

"""

    HasModifiedData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasModifiedData(self: Patient) -> bool

"""

    Hospital = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Hospital(self: Patient) -> Hospital

"""

    Id2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id2(self: Patient) -> str

"""

    LastName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LastName(self: Patient) -> str

"""

    MiddleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MiddleName(self: Patient) -> str

"""

    PrimaryOncologistId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrimaryOncologistId(self: Patient) -> str

"""

    Registrations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Registrations(self: Patient) -> IEnumerable[Registration]

"""

    Sex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Sex(self: Patient) -> str

"""

    SSN = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SSN(self: Patient) -> str

"""

    StructureSets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StructureSets(self: Patient) -> IEnumerable[StructureSet]

"""

    Studies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Studies(self: Patient) -> IEnumerable[Study]

"""



class PatientSummary(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: PatientSummary, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    CreationDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreationDateTime(self: PatientSummary) -> Nullable[DateTime]

"""

    DateOfBirth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DateOfBirth(self: PatientSummary) -> Nullable[DateTime]

"""

    FirstName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FirstName(self: PatientSummary) -> str

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: PatientSummary) -> str

"""

    Id2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id2(self: PatientSummary) -> str

"""

    LastName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LastName(self: PatientSummary) -> str

"""

    MiddleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MiddleName(self: PatientSummary) -> str

"""

    Sex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Sex(self: PatientSummary) -> str

"""

    SSN = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SSN(self: PatientSummary) -> str

"""



class PlanningItemDose(Dose, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: PlanningItemDose, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class PlanSum(PlanningItem, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetPlanSumOperation(self, planSetupInPlanSum):
        """ GetPlanSumOperation(self: PlanSum, planSetupInPlanSum: PlanSetup) -> PlanSumOperation """
        pass

    def GetPlanWeight(self, planSetupInPlanSum):
        """ GetPlanWeight(self: PlanSum, planSetupInPlanSum: PlanSetup) -> float """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: PlanSum, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Course = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Course(self: PlanSum) -> Course

"""

    PlanSetups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlanSetups(self: PlanSum) -> IEnumerable[PlanSetup]

"""

    PlanSumComponents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlanSumComponents(self: PlanSum) -> IEnumerable[PlanSumComponent]

"""



class PlanSumComponent(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: PlanSumComponent, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    PlanSetupId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlanSetupId(self: PlanSumComponent) -> str

"""

    PlanSumOperation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlanSumOperation(self: PlanSumComponent) -> PlanSumOperation

"""

    PlanWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlanWeight(self: PlanSumComponent) -> float

"""



class PlanTreatmentSession(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: PlanTreatmentSession, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    PlanSetup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlanSetup(self: PlanTreatmentSession) -> PlanSetup

"""

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Status(self: PlanTreatmentSession) -> TreatmentSessionStatus

"""

    TreatmentSession = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TreatmentSession(self: PlanTreatmentSession) -> TreatmentSession

"""



class PlanUncertainty(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetDVHCumulativeData(self, structure, dosePresentation, volumePresentation, binWidth):
        """ GetDVHCumulativeData(self: PlanUncertainty, structure: Structure, dosePresentation: DoseValuePresentation, volumePresentation: VolumePresentation, binWidth: float) -> DVHData """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: PlanUncertainty, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BeamUncertainties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BeamUncertainties(self: PlanUncertainty) -> IEnumerable[BeamUncertainty]

"""

    CalibrationCurveError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CalibrationCurveError(self: PlanUncertainty) -> float

"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayName(self: PlanUncertainty) -> str

"""

    Dose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dose(self: PlanUncertainty) -> Dose

"""

    IsocenterShift = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsocenterShift(self: PlanUncertainty) -> VVector

"""

    UncertaintyType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UncertaintyType(self: PlanUncertainty) -> PlanUncertaintyType

"""



class ProtocolPhaseMeasure(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: ProtocolPhaseMeasure, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ActualValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActualValue(self: ProtocolPhaseMeasure) -> float

"""

    Modifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Modifier(self: ProtocolPhaseMeasure) -> MeasureModifier

"""

    StructureId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StructureId(self: ProtocolPhaseMeasure) -> str

"""

    TargetIsMet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TargetIsMet(self: ProtocolPhaseMeasure) -> Nullable[bool]

"""

    TargetValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TargetValue(self: ProtocolPhaseMeasure) -> float

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: ProtocolPhaseMeasure) -> MeasureType

"""

    TypeText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeText(self: ProtocolPhaseMeasure) -> str

"""



class ProtocolPhasePrescription(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: ProtocolPhasePrescription, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ActualTotalDose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActualTotalDose(self: ProtocolPhasePrescription) -> DoseValue

"""

    PrescModifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrescModifier(self: ProtocolPhasePrescription) -> PrescriptionModifier

"""

    PrescParameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrescParameter(self: ProtocolPhasePrescription) -> float

"""

    PrescType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrescType(self: ProtocolPhasePrescription) -> PrescriptionType

"""

    StructureId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StructureId(self: ProtocolPhasePrescription) -> str

"""

    TargetFractionDose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TargetFractionDose(self: ProtocolPhasePrescription) -> DoseValue

"""

    TargetIsMet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TargetIsMet(self: ProtocolPhasePrescription) -> Nullable[bool]

"""

    TargetTotalDose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TargetTotalDose(self: ProtocolPhasePrescription) -> DoseValue

"""



class RadioactiveSource(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: RadioactiveSource, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CalibrationDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CalibrationDate(self: RadioactiveSource) -> Nullable[DateTime]

"""

    NominalActivity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NominalActivity(self: RadioactiveSource) -> bool

"""

    RadioactiveSourceModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RadioactiveSourceModel(self: RadioactiveSource) -> RadioactiveSourceModel

"""

    SerialNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SerialNumber(self: RadioactiveSource) -> str

"""

    Strength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Strength(self: RadioactiveSource) -> float

"""



class RadioactiveSourceModel(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: RadioactiveSourceModel, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ActiveSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveSize(self: RadioactiveSourceModel) -> VVector

"""

    ActivityConversionFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActivityConversionFactor(self: RadioactiveSourceModel) -> float

"""

    CalculationModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CalculationModel(self: RadioactiveSourceModel) -> str

"""

    DoseRateConstant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DoseRateConstant(self: RadioactiveSourceModel) -> float

"""

    HalfLife = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HalfLife(self: RadioactiveSourceModel) -> float

"""

    LiteratureReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LiteratureReference(self: RadioactiveSourceModel) -> str

"""

    Manufacturer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Manufacturer(self: RadioactiveSourceModel) -> str

"""

    SourceType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SourceType(self: RadioactiveSourceModel) -> str

"""

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Status(self: RadioactiveSourceModel) -> str

"""

    StatusDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StatusDate(self: RadioactiveSourceModel) -> Nullable[DateTime]

"""

    StatusUserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StatusUserName(self: RadioactiveSourceModel) -> str

"""



class RangeModulator(AddOn, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: RangeModulator, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: RangeModulator) -> RangeModulatorType

"""



class RangeModulatorSettings(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: RangeModulatorSettings, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    IsocenterToRangeModulatorDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsocenterToRangeModulatorDistance(self: RangeModulatorSettings) -> float

"""

    RangeModulatorGatingStartValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RangeModulatorGatingStartValue(self: RangeModulatorSettings) -> float

"""

    RangeModulatorGatingStarWaterEquivalentThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RangeModulatorGatingStarWaterEquivalentThickness(self: RangeModulatorSettings) -> float

"""

    RangeModulatorGatingStopValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RangeModulatorGatingStopValue(self: RangeModulatorSettings) -> float

"""

    RangeModulatorGatingStopWaterEquivalentThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RangeModulatorGatingStopWaterEquivalentThickness(self: RangeModulatorSettings) -> float

"""

    ReferencedRangeModulator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferencedRangeModulator(self: RangeModulatorSettings) -> RangeModulator

"""



class RangeShifter(AddOn, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: RangeShifter, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: RangeShifter) -> RangeShifterType

"""



class RangeShifterSettings(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: RangeShifterSettings, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    IsocenterToRangeShifterDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsocenterToRangeShifterDistance(self: RangeShifterSettings) -> float

"""

    RangeShifterSetting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RangeShifterSetting(self: RangeShifterSettings) -> str

"""

    RangeShifterWaterEquivalentThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RangeShifterWaterEquivalentThickness(self: RangeShifterSettings) -> float

"""

    ReferencedRangeShifter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferencedRangeShifter(self: RangeShifterSettings) -> RangeShifter

"""



class ReferencePoint(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetReferencePointLocation(self, planSetup):
        """ GetReferencePointLocation(self: ReferencePoint, planSetup: PlanSetup) -> VVector """
        pass

    def HasLocation(self, planSetup):
        """ HasLocation(self: ReferencePoint, planSetup: PlanSetup) -> bool """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: ReferencePoint, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DailyDoseLimit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DailyDoseLimit(self: ReferencePoint) -> DoseValue

Set: DailyDoseLimit(self: ReferencePoint) = value
"""

    PatientVolumeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PatientVolumeId(self: ReferencePoint) -> str

"""

    SessionDoseLimit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SessionDoseLimit(self: ReferencePoint) -> DoseValue

Set: SessionDoseLimit(self: ReferencePoint) = value
"""

    TotalDoseLimit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalDoseLimit(self: ReferencePoint) -> DoseValue

Set: TotalDoseLimit(self: ReferencePoint) = value
"""



class Registration(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def InverseTransformPoint(self, pt):
        """ InverseTransformPoint(self: Registration, pt: VVector) -> VVector """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def TransformPoint(self, pt):
        """ TransformPoint(self: Registration, pt: VVector) -> VVector """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: Registration, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CreationDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreationDateTime(self: Registration) -> Nullable[DateTime]

"""

    RegisteredFOR = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RegisteredFOR(self: Registration) -> str

"""

    SourceFOR = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SourceFOR(self: Registration) -> str

"""

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Status(self: Registration) -> RegistrationApprovalStatus

"""

    StatusDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StatusDateTime(self: Registration) -> Nullable[DateTime]

"""

    StatusUserDisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StatusUserDisplayName(self: Registration) -> str

"""

    StatusUserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StatusUserName(self: Registration) -> str

"""

    TransformationMatrix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransformationMatrix(self: Registration) -> Array[float]

"""

    UID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UID(self: Registration) -> str

"""



class RTPrescription(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: RTPrescription, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BolusFrequency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BolusFrequency(self: RTPrescription) -> str

"""

    BolusThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BolusThickness(self: RTPrescription) -> str

"""

    Energies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Energies(self: RTPrescription) -> IEnumerable[str]

"""

    EnergyModes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EnergyModes(self: RTPrescription) -> IEnumerable[str]

"""

    Gating = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Gating(self: RTPrescription) -> str

"""

    LatestRevision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LatestRevision(self: RTPrescription) -> RTPrescription

"""

    Notes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Notes(self: RTPrescription) -> str

"""

    NumberOfFractions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfFractions(self: RTPrescription) -> Nullable[int]

"""

    OrgansAtRisk = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrgansAtRisk(self: RTPrescription) -> IEnumerable[RTPrescriptionOrganAtRisk]

"""

    PhaseType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PhaseType(self: RTPrescription) -> str

"""

    PredecessorPrescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PredecessorPrescription(self: RTPrescription) -> RTPrescription

"""

    RevisionNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RevisionNumber(self: RTPrescription) -> int

"""

    SimulationNeeded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SimulationNeeded(self: RTPrescription) -> Nullable[bool]

"""

    Site = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Site(self: RTPrescription) -> str

"""

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Status(self: RTPrescription) -> str

"""

    TargetConstraintsWithoutTargetLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TargetConstraintsWithoutTargetLevel(self: RTPrescription) -> IEnumerable[RTPrescriptionTargetConstraints]

"""

    Targets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Targets(self: RTPrescription) -> IEnumerable[RTPrescriptionTarget]

"""

    Technique = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Technique(self: RTPrescription) -> str

"""



class RTPrescriptionConstraint(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: RTPrescriptionConstraint, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ConstraintType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConstraintType(self: RTPrescriptionConstraint) -> RTPrescriptionConstraintType

"""

    Unit1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Unit1(self: RTPrescriptionConstraint) -> str

"""

    Unit2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Unit2(self: RTPrescriptionConstraint) -> str

"""

    Value1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value1(self: RTPrescriptionConstraint) -> str

"""

    Value2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value2(self: RTPrescriptionConstraint) -> str

"""



class RTPrescriptionOrganAtRisk(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: RTPrescriptionOrganAtRisk, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Constraints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Constraints(self: RTPrescriptionOrganAtRisk) -> IEnumerable[RTPrescriptionConstraint]

"""

    OrganAtRiskId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrganAtRiskId(self: RTPrescriptionOrganAtRisk) -> str

"""



class RTPrescriptionTarget(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: RTPrescriptionTarget, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Constraints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Constraints(self: RTPrescriptionTarget) -> IEnumerable[RTPrescriptionConstraint]

"""

    DosePerFraction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DosePerFraction(self: RTPrescriptionTarget) -> DoseValue

"""

    NumberOfFractions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfFractions(self: RTPrescriptionTarget) -> int

"""

    TargetId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TargetId(self: RTPrescriptionTarget) -> str

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: RTPrescriptionTarget) -> RTPrescriptionTargetType

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: RTPrescriptionTarget) -> float

"""



class RTPrescriptionTargetConstraints(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: RTPrescriptionTargetConstraints, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Constraints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Constraints(self: RTPrescriptionTargetConstraints) -> IEnumerable[RTPrescriptionConstraint]

"""

    TargetId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TargetId(self: RTPrescriptionTargetConstraints) -> str

"""



class ScriptContext(object):
    """ ScriptContext(context: object, user: object, appName: str) """
    @staticmethod # known case of __new__
    def __new__(self, context, user, appName):
        """ __new__(cls: type, context: object, user: object, appName: str) """
        pass

    ApplicationName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplicationName(self: ScriptContext) -> str

"""

    BrachyPlanSetup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BrachyPlanSetup(self: ScriptContext) -> BrachyPlanSetup

"""

    BrachyPlansInScope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BrachyPlansInScope(self: ScriptContext) -> IEnumerable[BrachyPlanSetup]

"""

    Course = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Course(self: ScriptContext) -> Course

"""

    CurrentUser = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentUser(self: ScriptContext) -> User

"""

    ExternalPlanSetup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExternalPlanSetup(self: ScriptContext) -> ExternalPlanSetup

"""

    ExternalPlansInScope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExternalPlansInScope(self: ScriptContext) -> IEnumerable[ExternalPlanSetup]

"""

    Image = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Image(self: ScriptContext) -> Image

"""

    IonPlanSetup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IonPlanSetup(self: ScriptContext) -> IonPlanSetup

"""

    IonPlansInScope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IonPlansInScope(self: ScriptContext) -> IEnumerable[IonPlanSetup]

"""

    Patient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Patient(self: ScriptContext) -> Patient

"""

    PlanSetup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlanSetup(self: ScriptContext) -> PlanSetup

"""

    PlansInScope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlansInScope(self: ScriptContext) -> IEnumerable[PlanSetup]

"""

    PlanSumsInScope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlanSumsInScope(self: ScriptContext) -> IEnumerable[PlanSum]

"""

    StructureSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StructureSet(self: ScriptContext) -> StructureSet

"""

    VersionInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VersionInfo(self: ScriptContext) -> str

"""



class ScriptEnvironment(object):
    """ ScriptEnvironment(appName: str, scripts: IEnumerable[IApplicationScript], scriptExecutionEngine: Action[Assembly, object, Window, object]) """
    def ExecuteScript(self, scriptAssembly, scriptContext, window):
        """ ExecuteScript(self: ScriptEnvironment, scriptAssembly: Assembly, scriptContext: ScriptContext, window: Window) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, appName, scripts, scriptExecutionEngine):
        """ __new__(cls: type, appName: str, scripts: IEnumerable[IApplicationScript], scriptExecutionEngine: Action[Assembly, object, Window, object]) """
        pass

    ApiVersionInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApiVersionInfo(self: ScriptEnvironment) -> str

"""

    ApplicationName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplicationName(self: ScriptEnvironment) -> str

"""

    Scripts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Scripts(self: ScriptEnvironment) -> IEnumerable[ApplicationScript]

"""

    VersionInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VersionInfo(self: ScriptEnvironment) -> str

"""



class SearchBodyParameters(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def LoadDefaults(self):
        """ LoadDefaults(self: SearchBodyParameters) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: SearchBodyParameters, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    FillAllCavities = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FillAllCavities(self: SearchBodyParameters) -> bool

Set: FillAllCavities(self: SearchBodyParameters) = value
"""

    KeepLargestParts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: KeepLargestParts(self: SearchBodyParameters) -> bool

Set: KeepLargestParts(self: SearchBodyParameters) = value
"""

    LowerHUThreshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LowerHUThreshold(self: SearchBodyParameters) -> int

Set: LowerHUThreshold(self: SearchBodyParameters) = value
"""

    MREdgeThresholdHigh = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MREdgeThresholdHigh(self: SearchBodyParameters) -> int

Set: MREdgeThresholdHigh(self: SearchBodyParameters) = value
"""

    MREdgeThresholdLow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MREdgeThresholdLow(self: SearchBodyParameters) -> int

Set: MREdgeThresholdLow(self: SearchBodyParameters) = value
"""

    NumberOfLargestPartsToKeep = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfLargestPartsToKeep(self: SearchBodyParameters) -> int

Set: NumberOfLargestPartsToKeep(self: SearchBodyParameters) = value
"""

    PreCloseOpenings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreCloseOpenings(self: SearchBodyParameters) -> bool

Set: PreCloseOpenings(self: SearchBodyParameters) = value
"""

    PreCloseOpeningsRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreCloseOpeningsRadius(self: SearchBodyParameters) -> float

Set: PreCloseOpeningsRadius(self: SearchBodyParameters) = value
"""

    PreDisconnect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreDisconnect(self: SearchBodyParameters) -> bool

Set: PreDisconnect(self: SearchBodyParameters) = value
"""

    PreDisconnectRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreDisconnectRadius(self: SearchBodyParameters) -> float

Set: PreDisconnectRadius(self: SearchBodyParameters) = value
"""

    Smoothing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Smoothing(self: SearchBodyParameters) -> bool

Set: Smoothing(self: SearchBodyParameters) = value
"""

    SmoothingLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmoothingLevel(self: SearchBodyParameters) -> int

Set: SmoothingLevel(self: SearchBodyParameters) = value
"""



class SeedCollection(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: SeedCollection, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BrachyFieldReferencePoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BrachyFieldReferencePoints(self: SeedCollection) -> IEnumerable[BrachyFieldReferencePoint]

"""

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Color(self: SeedCollection) -> Color

"""

    SourcePositions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SourcePositions(self: SeedCollection) -> IEnumerable[SourcePosition]

"""



class SegmentVolume(SerializableObject, IXmlSerializable):
    # no doc
    def And(self, other):
        """ And(self: SegmentVolume, other: SegmentVolume) -> SegmentVolume """
        pass

    def AsymmetricMargin(self, margins):
        """ AsymmetricMargin(self: SegmentVolume, margins: AxisAlignedMargins) -> SegmentVolume """
        pass

    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def Margin(self, marginInMM):
        """ Margin(self: SegmentVolume, marginInMM: float) -> SegmentVolume """
        pass

    def Not(self):
        """ Not(self: SegmentVolume) -> SegmentVolume """
        pass

    def Or(self, other):
        """ Or(self: SegmentVolume, other: SegmentVolume) -> SegmentVolume """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def Sub(self, other):
        """ Sub(self: SegmentVolume, other: SegmentVolume) -> SegmentVolume """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: SegmentVolume, writer: XmlWriter) """
        pass

    def Xor(self, other):
        """ Xor(self: SegmentVolume, other: SegmentVolume) -> SegmentVolume """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class Series(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def SetImagingDevice(self, imagingDeviceId):
        """ SetImagingDevice(self: Series, imagingDeviceId: str) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: Series, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    FOR = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FOR(self: Series) -> str

"""

    Images = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Images(self: Series) -> IEnumerable[Image]

"""

    ImagingDeviceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ImagingDeviceId(self: Series) -> str

"""

    ImagingDeviceManufacturer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ImagingDeviceManufacturer(self: Series) -> str

"""

    ImagingDeviceModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ImagingDeviceModel(self: Series) -> str

"""

    ImagingDeviceSerialNo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ImagingDeviceSerialNo(self: Series) -> str

"""

    Modality = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Modality(self: Series) -> SeriesModality

"""

    Study = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Study(self: Series) -> Study

"""

    UID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UID(self: Series) -> str

"""



class Slot(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: Slot, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Number(self: Slot) -> int

"""



class SourcePosition(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: SourcePosition, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DwellTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DwellTime(self: SourcePosition) -> float

"""

    RadioactiveSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RadioactiveSource(self: SourcePosition) -> RadioactiveSource

"""

    Transform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Transform(self: SourcePosition) -> Array[float]

"""

    Translation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Translation(self: SourcePosition) -> VVector

"""



class StandardWedge(Wedge, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: StandardWedge, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class Structure(ApiDataObject, IXmlSerializable):
    # no doc
    def AddContourOnImagePlane(self, contour, z):
        """ AddContourOnImagePlane(self: Structure, contour: Array[VVector], z: int) """
        pass

    def And(self, other):
        """ And(self: Structure, other: SegmentVolume) -> SegmentVolume """
        pass

    def AsymmetricMargin(self, margins):
        """ AsymmetricMargin(self: Structure, margins: AxisAlignedMargins) -> SegmentVolume """
        pass

    def CanConvertToHighResolution(self):
        """ CanConvertToHighResolution(self: Structure) -> bool """
        pass

    def CanEditSegmentVolume(self, errorMessage):
        """ CanEditSegmentVolume(self: Structure) -> (bool, str) """
        pass

    def CanSetAssignedHU(self, errorMessage):
        """ CanSetAssignedHU(self: Structure) -> (bool, str) """
        pass

    def ClearAllContoursOnImagePlane(self, z):
        """ ClearAllContoursOnImagePlane(self: Structure, z: int) """
        pass

    def ConvertDoseLevelToStructure(self, dose, doseLevel):
        """ ConvertDoseLevelToStructure(self: Structure, dose: Dose, doseLevel: DoseValue) """
        pass

    def ConvertToHighResolution(self):
        """ ConvertToHighResolution(self: Structure) """
        pass

    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetAssignedHU(self, huValue):
        """ GetAssignedHU(self: Structure) -> (bool, float) """
        pass

    def GetContoursOnImagePlane(self, z):
        """ GetContoursOnImagePlane(self: Structure, z: int) -> Array[Array[VVector]] """
        pass

    def GetNumberOfSeparateParts(self):
        """ GetNumberOfSeparateParts(self: Structure) -> int """
        pass

    def GetReferenceLinePoints(self):
        """ GetReferenceLinePoints(self: Structure) -> Array[VVector] """
        pass

    def GetSegmentProfile(self, start, stop, preallocatedBuffer):
        """ GetSegmentProfile(self: Structure, start: VVector, stop: VVector, preallocatedBuffer: BitArray) -> SegmentProfile """
        pass

    def IsPointInsideSegment(self, point):
        """ IsPointInsideSegment(self: Structure, point: VVector) -> bool """
        pass

    def Margin(self, marginInMM):
        """ Margin(self: Structure, marginInMM: float) -> SegmentVolume """
        pass

    def Not(self):
        """ Not(self: Structure) -> SegmentVolume """
        pass

    def Or(self, other):
        """ Or(self: Structure, other: SegmentVolume) -> SegmentVolume """
        pass

    def ResetAssignedHU(self):
        """ ResetAssignedHU(self: Structure) -> bool """
        pass

    def SetAssignedHU(self, huValue):
        """ SetAssignedHU(self: Structure, huValue: float) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def Sub(self, other):
        """ Sub(self: Structure, other: SegmentVolume) -> SegmentVolume """
        pass

    def SubtractContourOnImagePlane(self, contour, z):
        """ SubtractContourOnImagePlane(self: Structure, contour: Array[VVector], z: int) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: Structure, writer: XmlWriter) """
        pass

    def Xor(self, other):
        """ Xor(self: Structure, other: SegmentVolume) -> SegmentVolume """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ApprovalHistory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApprovalHistory(self: Structure) -> IEnumerable[StructureApprovalHistoryEntry]

"""

    CenterPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CenterPoint(self: Structure) -> VVector

"""

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Color(self: Structure) -> Color

"""

    DicomType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DicomType(self: Structure) -> str

"""

    HasSegment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasSegment(self: Structure) -> bool

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: Structure) -> str

Set: Id(self: Structure) = value
"""

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEmpty(self: Structure) -> bool

"""

    IsHighResolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsHighResolution(self: Structure) -> bool

"""

    MeshGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MeshGeometry(self: Structure) -> MeshGeometry3D

"""

    ROINumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ROINumber(self: Structure) -> int

"""

    SegmentVolume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SegmentVolume(self: Structure) -> SegmentVolume

Set: SegmentVolume(self: Structure) = value
"""

    StructureCodeInfos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StructureCodeInfos(self: Structure) -> IEnumerable[StructureCodeInfo]

"""

    Volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Volume(self: Structure) -> float

"""



class StructureSet(ApiDataObject, IXmlSerializable):
    # no doc
    def AddStructure(self, dicomType, id):
        """ AddStructure(self: StructureSet, dicomType: str, id: str) -> Structure """
        pass

    def CanAddStructure(self, dicomType, id):
        """ CanAddStructure(self: StructureSet, dicomType: str, id: str) -> bool """
        pass

    def CanRemoveStructure(self, structure):
        """ CanRemoveStructure(self: StructureSet, structure: Structure) -> bool """
        pass

    def Copy(self):
        """ Copy(self: StructureSet) -> StructureSet """
        pass

    def CreateAndSearchBody(self, parameters):
        """ CreateAndSearchBody(self: StructureSet, parameters: SearchBodyParameters) -> Structure """
        pass

    def Delete(self):
        """ Delete(self: StructureSet) """
        pass

    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetDefaultSearchBodyParameters(self):
        """ GetDefaultSearchBodyParameters(self: StructureSet) -> SearchBodyParameters """
        pass

    def RemoveStructure(self, structure):
        """ RemoveStructure(self: StructureSet, structure: Structure) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: StructureSet, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ApplicationScriptLogs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplicationScriptLogs(self: StructureSet) -> IEnumerable[ApplicationScriptLog]

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: StructureSet) -> str

Set: Id(self: StructureSet) = value
"""

    Image = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Image(self: StructureSet) -> Image

"""

    Patient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Patient(self: StructureSet) -> Patient

"""

    Structures = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Structures(self: StructureSet) -> IEnumerable[Structure]

"""

    UID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UID(self: StructureSet) -> str

"""



class Study(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: Study, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CreationDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreationDateTime(self: Study) -> Nullable[DateTime]

"""

    Series = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Series(self: Study) -> IEnumerable[Series]

"""

    UID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UID(self: Study) -> str

"""



class Technique(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: Technique, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class TradeoffExplorationContext(object):
    # no doc
    def AddTargetHomogeneityObjective(self, targetStructure):
        """ AddTargetHomogeneityObjective(self: TradeoffExplorationContext, targetStructure: Structure) -> bool """
        pass

    def AddTradeoffObjective(self, *__args):
        """
        AddTradeoffObjective(self: TradeoffExplorationContext, structure: Structure) -> bool
        AddTradeoffObjective(self: TradeoffExplorationContext, objective: OptimizationObjective) -> bool
        """
        pass

    def ApplyTradeoffExplorationResult(self):
        """ ApplyTradeoffExplorationResult(self: TradeoffExplorationContext) """
        pass

    def CreateDeliverableVmatPlan(self, useIntermediateDose):
        """ CreateDeliverableVmatPlan(self: TradeoffExplorationContext, useIntermediateDose: bool) -> bool """
        pass

    def CreatePlanCollection(self, continueOptimization, intermediateDoseMode, useHybridOptimizationForVmat):
        """ CreatePlanCollection(self: TradeoffExplorationContext, continueOptimization: bool, intermediateDoseMode: TradeoffPlanGenerationIntermediateDoseMode, useHybridOptimizationForVmat: bool) -> bool """
        pass

    def GetObjectiveCost(self, objective):
        """ GetObjectiveCost(self: TradeoffExplorationContext, objective: TradeoffObjective) -> float """
        pass

    def GetObjectiveLowerLimit(self, objective):
        """ GetObjectiveLowerLimit(self: TradeoffExplorationContext, objective: TradeoffObjective) -> float """
        pass

    def GetObjectiveUpperLimit(self, objective):
        """ GetObjectiveUpperLimit(self: TradeoffExplorationContext, objective: TradeoffObjective) -> float """
        pass

    def GetObjectiveUpperRestrictor(self, objective):
        """ GetObjectiveUpperRestrictor(self: TradeoffExplorationContext, objective: TradeoffObjective) -> float """
        pass

    def GetStructureDvh(self, structure):
        """ GetStructureDvh(self: TradeoffExplorationContext, structure: Structure) -> DVHData """
        pass

    def LoadSavedPlanCollection(self):
        """ LoadSavedPlanCollection(self: TradeoffExplorationContext) -> bool """
        pass

    def RemoveAllTradeoffObjectives(self):
        """ RemoveAllTradeoffObjectives(self: TradeoffExplorationContext) """
        pass

    def RemovePlanCollection(self):
        """ RemovePlanCollection(self: TradeoffExplorationContext) """
        pass

    def RemoveTargetHomogeneityObjective(self, targetStructure):
        """ RemoveTargetHomogeneityObjective(self: TradeoffExplorationContext, targetStructure: Structure) -> bool """
        pass

    def RemoveTradeoffObjective(self, *__args):
        """
        RemoveTradeoffObjective(self: TradeoffExplorationContext, tradeoffObjective: TradeoffObjective) -> bool
        RemoveTradeoffObjective(self: TradeoffExplorationContext, structure: Structure) -> bool
        """
        pass

    def ResetToBalancedPlan(self):
        """ ResetToBalancedPlan(self: TradeoffExplorationContext) """
        pass

    def SetObjectiveCost(self, tradeoffObjective, cost):
        """ SetObjectiveCost(self: TradeoffExplorationContext, tradeoffObjective: TradeoffObjective, cost: float) """
        pass

    def SetObjectiveUpperRestrictor(self, tradeoffObjective, restrictorValue):
        """ SetObjectiveUpperRestrictor(self: TradeoffExplorationContext, tradeoffObjective: TradeoffObjective, restrictorValue: float) """
        pass

    CanCreatePlanCollection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanCreatePlanCollection(self: TradeoffExplorationContext) -> bool

"""

    CanLoadSavedPlanCollection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanLoadSavedPlanCollection(self: TradeoffExplorationContext) -> bool

"""

    CanUseHybridOptimizationInPlanGeneration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanUseHybridOptimizationInPlanGeneration(self: TradeoffExplorationContext) -> bool

"""

    CanUsePlanDoseAsIntermediateDose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanUsePlanDoseAsIntermediateDose(self: TradeoffExplorationContext) -> bool

"""

    CurrentDose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentDose(self: TradeoffExplorationContext) -> Dose

"""

    HasPlanCollection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasPlanCollection(self: TradeoffExplorationContext) -> bool

"""

    TargetStructures = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TargetStructures(self: TradeoffExplorationContext) -> IReadOnlyList[Structure]

"""

    TradeoffObjectiveCandidates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TradeoffObjectiveCandidates(self: TradeoffExplorationContext) -> IReadOnlyList[OptimizationObjective]

"""

    TradeoffObjectives = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TradeoffObjectives(self: TradeoffExplorationContext) -> IReadOnlyCollection[TradeoffObjective]

"""

    TradeoffStructureCandidates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TradeoffStructureCandidates(self: TradeoffExplorationContext) -> IReadOnlyList[Structure]

"""



class TradeoffObjective(object):
    # no doc
    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: TradeoffObjective) -> int

"""

    OptimizationObjectives = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OptimizationObjectives(self: TradeoffObjective) -> IEnumerable[OptimizationObjective]

"""

    Structure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Structure(self: TradeoffObjective) -> Structure

"""



class TradeoffPlanGenerationIntermediateDoseMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum TradeoffPlanGenerationIntermediateDoseMode, values: Calculate (2), NotUsed (0), UsePlanDose (1) """
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

    Calculate = None
    NotUsed = None
    UsePlanDose = None
    value__ = None


class Tray(AddOn, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: Tray, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class TreatmentPhase(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: TreatmentPhase, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    OtherInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OtherInfo(self: TreatmentPhase) -> str

"""

    PhaseGapNumberOfDays = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PhaseGapNumberOfDays(self: TreatmentPhase) -> int

"""

    Prescriptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Prescriptions(self: TreatmentPhase) -> IEnumerable[RTPrescription]

"""

    TimeGapType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TimeGapType(self: TreatmentPhase) -> str

"""



class TreatmentSession(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: TreatmentSession, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SessionNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SessionNumber(self: TreatmentSession) -> Int64

"""

    SessionPlans = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SessionPlans(self: TreatmentSession) -> IEnumerable[PlanTreatmentSession]

"""



class TreatmentUnitOperatingLimit(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: TreatmentUnitOperatingLimit, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Label(self: TreatmentUnitOperatingLimit) -> str

"""

    MaxValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxValue(self: TreatmentUnitOperatingLimit) -> float

"""

    MinValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinValue(self: TreatmentUnitOperatingLimit) -> float

"""

    Precision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Precision(self: TreatmentUnitOperatingLimit) -> Nullable[int]

"""

    UnitString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnitString(self: TreatmentUnitOperatingLimit) -> str

"""



class TreatmentUnitOperatingLimits(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: TreatmentUnitOperatingLimits, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    CollimatorAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CollimatorAngle(self: TreatmentUnitOperatingLimits) -> TreatmentUnitOperatingLimit

"""

    GantryAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GantryAngle(self: TreatmentUnitOperatingLimits) -> TreatmentUnitOperatingLimit

"""

    MU = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MU(self: TreatmentUnitOperatingLimits) -> TreatmentUnitOperatingLimit

"""

    PatientSupportAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PatientSupportAngle(self: TreatmentUnitOperatingLimits) -> TreatmentUnitOperatingLimit

"""



class TypeBasedIdValidator(object):
    # no doc
    @staticmethod
    def IsValidId(id, dataObject, errorHint):
        """ IsValidId(id: str, dataObject: ApiDataObject, errorHint: StringBuilder) -> bool """
        pass

    @staticmethod
    def ThrowIfNotValidId(id, dataObject):
        """ ThrowIfNotValidId(id: str, dataObject: ApiDataObject) """
        pass

    __all__ = [
        'IsValidId',
        'ThrowIfNotValidId',
    ]


class User(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        """ EndSerialization(self: SerializableObject) """
        pass

    def Equals(self, obj):
        """ Equals(self: User, obj: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: User) -> int """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def ToString(self):
        """ ToString(self: User) -> str """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: User, writer: XmlWriter) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: User) -> str

"""

    Language = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Language(self: User) -> str

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: User) -> str

"""



