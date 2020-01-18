# Section 09.1: Pinhole Camera Calibration

Cannonical theories and methods of pinhole camera calibration have been deeply investigated for about two centuries. OpenCV tutorial [Camera calibration With OpenCV](https://docs.opencv.org/4.2.0/d4/d94/tutorial_camera_calibration.html) has clearly elaborated all intrinsic parameters to be calculated after camera calibration.
- 4 parameters referred as camera matrix,
$$
\begin{pmatrix}
f_x & 0 & c_x \\
0 & f_y & c_y \\
0 & 0 & 1
\end{pmatrix}
$$
in which $$(f_x, f_y)$$ are two focal lengths in two directions, and $$(c_x, c_y)$$ represent two optical centers;
- 3 parameters $$(k_1, k_2, k_3)$$ referred as radial factors;
- 2 parameters $$(p_1, p_2)$$ referred as tangential factors.

OpenCV tutorial [Camera calibration With OpenCV](https://docs.opencv.org/4.2.0/d4/d94/tutorial_camera_calibration.html) also dedicately summarized three calibration methods for a single pinhole camera, according to different calibration boards, including:
- Classical black-white chessboard
![Classical black-white chessboard](https://docs.opencv.org/4.2.0/pattern.png)

- Symmetrical circle pattern<br/>
Clearly, since a circle itself is symmetrical, if the circle pattern is designed as symmetrical, the entire symmetrical circle pattern is symmetrical as well, which will cause the ambiguity when the calibration board is turned around 180 degree. That's possibly why a symmetrical circle pattern is NOT provided in [OpenCV](https://opencv.org/).


- Asymmetrical circle pattern
![Asymmetrical circle pattern](https://docs.opencv.org/4.2.0/acircles_pattern.png)


The best low-cost way to design such a pattern is not to have it printed on a hardboard, but directly have it displayed on an extra monitor. In such a way,
- you not only ensure the perfect flatness of the calibration board,
- but also move a portable camera in front of the monitor rather than hold the calibration board and move it around the fixed camera.


In this chapter, we're using a Logitech C930e for our tests.

```console
➜  ~ lsusb
......
Bus 001 Device 006: ID 046d:0843 Logitech, Inc. Webcam C930e
......
```


[Activity09.01.py](../Activity09.01/Activity09.01.py) provides a code snippet for calibration using a chessboard.

The following 10 experimental images demonstrate the chessboard corner finding performace.

|   Column 1   |      Column 2      | 
|:----------:|:----------:|
| ![Cornors 0](chessboard/0.jpg) | ![Cornors 1](chessboard/1.jpg) |
| ![Cornors 2](chessboard/2.jpg) | ![Cornors 3](chessboard/3.jpg) |
| ![Cornors 4](chessboard/4.jpg) | ![Cornors 5](chessboard/5.jpg) |
| ![Cornors 6](chessboard/6.jpg) | ![Cornors 7](chessboard/7.jpg) |
| ![Cornors 8](chessboard/8.jpg) | ![Cornors 9](chessboard/9.jpg) |

And the resultant calibration matrix is calculated as in this [calibration.yaml](chessboard/calibration.yaml).


[Activity09.02.py](../Activity09.02/Activity09.02.py) provides a code snippet for calibration using an asymmetrical circle pattern.

Similar to [Activity09.01.py](../Activity09.01/Activity09.01.py), calibration can also be done using circle grids. 10 experimental images clearly demonstrate the performance to find the circle centers.

|   Column 1   |      Column 2      | 
|:----------:|:----------:|
| ![Circles 0](circlegrid/0.jpg) | ![Circles 1](circlegrid/1.jpg) |
| ![Circles 2](circlegrid/2.jpg) | ![Circles 3](circlegrid/3.jpg) |
| ![Circles 4](circlegrid/4.jpg) | ![Circles 5](circlegrid/5.jpg) |
| ![Circles 6](circlegrid/6.jpg) | ![Circles 7](circlegrid/7.jpg) |
| ![Circles 8](circlegrid/8.jpg) | ![Circles 9](circlegrid/9.jpg) |

The resultant calibration matrix is estimated as in this [calibration.yaml](circlegrid/calibration.yaml).


Clearly, these two resultant calibration.yaml files are of little differences. 


**Exercise 09.01**<br/>
Generate any calibration pattern as you wish, and calibrate your camera with it. You are encouraged to try out [pattern generator from Calib.io](https://calib.io/pages/camera-calibration-pattern-generator) to generate your own patterns for camera calibration.
