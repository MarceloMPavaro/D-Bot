import discord
 
#intents = discord.Intents.all() # --> caso algum comando pare de funcionar/apresente mal funcionamento, descomentar essa linha de código e comentar a linha abaixo
intents = discord.Intents.default()
intents.members = True
client = discord.Client(command_prefix='./', intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
 
@client.event
async def on_message(message):
    print(message.author)
    if message.author == client.user:
        return
    if message.content == str(message.author.id):
        await message.channel.send('Your ID matches')
    
    
 
client.run('MTA3MTg2MDQxMDgxMjIwMzAwOA.GbFlkQ.8dLzHLLmOaWTrer9G_-ETDfKP85nAOrM6oYuXg')