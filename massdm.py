import discord
import requests
from colorama import Fore
import threading
import time
from colored import fg


def SendMessage(recipient_id, user, session: requests.Session, content):
  res = session.post(f"https://discord.com/api/v8/channels/{recipient_id}/messages", json={ 'content': f'{user.mention} '+content}, headers={ "Authorization": "Bot "+TOKEN})
  if res.status_code == 204 or 200 or 201:
    print(f"Sent message to {user.name}")
  elif res.status_code == 429:
    time.sleep(res.json()['retry_after'])
    SendMessage(recipient_id, user, session, content)
 
class MassDm(discord.Client):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.color = fg('#ff4b00')
    self.session = requests.Session()
    self.ansi = """
                                             █████╗ ██████╗  ██████╗  ██████╗ 
                                            ██╔══██╗╚════██╗██╔═████╗██╔═████╗
                                            ╚█████╔╝ █████╔╝██║██╔██║██║██╔██║
                                            ██╔══██╗ ╚═══██╗████╔╝██║████╔╝██║
                                            ╚█████╔╝██████╔╝╚██████╔╝╚██████╔╝
                                             ╚════╝ ╚═════╝  ╚═════╝  ╚═════╝ 
                                       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                         ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  
                                        """.replace("█", f"{Fore.LIGHTBLACK_EX}█{self.color}")

  async def on_connect(self):
    print(self.ansi)
    guild_id = int(input("Server ID: "))
    message = str(input("Mass Dm Message: "))
    guild = self.get_guild(guild_id)
    for member in guild.members:
      try:
        data = await member.create_dm()
        threading.Thread(target=SendMessage, args=(data.id, data.recipient, self.session, message,)).start()
      except:
        continue


client = MassDm(intents=discord.Intents.all())
TOKEN = open('Token.txt', 'r').readline()
client.run(TOKEN)