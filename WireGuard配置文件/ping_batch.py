with open("ip_sample_list.txt","r") as f:
    ip_list=[i.strip() for i in f.readlines()]

from utils import ping

success,fail=ping(ip_list)

print()
print("Total:",len(ip_list))
print("Success:",len(success))
print("Fail:",len(fail))
print("Success Rate:",len(success)/len(ip_list))