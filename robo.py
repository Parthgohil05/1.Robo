import pyttsx3

if __name__=="__main__":
    text_speech = pyttsx3.init()
    while True:
        answer = input("What you want to speak??")
        text_speech.say(answer)
        text_speech.runAndWait()
    