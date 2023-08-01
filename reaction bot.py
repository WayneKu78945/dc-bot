import discord

client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
  print("bot is online")


@client.event
async def on_raw_reaction_add(payload):
  message_id = payload.message_id
  if message_id == 1128559165787357307:
    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

  if payload.emoji.name == "Hehe":
    role = discord.utils.get(guild.roles , name="test")
  elif payload.emoji.name == "IDK":
    role = discord.utils.get(guild.roles , name="野狗幫")


  if role is not None:
    member = await(await client.fetch_guild(payload.guild_id)).fetch_member(payload.user_id)
    if member is not None:
      await member.add_roles(role)
      print("done")
    else:
      print("Member not found.")
  else:
    print("role not found.")

@client.event
async def on_raw_reaction_remove(payload):
  message_id = payload.message_id
  if message_id == 1128559165787357307:
    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

  if payload.emoji.name == "Hehe":
    role = discord.utils.get(guild.roles , name="test")
  elif payload.emoji.name == "meh":
    role = discord.utils.get(guild.roles , name="要去網聚的")
  else:
    role = discord.utils.get(guild.roles , name=payload.emoji.name)

  if role is not None:
    member = await(await client.fetch_guild(payload.guild_id)).fetch_member(payload.user_id)
    if member is not None:
      await member.remove_roles(role)
      print("done")
    else:
      print("Member not found.")
  else:
    print("role not found.")

client.run("MTExNjc4MzU1MDc2MzYzMDY5Mg.Gcp7uh.umjggTiIgap_Mo_iaaFRYaSTNpgVURbqJqDamw")

