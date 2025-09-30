from discord.ext import commands
bot= commands.Bot(command_prefix='/', intents=intents)
async def on_ready():
    print(f"{bot.user} is ready to judge your progress!")

@bot.command()
async def set_goal (user_id,goal):
    conn=sqlite3.connect('goals.db')
    c=conn.cursor()
    c.execute ("SELECT progress FROM goals WHERE user_id=?", (user_id))
    row=c.fetchone()
    if row:
        new_progress=row[0]+amount
        c.execute('UPDATE goals SET progress=? WHERE user_id=?',(new_progress,user_id))
        conn.commit()
        conn.close()
        return new_progress
    else:
        conn.close()
        return None
    