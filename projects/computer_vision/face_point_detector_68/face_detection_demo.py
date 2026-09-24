"""Example: detect 68 face landmarks using the FaceDetector from face_landmark_detector."""

import face_landmark_detector

face_detector = face_landmark_detector.FaceDetector()
points = [None]
face_detector.detect_points(points)
