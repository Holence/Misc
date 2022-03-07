from DTPySide import *
from MainWindow import MainSession

QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
app=DTAPP([])
mainsession=MainSession(app)
app.setMainSession(mainsession)
app.run()

# for file in os.listdir("./data"):
#     print(os.path.split(file))