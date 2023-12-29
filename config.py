from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = "your bot token"
ADMINS = env.list("ADMINS")
