import discord
import requests
from colorama import Fore
from colored import fg, attr
class colors:
    red = fg('#ff004d8')
    reset = attr('reset')
    gray = fg('#ff4b00')
    gray = fg('#ff4b00')
TOKEN = "ODMyMjI0MDU4ODM3ODI3NTg0.YHgrDQ.fDGDj9oFnkbLyMeemArMYH1ANdA"
client = discord.Client(intents=discord.Intents.all())
print(f'''
                                             {Fore.LIGHTBLACK_EX}█████{colors.gray}╗ {Fore.LIGHTBLACK_EX}██████{colors.gray}╗  {Fore.LIGHTBLACK_EX}██████{colors.gray}╗  {Fore.LIGHTBLACK_EX}██████{colors.gray}╗ 
                                            {Fore.LIGHTBLACK_EX}██{colors.gray}╔══{Fore.LIGHTBLACK_EX}██{colors.gray}╗╚════{Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╔═{Fore.LIGHTBLACK_EX}████{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╔═{Fore.LIGHTBLACK_EX}████{colors.gray}╗
                                            {Fore.LIGHTBLACK_EX}{colors.gray}╚{Fore.LIGHTBLACK_EX}█████{colors.gray}╔╝{Fore.LIGHTBLACK_EX} █████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║
                                            {Fore.LIGHTBLACK_EX}{Fore.LIGHTBLACK_EX}██{colors.gray}╔══{Fore.LIGHTBLACK_EX}██{colors.gray}╗ ╚═══{Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║
                                            {Fore.LIGHTBLACK_EX}{colors.gray}╚{Fore.LIGHTBLACK_EX}█████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝
                                             {colors.gray}╚════╝ ╚═════╝  ╚═════╝  ╚═════╝ 
                                       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
                                         ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  
''')
@client.event
async def on_connect():
   ask = int(input("server id: "))
   msg = input("what u wanna say?: ")
   guild = client.get_guild(ask)
   session = requests.Session()
   for member in guild.members:
      try:
        data = await member.create_dm()
        r = session.post(f"https://discord.com/api/v8/channels/{data.id}/messages", json={'content': f'{data.recipient.mention} '+msg}, headers={'Authorization': f'Bot {TOKEN}'})
        if r.status_code == 204 or 201 or 200:
           print(f"> DMED {data.recipient.name}")
      except:
        continue

client.run(TOKEN)
