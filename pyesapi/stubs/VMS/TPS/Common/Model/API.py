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
        # type: ()
        """ ClearSerializationHistory() """
        pass

    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetSchema(self):
        # type: (self: SerializableObject) -> XmlSchema
        """ GetSchema(self: SerializableObject) -> XmlSchema """
        pass

    def ReadXml(self, reader):
        # type: (self: SerializableObject, reader: XmlReader)
        """ ReadXml(self: SerializableObject, reader: XmlReader) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: SerializableObject, writer: XmlWriter)
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
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def Equals(self, obj):
        # type: (self: ApiDataObject, obj: object) -> bool
        """ Equals(self: ApiDataObject, obj: object) -> bool """
        pass

    def GetHashCode(self):
        # type: (self: ApiDataObject) -> int
        """ GetHashCode(self: ApiDataObject) -> int """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def ToString(self):
        # type: (self: ApiDataObject) -> str
        """ ToString(self: ApiDataObject) -> str """
        pass

    def WriteXml(self, writer):
        # type: (self: ApiDataObject, writer: XmlWriter)
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
    # type: (self: ApiDataObject) -> str
    """ Get: Comment(self: ApiDataObject) -> str """

    HistoryDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ApiDataObject) -> DateTime
    """ Get: HistoryDateTime(self: ApiDataObject) -> DateTime """

    HistoryUserDisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ApiDataObject) -> str
    """ Get: HistoryUserDisplayName(self: ApiDataObject) -> str """

    HistoryUserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ApiDataObject) -> str
    """ Get: HistoryUserName(self: ApiDataObject) -> str """

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ApiDataObject) -> str
    """ Get: Id(self: ApiDataObject) -> str """

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ApiDataObject) -> str
    """ Get: Name(self: ApiDataObject) -> str """



class AddOn(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: AddOn, writer: XmlWriter)
        """ WriteXml(self: AddOn, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CreationDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: AddOn) -> Nullable[DateTime]
    """ Get: CreationDateTime(self: AddOn) -> Nullable[DateTime] """



class AddOnMaterial(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: AddOnMaterial, writer: XmlWriter)
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
        # type: (self: Application)
        """ ClosePatient(self: Application) """
        pass

    @staticmethod
    def CreateApplication(username=None, password=None):
        # type: (username: str, password: str) -> Application
        """
        CreateApplication(username: str, password: str) -> Application
        CreateApplication() -> Application
        """
        pass

    def Dispose(self):
        # type: (self: Application)
        """ Dispose(self: Application) """
        pass

    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def OpenPatient(self, patientSummary):
        # type: (self: Application, patientSummary: PatientSummary) -> Patient
        """ OpenPatient(self: Application, patientSummary: PatientSummary) -> Patient """
        pass

    def OpenPatientById(self, id):
        # type: (self: Application, id: str) -> Patient
        """ OpenPatientById(self: Application, id: str) -> Patient """
        pass

    def SaveModifications(self):
        # type: (self: Application)
        """ SaveModifications(self: Application) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: Application, writer: XmlWriter)
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
    # type: (self: Application) -> User
    """ Get: CurrentUser(self: Application) -> User """

    PatientSummaries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Application) -> IEnumerable[PatientSummary]
    """ Get: PatientSummaries(self: Application) -> IEnumerable[PatientSummary] """

    ScriptEnvironment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Application) -> ScriptEnvironment
    """ Get: ScriptEnvironment(self: Application) -> ScriptEnvironment """



class ApplicationScript(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: ApplicationScript, writer: XmlWriter)
        """ WriteXml(self: ApplicationScript, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ApprovalStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ApplicationScript) -> ApplicationScriptApprovalStatus
    """ Get: ApprovalStatus(self: ApplicationScript) -> ApplicationScriptApprovalStatus """

    ApprovalStatusDisplayText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ApplicationScript) -> str
    """ Get: ApprovalStatusDisplayText(self: ApplicationScript) -> str """

    AssemblyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ApplicationScript) -> AssemblyName
    """ Get: AssemblyName(self: ApplicationScript) -> AssemblyName """

    ExpirationDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ApplicationScript) -> Nullable[DateTime]
    """ Get: ExpirationDate(self: ApplicationScript) -> Nullable[DateTime] """

    IsReadOnlyScript = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ApplicationScript) -> bool
    """ Get: IsReadOnlyScript(self: ApplicationScript) -> bool """

    IsWriteableScript = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ApplicationScript) -> bool
    """ Get: IsWriteableScript(self: ApplicationScript) -> bool """

    PublisherName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ApplicationScript) -> str
    """ Get: PublisherName(self: ApplicationScript) -> str """

    ScriptType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ApplicationScript) -> ApplicationScriptType
    """ Get: ScriptType(self: ApplicationScript) -> ApplicationScriptType """

    StatusDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ApplicationScript) -> Nullable[DateTime]
    """ Get: StatusDate(self: ApplicationScript) -> Nullable[DateTime] """

    StatusUserIdentity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ApplicationScript) -> UserIdentity
    """ Get: StatusUserIdentity(self: ApplicationScript) -> UserIdentity """



class ApplicationScriptLog(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: ApplicationScriptLog, writer: XmlWriter)
        """ WriteXml(self: ApplicationScriptLog, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CourseId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ApplicationScriptLog) -> str
    """ Get: CourseId(self: ApplicationScriptLog) -> str """

    PatientId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ApplicationScriptLog) -> str
    """ Get: PatientId(self: ApplicationScriptLog) -> str """

    PlanSetupId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ApplicationScriptLog) -> str
    """ Get: PlanSetupId(self: ApplicationScriptLog) -> str """

    PlanUID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ApplicationScriptLog) -> str
    """ Get: PlanUID(self: ApplicationScriptLog) -> str """

    Script = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ApplicationScriptLog) -> ApplicationScript
    """ Get: Script(self: ApplicationScriptLog) -> ApplicationScript """

    ScriptFullName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ApplicationScriptLog) -> str
    """ Get: ScriptFullName(self: ApplicationScriptLog) -> str """

    StructureSetId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ApplicationScriptLog) -> str
    """ Get: StructureSetId(self: ApplicationScriptLog) -> str """

    StructureSetUID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ApplicationScriptLog) -> str
    """ Get: StructureSetUID(self: ApplicationScriptLog) -> str """



class Applicator(AddOn, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: Applicator, writer: XmlWriter)
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
        # type: (self: Beam, beamParams: BeamParameters)
        """ ApplyParameters(self: Beam, beamParams: BeamParameters) """
        pass

    def CanSetOptimalFluence(self, fluence, message):
        # type: (self: Beam, fluence: Fluence) -> (bool, str)
        """ CanSetOptimalFluence(self: Beam, fluence: Fluence) -> (bool, str) """
        pass

    def CollimatorAngleToUser(self, val):
        # type: (self: Beam, val: float) -> float
        """ CollimatorAngleToUser(self: Beam, val: float) -> float """
        pass

    def CreateOrReplaceDRR(self, parameters):
        # type: (self: Beam, parameters: DRRCalculationParameters) -> Image
        """ CreateOrReplaceDRR(self: Beam, parameters: DRRCalculationParameters) -> Image """
        pass

    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def FitCollimatorToStructure(self, margins, structure, useAsymmetricXJaws, useAsymmetricYJaws, optimizeCollimatorRotation):
        # type: (self: Beam, margins: FitToStructureMargins, structure: Structure, useAsymmetricXJaws: bool, useAsymmetricYJaws: bool, optimizeCollimatorRotation: bool)
        """ FitCollimatorToStructure(self: Beam, margins: FitToStructureMargins, structure: Structure, useAsymmetricXJaws: bool, useAsymmetricYJaws: bool, optimizeCollimatorRotation: bool) """
        pass

    def FitMLCToOutline(self, outline, optimizeCollimatorRotation=None, jawFit=None, olmp=None, clmp=None):
        # type: (self: Beam, outline: Array[Array[Point]])FitMLCToOutline(self: Beam, outline: Array[Array[Point]], optimizeCollimatorRotation: bool, jawFit: JawFitting, olmp: OpenLeavesMeetingPoint, clmp: ClosedLeavesMeetingPoint)
        """ FitMLCToOutline(self: Beam, outline: Array[Array[Point]])FitMLCToOutline(self: Beam, outline: Array[Array[Point]], optimizeCollimatorRotation: bool, jawFit: JawFitting, olmp: OpenLeavesMeetingPoint, clmp: ClosedLeavesMeetingPoint) """
        pass

    def FitMLCToStructure(self, *__args):
        # type: (self: Beam, structure: Structure)FitMLCToStructure(self: Beam, margins: FitToStructureMargins, structure: Structure, optimizeCollimatorRotation: bool, jawFit: JawFitting, olmp: OpenLeavesMeetingPoint, clmp: ClosedLeavesMeetingPoint)
        """ FitMLCToStructure(self: Beam, structure: Structure)FitMLCToStructure(self: Beam, margins: FitToStructureMargins, structure: Structure, optimizeCollimatorRotation: bool, jawFit: JawFitting, olmp: OpenLeavesMeetingPoint, clmp: ClosedLeavesMeetingPoint) """
        pass

    def GantryAngleToUser(self, val):
        # type: (self: Beam, val: float) -> float
        """ GantryAngleToUser(self: Beam, val: float) -> float """
        pass

    def GetEditableParameters(self):
        # type: (self: Beam) -> BeamParameters
        """ GetEditableParameters(self: Beam) -> BeamParameters """
        pass

    def GetOptimalFluence(self):
        # type: (self: Beam) -> Fluence
        """ GetOptimalFluence(self: Beam) -> Fluence """
        pass

    def GetSourceLocation(self, gantryAngle):
        # type: (self: Beam, gantryAngle: float) -> VVector
        """ GetSourceLocation(self: Beam, gantryAngle: float) -> VVector """
        pass

    def GetStructureOutlines(self, structure, inBEV):
        # type: (self: Beam, structure: Structure, inBEV: bool) -> Array[Array[Point]]
        """ GetStructureOutlines(self: Beam, structure: Structure, inBEV: bool) -> Array[Array[Point]] """
        pass

    def JawPositionsToUserString(self, val):
        # type: (self: Beam, val: VRect[float]) -> str
        """ JawPositionsToUserString(self: Beam, val: VRect[float]) -> str """
        pass

    def PatientSupportAngleToUser(self, val):
        # type: (self: Beam, val: float) -> float
        """ PatientSupportAngleToUser(self: Beam, val: float) -> float """
        pass

    def SetOptimalFluence(self, fluence):
        # type: (self: Beam, fluence: Fluence)
        """ SetOptimalFluence(self: Beam, fluence: Fluence) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: Beam, writer: XmlWriter)
        """ WriteXml(self: Beam, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Applicator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> Applicator
    """ Get: Applicator(self: Beam) -> Applicator """

    ArcLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> float
    """ Get: ArcLength(self: Beam) -> float """

    AverageSSD = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> float
    """ Get: AverageSSD(self: Beam) -> float """

    BeamNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> int
    """ Get: BeamNumber(self: Beam) -> int """

    Blocks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> IEnumerable[Block]
    """ Get: Blocks(self: Beam) -> IEnumerable[Block] """

    Boluses = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> IEnumerable[Bolus]
    """ Get: Boluses(self: Beam) -> IEnumerable[Bolus] """

    CalculationLogs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> IEnumerable[BeamCalculationLog]
    """ Get: CalculationLogs(self: Beam) -> IEnumerable[BeamCalculationLog] """

    Compensator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> Compensator
    """ Get: Compensator(self: Beam) -> Compensator """

    ControlPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> ControlPointCollection
    """ Get: ControlPoints(self: Beam) -> ControlPointCollection """

    CreationDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> Nullable[DateTime]
    """ Get: CreationDateTime(self: Beam) -> Nullable[DateTime] """

    Dose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> BeamDose
    """ Get: Dose(self: Beam) -> BeamDose """

    DoseRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> int
    """ Get: DoseRate(self: Beam) -> int """

    DosimetricLeafGap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> float
    """ Get: DosimetricLeafGap(self: Beam) -> float """

    EnergyModeDisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> str
    """ Get: EnergyModeDisplayName(self: Beam) -> str """

    FieldReferencePoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> IEnumerable[FieldReferencePoint]
    """ Get: FieldReferencePoints(self: Beam) -> IEnumerable[FieldReferencePoint] """

    GantryDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> GantryDirection
    """ Get: GantryDirection(self: Beam) -> GantryDirection """

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> str
    """
    Get: Id(self: Beam) -> str
    
    Set: Id(self: Beam) = value
    """

    IsocenterPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> VVector
    """ Get: IsocenterPosition(self: Beam) -> VVector """

    IsSetupField = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> bool
    """ Get: IsSetupField(self: Beam) -> bool """

    Meterset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> MetersetValue
    """ Get: Meterset(self: Beam) -> MetersetValue """

    MetersetPerGy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> float
    """ Get: MetersetPerGy(self: Beam) -> float """

    MLC = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> MLC
    """ Get: MLC(self: Beam) -> MLC """

    MLCPlanType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> MLCPlanType
    """ Get: MLCPlanType(self: Beam) -> MLCPlanType """

    MLCTransmissionFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> float
    """ Get: MLCTransmissionFactor(self: Beam) -> float """

    MotionCompensationTechnique = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> str
    """ Get: MotionCompensationTechnique(self: Beam) -> str """

    MotionSignalSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> str
    """ Get: MotionSignalSource(self: Beam) -> str """

    NormalizationFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> float
    """ Get: NormalizationFactor(self: Beam) -> float """

    NormalizationMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> str
    """ Get: NormalizationMethod(self: Beam) -> str """

    Plan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> PlanSetup
    """ Get: Plan(self: Beam) -> PlanSetup """

    PlannedSSD = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> float
    """ Get: PlannedSSD(self: Beam) -> float """

    ReferenceImage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> Image
    """ Get: ReferenceImage(self: Beam) -> Image """

    SetupTechnique = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> SetupTechnique
    """ Get: SetupTechnique(self: Beam) -> SetupTechnique """

    SSD = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> float
    """ Get: SSD(self: Beam) -> float """

    SSDAtStopAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> float
    """ Get: SSDAtStopAngle(self: Beam) -> float """

    Technique = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> Technique
    """ Get: Technique(self: Beam) -> Technique """

    ToleranceTableLabel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> str
    """ Get: ToleranceTableLabel(self: Beam) -> str """

    Trays = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> IEnumerable[Tray]
    """ Get: Trays(self: Beam) -> IEnumerable[Tray] """

    TreatmentTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> float
    """ Get: TreatmentTime(self: Beam) -> float """

    TreatmentUnit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> ExternalBeamTreatmentUnit
    """ Get: TreatmentUnit(self: Beam) -> ExternalBeamTreatmentUnit """

    Wedges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> IEnumerable[Wedge]
    """ Get: Wedges(self: Beam) -> IEnumerable[Wedge] """

    WeightFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Beam) -> float
    """ Get: WeightFactor(self: Beam) -> float """



class BeamCalculationLog(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: BeamCalculationLog, writer: XmlWriter)
        """ WriteXml(self: BeamCalculationLog, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Beam = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BeamCalculationLog) -> Beam
    """ Get: Beam(self: BeamCalculationLog) -> Beam """

    Category = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BeamCalculationLog) -> str
    """ Get: Category(self: BeamCalculationLog) -> str """

    MessageLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BeamCalculationLog) -> IEnumerable[str]
    """ Get: MessageLines(self: BeamCalculationLog) -> IEnumerable[str] """



class Dose(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetDoseProfile(self, start, stop, preallocatedBuffer):
        # type: (self: Dose, start: VVector, stop: VVector, preallocatedBuffer: Array[float]) -> DoseProfile
        """ GetDoseProfile(self: Dose, start: VVector, stop: VVector, preallocatedBuffer: Array[float]) -> DoseProfile """
        pass

    def GetDoseToPoint(self, at):
        # type: (self: Dose, at: VVector) -> DoseValue
        """ GetDoseToPoint(self: Dose, at: VVector) -> DoseValue """
        pass

    def GetVoxels(self, planeIndex, preallocatedBuffer):
        # type: (self: Dose, planeIndex: int, preallocatedBuffer: Array[int])
        """ GetVoxels(self: Dose, planeIndex: int, preallocatedBuffer: Array[int]) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def VoxelToDoseValue(self, voxelValue):
        # type: (self: Dose, voxelValue: int) -> DoseValue
        """ VoxelToDoseValue(self: Dose, voxelValue: int) -> DoseValue """
        pass

    def WriteXml(self, writer):
        # type: (self: Dose, writer: XmlWriter)
        """ WriteXml(self: Dose, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DoseMax3D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Dose) -> DoseValue
    """ Get: DoseMax3D(self: Dose) -> DoseValue """

    DoseMax3DLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Dose) -> VVector
    """ Get: DoseMax3DLocation(self: Dose) -> VVector """

    Isodoses = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Dose) -> IEnumerable[Isodose]
    """ Get: Isodoses(self: Dose) -> IEnumerable[Isodose] """

    Origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Dose) -> VVector
    """ Get: Origin(self: Dose) -> VVector """

    Series = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Dose) -> Series
    """ Get: Series(self: Dose) -> Series """

    SeriesUID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Dose) -> str
    """ Get: SeriesUID(self: Dose) -> str """

    UID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Dose) -> str
    """ Get: UID(self: Dose) -> str """

    XDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Dose) -> VVector
    """ Get: XDirection(self: Dose) -> VVector """

    XRes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Dose) -> float
    """ Get: XRes(self: Dose) -> float """

    XSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Dose) -> int
    """ Get: XSize(self: Dose) -> int """

    YDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Dose) -> VVector
    """ Get: YDirection(self: Dose) -> VVector """

    YRes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Dose) -> float
    """ Get: YRes(self: Dose) -> float """

    YSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Dose) -> int
    """ Get: YSize(self: Dose) -> int """

    ZDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Dose) -> VVector
    """ Get: ZDirection(self: Dose) -> VVector """

    ZRes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Dose) -> float
    """ Get: ZRes(self: Dose) -> float """

    ZSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Dose) -> int
    """ Get: ZSize(self: Dose) -> int """



class BeamDose(Dose, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetAbsoluteBeamDoseValue(self, relative):
        # type: (self: BeamDose, relative: DoseValue) -> DoseValue
        """ GetAbsoluteBeamDoseValue(self: BeamDose, relative: DoseValue) -> DoseValue """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: BeamDose, writer: XmlWriter)
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
        # type: (self: BeamParameters, leafPositions: Array[Single])
        """ SetAllLeafPositions(self: BeamParameters, leafPositions: Array[Single]) """
        pass

    def SetJawPositions(self, positions):
        # type: (self: BeamParameters, positions: VRect[float])
        """ SetJawPositions(self: BeamParameters, positions: VRect[float]) """
        pass

    ControlPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BeamParameters) -> IEnumerable[ControlPointParameters]
    """ Get: ControlPoints(self: BeamParameters) -> IEnumerable[ControlPointParameters] """

    GantryDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BeamParameters) -> GantryDirection
    """ Get: GantryDirection(self: BeamParameters) -> GantryDirection """

    Isocenter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BeamParameters) -> VVector
    """
    Get: Isocenter(self: BeamParameters) -> VVector
    
    Set: Isocenter(self: BeamParameters) = value
    """

    WeightFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BeamParameters) -> float
    """
    Get: WeightFactor(self: BeamParameters) -> float
    
    Set: WeightFactor(self: BeamParameters) = value
    """



