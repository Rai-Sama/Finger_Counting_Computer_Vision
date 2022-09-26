# Finger_Counting_Computer_Vision
* A simple Computer Vision project created to learn uses of OpenCV.
* Uses computer vision to dynamically count the number of fingers held up by the user.

## Hand_tracking_module.py
* A general module created for all my hand gesture tracking programs.
* Uses mediapipe for tracking landmarks on the hand.

## fingerCounting.py
Uses the hand tracking module to recognize the hand and the fingers individually. It then, counts and displays the number of fingers held up.

### Note
The program does the calculations assuming the user uses their right hand. The formulae can be easily modified to work with the left hand as well. (The position of the thumb is the only difference)

# Demo
![alt-text](https://github.com/Rai-Sama/Finger_Counting_Computer_Vision/blob/master/Demo.gif)
