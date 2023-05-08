from PyPDF2 import PdfReader

import pyttsx3

reader = PdfReader("C Programming Book.pdf")


TextToSpeech = pyttsx3.init()


TextToSpeech.say("which page number do you want?")
TextToSpeech.runAndWait()
page = reader.pages[int(input("which page number do you want?"))-1]


Text = page.extract_text()
line = Text.split("\n")
print(Text)


dictionary = {}
i = 0
for num in line:
    i += 1
    dictionary[i] = num
#print(dictionary)
    

TextToSpeech.setProperty("rate", 150)  #slows down speed of dictator
TextToSpeech.say(Text)
TextToSpeech.runAndWait()


reread = ''
while reread != 'none':
    TextToSpeech.say("Which line do you want me to repeat?")
    TextToSpeech.runAndWait()
    reread = input('Which line do you want me to repeat?')
    for number,sentence in list(dictionary.items()):
        if reread in sentence:
            try:
                TextToSpeech.say("I'll repeat."+"."+"."+"."+"."+"."+"."+"."+dictionary[number]+dictionary[number+1])
                TextToSpeech.runAndWait()
                TextToSpeech.say("Do you want me to read further?")
                TextToSpeech.runAndWait()
                readon =input("Do you want me to read further?")
                #print(readon)
                if  readon == "yes":
                    TextToSpeech.say("I'll repeat."+"."+"."+"."+"."+"."+"."+"."+dictionary[number + 2]+dictionary[number+3])
                    TextToSpeech.runAndWait()
                elif readon == "no":
                    TextToSpeech.say("Ok")
                    TextToSpeech.runAndWait()
                else:
                    TextToSpeech.say("Reply in yes or no")
                    TextToSpeech.runAndWait()
            except:
                TextToSpeech.say("I'll repeat."+"."+"."+"."+"."+"."+"."+"."+dictionary[number])
                TextToSpeech.runAndWait()

else:
    TextToSpeech.say("Thank you for using Text Dictator")
    TextToSpeech.runAndWait()
