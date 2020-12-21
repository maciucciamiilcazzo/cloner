import discord
from discord.ext import commands

class Cloner(commands.Cog):

	def __init__(self, bot):

		self.bot = bot

	@commands.command()
	@commands.has_permissions(administrator = True)
	async def clone(self, ctx, guild_id: int):

		guild2 = ctx.guild

		try:
			guild1 = self.bot.get_guild(guild_id)

		except:
			return await ctx.send("Guild not found.")

		for a in guild2.text_channels:
			await a.delete()

		for a in guild2.voice_channels:
			await a.delete()

		for a in guild2.categories:
			await a.delete()
			
		for a in guild2.roles:
			try:
				await a.delete()
			except:
				pass

		for a in guild1.categories:
			await guild2.create_category(name = a.name)

		for a in guild1.text_channels:
			cat = discord.utils.get(guild2.categories, name = a.category.name)
			await guild2.create_text_channel(name = a.name, category = cat, position = a.position, topic = a.topic, slowmode_delay = a.slowmode_delay)

		for a in guild1.voice_channels:
			cat = discord.utils.get(guild2.categories, name = a.category.name)
			await guild2.create_voice_channel(name = a.name, category = cat, position = a.position, user_limit = a.user_limit, bitrate = a.bitrate)
		
		roles = guild1.roles
		roles.reverse()
		for a in roles:
			if a != guild1.default_roles:
				await guild2.create_role(name=role.name, color=role.color, permissions=role.permissions)
			else:
				await guild2.default_role.edit(permissions=a.permissions)

		await ctx.author.send("Done!")

def setup(bot):
	bot.add_cog(Cloner(bot))
