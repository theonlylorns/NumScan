import requests
import re
import os
import time
import sys
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import progressbar 
import subprocess
#import geocoder < - - - - - - - - - This To get Location For The One Who Use Your App ;)
from ipregistry import IpregistryClient
import socket   
from termcolor import colored
from colorama import init, Fore, Back, Style

init()

from sys import stdout
print(Fore.RED + Style.BRIGHT + "Hey")
api = 'xwg6wnkwctvw7n'
def print_slow(str):
        for letter in str:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.05)
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)    
print_slow("Your Computer Name - - - - - > " + hostname)  
client = IpregistryClient(api)  
ipInfo = client.lookup() 
cit=re.search(r'"city": "(.*?)"', str(ipInfo)).group(1)
ip =re.search(r'"ip": "(.*?)"', str(ipInfo)).group(1)
d=re.search(r'"domain": "(.*?)"', str(ipInfo)).group(1)
print(' ')
print(' ')
print_slow('Your Ip - - - - - > ' + ip)
print(' ')
print('')
print_slow('Your City - - - - - > ' + cit)
print('')
print('')
print_slow('Your Domain - - - - - > '+ d)
print('')
print('')
time.sleep(5)
try:

    networks = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])
    networks = networks.decode=("utf-8")
    networks = networks.replace('\r', '')
    ssid = networks.split('\n')
    ssid = ssid[4:]
    ssids = []
    x = 0

    while x < len(ssid):
        if x % 5 == 0:
            ssids.append(ssid[x])
        x += 1
    print_slow(ssids)  
except:
    print("Can't Get Your Wifi Name !")
    print('')
#g = geocoder.ip('me')
#print_slow('Your Location - - - - - - > ' + str(g.latlng))
print('')
print('')
time.sleep(4)
print(Fore.RED + Style.BRIGHT +'''

                               ,-.
                               | |
                               | |
                      ,-"""""""-.|
                     /  __:::__()\
                    J ."_______". L
                    JJ,"       ".LL
                    |J|         |L|
                    |||         |||
                    L||         ||J
                    LJ|@8r18    |LJ
                    LJ._________,LJ
                    L ___     ___ J
                    | \__)---(__/ |
                    J----(===)----L
                     L\ "-___-" /J
                     | "-------" |
                     |           |
                     |           |
                     |           |
                     |           |
                     |           |
                     |           |
                     |           |
                     |    ...    |
                     "-----------"



''')
print_slow('''WelCome
This Tool Is By instagram : @8r18 && @lordalgamdi < - - - - - - Upgrade it Or Just Use It
                     All Bruh To You (*_*)''')
print('')


def animated_marker(): 
      
    widgets = ['Scrap The Number: ', progressbar.AnimatedMarker()] 
    bar = progressbar.ProgressBar(widgets=widgets).start() 
      
    for i in range(50): 
        time.sleep(0.1) 
        bar.update(i) 
          




