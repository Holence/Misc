import json

# 用下面网址获取server列表，保存为servers.json
# https://api.nordvpn.com/v1/servers?fields[servers.id]&fields[servers.name]&fields[servers.hostname]&fields[servers.load]&fields[servers.station]&fields[servers.technologies]&limit=20000

with open("servers.json","r") as f:
    servers=json.load(f)

server_dict={}
for i in servers:
    if "-" in i["hostname"]:
        continue
    country=" ".join(i["name"].split()[:-1]).title()
    
    if server_dict.get(country)==None:
        server_dict[country]={
            "country":country,
            "name":i["hostname"][:2],
            "nums":0,
            "servers":{}
        }
    
    pk=None
    for j in i["technologies"]:
        if j["name"]=="Wireguard":
            pk=j["metadata"][0]["value"]
    if pk==None:
        continue

    ip_prefix=i["station"][:i["station"].rfind(".")]
    ip_surfix=int(i["station"][i["station"].rfind(".")+1:])
    server_dict[country]["nums"]+=1
    if server_dict[country]["servers"].get(ip_prefix)==None:
        server_dict[country]["servers"][ip_prefix]={
            "surfixs":[ip_surfix],
            "pk":pk
        }
        server_dict[country]["servers"]=dict(sorted(server_dict[country]["servers"].items(),key=lambda x:x[0]))

    else:
        server_dict[country]["servers"][ip_prefix]["surfixs"].append(ip_surfix)
        server_dict[country]["servers"][ip_prefix]["surfixs"].sort()
        if pk!=server_dict[country]["servers"][ip_prefix]["pk"]:
            print(country,ip_prefix,ip_surfix,pk)
            print(server_dict[country]["servers"][ip_prefix])

server_dict=dict(sorted(server_dict.items(),key=lambda x:x[0]))

with open("servers_analyzed.json","w") as f:
    json.dump(server_dict,f)