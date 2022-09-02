from tkinter import *
from PyDictionary import PyDictionary
#Create Window User interface
root = Tk()
root.geometry('250x200')

# Defining the meaning of the word
def find_meaning():
    word = ent.get()
    dictionary = PyDictionary(word)
    meaning = dictionary.printMeanings()
    print(meaning)

ent= Entry(root, font=("times", 15, "bold"))
ent.grid(row=2,column=2)
btn= Button(root,text="find meaning",command=find_meaning)
btn.grid(row=1,column=2)

root.mainloop()


