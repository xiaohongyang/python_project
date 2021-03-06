import tkinter as tk
from tkinter import *
import tkinter.messagebox
from urllib import *
import urllib.request
import json
from lib import  *
import lib.LogTool

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

		entry_password = Entry(self, show="*")
		entry_password.grid(row=1, column=1)

		self.entry_username = entry_username
		self.entry_password = entry_password

		btn_regist = Button(self, text="注册", command=self.register)
		btn_regist.grid(row=2)

		btn_submit = Button(self, text="登录", command=self.doLogin);
		btn_submit.grid(row=2,column=2)

	def doLogin(self):
		username = self.entry_username.get()
		password = self.entry_password.get()
		if len(username) < 1 :
			tk.messagebox.showinfo("提示:", "账号不能为空")
		elif len(password) < 1 :
			tk.messagebox.showinfo("提示:", "密码不能为空")
		elif self.postLoginUser(username=username, password=password):
			tk.messagebox.showinfo("提示:", "登录成功")
		else :
			message =  self.message if hasattr(self, 'message') else "登录失败"
			print(self.message)
			tk.messagebox.showinfo("提示:", message)

	def postLoginUser(self, username="", password=""):

		result = False
		loginUrl = 'http://laravel.54.com:5000/passwordToken?email=' + username + '&password=' + password
		print(loginUrl)

		try :
			req = urllib.request.Request(loginUrl)
			reqObj = urllib.request.urlopen(req)
			apiContent = reqObj.read()
			info = str(apiContent, encoding="utf-8")
			info = json.loads(info)
			print(info)
			if info['status'] == 1 and len(info['data']) >0 :
				result = True
			else :
				self.message = info['message']
				lib.LogTool.LogTool.log(self.message)


		except Exception as e:
			self.message = str(e)
			print(str(e))
			lib.LogTool.LogTool.log(str(e))

		return  result
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

		top.grab_set()
		#tk.messagebox.showinfo("username", "321")

	def doRegister(self,master):
		username = master.entry_username.get()
		tk.messagebox.showinfo("hello","username %s" % username)
		master.grab_set()

if __name__ == "__main__" :
	root = tk.Tk()
	app = MyCheckButton(master = root)
	app.master.title("用户登录")
	app.mainloop()