
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from speechtotext import speech_to_text
from google_search import open_google_and_search


app = Flask("hi")

vn_bot = ChatBot("bot_404", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(vn_bot)
trainer.train(r".\\databases\\vietnamese")


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

@app.route("/searching")
def get_bot_response3():
    userText = str(request.args.get('msg'))
    return open_google_and_search(userText)


if __name__ == "__main__":
    app.run()
