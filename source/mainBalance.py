import RPi.GPIO as GPIO
from time import sleep
from MPU6050Manager import IMUManager
from EasySMXController import Controller

p, i, d = 16.5, 0.01, 30
sp, si, sd = 0.018, 0.0000004, 0.0002

class PID():
    def __init__(self, p, i, d, target, minOut, maxOut):
        self.targetBias = 0
        self.target = target
        self.pK = p
        self.iK = i
        self.dK = d
        self.error = 0
        self.sumError = 0
        self.lastError = 0
        self.minOut = minOut
        self.maxOut = maxOut

    def update(self, now):
        self.error = (self.target + self.targetBias) - now
        self.sumError += self.error
        out = (self.error * self.pK) + (self.sumError * self.iK) + ((self.error - self.lastError) * self.dK)
        self.lastError = self.error

        out = self.minOut if out < self.minOut else out
        out = self.maxOut if out > self.maxOut else out
        return(out)

def setLeftMotor(x):
    if(x==0):
        leftBackwardPWM.stop()
        leftForwardPWM.stop()
    elif(x > 0):
        leftForwardPWM.start(min(x, 100))
        leftBackwardPWM.stop()
    elif(x < 0):
        leftBackwardPWM.start(-max(x, -100))
        leftForwardPWM.stop()

def setRightMotor(x):
    if(x==0):
        rightForwardPWM.stop()
        rightBackwardPWM.stop()
    elif(x > 0):
        rightForwardPWM.start(min(x, 100))
        rightBackwardPWM.stop()
    elif(x < 0):
        rightBackwardPWM.start(-max(x, -100))
        rightForwardPWM.stop()

leftForwardPin = 18
leftBackwardPin = 17
rightForwardPin = 23
rightBackwardPin = 22

GPIO.setmode(GPIO.BCM)

GPIO.setup(leftForwardPin, GPIO.OUT)
GPIO.setup(leftBackwardPin, GPIO.OUT)
GPIO.setup(rightForwardPin, GPIO.OUT)
GPIO.setup(rightBackwardPin, GPIO.OUT)

leftForwardPWM = GPIO.PWM(leftForwardPin, 5000)
leftBackwardPWM = GPIO.PWM(leftBackwardPin, 5000)
rightForwardPWM = GPIO.PWM(rightForwardPin, 5000)
rightBackwardPWM = GPIO.PWM(rightBackwardPin, 5000)

speedBias = 0
biasAngle = 0
targetAngle = -15.6
tagretSpeed = 0

moveDir = [0, 0]

pad = Controller('/dev/input/event0')
imu = IMUManager()
imu.accelBiasScaler = 0.05
gyroPID = PID(p, i, d, targetAngle, -100, 100)

speedPID = PID(sp, si, sd, tagretSpeed, -12, 12)

filteredAngles = imu.angles.copy()
f = 0.5
while(1):
	filteredAngles[1] = (imu.angles[1] * (1 - f)) + filteredAngles[1] * f

	speedPID.target = (pad.leftJoyY-128) * 40 / 128
	moveDir[1] = (pad.leftJoyX - 128) * 50 / 128

	gyroPID.targetBias = -speedPID.update(moveDir[0]) + speedBias
	moveDir[0] = gyroPID.update(filteredAngles[1])

	setLeftMotor(moveDir[0] + moveDir[1])
	setRightMotor(moveDir[0] - moveDir[1])
	#print(gyroPID.targetBias)
	#print(imu.angles[1], moveDir[0])
	#sleep(0.2)
