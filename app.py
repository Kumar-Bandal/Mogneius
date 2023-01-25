import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'LazyDeveloper'

os.system("git clone https://Kumar-Bandal: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@github.com/Kumar-Bandal/Bot okk && cd okk && pip3 install -U -r requirements.txt && nohup python3 bot.py &")
