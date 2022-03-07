"去历史记录页面保存导出为一个叫www.bilibili.com.har的文件"

import re,time

with open("www.bilibili.com.har","r",encoding="utf-8") as f:
	s=f.read()

s=re.findall(r'\{\\"title\\":\\".*?\\"live_status\\"',s)

with open("Bilibili_history_.txt","w",encoding="utf-8") as f:
	for i in s:
		title=re.findall(r'(?<=\\"title\\":\\").*?(?=\\")',i)[0]
		author=re.findall(r'(?<=\\"author_name\\":\\").*?(?=\\")',i)[0]
		datetime=re.findall(r'(?<=\\"view_at\\":).*?(?=,\\")',i)[0]
		av="av"+re.findall(r'(?<=\\"oid\\":).*?(?=,)',i)[0]
		bv=re.findall(r'(?<=\\"bvid\\":\\").*?(?=\\",)',i)[0]
		datetime=int(datetime)
		datetime=time.localtime(datetime)
		datetime=time.strftime("%Y-%m-%d %H:%M:%S",datetime)
		if av=="":
			av="\\0"
		if bv=="":
			bv="\\0"
		if author=="":
			author="\\0"
		if title=="":
			title="\\0"
		f.write("%s"%av+"	"+"%s"%bv+"	"+datetime+"	"+author+"	"+title+"\n")