class BeamUncertainty(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: BeamUncertainty, writer: XmlWriter)
        """ WriteXml(self: BeamUncertainty, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Beam = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BeamUncertainty) -> Beam
    """ Get: Beam(self: BeamUncertainty) -> Beam """

    BeamNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BeamUncertainty) -> BeamNumber
    """ Get: BeamNumber(self: BeamUncertainty) -> BeamNumber """

    Dose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BeamUncertainty) -> Dose
    """ Get: Dose(self: BeamUncertainty) -> Dose """



class Block(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: Block, writer: XmlWriter)
        """ WriteXml(self: Block, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AddOnMaterial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Block) -> AddOnMaterial
    """ Get: AddOnMaterial(self: Block) -> AddOnMaterial """

    IsDiverging = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Block) -> bool
    """ Get: IsDiverging(self: Block) -> bool """

    Outline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Block) -> Array[Array[Point]]
    """ Get: Outline(self: Block) -> Array[Array[Point]] """

    TransmissionFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Block) -> float
    """ Get: TransmissionFactor(self: Block) -> float """

    Tray = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Block) -> Tray
    """ Get: Tray(self: Block) -> Tray """

    TrayTransmissionFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Block) -> float
    """ Get: TrayTransmissionFactor(self: Block) -> float """

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Block) -> BlockType
    """ Get: Type(self: Block) -> BlockType """



class Bolus(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: Bolus, writer: XmlWriter)
        """ WriteXml(self: Bolus, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Bolus) -> str
    """ Get: Id(self: Bolus) -> str """

    MaterialCTValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Bolus) -> float
    """ Get: MaterialCTValue(self: Bolus) -> float """

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Bolus) -> str
    """ Get: Name(self: Bolus) -> str """



class BrachyFieldReferencePoint(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: BrachyFieldReferencePoint, writer: XmlWriter)
        """ WriteXml(self: BrachyFieldReferencePoint, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    FieldDose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachyFieldReferencePoint) -> DoseValue
    """ Get: FieldDose(self: BrachyFieldReferencePoint) -> DoseValue """

    IsFieldDoseNominal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachyFieldReferencePoint) -> bool
    """ Get: IsFieldDoseNominal(self: BrachyFieldReferencePoint) -> bool """

    IsPrimaryReferencePoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachyFieldReferencePoint) -> bool
    """ Get: IsPrimaryReferencePoint(self: BrachyFieldReferencePoint) -> bool """

    ReferencePoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachyFieldReferencePoint) -> ReferencePoint
    """ Get: ReferencePoint(self: BrachyFieldReferencePoint) -> ReferencePoint """

    RefPointLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachyFieldReferencePoint) -> VVector
    """ Get: RefPointLocation(self: BrachyFieldReferencePoint) -> VVector """



class PlanningItem(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetDoseAtVolume(self, structure, volume, volumePresentation, requestedDosePresentation):
        # type: (self: PlanningItem, structure: Structure, volume: float, volumePresentation: VolumePresentation, requestedDosePresentation: DoseValuePresentation) -> DoseValue
        """ GetDoseAtVolume(self: PlanningItem, structure: Structure, volume: float, volumePresentation: VolumePresentation, requestedDosePresentation: DoseValuePresentation) -> DoseValue """
        pass

    def GetDVHCumulativeData(self, structure, dosePresentation, volumePresentation, binWidth):
        # type: (self: PlanningItem, structure: Structure, dosePresentation: DoseValuePresentation, volumePresentation: VolumePresentation, binWidth: float) -> DVHData
        """ GetDVHCumulativeData(self: PlanningItem, structure: Structure, dosePresentation: DoseValuePresentation, volumePresentation: VolumePresentation, binWidth: float) -> DVHData """
        pass

    def GetVolumeAtDose(self, structure, dose, requestedVolumePresentation):
        # type: (self: PlanningItem, structure: Structure, dose: DoseValue, requestedVolumePresentation: VolumePresentation) -> float
        """ GetVolumeAtDose(self: PlanningItem, structure: Structure, dose: DoseValue, requestedVolumePresentation: VolumePresentation) -> float """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: PlanningItem, writer: XmlWriter)
        """ WriteXml(self: PlanningItem, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CreationDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanningItem) -> Nullable[DateTime]
    """ Get: CreationDateTime(self: PlanningItem) -> Nullable[DateTime] """

    Dose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanningItem) -> PlanningItemDose
    """ Get: Dose(self: PlanningItem) -> PlanningItemDose """

    DoseValuePresentation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanningItem) -> DoseValuePresentation
    """
    Get: DoseValuePresentation(self: PlanningItem) -> DoseValuePresentation
    
    Set: DoseValuePresentation(self: PlanningItem) = value
    """

    StructureSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanningItem) -> StructureSet
    """ Get: StructureSet(self: PlanningItem) -> StructureSet """

    StructuresSelectedForDvh = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanningItem) -> IEnumerable[Structure]
    """ Get: StructuresSelectedForDvh(self: PlanningItem) -> IEnumerable[Structure] """



class PlanSetup(PlanningItem, IXmlSerializable):
    # no doc
    def AddReferencePoint(self, structure, location, id, name):
        # type: (self: PlanSetup, structure: Structure, location: Nullable[VVector], id: str, name: str) -> ReferencePoint
        """ AddReferencePoint(self: PlanSetup, structure: Structure, location: Nullable[VVector], id: str, name: str) -> ReferencePoint """
        pass

    def AttachToCalcClient(self, *args): #cannot find CLR method
        # type: (self: PlanSetup, doseCalcClient: ICalculationClient)
        """ AttachToCalcClient(self: PlanSetup, doseCalcClient: ICalculationClient) """
        pass

    def ClearCalculationModel(self, calculationType):
        # type: (self: PlanSetup, calculationType: CalculationType)
        """ ClearCalculationModel(self: PlanSetup, calculationType: CalculationType) """
        pass

    def DetachFromCalcClient(self, *args): #cannot find CLR method
        # type: (self: PlanSetup, doseCalcClient: ICalculationClient)
        """ DetachFromCalcClient(self: PlanSetup, doseCalcClient: ICalculationClient) """
        pass

    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetCalculationModel(self, calculationType):
        # type: (self: PlanSetup, calculationType: CalculationType) -> str
        """ GetCalculationModel(self: PlanSetup, calculationType: CalculationType) -> str """
        pass

    def GetCalculationOption(self, calculationModel, optionName, optionValue):
        # type: (self: PlanSetup, calculationModel: str, optionName: str) -> (bool, str)
        """ GetCalculationOption(self: PlanSetup, calculationModel: str, optionName: str) -> (bool, str) """
        pass

    def GetCalculationOptions(self, calculationModel):
        # type: (self: PlanSetup, calculationModel: str) -> Dictionary[str, str]
        """ GetCalculationOptions(self: PlanSetup, calculationModel: str) -> Dictionary[str, str] """
        pass

    def GetProtocolPrescriptionsAndMeasures(self, prescriptions, measures):
        # type: (self: PlanSetup, prescriptions: List[ProtocolPhasePrescription], measures: List[ProtocolPhaseMeasure]) -> (List[ProtocolPhasePrescription], List[ProtocolPhaseMeasure])
        """ GetProtocolPrescriptionsAndMeasures(self: PlanSetup, prescriptions: List[ProtocolPhasePrescription], measures: List[ProtocolPhaseMeasure]) -> (List[ProtocolPhasePrescription], List[ProtocolPhaseMeasure]) """
        pass

    def Report(self, *args): #cannot find CLR method
        # type: (self: PlanSetup, str: str)
        """ Report(self: PlanSetup, str: str) """
        pass

    def SetCalculationModel(self, calculationType, model):
        # type: (self: PlanSetup, calculationType: CalculationType, model: str)
        """ SetCalculationModel(self: PlanSetup, calculationType: CalculationType, model: str) """
        pass

    def SetCalculationOption(self, calculationModel, optionName, optionValue):
        # type: (self: PlanSetup, calculationModel: str, optionName: str, optionValue: str) -> bool
        """ SetCalculationOption(self: PlanSetup, calculationModel: str, optionName: str, optionValue: str) -> bool """
        pass

    def SetPrescription(self, numberOfFractions, dosePerFraction, treatmentPercentage):
        # type: (self: PlanSetup, numberOfFractions: int, dosePerFraction: DoseValue, treatmentPercentage: float)
        """ SetPrescription(self: PlanSetup, numberOfFractions: int, dosePerFraction: DoseValue, treatmentPercentage: float) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: PlanSetup, writer: XmlWriter)
        """ WriteXml(self: PlanSetup, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ApplicationScriptLogs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> IEnumerable[ApplicationScriptLog]
    """ Get: ApplicationScriptLogs(self: PlanSetup) -> IEnumerable[ApplicationScriptLog] """

    ApprovalHistory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> IEnumerable[ApprovalHistoryEntry]
    """ Get: ApprovalHistory(self: PlanSetup) -> IEnumerable[ApprovalHistoryEntry] """

    ApprovalStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> PlanSetupApprovalStatus
    """ Get: ApprovalStatus(self: PlanSetup) -> PlanSetupApprovalStatus """

    Beams = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> IEnumerable[Beam]
    """ Get: Beams(self: PlanSetup) -> IEnumerable[Beam] """

    Course = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> Course
    """ Get: Course(self: PlanSetup) -> Course """

    CreationUserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> str
    """ Get: CreationUserName(self: PlanSetup) -> str """

    DosePerFraction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> DoseValue
    """ Get: DosePerFraction(self: PlanSetup) -> DoseValue """

    DosePerFractionInPrimaryRefPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> DoseValue
    """ Get: DosePerFractionInPrimaryRefPoint(self: PlanSetup) -> DoseValue """

    DVHEstimates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> IEnumerable[EstimatedDVH]
    """ Get: DVHEstimates(self: PlanSetup) -> IEnumerable[EstimatedDVH] """

    ElectronCalculationModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> str
    """ Get: ElectronCalculationModel(self: PlanSetup) -> str """

    ElectronCalculationOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> Dictionary[str, str]
    """ Get: ElectronCalculationOptions(self: PlanSetup) -> Dictionary[str, str] """

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> str
    """
    Get: Id(self: PlanSetup) -> str
    
    Set: Id(self: PlanSetup) = value
    """

    IsDoseValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> bool
    """ Get: IsDoseValid(self: PlanSetup) -> bool """

    IsTreated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> bool
    """ Get: IsTreated(self: PlanSetup) -> bool """

    NumberOfFractions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> Nullable[int]
    """ Get: NumberOfFractions(self: PlanSetup) -> Nullable[int] """

    OptimizationSetup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> OptimizationSetup
    """ Get: OptimizationSetup(self: PlanSetup) -> OptimizationSetup """

    PhotonCalculationModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> str
    """ Get: PhotonCalculationModel(self: PlanSetup) -> str """

    PhotonCalculationOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> Dictionary[str, str]
    """ Get: PhotonCalculationOptions(self: PlanSetup) -> Dictionary[str, str] """

    PlanIntent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> str
    """ Get: PlanIntent(self: PlanSetup) -> str """

    PlannedDosePerFraction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> DoseValue
    """ Get: PlannedDosePerFraction(self: PlanSetup) -> DoseValue """

    PlanningApprovalDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> str
    """ Get: PlanningApprovalDate(self: PlanSetup) -> str """

    PlanningApprover = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> str
    """ Get: PlanningApprover(self: PlanSetup) -> str """

    PlanningApproverDisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> str
    """ Get: PlanningApproverDisplayName(self: PlanSetup) -> str """

    PlanNormalizationMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> str
    """ Get: PlanNormalizationMethod(self: PlanSetup) -> str """

    PlanNormalizationPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> VVector
    """ Get: PlanNormalizationPoint(self: PlanSetup) -> VVector """

    PlanNormalizationValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> float
    """
    Get: PlanNormalizationValue(self: PlanSetup) -> float
    
    Set: PlanNormalizationValue(self: PlanSetup) = value
    """

    PlanObjectiveStructures = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> IEnumerable[str]
    """ Get: PlanObjectiveStructures(self: PlanSetup) -> IEnumerable[str] """

    PlanType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> PlanType
    """ Get: PlanType(self: PlanSetup) -> PlanType """

    PlanUncertainties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> IEnumerable[PlanUncertainty]
    """ Get: PlanUncertainties(self: PlanSetup) -> IEnumerable[PlanUncertainty] """

    PredecessorPlan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> PlanSetup
    """ Get: PredecessorPlan(self: PlanSetup) -> PlanSetup """

    PrescribedDosePerFraction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> DoseValue
    """ Get: PrescribedDosePerFraction(self: PlanSetup) -> DoseValue """

    PrescribedPercentage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> float
    """ Get: PrescribedPercentage(self: PlanSetup) -> float """

    PrimaryReferencePoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> ReferencePoint
    """ Get: PrimaryReferencePoint(self: PlanSetup) -> ReferencePoint """

    ProtocolID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> str
    """ Get: ProtocolID(self: PlanSetup) -> str """

    ProtocolPhaseID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> str
    """ Get: ProtocolPhaseID(self: PlanSetup) -> str """

    ProtonCalculationModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> str
    """ Get: ProtonCalculationModel(self: PlanSetup) -> str """

    ProtonCalculationOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> Dictionary[str, str]
    """ Get: ProtonCalculationOptions(self: PlanSetup) -> Dictionary[str, str] """

    ReferencePoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> IEnumerable[ReferencePoint]
    """ Get: ReferencePoints(self: PlanSetup) -> IEnumerable[ReferencePoint] """

    RTPrescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> RTPrescription
    """ Get: RTPrescription(self: PlanSetup) -> RTPrescription """

    Series = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> Series
    """ Get: Series(self: PlanSetup) -> Series """

    SeriesUID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> str
    """ Get: SeriesUID(self: PlanSetup) -> str """

    TargetVolumeID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> str
    """ Get: TargetVolumeID(self: PlanSetup) -> str """

    TotalDose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> DoseValue
    """ Get: TotalDose(self: PlanSetup) -> DoseValue """

    TotalPrescribedDose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> DoseValue
    """ Get: TotalPrescribedDose(self: PlanSetup) -> DoseValue """

    TreatmentApprovalDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> str
    """ Get: TreatmentApprovalDate(self: PlanSetup) -> str """

    TreatmentApprover = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> str
    """ Get: TreatmentApprover(self: PlanSetup) -> str """

    TreatmentApproverDisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> str
    """ Get: TreatmentApproverDisplayName(self: PlanSetup) -> str """

    TreatmentOrientation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> PatientOrientation
    """ Get: TreatmentOrientation(self: PlanSetup) -> PatientOrientation """

    TreatmentPercentage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> float
    """ Get: TreatmentPercentage(self: PlanSetup) -> float """

    TreatmentSessions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> IEnumerable[PlanTreatmentSession]
    """ Get: TreatmentSessions(self: PlanSetup) -> IEnumerable[PlanTreatmentSession] """

    UID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> str
    """ Get: UID(self: PlanSetup) -> str """

    UseGating = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> bool
    """
    Get: UseGating(self: PlanSetup) -> bool
    
    Set: UseGating(self: PlanSetup) = value
    """

    VerifiedPlan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSetup) -> PlanSetup
    """ Get: VerifiedPlan(self: PlanSetup) -> PlanSetup """


    m_errorsOnCalculationCompleted = None


class BrachyPlanSetup(PlanSetup, IXmlSerializable):
    # no doc
    def AttachToCalcClient(self, *args): #cannot find CLR method
        # type: (self: PlanSetup, doseCalcClient: ICalculationClient)
        """ AttachToCalcClient(self: PlanSetup, doseCalcClient: ICalculationClient) """
        pass

    def CalculateAccurateTG43DoseProfile(self, start, stop, preallocatedBuffer):
        # type: (self: BrachyPlanSetup, start: VVector, stop: VVector, preallocatedBuffer: Array[float]) -> DoseProfile
        """ CalculateAccurateTG43DoseProfile(self: BrachyPlanSetup, start: VVector, stop: VVector, preallocatedBuffer: Array[float]) -> DoseProfile """
        pass

    def DetachFromCalcClient(self, *args): #cannot find CLR method
        # type: (self: PlanSetup, doseCalcClient: ICalculationClient)
        """ DetachFromCalcClient(self: PlanSetup, doseCalcClient: ICalculationClient) """
        pass

    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def Report(self, *args): #cannot find CLR method
        # type: (self: PlanSetup, str: str)
        """ Report(self: PlanSetup, str: str) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: BrachyPlanSetup, writer: XmlWriter)
        """ WriteXml(self: BrachyPlanSetup, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ApplicationSetupType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachyPlanSetup) -> str
    """ Get: ApplicationSetupType(self: BrachyPlanSetup) -> str """

    Catheters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachyPlanSetup) -> IEnumerable[Catheter]
    """ Get: Catheters(self: BrachyPlanSetup) -> IEnumerable[Catheter] """

    NumberOfPdrPulses = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachyPlanSetup) -> Nullable[int]
    """ Get: NumberOfPdrPulses(self: BrachyPlanSetup) -> Nullable[int] """

    PdrPulseInterval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachyPlanSetup) -> Nullable[float]
    """ Get: PdrPulseInterval(self: BrachyPlanSetup) -> Nullable[float] """

    SeedCollections = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachyPlanSetup) -> IEnumerable[SeedCollection]
    """ Get: SeedCollections(self: BrachyPlanSetup) -> IEnumerable[SeedCollection] """

    SolidApplicators = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachyPlanSetup) -> IEnumerable[BrachySolidApplicator]
    """ Get: SolidApplicators(self: BrachyPlanSetup) -> IEnumerable[BrachySolidApplicator] """

    TreatmentDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachyPlanSetup) -> Nullable[DateTime]
    """ Get: TreatmentDateTime(self: BrachyPlanSetup) -> Nullable[DateTime] """

    TreatmentTechnique = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachyPlanSetup) -> str
    """ Get: TreatmentTechnique(self: BrachyPlanSetup) -> str """


    m_errorsOnCalculationCompleted = None


class BrachySolidApplicator(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: BrachySolidApplicator, writer: XmlWriter)
        """ WriteXml(self: BrachySolidApplicator, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ApplicatorSetName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachySolidApplicator) -> str
    """ Get: ApplicatorSetName(self: BrachySolidApplicator) -> str """

    ApplicatorSetType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachySolidApplicator) -> str
    """ Get: ApplicatorSetType(self: BrachySolidApplicator) -> str """

    Category = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachySolidApplicator) -> str
    """ Get: Category(self: BrachySolidApplicator) -> str """

    Catheters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachySolidApplicator) -> IEnumerable[Catheter]
    """ Get: Catheters(self: BrachySolidApplicator) -> IEnumerable[Catheter] """

    Note = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachySolidApplicator) -> str
    """ Get: Note(self: BrachySolidApplicator) -> str """

    PartName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachySolidApplicator) -> str
    """ Get: PartName(self: BrachySolidApplicator) -> str """

    PartNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachySolidApplicator) -> str
    """ Get: PartNumber(self: BrachySolidApplicator) -> str """

    Summary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachySolidApplicator) -> str
    """ Get: Summary(self: BrachySolidApplicator) -> str """

    UID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachySolidApplicator) -> str
    """ Get: UID(self: BrachySolidApplicator) -> str """

    Vendor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachySolidApplicator) -> str
    """ Get: Vendor(self: BrachySolidApplicator) -> str """

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachySolidApplicator) -> str
    """ Get: Version(self: BrachySolidApplicator) -> str """



