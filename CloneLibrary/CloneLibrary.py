from DTPySide import *

class Label(QLabel):

    dropped=Signal(list)

    def __init__(self, text: str, parent):
        super().__init__(text, parent=parent)
        self.setAcceptDrops(True)
    
    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
    
    def dragMoveEvent(self, event: QDragEnterEvent):
        event.acceptProposedAction()
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
    
    def dropEvent(self, event: QDropEvent):
        
        if event.mimeData().hasUrls():
            urls=event.mimeData().urls()
            urls=[os.path.abspath(url.toString().replace("file:///","")) for url in urls]
            self.dropped.emit(urls)

class MainSession(DTSession.DTMainSession):
    def __init__(self, app):
        super().__init__(app)
        self.setMaximumSize(500,500)

        self.label=QLabel("Copy to which root?")
        self.lineedit=QLineEdit()
        self.lineedit.setText("D:\\dlcw")
        self.lineedit.setPlaceholderText("D:\\dlcw")
        
        self.label2=QLabel("Copy from which library base?")
        self.lineedit2=QLineEdit()
        self.lineedit2.setText("E:\\dlcw")
        self.lineedit2.setPlaceholderText("E:\\dlcw")

        self.area=Label("\nDrag in files to copy.\n\n",self)
        self.area.dropped.connect(self.Copy)
        
        layout=QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.lineedit)
        layout.addWidget(self.label2)
        layout.addWidget(self.lineedit2)
        layout.addWidget(self.area)

        self.widget=QWidget()
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)        
    
    def Copy(self,urls):
        copydst_root=self.lineedit.text()
        library_base=self.lineedit2.text()
        
        dst_dict={}
        for url in urls:
            surfix=url.replace((library_base+"\\").replace("\\\\","\\"),"")
            dst=os.path.dirname(copydst_root+"\\"+surfix)

            if not os.path.exists(dst):
                os.makedirs(dst)
            
            if dst_dict.get(dst)==None:
                dst_dict[dst]=[url]
            else:
                dst_dict[dst].append(url)

        for dst,url_list in dst_dict.items():
            Win32_Shellcopy(url_list,dst)

app=DTAPP(sys.argv)

app.setApplicationName("CloneLibrary")
app.setWindowIcon(DTIcon.HoloIcon2())
app.setAuthor("Holence")
app.setApplicationVersion("1.0.0.0")
app.setLoginEnable(False)

session=MainSession(app)
app.setMainSession(session)

# app.debugRun("123",True)
app.run()