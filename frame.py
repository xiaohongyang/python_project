from tkinter import *

root = Tk()

topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side='bottom')

button01 = Button(topFrame, text="button01", fg='red')
button02 = Button(topFrame, text="button02", fg='yellow')
button03 = Button(topFrame, text="button03", fg='green')
button04 = Button(bottomFrame, text="button04", fg='blue')

button01.pack(side='left')
button02.pack(side='left')
button03.pack(side='left')
button04.pack()

root.mainloop()