import os
import db_acsess
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
GUILD = os.getenv('GUILD')
print(GUILD)
db_acsess.init_db()

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

black_list = []


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all requirements :rolling_eyes:.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have all the requirements :angry:")


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has been kick due inappropriate language')


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'User {member} has been baned due inappropriate language')


@bot.event
async def on_message(message):
    global black_list
    bads = db_acsess.get_curses()
    for bad in bads:
        if bad in message.content:
            print("found bad :(")
            ctx = await bot.get_context(message)
            if message.author not in black_list:
                print(black_list)
                black_list.append(message.author)
                await ctx.invoke(bot.get_command('kick'), member=message.author, reason='Using inappropriate language')
            else:
                await ctx.invoke(bot.get_command('ban'), member=message.author, reason='Using inappropriate language')
            return  # Exit after banning to prevent multiple bans for the same message
    await bot.process_commands(message)


bot.run(TOKEN)