class BrachyTreatmentUnit(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetActiveRadioactiveSource(self):
        # type: (self: BrachyTreatmentUnit) -> RadioactiveSource
        """ GetActiveRadioactiveSource(self: BrachyTreatmentUnit) -> RadioactiveSource """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: BrachyTreatmentUnit, writer: XmlWriter)
        """ WriteXml(self: BrachyTreatmentUnit, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DoseRateMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachyTreatmentUnit) -> str
    """ Get: DoseRateMode(self: BrachyTreatmentUnit) -> str """

    DwellTimeResolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachyTreatmentUnit) -> float
    """ Get: DwellTimeResolution(self: BrachyTreatmentUnit) -> float """

    MachineInterface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachyTreatmentUnit) -> str
    """ Get: MachineInterface(self: BrachyTreatmentUnit) -> str """

    MachineModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachyTreatmentUnit) -> str
    """ Get: MachineModel(self: BrachyTreatmentUnit) -> str """

    MaxDwellTimePerChannel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachyTreatmentUnit) -> float
    """ Get: MaxDwellTimePerChannel(self: BrachyTreatmentUnit) -> float """

    MaxDwellTimePerPos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachyTreatmentUnit) -> float
    """ Get: MaxDwellTimePerPos(self: BrachyTreatmentUnit) -> float """

    MaxDwellTimePerTreatment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachyTreatmentUnit) -> float
    """ Get: MaxDwellTimePerTreatment(self: BrachyTreatmentUnit) -> float """

    MaximumChannelLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachyTreatmentUnit) -> float
    """ Get: MaximumChannelLength(self: BrachyTreatmentUnit) -> float """

    MaximumDwellPositionsPerChannel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachyTreatmentUnit) -> int
    """ Get: MaximumDwellPositionsPerChannel(self: BrachyTreatmentUnit) -> int """

    MaximumStepSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachyTreatmentUnit) -> float
    """ Get: MaximumStepSize(self: BrachyTreatmentUnit) -> float """

    MinimumChannelLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachyTreatmentUnit) -> float
    """ Get: MinimumChannelLength(self: BrachyTreatmentUnit) -> float """

    MinimumStepSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachyTreatmentUnit) -> float
    """ Get: MinimumStepSize(self: BrachyTreatmentUnit) -> float """

    NumberOfChannels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachyTreatmentUnit) -> int
    """ Get: NumberOfChannels(self: BrachyTreatmentUnit) -> int """

    SourceCenterOffsetFromTip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachyTreatmentUnit) -> float
    """ Get: SourceCenterOffsetFromTip(self: BrachyTreatmentUnit) -> float """

    SourceMovementType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachyTreatmentUnit) -> str
    """ Get: SourceMovementType(self: BrachyTreatmentUnit) -> str """

    StepSizeResolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: BrachyTreatmentUnit) -> float
    """ Get: StepSizeResolution(self: BrachyTreatmentUnit) -> float """



class CalculationResult(object):
    # no doc
    Success = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: CalculationResult) -> bool
    """ Get: Success(self: CalculationResult) -> bool """



class Catheter(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetSourcePosCenterDistanceFromTip(self, sourcePosition):
        # type: (self: Catheter, sourcePosition: SourcePosition) -> float
        """ GetSourcePosCenterDistanceFromTip(self: Catheter, sourcePosition: SourcePosition) -> float """
        pass

    def GetTotalDwellTime(self):
        # type: (self: Catheter) -> float
        """ GetTotalDwellTime(self: Catheter) -> float """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: Catheter, writer: XmlWriter)
        """ WriteXml(self: Catheter, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ApplicatorLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Catheter) -> float
    """ Get: ApplicatorLength(self: Catheter) -> float """

    BrachyFieldReferencePoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Catheter) -> IEnumerable[BrachyFieldReferencePoint]
    """ Get: BrachyFieldReferencePoints(self: Catheter) -> IEnumerable[BrachyFieldReferencePoint] """

    BrachySolidApplicatorPartID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Catheter) -> int
    """ Get: BrachySolidApplicatorPartID(self: Catheter) -> int """

    ChannelNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Catheter) -> int
    """ Get: ChannelNumber(self: Catheter) -> int """

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Catheter) -> Color
    """ Get: Color(self: Catheter) -> Color """

    DeadSpaceLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Catheter) -> float
    """ Get: DeadSpaceLength(self: Catheter) -> float """

    Shape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Catheter) -> Array[VVector]
    """ Get: Shape(self: Catheter) -> Array[VVector] """

    SourcePositions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Catheter) -> IEnumerable[SourcePosition]
    """ Get: SourcePositions(self: Catheter) -> IEnumerable[SourcePosition] """

    StepSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Catheter) -> float
    """ Get: StepSize(self: Catheter) -> float """

    TreatmentUnit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Catheter) -> BrachyTreatmentUnit
    """ Get: TreatmentUnit(self: Catheter) -> BrachyTreatmentUnit """



class Compensator(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: Compensator, writer: XmlWriter)
        """ WriteXml(self: Compensator, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Material = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Compensator) -> AddOnMaterial
    """ Get: Material(self: Compensator) -> AddOnMaterial """

    Slot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Compensator) -> Slot
    """ Get: Slot(self: Compensator) -> Slot """

    Tray = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Compensator) -> Tray
    """ Get: Tray(self: Compensator) -> Tray """



class ControlPoint(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: ControlPoint, writer: XmlWriter)
        """ WriteXml(self: ControlPoint, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Beam = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ControlPoint) -> Beam
    """ Get: Beam(self: ControlPoint) -> Beam """

    CollimatorAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ControlPoint) -> float
    """ Get: CollimatorAngle(self: ControlPoint) -> float """

    GantryAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ControlPoint) -> float
    """ Get: GantryAngle(self: ControlPoint) -> float """

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ControlPoint) -> int
    """ Get: Index(self: ControlPoint) -> int """

    JawPositions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ControlPoint) -> VRect[float]
    """ Get: JawPositions(self: ControlPoint) -> VRect[float] """

    LeafPositions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ControlPoint) -> Array[Single]
    """ Get: LeafPositions(self: ControlPoint) -> Array[Single] """

    MetersetWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ControlPoint) -> float
    """ Get: MetersetWeight(self: ControlPoint) -> float """

    PatientSupportAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ControlPoint) -> float
    """ Get: PatientSupportAngle(self: ControlPoint) -> float """

    TableTopLateralPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ControlPoint) -> float
    """ Get: TableTopLateralPosition(self: ControlPoint) -> float """

    TableTopLongitudinalPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ControlPoint) -> float
    """ Get: TableTopLongitudinalPosition(self: ControlPoint) -> float """

    TableTopVerticalPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ControlPoint) -> float
    """ Get: TableTopVerticalPosition(self: ControlPoint) -> float """



class ControlPointCollection(SerializableObject, IXmlSerializable, IEnumerable[ControlPoint], IEnumerable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetEnumerator(self):
        # type: (self: ControlPointCollection) -> IEnumerator[ControlPoint]
        """ GetEnumerator(self: ControlPointCollection) -> IEnumerator[ControlPoint] """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: ControlPointCollection, writer: XmlWriter)
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
    # type: (self: ControlPointCollection) -> int
    """ Get: Count(self: ControlPointCollection) -> int """



class ControlPointParameters(object):
    # no doc
    CollimatorAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ControlPointParameters) -> float
    """ Get: CollimatorAngle(self: ControlPointParameters) -> float """

    GantryAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ControlPointParameters) -> float
    """ Get: GantryAngle(self: ControlPointParameters) -> float """

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ControlPointParameters) -> int
    """ Get: Index(self: ControlPointParameters) -> int """

    JawPositions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ControlPointParameters) -> VRect[float]
    """
    Get: JawPositions(self: ControlPointParameters) -> VRect[float]
    
    Set: JawPositions(self: ControlPointParameters) = value
    """

    LeafPositions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ControlPointParameters) -> Array[Single]
    """
    Get: LeafPositions(self: ControlPointParameters) -> Array[Single]
    
    Set: LeafPositions(self: ControlPointParameters) = value
    """

    MetersetWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ControlPointParameters) -> float
    """ Get: MetersetWeight(self: ControlPointParameters) -> float """

    PatientSupportAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ControlPointParameters) -> float
    """ Get: PatientSupportAngle(self: ControlPointParameters) -> float """

    TableTopLateralPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ControlPointParameters) -> float
    """ Get: TableTopLateralPosition(self: ControlPointParameters) -> float """

    TableTopLongitudinalPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ControlPointParameters) -> float
    """ Get: TableTopLongitudinalPosition(self: ControlPointParameters) -> float """

    TableTopVerticalPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ControlPointParameters) -> float
    """ Get: TableTopVerticalPosition(self: ControlPointParameters) -> float """



class Course(ApiDataObject, IXmlSerializable):
    # no doc
    def AddExternalPlanSetup(self, structureSet):
        # type: (self: Course, structureSet: StructureSet) -> ExternalPlanSetup
        """ AddExternalPlanSetup(self: Course, structureSet: StructureSet) -> ExternalPlanSetup """
        pass

    def AddExternalPlanSetupAsVerificationPlan(self, structureSet, verifiedPlan):
        # type: (self: Course, structureSet: StructureSet, verifiedPlan: ExternalPlanSetup) -> ExternalPlanSetup
        """ AddExternalPlanSetupAsVerificationPlan(self: Course, structureSet: StructureSet, verifiedPlan: ExternalPlanSetup) -> ExternalPlanSetup """
        pass

    def AddIonPlanSetup(self, structureSet, patientSupportDeviceId):
        # type: (self: Course, structureSet: StructureSet, patientSupportDeviceId: str) -> IonPlanSetup
        """ AddIonPlanSetup(self: Course, structureSet: StructureSet, patientSupportDeviceId: str) -> IonPlanSetup """
        pass

    def AddIonPlanSetupAsVerificationPlan(self, structureSet, patientSupportDeviceId, verifiedPlan):
        # type: (self: Course, structureSet: StructureSet, patientSupportDeviceId: str, verifiedPlan: IonPlanSetup) -> IonPlanSetup
        """ AddIonPlanSetupAsVerificationPlan(self: Course, structureSet: StructureSet, patientSupportDeviceId: str, verifiedPlan: IonPlanSetup) -> IonPlanSetup """
        pass

    def CanAddPlanSetup(self, structureSet):
        # type: (self: Course, structureSet: StructureSet) -> bool
        """ CanAddPlanSetup(self: Course, structureSet: StructureSet) -> bool """
        pass

    def CanRemovePlanSetup(self, planSetup):
        # type: (self: Course, planSetup: PlanSetup) -> bool
        """ CanRemovePlanSetup(self: Course, planSetup: PlanSetup) -> bool """
        pass

    def CopyPlanSetup(self, sourcePlan, structureset=None, outputDiagnostics=None):
        # type: (self: Course, sourcePlan: PlanSetup) -> PlanSetup
        """
        CopyPlanSetup(self: Course, sourcePlan: PlanSetup) -> PlanSetup
        CopyPlanSetup(self: Course, sourcePlan: PlanSetup, structureset: StructureSet, outputDiagnostics: StringBuilder) -> PlanSetup
        """
        pass

    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def RemovePlanSetup(self, planSetup):
        # type: (self: Course, planSetup: PlanSetup)
        """ RemovePlanSetup(self: Course, planSetup: PlanSetup) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: Course, writer: XmlWriter)
        """ WriteXml(self: Course, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BrachyPlanSetups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Course) -> IEnumerable[BrachyPlanSetup]
    """ Get: BrachyPlanSetups(self: Course) -> IEnumerable[BrachyPlanSetup] """

    CompletedDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Course) -> Nullable[DateTime]
    """ Get: CompletedDateTime(self: Course) -> Nullable[DateTime] """

    Diagnoses = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Course) -> IEnumerable[Diagnosis]
    """ Get: Diagnoses(self: Course) -> IEnumerable[Diagnosis] """

    ExternalPlanSetups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Course) -> IEnumerable[ExternalPlanSetup]
    """ Get: ExternalPlanSetups(self: Course) -> IEnumerable[ExternalPlanSetup] """

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Course) -> str
    """
    Get: Id(self: Course) -> str
    
    Set: Id(self: Course) = value
    """

    Intent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Course) -> str
    """ Get: Intent(self: Course) -> str """

    IonPlanSetups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Course) -> IEnumerable[IonPlanSetup]
    """ Get: IonPlanSetups(self: Course) -> IEnumerable[IonPlanSetup] """

    Patient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Course) -> Patient
    """ Get: Patient(self: Course) -> Patient """

    PlanSetups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Course) -> IEnumerable[PlanSetup]
    """ Get: PlanSetups(self: Course) -> IEnumerable[PlanSetup] """

    PlanSums = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Course) -> IEnumerable[PlanSum]
    """ Get: PlanSums(self: Course) -> IEnumerable[PlanSum] """

    StartDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Course) -> Nullable[DateTime]
    """ Get: StartDateTime(self: Course) -> Nullable[DateTime] """

    TreatmentPhases = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Course) -> IEnumerable[TreatmentPhase]
    """ Get: TreatmentPhases(self: Course) -> IEnumerable[TreatmentPhase] """

    TreatmentSessions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Course) -> IEnumerable[TreatmentSession]
    """ Get: TreatmentSessions(self: Course) -> IEnumerable[TreatmentSession] """



class CustomScriptExecutable(object):
    # no doc
    @staticmethod
    def CreateApplication(scriptName):
        # type: (scriptName: str) -> Application
        """ CreateApplication(scriptName: str) -> Application """
        pass

    __all__ = [
        'CreateApplication',
    ]


class Diagnosis(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: Diagnosis, writer: XmlWriter)
        """ WriteXml(self: Diagnosis, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ClinicalDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Diagnosis) -> str
    """ Get: ClinicalDescription(self: Diagnosis) -> str """

    Code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Diagnosis) -> str
    """ Get: Code(self: Diagnosis) -> str """

    CodeTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Diagnosis) -> str
    """ Get: CodeTable(self: Diagnosis) -> str """



class DVHData(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: DVHData, writer: XmlWriter)
        """ WriteXml(self: DVHData, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Coverage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: DVHData) -> float
    """ Get: Coverage(self: DVHData) -> float """

    CurveData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: DVHData) -> Array[DVHPoint]
    """ Get: CurveData(self: DVHData) -> Array[DVHPoint] """

    MaxDose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: DVHData) -> DoseValue
    """ Get: MaxDose(self: DVHData) -> DoseValue """

    MeanDose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: DVHData) -> DoseValue
    """ Get: MeanDose(self: DVHData) -> DoseValue """

    MedianDose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: DVHData) -> DoseValue
    """ Get: MedianDose(self: DVHData) -> DoseValue """

    MinDose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: DVHData) -> DoseValue
    """ Get: MinDose(self: DVHData) -> DoseValue """

    SamplingCoverage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: DVHData) -> float
    """ Get: SamplingCoverage(self: DVHData) -> float """

    StdDev = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: DVHData) -> float
    """ Get: StdDev(self: DVHData) -> float """

    Volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: DVHData) -> float
    """ Get: Volume(self: DVHData) -> float """



class Wedge(AddOn, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: Wedge, writer: XmlWriter)
        """ WriteXml(self: Wedge, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Wedge) -> float
    """ Get: Direction(self: Wedge) -> float """

    WedgeAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Wedge) -> float
    """ Get: WedgeAngle(self: Wedge) -> float """



class DynamicWedge(Wedge, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: DynamicWedge, writer: XmlWriter)
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
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: EnhancedDynamicWedge, writer: XmlWriter)
        """ WriteXml(self: EnhancedDynamicWedge, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class ESAPIActionPackAttribute(Attribute, _Attribute):
    # type: ()
    """ ESAPIActionPackAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    IsWriteable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ESAPIActionPackAttribute) -> bool
    """
    Get: IsWriteable(self: ESAPIActionPackAttribute) -> bool
    
    Set: IsWriteable(self: ESAPIActionPackAttribute) = value
    """



class ESAPIScriptAttribute(Attribute, _Attribute):
    # type: ()
    """ ESAPIScriptAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    IsWriteable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ESAPIScriptAttribute) -> bool
    """
    Get: IsWriteable(self: ESAPIScriptAttribute) -> bool
    
    Set: IsWriteable(self: ESAPIScriptAttribute) = value
    """



