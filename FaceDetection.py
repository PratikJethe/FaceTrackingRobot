import numpy as np
import cv2
import requests



data = ""
ForwardLimit = 0
BackwardLimit= 0
firstime = True

url="http://192.168.0.106:8080/shot.jpg"#URL OF IP web cam
face_cascade=cv2.CascadeClassifier(r'C:\Users\prati\Desktop\py project\FaceBot\venv\Lib\site-packages\cv2\data\haarcascade_frontalface_alt2.xml')


def makeurl(direction):#TO SEND GET REQUEST TO ESP-32 WEBSERVER
    url1 = "http://192.168.0.112/"+ direction #URL WHERE REQUEST WILL BE MADE
    try:
        requests.get(url1)
    except:
        print("OK")#AS ESP32 SERVER IS NOT SENDING RESPONSE,

while True:

    try:
    #print("waiting 3")
        img_resp = requests.get(url)#requesting image from ipwebcam url
        img_arr = np.array(bytearray(img_resp.content),dtype=np.uint8)#converting it into np array
        img = cv2.imdecode(img_arr,-1)

        width,height = img.shape[1], img.shape[0]#getting height and width
        #print(width, height)
        ################################################
        ##<<<---Face Detection And Constructing Frame Around Face--->>>
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=2, minNeighbors=5)
        cv2.rectangle(img, (320 - 60, 240 - 60), (320 + 60, 240 + 60), color=(0, 0, 255))
        cv2.rectangle(img, (320 - 60, 0), (320 + 60, 480), color=(0, 0, 255))
        cv2.circle(img, (320, 240), 60, (0, 255, 0), 2)
        # # cv2.imshow('IP Camera stream', frame)
        #print(len(faces))

        for (x, y, h, w) in faces:
            #print(x, y, h, w)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
            color = (255, 0, 0)
            stroke = 2
            end_chord_x = x + w
            end_chord_y = y + h


            cv2.rectangle(img, (x, y), (end_chord_x, end_chord_y), color, stroke)
            Area = (x+w)*(y+h)
            cv2.putText(img, str(Area), (100, 100), fontFace=cv2.FONT_ITALIC, fontScale=1, color=(255, 120, 120),thickness=2)
            cx= int(x+(w/2))
            cy = int(y+(h/2))
            cv2.circle(img,(cx,cy), 20,(255, 130, 130), 2)
            #print(Area)

            #forwardbackward()
            #<<<<---------------CO-ORDINATE CHECKING CONDITIONS-------------->>#

            if(len(faces)!=0):
                if (cx<260):
                    print("MOVE LEFT")
                    makeurl("left")

                    #movLeft(data)q
                if (cx>380):
                    print("MOVE RIGHT")
                    makeurl("right")
                else:

                     print("CENTERED")
                     makeurl("center")



            else:
                if(firstime==True):
                    print("Searching")
                    makeurl("search")
                    firstime==False
                else:
                    makeurl("stop")

    except:
        print("IP Web Cam Closed")
        break

    cv2.imshow("cam", img)
    if cv2.waitKey(1)==27:

        break
