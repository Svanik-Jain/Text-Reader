# DEPENDENCIES
from PyPDF2 import PdfReader
import signal
import pyttsx3
from tkinter import *
from tkinter import filedialog as fd

# VARIABLES
TextToSpeech = pyttsx3.init()
TextToSpeech.setProperty("rate", 150)  # Slows down speed of dictator
stop = False
AskPath = Tk()
AskPath.withdraw()
file_path = fd.askopenfilename(
    title="SELECT PDF",
    filetypes=(("PDF files", "*.pdf"),)
    )
AskPath.destroy()
AskPath.mainloop()
reread = ''

reader = PdfReader(file_path)

# THIS FUNCTION WILL ALLOW AS TO END THE CODE BY PRESSING CTRL+C
def stopTheCode(signal,frame):
    global stop
    stop = True
signal.signal(signal.SIGINT, stopTheCode)

TextToSpeech.say("Which page number do you want to read?")
TextToSpeech.runAndWait()
page = reader.pages[int(input("Which page number do you want to read: "))-1]

Text = page.extract_text()
lines = Text.split("\n")

for line in lines:
    TextToSpeech.say(line)
    TextToSpeech.runAndWait()
    if(stop):
        break

dictionary = {}
i = 0
for num in lines:
    i += 1
    dictionary[i] = num
print(dictionary)


while reread != 'none':
    TextToSpeech.say("Which line do you want me to repeat?")
    TextToSpeech.runAndWait()
    reread = input('Which line do you want me to repeat?')
    for number,sentence in list(dictionary.items()):
        if reread in sentence:
            try:
                TextToSpeech.say("I'll repeat."+"\n"+dictionary[number]+dictionary[number+1])
                TextToSpeech.runAndWait()
                TextToSpeech.say("Do you want me to read further?")
                TextToSpeech.runAndWait()
                readon =input("Do you want me to read further?")
                #print(readon)
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
    if(stop):
        break

else:
    TextToSpeech.say("Thank you for using Text Dictator")
    TextToSpeech.runAndWait()
