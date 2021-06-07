""" code pour faire des acquisitions avec un time lapse"""
# importer les bibliothéques nécessaire pour le temps , le répertoire et la lecture des caméras
# cv2 pour lecture des cameras, time pour définir l'interval de temps pour chaque acquisition
# os et os.path pour créer le répertoire le fichier dans le lequel les images seront enregistrées
import os, os.path
import cv2
import time

# Lecture de la caméra
camera = cv2.VideoCapture(0)
Interval = 10
while True:
        ret, frame = camera.read()
        path="./Bureau/Imagetest"
        if ret:
            cv2.imshow('image',frame)
            cv2.imwrite(os.path.join(path, "tournesol" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".png"), cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            time.sleep(Interval)
            
        if cv2.waitKey(1) & 0xFF == ord('t'):
            break
        
        
camera.release()
cv2.destroyAllWindows()
    
            
