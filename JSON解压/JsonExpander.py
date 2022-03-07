from DTPySide import *

class Thread(QThread):

    step=Signal(int)
    finish=Signal()

    def __init__(self, parent,path) -> None:
        super().__init__(parent=parent)
        self.path=path

    def run(self):
        new_path=os.path.dirname(self.path)+"\\NEW_"+os.path.basename(self.path)
        self.step.emit(1)
        data=Json_Load(self.path)
        self.step.emit(2)
        Json_Save(data,new_path)
        self.step.emit(3)
        self.finish.emit()

class Label(QLabel):
    def __init__(self, text: str, parent):
        super().__init__(text, parent=parent)
        self.setAcceptDrops(True)
    
    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            url=event.mimeData().urls()
            if len(url)==1 and os.path.splitext(url[0].toString())[1].lower()==".json":
                event.acceptProposedAction()
            else:
                event.ignore()
    
    def dragMoveEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            url=event.mimeData().urls()
            if len(url)==1 and os.path.splitext(url[0].toString())[1].lower()==".json":
                event.acceptProposedAction()
            else:
                event.ignore()
    
    def dropEvent(self, event: QDropEvent):
        def stepping():
            self.setText(self.text()+"...... ")
        
        def finish():
            self.Thread.deleteLater()
            self.setText("\nDrag in a json file.\n\n")
        
        if event.mimeData().hasUrls():
            url=event.mimeData().urls()
            if len(url)==1 and os.path.splitext(url[0].toString())[1].lower()==".json":
                path=os.path.abspath(url[0].toString().replace("file:///",""))
                
                self.Thread=Thread(self,path)
                self.Thread.step.connect(stepping)
                self.Thread.finish.connect(finish)
                self.Thread.start()
                
            else:
                event.ignore()

class MainSession(DTSession.DTMainSession):
    def __init__(self, app):
        super().__init__(app)
        self.setMaximumSize(500,300)
        self.label=Label("\nDrag in a json file.\n\n",self)
        self.label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.label)

app=DTAPP(sys.argv)

app.setApplicationName("Json Expander")
app.setWindowIcon(DTIcon.HoloIcon2())
app.setAuthor("Holence")
app.setApplicationVersion("1.0.0.0")
app.setLoginEnable(False)

session=MainSession(app)
app.setMainSession(session)

# app.debugRun("123",True)
app.run()