from multiprocessing.connection import Listener
import cv2
from cv2 import VideoCapture
import numpy as np
from matplotlib import pyplot as plt
#from simple_pyspin import Camera as FLIR
from pynput.keyboard import Listener
import time
import skimage


IS_KEY_S_PRESSED = False  # detect if the


def on_press(key):  # The function that's called when a key is pressed
    global IS_KEY_S_PRESSED
    if 'char' in dir(key):  # check if char method exists,
        if key.char == 's':
            IS_KEY_S_PRESSED = True


##-----------------------------------------------------------------------


if __name__ == '__main__':
    task_name = 'tadek_camera'
    # task_name = 'stereo_calib_flir'
    img_counter = 0
    exposure_time = 25000


    cam1 = VideoCapture(0)
    cam2 = VideoCapture(2)

    # live stream
    print('start streaming-------------------------')
    listener = Listener(on_press=lambda x: on_press(x))
    listener.start()
    while True:
        # acquire data
        retval1, frame1 = cam1.read()  # resolution: [3000, 4096]
        retval2, frame2 = cam2.read()
        #result1, image2 = cam2.read()
        #left_right_image = np.split(frame, 2, axis=1)
        # Display images
        #cv2.imshow("left RAW", frame1)

        #left_rect = cv2.remap(left_right_image[0], map_left_x, map_left_y, interpolation=cv2.INTER_LINEAR)
        #right_rect = cv2.remap(left_right_image[1], map_right_x, map_right_y, interpolation=cv2.INTER_LINEAR)

        #cv2.imshow("left RECT", np.concatenate([left_right_image[0], left_right_image[1]], axis=1))
        #cv2.imshow("left RECT", frame)
        #flir_img1 = cv2.resize(image1, (1920, 1200))
        #flir_img2 = cam2.get_array()  # resolution: [3000, 4096]
        #flir_img2 = cv2.resize(image2, (2048, 1500))
        
        # plot
        scale_factor = 1
        flir_for_plot1 = cv2.resize(frame1, (frame1.shape[1] // scale_factor, frame1.shape[0] // scale_factor))
        flir_for_plot2 = cv2.resize(frame2, (frame2.shape[1] // scale_factor, frame2.shape[0] // scale_factor))
        flir_for_plot = np.concatenate([flir_for_plot2, flir_for_plot1], axis=1)
        #flir_for_plot = skimage.transform.rescale(flir_for_plot, 0.6)
        cv2.imshow('concated imgs', flir_for_plot)
        k = cv2.waitKey(1)

        # save images
        if IS_KEY_S_PRESSED is True:
            print('capturing the {}-th pair'.format(img_counter))

            cv2.imwrite('./data/{}/left/{}.png'.format(task_name, img_counter), frame1)             
            cv2.imwrite('./data/{}/right/{}.png'.format(task_name, img_counter), frame2)
            #cv2.imwrite('./data/{}/right/{}.png'.format(task_name, img_counter), frame)
            
            img_counter += 1
            time.sleep(0.1)
            IS_KEY_S_PRESSED = False
            if (img_counter == 18):
                break
