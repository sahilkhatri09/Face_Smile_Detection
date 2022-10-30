
import cv2
from random import randrange

#LOADING TRAINED DATA
face_detector = cv2.CascadeClassifier('face_detector.xml')









 #1
#LOADING IMAGE
image_path = 'test_images/vk1.jpg'
img = cv2.imread(image_path)

#CONVERTING TO GRAYSCALE
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#DETECT FACES
face_coordinates = face_detector.detectMultiScale(grayscaled_img)

#DRAW GREEN RECTANGLE[S] AROUND THE PREDICTED FACE[S]
for face_coordinate in face_coordinates:
    (x, y, w, h)=face_coordinate
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

#SHOWING IMAGE
cv2.imshow('RDJ', img)
cv2.waitKey()










#  2
#LOADING WEBCAME STREAM
webcam = cv2.VideoCapture(0)
#PASS VIDEO PATH AS AN ARGUMENT TO ABOVE FUNCTION TO DETECT FACES IN LOCAL VIDEOS

#SAME THING ON WEBCAM
while True:
    is_frame_read_success, frame = webcam.read()
    grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_frame)
    for face_coordinate in face_coordinates:
        (x, y, w, h)=face_coordinate
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(255), randrange(255), randrange(255)), 2)
    cv2.imshow('WEBCAM', frame)
    key = cv2.waitKey(1)

    if(key==81 or key==113):
        break

webcam.release()


















face_detector = cv2.CascadeClassifier('face_detector.xml')
smile_detector = cv2.CascadeClassifier('smile_detector.xml')

# webcam = cv2.VideoCapture(0)

# while True:
#     successful_frame_read, frame = webcam.read()
#     if not successful_frame_read:
#         break
image_path = 'test_images/vk1.jpg'
img = cv2.imread(image_path)

#CONVERTING TO GRAYSCALE
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#DETECT FACES
face_coordinates = face_detector.detectMultiScale(grayscaled_img)
for face_coordinate in face_coordinates:
    (x, y, w, h)=face_coordinate
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    smiles = smile_detector.detectMultiScale(grayscaled_img, scaleFactor=1.7, minNeighbors=20)
    # for (x_smile, y_smile, w_smile, h_smile) in smiles:
    #     cv2.rectangle(img, (x_smile, y_smile), (x_smile+w_smile, y_smile+h_smile), (50, 50, 200), 3)
    if(len(smiles)>0):
        cv2.putText(img, 'smiling', (x, y+h+40), fontScale=3, fontFace=cv2.FONT_HERSHEY_PLAIN, color=(255, 255, 255))


cv2.imshow('smile detector', img)
key = cv2.waitKey()
