import re
import os

def purify(s:str):
    s=re.sub("\n{2,20}","\n",s)
    s=s.split("\n")
    s=[i.strip().replace("~","\~") for i in s]
    s="\n\n".join(s)
    return s

def getNovel(api,novel_info_dict):
    novel_id, novel_title, novel_description = novel_info_dict["id"], novel_info_dict["title"], novel_info_dict["caption"].replace("<br />","\n\n")
    res=api.novel_text(novel_id)
    novel_text=purify(res["novel_text"])
    next_novel_info_dict=res["series_next"]
    return novel_id, novel_title, novel_description, novel_text, next_novel_info_dict

class MarkdownBook:
    def __init__(self, name, author, description, cover_dir) -> None:
        self.name=name
        cover_dir=cover_dir.replace("\\","/")
        self.__markdown=f"""---
title: {name}
author: {author}
abstract: "{description}"
description: "{description}"
cover-image: {cover_dir}
---

"""
    
    def appendChapter(self, title, description, text):
        self.__markdown+=f"""# {title}

## 前言

{description}

## 正文

{text}

"""

    def polish(self):
        self.__markdown=re.sub("\n{3,20}","\n\n",self.__markdown)
    
    def saveMarkdown(self, root):
        self.polish()
        root=os.path.abspath(root)
        file=os.path.join(root,self.name+".md")
        with open(file,"w",encoding="utf-8") as f:
            f.write(self.__markdown)
    
    def saveEPUB(self, root):
        self.polish()
        root=os.path.abspath(root)
        self.saveMarkdown(root)
        file=os.path.join(root,self.name+".md")
        out_file=os.path.join(root,self.name+".epub")
        cmd="start powershell "
        cmd+="chcp 65001;"
        cmd+="pandoc -i \"%s\" -o \"%s\" -s --toc -c default.css;"%(file, out_file)
        # cmd+="pause;"
        os.system(cmd)