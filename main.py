import discord 
import time
from discord.ext import commands  # type: ignore
from discord import app_commands # type: ignore
import logging
from dotenv import load_dotenv # type: ignore
import os


load_dotenv()
token = os.getenv('DISCORD_TOKEN')
sleekID = os.getenv('sleecker')
teaID = os.getenv('tea')
suraID = os.getenv('sura')
ghostID = os.getenv('gh')


class Client(commands.Bot):
    async def on_ready(self):  
        print(f'Logged on as {self.user}!')
        
        botactivity = discord.Activity(type=discord.ActivityType.playing, name="Fortnite 67")
        await Client.change_presence(self, activity=botactivity)

        try:
            sleek = discord.Object(id=sleekID)
            tea = discord.Object(id=teaID)
            sura = discord.Object(id=suraID)
            gh = discord.Object(id=ghostID)

            a = await self.tree.sync(guild=sleek)
            b = await self.tree.sync(guild=tea)
            c = await self.tree.sync(guild=sura)
            d = await self.tree.sync(guild=gh)

            print(f'Synced {len(a)} commands to sleek {sleek.id}')
            print(f'Synced {len(b)} commands to tea {tea.id}')
            print(f'Synced {len(c)} commands to sura {sura.id}')
            print(f'Synced {len(d)} commands to gh {gh.id}')

        except Exception as e:
            print(f'Error syncing commands: {e}')


    async def on_message(self, message):
        strings = ["it migu", "its migu", "it's migu"]
        bad = ["stfu", "gtfo", "get out", "shut up"]
        
        text = message.content.casefold()

        # print(f'Message from {message.author}: {message.content}')
        if message.author == self.user:
            return

        if self.user in message.mentions:
            if not message.reference:
                if "miku" in text:
                    await message.reply("migu not miku!", mention_author=False)
                else:
                    await message.reply(f"migudayo!", mention_author=False)
            else:
                if "miku" in text:
                    await message.reply("migu not miku!", mention_author=False)
                else:
                    await message.reply("thats what im sayin!!", mention_author=False)

        if text == "migu":
            await message.reply(f'migudayo!', mention_author=False)

        for a in strings:
            if a in text:
                if text == "omg it migu":
                    await message.reply(f'yeee', mention_author=False)
                else:   
                    await message.reply(f'migudayo!', mention_author=False)

        if text.startswith('migu help'):
            await message.reply(f'Mention me or reply to me!\n' 
                                'React to any of my messages!\n'
                                'Say hi, bye, gm, or gn to me!\n\n'
                                'PS: if I work that means axe is on'
                                ' or his pc is sending his electric bill to the moon while he sleeps :D')


        if "gm migu" in text:
            await message.reply(f'gm {message.author}!', mention_author=False)

        if "gn migu" in text:
            await message.reply(f'gn {message.author}!', mention_author=False)

        if "hi migu" in text:
            await message.reply('https://tenor.com/view/miku-bestie-hi-hello-hi-bestie-gif-22693513', mention_author=False)

        if "bye migu" in text:
            await message.reply('https://tenor.com/view/bye-worstie-worstie-bye-miku-hatsune-miku-gif-22693524', mention_author=False)

        if "migudayo" in text:
             await message.reply("thats what im sayin!!", mention_author=True)

        if text.startswith('migu say'):
             s = f'{message.content}'
             s1 = s.replace("migu say", "")
             await message.delete()
             await message.channel.send(s1)

        if "massive" in text:
            await message.reply('https://tenor.com/view/ninja-fortnite-reaction-ninja-low-taper-fade-gif-1784137995500051652', mention_author=False)
        
        for b in bad:
            if b in text:
                if "migu" in text:
                    await message.reply("https://tenor.com/view/hatsune-miku-miku-hatsune-miku-angry-not-happy-gif-10473291184535189680", mention_author=False)
                else:   
                    return
                
        if message.author.id == 1362052078318653620:     
            if message.content == "haiiiiiii!":
                time.sleep(1)
                await message.channel.send('nani ga suki???')

    async def on_reaction_add(self, reaction, user):
        if reaction.message.author == self.user:
            if reaction.emoji == "❤️":
                await reaction.message.channel.send(':D')
            elif reaction.emoji == "🩵":
                await reaction.message.channel.send('yahoo!')
            elif reaction.emoji == "🖕":
                await reaction.message.channel.send("ah 🥷 don't hate me cause I'm beautiful 🥷")
                time.sleep(2)
                await reaction.message.channel.send("maybe if you got rid of that old yee-yee ass haircut you got you'd get some bitches on yo dick")
                time.sleep(3)
                await reaction.message.channel.send("oh better yet")
                await reaction.message.channel.send("maybe Tanisha'll call your dog ass if she ever stop f---n' with that brain surgeon or lawyer she f---g with")
                time.sleep(3)
                await reaction.message.channel.send("🥷aaaa")



intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
client = Client(command_prefix="!", intents=intents)

#slash commands I think---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
sleek = discord.Object(id=sleekID)
tea = discord.Object(id=teaID)
sura = discord.Object(id=suraID)
gh = discord.Object(id=ghostID)



gangserv = [sleek, tea, sura, gh]

@client.tree.command(name="hello", description="say hello", guilds=gangserv)
async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message("hello :D")
    time.sleep(2)
    await interaction.channel.send("that's it. that's the command")


@client.tree.command(name="say", description="the slash version of migu say", guilds=gangserv)
async def printer(interaction: discord.Interaction, text: str):
    await interaction.response.send_message(text)


@client.tree.command(name="inv", description="clone migu for your server (not recommended)", guilds=gangserv)
async def myButton(interaction: discord.Interaction):
    await interaction.response.send_message("you want more of them??", view=InviteMenu())


@client.tree.command(name="pat", description="pat", guilds=gangserv)
async def myButton(interaction: discord.Interaction):
    await interaction.response.send_message("https://tenor.com/view/hatsune-miku-hatsune-miku-miku-plushie-vocaloid-gif-8480003515036448258")

@client.tree.command(name="chocominto", description="bothers pepo", guilds=gangserv)
async def myButton(interaction: discord.Interaction):
    await interaction.response.send_message("pepo-chan!")


#embeds
#icon https://tinyurl.com/2bbbea33
#gif https://tinyurl.com/27wkw34t
#00fffb light blue
@client.tree.command(name="help", description="what does migu even do", guilds=gangserv)
async def embeddy(interaction: discord.Interaction):
    embed = discord.Embed(title="what does migu even do?", description=f"wip silly bot made with [A CODING LANGUAGE]\n"
                                                                        "not to be confused with Miku\n"
                                                                        "(don't try calling her that)", color=0x5dadec)
    embed.set_thumbnail(url="https://tinyurl.com/2bbbea33")
    embed.add_field(name=f"normal text", value="[gm, gn, hi, bye] migu\n"
                                                "migu [help, say]\n"
                                                "migu(!)\n"
                                                "replies and @mentions", inline=False)
    embed.add_field(name="reactions", value = "heart\n"
                                                "light_blue_heart\n"
                                                "very rude gesture\n", inline=False)
    embed.add_field(name="slash commands", value = "/hello\n"
                                                    "/help (this one)\n"
                                                    "/inv\n"
                                                    "/say\n")
    embed.set_footer(text="see also: pepo")
    embed.set_author(name='migu, made by axejpg', icon_url="https://tinyurl.com/26kxtqht")
    await interaction.response.send_message(embed=embed)
    


#button
class InviteMenu(discord.ui.View):
    @discord.ui.button(label = "migu generator", style=discord.ButtonStyle.primary)
    async def button_callback(self, button, interaction):
        await button.response.edit_message(content=f"have fun\nhttps://discord.com/oauth2/authorize?client_id=1361441336397529229", view=None)







    
    




#THE APP-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# client = Client(intents=intents)
client.run(token)


