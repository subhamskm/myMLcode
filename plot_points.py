import speech_recognition as sr
import matplotlib.pyplot as plt
import os

def plot(u,v):
   plt.plot(u,v)
   plt.show()
   

r=sr.Recognizer()
with sr.Microphone() as source:
    print ("Say the line \'plot the points _, _ and _, _ and _, _\' with the corressponding points replacing _: ")
    audio = r.listen(source)

try:
    str=r.recognize_google(audio)
    s=str.split()
    x=int(s[3][0:-1])
    y=int(s[4])
    a=int(s[6][0:-1])
    b=int(s[7])
    msg1="plotting the points and opening ImageViewer.."
    os.system('echo '+msg1+' | festival --tts')
    plot([ x, a, int(s[9][0:-1]) ],[ y, b, int(s[10]) ])
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service;{0}".format(e))   
