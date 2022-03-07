import os
if not os.path.exists("./sswan"):
    os.makedirs("./sswan")

with open("servers.txt","r",encoding="utf-8") as f:
    a=f.readlines()

o=0
for i in a:
    if i=="\n":
        continue
    name,addr,id=i[:-1].split(", ")
    text="""{
        "uuid": "559eb893-1cee-4196-8b97-67045e029e%02d",
        "name": "%s",
        "type": "ikev2-eap",
        "remote": {
            "addr": "%s",
            "id": "%s"
        },
        "apps":[
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
    with open("./sswan/%s.sswan"%name,"w",encoding="utf-8") as f:
        f.write(text)
    o+=1