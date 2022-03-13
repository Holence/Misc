import os,shutil

def deepin(dir):
    list=os.listdir(dir)
    for i in list:
        path=os.path.join(dir,i)
        if os.path.isdir(path):
            if os.listdir(path)==[]:
                shutil.rmtree(path)
                print("Delete",path)
            else:
                deepin(path)
                if os.listdir(path)==[]:
                    shutil.rmtree(path)
                    print("Delete",path)

confirm=input("输入Confirmed开始执行任务:")
if confirm!="Confirmed":
    exit()
dir=os.getcwd()
deepin(dir)

print("OK")
os.system("pause")