# 检查这几项
# ^(?!.*?_).*$
# ^</Cell>
# ^(?!<Row>).*

file_and_method=[
    ("text_rich_presence.xml"           ," "),
    ("text_ui_dialog.xml"               ," &lt;br/&gt; "),
    ("text_ui_HUD.xml"                  ," "),
    ("text_ui_ingame.xml"               ," "),
    ("text_ui_items.xml"                ," "),
    ("text_ui_menus.xml"                ," "),
    ("text_ui_minigames.xml"            ," "),
    ("text_ui_misc.xml"                 ," &lt;br/&gt; "),
    ("text_ui_quest.xml"                ," &lt;br/&gt; "), # 任务
    ("text_ui_soul.xml"                 ," "), # 名词
    ("text_ui_tutorials.xml"            ," &amp;lt;br/&amp;gt; ")
]

for thing in file_and_method:
    file=thing[0]
    method=thing[1]

    with open("./ch/"+file,"r",encoding="utf-8") as f:
        a=f.readlines()
    trans_dict={}
    offset1=len("<Row><Cell>")
    offset2=len("<Cell>")
    for i in range(1,len(a)-1):
        t=a[i]
        b1=offset1
        e1=t.find("</Cell><Cell>")
        key=t[b1:e1]
        b2=t.rfind("<Cell>")+offset2
        e2=t.rfind("</Cell>")
        value=t[b2:e2]
        trans_dict[key]=value

    with open("./en/"+file,"r",encoding="utf-8") as f:
        a=f.readlines()
    offset1=len("<Row><Cell>")
    offset2=len("<Cell>")
    error=""
    for i in range(1,len(a)-1):
        t=a[i]
        
        if file=="text_ui_ingame.xml" and "_shortcut" in t: # 方位NESW不用翻译
            continue
        if file=="text_ui_menus.xml" and "ui_copyright_menu" in t: # 版本不用翻译
            continue
        if file=="text_ui_menus.xml" and "ui_key_" in t: # 键不用翻译
            continue
        if file=="text_ui_menus.xml" and "ui_hour" in t: # 小时不用翻译
            continue
        
        b1=offset1
        e1=t.find("</Cell><Cell>")
        key=t[b1:e1]
        try:
            trans=trans_dict[key]
            b2=t.rfind("<Cell>")+offset2
            e2=t.rfind("</Cell>")
            orig=t[b2:e2]
            
            if file=="text_ui_menus.xml" and "ui_codex_cont" in t: # codex是要换行的
                method=" &lt;br/&gt;&amp;nbsp;&lt;br/&gt; "
            else:
                method=thing[1]
            
            a[i]=t[:b2]+trans+method+orig+t[e2:]
        except:
            error+=key+"\n"
            if "_" not in key:
                print(key)

    with open("./merge/"+file,"w",encoding="utf-8") as f:
        f.writelines(a)

    with open("error-%s.txt"%file,"w",encoding="utf-8") as f:
        f.writelines(error)