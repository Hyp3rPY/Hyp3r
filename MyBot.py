import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "?")

@client.event
async def on_ready():
	print("Bot is ready! ")

@client.command()
async def clear(ctx, amount=2):
	await ctx.channel.purge(limit=amount)

@client.command()
async def startgame(ctx):
	embed = discord.Embed(
		title = "The adventure of a hero! ",
		description = "In this fun game you will be faced with many choices that affects the outcome of your story",
		colour = discord.Colour.blue())
	embed.set_footer(text="Developed by Hyp3r", icon_url="")
	embed.set_image(url="https://images-ext-1.discordapp.net/external/FlEYHGk_pCctlP3MZSFRVOuz_csCahqiDoXDkLTAdMw/%3Ffit%3D2000%252C1211%26ssl%3D1/https/i0.wp.com/aaagameartstudio.com/wp-content/uploads/2018/08/hiddenobject-09-aaa-game-art-studio-hidden-object-objects-game-art-production-scene-sketch-render-texturing-studio-company-outsource-HO-external-development-paintover.png")
	embed.set_author(name="Adventure Bot", icon_url="")
	embed.add_field(name="Reactions", value="When faced with a choice reactions will appear in the form of ``A, B, C`` etc. React with the choice you want to go with and the story will progress!", inline=False)
	await ctx.channel.send(embed=embed)

client.run("Token")
