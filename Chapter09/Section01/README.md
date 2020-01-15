# Section 09.1: Pinhole Camera Calibration

Cannonical theories and methods of pinhole camera calibration have been deeply investigated for about two centuries. OpenCV tutorial [Camera calibration With OpenCV](https://docs.opencv.org/4.2.0/d4/d94/tutorial_camera_calibration.html) has dedicately summarized three calibration methods for a single pinhole camera, according to different calibration boards, including:
- Classical black-white chessboard
![Classical black-white chessboard](https://docs.opencv.org/4.2.0/pattern.png)

- Symmetrical circle pattern

- Asymmetrical circle pattern
![Asymmetrical circle pattern](https://docs.opencv.org/4.2.0/acircles_pattern.png)


The best way to design such a pattern is not to have it printed on a hardboard, but directly have it displayed on an extra monitor. In this way, instead of moving the calibration board around the fixed camera, we move the camera around in front of the monitor.



