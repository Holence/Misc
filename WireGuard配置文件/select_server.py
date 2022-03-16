import json
from utils import ping

with open("servers_analyzed.json","r") as f:
    server_dict=json.load(f)

test_country="Italy"
test_prefix="178.249.211" # None

print(test_country)
print("total ips:",server_dict[test_country]["nums"])
servers=server_dict[test_country]["servers"]
print("total prefixs:",len(servers))

if test_prefix==None:
    for prefix,value in servers.items():

        # 找那种分布在全域的前缀
        # if len(value["surfixs"])<15:
        #     continue

        end=value["surfixs"][-1]
        start=value["surfixs"][0]
        if end!=start:
            dense=len(value["surfixs"])/(end-start)*100
        else:
            dense=100
        pk=value["pk"]
        print("%11s    %3s - %3s = %3s   ~ %6.2f%%  %s  %s"%(prefix,start,end,end-start,dense,pk,value["surfixs"]))

        ping_list=[]
        for i in value["surfixs"]:
            for j in range(3):
                ip=prefix+".%s"%(i+j)
                if ip not in ping_list:
                    ping_list.append(ip)
        ping(ping_list)
        input()
else:
    value=servers[test_prefix]
    prefix=test_prefix
    end=value["surfixs"][-1]
    start=value["surfixs"][0]
    if end!=start:
        dense=len(value["surfixs"])/(end-start)*100
    else:
        dense=100
    pk=value["pk"]
    print("%11s    %3s - %3s = %3s   ~ %6.2f%%  %s  %s"%(prefix,start,end,end-start,dense,pk,value["surfixs"]))

    ping_list=[]
    for i in value["surfixs"]:
        for j in range(3):
            ip=prefix+".%s"%(i+j)
            if ip not in ping_list:
                ping_list.append(ip)
    ping(ping_list)
    input()