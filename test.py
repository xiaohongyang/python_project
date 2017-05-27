from tkinter   import  Frame, IntVar
 

class MyCheckButton(Frame) :
	def __init__(self, mastr = None) :
		Frame.init( self, master)
		self.pack(expand = True, fill = BOTH)
		self.master.title ("")
		self.master.minsize(200,200)
		self.var = IntVar()

		cb = Checkbutton(self, text="Show Title", variable = self.var, command = self.click)
		cb.place(x = 50, y = 50)

	def click(self):
		if self.var.get() == 1 :
			self.master.title = "CheckButton"
		else :
			self.master.title = ""


if __name__ == "__main__" :
	MyCheckButton().mainloop()