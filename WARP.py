import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys
os.system("𝐖𝐀𝐑𝐏+  𝐒𝐂𝐑𝐈𝐏𝐓" + " 𝐌𝐀𝐃𝐄 𝐁𝐘 ​Ratul ")
os.system('cls' if os.name == 'nt' else 'clear')
#__________________[ SYS ]__________________#
sys.stdout.write('\x1b]2;)☢️WARP ☣️FREE♻️ GP🔰\x07')
print("                 \033[45m𝐖𝐀𝐑𝐏+  𝐒𝐂𝐑𝐈𝐏𝐓" + " 𝐌𝐀𝐃𝐄 𝐁𝐘 ​Ratul\033[40m")
print("""\033[32m
____    __    ____  ___      .______      .______          
\   \  /  \  /   / /   \     |   _  \     |   _  \     _   
 \   \/    \/   / /  ^  \    |  |_)  |    |  |_)  |  _| |_ 
  \            / /  /_\  \   |      /     |   ___/  |_   _|
   \    /\    / /  _____  \  |  |\  \----.|  |        |_|  
    \__/  \__/ /__/     \__\ | _| `._____|| _|             
                                                           """)
print ("              ⭕\033[31m\033[47m𝐀𝐁𝐎𝐔𝐓\033[40m\033[30m⭕")
print ("")
print ("")
print ("\033[37m{🔴} 🔺𝐒𝐂𝐑𝐈𝐏𝐓 𝐌𝐀𝐃𝐄 𝐁𝐘 ✴️\033[33m𝙍​̲𝙖​̲𝙩​̲𝙪​̲𝙡✴️")
print ("\033[37m{⚫} 🔺𝐕𝐄𝐑𝐒𝐎𝐍:\033[33m 🔸𝟰.𝟬🔸")
print ("\033[37m--------")
print ("\033[37m[⚪] 🔰𝐆𝐈𝐓𝐇𝐔𝐁: \033[33mDevil9809") 
print ("\033[37m[🔵] 🔰𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌: \033[33m@mdratulahmed")
print ("--------")
referrer = input("[💀] ⚠️\033[41m\033[37m𝐄𝐧𝐭𝐞𝐫 𝐘𝐨𝐮𝐫 𝐖𝐀𝐑𝐏+ 𝐈𝐃\033[40m:")
def genString(stringLength):
	try:
		letters = string.ascii_letters + string.digits
		return ''.join(random.choice(letters) for i in range(stringLength))
	except Exception as error:
		print(error)		    
def digitString(stringLength):
	try:
		digit = string.digits
		return ''.join((random.choice(digit) for i in range(stringLength)))    
	except Exception as error:
		print(error)	
url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'
def run():
	try:
		install_id = genString(22)
		body = {"key": "{}=".format(genString(43)),
				"install_id": install_id,
				"fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
				"referrer": referrer,
				"warp_enabled": False,
				"tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
				"type": "Android",
				"locale": "es_ES"}
		data = json.dumps(body).encode('utf8')
		headers = {'Content-Type': 'application/json; charset=UTF-8',
					'Host': 'api.cloudflareclient.com',
					'Connection': 'Keep-Alive',
					'Accept-Encoding': 'gzip',
					'User-Agent': 'okhttp/3.12.1'
					}
		req         = urllib.request.Request(url, data, headers)
		response    = urllib.request.urlopen(req)
		status_code = response.getcode()	
		return status_code
	except Exception as error:
		print(error)	

g = 0
b = 0
while True:
	result = run()
	if result == 200:
		g = g + 1
		os.system('cls' if os.name == 'nt' else 'clear')
		print("")
		print("                  \033[45m𝐖𝐀𝐑𝐏+  𝐒𝐂𝐑𝐈𝐏𝐓" + " 𝐌𝐀𝐃𝐄 𝐁𝐘 𝙋​̲𝙧​̲𝙤​̲𝙛​̲𝙚​̲𝙨​̲𝙨​̲𝙤​̲𝙧​̲ ​̲𝙍​̲𝙖​̲𝙩​̲𝙪​̲𝙡\033[40m")
		print("")
		animation = ["\033[30m[■□□□□□□□□□] 10%","\033[34m[■■□□□□□□□□] 20%", "\033[33m[■■■□□□□□□□] 30%", "\033[32m[■■■■□□□□□□] 40%", "\033[31m[■■■■■□□□□□] 50%", "\033[39m[■■■■■■□□□□] 60%", "\033[37m[■■■■■■■□□□] 70%", "\033[36m[■■■■■■■■□□] 80%", "\033[35m[■■■■■■■■■□] 90%", "\033[34m[■■■■■■■■■■] 100%"] 
		for i in range(len(animation)):
			time.sleep(0.5)
			sys.stdout.write("\r[💀] ☢️𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠... " + animation[i % len(animation)])
			sys.stdout.flush()
		print(f"\n[-] 🤗𝐖𝐎𝐑𝐊 𝐎𝐍 𝐈𝐃: {referrer}")    
		print(f"[:)] {g} 🛡️𝐆𝐁 𝐒𝐔𝐂𝐂𝐄𝐒𝐒𝐅𝐔𝐋𝐋𝐘 𝐀𝐃𝐃 𝐓𝐎 𝐘𝐎𝐔𝐑 𝐀𝐂𝐂𝐎𝐔𝐍𝐓⚪.")
		print(f"[#] 💀𝐓𝐎𝐓𝐀𝐋: {g} 🤯\033[41m𝐆𝐎𝐎𝐃\033[40m {b} 🥺\033[41m𝐁𝐀𝐃\033[40m")
		print("[*] ⏸️\033[43m𝐀𝐟𝐭𝐞𝐫 05 𝐒𝐞𝐜𝐨𝐧𝐝𝐬, 𝐀 𝐍𝐞𝐰 𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐖𝐢𝐥𝐥 𝐁𝐞 𝐒𝐞𝐧𝐭\033[40m.")
		print("""\033[36
▒██   ██▒▓██   ██▓ ██▓     ▒█████   ███▄    █ 
▒▒ █ █ ▒░ ▒██  ██▒▓██▒    ▒██▒  ██▒ ██ ▀█   █ 
░░  █   ░  ▒██ ██░▒██░    ▒██░  ██▒▓██  ▀█ ██▒
 ░ █ █ ▒   ░ ▐██▓░▒██░    ▒██   ██░▓██▒  ▐▌██▒
▒██▒ ▒██▒  ░ ██▒▓░░██████▒░ ████▓▒░▒██░   ▓██░
▒▒ ░ ░▓ ░   ██▒▒▒ ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
░░   ░▒ ░ ▓██ ░▒░ ░ ░ ▒  ░  ░ ▒ ▒░ ░ ░░   ░ ▒░
 ░    ░   ▒ ▒ ░░    ░ ░   ░ ░ ░ ▒     ░   ░ ░ 
 ░    ░   ░ ░         ░  ░    ░ ░           ░ 
          ░ ░                                """)
		time.sleep(05)
	else:
		b = b + 1
		os.system('cls' if os.name == 'nt' else 'clear')
		print("")
		print("                  \033[45m𝐖𝐀𝐑𝐏+  𝐒𝐂𝐑𝐈𝐏𝐓" + " 𝐌𝐀𝐃𝐄 𝐁𝐘 Ratul\033[40m")
		print("")
		print("[:(] Error when connecting to server.")
		print(f"[#] 𝐓𝐎𝐓𝐀𝐋: {g} 🤯𝐆𝐎𝐎𝐃 {b} 🥺𝐁𝐀𝐃")