import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "29532820"))
    API_HASH = os.environ.get("API_HASH", "f0d6c78e4c2d8ca5c4347555891d6cf1")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6515877465:AAGrqdENncLmH0kv3MLKmTBi8GVWus1Hrdw")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOMUBu7schCVDoqcBhtcHbM1kINcbeGQlQ8SqGImlrrebjdUfJQdrfP8lUGgt7PVky6EUwIYY5cjECWT-eaKbNyhcC5hF9aLIstK0TsG1Tb1MSovdHib_bJLUXXt5Hw4KwGKIoBn3ca3VoE3CzXbf0qQu9q_HneWVEAVyR7z7cy4m22qd4a8uZUaoVwrn7EqW77e5RyRKl7WWtfkW_k3yhmbURuIEVYTm6TW01DjDvMsO7zFLUzmlKITDJUwCK8Q-apr4bGx76NdQDzUoCOPc90M235oCrQGxZQMeJUCfnAb62DvbCB3rqJzuyvrJZDIxWTvjcOyuH7oTLnBTPswepnqGchk=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@T4U_musicbot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
