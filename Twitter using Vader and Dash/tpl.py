import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import style
import sqlite3
import pandas as pd
import numpy as np
import os

style.use('fivethirtyeight')

sentiment_term = ""


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
conn = sqlite3.connect('twitter.db')
c = conn.cursor()
df = pd.read_sql("SELECT * FROM sentiment WHERE tweet LIKE ? ORDER BY unix DESC LIMIT 1000", conn,params=('%' + sentiment_term + '%',))
df.sort_values('unix', inplace=True)
df['sentiment_smoothed'] = df['sentiment'].rolling(int(len(df)/5)).mean()
df.dropna(inplace=True)


def animate(i):
    conn = sqlite3.connect('twitter.db')
    c = conn.cursor()
    df = pd.read_sql("SELECT * FROM sentiment WHERE tweet LIKE ? ORDER BY unix DESC LIMIT 1000", conn,params=('%' + sentiment_term + '%',))
    df.sort_values('unix', inplace=True)
    df['sentiment_smoothed'] = df['sentiment'].rolling(int(len(df)/5)).mean()
    df.dropna(inplace=True)
    count = df.unix.values[:]
    x = df.unix.values[len(count)-15:]
    y = df.sentiment_smoothed.values[len(count)-15:]
    ax1.clear()
    ax1.plot(x,y,marker='o',linestyle='-',linewidth=1)
  
	
anim = animation.FuncAnimation(fig, animate	, interval=10)
plt.show()