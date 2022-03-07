from DTPySide import *

class MenuButton(QPushButton):
	def __init__(self,text):
		super().__init__()
		self.setText(text)
		self.setFlat(True)
		self.setFixedSize(64,64)