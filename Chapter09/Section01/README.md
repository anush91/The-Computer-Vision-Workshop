# Section 09.1: Pinhole Camera Calibration

Cannonical theories and methods of pinhole camera calibration have been deeply investigated for about two centuries. OpenCV tutorial [Camera calibration With OpenCV](https://docs.opencv.org/4.2.0/d4/d94/tutorial_camera_calibration.html) has dedicately summarized three calibration methods for a single pinhole camera, according to different calibration boards, including:
- Classical black-white chessboard
![Classical black-white chessboard](https://docs.opencv.org/4.2.0/pattern.png)

- Symmetrical circle pattern<br/>
Clearly, since a circle itself is symmetrical, if the circle pattern is designed as symmetrical, the entire symmetrical circle pattern is symmetrical as well, which will cause the ambiguity when the calibration board is turned around 180 degree. That's possibly why a symmetrical circle pattern is NOT provided in [OpenCV](https://opencv.org/).


- Asymmetrical circle pattern
![Asymmetrical circle pattern](https://docs.opencv.org/4.2.0/acircles_pattern.png)


The best low-cost way to design such a pattern is not to have it printed on a hardboard, but directly have it displayed on an extra monitor. In such a way,
- you not only ensure the perfect flatness of the calibration board,
- but also move a portable camera in front of the monitor rather than hold the calibration board and move it around the fixed camera.


[Activity09.01.py](../Activity09.01/Activity09.01.py) provides a code snippet for calibration using a chessboard.


[Activity09.02.py](../Activity09.02/Activity09.02.py) provides a code snippet for calibration using an asymmetrical circle pattern.


**Exercise09.01**<br/>
Generate any calibration pattern as you wish, and calibrate your camera with it. You can try out [camera calibration pattern generator from Calib.io](https://calib.io/pages/camera-calibration-pattern-generator)