class EstimatedDVH(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: EstimatedDVH, writer: XmlWriter)
        """ WriteXml(self: EstimatedDVH, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CurveData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: EstimatedDVH) -> Array[DVHPoint]
    """ Get: CurveData(self: EstimatedDVH) -> Array[DVHPoint] """

    PlanSetup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: EstimatedDVH) -> PlanSetup
    """ Get: PlanSetup(self: EstimatedDVH) -> PlanSetup """

    PlanSetupId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: EstimatedDVH) -> str
    """ Get: PlanSetupId(self: EstimatedDVH) -> str """

    Structure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: EstimatedDVH) -> Structure
    """ Get: Structure(self: EstimatedDVH) -> Structure """

    StructureId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: EstimatedDVH) -> str
    """ Get: StructureId(self: EstimatedDVH) -> str """

    TargetDoseLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: EstimatedDVH) -> DoseValue
    """ Get: TargetDoseLevel(self: EstimatedDVH) -> DoseValue """

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: EstimatedDVH) -> DVHEstimateType
    """ Get: Type(self: EstimatedDVH) -> DVHEstimateType """



class EvaluationDose(Dose, IXmlSerializable):
    # no doc
    def DoseValueToVoxel(self, doseValue):
        # type: (self: EvaluationDose, doseValue: DoseValue) -> int
        """ DoseValueToVoxel(self: EvaluationDose, doseValue: DoseValue) -> int """
        pass

    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def SetVoxels(self, planeIndex, values):
        # type: (self: EvaluationDose, planeIndex: int, values: Array[int])
        """ SetVoxels(self: EvaluationDose, planeIndex: int, values: Array[int]) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: EvaluationDose, writer: XmlWriter)
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
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: ExternalBeamTreatmentUnit, writer: XmlWriter)
        """ WriteXml(self: ExternalBeamTreatmentUnit, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    MachineModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ExternalBeamTreatmentUnit) -> str
    """ Get: MachineModel(self: ExternalBeamTreatmentUnit) -> str """

    MachineModelName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ExternalBeamTreatmentUnit) -> str
    """ Get: MachineModelName(self: ExternalBeamTreatmentUnit) -> str """

    MachineScaleDisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ExternalBeamTreatmentUnit) -> str
    """ Get: MachineScaleDisplayName(self: ExternalBeamTreatmentUnit) -> str """

    OperatingLimits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ExternalBeamTreatmentUnit) -> TreatmentUnitOperatingLimits
    """ Get: OperatingLimits(self: ExternalBeamTreatmentUnit) -> TreatmentUnitOperatingLimits """

    SourceAxisDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ExternalBeamTreatmentUnit) -> float
    """ Get: SourceAxisDistance(self: ExternalBeamTreatmentUnit) -> float """



class ExternalPlanSetup(PlanSetup, IXmlSerializable):
    # no doc
    def AddArcBeam(self, machineParameters, jawPositions, collimatorAngle, gantryAngle, gantryStop, gantryDirection, patientSupportAngle, isocenter):
        # type: (self: ExternalPlanSetup, machineParameters: ExternalBeamMachineParameters, jawPositions: VRect[float], collimatorAngle: float, gantryAngle: float, gantryStop: float, gantryDirection: GantryDirection, patientSupportAngle: float, isocenter: VVector) -> Beam
        """ AddArcBeam(self: ExternalPlanSetup, machineParameters: ExternalBeamMachineParameters, jawPositions: VRect[float], collimatorAngle: float, gantryAngle: float, gantryStop: float, gantryDirection: GantryDirection, patientSupportAngle: float, isocenter: VVector) -> Beam """
        pass

    def AddConformalArcBeam(self, machineParameters, collimatorAngle, controlPointCount, gantryAngle, gantryStop, gantryDirection, patientSupportAngle, isocenter):
        # type: (self: ExternalPlanSetup, machineParameters: ExternalBeamMachineParameters, collimatorAngle: float, controlPointCount: int, gantryAngle: float, gantryStop: float, gantryDirection: GantryDirection, patientSupportAngle: float, isocenter: VVector) -> Beam
        """ AddConformalArcBeam(self: ExternalPlanSetup, machineParameters: ExternalBeamMachineParameters, collimatorAngle: float, controlPointCount: int, gantryAngle: float, gantryStop: float, gantryDirection: GantryDirection, patientSupportAngle: float, isocenter: VVector) -> Beam """
        pass

    def AddMLCArcBeam(self, machineParameters, leafPositions, jawPositions, collimatorAngle, gantryAngle, gantryStop, gantryDirection, patientSupportAngle, isocenter):
        # type: (self: ExternalPlanSetup, machineParameters: ExternalBeamMachineParameters, leafPositions: Array[Single], jawPositions: VRect[float], collimatorAngle: float, gantryAngle: float, gantryStop: float, gantryDirection: GantryDirection, patientSupportAngle: float, isocenter: VVector) -> Beam
        """ AddMLCArcBeam(self: ExternalPlanSetup, machineParameters: ExternalBeamMachineParameters, leafPositions: Array[Single], jawPositions: VRect[float], collimatorAngle: float, gantryAngle: float, gantryStop: float, gantryDirection: GantryDirection, patientSupportAngle: float, isocenter: VVector) -> Beam """
        pass

    def AddMLCBeam(self, machineParameters, leafPositions, jawPositions, collimatorAngle, gantryAngle, patientSupportAngle, isocenter):
        # type: (self: ExternalPlanSetup, machineParameters: ExternalBeamMachineParameters, leafPositions: Array[Single], jawPositions: VRect[float], collimatorAngle: float, gantryAngle: float, patientSupportAngle: float, isocenter: VVector) -> Beam
        """ AddMLCBeam(self: ExternalPlanSetup, machineParameters: ExternalBeamMachineParameters, leafPositions: Array[Single], jawPositions: VRect[float], collimatorAngle: float, gantryAngle: float, patientSupportAngle: float, isocenter: VVector) -> Beam """
        pass

    def AddMultipleStaticSegmentBeam(self, machineParameters, metersetWeights, collimatorAngle, gantryAngle, patientSupportAngle, isocenter):
        # type: (self: ExternalPlanSetup, machineParameters: ExternalBeamMachineParameters, metersetWeights: IEnumerable[float], collimatorAngle: float, gantryAngle: float, patientSupportAngle: float, isocenter: VVector) -> Beam
        """ AddMultipleStaticSegmentBeam(self: ExternalPlanSetup, machineParameters: ExternalBeamMachineParameters, metersetWeights: IEnumerable[float], collimatorAngle: float, gantryAngle: float, patientSupportAngle: float, isocenter: VVector) -> Beam """
        pass

    def AddSlidingWindowBeam(self, machineParameters, metersetWeights, collimatorAngle, gantryAngle, patientSupportAngle, isocenter):
        # type: (self: ExternalPlanSetup, machineParameters: ExternalBeamMachineParameters, metersetWeights: IEnumerable[float], collimatorAngle: float, gantryAngle: float, patientSupportAngle: float, isocenter: VVector) -> Beam
        """ AddSlidingWindowBeam(self: ExternalPlanSetup, machineParameters: ExternalBeamMachineParameters, metersetWeights: IEnumerable[float], collimatorAngle: float, gantryAngle: float, patientSupportAngle: float, isocenter: VVector) -> Beam """
        pass

    def AddStaticBeam(self, machineParameters, jawPositions, collimatorAngle, gantryAngle, patientSupportAngle, isocenter):
        # type: (self: ExternalPlanSetup, machineParameters: ExternalBeamMachineParameters, jawPositions: VRect[float], collimatorAngle: float, gantryAngle: float, patientSupportAngle: float, isocenter: VVector) -> Beam
        """ AddStaticBeam(self: ExternalPlanSetup, machineParameters: ExternalBeamMachineParameters, jawPositions: VRect[float], collimatorAngle: float, gantryAngle: float, patientSupportAngle: float, isocenter: VVector) -> Beam """
        pass

    def AddVMATBeam(self, machineParameters, metersetWeights, collimatorAngle, gantryAngle, gantryStop, gantryDirection, patientSupportAngle, isocenter):
        # type: (self: ExternalPlanSetup, machineParameters: ExternalBeamMachineParameters, metersetWeights: IEnumerable[float], collimatorAngle: float, gantryAngle: float, gantryStop: float, gantryDirection: GantryDirection, patientSupportAngle: float, isocenter: VVector) -> Beam
        """ AddVMATBeam(self: ExternalPlanSetup, machineParameters: ExternalBeamMachineParameters, metersetWeights: IEnumerable[float], collimatorAngle: float, gantryAngle: float, gantryStop: float, gantryDirection: GantryDirection, patientSupportAngle: float, isocenter: VVector) -> Beam """
        pass

    def AttachToCalcClient(self, *args): #cannot find CLR method
        # type: (self: PlanSetup, doseCalcClient: ICalculationClient)
        """ AttachToCalcClient(self: PlanSetup, doseCalcClient: ICalculationClient) """
        pass

    def CalculateDose(self):
        # type: (self: ExternalPlanSetup) -> CalculationResult
        """ CalculateDose(self: ExternalPlanSetup) -> CalculationResult """
        pass

    def CalculateDoseWithPresetValues(self, presetValues):
        # type: (self: ExternalPlanSetup, presetValues: List[KeyValuePair[str, MetersetValue]]) -> CalculationResult
        """ CalculateDoseWithPresetValues(self: ExternalPlanSetup, presetValues: List[KeyValuePair[str, MetersetValue]]) -> CalculationResult """
        pass

    def CalculateDVHEstimates(self, modelId, targetDoseLevels, structureMatches):
        # type: (self: ExternalPlanSetup, modelId: str, targetDoseLevels: Dictionary[str, DoseValue], structureMatches: Dictionary[str, str]) -> CalculationResult
        """ CalculateDVHEstimates(self: ExternalPlanSetup, modelId: str, targetDoseLevels: Dictionary[str, DoseValue], structureMatches: Dictionary[str, str]) -> CalculationResult """
        pass

    def CalculateLeafMotions(self, options=None):
        # type: (self: ExternalPlanSetup) -> CalculationResult
        """
        CalculateLeafMotions(self: ExternalPlanSetup) -> CalculationResult
        CalculateLeafMotions(self: ExternalPlanSetup, options: LMCVOptions) -> CalculationResult
        CalculateLeafMotions(self: ExternalPlanSetup, options: SmartLMCOptions) -> CalculationResult
        CalculateLeafMotions(self: ExternalPlanSetup, options: LMCMSSOptions) -> CalculationResult
        """
        pass

    def CalculateLeafMotionsAndDose(self):
        # type: (self: ExternalPlanSetup) -> CalculationResult
        """ CalculateLeafMotionsAndDose(self: ExternalPlanSetup) -> CalculationResult """
        pass

    def CopyEvaluationDose(self, existing):
        # type: (self: ExternalPlanSetup, existing: Dose) -> EvaluationDose
        """ CopyEvaluationDose(self: ExternalPlanSetup, existing: Dose) -> EvaluationDose """
        pass

    def CreateEvaluationDose(self):
        # type: (self: ExternalPlanSetup) -> EvaluationDose
        """ CreateEvaluationDose(self: ExternalPlanSetup) -> EvaluationDose """
        pass

    def DetachFromCalcClient(self, *args): #cannot find CLR method
        # type: (self: PlanSetup, doseCalcClient: ICalculationClient)
        """ DetachFromCalcClient(self: PlanSetup, doseCalcClient: ICalculationClient) """
        pass

    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetModelsForCalculationType(self, calculationType):
        # type: (self: ExternalPlanSetup, calculationType: CalculationType) -> IEnumerable[str]
        """ GetModelsForCalculationType(self: ExternalPlanSetup, calculationType: CalculationType) -> IEnumerable[str] """
        pass

    def Optimize(self, *__args):
        # type: (self: ExternalPlanSetup, maxIterations: int) -> OptimizerResult
        """
        Optimize(self: ExternalPlanSetup, maxIterations: int) -> OptimizerResult
        Optimize(self: ExternalPlanSetup, maxIterations: int, optimizationOption: OptimizationOption) -> OptimizerResult
        Optimize(self: ExternalPlanSetup, maxIterations: int, optimizationOption: OptimizationOption, mlcId: str) -> OptimizerResult
        Optimize(self: ExternalPlanSetup) -> OptimizerResult
        Optimize(self: ExternalPlanSetup, options: OptimizationOptionsIMRT) -> OptimizerResult
        """
        pass

    def OptimizeVMAT(self, *__args):
        # type: (self: ExternalPlanSetup, mlcId: str) -> OptimizerResult
        """
        OptimizeVMAT(self: ExternalPlanSetup, mlcId: str) -> OptimizerResult
        OptimizeVMAT(self: ExternalPlanSetup) -> OptimizerResult
        OptimizeVMAT(self: ExternalPlanSetup, options: OptimizationOptionsVMAT) -> OptimizerResult
        """
        pass

    def RemoveBeam(self, beam):
        # type: (self: ExternalPlanSetup, beam: Beam)
        """ RemoveBeam(self: ExternalPlanSetup, beam: Beam) """
        pass

    def Report(self, *args): #cannot find CLR method
        # type: (self: PlanSetup, str: str)
        """ Report(self: PlanSetup, str: str) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: ExternalPlanSetup, writer: XmlWriter)
        """ WriteXml(self: ExternalPlanSetup, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DoseAsEvaluationDose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ExternalPlanSetup) -> EvaluationDose
    """ Get: DoseAsEvaluationDose(self: ExternalPlanSetup) -> EvaluationDose """

    TradeoffExplorationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ExternalPlanSetup) -> TradeoffExplorationContext
    """ Get: TradeoffExplorationContext(self: ExternalPlanSetup) -> TradeoffExplorationContext """


    m_errorsOnCalculationCompleted = None


class FieldReferencePoint(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: FieldReferencePoint, writer: XmlWriter)
        """ WriteXml(self: FieldReferencePoint, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    EffectiveDepth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: FieldReferencePoint) -> float
    """ Get: EffectiveDepth(self: FieldReferencePoint) -> float """

    FieldDose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: FieldReferencePoint) -> DoseValue
    """ Get: FieldDose(self: FieldReferencePoint) -> DoseValue """

    IsFieldDoseNominal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: FieldReferencePoint) -> bool
    """ Get: IsFieldDoseNominal(self: FieldReferencePoint) -> bool """

    IsPrimaryReferencePoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: FieldReferencePoint) -> bool
    """ Get: IsPrimaryReferencePoint(self: FieldReferencePoint) -> bool """

    ReferencePoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: FieldReferencePoint) -> ReferencePoint
    """ Get: ReferencePoint(self: FieldReferencePoint) -> ReferencePoint """

    RefPointLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: FieldReferencePoint) -> VVector
    """ Get: RefPointLocation(self: FieldReferencePoint) -> VVector """

    SSD = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: FieldReferencePoint) -> float
    """ Get: SSD(self: FieldReferencePoint) -> float """



class Globals(object):
    # type: ()
    """ Globals() """
    @staticmethod
    def DisableApiAccessTrace():
        # type: ()
        """ DisableApiAccessTrace() """
        pass

    @staticmethod
    def EnableApiAccessTrace():
        # type: ()
        """ EnableApiAccessTrace() """
        pass

    @staticmethod
    def GetLoggedApiCalls():
        # type: () -> IEnumerable[str]
        """ GetLoggedApiCalls() -> IEnumerable[str] """
        pass

    @staticmethod
    def SetMaximumNumberOfLoggedApiCalls(apiLogCacheSize):
        # type: (apiLogCacheSize: int)
        """ SetMaximumNumberOfLoggedApiCalls(apiLogCacheSize: int) """
        pass

    AbortNow = False
    DefaultMaximumNumberOfLoggedApiCalls = 200


class Hospital(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: Hospital, writer: XmlWriter)
        """ WriteXml(self: Hospital, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CreationDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Hospital) -> Nullable[DateTime]
    """ Get: CreationDateTime(self: Hospital) -> Nullable[DateTime] """

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Hospital) -> str
    """ Get: Location(self: Hospital) -> str """



class Image(ApiDataObject, IXmlSerializable):
    # no doc
    def CreateNewStructureSet(self):
        # type: (self: Image) -> StructureSet
        """ CreateNewStructureSet(self: Image) -> StructureSet """
        pass

    def DicomToUser(self, dicom, planSetup):
        # type: (self: Image, dicom: VVector, planSetup: PlanSetup) -> VVector
        """ DicomToUser(self: Image, dicom: VVector, planSetup: PlanSetup) -> VVector """
        pass

    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetImageProfile(self, start, stop, preallocatedBuffer):
        # type: (self: Image, start: VVector, stop: VVector, preallocatedBuffer: Array[float]) -> ImageProfile
        """ GetImageProfile(self: Image, start: VVector, stop: VVector, preallocatedBuffer: Array[float]) -> ImageProfile """
        pass

    def GetVoxels(self, planeIndex, preallocatedBuffer):
        # type: (self: Image, planeIndex: int, preallocatedBuffer: Array[int])
        """ GetVoxels(self: Image, planeIndex: int, preallocatedBuffer: Array[int]) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def UserToDicom(self, user, planSetup):
        # type: (self: Image, user: VVector, planSetup: PlanSetup) -> VVector
        """ UserToDicom(self: Image, user: VVector, planSetup: PlanSetup) -> VVector """
        pass

    def VoxelToDisplayValue(self, voxelValue):
        # type: (self: Image, voxelValue: int) -> float
        """ VoxelToDisplayValue(self: Image, voxelValue: int) -> float """
        pass

    def WriteXml(self, writer):
        # type: (self: Image, writer: XmlWriter)
        """ WriteXml(self: Image, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ApprovalHistory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Image) -> IEnumerable[ImageApprovalHistoryEntry]
    """ Get: ApprovalHistory(self: Image) -> IEnumerable[ImageApprovalHistoryEntry] """

    ContrastBolusAgentIngredientName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Image) -> str
    """ Get: ContrastBolusAgentIngredientName(self: Image) -> str """

    CreationDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Image) -> Nullable[DateTime]
    """ Get: CreationDateTime(self: Image) -> Nullable[DateTime] """

    DisplayUnit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Image) -> str
    """ Get: DisplayUnit(self: Image) -> str """

    FOR = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Image) -> str
    """ Get: FOR(self: Image) -> str """

    HasUserOrigin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Image) -> bool
    """ Get: HasUserOrigin(self: Image) -> bool """

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Image) -> str
    """
    Get: Id(self: Image) -> str
    
    Set: Id(self: Image) = value
    """

    ImagingOrientation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Image) -> PatientOrientation
    """ Get: ImagingOrientation(self: Image) -> PatientOrientation """

    IsProcessed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Image) -> bool
    """ Get: IsProcessed(self: Image) -> bool """

    Level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Image) -> int
    """ Get: Level(self: Image) -> int """

    Origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Image) -> VVector
    """ Get: Origin(self: Image) -> VVector """

    Series = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Image) -> Series
    """ Get: Series(self: Image) -> Series """

    UserOrigin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Image) -> VVector
    """
    Get: UserOrigin(self: Image) -> VVector
    
    Set: UserOrigin(self: Image) = value
    """

    UserOriginComments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Image) -> str
    """ Get: UserOriginComments(self: Image) -> str """

    Window = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Image) -> int
    """ Get: Window(self: Image) -> int """

    XDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Image) -> VVector
    """ Get: XDirection(self: Image) -> VVector """

    XRes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Image) -> float
    """ Get: XRes(self: Image) -> float """

    XSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Image) -> int
    """ Get: XSize(self: Image) -> int """

    YDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Image) -> VVector
    """ Get: YDirection(self: Image) -> VVector """

    YRes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Image) -> float
    """ Get: YRes(self: Image) -> float """

    YSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Image) -> int
    """ Get: YSize(self: Image) -> int """

    ZDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Image) -> VVector
    """ Get: ZDirection(self: Image) -> VVector """

    ZRes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Image) -> float
    """ Get: ZRes(self: Image) -> float """

    ZSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Image) -> int
    """ Get: ZSize(self: Image) -> int """



class IonBeam(Beam, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetEditableParameters(self):
        # type: (self: IonBeam) -> IonBeamParameters
        """ GetEditableParameters(self: IonBeam) -> IonBeamParameters """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: IonBeam, writer: XmlWriter)
        """ WriteXml(self: IonBeam, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AirGap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonBeam) -> float
    """ Get: AirGap(self: IonBeam) -> float """

    DistalTargetMargin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonBeam) -> float
    """ Get: DistalTargetMargin(self: IonBeam) -> float """

    IonControlPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonBeam) -> IonControlPointCollection
    """ Get: IonControlPoints(self: IonBeam) -> IonControlPointCollection """

    LateralMargins = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonBeam) -> VRect[float]
    """ Get: LateralMargins(self: IonBeam) -> VRect[float] """

    LateralSpreadingDevices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonBeam) -> IEnumerable[LateralSpreadingDevice]
    """ Get: LateralSpreadingDevices(self: IonBeam) -> IEnumerable[LateralSpreadingDevice] """

    NominalRange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonBeam) -> float
    """ Get: NominalRange(self: IonBeam) -> float """

    NominalSOBPWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonBeam) -> float
    """ Get: NominalSOBPWidth(self: IonBeam) -> float """

    OptionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonBeam) -> str
    """ Get: OptionId(self: IonBeam) -> str """

    PatientSupportId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonBeam) -> str
    """ Get: PatientSupportId(self: IonBeam) -> str """

    PatientSupportType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonBeam) -> PatientSupportType
    """ Get: PatientSupportType(self: IonBeam) -> PatientSupportType """

    ProximalTargetMargin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonBeam) -> float
    """ Get: ProximalTargetMargin(self: IonBeam) -> float """

    RangeModulators = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonBeam) -> IEnumerable[RangeModulator]
    """ Get: RangeModulators(self: IonBeam) -> IEnumerable[RangeModulator] """

    RangeShifters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonBeam) -> IEnumerable[RangeShifter]
    """ Get: RangeShifters(self: IonBeam) -> IEnumerable[RangeShifter] """

    ScanMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonBeam) -> IonBeamScanMode
    """ Get: ScanMode(self: IonBeam) -> IonBeamScanMode """

    SnoutId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonBeam) -> str
    """ Get: SnoutId(self: IonBeam) -> str """

    TargetStructure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonBeam) -> Structure
    """ Get: TargetStructure(self: IonBeam) -> Structure """

    VirtualSADX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonBeam) -> float
    """ Get: VirtualSADX(self: IonBeam) -> float """

    VirtualSADY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonBeam) -> float
    """ Get: VirtualSADY(self: IonBeam) -> float """



class IonBeamParameters(BeamParameters):
    # no doc
    ControlPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonBeamParameters) -> IEnumerable[IonControlPointParameters]
    """ Get: ControlPoints(self: IonBeamParameters) -> IEnumerable[IonControlPointParameters] """

    IonControlPointPairs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonBeamParameters) -> IonControlPointPairCollection
    """ Get: IonControlPointPairs(self: IonBeamParameters) -> IonControlPointPairCollection """



