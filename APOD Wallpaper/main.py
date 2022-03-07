from DTPySide import *
from ctypes import windll
import feedparser

class APODThread(QThread):

	faild=Signal(str)
	successed=Signal(str)

	def __init__(self, parent) -> None:
		super().__init__(parent=parent)

	def run(self) -> None:
		self.do()
	
	def do(self):
		explain_dict=Json_Load("explain")
		
		date_dict={"January":"1","February":"2","March":"3","April":"4","May":"5","June":"6","July":"7","August":"8","September":"9","October":"10","November":"11","December":"12"}
		have=[]
		for name in os.listdir("./wallpaper"):
			name=re.sub("\d+\.\d+\.\d+ ","",name)
			have.append(name)
		
		result=feedparser.parse("https://apod.nasa.gov/apod.rss")
		
		for index in range(len(result["entries"])):
			item=result["entries"][index]
			title=item["title"].replace(":","：")+".jpg"
			if title not in have:
				
				link=item["link"]
				status,html=GetWebPageHTML(link)
				
				
				if status==True:
					html= etree.HTML(html)
					
					y,m,d=html.xpath("/html/body/center[1]/p[2]/text()")[0].split()
					m=date_dict[m]
					date="%s.%s.%s"%(y,m,d)
					
					title=date+" "+title

					explain=html.xpath("/html/body/p[1]//text()")
					explain="".join(explain)
					explain=re.sub("[\s]+"," ",explain)
					explain_dict[title]=explain

					last=html.xpath("/html/body/center[1]/p[2]/a/@href")[0]
					link="https://apod.nasa.gov/apod/"+last
					status,img=GetWebPagePic(link)
					if status==True:
						with open("./wallpaper/%s"%title,"wb") as f:
							f.write(img)
						self.successed.emit("Downloaded "+title)
						

					else:
						self.faild.emit("Failed to load "+link)
				else:
					self.faild.emit("Failed to load "+link)
		
		Json_Save(explain_dict,"explain")
		

from Ui_Mainwindow import Ui_Mainwindow
class Mainwindow(Ui_Mainwindow,QWidget):
	def __init__(self,Headquarter) -> None:
		super().__init__()
		self.setupUi(self)
		self.Headquarter=Headquarter
		self.listWidget.itemClicked.connect(self.setwallpaper)
	
	def about(self):
		
		about_text=self.explain_dict[self.current]
		dlg=DTFrame.DTConfirmBox(self,self.current,about_text)
		dlg.buttonBox.button(QDialogButtonBox.Ok).setText("Quit")
		dlg.buttonBox.button(QDialogButtonBox.Cancel).setText("Stay")
		if dlg.exec_():
			self.Headquarter.quitApp.emit()
		
		
	def setwallpaper(self,name):
		if type(name)==str:
			pass
		else:
			name=self.listWidget.currentItem().text()
		
		self.current=name
		path=os.path.abspath("./wallpaper/"+name)
		windll.user32.SystemParametersInfoW(20, 0, path, 1)

		self.about()
	
	def refresh(self):
		self.explain_dict=Json_Load("explain")
		self.listWidget.clear()
		for title in os.listdir("./wallpaper"):
			item=QListWidgetItem(title)
			item.setIcon(QPixmap("./wallpaper/%s"%title).scaled(512,512,Qt.KeepAspectRatioByExpanding))
			self.listWidget.addItem(item)

class WallpaperChanger(DTSession.DTMainSession):
	def closeEvent(self,event):
		QCloseEvent()
	
	def __init__(self, app):
		super().__init__(app)
		self.module=Mainwindow(self)
		def slot(msg):
			self.app.TrayIcon.showMessage("Error",msg,DTIcon.Error())
		def slot2(msg):
			self.app.TrayIcon.showMessage("Information",msg,DTIcon.Happy())
		
		def done():
			self.app.setWindowIcon(QIcon(QPixmap(":/favicon.ico").scaled(64,64)))
			self.TitleBar.updateWindowIcon()
			self.app.TrayIcon.setIcon(self.windowIcon())
			self.module.setwallpaper(os.listdir("./wallpaper")[-1])

		if os.path.exists("./wallpaper")==False:
			os.makedirs("./wallpaper")
		
		if os.path.exists("./explain")==False:
			Json_Save({},"./explain")

		self.Thread=APODThread(self)
		self.Thread.finished.connect(self.module.refresh)
		self.Thread.finished.connect(done)
		self.Thread.finished.connect(self.Thread.deleteLater)
		self.Thread.faild.connect(slot)
		self.Thread.successed.connect(slot2)
		self.Thread.start()
	
	def initializeWindow(self):
		self.TitleBar.setFull(False)
		self.TitleBar.updateWindowIcon()
		self.setWindowTitle(self.app.applicationName())
		self.setCentralWidget(self.module)
		self.module.refresh()
	
	def initializeSignal(self):
		self.actionExit.triggered.connect(self.quitApp.emit)
		self.actionAbout.triggered.connect(self.about)

	def initializeMenu(self):
		self._MainMenu.addAction(self.actionAbout)
		self._MainMenu.addAction(self.actionExit)
	
	def about(self):
		self.module.about()

app=DTAPP([])
app.setApplicationName("APOD Wallpaper")
app.setWindowIcon(QIcon(":/white_rotate-cw.svg"))
mainsession=WallpaperChanger(app)
app.setMainSession(mainsession)
app.run(show=False)