from flask import Flask, render_template
from chatterbot import ChatBot
from flask import request
from flask_cors import CORS
from chatterbot.trainers import ChatterBotCorpusTrainer


import json
#import MySQLdb
import re

data2={"conversation":[]}
#data2["conversation"]=[];
new_arr=[]
 


app = Flask(__name__)
CORS(app)
english_bot = ChatBot("English Bot")
english_bot.set_trainer(ChatterBotCorpusTrainer)
english_bot.train("chatterbot.corpus.oam")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sign_users",methods = ['POST', 'GET'])
def get_raw_response():
    query=request.args.get('name')
    return str(english_bot.get_response(query)).encode('utf-8')


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5004)
