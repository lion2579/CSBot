import discord
import CsBotInfo
import datetime

client = discord.Client()
welcomeMessage = """
Hi there {}, welcome to the server!

Check out the announcements section for important information.
"""

# Logging information for start-up.
@client.event
async def on_ready():
    print("I'm all set as {0.user}.".format(client))
    if len(client.guilds) == 0:
        print("I'm not in any servers.")
    else:
        print("I'm in the server/servers:", end = "")
        for item in client.guilds:
            print(" " + item.name, end = "")
        print(".")

# Logs new users and sends the welcome message.
@client.event
async def on_member_join(member):
    print(f"Recognized {member.name} joined a server on {datetime.datetime.now(datetime.timezone.utc)}.")
    await client.get_channel(CsBotInfo.getWelcomeID()).send(welcomeMessage.format(member.name))

#Help message will be updated along with additional functionalities.
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == ("!help"):
        await client.get_user(message.author.id).send("I don't do much yet. If you have any suggestions, bugs, or just need someone to talk to, send a message to UnicornBlood#9295.")

client.run(CsBotInfo.getToken())
