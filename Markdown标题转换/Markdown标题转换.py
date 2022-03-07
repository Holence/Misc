import tkinter as tk
import os
import re

window = tk.Tk()
window.title('标题转换') # 标题
window.geometry('500x800') # 窗口尺寸
textbox1 = tk.Text(window, width=50, height=50)
textbox1.pack()
def process():
	text=""
	try:
		text = textbox1.get('1.0', tk.END)#get要指定头到尾，1.0是第一行第一列的字符
		text=text.split("\n")
		x=int(text[-2])#最后一行的数字
		textbox1.delete('1.0', tk.END)
		n=0
		for i in text:
			if re.findall("^#*",i)==['']:
				s=i
			else:
				if i.count("#")-x<1:
					textbox1.delete('1.0', tk.END)
					textbox1.insert(tk.END,"级数越界！！")
					return
				else:
					s=re.sub("^#*","#"*(i.count("#")-x),i)
			textbox1.insert(tk.END,s+"\n")
			n+=1
		textbox1.delete('%s.0'%n, tk.END)
	except:
		pass

button = tk.Button(window, text='开始转换', width=15, height=2, command=process)
button.pack()
window.mainloop()