# π Β© @tofik_dn
# β οΈ Do not remove credits

import requests

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import geez_cmd


@geez_cmd(pattern="asupan$")
async def _(event):
    try:
        response = requests.get("https://api-tede.herokuapp.com/api/asupan/ptl").json()
        await event.client.send_file(event.chat_id, response["url"])
        await event.delete()
    except Exception:
        await event.edit("**Tidak bisa menemukan video asupan.**")


@geez_cmd(pattern="wibu$")
async def _(event):
    try:
        response = requests.get("https://api-tede.herokuapp.com/api/asupan/wibu").json()
        await event.client.send_file(event.chat_id, response["url"])
        await event.delete()
    except Exception:
        await event.edit("**Tidak bisa menemukan video wibu.**")


@geez_cmd(pattern="chika$")
async def _(event):
    try:
        response = requests.get("https://api-tede.herokuapp.com/api/chika").json()
        await event.client.send_file(event.chat_id, response["url"])
        await event.delete()
    except Exception:
        await event.edit("**Tidak bisa menemukan video chikakiku.**")


CMD_HELP.update(
    {
        "asupan": f"**Plugin : **`asupan`\
        \n\n  πΎπ€π’π’ππ£π :** `{cmd}asupan`\
        \n  β³ : **Untuk Mengirim video asupan secara random.\
        \n\n  πΎπ€π’π’ππ£π :** `{cmd}wibu`\
        \n  β³ : **Untuk Mengirim video wibu secara random.\
        \n\n  πΎπ€π’π’ππ£π :** `{cmd}chika`\
        \n  β³ : **Untuk Mengirim video chikakiku secara random.\
    "
    }
)
