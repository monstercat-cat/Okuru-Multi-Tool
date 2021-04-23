import requests, json
import os
import time

os.system(f'mode 55,10')
os.system(f'title [Okuru Multi-Tool] - Scrape')

createfriendsfile = open('Scraped/friends.json','w')
createfriendsfile.close()
createguildsfile = open('Scraped/guilds.json','w')
createguildsfile.close()
file = open('Scraped/friends.json','a')
guild = open('Scraped/guilds.json','a')
with open('settings.json') as f:
    config = json.load(f)
token = config.get('accountnuketoken')
headers = {'Authorization': token}
def scrape():
  r = requests.get('https://discord.com/api/v8/users/@me/relationships', headers=headers)
  for x in r.json():
    file.write(f'{x["id"]}\n')
  p = requests.get('https://discord.com/api/v8/users/@me/guilds', headers=headers)
  for t in p.json():
    guild.write(f'{t["id"]}\n')
    print("Scraping Info...")
    time.sleep(0.1)
    os.system('color 5')
    time.sleep(00.06)
    os.system('color 1')
    time.sleep(00.06)
    os.system('color 2')
    time.sleep(00.06)
    os.system('color 3')
    time.sleep(00.06)
    os.system('color 4')
    time.sleep(00.06)
    os.system('color 5')
    time.sleep(00.06)
    os.system('color 3')
    time.sleep(00.06)
    os.system('color 4')
    time.sleep(00.06)
    exit()
scrape()