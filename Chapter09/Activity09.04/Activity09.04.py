MIT License

Copyright (c) 2020 Packt Workshops

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



################################################################################
#                                                                              #
#                                                                              #
#           IMPORTANT: READ BEFORE DOWNLOADING, COPYING AND USING.             #
#                                                                              #
#                                                                              #
#      Copyright [2017] [ShenZhen Longer Vision Technology], Licensed under    #
#      ******** GNU General Public License, version 3.0 (GPL-3.0) ********     #
#      You are allowed to use this file, modify it, redistribute it, etc.      #
#      You are NOT allowed to use this file WITHOUT keeping the License.       #
#                                                                              #
#      Longer Vision Technology is a startup located in Chinese Silicon Valley #
#      NanShan, ShenZhen, China, (http://www.longervision.cn), which provides  #
#      the total solution to the area of Machine Vision & Computer Vision.     #
#      The founder Mr. Pei JIA has been advocating Open Source Software (OSS)  #
#      for over 12 years ever since he started his PhD's research in England.  #
#                                                                              #
#      Longer Vision Blog is Longer Vision Technology's blog hosted on github  #
#      (http://longervision.github.io). Besides the published articles, a lot  #
#      more source code can be found at the organization's source code pool:   #
#      (https://github.com/LongerVision/OpenCV_Examples).                      #
#                                                                              #
#      For those who are interested in our blogs and source code, please do    #
#      NOT hesitate to comment on our blogs. Whenever you find any issue,      #
#      please do NOT hesitate to fire an issue on github. We'll try to reply   #
#      promptly.                                                               #
#                                                                              #
#                                                                              #
# Version:          0.0.1                                                      #
# Author:           JIA Pei                                                    #
# Contact:          jiapei@longervision.com                                    #
# URL:              http://www.longervision.cn                                 #
# Create Date:      2017-03-10                                                 #
################################################################################

import sys
sys.path.append('/usr/local/python/3.5')  # whichever folder that contains **cv2.so** when you built OpenCV

import os
import cv2
from cv2 import aruco
import numpy as np



calibrationFile = "calibrationFileName.xml"
calibrationParams = cv2.FileStorage(calibrationFile, cv2.FILE_STORAGE_READ)
camera_matrix = calibrationParams.getNode("cameraMatrix").mat()
dist_coeffs = calibrationParams.getNode("distCoeffs").mat()

r = calibrationParams.getNode("R").mat()
new_camera_matrix = calibrationParams.getNode("newCameraMatrix").mat()

image_size = (1920, 1080)
map1, map2 = cv2.fisheye.initUndistortRectifyMap(camera_matrix, dist_coeffs, r, new_camera_matrix, image_size, cv2.CV_16SC2)



aruco_dict = aruco.Dictionary_get( aruco.DICT_6X6_1000 )
markerLength = 20   # Here, our measurement unit is centimetre.
arucoParams = aruco.DetectorParameters_create()



imgDir = "imgSequence"  # Specify the image directory
imgFileNames = [os.path.join(imgDir, fn) for fn in next(os.walk(imgDir))[2]]
nbOfImgs = len(imgFileNames)

for i in range(0, nbOfImgs):
    img = cv2.imread(imgFileNames[i], cv2.IMREAD_COLOR)
    imgRemapped = cv2.remap(img, map1, map2, cv2.INTER_LINEAR, cv2.BORDER_CONSTANT) # for fisheye remapping
    imgRemapped_gray = cv2.cvtColor(imgRemapped, cv2.COLOR_BGR2GRAY)    # aruco.detectMarkers() requires gray image
    corners, ids, rejectedImgPoints = aruco.detectMarkers(imgRemapped_gray, aruco_dict, parameters=arucoParams) # Detect aruco
    if ids != None: # if aruco marker detected
        rvec, tvec = aruco.estimatePoseSingleMarkers(corners, markerLength, camera_matrix, dist_coeffs) # posture estimation from a single marker
        imgWithAruco = aruco.drawDetectedMarkers(imgRemapped, corners, ids, (0,255,0))
        imgWithAruco = aruco.drawAxis(imgWithAruco, camera_matrix, dist_coeffs, rvec, tvec, 100)    # axis length 100 can be changed according to your requirement
    else:   # if aruco marker is NOT detected
        imgWithAruco = imgRemapped  # assign imRemapped_color to imgWithAruco directly

    cv2.imshow("aruco", imgWithAruco)   # display

    if cv2.waitKey(2) & 0xFF == ord('q'):   # if 'q' is pressed, quit.
        break

