import os
import time
import numpy as np
import cv2
from cv2 import VideoCapture
from matplotlib import pyplot as plt


if __name__ == '__main__':
    # setups

    task_name = 'tadek_capture'
    # task_name = 'stereo_calib_flir'
    img_counter = 0
    exposure_time = 25000
    #cam1 = VideoCapture(0)
    cam1 = VideoCapture(0)




    proj_w, proj_h = 1280, 800
    major_screen_resolution = int(3840)  # resolution of the laptop's screen (e.g., 1080P laptop with 150% scaling)
    #major_screen_resolution = int(720)  # resolution of the laptop's screen (e.g., 1080P laptop with 150% scaling)
    # generate patterns
    graycode = cv2.structured_light_GrayCodePattern.create(width=proj_w, height=proj_h)
    graycodes = graycode.generate()
    patterns = graycodes[1]
    masks = graycode.getImagesForShadowMasks(np.zeros_like(patterns[0]), np.zeros_like(patterns[0]))
    patterns = patterns + (masks[0], masks[1])   # horizontal, vertical, black-white
    print('{} pictures in total for the projector resolution ({}, {})'.format(len(patterns), proj_w, proj_h))

    for i, x in enumerate(patterns):
        print('showing the {}-th image'.format(i))
        capname = '{}'.format(i)
        cv2.namedWindow(capname, cv2.WND_PROP_FULLSCREEN)
        cv2.moveWindow(capname, major_screen_resolution, 0)
        cv2.setWindowProperty(capname, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        
        cv2.imshow(capname, x)

        
        #time.sleep(1)
        
        #time.sleep(0.1)

        k = cv2.waitKey(0)
        if k == ord("q"):
            cv2.destroyWindow(capname)
            retval, frame = cam1.read()
            left_right_image = np.split(frame, 2, axis=1)
            cv2.imwrite('./data/{}/left/{}.png'.format(task_name, img_counter), left_right_image[0])             
            cv2.imwrite('./data/{}/right/{}.png'.format(task_name, img_counter), left_right_image[1])
            img_counter += 1
            continue
        else:
            time.sleep(2)
            cv2.destroyWindow(capname)
            continue