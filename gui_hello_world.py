#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter as tk
 

class LogForm(tk.Frame) :
	def __init__(self, master=  None):
		super().__init__(master)
		
		self.pack()
		self.create_widget()


	def create_widget(self):

		self.height = 300

		 

		quit = tk.Button(self, text="退出", command = root.destroy)
		 
		quit.place(x=50, y=50)


	def say_hi(self) :
		print("Hello World")

root = tk.Tk()
app = LogForm(master=root)

app.master.title("Hello 肖红阳")
app.master.maxsize(500, 500)
app.master.minsize(300, 300)
app.mainloop()


#用户名

#密码

#登录按钮