phone = input('Enter The Phone Num - - - - - > +966 ')
animated_marker() 
os.system('cls')
lastwonm = re.search(r'05\w\w\w\w\w\w(.*)', str(phone)).group(1)
withoutz = re.search(r'\w(.*)', str(phone)).group(1)
agent={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36'}
r = requests.session()
instagram = 'https://www.instagram.com/'
csg = r.get(instagram, headers=agent).headers
csrf = re.search(r'csrftoken=(.*?);', str(csg)).group(1)
hdinsta={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36',
    'x-csrftoken': csrf,
    'referer': 'https://www.instagram.com/accounts/password/reset/',
    'x-requested-with': 'XMLHttpRequest'
    
    }
dtinsta={
    'email_or_username': phone,
    'recaptcha_challenge_field': '',
    'flow': ''
    
    }

foundinsta = r.post('https://www.instagram.com/accounts/account_recovery_send_ajax/', data=dtinsta, headers=hdinsta).text
if ('We sent an SMS to') in foundinsta:
    print(Fore.RED + Style.BRIGHT +'Found Num In instagram - - - - - > ' + phone)
elif ('Please wait a few minutes before you try again') in foundinsta:
    print(Fore.RED + Style.BRIGHT +'Found Num In instagram - - - - - > ' + phone)
    time.sleep(3)
else:
    print('Not Found Num in instagram - - - - - > ' + phone)
    time.sleep(3)
snapchat = 'https://accounts.snapchat.com/accounts/password_reset/phone'
cg = r.get(snapchat, headers=agent).headers
cookies1 = re.search(r"'Set-Cookie': 'web_client_id=(.*?);", str(cg)).group(1)
cookies2 = re.search(r"'Set-Cookie': 'web_client_id=.*?;.*?xsrf_token=(.*?);", str(cg)).group(1)
snapf = 'https://accounts.snapchat.com/accounts/validate_phone_number'
dtsnap={
    'phone_number': phone,
    'phone_country_code': 'SA',
    'xsrf_token': cookies2,
    'g-recaptcha-response': '03AHaCkAYAC1g6xGRap0tIgFDWOOKxYFui0v9sfI0V7CHSvVYJawQCJLuQYS3FnOArzfOxdoMVOwEF05cP8k8Ft-pS06RXNGxRUZoUw5wT8tq17K3Su_obiyKmgIpkgf7jTu0lFbDEtLK4lAsd-rweqyxGuISTP5HNZRCln1TYkt6Mp4TIv9C7h45QLhJqEo031HO6IgF7FjJ_uEzGHhkP9j47AfQd6PvXJDTNKTLkqjLi654U5rrRQWincridLDEnOgEF5HfGi2tV2KpRBJYKdZH1NDJdDfAQfbO86q58eEbu9YLwUAKDXz91DC7Lk7S2rSnYgpbwZWJSPDGLKrmA00JFeOGyz44Q-5abNEBkPopM7QzOL5U4HK8zC9asWT9ffq6vyldD3gRG'
    }
hdsnap={
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36',
    'referer': 'https://accounts.snapchat.com/',
    'cookie': 'xsrf_token=' + cookies2 + ';'+'web_client_id=' + cookies1 + ';' + 'sc-cookies-accepted=true; Preferences=true; Performance=true; Marketing=true'
    }
foundsnap = r.post(snapf, data=dtsnap, headers=hdsnap).text
if ('Phone number is taken.') in foundsnap:
    print('')
    print(Fore.RED + Style.BRIGHT +'Found Num In Snapchat - - - - - > ' + phone)
    time.sleep(3)
else:
    print('')
    print('Not Found Num in SnapChat - - - - - > ' + phone)
    time.sleep(3)

email = 'https://accounts.google.com/_/lookup/accountlookup?hl=ar&_reqid=45934&rt=j'
hdemail={
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'content-length': '3772',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'cookie': 'SMSV=ADHTe-BzJyd6JgQUcS5vib1nMn8HvTcu8LU-XyPtOsizqm8yl0R75eM96KWQH4ducZ5tKo7PW3-oMLV8l_pRFFcUOAGXdfrMPWLocjeE-sG4mQ-v9oWlzu8; SEARCH_SAMESITE=CgQIp5EB; LSID=doritos|o.mail.google.com|o.myaccount.google.com|s.SA|s.blogger|s.youtube:4gcQaDvPM8CH-TP_YiQ4r5K-pQ20GwuJWGESj8QM2fEL-cMgQpg3zOTxYLbPQ4hndq_X9A.; __Host-3PLSID=doritos|o.mail.google.com|o.myaccount.google.com|s.SA|s.blogger|s.youtube:4gcQaDvPM8CH-TP_YiQ4r5K-pQ20GwuJWGESj8QM2fEL-cMgS6Vjk-9QkSy3NPaNjZ-JZQ.; HSID=Ah6sK0rhGbi3Db7UB; SSID=A5qkfzOlwrwGo0ORb; APISID=VU5DCZaxamCkW3NP/Ap6SJ2S6ccjOjYWv2; SAPISID=7FhwqDFh2I-omiAq/AhQb5N9dgL-xV1_vQ; __Secure-3PAPISID=7FhwqDFh2I-omiAq/AhQb5N9dgL-xV1_vQ; ACCOUNT_CHOOSER=AFx_qI6CSHftTYfqCgCitpeakmYCnzeA2bQSrmL8dZMTgiM6ZqEscVfxbeRaB6m19-m3zCD_6ALnZDDMkeqMbv25g8tPXmhR67f76EiAWI4E8N29Hw3M_-ee8qBkenvV6FxZYKt-vxlPlXgQGODfzro_PFvZc_sv13gri6kALmqbXi61jngKkzFMwEjVbXO1lcxxk6Zi92iK; CONSENT=YES+SA.ar+201909; SID=4gcQaCt0SMzVuXg6NLvnCdvJNAeJdsPm5xxnC4MZA_9zlt8WpnbcejqcTRTozedFxDYz0g.; __Secure-3PSID=4gcQaCt0SMzVuXg6NLvnCdvJNAeJdsPm5xxnC4MZA_9zlt8WzZoclJNBZtTNNFisr1JNTQ.; 1P_JAR=2020-12-15-09; NID=204=jiCc8f7fyffA4HvGDn7myFmkYMDEIrE6HOPCfV4QWi81CVWPTmKaTvFyEuElc5U3QxoUCInedBg-uvVVkBcfayyUEnhy_Ems5K-wvLPZ2vP3olSJs4LqZ3xeuj42sYrI4Gnj84y_uOx1m8WWnK7A51lTi0vQG5nfWmc3Gz4d3JnIJzI4-C6HZwSVBa9OAxxKqKbLbhD9CZp7rr8eEgZdls-1slkbvb_47IYzLXFvAdO-kIbpu5aX7j1dsQMaW6YS7no; __Host-GAPS=1:ORMvbpc3Cxu1iw_96AMkx2GnO9lxClp57FDBwRTdIxLqU_8ivYkEE4mtawn6DRKNNj_szTzBYvZDLVhj6wtbaaBXJud5Bw:PNIrKYNetqD62hjp; SIDCC=AJi4QfHn23fxo-qU2w2N4vUYJfMhobO1g94S5cXZvH1igCWJOcXGLxu5O0cPcihLjouAD0cFng; __Secure-3PSIDCC=AJi4QfFQhNsKdrbFzsaW6-h2Ox2NmM-yCpTjTTyqW3G-nw1rRmSyzAkgVLjssGnMirP9ImvzeA',
    'google-accounts-xsrf': '1',
    'origin': 'https://accounts.google.com',
    'referer': 'https://accounts.google.com/signin/v2/queryname?hl=ar&continue=https%3A%2F%2Fmail.google.com%2Fmail&service=mail&ec=GAlAFw&flowName=GlifWebSignIn&flowEntry=AddSession',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36',
    'x-same-domain': '1'
    }

dtemail={
    'continue': 'https://mail.google.com/mail',
    'service': 'mail',
    'hl': 'ar',
    'f.req': '[''"'+phone+'"'',"AEThLlwBlHDIMDVXBKsE2U9hO5np0i0EmMxViNTqn8DLLrDCjQjQ6JiLtOhs6NYPXeNSXo-Z7oabqI9Ot5iZikMsp4bgFJyhfA8ZFNgFBs60SjWqrVTFdTQ4TuML7ehGK_RvcIvbJoP51IZwrQIZPue1KzlNAZUZFWOVK7_pU0-yv6i-vfO4sb8_U2PdO2Tp0HioM5D88Oyj",[],null,null,"lord","lord",1,false,null,[null,null,[2,1,null,1,"https://accounts.google.com/AddSession?hl=ar&continue=https%3A%2F%2Fmail.google.com%2Fmail&service=mail&ec=GAlAFw",null,[],4,[],"GlifWebSignIn",null,[]],1,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[],null,null,null,[],[]],null,null,null,true],null,null,null,null,null,null,[]]',
    'bgRequest': '["username-recovery","!YmGlYUjNAAXj0ixo40IiAHyw3TETm1iN1fnxAW2bNwIAAAG_UgAAABtoAQeZBh8q6NHIUGdQirrTtonemF8GkmXsmNRgmZzKg9THZkq6_Z33vuj8JfzXIgx5h7YSfI8rczauoep1hxyxiKRTtdHStwoIqvwQu0GDvMSu0-GMgkSduqudvrhPhR_sspF_aqGECiGSvC64IIYsQ-sYalA7yGwiICMm1I4peJ4QmuqOeLRMPZRfCVuup2OM7_IIUwO1ksA5F78k8M7VoY82__X7EDU9bwVcihFr0o5ZrCXKMU-7kca2N94wyeJretEUXeR9TamSKW3U2YeffV45p-fPp33QxVML-_0re8A0UlG_1ARysce3H7CYqfk3Mkl3-99BdML_FPNlb5-0WIDFuH6mj9_ZMMcwNU-NcRLxUID5YM9V0obKNxsJ-SS6mglAx3KW-lAoJNcUbjZI8JWKvq_MVK62aO4Da_bjL96yPiCCrQJTPWYRJxcXRXHCBKCKFNPrFOLkUK7xHXeKFPZZma6oWvPNg9ZLg1eoodxM0mHZasF2yWxXAjwoDdw-GBUGDww_W6xoDOSwQWwi_VYE-orqTYePFoFC5gmdUK0o47M99C5sSVmN5Yyi6e7gWKzx6jJMQE_8_onedMeuDLvv7dGa3m73CsIupa1MPmZu6EoW5BafsIFilR9GlELMkYQXC4PTpf6QgAyd90T2LLpJ19UXiTMq9GGDUVOgeL4yf253cCuOT8ZhYvQPXH-5Qmy9r1Y3IIug5ip-xxjHUcvzC_XOVOL2dl0qmkD8ZRDyUVw51yyUCDkOzAu-IrUY1udMobFAZpONjsOUn1BqBFiEZFA8VnYYi4cPYQ5Mi-hYlefY1FhxHT6yRvSb4h-gpSO3GuiYkZYk5ycyBcDKsiKeh7bB9tjdoxP34sYgh14dV_mYPr3_e6pY49pAZagtoFlMmrK4S7I6dgFmEuknzV7E8Gwwmtk8sgFUzIKvexUTbjm4qa0Xi8Qe9Gdlx8XwwPIaC37bH0TybLMeaMJMkKmo_QfFThUdQXU-spySQj5o99noCswxZhlwZw2ZNwk1bQ0sOKKm7gEM70q80z43gcB1zb_1PiwlE8FiiOKxfobch75w8Cyk-2C14kG1yLJsz4PYF9aEIm-H-8z9qkb_JLGc-U47LrUBWeadB1IQuGVF-iK0lC3XBVEaimMofTBwNg20J760LNsSwIsvKZnIyJPUfv9yJk5X9lGk0n-87XudpJp-E1ierOnb1pAWBg8KWjlMjQzQcanfbibUOaEcmn2HlZGmVvgEzC6qFu9Vk4TgbDhrKSQ1xY13bqGVFoNjT_PoiPqOxf-BVX1Dj5-UfVp2VBJ4l_5LEk9q_diNa5EobqvhSpUWW74mb9X7Fhsa8g9X0457qFsgUQMAl_BNFT5WR6SXvHg4S7BPc3LsV8mrvltYxJL2P7rk4-P2y-S6GRc2NCJjNa8i7FEgD-a0-hW0Rgk2wrgKzKCSSyQFYJzKEqTzNtiammy3ISWTtZHz3s4oWB3g9S1wRbaQjuErQPV8oO6IBt1joXqNhS11Cf7ilZD-OhQMjbNgw6b5T50sTXYYT0ud1dY7GjAkwGQgxj88RMFzFk1X4elhhUzvvdEw1czI09q9ZqU4H0pxl0zLNIyfmWX8JQeEg5fA4olssncc_-f8P4RQL9aDjMT4mDDNTm2sekzuOSpdTWMLoCfPlBF5C-rr8Y9NdZhdbwNgm7TSZe967GEA4dpP_B2Ao9iTwyksufGjFnrzVkwDLkEgYeLV2X3RLyc17BxgBJvcEEy6z8GWac9unZP55W0IFHeBLeYeY21hAwQtkHSrHo8XkGEEkwqdfmnZl7NTm4wDA8L3bsevSrrdRjOgGuYQh4wVjxbwwphp9njGN7Ff7_ij5KZ3hGJL8Ld981qjzOAddOCC6R9zu2gRarOj9Auzu1SmOGs20-VJ7m0oGEsQziV01xeMKqcsRXJTmqOcrNbmeliDPfHqR171hC_WhzWRTuEXBXqww5WrCBKaQlCrGoTMbV-WavO-wHIqV1T4w4KLyjbac6xPU3byRTbnEdxEXKQsbRB-gwwdQwZYx2bx6UQ8cRiYTFoYZVkeed2b_81hzJOOYD3ZdmCojDfAP3SkCFYiJvlt"]',
    'at': 'AFoagUXLWMzNcUfKGf_K2_fkqkxY2wLTRg:1608025496526',
    'azt': 'AFoagUVFIiZx--35c5IDTS9BrfOeBvqplg:1608025496526',
    'cookiesDisabled': 'false',
    'deviceinfo': '[null,null,null,[],null,"SA",null,null,[],"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[],null,null,null,[],[]],null,null,null,null,2,null,false]',
    'gmscoreversion': 'undefined',
    'checkConnection': 'youtube:384:0',
    'checkedDomains': 'youtube',
    'pstMsg': '1'
    }
foundemail = r.post(email, data=dtemail, headers=hdemail).text
if ('يُرجى إدخال عنوان بريد إلكتروني أو رقم هاتف صالح') in foundemail:
    print('')
    print('Not Found Num in Email - - - - - > ' + phone)
    time.sleep(3)
    print('')
else:
    print('')
    print(Fore.RED + Style.BRIGHT +'Found Num in Email - - - - - > ' + phone)
    time.sleep(3)





twitter = 'https://twitter.com/account/begin_password_reset'
hdtiwit={
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'cache-control': 'max-age=0',
'cookie': '_sl=1; personalization_id="v1_8HR67vKTQ8FVjONj2mmA1g=="; guest_id=v1%3A160719378482004005; at_check=true; mbox=session#ea647a3cb75243d08272db60d50ed2b9#1607303352|PC#ea647a3cb75243d08272db60d50ed2b9.38_0#1670546293; ct0=45e20553d29d34b447fa835d48979bfc; gt=1339043747477270528; att=1-TGEnll9aQohZv842f7vHhakxTtvDWXe0NTgbXx74; _twitter_sess=BAh7CiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCJhZNzR2AToMY3NyZl9p%250AZCIlZWJiZDEyOWY5MjM5NmQyNjQzYWYwOGQ2ZWFiZmM2ZmY6B2lkIiUwYmM3%250AZjNiNzk3OWM0NWNkMTRmZDkzN2Q5ZDE1YTI5ZiIJcHJycCIA--0a7350c997dffea474dd6738ac5b77ca41add0e2; fm=V2UgZm91bmQgbW9yZSB0aGFuIG9uZSBhY2NvdW50IHdpdGggdGhhdCBwaG9u%250AZSBudW1iZXIuIFBsZWFzZSB0cnkgYWdhaW4gd2l0aCB5b3VyIHVzZXJuYW1l%250AIG9yIGVtYWlsLg%253D%253D--6bf96c51ecbe639da7edb8388c25ed8f705ec556',
'referer': twitter,
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'same-origin',
'sec-fetch-user': '?1',
'sec-gpc': '1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36'
    }
dttwit={
    'authenticity_token': '560d4242d28e65b0e9a00788e5f6a93502d519fe',
    'account_identifier': phone

    }

tiwt = r.post(twitter, data=dttwit, headers=hdtiwit).text
if ('We found more than one account with that phone number') in tiwt:
    print('')
    print(Fore.RED + Style.BRIGHT +'Found Num in Twitter - - - - - > ' + phone)
    time.sleep(3)
    print('')
elif ("We couldn't find your account with that information") in tiwt:
    print('')
    print('Not Found Num in Twitter - - - - - > ' + phone)
    time.sleep(3)
    print('')
elif ("You've exceeded the number of attempts. Please try again later.") in tiwt:
    print('')
    print('You Have Limt In Twitter - - - - - > ' + phone)
    time.sleep(3)
    print('')
else:
    print('')
    print(Fore.RED + Style.BRIGHT +'Found Num in Twitter - - - - - > ' + phone)
    time.sleep(3)
    print('')

telegram = 'https://venus.web.telegram.org/apiw1'

print('')
print_slow('Try To Text Him ;) - - - - - - > https://api.whatsapp.com/send?phone=966' + withoutz)
print('')
time.sleep(6)
try:
        all1 = "+966" + phone

        ro_number = phonenumbers.parse(all1, "en")

        Service = carrier.name_for_number(ro_number, "en")

        Gdd = geocoder.description_for_number(ro_number, "en")
        print(" ")
        print(Fore.RED + Style.BRIGHT +"Service - - - - - - > ", Service + Style.RESET_ALL + "\n")
        print('')
except:
        print("")
        print("Number Not Found...")

print(Fore.GREEN + Style.BRIGHT +'')
print_slow('Try This WebSite it is a NumberBook Search For Him ;) - - - - > https://storage.googleapis.com/ksa-n/index.html')
time.sleep(3)
print('')
print('')
input('''Finsh Press Enter To Exit...


___$$$___$$$____
__$$$$$_$$$$$___
__$$$$$$$$$$$___
____$$$$$$$_____
______$$$_______
_______$
_____¸.•´¸.•*¸.•*´¨`*•.♥
_____*.¸¸.•*¨`

Do you have additions? Contact me then instagram ( @8r18 )

---------------------------------------------------------
''')
# ما احللك تنسب السورس لنفسكك !