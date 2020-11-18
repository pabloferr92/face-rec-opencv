import sys, os
path =os.path.abspath("../../")
sys.path.append(path)

print(sys.path)

from domain.logic.face_capture import FaceCapture
from domain.logic.face_recognize import FaceRecognize

# from domain.model.user_model import User

import numpy as np
import cv2

## Parametro 0 irá abrir a webcam 

## Para câmera ip utilizar cv2.VideoCapture("rtsp://endereço")
cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

while(True):
	try_face_detect = True

	users = []

	option = int(input("Digite 1 para reconhecer e 2 para capturar: "))
	if option == 2:
		##inserir funcão para capturar
		username = input("Digite seu nome: ")
		FaceCapture(username)




	if option == 1:
		username = input("Digite seu nome para reconhecer: ")
		FaceRecognize(username)
		

cap.release()
cv2.destroyAllWindows()



