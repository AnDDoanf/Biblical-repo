import tkinter as tk
from tkinter import *
from tkinter import ttk
from Recommender import Recommender

recommender = Recommender()
window = tk.Tk()
window.title("Bible verse recommender")
window.geometry('600x400')
window.resizable(False, False)

def onClick_submit():
    verse = entry.get()
    verses = recommender.recommend(verse=verse)
    myList.delete(0, END)
    if verses:
        for index, verse in enumerate(verses):
            myList.insert(END, verse)
    else: 
        myList.insert(END, "Invalid Input, please try again")

title_label = ttk.Label(master=window, text="Input your verse address", font='Calibri 36 bold')
title_label.pack()

scrollbar = Scrollbar(window)
scrollbar.pack(side="right", fill="y" )

input_frame = ttk.Frame(master=window)
input_frame.pack()

entry = ttk.Entry(master=input_frame, width=40, font=('Arial 16'))
entry.pack(padx=10, pady=10, side="left", expand=True)

button = ttk.Button(master=input_frame, text="Process", command=onClick_submit)
button.pack(padx=10, pady=10, side="right")

myList = Listbox(window, yscrollcommand=scrollbar.set, justify="center")
myList.pack(fill=BOTH, ipadx=20)
myList.config(font=('Arial 16'))
scrollbar.config(command=myList.yview)

window.mainloop()
