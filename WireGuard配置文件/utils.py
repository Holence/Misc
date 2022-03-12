import subprocess
import re

def ping(ip_list):
    success=[]
    fail=[]
    for ip in ip_list:
        try:
            result = subprocess.Popen(["ping", ip, "-n", "1","-w","1000"], stdout = subprocess.PIPE,stderr = subprocess.PIPE, shell=True)
            result = result.communicate()
            pattern = r"Average = (\d+\S+)"
            if len(re.findall(pattern, result[0].decode()))!=0:
                times=re.findall(pattern, result[0].decode())[0]
                print("%11s"%ip,times)
                success.append(ip)
            else:
                print("%11s"%ip)
                fail.append(ip)
        
        # ctrl+c终止ping
        except KeyboardInterrupt:
            print("强制停止！")
            break
    
    return success,fail