class IonControlPoint(ControlPoint, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: IonControlPoint, writer: XmlWriter)
        """ WriteXml(self: IonControlPoint, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    FinalSpotList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonControlPoint) -> IonSpotCollection
    """ Get: FinalSpotList(self: IonControlPoint) -> IonSpotCollection """

    LateralSpreadingDeviceSettings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonControlPoint) -> IEnumerable[LateralSpreadingDeviceSettings]
    """ Get: LateralSpreadingDeviceSettings(self: IonControlPoint) -> IEnumerable[LateralSpreadingDeviceSettings] """

    NominalBeamEnergy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonControlPoint) -> float
    """ Get: NominalBeamEnergy(self: IonControlPoint) -> float """

    NumberOfPaintings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonControlPoint) -> int
    """ Get: NumberOfPaintings(self: IonControlPoint) -> int """

    RangeModulatorSettings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonControlPoint) -> IEnumerable[RangeModulatorSettings]
    """ Get: RangeModulatorSettings(self: IonControlPoint) -> IEnumerable[RangeModulatorSettings] """

    RangeShifterSettings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonControlPoint) -> IEnumerable[RangeShifterSettings]
    """ Get: RangeShifterSettings(self: IonControlPoint) -> IEnumerable[RangeShifterSettings] """

    RawSpotList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonControlPoint) -> IonSpotCollection
    """ Get: RawSpotList(self: IonControlPoint) -> IonSpotCollection """

    ScanningSpotSizeX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonControlPoint) -> float
    """ Get: ScanningSpotSizeX(self: IonControlPoint) -> float """

    ScanningSpotSizeY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonControlPoint) -> float
    """ Get: ScanningSpotSizeY(self: IonControlPoint) -> float """

    ScanSpotTuneId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonControlPoint) -> str
    """ Get: ScanSpotTuneId(self: IonControlPoint) -> str """

    SnoutPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonControlPoint) -> float
    """ Get: SnoutPosition(self: IonControlPoint) -> float """



class IonControlPointCollection(SerializableObject, IXmlSerializable, IEnumerable[IonControlPoint], IEnumerable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetEnumerator(self):
        # type: (self: IonControlPointCollection) -> IEnumerator[IonControlPoint]
        """ GetEnumerator(self: IonControlPointCollection) -> IEnumerator[IonControlPoint] """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: IonControlPointCollection, writer: XmlWriter)
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
    # type: (self: IonControlPointCollection) -> int
    """ Get: Count(self: IonControlPointCollection) -> int """



class IonControlPointPair(object):
    # no doc
    def ResizeFinalSpotList(self, count):
        # type: (self: IonControlPointPair, count: int)
        """ ResizeFinalSpotList(self: IonControlPointPair, count: int) """
        pass

    def ResizeRawSpotList(self, count):
        # type: (self: IonControlPointPair, count: int)
        """ ResizeRawSpotList(self: IonControlPointPair, count: int) """
        pass

    EndControlPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonControlPointPair) -> IonControlPointParameters
    """ Get: EndControlPoint(self: IonControlPointPair) -> IonControlPointParameters """

    FinalSpotList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonControlPointPair) -> IonSpotParametersCollection
    """ Get: FinalSpotList(self: IonControlPointPair) -> IonSpotParametersCollection """

    NominalBeamEnergy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonControlPointPair) -> float
    """ Get: NominalBeamEnergy(self: IonControlPointPair) -> float """

    RawSpotList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonControlPointPair) -> IonSpotParametersCollection
    """ Get: RawSpotList(self: IonControlPointPair) -> IonSpotParametersCollection """

    StartControlPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonControlPointPair) -> IonControlPointParameters
    """ Get: StartControlPoint(self: IonControlPointPair) -> IonControlPointParameters """

    StartIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonControlPointPair) -> int
    """ Get: StartIndex(self: IonControlPointPair) -> int """



class IonControlPointPairCollection(object, IEnumerable[IonControlPointPair], IEnumerable):
    # no doc
    def GetEnumerator(self):
        # type: (self: IonControlPointPairCollection) -> IEnumerator[IonControlPointPair]
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
    # type: (self: IonControlPointPairCollection) -> int
    """ Get: Count(self: IonControlPointPairCollection) -> int """



class IonControlPointParameters(ControlPointParameters):
    # no doc
    FinalSpotList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonControlPointParameters) -> IonSpotParametersCollection
    """ Get: FinalSpotList(self: IonControlPointParameters) -> IonSpotParametersCollection """

    RawSpotList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonControlPointParameters) -> IonSpotParametersCollection
    """ Get: RawSpotList(self: IonControlPointParameters) -> IonSpotParametersCollection """



class IonPlanSetup(PlanSetup, IXmlSerializable):
    # no doc
    def AttachToCalcClient(self, *args): #cannot find CLR method
        # type: (self: PlanSetup, doseCalcClient: ICalculationClient)
        """ AttachToCalcClient(self: PlanSetup, doseCalcClient: ICalculationClient) """
        pass

    def CalculateDose(self):
        # type: (self: IonPlanSetup) -> CalculationResult
        """ CalculateDose(self: IonPlanSetup) -> CalculationResult """
        pass

    def CalculateDoseWithoutPostProcessing(self):
        # type: (self: IonPlanSetup) -> CalculationResult
        """ CalculateDoseWithoutPostProcessing(self: IonPlanSetup) -> CalculationResult """
        pass

    def CopyEvaluationDose(self, existing):
        # type: (self: IonPlanSetup, existing: Dose) -> EvaluationDose
        """ CopyEvaluationDose(self: IonPlanSetup, existing: Dose) -> EvaluationDose """
        pass

    def CreateEvaluationDose(self):
        # type: (self: IonPlanSetup) -> EvaluationDose
        """ CreateEvaluationDose(self: IonPlanSetup) -> EvaluationDose """
        pass

    def DetachFromCalcClient(self, *args): #cannot find CLR method
        # type: (self: PlanSetup, doseCalcClient: ICalculationClient)
        """ DetachFromCalcClient(self: PlanSetup, doseCalcClient: ICalculationClient) """
        pass

    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetModelsForCalculationType(self, calculationType):
        # type: (self: IonPlanSetup, calculationType: CalculationType) -> IEnumerable[str]
        """ GetModelsForCalculationType(self: IonPlanSetup, calculationType: CalculationType) -> IEnumerable[str] """
        pass

    def PostProcessAndCalculateDose(self):
        # type: (self: IonPlanSetup) -> CalculationResult
        """ PostProcessAndCalculateDose(self: IonPlanSetup) -> CalculationResult """
        pass

    def Report(self, *args): #cannot find CLR method
        # type: (self: PlanSetup, str: str)
        """ Report(self: PlanSetup, str: str) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: IonPlanSetup, writer: XmlWriter)
        """ WriteXml(self: IonPlanSetup, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DoseAsEvaluationDose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonPlanSetup) -> EvaluationDose
    """ Get: DoseAsEvaluationDose(self: IonPlanSetup) -> EvaluationDose """

    IonBeams = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonPlanSetup) -> IEnumerable[IonBeam]
    """ Get: IonBeams(self: IonPlanSetup) -> IEnumerable[IonBeam] """

    IsPostProcessingNeeded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonPlanSetup) -> bool
    """
    Get: IsPostProcessingNeeded(self: IonPlanSetup) -> bool
    
    Set: IsPostProcessingNeeded(self: IonPlanSetup) = value
    """


    m_errorsOnCalculationCompleted = None


class IonSpot(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: IonSpot, writer: XmlWriter)
        """ WriteXml(self: IonSpot, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonSpot) -> VVector
    """ Get: Position(self: IonSpot) -> VVector """

    Weight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonSpot) -> Single
    """ Get: Weight(self: IonSpot) -> Single """



class IonSpotCollection(SerializableObject, IXmlSerializable, IEnumerable[IonSpot], IEnumerable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetEnumerator(self):
        # type: (self: IonSpotCollection) -> IEnumerator[IonSpot]
        """ GetEnumerator(self: IonSpotCollection) -> IEnumerator[IonSpot] """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: IonSpotCollection, writer: XmlWriter)
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
    # type: (self: IonSpotCollection) -> int
    """ Get: Count(self: IonSpotCollection) -> int """



class IonSpotParameters(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: IonSpotParameters, writer: XmlWriter)
        """ WriteXml(self: IonSpotParameters, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Weight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonSpotParameters) -> Single
    """
    Get: Weight(self: IonSpotParameters) -> Single
    
    Set: Weight(self: IonSpotParameters) = value
    """

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonSpotParameters) -> Single
    """
    Get: X(self: IonSpotParameters) -> Single
    
    Set: X(self: IonSpotParameters) = value
    """

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: IonSpotParameters) -> Single
    """
    Get: Y(self: IonSpotParameters) -> Single
    
    Set: Y(self: IonSpotParameters) = value
    """



class IonSpotParametersCollection(SerializableObject, IXmlSerializable, IEnumerable[IonSpotParameters], IEnumerable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetEnumerator(self):
        # type: (self: IonSpotParametersCollection) -> IEnumerator[IonSpotParameters]
        """ GetEnumerator(self: IonSpotParametersCollection) -> IEnumerator[IonSpotParameters] """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: IonSpotParametersCollection, writer: XmlWriter)
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
    # type: (self: IonSpotParametersCollection) -> int
    """ Get: Count(self: IonSpotParametersCollection) -> int """



class Isodose(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: Isodose, writer: XmlWriter)
        """ WriteXml(self: Isodose, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Isodose) -> Color
    """ Get: Color(self: Isodose) -> Color """

    Level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Isodose) -> DoseValue
    """ Get: Level(self: Isodose) -> DoseValue """

    MeshGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Isodose) -> MeshGeometry3D
    """ Get: MeshGeometry(self: Isodose) -> MeshGeometry3D """



class LateralSpreadingDevice(AddOn, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: LateralSpreadingDevice, writer: XmlWriter)
        """ WriteXml(self: LateralSpreadingDevice, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: LateralSpreadingDevice) -> LateralSpreadingDeviceType
    """ Get: Type(self: LateralSpreadingDevice) -> LateralSpreadingDeviceType """



class LateralSpreadingDeviceSettings(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: LateralSpreadingDeviceSettings, writer: XmlWriter)
        """ WriteXml(self: LateralSpreadingDeviceSettings, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    IsocenterToLateralSpreadingDeviceDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: LateralSpreadingDeviceSettings) -> float
    """ Get: IsocenterToLateralSpreadingDeviceDistance(self: LateralSpreadingDeviceSettings) -> float """

    LateralSpreadingDeviceSetting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: LateralSpreadingDeviceSettings) -> str
    """ Get: LateralSpreadingDeviceSetting(self: LateralSpreadingDeviceSettings) -> str """

    LateralSpreadingDeviceWaterEquivalentThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: LateralSpreadingDeviceSettings) -> float
    """ Get: LateralSpreadingDeviceWaterEquivalentThickness(self: LateralSpreadingDeviceSettings) -> float """

    ReferencedLateralSpreadingDevice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: LateralSpreadingDeviceSettings) -> LateralSpreadingDevice
    """ Get: ReferencedLateralSpreadingDevice(self: LateralSpreadingDeviceSettings) -> LateralSpreadingDevice """



class MLC(AddOn, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: MLC, writer: XmlWriter)
        """ WriteXml(self: MLC, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ManufacturerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: MLC) -> str
    """ Get: ManufacturerName(self: MLC) -> str """

    MinDoseDynamicLeafGap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: MLC) -> float
    """ Get: MinDoseDynamicLeafGap(self: MLC) -> float """

    Model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: MLC) -> str
    """ Get: Model(self: MLC) -> str """

    SerialNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: MLC) -> str
    """ Get: SerialNumber(self: MLC) -> str """



class MotorizedWedge(Wedge, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: MotorizedWedge, writer: XmlWriter)
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
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: OmniWedge, writer: XmlWriter)
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
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def Equals(self, obj):
        # type: (self: OptimizationObjective, obj: object) -> bool
        """ Equals(self: OptimizationObjective, obj: object) -> bool """
        pass

    def GetHashCode(self):
        # type: (self: OptimizationObjective) -> int
        """ GetHashCode(self: OptimizationObjective) -> int """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: OptimizationObjective, writer: XmlWriter)
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
    # type: (self: OptimizationObjective) -> OptimizationObjectiveOperator
    """ Get: Operator(self: OptimizationObjective) -> OptimizationObjectiveOperator """

    Priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizationObjective) -> float
    """ Get: Priority(self: OptimizationObjective) -> float """

    Structure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizationObjective) -> Structure
    """ Get: Structure(self: OptimizationObjective) -> Structure """

    StructureId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizationObjective) -> str
    """ Get: StructureId(self: OptimizationObjective) -> str """



class OptimizationEUDObjective(OptimizationObjective, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: OptimizationEUDObjective, writer: XmlWriter)
        """ WriteXml(self: OptimizationEUDObjective, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Dose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizationEUDObjective) -> DoseValue
    """ Get: Dose(self: OptimizationEUDObjective) -> DoseValue """

    ParameterA = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizationEUDObjective) -> float
    """ Get: ParameterA(self: OptimizationEUDObjective) -> float """



class OptimizationParameter(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def Equals(self, obj):
        # type: (self: OptimizationParameter, obj: object) -> bool
        """ Equals(self: OptimizationParameter, obj: object) -> bool """
        pass

    def GetHashCode(self):
        # type: (self: OptimizationParameter) -> int
        """ GetHashCode(self: OptimizationParameter) -> int """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: OptimizationParameter, writer: XmlWriter)
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
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: OptimizationExcludeStructureParameter, writer: XmlWriter)
        """ WriteXml(self: OptimizationExcludeStructureParameter, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Structure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizationExcludeStructureParameter) -> Structure
    """ Get: Structure(self: OptimizationExcludeStructureParameter) -> Structure """



class OptimizationIMRTBeamParameter(OptimizationParameter, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: OptimizationIMRTBeamParameter, writer: XmlWriter)
        """ WriteXml(self: OptimizationIMRTBeamParameter, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Beam = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizationIMRTBeamParameter) -> Beam
    """ Get: Beam(self: OptimizationIMRTBeamParameter) -> Beam """

    BeamId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizationIMRTBeamParameter) -> str
    """ Get: BeamId(self: OptimizationIMRTBeamParameter) -> str """

    Excluded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizationIMRTBeamParameter) -> bool
    """ Get: Excluded(self: OptimizationIMRTBeamParameter) -> bool """

    FixedJaws = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizationIMRTBeamParameter) -> bool
    """ Get: FixedJaws(self: OptimizationIMRTBeamParameter) -> bool """

    SmoothX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizationIMRTBeamParameter) -> float
    """ Get: SmoothX(self: OptimizationIMRTBeamParameter) -> float """

    SmoothY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizationIMRTBeamParameter) -> float
    """ Get: SmoothY(self: OptimizationIMRTBeamParameter) -> float """



class OptimizationJawTrackingUsedParameter(OptimizationParameter, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: OptimizationJawTrackingUsedParameter, writer: XmlWriter)
        """ WriteXml(self: OptimizationJawTrackingUsedParameter, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class OptimizationLineObjective(OptimizationObjective, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: OptimizationLineObjective, writer: XmlWriter)
        """ WriteXml(self: OptimizationLineObjective, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    CurveData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizationLineObjective) -> Array[DVHPoint]
    """ Get: CurveData(self: OptimizationLineObjective) -> Array[DVHPoint] """



class OptimizationMeanDoseObjective(OptimizationObjective, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: OptimizationMeanDoseObjective, writer: XmlWriter)
        """ WriteXml(self: OptimizationMeanDoseObjective, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Dose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizationMeanDoseObjective) -> DoseValue
    """ Get: Dose(self: OptimizationMeanDoseObjective) -> DoseValue """



class OptimizationNormalTissueParameter(OptimizationParameter, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: OptimizationNormalTissueParameter, writer: XmlWriter)
        """ WriteXml(self: OptimizationNormalTissueParameter, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DistanceFromTargetBorderInMM = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizationNormalTissueParameter) -> float
    """ Get: DistanceFromTargetBorderInMM(self: OptimizationNormalTissueParameter) -> float """

    EndDosePercentage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizationNormalTissueParameter) -> float
    """ Get: EndDosePercentage(self: OptimizationNormalTissueParameter) -> float """

    FallOff = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizationNormalTissueParameter) -> float
    """ Get: FallOff(self: OptimizationNormalTissueParameter) -> float """

    IsAutomatic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizationNormalTissueParameter) -> bool
    """ Get: IsAutomatic(self: OptimizationNormalTissueParameter) -> bool """

    Priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizationNormalTissueParameter) -> float
    """ Get: Priority(self: OptimizationNormalTissueParameter) -> float """

    StartDosePercentage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizationNormalTissueParameter) -> float
    """ Get: StartDosePercentage(self: OptimizationNormalTissueParameter) -> float """



class OptimizationPointCloudParameter(OptimizationParameter, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: OptimizationPointCloudParameter, writer: XmlWriter)
        """ WriteXml(self: OptimizationPointCloudParameter, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    PointResolutionInMM = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizationPointCloudParameter) -> float
    """ Get: PointResolutionInMM(self: OptimizationPointCloudParameter) -> float """

    Structure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizationPointCloudParameter) -> Structure
    """ Get: Structure(self: OptimizationPointCloudParameter) -> Structure """



class OptimizationPointObjective(OptimizationObjective, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: OptimizationPointObjective, writer: XmlWriter)
        """ WriteXml(self: OptimizationPointObjective, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Dose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizationPointObjective) -> DoseValue
    """ Get: Dose(self: OptimizationPointObjective) -> DoseValue """

    Volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizationPointObjective) -> float
    """ Get: Volume(self: OptimizationPointObjective) -> float """



class OptimizationSetup(SerializableObject, IXmlSerializable):
    # no doc
    def AddAutomaticNormalTissueObjective(self, priority):
        # type: (self: OptimizationSetup, priority: float) -> OptimizationNormalTissueParameter
        """ AddAutomaticNormalTissueObjective(self: OptimizationSetup, priority: float) -> OptimizationNormalTissueParameter """
        pass

    def AddBeamSpecificParameter(self, beam, smoothX, smoothY, fixedJaws):
        # type: (self: OptimizationSetup, beam: Beam, smoothX: float, smoothY: float, fixedJaws: bool) -> OptimizationIMRTBeamParameter
        """ AddBeamSpecificParameter(self: OptimizationSetup, beam: Beam, smoothX: float, smoothY: float, fixedJaws: bool) -> OptimizationIMRTBeamParameter """
        pass

    def AddEUDObjective(self, structure, objectiveOperator, dose, parameterA, priority):
        # type: (self: OptimizationSetup, structure: Structure, objectiveOperator: OptimizationObjectiveOperator, dose: DoseValue, parameterA: float, priority: float) -> OptimizationEUDObjective
        """ AddEUDObjective(self: OptimizationSetup, structure: Structure, objectiveOperator: OptimizationObjectiveOperator, dose: DoseValue, parameterA: float, priority: float) -> OptimizationEUDObjective """
        pass

    def AddMeanDoseObjective(self, structure, dose, priority):
        # type: (self: OptimizationSetup, structure: Structure, dose: DoseValue, priority: float) -> OptimizationMeanDoseObjective
        """ AddMeanDoseObjective(self: OptimizationSetup, structure: Structure, dose: DoseValue, priority: float) -> OptimizationMeanDoseObjective """
        pass

    def AddNormalTissueObjective(self, priority, distanceFromTargetBorderInMM, startDosePercentage, endDosePercentage, fallOff):
        # type: (self: OptimizationSetup, priority: float, distanceFromTargetBorderInMM: float, startDosePercentage: float, endDosePercentage: float, fallOff: float) -> OptimizationNormalTissueParameter
        """ AddNormalTissueObjective(self: OptimizationSetup, priority: float, distanceFromTargetBorderInMM: float, startDosePercentage: float, endDosePercentage: float, fallOff: float) -> OptimizationNormalTissueParameter """
        pass

    def AddPointObjective(self, structure, objectiveOperator, dose, volume, priority):
        # type: (self: OptimizationSetup, structure: Structure, objectiveOperator: OptimizationObjectiveOperator, dose: DoseValue, volume: float, priority: float) -> OptimizationPointObjective
        """ AddPointObjective(self: OptimizationSetup, structure: Structure, objectiveOperator: OptimizationObjectiveOperator, dose: DoseValue, volume: float, priority: float) -> OptimizationPointObjective """
        pass

    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def RemoveObjective(self, objective):
        # type: (self: OptimizationSetup, objective: OptimizationObjective)
        """ RemoveObjective(self: OptimizationSetup, objective: OptimizationObjective) """
        pass

    def RemoveParameter(self, parameter):
        # type: (self: OptimizationSetup, parameter: OptimizationParameter)
        """ RemoveParameter(self: OptimizationSetup, parameter: OptimizationParameter) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: OptimizationSetup, writer: XmlWriter)
        """ WriteXml(self: OptimizationSetup, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Objectives = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizationSetup) -> IEnumerable[OptimizationObjective]
    """ Get: Objectives(self: OptimizationSetup) -> IEnumerable[OptimizationObjective] """

    Parameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizationSetup) -> IEnumerable[OptimizationParameter]
    """ Get: Parameters(self: OptimizationSetup) -> IEnumerable[OptimizationParameter] """

    UseJawTracking = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizationSetup) -> bool
    """
    Get: UseJawTracking(self: OptimizationSetup) -> bool
    
    Set: UseJawTracking(self: OptimizationSetup) = value
    """



class OptimizerDVH(object):
    # no doc
    CurveData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizerDVH) -> Array[DVHPoint]
    """ Get: CurveData(self: OptimizerDVH) -> Array[DVHPoint] """

    Structure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizerDVH) -> Structure
    """ Get: Structure(self: OptimizerDVH) -> Structure """



class OptimizerObjectiveValue(object):
    # no doc
    Structure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizerObjectiveValue) -> Structure
    """ Get: Structure(self: OptimizerObjectiveValue) -> Structure """

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizerObjectiveValue) -> float
    """ Get: Value(self: OptimizerObjectiveValue) -> float """



