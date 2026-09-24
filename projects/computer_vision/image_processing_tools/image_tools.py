import numpy as np
import imutils
import cv2

class image_tools(object):
    def __init__(self):
        pass
    def ConvertVideoToPanorama(self,video_path:str,save:bool = False,steps:int = 10): 
        #Input: Video Path +(opt)save?    => Output: Panorama photo array and display image + +(opt)save?
        #Video extension format: mp4, MOV ...
        video_cap = cv2.VideoCapture(video_path)
        i = 0
        images = []
        while video_cap.isOpened():
            ret,frame = video_cap.read()
            if ret == False:
                break
            images.append(frame)
        images = np.array(images)
        video_cap.release()
        panorama_img = images[0]
        steps = 10 #frame step to match
        for img in images[::steps]:
            HM = self.__FindHomographicMatrix(img,panorama_img) #Homographic Matrix
            panorama_img = self.__combineImages(img,panorama_img,HM)
        if save == True:
            cv2.imwrite("panorama.jpg",panorama_img)
        cv2.imshow("panorama.jpg",panorama_img)
        cv2.waitKey(10000)
        return panorama_img

    def __FindHomographicMatrix(self,img1,img2):
        img1 = np.asarray(img1,dtype = np.uint8)
        img2 = np.asarray(img2,dtype = np.uint8)
        sift = cv2.SIFT_create()
        matcher = cv2.FlannBasedMatcher_create()
        gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
        kp1,dp1 = sift.detectAndCompute(gray1,mask = None)
        kp2,dp2 = sift.detectAndCompute(gray2,mask = None)


        best_2 = matcher.knnMatch(  #return the list of best 2 matches keypoints e.g same angle,size,response/strength,pt coordinates
            queryDescriptors = dp1,
            trainDescriptors = dp2,
            k=2

        )

        ratio = 0.2
        match = []
        for m,n in best_2:
            if m.distance < ratio*n.distance: #Mask for most similiar points e.g same size , less size diffierence
                match.append(m)
        match = sorted(match,key=lambda x : x.distance) #Sort the match according to distance

        keypoints1 = np.array([kp1[m.queryIdx].pt for m in match])
        keypoints2 = np.array([kp2[m.trainIdx].pt for m in match])
        
        #Image 1 as the destination , Image 2 as the source
        src,dst = img2, img1
        src_kps , dst_kps = (keypoints2,keypoints1)
        H,status = cv2.findHomography(
            srcPoints = src_kps,
            dstPoints = dst_kps,
            method = cv2.USAC_ACCURATE,
            ransacReprojThreshold = 3
        )
        return H
    def __combineImages(self,img1,img2,h):
        rows1 , cols1 = img1.shape[:2]
        rows2, cols2 = img2.shape[:2]

        list_of_points_1 = np.float32([[0,0], [0, rows1],[cols1, rows1], [cols1, 0]]).reshape(-1, 1, 2)
        temp_points = np.float32([[0,0], [0,rows2], [cols2,rows2], [cols2,0]]).reshape(-1,1,2)

        #Warp perspective and change the field of view
        list_of_points_2 = cv2.perspectiveTransform(temp_points, h)

        list_of_points = np.concatenate((list_of_points_1,list_of_points_2), axis=0)

        [x_min, y_min] = np.int32(list_of_points.min(axis=0).ravel() - 0.5)
        [x_max, y_max] = np.int32(list_of_points.max(axis=0).ravel() + 0.5)
        
        translation_dist = [-x_min,-y_min]
        
        H_translation = np.array([[1, 0, translation_dist[0]], [0, 1, translation_dist[1]], [0, 0, 1]])

        output_img = cv2.warpPerspective(img2, H_translation.dot(h), (x_max-x_min, y_max-y_min))
        output_img[translation_dist[1]:rows1+translation_dist[1], translation_dist[0]:cols1+translation_dist[0]] = img1
        
        return output_img
    def pixelate(self,img_path,pixel_img_size): #e.g img_path = "./face.png",pixel_img_size = (20,20)
        img_path = img_path
        input = cv2.imread(img_path)
        i_h,i_w = input.shape[:2]
        o_h,o_w = pixel_img_size
        temp_image = cv2.resize(input,(o_w,o_h),interpolation=cv2.INTER_LINEAR)
        #compress image into pixelated size

        output = cv2.resize(temp_image,(i_w,i_h),interpolation=cv2.INTER_NEAREST)   
        return output
if __name__ == "__main__":
    img_tools = image_tools()
    img_tools.ConvertVideoToPanorama("wall_paint.MOV",save=False,steps=5) #Function 1: ConvertVideoToPanorama
    

