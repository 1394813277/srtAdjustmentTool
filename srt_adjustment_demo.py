#字幕调整工具

import tkinter as tk
import sys
from tkinter import *
from tkinter import filedialog

import srt_center

class App:



	def __init__(self,root):
		frame = tk.Frame(root)
		frame.pack()

		self.hi_there = tk.Button(frame,text = '选择srt字幕',fg='blue',command = self.sayHi)
		self.hi_there.pack(side = tk.LEFT)

		self.pathLabel = tk.Label(frame,text = '您还未选取文件...')
		self.pathLabel.pack(side = tk.LEFT)

		self.startButton = tk.Button(frame,text = '开始修改',fg = 'blue',command = self.startModify)
		self.startButton.pack(side = tk.LEFT)

		self.entry1 = tk.Entry(frame)
		self.entry1.insert(0,'+00:00:00,000')
		self.entry1.pack(side = tk.LEFT)
		
	def startModify(self):
		print('在这里开始转换')
		path1 = self.pathLabel['text']
		timeoffset = self.entry1.get()
		s1 = timeoffset[:1]
		s2 = timeoffset[1:]
		if len(path1) > 0:
			if path1.endswith('srt'):
				print(path1)
				print('您选取的是srt')
				print()
				srt_center.dispose(path1,s2,s1)

			else:
				print('目前只支持srt')
		else:
			print('请先选择文件。。。。。。')


	def sayHi(self):
		# path1 = self.entry1.get()
		fillName = filedialog.askopenfilename()
		print(fillName)
		self.pathLabel['text'] = fillName


root = tk.Tk()

root.title('srt字幕调整工具')

app = App(root)

root.mainloop()