import cv2
from cv2 import aruco
import numpy as np


# params
squaresX = 5                           # Number of squares in X direction
squaresY = 7                           # Number of squares in Y direction
squareLength = 60                      # Square side length (in pixels)
markerLength = 30                      # Marker side length (in pixels)
dictionaryId = '6x6_250'              # dictionary id
margins = squareLength - markerLength;  # Margins size (in pixels)
borderBits = 1                         # Number of bits in marker borders

# dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
# board = cv2.aruco.CharucoBoard_create(10, 10,.025,.0125,dictionary)
# img = board.draw((200*10,200*10))

board_size = [7.5, 5.6]  # square_length, marker_length
marker_division = [8, 10]  # squares_x, squares_y


aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_5X5_1000)
board = aruco.CharucoBoard_create(marker_division[0], marker_division[1], board_size[0], board_size[1], aruco_dict)
img = board.draw((200*8,200*10))

#Dump the calibration board to a file
cv2.imwrite('charuco.png',img)