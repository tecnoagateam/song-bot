from pyrogram import filters

from song.mrdarkprince import get_text
from song import app, LOGGER


@app.on_message(filters.command("tagall") & ~filters.edited & ~filters.bot)
async def tagall(client, message):
    await message.reply("`Tag Basladi!...`")
    sh = get_text(message)
    if not sh:
        sh = "Salam!"
    mentions = ""
    async for member in client.iter_chat_members(message.chat.id):
        mentions += member.user.mention + " "
    n = 4096
    kk = [mentions[i : i + n] for i in range(0, len(mentions), n)]
    s+=1
    if s==5
    for i in kk:
        j = f"<b>{sh}</b> \n{i}"
        await client.send_message(message.chat.id, j, parse_mode="html")
        mentions=''
        s=0


    else:
        return
        member[message.chat.id] = False