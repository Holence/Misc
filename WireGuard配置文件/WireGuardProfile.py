import os
import shutil
import random

PRIVATEKEY="PRIVATEKEY"
MAX_SAMPLE=5

# DEVICE="Android"
DEVICE="PC"

root=os.path.dirname(os.path.abspath(__file__))
conf_folder=os.path.join(root,"conf_%s"%DEVICE)
if os.path.exists(conf_folder):
    shutil.rmtree(conf_folder)
os.makedirs(conf_folder)

treasure_list=[
    ("COUNTRY_a",  "xxx.xxx.xxx",   1, 255,   8,   12,  "PUBLICKEY"),
    ("COUNTRY_b",  "xxx.xxx.xxx",   1, 255,   0,    1,  "PUBLICKEY"),
    ("COUNTRY_c",  "xxx.xxx.xxx",   [1,50,100,150,200], None, 8, False, "PUBLICKEY"),
    ("COUNTRY_d",  "xxx.xxx.xxx",   [1,50,100,150,200], None, 8, True, "PUBLICKEY"),
]

ip_full_file=open(os.path.join(root,"ip_full_list.txt"),"w")
ip_sample_file=open(os.path.join(root,"ip_sample_list.txt"),"w")

for ip_range in treasure_list:
    name=ip_range[0]
    ip_prefix=ip_range[1]
    start=ip_range[2]
    end=ip_range[3]
    step=ip_range[4]
    skip=ip_range[5]
    public_key=ip_range[6]

    server_folder=os.path.join(conf_folder,name)
    if not os.path.exists(server_folder):
        os.makedirs(server_folder)
    
    ip_list=[]
    if type(start)==int:
        while True:
            o=start
            for i in range(step+1):
                ip=ip_prefix+".%s"%o
                ip_list.append(ip)
                ip_full_file.write(ip+"\n")
                o+=1
            start+=skip
            if start>end:
                break
    elif type(start)==list:
        # 第六位这时候的True或False决定是否跳过该列表中的元素（列表中的大都被墙了，如果占比较大的话可以考虑跳过）
        if skip==False:
            for i in start:
                o=i
                for j in range(step+1):
                    ip=ip_prefix+".%s"%o
                    ip_list.append(ip)
                    ip_full_file.write(ip+"\n")
                    o+=1
        else:
            for i in start:
                o=i+1
                for j in range(step):
                    ip=ip_prefix+".%s"%o
                    ip_list.append(ip)
                    ip_full_file.write(ip+"\n")
                    o+=1


    if len(ip_list)<MAX_SAMPLE:
        sample=len(ip_list)
    else:
        sample=MAX_SAMPLE
    
    for i in random.sample(ip_list,sample):

        if DEVICE=="PC":
            conf=f"""[Interface]
PrivateKey = {PRIVATEKEY}
Address = 10.5.0.2/32
DNS = 103.86.99.98, 103.86.96.98

[Peer]
PublicKey = {public_key}
AllowedIPs = 0.0.0.0/0
Endpoint = {i}:51820
"""

        elif DEVICE=="Android":
            conf=f"""[Interface]
PrivateKey = {PRIVATEKEY}
Address = 10.5.0.2/32
DNS = 103.86.99.98, 103.86.96.98
IncludedApplications = com.google.android.apps.maps, com.google.android.syncadapters.contacts, com.ovital.ovitalMap, com.sorcerer.sorcery.iconpack, com.google.android.youtube, com.yandex.browser.alpha, net.nurik.roman.muzei, com.niksoftware.snapseed, com.quora.android, me.ghui.v2er, be.mygod.vpnhotspot, com.duolingo, jp.pxv.android, com.github.android, com.google.android.apps.translate, com.aimp.player, com.rakin.camstellar, com.nononsenseapps.feeder.play, com.google.android.gm, org.strongswan.android, com.reddit.frontpage, com.instagram.android, org.readera, org.thunderdog.challegram, com.telegram.messenger, com.gorillasoftware.everyproxy, com.twitter.android, com.redhome.sta, com.spotify.music, com.windyty.android, com.catchingnow.icebox, com.perol.play.pixez, eu.thedarken.sdm, com.androidvip.hebf, com.noctuasoftware.stellarium_plus, com.android.email, com.streema.simpleradio, jp.nicovideo.android, com.melodis.midomiMusicIdentifier.freemium, com.android.vending, com.google.android.ext.services, com.google.android.onetimeinitializer, com.google.android.ext.shared, com.google.android.overlay.modules.ext.services, com.google.android.overlay.gmsconfig, com.google.android.overlay.modules.documentsui, com.google.android.gms, com.google.android.gsf, com.google.android.documentsui, com.google.android.cellbroadcastservice.overlay.miui, com.google.android.cellbroadcastreceiver.overlay.miui,

[Peer]
PublicKey = {public_key}
AllowedIPs = 0.0.0.0/0
Endpoint = {i}:51820
"""
        ip_sample_file.write(i+"\n")
        with open(os.path.join(server_folder,"%s_%s.conf"%(name,i.split(".")[-1])),"w",encoding="utf-8") as f:
            f.write(conf)
        
        shutil.make_archive(os.path.join(conf_folder,name),"zip",server_folder)

ip_full_file.close()
ip_sample_file.close()