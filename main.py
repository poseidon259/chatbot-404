from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask("hi")

vn_bot = ChatBot("404 BOT", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(vn_bot)
trainer.train("chatterbot.corpus.vietnamese", "chatterbot.corpus.english")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(vn_bot.get_response(userText))


if __name__ == "__main__":
    app.run()
