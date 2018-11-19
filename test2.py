# import the necessary packages
import math
from dynamixel import * 
from collections import deque
import numpy as np


import time



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
inverse = 0

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
dxl_goal_position = [
    #1
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],

[206,510,512,512,731],
[206,508,512,512,730],
[206,506,512,512,729],
[206,504,512,512,728],
[206,510,512,512,731],
[206,508,512,512,730],
[206,506,512,512,729],
[206,504,512,512,728],
[206,510,512,512,731],
[206,508,512,512,730],
[206,506,512,512,729],
[206,504,512,512,728],
[206,510,512,512,731],
[206,508,512,512,730],
[206,506,512,512,729],
[206,504,512,512,728],
[206,510,512,512,731],
[206,508,512,512,730],
[206,506,512,512,729],
[206,504,512,512,728],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],
[206,512,512,512,732],

[206,510,512,512,731],
[206,508,512,512,730],
[206,506,512,512,729],
[206,504,512,512,728],
[206,510,512,512,731],
[206,508,512,512,730],
[206,506,512,512,729],
[206,504,512,512,728],
[206,510,512,512,731],
[206,508,512,512,730],
[206,506,512,512,729],
[206,504,512,512,728],
[206,510,512,512,731],
[206,508,512,512,730],
[206,506,512,512,729],
[206,504,512,512,728],
[206,510,512,512,731],
[206,508,512,512,730],
[206,506,512,512,729],
[206,504,512,512,728],
#100
#2
[206,502,512,512,727],
[206,500,512,512,726],
[206,498,512,512,725],
[206,496,512,512,724],
[206,494,512,512,723],
[206,492,512,512,722],
[206,490,512,512,721],
[206,488,512,512,720],
[206,486,512,512,719],
[206,484,512,512,718],
[206,482,512,512,717],
[206,480,512,512,716],
[206,478,512,512,700],
[206,476,512,512,690],
[206,474,512,512,670],
[206,472,512,512,650],
[206,470,512,512,630],
[206,468,512,512,610],
[206,466,512,512,600],
[206,464,512,512,580],
[206,462,512,512,560],
[206,460,512,512,540],
[206,458,512,512,520],
[206,456,512,512,510],
[206,454,512,512,500],
[206,452,512,512,500],
[206,450,512,512,500],
[206,448,512,512,500],
[206,446,512,512,500],
[206,444,512,512,500],
[206,442,512,512,500],
[206,440,512,512,500],
[206,438,512,512,500],
[206,436,512,512,500],
[206,434,512,512,500],
[206,432,512,512,500],
[206,430,512,512,500],
[206,428,512,512,500],
[206,426,512,512,500],
[206,424,512,512,500],
[206,422,512,512,500],
[206,420,512,512,500],
[206,418,512,512,500],
[206,416,512,512,500],
[206,414,512,512,500],
[206,412,512,512,500],
[206,410,512,512,500],
[206,408,512,512,500],
[206,406,512,512,500],
[206,404,512,512,500],
[206,402,512,512,500],
[206,400,512,512,500],
[206,398,512,512,500],
[206,395,512,512,500],
[206,390,512,512,500],
[206,385,512,512,500],
[206,380,512,512,500],
[206,375,512,512,500],
[206,370,512,512,500],
[206,365,512,512,500],
[206,360,512,512,500],
[206,355,512,512,500],
[206,350,512,512,500],
[206,345,512,512,500],
[206,340,512,512,500],
[206,335,512,512,500],
[206,330,512,512,500],
[206,325,512,512,500],
[206,320,512,512,500],
[206,315,512,512,500],
[206,310,512,512,500],
[206,305,512,512,500],
[206,300,512,512,500],
#3
[206,305,512,512,500],
[206,310,512,512,500],
[206,315,512,512,500],
[206,320,512,512,500],
[206,325,512,512,500],
[206,330,512,512,500],
[206,335,512,512,500],
[206,340,512,512,500],
[206,345,512,512,500],
[206,350,512,512,500],
[206,355,512,512,500],
[206,360,512,512,500],
[206,365,512,512,500],
[206,370,512,512,500],
[206,375,512,512,500],
[206,380,512,512,500],
[206,385,512,512,500],
[206,390,512,512,500],
[206,395,512,512,500],
[206,400,512,512,500],
[206,405,512,512,500],
[206,410,512,512,500],
[206,415,512,512,500],
[206,420,512,512,500],
[206,425,512,512,500],
[206,430,512,512,500],
[206,435,512,512,500],
[206,440,512,512,500],
[206,445,512,512,500],
[206,450,512,512,500],
[206,455,512,512,500],
[206,460,512,512,500],
[206,465,512,512,500],
[206,470,512,512,500],
[206,475,512,512,500],
[206,480,512,512,500],
[206,485,512,512,500],
[206,490,512,512,500],
[206,495,512,512,500],
[206,500,512,512,500],
[206,503,512,512,500],
[206,507,512,512,500],
[206,510,512,512,500],
[206,512,512,512,500],
[206,515,512,512,500],
[206,518,512,512,500],
[206,520,512,512,500],
[206,525,512,512,500],
[206,530,512,512,500],
[206,535,512,512,500],
[206,540,512,512,500],
[206,545,512,512,500],
[206,550,512,512,500],
[206,555,512,512,500],
[206,560,512,512,500],
[206,565,512,512,500],
[206,570,512,512,500],
[206,575,512,512,500],
[206,580,512,512,500],
[206,585,512,512,500],
[206,590,512,512,500],
[206,595,512,512,500],
[206,600,512,512,500],
[206,605,512,512,500],
[206,610,512,512,500],
[206,615,512,512,500],
[206,620,512,512,500],
[206,625,512,512,500],
[206,630,512,512,500],
[206,635,512,512,500],
[206,640,512,512,500],
[206,645,512,512,500],
[206,650,512,512,500],
[206,655,512,512,500],
[206,660,512,512,500],
[206,665,512,512,500],
[206,670,512,512,500],
[206,675,512,512,500],
[206,680,512,512,500],
[206,685,512,512,500],
[206,690,512,512,500],
[206,695,512,512,500],
[206,700,512,512,500],
[206,705,512,512,500],
[206,710,512,512,500],
[206,715,512,512,500],
[206,710,512,512,500],
[206,715,512,512,500],
[206,720,512,512,500],
[206,725,512,512,500],
[206,720,512,512,500],
[206,715,512,512,500],
[206,710,512,512,500],
[206,705,512,512,500],
[206,700,512,512,500],
[206,695,512,512,500],
[206,690,512,512,500],
[206,685,512,512,500],
[206,680,512,512,500],
[206,675,512,512,500],
[206,670,512,512,500],
[206,665,512,512,500],
[206,660,512,512,500],
[206,655,512,512,500],
[206,650,512,512,500],
[206,645,512,512,500],
[206,640,512,512,500],
[206,635,512,512,500],
[206,630,512,512,500],
[206,625,512,512,500],
[206,620,512,512,500],
[206,615,512,512,500],
[206,610,512,512,500],
[206,605,512,512,500],
[206,600,512,512,500],
[206,595,512,512,500],
[206,590,512,512,500],
[206,585,512,512,500],
[206,580,512,512,500],
[206,575,512,512,500],
[206,570,512,512,500],
[206,565,512,512,500],
[206,560,512,512,500],
[206,555,512,512,500],
[206,550,512,512,500],
[206,545,512,512,500],
[206,540,512,512,500],
[206,535,512,512,500],
[206,530,512,512,500],
[206,525,512,512,500],
[206,520,512,512,500],
[206,515,512,512,500],
[206,510,512,512,500],
[206,505,512,512,500],

