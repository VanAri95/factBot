import discord
import requests
from bs4 import BeautifulSoup
import random
import logging

logging.basicConfig(level=logging.DEBUG)

# Set Discord client with necessary intents
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

#Channel ID
channel_id = 123456789

# Define a function to scrape a random fact from Only Fun Facts
def get_fact():
    url = "https://uselessfacts.jsph.pl/random.json?language=de"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        fact = data["text"]
    except requests.exceptions.RequestException as e:
        logging.error(f"Error: {e}")
        fact = "Sorry, there was an error retrieving the fact."
    except KeyError as e:
        logging.error(f"Error: {e}")
        fact = "Sorry, there was an error parsing the fact data."
    return fact

# Define event listener when bot is ready
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    channel = client.get_channel(channel_id)
    print(channel) #Checking if channel object is retrieved successfully

# Define event listener when a message is received
@client.event
async def on_message(message):
    print(message.content)  
    if message.content.startswith('!fact'):
        print('Received !fact command')
        channel = client.get_channel(channel_id)
        if channel is not None and not isinstance(channel, discord.abc.PrivateChannel):
            fact = get_fact()
            await channel.send(f"{message.author.mention} sagt: {fact}")

# Start the bot
client.run('BotToken')




