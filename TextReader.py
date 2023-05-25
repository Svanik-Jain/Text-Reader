 # DEPENDENCIES
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
TextToSpeech.setProperty("rate", 150)  # SLOWS DOWN SPEED OF READER
stop = False
dictionary = {}
i = 0
reread = ''
AskPath = Tk()
r= sr.Recognizer()
reread = ''
stoploop = True

# OPENS FILE DIALOG TO SELECT PDF
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

# FUNCTION TO REPEAT LINES
def repeat():
    global reread
    global stoploop
    stoploop = True
    while stoploop:
        TextToSpeech.say("Which line do you want me to repeat?")
        TextToSpeech.runAndWait()
        with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print("Listening...")
                audio = r.listen(source)
        reread = r.recognize_google(audio)
        reread = reread.lower()
        if reread == 'none' or reread == 'no' or reread == 'stop':
                print("You said, "+reread)
                stoploop = False
        else:
            global readon
            readon = 'yes'
            for number,sentence in list(dictionary.items()):
                if reread.lower() in sentence.lower() and readon == 'yes':
                    try:
                        print("You said, "+reread)
                        TextToSpeech.say("I'll repeat."+"\n"+dictionary[number]+dictionary[number+1])
                        TextToSpeech.runAndWait()
                        TextToSpeech.say("Do you want me to read further?")
                        TextToSpeech.runAndWait()
                        with sr.Microphone() as source:
                            r.adjust_for_ambient_noise(source)
                            print("Listening...")
                            audio = r.listen(source)
                        readon = r.recognize_google(audio)
                        if  readon == "yes":
                            print("You said, yes")
                            TextToSpeech.say("I'll repeat."+"\n"+dictionary[number + 2]+dictionary[number+3])
                            TextToSpeech.runAndWait()
                            readon = "no"
                        elif readon == "no":
                            print("You said, no")
                            TextToSpeech.say("Ok")
                            TextToSpeech.runAndWait()
                        else:
                            print("You said, "+readon)
                            TextToSpeech.say("Please reply in yes or no")
                            TextToSpeech.runAndWait()
                    except:
                        TextToSpeech.say("I'll repeat."+"\n"+dictionary[number])
                        TextToSpeech.runAndWait()
global readpages
readpages = True
while readpages:
    global gotpage
    gotpage = 'notgot'
    while gotpage == 'notgot':
        TextToSpeech.say("Speak the page number you want me to read")
        TextToSpeech.runAndWait()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = r.listen(source)
            heard = r.recognize_google(audio)
        if heard == 'none' or heard == 'no' or heard == 'stop':
            readpages = False
            break
        else:        
            try:
                global page
                if heard.lower() == 'tu' or heard.lower() == 'do':
                    heard = 2
                    page = reader.pages[int(heard)-1] 
                    text = page.extract_text()
                    print('You said,',heard)
                    gotpage = 'got'
                elif heard == 'free' or heard == 'tree':
                    heard = 3
                    page = reader.pages[int(heard)-1] 
                    print('You said,',heard)
                    gotpage = 'got'
                elif heard == 'no':
                        TextToSpeech.say("Ok")
                        TextToSpeech.runAndWait() 
                elif int(heard) < len(reader.pages):
                    page = reader.pages[int(heard)-1] 
                    print('You said,',heard)
                    gotpage = 'got'
                else:
                    TextToSpeech.say("Looks like you said a page that does not exist in the PDF.")
                    TextToSpeech.runAndWait()
                    print('You said,',heard)
                    gotpage = 'notgot'
            except:
                TextToSpeech.say("Please say a number")
                TextToSpeech.runAndWait()
                print('You said,',heard)
    TextToSpeech.say("Do you want me to repeat two words at a time?")
    TextToSpeech.runAndWait()
    with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = r.listen(source)
            heard = r.recognize_google(audio)
    if heard == "yes":
        print("You said 'yes'")
 #FUNCTION TO DICTATE
        splitted_words = text.split()
        if len(splitted_words)%2 == 1:
            splitted_words += ' '
        word_pairs = {}
        p = 0
        list_pairs = []

        for word in splitted_words:
            p += 1
            if p % 2 == 1:
                list_pairs.append(word)
                print(list_pairs)
            else:
                list_pairs.append(word)
                print(list_pairs)
                word_pairs[p//2] = list_pairs
                list_pairs = []

        def repeatwice(dictionary):
            for number,pair in dictionary.items():
                TextToSpeech.say(pair[0])
                TextToSpeech.runAndWait()
                TextToSpeech.say(pair[1])
                TextToSpeech.runAndWait()
                TextToSpeech.say(pair[0])
                TextToSpeech.runAndWait()
                TextToSpeech.say(pair[1])
                TextToSpeech.runAndWait()
                if (stop):
                    break
        if input("Do you want me to dictate?: (yes or no)").lower() == 'yes':
            TextToSpeech.setProperty("rate", 200)  
            repeatwice(word_pairs)
        else:
            print("You said 'no'")

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

    while stoploop:
        repet = r.recognize_google(audio).lower()
        if repet == "yes":
            print("You said, "+repet)
            for num in lines:
                i += 1
                dictionary[i] = num
            print(dictionary)
            repeat()         #something may be wrong here
        elif repet == "no":
            print("You said, "+repet)
            break
    TextToSpeech.say("Ok")
    TextToSpeech.runAndWait()
TextToSpeech.say("No Problem. Thank You for using Text Dictator")
TextToSpeech.runAndWait()
