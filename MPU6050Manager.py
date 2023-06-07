from mpu6050 import mpu6050
from threading import Thread
import math
import time
class IMUManager():
	def __init__(self):
		self.mpu = mpu6050(0x68)
		self.accel = {"x":0, "y":0, "z":0}
		self.gyro = {"x":0, "y":0, "z":0}
		mpuThread = Thread(target = self.readLoop, args=())
		mpuThread.start()

		self.angles = [0, 0, 0]
		self.accelBiasScaler = 0.3
		self.gyroBias = [0, -2.8091603053435112, 0]

	def readLoop(self):
		dt = 0
		while(True):
			start = time.time()
			self.accel = self.mpu.get_accel_data()
			self.gyro = self.mpu.get_gyro_data()

			self.angles[1] -= (self.gyro["y"] + self.gyroBias[1])*dt
			self.angles[1] += (math.degrees(math.atan2(self.accel["x"], self.accel["z"])) - self.angles[1])*self.accelBiasScaler
			end = time.time()
			dt = end - start


if(__name__ == "__main__"):
	import time
	imu = IMUManager()
	while(True):
		print(imu.gyro)
		print(imu.accel)
		print(imu.angles[1], "\n")
		time.sleep(0.3)
