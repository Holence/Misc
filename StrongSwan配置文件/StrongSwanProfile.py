import os

root=os.path.dirname(os.path.abspath(__file__))
folder_dir=os.path.join(root,"sswan")
if not os.path.exists(folder_dir):
    os.makedirs(folder_dir)

with open(os.path.join(root,"new_servers.txt"),"r",encoding="utf-8") as f:
    a=f.readlines()
# with open(os.path.join(root,"old_servers.txt"),"r",encoding="utf-8") as f:
#     a=f.readlines()

o=0
for i in a:
    if i=="\n":
        continue
    name,addr,id=i[:-1].split(", ")
    text="""{
        "uuid": "559eb893-1cee-4196-8b97-67045e029e%02d",
        "name": "%s",
        "type": "ikev2-eap",
        "remote": {
            "addr": "%s",
            "id": "%s"
        },
        "dns-servers" : "1.1.1.1 1.0.0.1 103.86.99.98 103.86.96.98"
    }
    """%(o,name,addr,id)
    with open(os.path.join(folder_dir,"%s.sswan"%name),"w",encoding="utf-8") as f:
        f.write(text)
    o+=1