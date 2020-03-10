import discord
import random
from discord.ext import commands

command_prefix = 'r.'
client = commands.Bot(command_prefix)


@client.event
async def on_ready():
    print('Bot ready.')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')


@client.event
async def on_message(message):
    print('author: ', message.author, " client.user: ", client.user, " content: ", message.content)

    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == command_prefix + '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

    elif '<@!342363066874200076>' in message.content:  # Called when @Red is mentioned
        response = 'Red is not available at the moment, you can talk to me instead! 😃'
        await message.channel.send(response)

    elif '<@!686229539709648956>' in message.content:  # Called when @Red is mentioned
        response = 'Aha?'
        await message.channel.send(response)


client.run('Njg2MjI5NTM5NzA5NjQ4OTU2.XmeNwA.cfU8X6j5oCK9I1PghpXw2maY2mw')
