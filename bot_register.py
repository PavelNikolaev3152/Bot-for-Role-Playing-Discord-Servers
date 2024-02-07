import discord
from discord import app_commands
from discord.ext import commands
from config import settings


class bot_client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild=discord.Object(settings['server_id']))
            self.synced = True
        print(f'We have logged in as {self.user}.')


client = bot_client()
tree = app_commands.CommandTree(client)


@tree.command(name='gmregister', description='Регестрация ГМ',
              guild=discord.Object(settings['server_id']))
@commands.has_role('ГМ')
async def self(interaction: discord.Interaction, gmname: str,
               age: str, hour: str,
               gameformat: str, gamesystem: str,
               gmexperience: str, timeconact: str):
    await interaction.response.send_message(f"""
Имя: {gmname}
Возраст: {age}
Время игры: {hour}
Формат игры: {gameformat}
Игровая система: {gamesystem}
Опыт введеня игр: {gmexperience}
""")


@tree.command(name='sendmessage', description='Малютка учится говорить',
              guild=discord.Object(settings['server_id']))
@commands.has_role('Админ')
async def self2(interaction: discord.Interaction, message: str):
    await interaction.response.send_message(f"{message}")


client.run(settings['token'])
