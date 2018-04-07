pip install vaderSentiment
pip install tweepy
pip install pandas
pip install numpy
pip install dash==0.21.0  # The core dash backend
pip install dash-renderer==0.11.3  # The dash front-end
pip install dash-html-components==0.9.0  # HTML components
pip install dash-core-components==0.21.1  # Supercharged components
pip install plotly --upgrade  # Plotly graphing library used in examples
pip install unidecode


tbl.py to show graphical representation of sentiments on graph(sentiment values are stored in twitter.db sqlite3 database)
live_twitter.py to show on web interface

FOLLOW THESE STEPS TO RUN THE CODE:

1)INSTALL ALL THE DEPENDENCIES
2)OPEN 2 DIFFERENT TERMINAL (COMMAND PROMPT FOR WINDOWS USER)
3)ON TERMINAL 1: >>python creating_db_twitter.py
4)0N TERMINAL 2: >>python tbl.py            (for graph)
     OR
5)ON TERMINAL 2: >>python live_twitter.py     (for graph on web open http://127.0.0.1:8050/) 