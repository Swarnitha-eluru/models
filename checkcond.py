import re
#x = 'https://scontent.xx.fbcdn.net/v/t1.0-0/s130x130/44830409_2172218639456890_1127361733321555968_n.jpg?_nc_cat=110&_nc_ht=scontent.xx&oh=30a9d9ffe02e246c1026b6d8f75e6a53&oe=5C52D290'
#x = 'https://78.media.tumblr.com/1b39dfc7b8803331e0b506170f4f8f26/tumblr_oj81lyWXqQ1udfmseo3_1280.png'
#x = 'http://pbs.twimg.com/media/DsUqyjNWkAIpRVV.jpg'
#x = 'https://www.facebook.com/Harsimratkaurbadal/photos/a.286854861326620/2172218622790225/?type=3'
#x = 'https://pmcdeadline2.files.wordpress.com/2018/01/connie-sawyer.jpg?w=446&h=299&crop=1'
#x = 'https://pbs.twimg.com/card_img/1090626362799415296/1I-CH7HG?format=jpg&name=600x314'
x = 'https://www.facebook.com/Harsimratkaurbadal/photos/a.286854861326620/2172218622790225/?type=3'
print(x)
#if(re.match('.*jpg.*\w+',x)):
if(re.match('https://www.facebook.com/\W+/photos/\S.\d+/\d+/',x)):
    print(x)
else:
    print("---")


#facebook links output obtained
#https://www.facebook.com/TELUGUYUVATHABULLETS/photos/a.1634672210080089/2241703949376909/?type=3&eid=ARBtzPaNmDFR-EK9QmRpCa3PL3rLeUlkslgB5dDQH77pCgkWQ-sL0g5wI2QaEqYqiseZu0NGyyXViyWg&__xts__%5B0%5D=68.ARD9brNkz5moJcdv-2bTS52Mt28RGNxC2-FYp6__Tuugcm2MAqyxZ0Q1WZ3bqlqlhNbnQNj3SA91aAWvf4y-0H9MhgwBPm83gtPy7-kkOqW_7LmHRVpq_eY6qa8SOHOAOIG2xdISqWS38HugpbG62Y0FBBHYzMPfX_fD8JSHfOpj08dE7C35zlYmUGvGVkRlKAxPkpsG9HT9xaMfubr0oPTfBFLncAP5tGYuT1QZmpDtV-hB6Nz1oro6lFWulOuPmJSy08IrIKvk8AdoqaiyTGfpUQrYoGpblduThuwmy7_hBObyEpaey8xsW0buf7Zyv4oCitA_TgaPM_ROjDJ6xslCNDrvgcSyxTcL5-vBYb-WRk69-Rwg-ImF&__tn__=EEHH-R
#https://www.facebook.com/photo.php?fbid=1920637818049251&set=gm.1322867307851049&type=3&eid=ARAzsoJnb-7Wv8omiZMvcoDxUWsozyNJ5LEIwLSKDWQguEGyXlIeQCgQd3bsEWHi6mNxb-YNSKq_8xPP
#
