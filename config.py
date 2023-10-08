from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID",'28731705'))
API_HASH = getenv("API_HASH",'7ed8bb45ea845bef652aa0606584f413')

BOT_TOKEN = getenv("BOT_TOKEN",'6338221023:AAF7XDPQv6p6ebWdunT1tcCLDdsY1mBy_KA')
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID",'6647321265'))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/fuck_uff_XD")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/fuck_uff_XD")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6647321265").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
