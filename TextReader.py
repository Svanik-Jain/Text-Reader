'''Modules we can use:

Word detector from github: https://github.com/githubharald/WordDetector

Pytesseract
'''


import PyPDF2
import pyttsx3

pdfFile = PyPDF2.PdfFileReader("jemh101.pdf")
TextToSpeech = pyttsx3.init()

pageNumber = int(input("Which page do you want to read? "))

Text = pdfFile.getPage(pageNumber).extract_text()

line = Text.split("\n")

TextToSpeech.say(f"{line[0]}")
TextToSpeech.runAndWait()
