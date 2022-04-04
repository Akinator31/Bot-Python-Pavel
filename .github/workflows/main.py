from email import message
from time import sleep
from tracemalloc import stop
from turtle import delay
import discord
from discord.ext import commands
import datetime

from urllib import parse, request
import re

bot = commands.Bot(command_prefix='!', description="This is a Helper Bot")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Lorem Ipsum asdasd", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")

    await ctx.send(embed=embed)

@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    # print(html_content.read().decode())
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    print(search_results)
    # I will put just the first result, you can loop the response to show more results
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

# Events
@bot.event
async def on_ready():
    print('Le bot est prêt')


@bot.listen()
async def on_message(message):
    if "tutorial" in message.content.lower():
        # in this case don't respond with the word "Tutorial" or you will call the on_message event recursively
        await message.channel.send('This is that you want http://youtube.com/fazttech')
        await bot.process_commands(message)



@bot.command()
async def python(ctx):
    await ctx.send("Ouai c'est cool python mon grand")


@bot.command()
async def yo(ctx):
    await ctx.send("Salut ça va ?")

@bot.event
async def on_message(message):
    """ some on_message command """
    if message.author.id == bot.user.id:
        return
    msg_content = message.content.lower()

    curseWord = ['connard de merde', 'fdp']
    
    # delete curse word if match with the list
    if any(word in msg_content for word in curseWord):
        messages_interdit = "MOT INTERDIT PTN"
        await message.channel.send(messages_interdit)
        await sleep(3)
        await messages_interdit.delete(messages_interdit)
        await message.delete(message)
        await message.delete(message.channel.send)
    


        
bot.run('OTU4OTg2NjQwMzU1OTEzNzI4.YkVT6A.UpbNHuiE6FJbV7hgNwjAFMlNNKk')
