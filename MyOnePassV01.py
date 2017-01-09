#MyOnePass.py
#GUI for password management
#Date April 1st 2013
#Author Peter Su
#Version 0.1

#DESCRIPTION:
#Take input and encrypt Site with master key
#

#WORKING ON:
#
#FEATURES TO ADD:
#Draggable form
#

from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import re
FONTSIZE = 10
WIDTH = 500
HEIGHT = 500
NUMC = 3
NUMR = 3

#import tkinter as tk
class App:
	def __init__(self, master):
		#self.text = Label(master, text='test',bg='#%02x%02x%02x'%(64, 100, 61), width=int(400/FONTSIZE), height=int(400/FONTSIZE), font=("Helvetica", FONTSIZE)).grid(row=0,column=0)
		#for r in range(NUMR):
		#    for c in range(NUMC):
		#        self.text = Label(master, text='R%s/C%s'%(r,c), anchor=CENTER, bg='#%02x%02x%02x'%(255,255,255), width=int(WIDTH/(NUMC*FONTSIZE))+1, height=int((HEIGHT/(2*NUMR*FONTSIZE))+1), font=("Helvetica", FONTSIZE)).grid(row=r,column=c)
		content = ttk.Frame(master)
		frame = ttk.Frame(content, borderwidth = 5, relief='sunken', width=400, height=300)


		content.grid(column=0, row=0)
		frame.grid(column=0, row=0, columnspan=10, rowspan=10)

		#DragBar
		self.dragbar = Label(content, bitmap="gray25")
		self.dragbar.bind('<ButtonPress-1>', self.StartMove)
		self.dragbar.bind('<ButtonRelease-1>', self.StopMove)
		self.dragbar.bind('<B1-Motion>', self.OnMotion)
		self.dragbar.grid(column=0, row=0)

	
		#Word List GUI
		self.word_list_label = Label(content, text='Word List:')
		self.word_list_entry = Entry(content)
		self.word_list_button = Button(content, text='...', command= lambda: self.browse("word"))
		self.word_list_load_button = Button(content, text='Load', command=self.load_word)
		self.word_list_label.grid(column=0, row=1)
		self.word_list_entry.grid(column=1, row=1)
		self.word_list_button.grid(column=2, row=1)
		self.word_list_load_button.grid(column=3, row=1)


		#DB List GUI
		self.database_label = Label(content, text='Database:')
		self.database_entry = Entry(content)
		self.database_button = Button(content, text='...', command= lambda: self.browse("database"))
		self.database_load_button = Button(content, text='Load', command=self.load_database)
		self.database_label.grid(column=0, row=2)
		self.database_entry.grid(column=1, row=2)
		self.database_button.grid(column=2, row=2)
		self.database_load_button.grid(	column=3, row=2)


		self.name_label = Label(content, text='Name:')
		self.name_entry = Entry(content)
		self.name_search_button = Button(content, text='Search', command=self.browse)
		self.name_label.grid(column=0, row=3)
		self.name_entry.grid(column=1, row=3)
		self.name_search_button.grid(column=3, row=3)

		self.url_label = Label(content, text='url:')
		self.country_label = Label(content, text='country:')
		self.account_label = Label(content, text='account:')
		self.password_label= Label(content, text='password:')
		self.notes_label= Label(content, text='notes:')
		self.exit = Button(master, text='Quit', command=frame.quit)
		






		#self.url_label.grid(column=0, row=1)
		#self.country_label.grid(column=0, row=2) 
		#self.account_label.grid(column=0, row=3) 
		#self.password_label.grid(column=0, row=4)
		#self.notes_label= Label(content, text='notes:')
		self.exit.grid(column=10, row=10)

	#GUI functions
	def StartMove(self, event):
		self.x = event.x
		self.y = event.y

	def StopMove(self,event):
		self.x = None 
		self.y = None 

	def OnMotion(self, event):
		deltax = event.x - self.x
		deltay = event.y - self.y
		x = (event.x_root - self.x - self.dragbar.winfo_rootx() + self.dLeragbar.winfo_rootx())
		y = (event.y_root - self.y - self.dragbar.winfo_rooty() + self.dragbar.winfo_rooty())
		root.geometry("+%s+%s" % (x,y))

	def say_hi(self):
		print ("test")

	def browse(self, field):
		location = askopenfilename()
		if field == "word":
			self.word_list_entry.delete(0, END)
			self.word_list_entry.insert(0, location)
		elif field =="database":
			self.database_entry.delete(0, END)
			self.database_entry.insert(0, location)
		else:
			self.name_entry.insert(0, location)

	def search(self, **args):
		file_name = self.name_entry.get()
		
		#regexp match obtained from "http://txt2re.com/index-python.php"
		re1='(\\.)'	# Non-greedy match on filler
		re2='(nops\Z)'	# Word 1
		rg = re.compile(re1+re2,re.IGNORECASE|re.DOTALL)
		m = rg.search(file_name)
		if m:
			f = open(file_name, 'r')
			print (f)
			f.close()
		else:
			print("Wrong file type")

	def load_word(self, **args):
		file_name = self.word_list_entry.get()
		#regexp match obtained from "http://txt2re.com/index-python.php"
		re1='(\\.wl\Z)'	# Non-greedy match on filler
		rg = re.compile(re1,re.IGNORECASE|re.DOTALL)
		m = rg.search(file_name)
		if m:
			f = open(file_name, 'r')
			print (f)
			f.close()
		else:
			print("Wrong file type")

	def load_database(self, **args):
		file_name = self.database_entry.get()	
		#regexp match obtained from "http://txt2re.com/index-python.php"
		re1='(\\.db\Z)'	# Non-greedy match on filler
		rg = re.compile(re,re1.IGNORECASE|re.DOTALL)
		m = rg.search(file_name)
		if m:
			f = open(file_name, 'r')
			print (f)
			f.close()
		else:
			print("Wrong file type")


	def quit():
		global root
		root.quit()
root = Tk()

root.update()
root.minsize(WIDTH, HEIGHT)
root.lower()
#root.iconify()
root.geometry("500x500")
root.title('Password')
#make the default windows border dissappear
root.overrideredirect(1)
#print (int(WIDTH/NUMC/FONTSIZE))
#print (int(HEIGHT/NUMR/FONTSIZE))
print (int(WIDTH/(NUMC*FONTSIZE))+1)
print (int((HEIGHT/(2*NUMR*FONTSIZE))+1))
app = App(root)
root.mainloop()