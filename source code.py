#Major Project

from tkinter import *

#Encrypt function

def encrypt():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    newMessage = ''
    message = textentry1.get()#This collects the content of the text
    try:
        key = int(textentry2.get())#This collects the key
    except ValueError:
        popupmsg("Enter a key value first, then click Encrpyt", "KEY VALUE MISSING")
        print("Enter a key value first")
        return
    
    for character in message:
      if character in alphabet:
        position = alphabet.find(character)
        newPosition = (position + key) % 26
        newCharacter = alphabet[newPosition]
        newMessage += newCharacter
      else:
        newMessage += character

    output.delete(0.0,END)
    output.insert(INSERT,newMessage)
    
def decrypt():
    newMessage = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ciphertext = textentry1.get()#This collects the content of the text
    try:
        key = int(textentry2.get())#This collects the key
    except ValueError:
        popupmsg("Enter a key value first, then click Decrypt", "KEY VALUE MISSING")
        print("Enter a key value first")
        return
    
    for l in ciphertext:
        try:
            i = (alphabet.index(l) - key) % 26
            newMessage += alphabet[i]
        except ValueError:
            newMessage += l
            
    output.delete(0.0,END)
    output.insert(INSERT,newMessage)

#Popup message function
def popupmsg(msg, title):
            popup = Tk()
            popup.wm_title(title)
            label = Label(popup, text=msg, font="none 12")
            label.pack(side="top", fill="x", pady=10)
            button = Button(popup, text="OK...", pady=3, command = popup.destroy)
            button.pack()
            popup.mainloop()

#Clear function
    
def clear():
    output.delete(0.0, END)
    textentry1.delete(0, END)
    textentry2.delete(0, END)

#exit function
    
def close_window():
    window.destroy()
    exit

##### main:
window = Tk()
window.title("Ceaser encryptor")
window.configure(background="white")

#label(s)

Label (window, text="Enter the word you want to encrypt or decrypt:", bg="white", fg="black", font="none 12 bold") .grid(row=1, column=0, sticky=W)

Label (window, text="Enter the key(1-25):", bg="white", fg="black", font="none 12 bold") .grid(row=2, column=0, sticky=W)

Label (window, text="\nOutput:", bg="white", fg="black", font="none 12 bold") .grid(row=4, column=0, sticky=W)

#text entry box

textentry1 = Entry(window, width=50, bg="white")
textentry1.grid(row=1, column=1, sticky=W)

textentry2 = Entry(window, width=15, bg="white")
textentry2.grid(row=2, column=1, sticky=W)

#encrypt button

Button(window, text="ENCRYPT", width=7, command=encrypt) .grid(row=3, column=0, sticky= W)

#decrypt button

Button(window, text="DECRYPT", width=7, command=decrypt) .grid(row=3, column=1, sticky= W)

#clear button

Button(window, text="CLEAR", width=7, command=clear) .grid(row=3, column=2, sticky= W)

#text box for output

output = Text(window, width=75, height=6, wrap=WORD, background="white")
output.grid(row=12, column=0, columnspan=2, sticky=W)

#exit button

Button(window, text="EXIT", width=14, command=close_window) .grid(row=10, column=0, sticky=W)

    
#####run the main loop
window.mainloop()
