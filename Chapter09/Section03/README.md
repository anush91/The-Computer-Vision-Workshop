# Section 09.3: Camera Pose Estimation


With the calibration parameters (namely, camera intrinsic parameters), by providing any type of calibration board as the reference, the camera posture relative to this calibration board can be accurately estimated. And in this chapter, we're going to use [ArUco markers](https://docs.opencv.org/master/d9/d6a/group__aruco.html) to estimate poses of [Jevois camera](https://www.jevoisinc.com/products/jevois-a33-smart-machine-vision-camera?variant=36249051018) with its [120-degree fisheye lens](https://www.jevoisinc.com/products/jevois-1-3mp-sensor-with-120deg-fisheye-lens).


[Activity09.05.py](../Activity09.05/Activity09.05.py) provides a code snippet for pose estimation using an asymmetrical circle pattern.


[Activity09.06.py](../Activity09.06/Activity09.06.py) provides a code snippet for pose estimation using a single ArUco marker.


**Exercise 09.02**<br/>
Please use as many [OpenCV ArUco markers or groups of markers](https://docs.opencv.org/master/d9/d6a/group__aruco.html) as possible to estimate your camera's postures. Again, you are also encouraged to try out [pattern generator from Calib.io](https://calib.io/pages/camera-calibration-pattern-generator) to generate your own markers for estimating camera postures.


