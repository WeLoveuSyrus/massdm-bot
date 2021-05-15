import discord, requests, asyncio
from colorama import Fore, fg, atrr
from colored import fg, attr

class colors:
    red = fg('#ff004d8')
    reset = attr('reset')
    gray = fg('#ff4b00')
    gray = fg('#ff4b00')

TOKEN = input("insert token: ")
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


async def senddm(data, msg):
    r = requests.post(f"https://discord.com/api/v8/channels/{data.id}/messages", json={'content': f'{data.recipient.mention}, {msg}'}, headers={'Authorization': f'Bot {TOKEN}'})
    if r.status_code == 204 or 201 or 200:
        print(f"> DMED {data.recipient.name}")
    elif r.status_code == 429:
        print(f"> RATELIMITED FOR {r.json()['retry_after']} SECONDS")
        await asyncio.sleep(r.json()['retry_after'])
        await senddm(data, msg)

@client.event
async def on_connect():
   ask = int(input("server id: "))
   msg = input("what u wanna say?: ")
   guild = client.get_guild(ask)
   for member in guild.members:
      try:
        data = await member.create_dm()
        await senddm(data, msg)
      except:
        continue

client.run(TOKEN)
