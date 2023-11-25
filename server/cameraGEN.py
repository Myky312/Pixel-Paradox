import cv2
import pytesseract
import os

# Configure Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path

# Folder to store text files
cam_folder = 'server/cam'
if not os.path.exists(cam_folder):
    os.makedirs(cam_folder)

def save_text_to_file(text, file_number):
    file_path = os.path.join(cam_folder, f"text_{file_number}.txt")
    with open(file_path, "w") as file:
        file.write(text)

# Initialize camera
cap = cv2.VideoCapture(0)

file_number = 1
previous_text = ""
roi_start = (100, 100)
roi_end = (400, 400)

while True:
    ret, frame = cap.read()
    roi = frame[roi_start[1]:roi_end[1], roi_start[0]:roi_end[0]]

    # Image preprocessing for better OCR
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # OCR on the processed image
    current_text = pytesseract.image_to_string(thresh).strip()

    if current_text and current_text != previous_text:
        print(f"Recognized Text: {current_text}")
        save_text_to_file(current_text, file_number)
        file_number += 1
        previous_text = current_text

    cv2.rectangle(frame, roi_start, roi_end, (0, 255, 0), 2)
    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
