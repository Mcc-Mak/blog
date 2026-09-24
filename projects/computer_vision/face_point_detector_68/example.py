"""Example: detect 68 face landmarks using the FaceDetector from dlib_tut."""

import dlib_tut

face_detector = dlib_tut.FaceDetector()
points = [None]
face_detector.detect_points(points)
