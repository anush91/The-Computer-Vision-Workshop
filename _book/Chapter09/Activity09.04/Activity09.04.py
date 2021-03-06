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
# Create Date:      2020-01-18                                                 #
################################################################################

# Standard imports
import numpy as np
import cv2


# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
criteria_fisheye = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 1e-6)

########################################Blob Detector##############################################
# Setup SimpleBlobDetector parameters.
blobParams = cv2.SimpleBlobDetector_Params()

# Change thresholds
blobParams.minThreshold = 8
blobParams.maxThreshold = 255

# Filter by Area.
blobParams.filterByArea = True
blobParams.minArea = 64     # minArea may be adjusted to suit for your experiment
blobParams.maxArea = 2500   # maxArea may be adjusted to suit for your experiment

# Filter by Circularity
blobParams.filterByCircularity = True
blobParams.minCircularity = 0.1

# Filter by Convexity
blobParams.filterByConvexity = True
blobParams.minConvexity = 0.87

# Filter by Inertia
blobParams.filterByInertia = True
blobParams.minInertiaRatio = 0.01

# Create a detector with the parameters
blobDetector = cv2.SimpleBlobDetector_create(blobParams)
###################################################################################################


###################################################################################################
# Original blob coordinates, supposing all blobs are of z-coordinates 0
# And, the distance between every two neighbour blob circle centers is 72 centimetres
# In fact, any number can be used to replace 72.
# Namely, the real size of the circle is pointless while calculating camera calibration parameters.
objp = np.zeros((1, 44, 3), np.float32)
objp[0][0]  = (0  , 0  , 0)
objp[0][1]  = (0  , 72 , 0)
objp[0][2]  = (0  , 144, 0)
objp[0][3]  = (0  , 216, 0)
objp[0][4]  = (36 , 36 , 0)
objp[0][5]  = (36 , 108, 0)
objp[0][6]  = (36 , 180, 0)
objp[0][7]  = (36 , 252, 0)
objp[0][8]  = (72 , 0  , 0)
objp[0][9]  = (72 , 72 , 0)
objp[0][10] = (72 , 144, 0)
objp[0][11] = (72 , 216, 0)
objp[0][12] = (108, 36,  0)
objp[0][13] = (108, 108, 0)
objp[0][14] = (108, 180, 0)
objp[0][15] = (108, 252, 0)
objp[0][16] = (144, 0  , 0)
objp[0][17] = (144, 72 , 0)
objp[0][18] = (144, 144, 0)
objp[0][19] = (144, 216, 0)
objp[0][20] = (180, 36 , 0)
objp[0][21] = (180, 108, 0)
objp[0][22] = (180, 180, 0)
objp[0][23] = (180, 252, 0)
objp[0][24] = (216, 0  , 0)
objp[0][25] = (216, 72 , 0)
objp[0][26] = (216, 144, 0)
objp[0][27] = (216, 216, 0)
objp[0][28] = (252, 36 , 0)
objp[0][29] = (252, 108, 0)
objp[0][30] = (252, 180, 0)
objp[0][31] = (252, 252, 0)
objp[0][32] = (288, 0  , 0)
objp[0][33] = (288, 72 , 0)
objp[0][34] = (288, 144, 0)
objp[0][35] = (288, 216, 0)
objp[0][36] = (324, 36 , 0)
objp[0][37] = (324, 108, 0)
objp[0][38] = (324, 180, 0)
objp[0][39] = (324, 252, 0)
objp[0][40] = (360, 0  , 0)
objp[0][41] = (360, 72 , 0)
objp[0][42] = (360, 144, 0)
objp[0][43] = (360, 216, 0)
###################################################################################################


# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.


cap = cv2.VideoCapture(2)
#initialize the jevois cam. See below - don't change these as it capture videos without any process
cap.set(3,640) #width
cap.set(4,480) #height
cap.set(5,15) #fps
s,img = cap.read()

num = 10
found = 0
while(found < num):  # Here, 10 can be changed to whatever number you like to choose
    ret, img = cap.read() # Capture frame-by-frame
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    keypoints = blobDetector.detect(gray) # Detect blobs.

    # Draw detected blobs as red circles. This helps cv2.findCirclesGrid() . 
    im_with_keypoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    im_with_keypoints_gray = cv2.cvtColor(im_with_keypoints, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findCirclesGrid(im_with_keypoints, (4,11), None, flags = cv2.CALIB_CB_ASYMMETRIC_GRID)   # Find the circle grid

    if ret == True:
        objpoints.append(objp)  # Certainly, every loop objp is the same, in 3D.

        corners2 = cv2.cornerSubPix(im_with_keypoints_gray, corners, (11,11), (-1,-1), criteria)    # Refines the corner locations.
        imgpoints.append(corners2)

        # Draw and display the corners.
        im_with_keypoints = cv2.drawChessboardCorners(img, (4,11), corners2, ret)

        # Enable the following 2 lines if you want to save the calibration images.
        filename = str(found) +".jpg"
        cv2.imwrite(filename, im_with_keypoints)

        found += 1


    cv2.imshow("img", im_with_keypoints) # display
    cv2.waitKey(2)


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


K = np.zeros((3, 3))
D = np.zeros((4, 1))
rvecs = [np.zeros((1, 1, 3), dtype=np.float64) for i in range(num)]
tvecs = [np.zeros((1, 1, 3), dtype=np.float64) for i in range(num)]
retval, _, _, _, _ = \
    cv2.fisheye.calibrate(
        objpoints,
        imgpoints,
        gray.shape[::-1],
        K,
        D,
        rvecs,
        tvecs,
        cv2.fisheye.CALIB_RECOMPUTE_EXTRINSIC+cv2.fisheye.CALIB_FIX_SKEW,
        criteria_fisheye
    )

print(retval)
print(K)
print(D)

#  Python code to write the image (OpenCV 3.2)
fs = cv2.FileStorage('calibration.yml', cv2.FILE_STORAGE_WRITE)
fs.write('camera_matrix', K)
fs.write('dist_coeff', D)
fs.release()

