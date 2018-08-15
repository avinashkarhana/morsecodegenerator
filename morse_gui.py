from tkinter import *
root=Tk()
root.title("Morse Code Generator")
heading=Frame(root)
heading.pack(fill=BOTH)
lblhead = Label(heading,text="Morse Code Generator", font=("Times-New-Roman", 28))
lblhead.pack()
stringinp = Entry(root,font=("Helvetica", 28))
stringinp.pack(fill=BOTH)
stringinp.focus()
def pl():
    inp=stringinp.get()
    from morse_cli import playmorse
    playmorse(inp)
stringinp.bind('<Return>', lambda _: pl())
equal=Button(root,text="Play Morse Code",height = 2,command=pl)
equal.pack(side=BOTTOM,padx=5,pady=5)
root.mainloop()