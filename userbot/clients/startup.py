import sys
import requests

import telethon.utils

from userbot import BOT_VER as version
from userbot import (
    DEVS,
    LOGS,
    GEEZ2,
    GEEZ3,
    GEEZ4,
    GEEZ5,
    STRING_2,
    STRING_3,
    STRING_4,
    STRING_5,
    STRING_SESSION,
    blacklistgeez,
    bot,
    call_py,
)
from userbot.modules.gcast import GCAST_BLACKLIST as GBL


MSG_BLACKLIST = "MAKANYA GA USAH BERTINGKAH GOBLOK, USERBOT {} GUA MATIIN NAJIS BANGET DIPAKE JAMET KEK LU.\nGeezProjects v{}, Copyright © 2021-2022 VCKY! <https://github.com/vckyou>"


async def geez_client(client):
    client.me = await client.get_me()
    client.uid = telethon.utils.get_peer_id(client.me)


def multigeez():
    blacklistgeez = requests.get(
        "https://raw.githubusercontent.com/vckyou/Reforestation/master/blacklistgeez.json"
    ).json()
    if user.id in blacklistgeez:
        LOGS.warning(
            "NAMPAKNYA USERBOT TIDAK DAPAT BEKERJA, MUNGKIN ANDA TELAH DI BLACKLIST OLEH PEMILIK USERBOT.\nCredits: @VckyouuBitch"        )
        sys.exit(1)
    if -1001459812644 not in GBL:
        LOGS.warning(version)
        sys.exit(1)
    if 5155140917 not in DEVS:
        LOGS.warning(
            f"EOL\nGeezProjects v{BOT_VER}, Copyright © 2021-2022 VICKY <https://github.com/vckyou>"
        )
        sys.exit(1)
    failed = 0
    if STRING_SESSION:
        try:
            bot.start()
            call_py.start()
            bot.loop.run_until_complete(geez_client(bot))
            user = bot.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_SESSION detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——"
            )
            if user.id in blacklistgeez:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(f"{e}")

    if STRING_2:
        try:
            GEEZ2.start()
            GEEZ2.loop.run_until_complete(geez_client(GEEZ2))
            user = GEEZ2.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_2 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistgeez:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(f"{e}")

    if STRING_3:
        try:
            GEEZ3.start()
            GEEZ3.loop.run_until_complete(geez_client(GEEZ3))
            user = GEEZ3.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_3 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistgeez:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(f"{e}")

    if STRING_4:
        try:
            GEEZ4.start()
            GEEZ4.loop.run_until_complete(geez_client(GEEZ4))
            user = GEEZ4.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_4 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistgeez:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(f"{e}")

    if STRING_5:
        try:
            GEEZ5.start()
            GEEZ5.loop.run_until_complete(geez_client(GEEZ5))
            user = GEEZ5.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_5 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistgeez:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(f"{e}")

    if not STRING_SESSION:
        failed += 1
    if not STRING_2:
        failed += 1
    if not STRING_3:
        failed += 1
    if not STRING_4:
        failed += 1
    if not STRING_5:
        failed += 1
    return failed
