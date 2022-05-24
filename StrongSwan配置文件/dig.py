import subprocess
import re

def resolve_ip(domain_list):
    ip_list=[]
    for domain in domain_list:
        try:
            result = subprocess.Popen(["ping", domain, "-n", "1","-w","1000"], stdout = subprocess.PIPE,stderr = subprocess.PIPE, shell=True)
            result = result.communicate()

            pattern = r"Average = (\d+\S+)"
            pattern2 = r"(?<=\[).*?(?=\])"
            if len(re.findall(pattern, result[0].decode()))!=0:
                times=re.findall(pattern, result[0].decode())[0]
                ip=re.findall(pattern2, result[0].decode())[0]
                ip_list.append((domain,ip))
                print("%20s"%domain,"%11s"%ip,times)
            else:
                print("%20s"%domain,"Not found")
        
        # ctrl+c终止ping
        except KeyboardInterrupt:
            print("强制停止！")
            break
    
    return ip_list

def ping(domain_and_ip_list):
    success=[]
    fail=[]
    for thing in domain_and_ip_list:
        domain, ip = thing
        try:
            result = subprocess.Popen(["ping", ip, "-n", "1","-w","1000"], stdout = subprocess.PIPE,stderr = subprocess.PIPE, shell=True)
            result = result.communicate()
            pattern = r"Average = (\d+\S+)"
            if len(re.findall(pattern, result[0].decode()))!=0:
                times=re.findall(pattern, result[0].decode())[0]
                print("%20s"%domain,"%11s"%ip,times)
                success.append(ip)
            else:
                print("%20s"%domain,"%11s"%ip)
                fail.append(ip)
        
        # ctrl+c终止ping
        except KeyboardInterrupt:
            print("强制停止！")
            break
    
    return success,fail

domain_list=[]
# for i in range(1,10000):
    # domain_list.append("xxx.xxx.com"%i)

input("Resolve ip need a clean DNS...\nStart?")
res=resolve_ip(domain_list)
input("Please change your connection...\nDone?")
success,fail=ping(res)
print("---------------Successed---------------")
for i in success:
    print(i)