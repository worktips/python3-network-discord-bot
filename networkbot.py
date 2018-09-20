# Python 3 cryptonote network stats discord bot
# Cryptonote network stats discord bot that displays a variety of network information and statistics on demand
# Version 1.0
#
# DEPENDENCIES
# sudo apt-get install python3
# sudo apt-get -y install python3-pip
# python3 -m pip install discord.py==0.16.12
#
# HOW TO USE
#  Go to https://discordapp.com/developers/applications/
#  Create an application
#  Go to 'Bot' section of discordapp.com/developers portal from the menu and add new bot
#  Get a bot token and add it to TOKEN value inside networkbot.py file
#  Go to 'Auth' section of discordapp.com/developers portal and mark the checkbox 'bot' to generate an invite link for your new bot. 
#  Visit that generated link to invite your bot to your Discord server.
#
# RUN THE BOT (run from command line)
# python3 networkbot.py

import random
import asyncio
import aiohttp
import json
from discord.ext.commands import Bot

# bot description 
# bot description displayed in help section
description = '''Network bot displays a variety of information and statistics on almost any cryptonote network. To use the commands type them with the prefix of ampersand (&). You can find the commands and their use below. Add (&) in front of a command (EXAMPLE: &height)'''

# bot prefix (&)
# prefix used to call your bot's commands
BOT_PREFIX = ("&")

# secret bot token
# never give your secret bot token to anyone
# get it at discordapp.com/developers/applications/me
TOKEN = "YOUR_SUPER_SECRET_BOT_TOKEN_GOES_HERE"

# daemon address
# address used to communicate with the network (127.0.0.1 for localhost)
HOST = "YOUR_DAEMON_ADDRESS_GOES_HERE"

# daemon RPC port
# port used to communicate with the network (your network's RPC port)
PORT = "YOUR_RPC_PORT_GOES_HERE"

# start a bot
client = Bot(command_prefix=BOT_PREFIX, description=description)

# commmand: &height
# network top block height
@client.command(description="Network top block height.", brief="Blockchain height.")
async def height():
    url = 'http://' + str(HOST) + ':' + str(PORT) + '/getheight'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("🌐 **Network height:** " + str(response['height']))

# commmand: &hash
# appx. network hash rate
@client.command(description="Appx. network hash rate.", brief="Network hash rate.")
async def hash():
    url = 'http://' + str(HOST) + ':' + str(PORT) + '/getinfo'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("🌐 **Network hash rate:** " + str(response['hashrate']) + " H/s")

# commmand: &diff
# current network difficulty
@client.command(description="Current network difficulty.", brief="Network difficulty.")
async def diff():
    url = 'http://' + str(HOST) + ':' + str(PORT) + '/getinfo'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("🌐 **Network difficulty:** " + str(response['difficulty']))

# commmand: &tx
# total network transactions
@client.command(description="Total network transactions.", brief="Network transactions.")
async def tx():
    url = 'http://' + str(HOST) + ':' + str(PORT) + '/getinfo'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("🌐 **Network transactions:** " + str(response['tx_count']))

# commmand: &txpool
# current transactions pool size
@client.command(description="Current transactions pool size.", brief="TX pool size.")
async def txpool():
    url = 'http://' + str(HOST) + ':' + str(PORT) + '/getinfo'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("🌐 **Transactions pool:** " + str(response['tx_pool_size']))

# commmand: &ver
# current daemon version
@client.command(description="Current daemon version.", brief="Daemon version.")
async def ver():
    url = 'http://' + str(HOST) + ':' + str(PORT) + '/getinfo'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("🌐 **Daemon Version:** " + str(response['version']))

# commmand: &stats
# key network stats all in one place
@client.command(description="Key network stats all in one place.", brief="Network stats.")
async def stats():
    url = 'http://' + str(HOST) + ':' + str(PORT) + '/getinfo'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("🌐  NETWORK STATS\n**Height:** " + str(response['height']) + "    \n**Hash rate:** " + str(response['hashrate']) + " H/s    \n**Difficulty:** " + str(response['difficulty']) + "    \n**TX total:** " + str(response['tx_count']) + "    \n**TX in the pool:** " + str(response['tx_pool_size']) + "    \n**Daemon version:** " + str(response['version'])
         )


# print list of servers where this bot is active to console
async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        # you can customize the output message(s) below
        print("--- BOT ONLINE ---")
        for server in client.servers:
            # you can customize the output message(s) below
            print('Active servers: ' + str(server.name))
        await asyncio.sleep(600)


client.loop.create_task(list_servers())
client.run(TOKEN)