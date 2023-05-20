# # DEPENDENCIES
# from PyPDF2 import PdfReader
# import signal
# import pyttsx3
# from tkinter import *
# from tkinter import filedialog as fd

# # VARIABLES
# TextToSpeech = pyttsx3.init()
# TextToSpeech.setProperty("rate", 150)  # Slows down speed of dictator
# stop = False
# dictionary = {}
# i = 0
# reread = ''
# AskPath = Tk()

# TextToSpeech.say("Select PDF")
# TextToSpeech.runAndWait()

# AskPath.withdraw()
# file_path = fd.askopenfilename(
#     title="SELECT PDF",
#     filetypes=(("PDF files", "*.pdf"),)
#     )
# AskPath.destroy()
# AskPath.mainloop()
# reread = ''

# reader = PdfReader(file_path)

# # THIS FUNCTION WILL ALLOW AS TO END THE CODE BY PRESSING CTRL+C
# def stopTheCode(signal,frame):
#     global stop
#     stop = True
# signal.signal(signal.SIGINT, stopTheCode)

# TextToSpeech.say("Which page number do you want to read?")
# TextToSpeech.runAndWait()
# page = reader.pages[int(input("Which page number do you want to read: "))-1]

# Text = page.extract_text()
# lines = Text.split("\n")

# for line in lines:
#     TextToSpeech.say(line)
#     TextToSpeech.runAndWait()
#     if(stop):
#         break

# for num in lines:
#     i += 1
#     dictionary[i] = num
# print(dictionary)

# while reread != 'none':
#     TextToSpeech.say("Which line do you want me to repeat?")
#     TextToSpeech.runAndWait()
#     reread = input('Which line do you want me to repeat?')
#     for number,sentence in list(dictionary.items()):
#         if reread.lower() in sentence.lower():
#             try:
#                 TextToSpeech.say("I'll repeat."+"\n"+dictionary[number]+dictionary[number+1])
#                 TextToSpeech.runAndWait()
#                 TextToSpeech.say("Do you want me to read further?")
#                 TextToSpeech.runAndWait()
#                 readon =input("Do you want me to read further?")
#                 #print(readon)
#                 if  readon == "yes":
#                     TextToSpeech.say("I'll repeat."+"\n"+dictionary[number + 2]+dictionary[number+3])
#                     TextToSpeech.runAndWait()
#                 elif readon == "no":
#                     TextToSpeech.say("Ok")
#                     TextToSpeech.runAndWait()
#                 else:
#                     TextToSpeech.say("Reply in yes or no")
#                     TextToSpeech.runAndWait()
#             except:
#                 TextToSpeech.say("I'll repeat."+"\n"+dictionary[number])
#                 TextToSpeech.runAndWait()


# else:
#     TextToSpeech.say("Thank you for using Text Dictator")
#     TextToSpeech.runAndWait()



# DEPENDENCIES
from PyPDF2 import PdfReader
import signal
import pyttsx3
from tkinter import *
from tkinter import filedialog as fd
import speech_recognition as sr

# VARIABLES
TextToSpeech = pyttsx3.init()
TextToSpeech.setProperty("rate", 150)  # Slows down speed of dictator
stop = False
dictionary = {}
i = 0
reread = ''
AskPath = Tk()
r= sr.Recognizer()
gotpage = 'notgot'
reread = ''
stoploop = True
gotpage = 'notgot'
reread = ''

#Opens window to select PDF file
TextToSpeech.say("Select PDF")
TextToSpeech.runAndWait()

AskPath.withdraw()
file_path = fd.askopenfilename(
    title="SELECT PDF",
    filetypes=(("PDF files", "*.pdf"),)
    )
AskPath.destroy()
AskPath.mainloop()

reader = PdfReader(file_path)

# THIS FUNCTION WILL ALLOW AS TO END THE CODE BY PRESSING CTRL+C
def stopTheCode(signal,frame):
    global stop
    stop = True
signal.signal(signal.SIGINT, stopTheCode)

def repeat():
    global reread
    global stoploop
    stoploop = True
    while stoploop:
        TextToSpeech.say("Which line do you want me to repeat?")
        TextToSpeech.runAndWait()
        reread = input('Which line do you want me to repeat?')
        for number,sentence in list(dictionary.items()):
            if reread.lower() in sentence.lower():
                try:
                    TextToSpeech.say("I'll repeat."+"\n"+dictionary[number]+dictionary[number+1])
                    TextToSpeech.runAndWait()
                    TextToSpeech.say("Do you want me to read further?")
                    TextToSpeech.runAndWait()
                    readon =input("Do you want me to read further?")
                    if  readon == "yes":
                        TextToSpeech.say("I'll repeat."+"\n"+dictionary[number + 2]+dictionary[number+3])
                        TextToSpeech.runAndWait()
                    elif readon == "no":
                        TextToSpeech.say("Ok")
                        TextToSpeech.runAndWait()
                    else:
                        TextToSpeech.say("Reply in yes or no")
                        TextToSpeech.runAndWait()
                except:
                    TextToSpeech.say("I'll repeat."+"\n"+dictionary[number])
                    TextToSpeech.runAndWait()

while True:
    TextToSpeech.say("Speak the page number you want me to read")
    TextToSpeech.runAndWait()
    page = reader.pages[(int(input("Enter the Page number you want me to read: ")))-1]
    text = page.extract_text()
    #print(text)
    lines = text.split("\n")
    for line in lines:
        TextToSpeech.say(line)
        TextToSpeech.runAndWait()
        if(stop):
            break

    TextToSpeech.say("Do you want me to repeat?")
    TextToSpeech.runAndWait()
    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)

    while True:
        if r.recognize_google(audio) == "Yes" or "yes":
            for num in lines:
                i += 1
                dictionary[i] = num
                print(dictionary)

            repeat()  
            
        elif r.recognize_google(audio) == "no" or "No":
            TextToSpeech.say("Ok... No Problem. Thank You for using me")
            TextToSpeech.runAndWait()
            break
    TextToSpeech.say("Ok... No Problem. Thank You for using Text Dictator")
    TextToSpeech.runAndWait()
    break
