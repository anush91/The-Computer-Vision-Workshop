# Section 09.3: Camera Pose Estimation


With the calibration parameters (namely, camera intrinsic parameters), by providing any type of calibration board as the reference, the camera posture relative to this calibration board can be accurately estimated.


[Activity09.03.py](../Activity09.03/Activity09.03.py) provides a code snippet for pose estimation using an asymmetrical circle pattern.


[Activity09.04.py](../Activity09.04/Activity09.04.py) provides a code snippet for pose estimation using a single ArUco marker.


**Exercise 09.02**<br/>
Please use as many [OpenCV ArUco markers or groups of markers](https://docs.opencv.org/master/d9/d6a/group__aruco.html) as possible to estimate your camera's postures. Again, you are also encouraged to try out [pattern generator from Calib.io](https://calib.io/pages/camera-calibration-pattern-generator) to generate your own markers for estimating camera postures.