class OptimizerResult(CalculationResult):
    # no doc
    NumberOfIMRTOptimizerIterations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizerResult) -> int
    """ Get: NumberOfIMRTOptimizerIterations(self: OptimizerResult) -> int """

    StructureDVHs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizerResult) -> IEnumerable[OptimizerDVH]
    """ Get: StructureDVHs(self: OptimizerResult) -> IEnumerable[OptimizerDVH] """

    StructureObjectiveValues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizerResult) -> IEnumerable[OptimizerObjectiveValue]
    """ Get: StructureObjectiveValues(self: OptimizerResult) -> IEnumerable[OptimizerObjectiveValue] """

    TotalObjectiveFunctionValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: OptimizerResult) -> float
    """ Get: TotalObjectiveFunctionValue(self: OptimizerResult) -> float """



class Patient(ApiDataObject, IXmlSerializable):
    # no doc
    def AddCourse(self):
        # type: (self: Patient) -> Course
        """ AddCourse(self: Patient) -> Course """
        pass

    def AddEmptyPhantom(self, imageId, orientation, xSizePixel, ySizePixel, widthMM, heightMM, nrOfPlanes, planeSepMM):
        # type: (self: Patient, imageId: str, orientation: PatientOrientation, xSizePixel: int, ySizePixel: int, widthMM: float, heightMM: float, nrOfPlanes: int, planeSepMM: float) -> StructureSet
        """ AddEmptyPhantom(self: Patient, imageId: str, orientation: PatientOrientation, xSizePixel: int, ySizePixel: int, widthMM: float, heightMM: float, nrOfPlanes: int, planeSepMM: float) -> StructureSet """
        pass

    def BeginModifications(self):
        # type: (self: Patient)
        """ BeginModifications(self: Patient) """
        pass

    def CanAddCourse(self):
        # type: (self: Patient) -> bool
        """ CanAddCourse(self: Patient) -> bool """
        pass

    def CanAddEmptyPhantom(self, errorMessage):
        # type: (self: Patient) -> (bool, str)
        """ CanAddEmptyPhantom(self: Patient) -> (bool, str) """
        pass

    def CanCopyImageFromOtherPatient(self, targetStudy, otherPatientId, otherPatientStudyId, otherPatient3DImageId, errorMessage):
        # type: (self: Patient, targetStudy: Study, otherPatientId: str, otherPatientStudyId: str, otherPatient3DImageId: str) -> (bool, str)
        """ CanCopyImageFromOtherPatient(self: Patient, targetStudy: Study, otherPatientId: str, otherPatientStudyId: str, otherPatient3DImageId: str) -> (bool, str) """
        pass

    def CanModifyData(self):
        # type: (self: Patient) -> bool
        """ CanModifyData(self: Patient) -> bool """
        pass

    def CanRemoveCourse(self, course):
        # type: (self: Patient, course: Course) -> bool
        """ CanRemoveCourse(self: Patient, course: Course) -> bool """
        pass

    def CanRemoveEmptyPhantom(self, structureset, errorMessage):
        # type: (self: Patient, structureset: StructureSet) -> (bool, str)
        """ CanRemoveEmptyPhantom(self: Patient, structureset: StructureSet) -> (bool, str) """
        pass

    def CopyImageFromOtherPatient(self, *__args):
        # type: (self: Patient, otherPatientId: str, otherPatientStudyId: str, otherPatient3DImageId: str) -> StructureSet
        """
        CopyImageFromOtherPatient(self: Patient, otherPatientId: str, otherPatientStudyId: str, otherPatient3DImageId: str) -> StructureSet
        CopyImageFromOtherPatient(self: Patient, targetStudy: Study, otherPatientId: str, otherPatientStudyId: str, otherPatient3DImageId: str) -> StructureSet
        """
        pass

    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def RemoveCourse(self, course):
        # type: (self: Patient, course: Course)
        """ RemoveCourse(self: Patient, course: Course) """
        pass

    def RemoveEmptyPhantom(self, structureset):
        # type: (self: Patient, structureset: StructureSet)
        """ RemoveEmptyPhantom(self: Patient, structureset: StructureSet) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: Patient, writer: XmlWriter)
        """ WriteXml(self: Patient, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Courses = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Patient) -> IEnumerable[Course]
    """ Get: Courses(self: Patient) -> IEnumerable[Course] """

    CreationDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Patient) -> Nullable[DateTime]
    """ Get: CreationDateTime(self: Patient) -> Nullable[DateTime] """

    DateOfBirth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Patient) -> Nullable[DateTime]
    """ Get: DateOfBirth(self: Patient) -> Nullable[DateTime] """

    FirstName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Patient) -> str
    """ Get: FirstName(self: Patient) -> str """

    HasModifiedData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Patient) -> bool
    """ Get: HasModifiedData(self: Patient) -> bool """

    Hospital = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Patient) -> Hospital
    """ Get: Hospital(self: Patient) -> Hospital """

    Id2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Patient) -> str
    """ Get: Id2(self: Patient) -> str """

    LastName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Patient) -> str
    """ Get: LastName(self: Patient) -> str """

    MiddleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Patient) -> str
    """ Get: MiddleName(self: Patient) -> str """

    PrimaryOncologistId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Patient) -> str
    """ Get: PrimaryOncologistId(self: Patient) -> str """

    Registrations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Patient) -> IEnumerable[Registration]
    """ Get: Registrations(self: Patient) -> IEnumerable[Registration] """

    Sex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Patient) -> str
    """ Get: Sex(self: Patient) -> str """

    SSN = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Patient) -> str
    """ Get: SSN(self: Patient) -> str """

    StructureSets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Patient) -> IEnumerable[StructureSet]
    """ Get: StructureSets(self: Patient) -> IEnumerable[StructureSet] """

    Studies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Patient) -> IEnumerable[Study]
    """ Get: Studies(self: Patient) -> IEnumerable[Study] """



class PatientSummary(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: PatientSummary, writer: XmlWriter)
        """ WriteXml(self: PatientSummary, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    CreationDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PatientSummary) -> Nullable[DateTime]
    """ Get: CreationDateTime(self: PatientSummary) -> Nullable[DateTime] """

    DateOfBirth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PatientSummary) -> Nullable[DateTime]
    """ Get: DateOfBirth(self: PatientSummary) -> Nullable[DateTime] """

    FirstName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PatientSummary) -> str
    """ Get: FirstName(self: PatientSummary) -> str """

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PatientSummary) -> str
    """ Get: Id(self: PatientSummary) -> str """

    Id2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PatientSummary) -> str
    """ Get: Id2(self: PatientSummary) -> str """

    LastName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PatientSummary) -> str
    """ Get: LastName(self: PatientSummary) -> str """

    MiddleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PatientSummary) -> str
    """ Get: MiddleName(self: PatientSummary) -> str """

    Sex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PatientSummary) -> str
    """ Get: Sex(self: PatientSummary) -> str """

    SSN = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PatientSummary) -> str
    """ Get: SSN(self: PatientSummary) -> str """



class PlanningItemDose(Dose, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: PlanningItemDose, writer: XmlWriter)
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
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetPlanSumOperation(self, planSetupInPlanSum):
        # type: (self: PlanSum, planSetupInPlanSum: PlanSetup) -> PlanSumOperation
        """ GetPlanSumOperation(self: PlanSum, planSetupInPlanSum: PlanSetup) -> PlanSumOperation """
        pass

    def GetPlanWeight(self, planSetupInPlanSum):
        # type: (self: PlanSum, planSetupInPlanSum: PlanSetup) -> float
        """ GetPlanWeight(self: PlanSum, planSetupInPlanSum: PlanSetup) -> float """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: PlanSum, writer: XmlWriter)
        """ WriteXml(self: PlanSum, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Course = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSum) -> Course
    """ Get: Course(self: PlanSum) -> Course """

    PlanSetups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSum) -> IEnumerable[PlanSetup]
    """ Get: PlanSetups(self: PlanSum) -> IEnumerable[PlanSetup] """

    PlanSumComponents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSum) -> IEnumerable[PlanSumComponent]
    """ Get: PlanSumComponents(self: PlanSum) -> IEnumerable[PlanSumComponent] """



class PlanSumComponent(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: PlanSumComponent, writer: XmlWriter)
        """ WriteXml(self: PlanSumComponent, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    PlanSetupId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSumComponent) -> str
    """ Get: PlanSetupId(self: PlanSumComponent) -> str """

    PlanSumOperation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSumComponent) -> PlanSumOperation
    """ Get: PlanSumOperation(self: PlanSumComponent) -> PlanSumOperation """

    PlanWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanSumComponent) -> float
    """ Get: PlanWeight(self: PlanSumComponent) -> float """



class PlanTreatmentSession(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: PlanTreatmentSession, writer: XmlWriter)
        """ WriteXml(self: PlanTreatmentSession, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    PlanSetup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanTreatmentSession) -> PlanSetup
    """ Get: PlanSetup(self: PlanTreatmentSession) -> PlanSetup """

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanTreatmentSession) -> TreatmentSessionStatus
    """ Get: Status(self: PlanTreatmentSession) -> TreatmentSessionStatus """

    TreatmentSession = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanTreatmentSession) -> TreatmentSession
    """ Get: TreatmentSession(self: PlanTreatmentSession) -> TreatmentSession """



class PlanUncertainty(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetDVHCumulativeData(self, structure, dosePresentation, volumePresentation, binWidth):
        # type: (self: PlanUncertainty, structure: Structure, dosePresentation: DoseValuePresentation, volumePresentation: VolumePresentation, binWidth: float) -> DVHData
        """ GetDVHCumulativeData(self: PlanUncertainty, structure: Structure, dosePresentation: DoseValuePresentation, volumePresentation: VolumePresentation, binWidth: float) -> DVHData """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: PlanUncertainty, writer: XmlWriter)
        """ WriteXml(self: PlanUncertainty, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BeamUncertainties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanUncertainty) -> IEnumerable[BeamUncertainty]
    """ Get: BeamUncertainties(self: PlanUncertainty) -> IEnumerable[BeamUncertainty] """

    CalibrationCurveError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanUncertainty) -> float
    """ Get: CalibrationCurveError(self: PlanUncertainty) -> float """

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanUncertainty) -> str
    """ Get: DisplayName(self: PlanUncertainty) -> str """

    Dose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanUncertainty) -> Dose
    """ Get: Dose(self: PlanUncertainty) -> Dose """

    IsocenterShift = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanUncertainty) -> VVector
    """ Get: IsocenterShift(self: PlanUncertainty) -> VVector """

    UncertaintyType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: PlanUncertainty) -> PlanUncertaintyType
    """ Get: UncertaintyType(self: PlanUncertainty) -> PlanUncertaintyType """



class ProtocolPhaseMeasure(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: ProtocolPhaseMeasure, writer: XmlWriter)
        """ WriteXml(self: ProtocolPhaseMeasure, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ActualValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ProtocolPhaseMeasure) -> float
    """ Get: ActualValue(self: ProtocolPhaseMeasure) -> float """

    Modifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ProtocolPhaseMeasure) -> MeasureModifier
    """ Get: Modifier(self: ProtocolPhaseMeasure) -> MeasureModifier """

    StructureId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ProtocolPhaseMeasure) -> str
    """ Get: StructureId(self: ProtocolPhaseMeasure) -> str """

    TargetIsMet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ProtocolPhaseMeasure) -> Nullable[bool]
    """ Get: TargetIsMet(self: ProtocolPhaseMeasure) -> Nullable[bool] """

    TargetValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ProtocolPhaseMeasure) -> float
    """ Get: TargetValue(self: ProtocolPhaseMeasure) -> float """

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ProtocolPhaseMeasure) -> MeasureType
    """ Get: Type(self: ProtocolPhaseMeasure) -> MeasureType """

    TypeText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ProtocolPhaseMeasure) -> str
    """ Get: TypeText(self: ProtocolPhaseMeasure) -> str """



class ProtocolPhasePrescription(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: ProtocolPhasePrescription, writer: XmlWriter)
        """ WriteXml(self: ProtocolPhasePrescription, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ActualTotalDose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ProtocolPhasePrescription) -> DoseValue
    """ Get: ActualTotalDose(self: ProtocolPhasePrescription) -> DoseValue """

    PrescModifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ProtocolPhasePrescription) -> PrescriptionModifier
    """ Get: PrescModifier(self: ProtocolPhasePrescription) -> PrescriptionModifier """

    PrescParameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ProtocolPhasePrescription) -> float
    """ Get: PrescParameter(self: ProtocolPhasePrescription) -> float """

    PrescType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ProtocolPhasePrescription) -> PrescriptionType
    """ Get: PrescType(self: ProtocolPhasePrescription) -> PrescriptionType """

    StructureId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ProtocolPhasePrescription) -> str
    """ Get: StructureId(self: ProtocolPhasePrescription) -> str """

    TargetFractionDose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ProtocolPhasePrescription) -> DoseValue
    """ Get: TargetFractionDose(self: ProtocolPhasePrescription) -> DoseValue """

    TargetIsMet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ProtocolPhasePrescription) -> Nullable[bool]
    """ Get: TargetIsMet(self: ProtocolPhasePrescription) -> Nullable[bool] """

    TargetTotalDose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ProtocolPhasePrescription) -> DoseValue
    """ Get: TargetTotalDose(self: ProtocolPhasePrescription) -> DoseValue """



class RadioactiveSource(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: RadioactiveSource, writer: XmlWriter)
        """ WriteXml(self: RadioactiveSource, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CalibrationDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RadioactiveSource) -> Nullable[DateTime]
    """ Get: CalibrationDate(self: RadioactiveSource) -> Nullable[DateTime] """

    NominalActivity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RadioactiveSource) -> bool
    """ Get: NominalActivity(self: RadioactiveSource) -> bool """

    RadioactiveSourceModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RadioactiveSource) -> RadioactiveSourceModel
    """ Get: RadioactiveSourceModel(self: RadioactiveSource) -> RadioactiveSourceModel """

    SerialNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RadioactiveSource) -> str
    """ Get: SerialNumber(self: RadioactiveSource) -> str """

    Strength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RadioactiveSource) -> float
    """ Get: Strength(self: RadioactiveSource) -> float """



class RadioactiveSourceModel(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: RadioactiveSourceModel, writer: XmlWriter)
        """ WriteXml(self: RadioactiveSourceModel, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ActiveSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RadioactiveSourceModel) -> VVector
    """ Get: ActiveSize(self: RadioactiveSourceModel) -> VVector """

    ActivityConversionFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RadioactiveSourceModel) -> float
    """ Get: ActivityConversionFactor(self: RadioactiveSourceModel) -> float """

    CalculationModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RadioactiveSourceModel) -> str
    """ Get: CalculationModel(self: RadioactiveSourceModel) -> str """

    DoseRateConstant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RadioactiveSourceModel) -> float
    """ Get: DoseRateConstant(self: RadioactiveSourceModel) -> float """

    HalfLife = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RadioactiveSourceModel) -> float
    """ Get: HalfLife(self: RadioactiveSourceModel) -> float """

    LiteratureReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RadioactiveSourceModel) -> str
    """ Get: LiteratureReference(self: RadioactiveSourceModel) -> str """

    Manufacturer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RadioactiveSourceModel) -> str
    """ Get: Manufacturer(self: RadioactiveSourceModel) -> str """

    SourceType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RadioactiveSourceModel) -> str
    """ Get: SourceType(self: RadioactiveSourceModel) -> str """

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RadioactiveSourceModel) -> str
    """ Get: Status(self: RadioactiveSourceModel) -> str """

    StatusDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RadioactiveSourceModel) -> Nullable[DateTime]
    """ Get: StatusDate(self: RadioactiveSourceModel) -> Nullable[DateTime] """

    StatusUserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RadioactiveSourceModel) -> str
    """ Get: StatusUserName(self: RadioactiveSourceModel) -> str """



class RangeModulator(AddOn, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: RangeModulator, writer: XmlWriter)
        """ WriteXml(self: RangeModulator, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RangeModulator) -> RangeModulatorType
    """ Get: Type(self: RangeModulator) -> RangeModulatorType """



class RangeModulatorSettings(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: RangeModulatorSettings, writer: XmlWriter)
        """ WriteXml(self: RangeModulatorSettings, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    IsocenterToRangeModulatorDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RangeModulatorSettings) -> float
    """ Get: IsocenterToRangeModulatorDistance(self: RangeModulatorSettings) -> float """

    RangeModulatorGatingStartValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RangeModulatorSettings) -> float
    """ Get: RangeModulatorGatingStartValue(self: RangeModulatorSettings) -> float """

    RangeModulatorGatingStarWaterEquivalentThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RangeModulatorSettings) -> float
    """ Get: RangeModulatorGatingStarWaterEquivalentThickness(self: RangeModulatorSettings) -> float """

    RangeModulatorGatingStopValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RangeModulatorSettings) -> float
    """ Get: RangeModulatorGatingStopValue(self: RangeModulatorSettings) -> float """

    RangeModulatorGatingStopWaterEquivalentThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RangeModulatorSettings) -> float
    """ Get: RangeModulatorGatingStopWaterEquivalentThickness(self: RangeModulatorSettings) -> float """

    ReferencedRangeModulator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RangeModulatorSettings) -> RangeModulator
    """ Get: ReferencedRangeModulator(self: RangeModulatorSettings) -> RangeModulator """



class RangeShifter(AddOn, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: RangeShifter, writer: XmlWriter)
        """ WriteXml(self: RangeShifter, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RangeShifter) -> RangeShifterType
    """ Get: Type(self: RangeShifter) -> RangeShifterType """



class RangeShifterSettings(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: RangeShifterSettings, writer: XmlWriter)
        """ WriteXml(self: RangeShifterSettings, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    IsocenterToRangeShifterDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RangeShifterSettings) -> float
    """ Get: IsocenterToRangeShifterDistance(self: RangeShifterSettings) -> float """

    RangeShifterSetting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RangeShifterSettings) -> str
    """ Get: RangeShifterSetting(self: RangeShifterSettings) -> str """

    RangeShifterWaterEquivalentThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RangeShifterSettings) -> float
    """ Get: RangeShifterWaterEquivalentThickness(self: RangeShifterSettings) -> float """

    ReferencedRangeShifter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RangeShifterSettings) -> RangeShifter
    """ Get: ReferencedRangeShifter(self: RangeShifterSettings) -> RangeShifter """



class ReferencePoint(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetReferencePointLocation(self, planSetup):
        # type: (self: ReferencePoint, planSetup: PlanSetup) -> VVector
        """ GetReferencePointLocation(self: ReferencePoint, planSetup: PlanSetup) -> VVector """
        pass

    def HasLocation(self, planSetup):
        # type: (self: ReferencePoint, planSetup: PlanSetup) -> bool
        """ HasLocation(self: ReferencePoint, planSetup: PlanSetup) -> bool """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: ReferencePoint, writer: XmlWriter)
        """ WriteXml(self: ReferencePoint, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DailyDoseLimit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ReferencePoint) -> DoseValue
    """
    Get: DailyDoseLimit(self: ReferencePoint) -> DoseValue
    
    Set: DailyDoseLimit(self: ReferencePoint) = value
    """

    PatientVolumeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ReferencePoint) -> str
    """ Get: PatientVolumeId(self: ReferencePoint) -> str """

    SessionDoseLimit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ReferencePoint) -> DoseValue
    """
    Get: SessionDoseLimit(self: ReferencePoint) -> DoseValue
    
    Set: SessionDoseLimit(self: ReferencePoint) = value
    """

    TotalDoseLimit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ReferencePoint) -> DoseValue
    """
    Get: TotalDoseLimit(self: ReferencePoint) -> DoseValue
    
    Set: TotalDoseLimit(self: ReferencePoint) = value
    """



