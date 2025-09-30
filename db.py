import discord
import os
from dotenv import load_dotenv

load_dotenv()
token=os.getenv('bot_token')
intents=discord.intents.default()
intents.message_content=True
intents.members=True

Responses={'goal_set:','progress_good:','progress_bad:','completed;'}

def init_db():
    conn=sqlite3.connect('goals.db')
    c=conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users(id INTEGER, username TEXT, goals_completed INTEGER DEFAULT 0)''')
    c.execute('''CREATE TABLE IF NOT EXISTS goals(id INTEGER PRIMARY KEY, user_id INTEGER,title TEXT,progress INTEGER DEFAULT 0, completed BOOLEAN DEFAULT 0,CREATED_DATE TEXT)''')
    conn.commit()
    conn.close()
    