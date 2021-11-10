import pyttsx3 
import PyPDF2
import os
book = open('Scienceofscience.pdf', 'rb') 
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages



speaker = pyttsx3.init()
speaker.setProperty('rate',140)
for p in range(2,pages):
    eachpage = pdfreader.getPage(p)
    text = eachpage.extractText()
    speaker.say(text)
    speaker.runAndWait()