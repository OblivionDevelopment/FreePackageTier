# Free bot package for users
# Hello there, this the main infrastucture from any bot that you want to do with slash commands.
# In this case this one it's for Oblivion D&H users the free package base from scratch. From here we do magic and do bots like the ones we have in the server.
# Made with love by Oblivion Forgotten

import discord
from discord.ext import commands

TOKEN = 'YOUR_BOT_TOKEN_HERE' # YOU CAN ALSO USE .ENV, but in the free package we use it like that so we can host a single file not a whole pack or folder of files.

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents) # If you are doing it by your own, change "!" for any prfix you want. 

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Error syncing commands: {e}")

# Here's how we do the slash commands, with the tree sync function. Here's two silly but working command codes that work.

@bot.tree.command(name="hello", description="Says hello to the user.")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hello, {interaction.user.mention}! 👋")

@bot.tree.command(name="test", description="A simple test command.")
async def test(interaction: discord.Interaction):
    await interaction.response.send_message("This is a test command. Everything is working! ✅")

bot.run(TOKEN)
