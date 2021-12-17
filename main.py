# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from speechtotext import speech_to_text

app = Flask("hi")

vn_bot = ChatBot("404 BOT", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(vn_bot)
trainer.train(r".\databases\vietnamese")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(vn_bot.get_response(userText))

@app.route("/answer")
def get_bot_response2():
    userSpeech = speech_to_text()
    botAnswer = str(vn_bot.get_response(userSpeech))
    return {"user": userSpeech,
            "bot": botAnswer}



if __name__ == "__main__":
    app.run()
