# import the necessary packages
import math
from dynamixel import * 
from collections import deque
import numpy as np


import time
import cv2


#from core import *
import numpy as ny



trans = np.eye(4)



# define the lower and upper boundaries of the "green"
# ball in the HSV color space, then initialize the
# list of tracked points


settheta = [0,0,0,0]
settheta0 = [0,0,0,0]
focalLength = 319
KNOWN_WIDTH = 38.5
redLower = (138, 155, 125)
redUpper = (175, 255, 255)

ps = deque(maxlen=3)
savetheta = deque(maxlen=2)
savetheta1 = deque(maxlen=3)
counter = 0
clear = 0
begin = 0
stop = 0
s = -1
(dX, dY, dZ) = (0, 0, 0)
(x0,y0,z0) = (0,0,0)
(xa,ya,za) = (0,0,0)
direction = ""
#PID
setx = 320
P = 1
I = 0
D = 0
lasterrx = 0
iaccux = 0
nowerrx = 0
out = 512

dxl_goal =[512,85,695,686] 
settheta =[512,85,695,686]

# Initialize PortHandler instance
# Set the port path
# Get methods and members of PortHandlerLinux or PortHandlerWindows
portHandler = PortHandler(DEVICENAME)

# Initialize PacketHandler instance
# Set the protocol version
# Get methods and members of Protocol1PacketHandler or Protocol2PacketHandler
packetHandler = PacketHandler(PROTOCOL_VERSION)

# Open port
if portHandler.openPort():
    print("Succeeded to open the port")
else:
    print("Failed to open the port")
    print("Press any key to terminate...")
    getch()
    quit()


# Set port baudrate
if portHandler.setBaudRate(BAUDRATE):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    print("Press any key to terminate...")
    getch()
    quit()

# Enable Dynamixel Torque
for ID in range(1,5):
	dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, ID, ADDR_PRO_TORQUE_ENABLE, TORQUE_ENABLE)
	if dxl_comm_result != COMM_SUCCESS:
		print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
	elif dxl_error != 0:
		print("%s" % packetHandler.getRxPacketError(dxl_error))
	else:
		print("Dynamixel has been successfully connected")


	dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, ID, ADDR_PRO_GOAL_POSITION, dxl_goal[ID-1])
	if dxl_comm_result != COMM_SUCCESS:
		print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
	elif dxl_error != 0:
		print("%s" % packetHandler.getRxPacketError(dxl_error))

	dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, ID, ADDR_PRO_MOVE_SPEED , 180)
	if dxl_comm_result != COMM_SUCCESS:
		print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
	elif dxl_error != 0:
		print("%s" % packetHandler.getRxPacketError(dxl_error))




while True :
	out = out + 1
	settheta = [out,85,695,686]
	for ID in range(1,5):
		dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, ID, ADDR_PRO_GOAL_POSITION, settheta[ID-1])
		print(settheta[ID-1])
		if dxl_comm_result != COMM_SUCCESS:
			print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
		elif dxl_error != 0:
			print("%s" % packetHandler.getRxPacketError(dxl_error))
	time.sleep(0.05)

	#print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL_ID, dxl_goal_position, dxl_present_position))

	


	# show the frame to our screen




# Disable Dynamixel Torque
for ID in range(1,5):
	dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, ID, ADDR_PRO_TORQUE_ENABLE, TORQUE_DISABLE)
	if dxl_comm_result != COMM_SUCCESS:
		print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
	elif dxl_error != 0:
		print("%s" % packetHandler.getRxPacketError(dxl_error))

# Close port
portHandler.closePort()
