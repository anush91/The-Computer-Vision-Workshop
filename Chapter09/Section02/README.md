# Section 09.2: Fisheye Camera Calibrarion

A fisheye camera is a pinhole camera equipped with a fisheye lens. Normally, pictures taken by a fisheye camera are extremely distorted. OpenCV documentation [Fisheye camera model](https://docs.opencv.org/4.2.0/db/d58/group__calib3d__fisheye.html) provides plenty of functions to deal with **Fisheye cameras**. 


In this chapter, our experiments are tested on [Jevois](http://jevois.org) with its [120-degree fisheye lens](https://www.jevoisinc.com/products/jevois-1-3mp-sensor-with-120deg-fisheye-lens) for fisheye calibration.

```console
➜  ~ lsusb
......
Bus 001 Device 010: ID 1d6b:0102 Linux Foundation EEM Gadget
......
```

