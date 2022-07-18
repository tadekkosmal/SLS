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

    #cam1 = VideoCapture(0)
    cam1 = VideoCapture(1)
    # FLIR camera setup
    # flir_cam1 = FLIR(0)
    # flir_cam1.init()
    # flir_cam1.start()
    # flir_cam1.GainAuto = 'Off'
    # flir_cam1.Gain = min(20, flir_cam1.get_info('Gain')['max'])  # set the gain to 20 dB or the maximum of the camera.
    # flir_cam1.ExposureAuto = 'Off'
    # flir_cam1.ExposureTime = exposure_time

    # flir_cam2 = FLIR(1)
    # flir_cam2.init()
    # flir_cam2.start()
    # flir_cam2.GainAuto = 'Off'
    # flir_cam2.Gain = min(20, flir_cam1.get_info('Gain')['max'])  # set the gain to 20 dB or the maximum of the camera.
    # flir_cam2.ExposureAuto = 'Off'
    # flir_cam2.ExposureTime = exposure_time

    # live stream
    print('start streaming-------------------------')
    listener = Listener(on_press=lambda x: on_press(x))
    listener.start()
    while True:
        # acquire data
        retval, frame = cam1.read()  # resolution: [3000, 4096]
        #result1, image2 = cam2.read()
        left_right_image = np.split(frame, 2, axis=1)
        # Display images
        cv2.imshow("left RAW", left_right_image[0])

        #left_rect = cv2.remap(left_right_image[0], map_left_x, map_left_y, interpolation=cv2.INTER_LINEAR)
        #right_rect = cv2.remap(left_right_image[1], map_right_x, map_right_y, interpolation=cv2.INTER_LINEAR)

        #cv2.imshow("left RECT", np.concatenate([left_right_image[0], left_right_image[1]], axis=1))
        cv2.imshow("left RECT", left_right_image[1])
        #flir_img1 = cv2.resize(image1, (1920, 1200))
        #flir_img2 = cam2.get_array()  # resolution: [3000, 4096]
        #flir_img2 = cv2.resize(image2, (2048, 1500))
        
        # plot
        #flir_for_plot1 = cv2.resize(flir_img1, (flir_img1.shape[1] // 4, flir_img1.shape[0] // 4))
        #flir_for_plot2 = cv2.resize(flir_img2, (flir_img2.shape[1] // 2, flir_img2.shape[0] // 2))
        #flir_for_plot = np.concatenate([flir_for_plot2, flir_for_plot1], axis=1)
        #flir_for_plot = skimage.transform.rescale(flir_for_plot, 0.6)
        #cv2.imshow('concated imgs', image1)
        k = cv2.waitKey(1)

        # save images
        if IS_KEY_S_PRESSED is True:
            print('capturing the {}-th pair'.format(img_counter))

            cv2.imwrite('./data/{}/left/{}.png'.format(task_name, img_counter), left_right_image[0])             
            cv2.imwrite('./data/{}/right/{}.png'.format(task_name, img_counter), left_right_image[1])
            #cv2.imwrite('./data/{}/right/{}.png'.format(task_name, img_counter), frame)
            
            img_counter += 1
            time.sleep(0.1)
            IS_KEY_S_PRESSED = False
            if (img_counter == 18):
                break
