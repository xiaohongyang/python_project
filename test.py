import tkinter as tk
from tkinter import *
import tkinter.messagebox
 

class MyCheckButton(tk.Frame) :
	def __init__(self, master = None) :
		super().__init__( master)
		self.pack(expand = True)
		self.master.title ("")
		self.master.minsize(200,200)
		self.var = tk.IntVar()

		# cb = tk.Checkbutton(self, text="Show Title", variable = self.var, command = self.click)
		# cb.place(x = 150, y = 150)

		#cb.pack()
		# cb.place(x=50, y=56)

		self.init()

	def click(self):
		print('clicked')
		print(self.var.get())
		if self.var.get() == 1 :
			self.master.title("CheckButton")
		else :
			self.master.title("")

	def init(self):

		l_username = tk.Label(self, text="用户名").grid(row=0)
		entry_username = Entry(self, bd=1)
		entry_username.grid(row=0, column=1)


		l_password = Label(self, text="密码")
		l_password.grid(row=1)

		entry_password = Entry(self)
		entry_password.grid(row=1, column=1)

		btn_regist = Button(self, text="注册", command=self.register)
		btn_regist.grid(row=2)

		btn_submit = Button(self, text="登录");
		btn_submit.grid(row=2,column=2)

	def register(self):


		top = tk.Toplevel()

		l_username = Label(top, text="用户名")
		l_password = Label(top, text="密码")
		entry_username = Entry(top)
		entry_password = Entry(top)
		l_username.grid(row=0)
		entry_username.grid(row=0, column=1)
		l_password.grid(row=1)
		entry_password.grid(row=1, column=1)

		top.entry_username = entry_username

		btn_ok = Button(top, text="提交注册", command=lambda : self.doRegister(top))
		btn_ok.grid(row=2)

		#tk.messagebox.showinfo("username", "321")

	def doRegister(self,master):
		username = master.entry_username.get()
		tk.messagebox.showinfo("hello","username %s" % username)

if __name__ == "__main__" :
	root = tk.Tk()
	app = MyCheckButton(master = root)
	app.master.title("用户登录")
	app.mainloop()