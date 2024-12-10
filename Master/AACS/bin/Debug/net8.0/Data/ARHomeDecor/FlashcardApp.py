import tensorflow as tf
import speech_recognition as sr

model = tf.keras.models.load_model("flashcard_model.h5")

r = sr.Recognizer()

def recognize_speech():
    with sr.Microphone() as source:
        print("Say a word:")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

while True:
    word = recognize_speech()
    if word:
        # Process word and display corresponding flashcard
        print(f"You said: {word}")
        # ...