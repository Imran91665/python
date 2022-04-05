import pyttsx3
say = pyttsx3.init()
text = input("Tell something: ")
say.setProperty("rate", 100) #voice speed er jonno
voices = say.getProperty("voices") #voice change er jonno
say.setProperty("voice", voices[1].id) #index e 0 and 1 use korte hobe
say.say(text)
say.runAndWait()