class Registration(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def InverseTransformPoint(self, pt):
        # type: (self: Registration, pt: VVector) -> VVector
        """ InverseTransformPoint(self: Registration, pt: VVector) -> VVector """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def TransformPoint(self, pt):
        # type: (self: Registration, pt: VVector) -> VVector
        """ TransformPoint(self: Registration, pt: VVector) -> VVector """
        pass

    def WriteXml(self, writer):
        # type: (self: Registration, writer: XmlWriter)
        """ WriteXml(self: Registration, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CreationDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Registration) -> Nullable[DateTime]
    """ Get: CreationDateTime(self: Registration) -> Nullable[DateTime] """

    RegisteredFOR = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Registration) -> str
    """ Get: RegisteredFOR(self: Registration) -> str """

    SourceFOR = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Registration) -> str
    """ Get: SourceFOR(self: Registration) -> str """

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Registration) -> RegistrationApprovalStatus
    """ Get: Status(self: Registration) -> RegistrationApprovalStatus """

    StatusDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Registration) -> Nullable[DateTime]
    """ Get: StatusDateTime(self: Registration) -> Nullable[DateTime] """

    StatusUserDisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Registration) -> str
    """ Get: StatusUserDisplayName(self: Registration) -> str """

    StatusUserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Registration) -> str
    """ Get: StatusUserName(self: Registration) -> str """

    TransformationMatrix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Registration) -> Array[float]
    """ Get: TransformationMatrix(self: Registration) -> Array[float] """

    UID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Registration) -> str
    """ Get: UID(self: Registration) -> str """



class RTPrescription(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: RTPrescription, writer: XmlWriter)
        """ WriteXml(self: RTPrescription, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BolusFrequency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RTPrescription) -> str
    """ Get: BolusFrequency(self: RTPrescription) -> str """

    BolusThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RTPrescription) -> str
    """ Get: BolusThickness(self: RTPrescription) -> str """

    Energies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RTPrescription) -> IEnumerable[str]
    """ Get: Energies(self: RTPrescription) -> IEnumerable[str] """

    EnergyModes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RTPrescription) -> IEnumerable[str]
    """ Get: EnergyModes(self: RTPrescription) -> IEnumerable[str] """

    Gating = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RTPrescription) -> str
    """ Get: Gating(self: RTPrescription) -> str """

    LatestRevision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RTPrescription) -> RTPrescription
    """ Get: LatestRevision(self: RTPrescription) -> RTPrescription """

    Notes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RTPrescription) -> str
    """ Get: Notes(self: RTPrescription) -> str """

    NumberOfFractions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RTPrescription) -> Nullable[int]
    """ Get: NumberOfFractions(self: RTPrescription) -> Nullable[int] """

    OrgansAtRisk = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RTPrescription) -> IEnumerable[RTPrescriptionOrganAtRisk]
    """ Get: OrgansAtRisk(self: RTPrescription) -> IEnumerable[RTPrescriptionOrganAtRisk] """

    PhaseType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RTPrescription) -> str
    """ Get: PhaseType(self: RTPrescription) -> str """

    PredecessorPrescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RTPrescription) -> RTPrescription
    """ Get: PredecessorPrescription(self: RTPrescription) -> RTPrescription """

    RevisionNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RTPrescription) -> int
    """ Get: RevisionNumber(self: RTPrescription) -> int """

    SimulationNeeded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RTPrescription) -> Nullable[bool]
    """ Get: SimulationNeeded(self: RTPrescription) -> Nullable[bool] """

    Site = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RTPrescription) -> str
    """ Get: Site(self: RTPrescription) -> str """

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RTPrescription) -> str
    """ Get: Status(self: RTPrescription) -> str """

    TargetConstraintsWithoutTargetLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RTPrescription) -> IEnumerable[RTPrescriptionTargetConstraints]
    """ Get: TargetConstraintsWithoutTargetLevel(self: RTPrescription) -> IEnumerable[RTPrescriptionTargetConstraints] """

    Targets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RTPrescription) -> IEnumerable[RTPrescriptionTarget]
    """ Get: Targets(self: RTPrescription) -> IEnumerable[RTPrescriptionTarget] """

    Technique = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RTPrescription) -> str
    """ Get: Technique(self: RTPrescription) -> str """



class RTPrescriptionConstraint(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: RTPrescriptionConstraint, writer: XmlWriter)
        """ WriteXml(self: RTPrescriptionConstraint, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ConstraintType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RTPrescriptionConstraint) -> RTPrescriptionConstraintType
    """ Get: ConstraintType(self: RTPrescriptionConstraint) -> RTPrescriptionConstraintType """

    Unit1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RTPrescriptionConstraint) -> str
    """ Get: Unit1(self: RTPrescriptionConstraint) -> str """

    Unit2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RTPrescriptionConstraint) -> str
    """ Get: Unit2(self: RTPrescriptionConstraint) -> str """

    Value1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RTPrescriptionConstraint) -> str
    """ Get: Value1(self: RTPrescriptionConstraint) -> str """

    Value2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RTPrescriptionConstraint) -> str
    """ Get: Value2(self: RTPrescriptionConstraint) -> str """



class RTPrescriptionOrganAtRisk(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: RTPrescriptionOrganAtRisk, writer: XmlWriter)
        """ WriteXml(self: RTPrescriptionOrganAtRisk, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Constraints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RTPrescriptionOrganAtRisk) -> IEnumerable[RTPrescriptionConstraint]
    """ Get: Constraints(self: RTPrescriptionOrganAtRisk) -> IEnumerable[RTPrescriptionConstraint] """

    OrganAtRiskId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RTPrescriptionOrganAtRisk) -> str
    """ Get: OrganAtRiskId(self: RTPrescriptionOrganAtRisk) -> str """



class RTPrescriptionTarget(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: RTPrescriptionTarget, writer: XmlWriter)
        """ WriteXml(self: RTPrescriptionTarget, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Constraints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RTPrescriptionTarget) -> IEnumerable[RTPrescriptionConstraint]
    """ Get: Constraints(self: RTPrescriptionTarget) -> IEnumerable[RTPrescriptionConstraint] """

    DosePerFraction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RTPrescriptionTarget) -> DoseValue
    """ Get: DosePerFraction(self: RTPrescriptionTarget) -> DoseValue """

    NumberOfFractions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RTPrescriptionTarget) -> int
    """ Get: NumberOfFractions(self: RTPrescriptionTarget) -> int """

    TargetId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RTPrescriptionTarget) -> str
    """ Get: TargetId(self: RTPrescriptionTarget) -> str """

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RTPrescriptionTarget) -> RTPrescriptionTargetType
    """ Get: Type(self: RTPrescriptionTarget) -> RTPrescriptionTargetType """

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RTPrescriptionTarget) -> float
    """ Get: Value(self: RTPrescriptionTarget) -> float """



class RTPrescriptionTargetConstraints(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: RTPrescriptionTargetConstraints, writer: XmlWriter)
        """ WriteXml(self: RTPrescriptionTargetConstraints, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Constraints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RTPrescriptionTargetConstraints) -> IEnumerable[RTPrescriptionConstraint]
    """ Get: Constraints(self: RTPrescriptionTargetConstraints) -> IEnumerable[RTPrescriptionConstraint] """

    TargetId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: RTPrescriptionTargetConstraints) -> str
    """ Get: TargetId(self: RTPrescriptionTargetConstraints) -> str """



class ScriptContext(object):
    # type: (context: object, user: object, appName: str)
    """ ScriptContext(context: object, user: object, appName: str) """
    @staticmethod # known case of __new__
    def __new__(self, context, user, appName):
        """ __new__(cls: type, context: object, user: object, appName: str) """
        pass

    ApplicationName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ScriptContext) -> str
    """ Get: ApplicationName(self: ScriptContext) -> str """

    BrachyPlanSetup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ScriptContext) -> BrachyPlanSetup
    """ Get: BrachyPlanSetup(self: ScriptContext) -> BrachyPlanSetup """

    BrachyPlansInScope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ScriptContext) -> IEnumerable[BrachyPlanSetup]
    """ Get: BrachyPlansInScope(self: ScriptContext) -> IEnumerable[BrachyPlanSetup] """

    Course = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ScriptContext) -> Course
    """ Get: Course(self: ScriptContext) -> Course """

    CurrentUser = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ScriptContext) -> User
    """ Get: CurrentUser(self: ScriptContext) -> User """

    ExternalPlanSetup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ScriptContext) -> ExternalPlanSetup
    """ Get: ExternalPlanSetup(self: ScriptContext) -> ExternalPlanSetup """

    ExternalPlansInScope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ScriptContext) -> IEnumerable[ExternalPlanSetup]
    """ Get: ExternalPlansInScope(self: ScriptContext) -> IEnumerable[ExternalPlanSetup] """

    Image = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ScriptContext) -> Image
    """ Get: Image(self: ScriptContext) -> Image """

    IonPlanSetup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ScriptContext) -> IonPlanSetup
    """ Get: IonPlanSetup(self: ScriptContext) -> IonPlanSetup """

    IonPlansInScope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ScriptContext) -> IEnumerable[IonPlanSetup]
    """ Get: IonPlansInScope(self: ScriptContext) -> IEnumerable[IonPlanSetup] """

    Patient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ScriptContext) -> Patient
    """ Get: Patient(self: ScriptContext) -> Patient """

    PlanSetup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ScriptContext) -> PlanSetup
    """ Get: PlanSetup(self: ScriptContext) -> PlanSetup """

    PlansInScope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ScriptContext) -> IEnumerable[PlanSetup]
    """ Get: PlansInScope(self: ScriptContext) -> IEnumerable[PlanSetup] """

    PlanSumsInScope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ScriptContext) -> IEnumerable[PlanSum]
    """ Get: PlanSumsInScope(self: ScriptContext) -> IEnumerable[PlanSum] """

    StructureSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ScriptContext) -> StructureSet
    """ Get: StructureSet(self: ScriptContext) -> StructureSet """

    VersionInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ScriptContext) -> str
    """ Get: VersionInfo(self: ScriptContext) -> str """



class ScriptEnvironment(object):
    # type: (appName: str, scripts: IEnumerable[IApplicationScript], scriptExecutionEngine: Action[Assembly, object, Window, object])
    """ ScriptEnvironment(appName: str, scripts: IEnumerable[IApplicationScript], scriptExecutionEngine: Action[Assembly, object, Window, object]) """
    def ExecuteScript(self, scriptAssembly, scriptContext, window):
        # type: (self: ScriptEnvironment, scriptAssembly: Assembly, scriptContext: ScriptContext, window: Window)
        """ ExecuteScript(self: ScriptEnvironment, scriptAssembly: Assembly, scriptContext: ScriptContext, window: Window) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, appName, scripts, scriptExecutionEngine):
        """ __new__(cls: type, appName: str, scripts: IEnumerable[IApplicationScript], scriptExecutionEngine: Action[Assembly, object, Window, object]) """
        pass

    ApiVersionInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ScriptEnvironment) -> str
    """ Get: ApiVersionInfo(self: ScriptEnvironment) -> str """

    ApplicationName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ScriptEnvironment) -> str
    """ Get: ApplicationName(self: ScriptEnvironment) -> str """

    Scripts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ScriptEnvironment) -> IEnumerable[ApplicationScript]
    """ Get: Scripts(self: ScriptEnvironment) -> IEnumerable[ApplicationScript] """

    VersionInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: ScriptEnvironment) -> str
    """ Get: VersionInfo(self: ScriptEnvironment) -> str """



class SearchBodyParameters(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def LoadDefaults(self):
        # type: (self: SearchBodyParameters)
        """ LoadDefaults(self: SearchBodyParameters) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: SearchBodyParameters, writer: XmlWriter)
        """ WriteXml(self: SearchBodyParameters, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    FillAllCavities = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: SearchBodyParameters) -> bool
    """
    Get: FillAllCavities(self: SearchBodyParameters) -> bool
    
    Set: FillAllCavities(self: SearchBodyParameters) = value
    """

    KeepLargestParts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: SearchBodyParameters) -> bool
    """
    Get: KeepLargestParts(self: SearchBodyParameters) -> bool
    
    Set: KeepLargestParts(self: SearchBodyParameters) = value
    """

    LowerHUThreshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: SearchBodyParameters) -> int
    """
    Get: LowerHUThreshold(self: SearchBodyParameters) -> int
    
    Set: LowerHUThreshold(self: SearchBodyParameters) = value
    """

    MREdgeThresholdHigh = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: SearchBodyParameters) -> int
    """
    Get: MREdgeThresholdHigh(self: SearchBodyParameters) -> int
    
    Set: MREdgeThresholdHigh(self: SearchBodyParameters) = value
    """

    MREdgeThresholdLow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: SearchBodyParameters) -> int
    """
    Get: MREdgeThresholdLow(self: SearchBodyParameters) -> int
    
    Set: MREdgeThresholdLow(self: SearchBodyParameters) = value
    """

    NumberOfLargestPartsToKeep = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: SearchBodyParameters) -> int
    """
    Get: NumberOfLargestPartsToKeep(self: SearchBodyParameters) -> int
    
    Set: NumberOfLargestPartsToKeep(self: SearchBodyParameters) = value
    """

    PreCloseOpenings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: SearchBodyParameters) -> bool
    """
    Get: PreCloseOpenings(self: SearchBodyParameters) -> bool
    
    Set: PreCloseOpenings(self: SearchBodyParameters) = value
    """

    PreCloseOpeningsRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: SearchBodyParameters) -> float
    """
    Get: PreCloseOpeningsRadius(self: SearchBodyParameters) -> float
    
    Set: PreCloseOpeningsRadius(self: SearchBodyParameters) = value
    """

    PreDisconnect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: SearchBodyParameters) -> bool
    """
    Get: PreDisconnect(self: SearchBodyParameters) -> bool
    
    Set: PreDisconnect(self: SearchBodyParameters) = value
    """

    PreDisconnectRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: SearchBodyParameters) -> float
    """
    Get: PreDisconnectRadius(self: SearchBodyParameters) -> float
    
    Set: PreDisconnectRadius(self: SearchBodyParameters) = value
    """

    Smoothing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: SearchBodyParameters) -> bool
    """
    Get: Smoothing(self: SearchBodyParameters) -> bool
    
    Set: Smoothing(self: SearchBodyParameters) = value
    """

    SmoothingLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: SearchBodyParameters) -> int
    """
    Get: SmoothingLevel(self: SearchBodyParameters) -> int
    
    Set: SmoothingLevel(self: SearchBodyParameters) = value
    """



class SeedCollection(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: SeedCollection, writer: XmlWriter)
        """ WriteXml(self: SeedCollection, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BrachyFieldReferencePoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: SeedCollection) -> IEnumerable[BrachyFieldReferencePoint]
    """ Get: BrachyFieldReferencePoints(self: SeedCollection) -> IEnumerable[BrachyFieldReferencePoint] """

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: SeedCollection) -> Color
    """ Get: Color(self: SeedCollection) -> Color """

    SourcePositions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: SeedCollection) -> IEnumerable[SourcePosition]
    """ Get: SourcePositions(self: SeedCollection) -> IEnumerable[SourcePosition] """



class SegmentVolume(SerializableObject, IXmlSerializable):
    # no doc
    def And(self, other):
        # type: (self: SegmentVolume, other: SegmentVolume) -> SegmentVolume
        """ And(self: SegmentVolume, other: SegmentVolume) -> SegmentVolume """
        pass

    def AsymmetricMargin(self, margins):
        # type: (self: SegmentVolume, margins: AxisAlignedMargins) -> SegmentVolume
        """ AsymmetricMargin(self: SegmentVolume, margins: AxisAlignedMargins) -> SegmentVolume """
        pass

    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def Margin(self, marginInMM):
        # type: (self: SegmentVolume, marginInMM: float) -> SegmentVolume
        """ Margin(self: SegmentVolume, marginInMM: float) -> SegmentVolume """
        pass

    def Not(self):
        # type: (self: SegmentVolume) -> SegmentVolume
        """ Not(self: SegmentVolume) -> SegmentVolume """
        pass

    def Or(self, other):
        # type: (self: SegmentVolume, other: SegmentVolume) -> SegmentVolume
        """ Or(self: SegmentVolume, other: SegmentVolume) -> SegmentVolume """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def Sub(self, other):
        # type: (self: SegmentVolume, other: SegmentVolume) -> SegmentVolume
        """ Sub(self: SegmentVolume, other: SegmentVolume) -> SegmentVolume """
        pass

    def WriteXml(self, writer):
        # type: (self: SegmentVolume, writer: XmlWriter)
        """ WriteXml(self: SegmentVolume, writer: XmlWriter) """
        pass

    def Xor(self, other):
        # type: (self: SegmentVolume, other: SegmentVolume) -> SegmentVolume
        """ Xor(self: SegmentVolume, other: SegmentVolume) -> SegmentVolume """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class Series(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def SetImagingDevice(self, imagingDeviceId):
        # type: (self: Series, imagingDeviceId: str)
        """ SetImagingDevice(self: Series, imagingDeviceId: str) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: Series, writer: XmlWriter)
        """ WriteXml(self: Series, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    FOR = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Series) -> str
    """ Get: FOR(self: Series) -> str """

    Images = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Series) -> IEnumerable[Image]
    """ Get: Images(self: Series) -> IEnumerable[Image] """

    ImagingDeviceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Series) -> str
    """ Get: ImagingDeviceId(self: Series) -> str """

    ImagingDeviceManufacturer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Series) -> str
    """ Get: ImagingDeviceManufacturer(self: Series) -> str """

    ImagingDeviceModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Series) -> str
    """ Get: ImagingDeviceModel(self: Series) -> str """

    ImagingDeviceSerialNo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Series) -> str
    """ Get: ImagingDeviceSerialNo(self: Series) -> str """

    Modality = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Series) -> SeriesModality
    """ Get: Modality(self: Series) -> SeriesModality """

    Study = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Series) -> Study
    """ Get: Study(self: Series) -> Study """

    UID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Series) -> str
    """ Get: UID(self: Series) -> str """



class Slot(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: Slot, writer: XmlWriter)
        """ WriteXml(self: Slot, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Slot) -> int
    """ Get: Number(self: Slot) -> int """



class SourcePosition(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: SourcePosition, writer: XmlWriter)
        """ WriteXml(self: SourcePosition, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DwellTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: SourcePosition) -> float
    """ Get: DwellTime(self: SourcePosition) -> float """

    RadioactiveSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: SourcePosition) -> RadioactiveSource
    """ Get: RadioactiveSource(self: SourcePosition) -> RadioactiveSource """

    Transform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: SourcePosition) -> Array[float]
    """ Get: Transform(self: SourcePosition) -> Array[float] """

    Translation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: SourcePosition) -> VVector
    """ Get: Translation(self: SourcePosition) -> VVector """



