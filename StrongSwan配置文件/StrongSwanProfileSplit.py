import os

root=os.path.dirname(os.path.abspath(__file__))
folder_dir=os.path.join(root,"sswan\\Split")
if not os.path.exists(folder_dir):
    os.makedirs(folder_dir)

with open(os.path.join(root,"new_servers.txt"),"r",encoding="utf-8") as f:
    a=f.readlines()
# with open(os.path.join(root,"old_servers.txt"),"r",encoding="utf-8") as f:
#     a=f.readlines()

o=0
for i in a:
    if i=="\n":
        continue
    name,addr,id=i[:-1].split(", ")
    name="Split - "+name
    text="""{
        "uuid": "559eb893-1cee-4196-8b97-67045e029g%02d",
        "name": "%s",
        "type": "ikev2-eap",
        "remote": {
            "addr": "%s",
            "id": "%s"
        },
        "dns-servers" : "1.1.1.1 1.0.0.1 103.86.99.98 103.86.96.98",
        "apps":[
            "com.ximalaya.ting.himalaya",
            "tv.twitch.android.app",
            "dk.tacit.android.foldersync.full",
            "dk.tacit.android.foldersync.lite",
            "com.google.android.apps.maps",
            "com.google.android.syncadapters.contacts",
            "com.ovital.ovitalMap",
            "com.sorcerer.sorcery.iconpack",
            "com.google.android.youtube",
            "com.yandex.browser.alpha",
            "net.nurik.roman.muzei",
            "com.niksoftware.snapseed",
            "com.quora.android",
            "me.ghui.v2er",
            "be.mygod.vpnhotspot",
            "com.duolingo",
            "jp.pxv.android",
            "com.github.android",
            "com.google.android.apps.translate",
            "com.aimp.player",
            "com.rakin.camstellar",
            "com.nononsenseapps.feeder.play",
            "com.google.android.gm",
            "org.strongswan.android",
            "com.reddit.frontpage",
            "com.instagram.android",
            "org.readera",
            "org.thunderdog.challegram",
            "com.telegram.messenger",
            "com.gorillasoftware.everyproxy",
            "com.twitter.android",
            "com.redhome.sta",
            "com.spotify.music",
            "com.windyty.android",
            "com.catchingnow.icebox",
            "com.perol.play.pixez",
            "eu.thedarken.sdm",
            "com.androidvip.hebf",
            "com.noctuasoftware.stellarium_plus",
            "com.android.email",
            "com.streema.simpleradio",
            "jp.nicovideo.android",
            "com.melodis.midomiMusicIdentifier.freemium",
            "com.android.vending",
            "com.google.android.ext.services",
            "com.google.android.onetimeinitializer",
            "com.google.android.ext.shared",
            "com.google.android.overlay.modules.ext.services",
            "com.google.android.overlay.gmsconfig",
            "com.google.android.overlay.modules.documentsui",
            "com.google.android.gms",
            "com.google.android.gsf",
            "com.google.android.documentsui",
            "com.google.android.cellbroadcastservice.overlay.miui",
            "com.google.android.cellbroadcastreceiver.overlay.miui"
        ]
    }
    """%(o,name,addr,id)
    with open(os.path.join(folder_dir,"%s.sswan"%name),"w",encoding="utf-8") as f:
        f.write(text)
    o+=1