[206,502,512,512,727],
[206,500,512,512,726],
[206,498,512,512,725],
[206,496,512,512,724],
[206,494,512,512,723],
[206,492,512,512,722],
[206,490,512,512,721],
[206,488,512,512,720],
[206,486,512,512,719],
[206,484,512,512,718],
[206,482,512,512,717],
[206,480,512,512,716],
[206,478,512,512,700],
[206,476,512,512,690],
[206,474,512,512,670],
[206,472,512,512,650],
[206,470,512,512,630],
[206,468,512,512,610],
[206,466,512,512,600],
[206,464,512,512,580],
[206,462,512,512,560],
[206,460,512,512,540],
[206,458,512,512,520],
[206,456,512,512,510],
[206,454,512,512,500],
[206,452,512,512,500],
[206,450,512,512,500],
[206,448,512,512,500],
[206,446,512,512,500],
[206,444,512,512,500],
[206,442,512,512,500],
[206,440,512,512,500],
[206,438,512,512,500],
[206,436,512,512,500],
[206,434,512,512,500],
[206,432,512,512,500],
[206,430,512,512,500],
[206,428,512,512,500],
[206,426,512,512,500],
[206,424,512,512,500],
[206,422,512,512,500],
[206,420,512,512,500],
[206,418,512,512,500],
[206,416,512,512,500],
[206,414,512,512,500],
[206,412,512,512,500],
[206,410,512,512,500],
[206,408,512,512,500],
[206,406,512,512,500],
[206,404,512,512,500],
[206,402,512,512,500],
[206,400,512,512,500],
[206,398,512,512,500],
[206,395,512,512,500],
[206,390,512,512,500],
[206,385,512,512,500],
[206,380,512,512,500],
[206,375,512,512,500],
[206,370,512,512,500],
[206,365,512,512,500],
[206,360,512,512,500],
[206,355,512,512,500],
[206,350,512,512,500],
[206,345,512,512,500],
[206,340,512,512,500],
[206,335,512,512,500],
[206,330,512,512,500],
[206,325,512,512,500],
[206,320,512,512,500],
[206,315,512,512,500],
[206,310,512,512,500],
[206,305,512,512,500],
[206,300,512,512,500],
#3
[206,305,512,512,500],
[206,310,512,512,500],
[206,315,512,512,500],
[206,320,512,512,500],
[206,325,512,512,500],
[206,330,512,512,500],
[206,335,512,512,500],
[206,340,512,512,500],
[206,345,512,512,500],
[206,350,512,512,500],
[206,355,512,512,500],
[206,360,512,512,500],
[206,365,512,512,500],
[206,370,512,512,500],
[206,375,512,512,500],
[206,380,512,512,500],
[206,385,512,512,500],
[206,390,512,512,500],
[206,395,512,512,500],
[206,400,512,512,500],
[206,405,512,512,500],
[206,410,512,512,500],
[206,415,512,512,500],
[206,420,512,512,500],
[206,425,512,512,500],
[206,430,512,512,500],
[206,435,512,512,500],
[206,440,512,512,500],
[206,445,512,512,500],
[206,450,512,512,500],
[206,455,512,512,500],
[206,460,512,512,500],
[206,465,512,512,500],
[206,470,512,512,500],
[206,475,512,512,500],
[206,480,512,512,500],
[206,485,512,512,500],
[206,490,512,512,500],
[206,495,512,512,500],
[206,500,512,512,500],
[206,503,512,512,500],
[206,507,512,512,500],
[206,510,512,512,500],
[206,512,512,512,500],
[206,515,512,512,500],
[206,518,512,512,500],
[206,520,512,512,500],
[206,525,512,512,500],
[206,530,512,512,500],
[206,535,512,512,500],
[206,540,512,512,500],
[206,545,512,512,500],
[206,550,512,512,500],
[206,555,512,512,500],
[206,560,512,512,500],
[206,565,512,512,500],
[206,570,512,512,500],
[206,575,512,512,500],
[206,580,512,512,500],
[206,585,512,512,500],
[206,590,512,512,500],
[206,595,512,512,500],
[206,600,512,512,500],
[206,605,512,512,500],
[206,610,512,512,500],
[206,615,512,512,500],
[206,620,512,512,500],
[206,625,512,512,500],
[206,630,512,512,500],
[206,635,512,512,500],
[206,640,512,512,500],
[206,645,512,512,500],
[206,650,512,512,500],
[206,655,512,512,500],
[206,660,512,512,500],
[206,665,512,512,500],
[206,670,512,512,500],
[206,675,512,512,500],
[206,680,512,512,500],
[206,685,512,512,500],
[206,690,512,512,500],
[206,695,512,512,500],
[206,700,512,512,500],
[206,705,512,512,500],
[206,710,512,512,500],
[206,715,512,512,500],
[206,710,512,512,500],
[206,715,512,512,500],
[206,720,512,512,500],
[206,725,512,512,500],
[206,720,512,512,500],
[206,715,512,512,500],
[206,710,512,512,500],
[206,705,512,512,500],
[206,700,512,512,500],
[206,695,512,512,500],
[206,690,512,512,500],
[206,685,512,512,500],
[206,680,512,512,500],
[206,675,512,512,500],
[206,670,512,512,500],
[206,665,512,512,500],
[206,660,512,512,500],
[206,655,512,512,500],
[206,650,512,512,500],
[206,645,512,512,500],
[206,640,512,512,500],
[206,635,512,512,500],
[206,630,512,512,500],
[206,625,512,512,500],
[206,620,512,512,500],
[206,615,512,512,500],
[206,610,512,512,500],
[206,605,512,512,500],
[206,600,512,512,500],
[206,595,512,512,500],
[206,590,512,512,500],
[206,585,512,512,500],
[206,580,512,512,500],
[206,575,512,512,500],
[206,570,512,512,500],
[206,565,512,512,500],
[206,560,512,512,500],
[206,555,512,512,500],
[206,550,512,512,500],
[206,545,512,512,500],
[206,540,512,512,500],
[206,535,512,512,500],
[206,530,512,512,500],
[206,525,512,512,500],
[206,520,512,512,500],
[206,515,512,512,500],

