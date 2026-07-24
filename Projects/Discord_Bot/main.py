import discord

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if message.author == self.user:
            return
        if message.content.lower().startswith('hello'):
            await message.channel.send(f'Hi there {message.author}!')
    async def on_reaction_add(self, reaction, user):
        await reaction.message.channel.send(f'{user} reacted')

intents = discord.Intents.default()
intents.message_content = True
client = Client(intents=intents)
client.run('MTUyMjY2MTgzOTUzNDU1NTI1Nw.GVnpoC.St5DZAuA9uX945Tr68DHTaqQKt4gAvZwkMRJ0E')
