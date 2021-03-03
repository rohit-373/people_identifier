import cv2
import face_recognition as fr
from pdf2image import convert_from_path

temp = []

images = convert_from_path("person's_details/hallticket.pdf", poppler_path='Release-21.02.0/poppler-21.02.0/Library/bin')
for i in range(len(images)):
    images[i].save(f'images/page{i}.jpg', 'JPEG')
    image = cv2.imread(f'images/page{i}.jpg', -1)
    cascade = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(cascade)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        try:
            cv2.imwrite('images/hallticket.jpg', image[y - 30:y + h + 30, x - 30:x + w + 30])
        except:
            continue

images = convert_from_path("person's_details/collegeid.pdf", poppler_path='Release-21.02.0/poppler-21.02.0/Library/bin')
for i in range(len(images)):
    images[i].save(f'images/page{i}.jpg', 'JPEG')
    image = cv2.imread(f'images/page{i}.jpg', -1)
    cascade = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(cascade)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        try:
            cv2.imwrite('images/collegeid.jpg', image[y - 30:y + h + 30, x - 30:x + w + 30])
        except:
            continue

images = convert_from_path("person's_details/interview.pdf", poppler_path='Release-21.02.0/poppler-21.02.0/Library/bin')
for i in range(len(images)):
    images[i].save(f'images/page{i}.jpg', 'JPEG')
    image = cv2.imread(f'images/page{i}.jpg', -1)
    cascade = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(cascade)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    j = 0
    for (x, y, w, h) in faces:
        j += 1
        try:
            cv2.imwrite(f'images/face{j}.jpg', image[y - 30:y + h + 30, x - 30:x + w + 30])
            temp.append(f'face{j}.jpg')
        except:
            continue

hallticket_image = cv2.imread("images/hallticket.jpg")
hallticket_image = cv2.cvtColor(hallticket_image, cv2.COLOR_BGR2RGB)
hallticket_image_encoding = fr.face_encodings(hallticket_image)

collegeid_image = cv2.imread("images/collegeid.jpg")
collegeid_image = cv2.cvtColor(collegeid_image, cv2.COLOR_BGR2RGB)
collegeid_image_encoding = fr.face_encodings(collegeid_image)

if fr.compare_faces(hallticket_image_encoding, collegeid_image_encoding)[0]:
    for i in temp:
        unknown_image = cv2.imread(i)
        unknown_image = cv2.cvtColor(unknown_image, cv2.COLOR_BGR2RGB)
        unknown_encoding = fr.face_encodings(unknown_image)[0]

        results = fr.compare_faces(hallticket_image_encoding, unknown_encoding)[0]
        if results:
            print(i[:-4], 'is matching')
        else:
            print(i[:-4], 'is not matching')
else:
    print(i[:-4], 'is not matching')
