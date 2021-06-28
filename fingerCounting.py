import cv2 
import time
import os
import hand_tracking_module as htm
cap = cv2.VideoCapture(0)
wCam, hCam = 640, 720

WINDOW_NAME = "Volume Controller" # For full screen
cv2.namedWindow(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN) # New named window
cv2.setWindowProperty(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN) # Setting size of the window


cap.set(3, wCam) # 3 -> width
cap.set(4, hCam) # 4 -> height

folderPath = "Finger_Images" # Images folder
myList = os.listdir(folderPath) # List of image names
# print(myList)
overlayList = []
for impath in myList:
	image = cv2.imread(f'{folderPath}/{impath}') # Retrieving each image
	overlayList.append(image) # List of the images


detector = htm.handDetector(detectionCon=0.7)

tipIds = [4, 8, 12, 16, 20] 
# 4 -> Thumb, 8 -> Index, 12 -> middle, 16 -> ring, 20 -> pinky 

ptime = 0 # Previous time for fps calculation
while True:
	success, img = cap.read()

	img = cv2.flip(img, 1) # For flipping the image horizontally; since my webcam is flipped by default
	img = detector.findHands(img)
	lmList = detector.findPosition(img, draw=False)

	if(len(lmList)): # If a hand is detected
		fingers = []

		if lmList[4][1] < lmList[3][1]: # Special condition for thumb as it curls to the side not down
			fingers.append(1)
		else:
			fingers.append(0)

		for id in tipIds[1:]: # All fingers except thumb 
			if lmList[id][2] < lmList[id-2][2]:
				fingers.append(1)
			else:
				fingers.append(0)
		# print(fingers)
		totalFingers = sum(fingers) # Number of fingers up
		# Note that if a fist is made, totalFingers = 0 and so -1th element (last image) will be taken
		img[0:200, 0:200] = overlayList[totalFingers - 1]

		cv2.putText(img, str(totalFingers), (100, 275), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 10)


	# Calculating and displaying FPS
	ctime = time.time()
	fps = 1/(ctime - ptime)
	ptime = ctime
	cv2.putText(img, f'FPS: {int(fps)}', (500, 30), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 0, 0), 3)

	cv2.imshow(WINDOW_NAME, img) # For full screen display
	# cv2.imshow("Controller", img) # For 640 x 720 display window (better when debugging)

	if cv2.waitKey(1) & 0xFF == 27: # Press Esc to quit
		break