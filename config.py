import os



class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1936696733:AAHymeJ7F7Z-ktd0Sv0PQRJdp4SMCpXTuQc")
      API_ID = int(os.environ.get("APP_ID", 8901416))
      API_HASH = os.environ.get("API_HASH" ff05861c1bf07edcb2644f7f308584df)
      CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "nil")
      ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "@IamtheLuciferMorningstar")
      ADMIN_ID = int(os.environ.get("ADMIN_ID", 1998893767 )) 
      DB_URL = os.environ.get("DATABASE_URL", "")
