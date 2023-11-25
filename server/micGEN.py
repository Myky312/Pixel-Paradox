import speech_recognition as sr
import os

# Folder to store text files
mic_folder = "server/mic"
if not os.path.exists(mic_folder):
    os.makedirs(mic_folder)

def save_text_to_file(text, file_number):
    file_path = os.path.join(mic_folder, f"voice_{file_number}.txt")
    with open(file_path, "w") as file:
        file.write(text)

# Initialize recognizer
r = sr.Recognizer()

file_number = 1
while True:
    with sr.Microphone() as source:
        print("Please say the captcha:")
        audio = r.listen(source)

        try:
            # Using Google Web Speech API
            captcha_text = r.recognize_google(audio, language="en-US")
            processed_text = captcha_text.replace(" ", "").upper()  # Remove spaces and convert to uppercase
            save_text_to_file(processed_text, file_number)
            file_number += 1
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

    # The loop will break after each recognition; to continuously listen, remove the 'break' statement
    break
