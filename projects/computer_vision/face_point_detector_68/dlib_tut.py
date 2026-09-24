import dlib
import cv2
import imutils
from imutils import face_utils
import os


class FaceDetector:

    Model_PATH = "./shape_predictor_68_face_landmarks.dat"
    def __init__(self):
        self.face_points = []
        
        

    def detect_points(self,points=[None]): #Points =>list
        points = points
        Model_PATH =self.Model_PATH

        cap = cv2.VideoCapture(0)

        while cap.isOpened():
            ret,img = cap.read()

            img = imutils.resize(img,width=1280)
            detector = dlib.get_frontal_face_detector()
            faceLandmarkDetector = dlib.shape_predictor(Model_PATH)
            

            face_rects,scores,idx = detector.run(img,0)
            
            for i, d in enumerate(face_rects):
                x1 = d.left()
                y1 = d.top()
                x2 = d.right()
                y2 = d.bottom()
                rect = cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),4,cv2.LINE_AA)
                text = "Person %2.2f"%(scores[i])
                cv2.putText(img, text, (x1, y1), cv2.FONT_HERSHEY_DUPLEX,
            0.7, (255, 255, 255), 1, cv2.LINE_AA)

                
                detectedLandmarks = faceLandmarkDetector(img, d)
                detectedLandmarks = face_utils.shape_to_np(detectedLandmarks)
                self.face_points = []
                for pi,p in enumerate(detectedLandmarks):
                    
                    try:
                        if pi in points or points==[None]:
                            self.face_points.append((p[0],p[1]))
                            cv2.circle(img,(p[0],p[1]),2,(255,255,0),-1)
                            cv2.putText(img, "{}".format(pi), (p[0], p[1]), cv2.FONT_HERSHEY_DUPLEX,
                    0.3, (255, 255, 255), 1, cv2.LINE_AA)
                            print("{0}:{1}".format(str(pi),str(p))) 
                    except:
                        pass
            
            cv2.imshow("Face",cv2.resize(img,(800,600)))
            if cv2.waitKey(33) == 27:
                break
            
        cv2.destroyAllWindows()
        





if __name__ == "__main__":
    face_detector = FaceDetector()
    #points = [1,2,3,4,5,60,61,62] #show point of interest
    points = [None] #show All points
    #points = None #show no points
    face_detector.detect_points(points)




        