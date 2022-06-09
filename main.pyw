from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as messagebox
import threading
import os

filename = 'text\\text'
pid = os.getpid()
state = True

with open(filename, 'r') as file_object:
		text = file_object.readlines()
		if text == []:
			text = '%s' % '这里好像什么都没有哦~'
print(text)

class main_root():
	def __init__(self):
		global main_window
		self.main_window = Tk()
		self.main_window.title('Python 表白 (Version: 2.0)')
		main_root.center_window(self.main_window, 500, 300)
		self.main_window.resizable(width=False, height=False)
		self.main_window.protocol("WM_DELETE_WINDOW", main_root.callback)

		Label(text=text, width=60).place(x=65, y=20)

		Button(self.main_window, text='同意', width=50, command=main_root.agree).place(x=70, y=190)
		Button(self.main_window, text='不同意', width=50, command=main_root.disagree).place(x=70, y=240)

		self.main_window.mainloop()

	def center_window(root, width, height):
		screenwidth = root.winfo_screenwidth()
		screenheight = root.winfo_screenheight()
		size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
		root.geometry(size)
		root.update()

	def agree():
		global state
		os.system('taskkill /pid ' + str(pid) + ' /f')

	def disagree():
		messagebox.showwarning('%s' % '友情的提示 - 来自发布者', '%s' % '你确定不再想想嘛？ 要慎重考虑一下哦~')

	def callback():
		messagebox.showwarning('%s' % '友情的提示 - 来自发布者', '%s' % '“同意”和“不同意”之间你总得选一个吧？')

	def show_error():
		messagebox.showerror('%s' % '友情的提示 - 来自发布者', '%s' % '你不可以选择这种方式结束进程！否则...')
		os.system('start script\\reboot.bat')

if __name__ == '__main__':
	try:
		main_root()
	except:
		main_root.show_error()