#end
[206,520,512,512,500],
[206,540,490,490,500],
[206,560,460,460,500],
[206,580,430,430,500],
[206,600,420,420,500],
[206,620,400,400,500],
[206,640,370,370,500],
[206,660,350,350,500],
[206,680,320,330,500],
[206,700,300,310,500],
[206,720,279,300,500],
[206,740,250,270,500],
[206,760,220,250,500],
[206,780,200,220,500],
[206,800,170,200,500],
[206,820,150,180,500],
[206,840,120,175,500],
[206,860,100,175,500],
[206,880,90,175,500],
[206,900,90,175,500],
[206,920,90,175,500],
[206,940,90,175,500],
[206,953,90,175,500],
[206,953,90,175,500],
[206,953,90,175,500],
[206,953,90,175,500],
[206,953,90,175,500],
[206,953,90,175,500],
[206,953,90,175,500],
[206,953,90,175,500],
[206,953,90,175,500],
[206,953,90,175,500],
[206,953,90,175,500],
[206,953,90,175,500],
[206,953,90,175,500],
[206,953,90,175,500],
[206,953,90,175,500],
[206,953,90,175,500],
[206,953,90,175,500],
[206,953,90,175,500],
[206,953,90,175,500],
[206,953,90,175,500],
[206,953,90,175,500]
]





total=555
index = 0
while True :
	while True :
		for ID in range(1,5):
			dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, ID, ADDR_PRO_GOAL_POSITION, dxl_goal_position[index][ID-1])
			print(settheta[ID-1])
			if dxl_comm_result != COMM_SUCCESS:
				print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
			elif dxl_error != 0:
				print("%s" % packetHandler.getRxPacketError(dxl_error)) 

		time.sleep(0.1)
	if (index == total):
		time.sleep(30)
		break
	else:
		index = index + 1
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
