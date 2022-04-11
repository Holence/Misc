import os
import shutil
import re

root=r"PathToMangaFolder"

epub_list=[]
for i in os.listdir(root):
    if os.path.splitext(i)[1][1:]=="epub":
        epub_list.append(i)

temp_folder=os.path.join(root,"temp")

for epub_file in epub_list:
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)

    print("Extracting",epub_file)
    shutil.unpack_archive(os.path.join(root,epub_file),temp_folder,"zip")
    print("Extract Successed",epub_file)
    html_folder=os.path.join(temp_folder,"html")
    img_folder=os.path.join(temp_folder,"image")
    os.rename(os.path.join(img_folder,"cover.jpg"),os.path.join(img_folder,"0001.jpg"))
    html_filelist=sorted(os.listdir(html_folder), key = lambda x : int(x.split(".")[0]) if str.isnumeric(x.split(".")[0]) else 0)
    
    num=2
    for html_file in html_filelist:
        f=open(os.path.join(html_folder,html_file),encoding="utf-8")
        s=f.read()
        f.close()
        img_oldname=re.findall('(?<=<img src="\.\./image/).*?(?=")',s)[0]
        
        if "cover" in img_oldname or "createby" in img_oldname or "." not in img_oldname:
            continue
        
        ext=img_oldname.split(".")[-1]
        os.rename(os.path.join(img_folder,img_oldname),os.path.join(img_folder,"%04d.%s"%(num,ext)))
        num+=1
    
    book_name=epub_file.split(".")[0]
    cbz_file=os.path.join(root,book_name)
    shutil.make_archive(cbz_file,"zip",img_folder)
    os.rename(cbz_file+".zip",cbz_file+".cbz")
    print("Making CBZ Successed",epub_file)
    
    shutil.rmtree(temp_folder)