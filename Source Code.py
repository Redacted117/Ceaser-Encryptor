#Major Project
#Made by Sampad Banerjee, please give credit if you use it. Thank you.

from tkinter import *

#Encrypt function

def click():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    newMessage = ''
    message = textentry1.get()#This collects the content of the text
    key = int(textentry2.get())#This collects the key
    
    for character in message:
      if character in alphabet:
        position = alphabet.find(character)
        newPosition = (position + key) % 26
        newCharacter = alphabet[newPosition]
        newMessage += newCharacter
      else:
        newMessage += character
    
    output.insert(INSERT,newMessage)

#Clear function
    
def clear():
    output.delete(0.0, END)

#exit function
    
def close_window():
    window.destroy()
    exit

##### main:
window = Tk()
window.title("Ceaser encryptor")
window.configure(background="white")

#label(s)

Label (window, text="Enter the word you want to encrypt:", bg="white", fg="black", font="none 12 bold") .grid(row=1, column=0, sticky=W)

Label (window, text="Enter the key for encryption(1-25):", bg="white", fg="black", font="none 12 bold") .grid(row=2, column=0, sticky=W)

Label (window, text="\nOutput:", bg="white", fg="black", font="none 12 bold") .grid(row=4, column=0, sticky=W)

#text entry box

textentry1 = Entry(window, width=50, bg="white")
textentry1.grid(row=1, column=1, sticky=W)

textentry2 = Entry(window, width=15, bg="white")
textentry2.grid(row=2, column=1, sticky=W)

#submit button

Button(window, text="ENCRYPT", width=7, command=click) .grid(row=3, column=0, sticky= W)

#clear button

Button(window, text="Clear", width=7, command=clear) .grid(row=3, column=2, sticky= W)

#text box for output

output = Text(window, width=75, height=6, wrap=WORD, background="white")
output.grid(row=5, column=0, columnspan=2, sticky=W)

#exit button

Button(window, text="EXIT", width=14, command=close_window) .grid(row=7, column=0, sticky=W)

    
#####run the main loop
window.mainloop()
