from enum import Enum, auto
from commands2 import SubsystemBase
from wpilib import PneumaticsModuleType, Solenoid
from ctre import ControlMode
from util.ctrecheck import ctreCheckError
from util.simfalcon import createMotor
import constants


import constants
from subsystems.drivesubsystem import DriveSubsystem
from util import advantagescopeconvert
from util.convenientmath import pose3dFrom2d


class IntakeSubsystem(SubsystemBase):
    class Mode(Enum):
        Deployed = auto()
        Retracted = auto()
        Reversed = auto()

    def __init__(self) -> None:
        SubsystemBase.__init__(self)
        self.setName(__class__.__name__)
        self.state = self.Mode.Retracted()    

        self.intakeSolenoid = Solenoid(
            PneumaticsModuleType.REVPH, constants.kIntakeSolenoidChannelId
        )

        self.intakeMotor = createMotor(
            constants.kIntakeMotorId,
            constants.kCANivoreName,
        )

    def periodic(self) -> None:
        if self.state == self.Mode.Deployed():
            self.intakeSolenoid.set(True)
            self.intakeMotor.set(ControlMode.Velocity, 50)
        if self.state == self.Mode.Reversed():
            self.intakeSolenoid.set(True)
            self.intakeMoter.set(ControlMode.velocity, -50)
        if self.state == self.Mode.Retracted():
            self.intakeSolenoid.set(False)
            self.intakeMotor.neutralOutput()


