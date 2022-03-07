from DTPySide import *



class MainSession(DTSession.DTMainSession):
	def __init__(self, app):
		super().__init__(app)
	
	def initializeData(self):
		return
	
	def initializeWindow(self):
		super().initializeWindow()
		self.mainwindow=MainWindow(self)
		self.setCentralWidget(self.mainwindow)
		
		# 真是奇了怪了，在DTWindow里设置会导致无法正常最大化
		# 在这里设置却因为有QWebEngineView就没有问题？
		if self.app.WindowEffect()!="Normal":
			self.setAttribute(Qt.WA_TranslucentBackground)
	
	def loadSectionData(self,index):
		self.SectionData=Json_Load("data%s.json"%index)
		# self.SectionData=Fernet_Decrypt_Load(self.password(),"data.dlcw")
	
	def saveSectionData(self,index):
		Json_Save(self.SectionData,"data%s.json"%index)
		# Fernet_Encrypt_Save(self.password(),self.SectionData,"data.dlcw")
	
	def __getSection(self):
		section_list=Fernet_Decrypt(self.password(),self.UserSetting().value("Section"))
		if section_list==False:
			section_list=[]
			self.UserSetting().setValue("Section",Fernet_Encrypt(self.password(),section_list))
		return section_list

	def getSectionName(self,index):
		section_list=self.__getSection()
		try:
			return section_list[index]
		except:
			return ""
	
	def addSection(self,name):
		section_list=self.__getSection()
		section_list.append(name)
		self.UserSetting().setValue("Section",Fernet_Encrypt(self.password(),section_list))
		self.SectionData={
			"name":name,
			"feed":{},
			"top":[]
		}

from Ui_MainWindow import Ui_MainWindow
class MainWindow(QWidget,Ui_MainWindow):
	def __init__(self, parent:MainSession):
		super().__init__(parent=parent)
		self.setupUi(self)
		self.Headquarter=parent

		from PySide2.QtWebEngineWidgets import QWebEngineView,QWebEngineSettings
		self.browser=QWebEngineView(self)
		self.browser.settings().setAttribute(QWebEngineSettings.PluginsEnabled,True)
		self.browser.settings().setAttribute(QWebEngineSettings.JavascriptEnabled,True)
		self.browser.settings().setAttribute(QWebEngineSettings.AllowWindowActivationFromJavaScript,True)
		self.browser.settings().setAttribute(QWebEngineSettings.WebGLEnabled,True)
		self.browser.settings().setAttribute(QWebEngineSettings.ScrollAnimatorEnabled,True)
		self.browser.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled,True)
		self.browser.settings().setAttribute(QWebEngineSettings.Accelerated2dCanvasEnabled,True)
		self.browser.settings().setAttribute(QWebEngineSettings.AllowRunningInsecureContent,True)
		self.splitter.addWidget(self.browser)
		self.splitter.setStretchFactor(0,1)
		self.splitter.setStretchFactor(1,1)
		self.splitter.setStretchFactor(2,5)

		# 不加载一下就不让改高度？？？
		self.setWebPage("http://???")
		self.initialze()

	def initialze(self):
		self.refreshMenuButtons()
	
	def initializeSignal(self):
		self.actionCreate_New_Section.triggered.connect(self.addSection)
	
	def refreshMenuButtons(self):
		Clear_Layout(self.buttonLayout)

		from MenuButton import MenuButton
		index=0
		for file in os.listdir("./data"):
			name=os.path.splitext(file)[0]
			if name[:4]=="data" and str(name[4:]).isdigit():
				name=self.Headquarter.getSectionName(index)
				btn=MenuButton(name)
				self.buttonLayout.addWidget(btn)
				index+=1
	
	def refreshTable(self):
		self.feedTable.clear()
		self.topfeedTable.clear()
		self.articleTable.clear()

	def setWebPage(self,url):
		self.browser.load(url)
	
	def addSection(self):
		dlg=DTFrame.DTDialog(self,"Add Section")
		lable=QLabel("Section Name:",dlg)
		lineedit=QLineEdit(dlg)
		layout=QVBoxLayout(dlg)
		layout.addWidget(lable)
		layout.addWidget(lineedit)
		dlg.setCentralWidget(layout)
		if dlg.exec_():
			name=lineedit.text()
			self.Headquarter.addSection(name,self.buttonLayout.count())
			self.Headquarter.SectionData={}
			self.Headquarter.saveSectionData()
			self.refreshMenuButtons()
			self.refreshTable()