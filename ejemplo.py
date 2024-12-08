import discord
from discord.ext import commands

description='''este es un programa donde vamos a vincular a discord con visual studio code para lanzar imagenes'''

intents=discord.Intents.default()
intents.members=True
intents.message_content=True

bot=commands.Bot(command_prefix="/",description=description,intents=intents)

@bot.event
async def on_ready():
    print(f'logueado como {bot.user} (ID: {bot.user.id}) ')

@bot.event
async def on_message(message):
    if message.author==bot.user:
        return
    
    if message.content.lower()=="/sendmono":
        with open('mono.jpg', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(content="aqui esta la imagen de tu mono",file=picture)
   
            
    if message.content.lower()=="/sendmeme1":
        with open('image.jpg', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(content="aqui esta la imagen de tu meme",file=picture)
            
            
    if message.content.lower()=="/sendmeme2":
        with open('image1.jpg', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(content="aqui esta la imagen de tu meme",file=picture)
            
            
    if message.content.lower()=="/sendmeme3":
        with open('image2.jpg', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(content="aqui esta la imagen de tu meme",file=picture)
            
            
    if message.content.lower()=="/sendmeme4":
        with open('meme2.jpg', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(content="aqui esta la imagen de tu meme",file=picture)
    
    
    if message.content.lower()=="/sendmeme4":
        with open('meme2.jpg', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(content="aqui esta la imagen de tu meme",file=picture)
    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
bot.run("MTI0NDM0NDE2ODc1NTc2MTE4Mg.GdBn_U.SIqnIQ0GbWyfT8PnDjJSkXLsgf4MAaf-eDTrgc")








# Este fragmento nos permite leer la totalidad de un archivo de texto
f = open('text.txt', 'r', encoding='utf-8')
text = f.read()
print(text)
f.close()


# Y así es como podemos reescribir la totalidad de un archivo de texto
f = open('text.txt', 'w', encoding='utf-8')
text = 'perro'
f.write(text)
f.close()


# Y he aquí una versión más corta
with open('text.txt', 'r', encoding='utf-8') as f:
    print(f.read())
    
    
    