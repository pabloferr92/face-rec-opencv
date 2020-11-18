from domain.model.user_model import arr_users




def FaceRecognize(username):
    if len(arr_users)>0:
        for u in arr_users:
            if username == u.username:
                print('achei')
                cont = 0
                while(cont<=5):
                    print("Tentativa 1 de 5 para reconhecer ")
                    _, frame = cap.read()
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                    for (x,y,w,h) in faces:
                        image_save = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                        roi_gray = gray[y:y+h, x:x+w]
                        roi_color = frame[y:y+h, x:x+w]
                        eyes = eye_cascade.detectMultiScale(roi_gray)
                        for (ex,ey,ew,eh) in eyes:
                            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                    if image_save == u.foto:
                        print("usuário reconhecido : {}". format(u['username']))
                        try_face_detect = False
                        cap.release()

                    cont = cont +1
            else:
                print("usuário nao localizado")
    else:
        print("não há usuários registrados")
					