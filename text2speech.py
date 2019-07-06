import pyttsx3
import tkinter as tk
engine=pyttsx3.init()
class Widget():
    def __init__(self):
        self.root=tk.Tk()
        self.root.title("text to speech")
        self.root.resizable(0,0)
        self.label=tk.Label(self.root,text="what do you want to speak ?")
        self.label.pack()
        self.entry=tk.Entry(self.root)
        self.entry.pack()
        self.button=tk.Button(self.root,text="Speak",command=self.clicked)
        self.button.pack()
        self.root.mainloop()
    def speak(self,text):
        engine.say(text)
        engine.runAndWait()
    def clicked(self):
        text=self.entry.get()
        self.speak(text)
if __name__=='__main__':
    widget=Widget()

