import os
import shutil
import random

root=os.path.dirname(os.path.abspath(__file__))
conf_folder=os.path.join(root,"conf")
if os.path.exists(conf_folder):
    shutil.rmtree(conf_folder)
os.makedirs(conf_folder)

PRIVATEKEY="PRIVATEKEY"
MAX_SAMPLE=10

# DEVICE="Android"
DEVICE="PC"

treasure_list=[
    # ("CountryName", "xxx.xxx.xxx", 1, 255, "PUBLICKEY")
]


for server in treasure_list:
    name=server[0]
    ip=server[1]
    start=server[2]
    end=server[3]
    public_key=server[4]

    country_folder=os.path.join(conf_folder,name)
    if not os.path.exists(country_folder):
        os.makedirs(country_folder)
    
    if end-start+1<MAX_SAMPLE:
        sample=end-start+1
    else:
        sample=MAX_SAMPLE
    
    for i in random.sample(range(start,end+1),sample):

        if DEVICE=="PC":
            conf=f"""[Interface]
PrivateKey = {PRIVATEKEY}
Address = 10.5.0.2/32
DNS = 103.86.99.98, 103.86.96.98

[Peer]
PublicKey = {public_key}
AllowedIPs = 0.0.0.0/0
Endpoint = {ip+".%s"%i}:51820
"""

        elif DEVICE=="Android":
            conf=f"""[Interface]
PrivateKey = {PRIVATEKEY}
Address = 10.5.0.2/32
DNS = 103.86.99.98, 103.86.96.98
IncludedApplications = com.google.android.apps.maps, com.google.android.syncadapters.contacts, com.ovital.ovitalMap, com.sorcerer.sorcery.iconpack, com.google.android.youtube, com.yandex.browser.alpha, net.nurik.roman.muzei, com.niksoftware.snapseed, com.quora.android, me.ghui.v2er, be.mygod.vpnhotspot, com.duolingo, jp.pxv.android, com.github.android, com.google.android.apps.translate, com.aimp.player, com.rakin.camstellar, com.nononsenseapps.feeder.play, com.google.android.gm, org.strongswan.android, com.reddit.frontpage, com.instagram.android, org.readera, org.thunderdog.challegram, com.gorillasoftware.everyproxy, com.twitter.android, com.redhome.sta, com.spotify.music, com.windyty.android, com.catchingnow.icebox, com.perol.play.pixez, eu.thedarken.sdm, com.androidvip.hebf, com.noctuasoftware.stellarium_plus, com.android.email, com.streema.simpleradio, jp.nicovideo.android, com.melodis.midomiMusicIdentifier.freemium, com.android.vending, com.google.android.ext.services, com.google.android.onetimeinitializer, com.google.android.ext.shared, com.google.android.overlay.modules.ext.services, com.google.android.overlay.gmsconfig, com.google.android.overlay.modules.documentsui, com.google.android.gms, com.google.android.gsf, com.google.android.documentsui, com.google.android.cellbroadcastservice.overlay.miui, com.google.android.cellbroadcastreceiver.overlay.miui,

[Peer]
PublicKey = {public_key}
AllowedIPs = 0.0.0.0/0
Endpoint = {ip+".%s"%i}:51820
"""

        with open(os.path.join(country_folder,"%s_%s.conf"%(name,i)),"w",encoding="utf-8") as f:
            f.write(conf)
        
        shutil.make_archive(os.path.join(conf_folder,name),"zip",country_folder)