class StandardWedge(Wedge, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: StandardWedge, writer: XmlWriter)
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
        # type: (self: Structure, contour: Array[VVector], z: int)
        """ AddContourOnImagePlane(self: Structure, contour: Array[VVector], z: int) """
        pass

    def And(self, other):
        # type: (self: Structure, other: SegmentVolume) -> SegmentVolume
        """ And(self: Structure, other: SegmentVolume) -> SegmentVolume """
        pass

    def AsymmetricMargin(self, margins):
        # type: (self: Structure, margins: AxisAlignedMargins) -> SegmentVolume
        """ AsymmetricMargin(self: Structure, margins: AxisAlignedMargins) -> SegmentVolume """
        pass

    def CanConvertToHighResolution(self):
        # type: (self: Structure) -> bool
        """ CanConvertToHighResolution(self: Structure) -> bool """
        pass

    def CanEditSegmentVolume(self, errorMessage):
        # type: (self: Structure) -> (bool, str)
        """ CanEditSegmentVolume(self: Structure) -> (bool, str) """
        pass

    def CanSetAssignedHU(self, errorMessage):
        # type: (self: Structure) -> (bool, str)
        """ CanSetAssignedHU(self: Structure) -> (bool, str) """
        pass

    def ClearAllContoursOnImagePlane(self, z):
        # type: (self: Structure, z: int)
        """ ClearAllContoursOnImagePlane(self: Structure, z: int) """
        pass

    def ConvertDoseLevelToStructure(self, dose, doseLevel):
        # type: (self: Structure, dose: Dose, doseLevel: DoseValue)
        """ ConvertDoseLevelToStructure(self: Structure, dose: Dose, doseLevel: DoseValue) """
        pass

    def ConvertToHighResolution(self):
        # type: (self: Structure)
        """ ConvertToHighResolution(self: Structure) """
        pass

    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetAssignedHU(self, huValue):
        # type: (self: Structure) -> (bool, float)
        """ GetAssignedHU(self: Structure) -> (bool, float) """
        pass

    def GetContoursOnImagePlane(self, z):
        # type: (self: Structure, z: int) -> Array[Array[VVector]]
        """ GetContoursOnImagePlane(self: Structure, z: int) -> Array[Array[VVector]] """
        pass

    def GetNumberOfSeparateParts(self):
        # type: (self: Structure) -> int
        """ GetNumberOfSeparateParts(self: Structure) -> int """
        pass

    def GetReferenceLinePoints(self):
        # type: (self: Structure) -> Array[VVector]
        """ GetReferenceLinePoints(self: Structure) -> Array[VVector] """
        pass

    def GetSegmentProfile(self, start, stop, preallocatedBuffer):
        # type: (self: Structure, start: VVector, stop: VVector, preallocatedBuffer: BitArray) -> SegmentProfile
        """ GetSegmentProfile(self: Structure, start: VVector, stop: VVector, preallocatedBuffer: BitArray) -> SegmentProfile """
        pass

    def IsPointInsideSegment(self, point):
        # type: (self: Structure, point: VVector) -> bool
        """ IsPointInsideSegment(self: Structure, point: VVector) -> bool """
        pass

    def Margin(self, marginInMM):
        # type: (self: Structure, marginInMM: float) -> SegmentVolume
        """ Margin(self: Structure, marginInMM: float) -> SegmentVolume """
        pass

    def Not(self):
        # type: (self: Structure) -> SegmentVolume
        """ Not(self: Structure) -> SegmentVolume """
        pass

    def Or(self, other):
        # type: (self: Structure, other: SegmentVolume) -> SegmentVolume
        """ Or(self: Structure, other: SegmentVolume) -> SegmentVolume """
        pass

    def ResetAssignedHU(self):
        # type: (self: Structure) -> bool
        """ ResetAssignedHU(self: Structure) -> bool """
        pass

    def SetAssignedHU(self, huValue):
        # type: (self: Structure, huValue: float)
        """ SetAssignedHU(self: Structure, huValue: float) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def Sub(self, other):
        # type: (self: Structure, other: SegmentVolume) -> SegmentVolume
        """ Sub(self: Structure, other: SegmentVolume) -> SegmentVolume """
        pass

    def SubtractContourOnImagePlane(self, contour, z):
        # type: (self: Structure, contour: Array[VVector], z: int)
        """ SubtractContourOnImagePlane(self: Structure, contour: Array[VVector], z: int) """
        pass

    def WriteXml(self, writer):
        # type: (self: Structure, writer: XmlWriter)
        """ WriteXml(self: Structure, writer: XmlWriter) """
        pass

    def Xor(self, other):
        # type: (self: Structure, other: SegmentVolume) -> SegmentVolume
        """ Xor(self: Structure, other: SegmentVolume) -> SegmentVolume """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ApprovalHistory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Structure) -> IEnumerable[StructureApprovalHistoryEntry]
    """ Get: ApprovalHistory(self: Structure) -> IEnumerable[StructureApprovalHistoryEntry] """

    CenterPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Structure) -> VVector
    """ Get: CenterPoint(self: Structure) -> VVector """

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Structure) -> Color
    """ Get: Color(self: Structure) -> Color """

    DicomType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Structure) -> str
    """ Get: DicomType(self: Structure) -> str """

    HasSegment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Structure) -> bool
    """ Get: HasSegment(self: Structure) -> bool """

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Structure) -> str
    """
    Get: Id(self: Structure) -> str
    
    Set: Id(self: Structure) = value
    """

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Structure) -> bool
    """ Get: IsEmpty(self: Structure) -> bool """

    IsHighResolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Structure) -> bool
    """ Get: IsHighResolution(self: Structure) -> bool """

    MeshGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Structure) -> MeshGeometry3D
    """ Get: MeshGeometry(self: Structure) -> MeshGeometry3D """

    ROINumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Structure) -> int
    """ Get: ROINumber(self: Structure) -> int """

    SegmentVolume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Structure) -> SegmentVolume
    """
    Get: SegmentVolume(self: Structure) -> SegmentVolume
    
    Set: SegmentVolume(self: Structure) = value
    """

    StructureCodeInfos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Structure) -> IEnumerable[StructureCodeInfo]
    """ Get: StructureCodeInfos(self: Structure) -> IEnumerable[StructureCodeInfo] """

    Volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Structure) -> float
    """ Get: Volume(self: Structure) -> float """



class StructureSet(ApiDataObject, IXmlSerializable):
    # no doc
    def AddStructure(self, dicomType, id):
        # type: (self: StructureSet, dicomType: str, id: str) -> Structure
        """ AddStructure(self: StructureSet, dicomType: str, id: str) -> Structure """
        pass

    def CanAddStructure(self, dicomType, id):
        # type: (self: StructureSet, dicomType: str, id: str) -> bool
        """ CanAddStructure(self: StructureSet, dicomType: str, id: str) -> bool """
        pass

    def CanRemoveStructure(self, structure):
        # type: (self: StructureSet, structure: Structure) -> bool
        """ CanRemoveStructure(self: StructureSet, structure: Structure) -> bool """
        pass

    def Copy(self):
        # type: (self: StructureSet) -> StructureSet
        """ Copy(self: StructureSet) -> StructureSet """
        pass

    def CreateAndSearchBody(self, parameters):
        # type: (self: StructureSet, parameters: SearchBodyParameters) -> Structure
        """ CreateAndSearchBody(self: StructureSet, parameters: SearchBodyParameters) -> Structure """
        pass

    def Delete(self):
        # type: (self: StructureSet)
        """ Delete(self: StructureSet) """
        pass

    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def GetDefaultSearchBodyParameters(self):
        # type: (self: StructureSet) -> SearchBodyParameters
        """ GetDefaultSearchBodyParameters(self: StructureSet) -> SearchBodyParameters """
        pass

    def RemoveStructure(self, structure):
        # type: (self: StructureSet, structure: Structure)
        """ RemoveStructure(self: StructureSet, structure: Structure) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: StructureSet, writer: XmlWriter)
        """ WriteXml(self: StructureSet, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ApplicationScriptLogs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: StructureSet) -> IEnumerable[ApplicationScriptLog]
    """ Get: ApplicationScriptLogs(self: StructureSet) -> IEnumerable[ApplicationScriptLog] """

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: StructureSet) -> str
    """
    Get: Id(self: StructureSet) -> str
    
    Set: Id(self: StructureSet) = value
    """

    Image = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: StructureSet) -> Image
    """ Get: Image(self: StructureSet) -> Image """

    Patient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: StructureSet) -> Patient
    """ Get: Patient(self: StructureSet) -> Patient """

    Structures = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: StructureSet) -> IEnumerable[Structure]
    """ Get: Structures(self: StructureSet) -> IEnumerable[Structure] """

    UID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: StructureSet) -> str
    """ Get: UID(self: StructureSet) -> str """



class Study(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: Study, writer: XmlWriter)
        """ WriteXml(self: Study, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CreationDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Study) -> Nullable[DateTime]
    """ Get: CreationDateTime(self: Study) -> Nullable[DateTime] """

    Series = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Study) -> IEnumerable[Series]
    """ Get: Series(self: Study) -> IEnumerable[Series] """

    UID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: Study) -> str
    """ Get: UID(self: Study) -> str """



class Technique(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: Technique, writer: XmlWriter)
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
        # type: (self: TradeoffExplorationContext, targetStructure: Structure) -> bool
        """ AddTargetHomogeneityObjective(self: TradeoffExplorationContext, targetStructure: Structure) -> bool """
        pass

    def AddTradeoffObjective(self, *__args):
        # type: (self: TradeoffExplorationContext, structure: Structure) -> bool
        """
        AddTradeoffObjective(self: TradeoffExplorationContext, structure: Structure) -> bool
        AddTradeoffObjective(self: TradeoffExplorationContext, objective: OptimizationObjective) -> bool
        """
        pass

    def ApplyTradeoffExplorationResult(self):
        # type: (self: TradeoffExplorationContext)
        """ ApplyTradeoffExplorationResult(self: TradeoffExplorationContext) """
        pass

    def CreateDeliverableVmatPlan(self, useIntermediateDose):
        # type: (self: TradeoffExplorationContext, useIntermediateDose: bool) -> bool
        """ CreateDeliverableVmatPlan(self: TradeoffExplorationContext, useIntermediateDose: bool) -> bool """
        pass

    def CreatePlanCollection(self, continueOptimization, intermediateDoseMode, useHybridOptimizationForVmat):
        # type: (self: TradeoffExplorationContext, continueOptimization: bool, intermediateDoseMode: TradeoffPlanGenerationIntermediateDoseMode, useHybridOptimizationForVmat: bool) -> bool
        """ CreatePlanCollection(self: TradeoffExplorationContext, continueOptimization: bool, intermediateDoseMode: TradeoffPlanGenerationIntermediateDoseMode, useHybridOptimizationForVmat: bool) -> bool """
        pass

    def GetObjectiveCost(self, objective):
        # type: (self: TradeoffExplorationContext, objective: TradeoffObjective) -> float
        """ GetObjectiveCost(self: TradeoffExplorationContext, objective: TradeoffObjective) -> float """
        pass

    def GetObjectiveLowerLimit(self, objective):
        # type: (self: TradeoffExplorationContext, objective: TradeoffObjective) -> float
        """ GetObjectiveLowerLimit(self: TradeoffExplorationContext, objective: TradeoffObjective) -> float """
        pass

    def GetObjectiveUpperLimit(self, objective):
        # type: (self: TradeoffExplorationContext, objective: TradeoffObjective) -> float
        """ GetObjectiveUpperLimit(self: TradeoffExplorationContext, objective: TradeoffObjective) -> float """
        pass

    def GetObjectiveUpperRestrictor(self, objective):
        # type: (self: TradeoffExplorationContext, objective: TradeoffObjective) -> float
        """ GetObjectiveUpperRestrictor(self: TradeoffExplorationContext, objective: TradeoffObjective) -> float """
        pass

    def GetStructureDvh(self, structure):
        # type: (self: TradeoffExplorationContext, structure: Structure) -> DVHData
        """ GetStructureDvh(self: TradeoffExplorationContext, structure: Structure) -> DVHData """
        pass

    def LoadSavedPlanCollection(self):
        # type: (self: TradeoffExplorationContext) -> bool
        """ LoadSavedPlanCollection(self: TradeoffExplorationContext) -> bool """
        pass

    def RemoveAllTradeoffObjectives(self):
        # type: (self: TradeoffExplorationContext)
        """ RemoveAllTradeoffObjectives(self: TradeoffExplorationContext) """
        pass

    def RemovePlanCollection(self):
        # type: (self: TradeoffExplorationContext)
        """ RemovePlanCollection(self: TradeoffExplorationContext) """
        pass

    def RemoveTargetHomogeneityObjective(self, targetStructure):
        # type: (self: TradeoffExplorationContext, targetStructure: Structure) -> bool
        """ RemoveTargetHomogeneityObjective(self: TradeoffExplorationContext, targetStructure: Structure) -> bool """
        pass

    def RemoveTradeoffObjective(self, *__args):
        # type: (self: TradeoffExplorationContext, tradeoffObjective: TradeoffObjective) -> bool
        """
        RemoveTradeoffObjective(self: TradeoffExplorationContext, tradeoffObjective: TradeoffObjective) -> bool
        RemoveTradeoffObjective(self: TradeoffExplorationContext, structure: Structure) -> bool
        """
        pass

    def ResetToBalancedPlan(self):
        # type: (self: TradeoffExplorationContext)
        """ ResetToBalancedPlan(self: TradeoffExplorationContext) """
        pass

    def SetObjectiveCost(self, tradeoffObjective, cost):
        # type: (self: TradeoffExplorationContext, tradeoffObjective: TradeoffObjective, cost: float)
        """ SetObjectiveCost(self: TradeoffExplorationContext, tradeoffObjective: TradeoffObjective, cost: float) """
        pass

    def SetObjectiveUpperRestrictor(self, tradeoffObjective, restrictorValue):
        # type: (self: TradeoffExplorationContext, tradeoffObjective: TradeoffObjective, restrictorValue: float)
        """ SetObjectiveUpperRestrictor(self: TradeoffExplorationContext, tradeoffObjective: TradeoffObjective, restrictorValue: float) """
        pass

    CanCreatePlanCollection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: TradeoffExplorationContext) -> bool
    """ Get: CanCreatePlanCollection(self: TradeoffExplorationContext) -> bool """

    CanLoadSavedPlanCollection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: TradeoffExplorationContext) -> bool
    """ Get: CanLoadSavedPlanCollection(self: TradeoffExplorationContext) -> bool """

    CanUseHybridOptimizationInPlanGeneration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: TradeoffExplorationContext) -> bool
    """ Get: CanUseHybridOptimizationInPlanGeneration(self: TradeoffExplorationContext) -> bool """

    CanUsePlanDoseAsIntermediateDose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: TradeoffExplorationContext) -> bool
    """ Get: CanUsePlanDoseAsIntermediateDose(self: TradeoffExplorationContext) -> bool """

    CurrentDose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: TradeoffExplorationContext) -> Dose
    """ Get: CurrentDose(self: TradeoffExplorationContext) -> Dose """

    HasPlanCollection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: TradeoffExplorationContext) -> bool
    """ Get: HasPlanCollection(self: TradeoffExplorationContext) -> bool """

    TargetStructures = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: TradeoffExplorationContext) -> IReadOnlyList[Structure]
    """ Get: TargetStructures(self: TradeoffExplorationContext) -> IReadOnlyList[Structure] """

    TradeoffObjectiveCandidates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: TradeoffExplorationContext) -> IReadOnlyList[OptimizationObjective]
    """ Get: TradeoffObjectiveCandidates(self: TradeoffExplorationContext) -> IReadOnlyList[OptimizationObjective] """

    TradeoffObjectives = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: TradeoffExplorationContext) -> IReadOnlyCollection[TradeoffObjective]
    """ Get: TradeoffObjectives(self: TradeoffExplorationContext) -> IReadOnlyCollection[TradeoffObjective] """

    TradeoffStructureCandidates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: TradeoffExplorationContext) -> IReadOnlyList[Structure]
    """ Get: TradeoffStructureCandidates(self: TradeoffExplorationContext) -> IReadOnlyList[Structure] """



class TradeoffObjective(object):
    # no doc
    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: TradeoffObjective) -> int
    """ Get: Id(self: TradeoffObjective) -> int """

    OptimizationObjectives = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: TradeoffObjective) -> IEnumerable[OptimizationObjective]
    """ Get: OptimizationObjectives(self: TradeoffObjective) -> IEnumerable[OptimizationObjective] """

    Structure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: TradeoffObjective) -> Structure
    """ Get: Structure(self: TradeoffObjective) -> Structure """



class TradeoffPlanGenerationIntermediateDoseMode(Enum, IComparable, IFormattable, IConvertible):
    # type: (2), NotUsed (0), UsePlanDose (1)
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
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: Tray, writer: XmlWriter)
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
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: TreatmentPhase, writer: XmlWriter)
        """ WriteXml(self: TreatmentPhase, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    OtherInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: TreatmentPhase) -> str
    """ Get: OtherInfo(self: TreatmentPhase) -> str """

    PhaseGapNumberOfDays = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: TreatmentPhase) -> int
    """ Get: PhaseGapNumberOfDays(self: TreatmentPhase) -> int """

    Prescriptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: TreatmentPhase) -> IEnumerable[RTPrescription]
    """ Get: Prescriptions(self: TreatmentPhase) -> IEnumerable[RTPrescription] """

    TimeGapType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: TreatmentPhase) -> str
    """ Get: TimeGapType(self: TreatmentPhase) -> str """



class TreatmentSession(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: TreatmentSession, writer: XmlWriter)
        """ WriteXml(self: TreatmentSession, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SessionNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: TreatmentSession) -> Int64
    """ Get: SessionNumber(self: TreatmentSession) -> Int64 """

    SessionPlans = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: TreatmentSession) -> IEnumerable[PlanTreatmentSession]
    """ Get: SessionPlans(self: TreatmentSession) -> IEnumerable[PlanTreatmentSession] """



class TreatmentUnitOperatingLimit(ApiDataObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: TreatmentUnitOperatingLimit, writer: XmlWriter)
        """ WriteXml(self: TreatmentUnitOperatingLimit, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: TreatmentUnitOperatingLimit) -> str
    """ Get: Label(self: TreatmentUnitOperatingLimit) -> str """

    MaxValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: TreatmentUnitOperatingLimit) -> float
    """ Get: MaxValue(self: TreatmentUnitOperatingLimit) -> float """

    MinValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: TreatmentUnitOperatingLimit) -> float
    """ Get: MinValue(self: TreatmentUnitOperatingLimit) -> float """

    Precision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: TreatmentUnitOperatingLimit) -> Nullable[int]
    """ Get: Precision(self: TreatmentUnitOperatingLimit) -> Nullable[int] """

    UnitString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: TreatmentUnitOperatingLimit) -> str
    """ Get: UnitString(self: TreatmentUnitOperatingLimit) -> str """



class TreatmentUnitOperatingLimits(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def WriteXml(self, writer):
        # type: (self: TreatmentUnitOperatingLimits, writer: XmlWriter)
        """ WriteXml(self: TreatmentUnitOperatingLimits, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    CollimatorAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: TreatmentUnitOperatingLimits) -> TreatmentUnitOperatingLimit
    """ Get: CollimatorAngle(self: TreatmentUnitOperatingLimits) -> TreatmentUnitOperatingLimit """

    GantryAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: TreatmentUnitOperatingLimits) -> TreatmentUnitOperatingLimit
    """ Get: GantryAngle(self: TreatmentUnitOperatingLimits) -> TreatmentUnitOperatingLimit """

    MU = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: TreatmentUnitOperatingLimits) -> TreatmentUnitOperatingLimit
    """ Get: MU(self: TreatmentUnitOperatingLimits) -> TreatmentUnitOperatingLimit """

    PatientSupportAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: TreatmentUnitOperatingLimits) -> TreatmentUnitOperatingLimit
    """ Get: PatientSupportAngle(self: TreatmentUnitOperatingLimits) -> TreatmentUnitOperatingLimit """



class TypeBasedIdValidator(object):
    # no doc
    @staticmethod
    def IsValidId(id, dataObject, errorHint):
        # type: (id: str, dataObject: ApiDataObject, errorHint: StringBuilder) -> bool
        """ IsValidId(id: str, dataObject: ApiDataObject, errorHint: StringBuilder) -> bool """
        pass

    @staticmethod
    def ThrowIfNotValidId(id, dataObject):
        # type: (id: str, dataObject: ApiDataObject)
        """ ThrowIfNotValidId(id: str, dataObject: ApiDataObject) """
        pass

    __all__ = [
        'IsValidId',
        'ThrowIfNotValidId',
    ]


class User(SerializableObject, IXmlSerializable):
    # no doc
    def EndSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject)
        """ EndSerialization(self: SerializableObject) """
        pass

    def Equals(self, obj):
        # type: (self: User, obj: object) -> bool
        """ Equals(self: User, obj: object) -> bool """
        pass

    def GetHashCode(self):
        # type: (self: User) -> int
        """ GetHashCode(self: User) -> int """
        pass

    def StartSerialization(self, *args): #cannot find CLR method
        # type: (self: SerializableObject, typeName: str, typeId: str)
        """ StartSerialization(self: SerializableObject, typeName: str, typeId: str) """
        pass

    def ToString(self):
        # type: (self: User) -> str
        """ ToString(self: User) -> str """
        pass

    def WriteXml(self, writer):
        # type: (self: User, writer: XmlWriter)
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
    # type: (self: User) -> str
    """ Get: Id(self: User) -> str """

    Language = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: User) -> str
    """ Get: Language(self: User) -> str """

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    # type: (self: User) -> str
    """ Get: Name(self: User) -> str """



