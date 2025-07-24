import os

class Config:
    API_ID = int(os.getenv("API_ID", 7813390))
    API_HASH = os.getenv("API_HASH", '1faadd9cc60374bca1e88c2f44e3ee2f')
    BOT_TOKEN = os.getenv("BOT_TOKEN", '8132280304:AAEAotAxpqUbh1Lqd0HaLx43TR__g3T2Vr4')
