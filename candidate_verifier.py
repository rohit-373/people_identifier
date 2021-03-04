import os
import cv2
import face_recognition as fr
from pdf2image import convert_from_path

temp = []
results = 0
f = open("candidate.txt", "a")
entries = os.listdir("details")
college_id_image_encoding = None
hall_ticket_image_encoding = None
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

for candidate_name in entries:
    pages = convert_from_path(f"details/{candidate_name}/hall_ticket.pdf")
    for index, page in enumerate(pages):
        page.save(f"details/{candidate_name}/page.jpg", "JPEG")
        img = cv2.imread(f"details/{candidate_name}/page.jpg", 0)
        for (x, y, w, h) in face_cascade.detectMultiScale(img, 1.3, 5):
            try:
                hall_ticket_image = cv2.cvtColor(img[y - 30:y + h + 30, x - 30:x + w + 30], cv2.COLOR_GRAY2RGB)
                hall_ticket_image_encoding = fr.face_encodings(hall_ticket_image)
                cv2.imwrite(f"details/{candidate_name}/hall_ticket.jpg", hall_ticket_image)
            except:
                continue

    pages = convert_from_path(f"details/{candidate_name}/college_id.pdf")
    for index, page in enumerate(pages):
        page.save(f"details/{candidate_name}/page.jpg", "JPEG")
        img = cv2.imread(f"details/{candidate_name}/page.jpg", 0)
        for (x, y, w, h) in face_cascade.detectMultiScale(img, 1.3, 5):
            try:
                college_id_image = cv2.cvtColor(img[y - 30:y + h + 30, x - 30:x + w + 30], cv2.COLOR_GRAY2RGB)
                college_id_image_encoding = fr.face_encodings(college_id_image)[0]
                cv2.imwrite(f"details/{candidate_name}/college_id.jpg", college_id_image)
            except:
                continue

    if fr.compare_faces(hall_ticket_image_encoding, college_id_image_encoding)[0]:
        pages = convert_from_path(f"details/{candidate_name}/interview.pdf")
        for index, page in enumerate(pages):
            page.save(f"details/{candidate_name}/page.jpg", "JPEG")
            img = cv2.imread(f"details/{candidate_name}/page.jpg", 0)
            for i, (x, y, w, h) in enumerate(face_cascade.detectMultiScale(img, 1.3, 5)):
                try:
                    unknown_image = cv2.cvtColor(img[y - 30:y + h + 30, x - 30:x + w + 30], cv2.COLOR_GRAY2RGB)
                    unknown_encoding = fr.face_encodings(unknown_image)[0]
                    cv2.imwrite(f"details/{candidate_name}/interview_faces_{i + 1}.jpg", unknown_image)
                    results += fr.compare_faces(hall_ticket_image_encoding, unknown_encoding)[0]
                except:
                    continue

        f.write(', '.join([candidate_name, 'True', str(bool(results))]) + '\n')
    else:
        f.write(', '.join([candidate_name, 'False', 'NA']) + '\n')
    os.remove(f"details/{candidate_name}/page.jpg")

f.close()
