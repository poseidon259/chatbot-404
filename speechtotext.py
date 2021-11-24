# -*- coding: utf-8 -*-

import speech_recognition as sp
from gtts import gTTS
import os


def speech_to_text():
    bot_ear = sp.Recognizer()
    with sp.Microphone() as mic:
        #audio = bot_ear.listen(mic)
        audio = bot_ear.record(mic, duration= 3) #Siri nghe trong vòng 3 giây sau đó tắt Mic, tránh treo máy do bật Mic lien tục
    try:
        you = bot_ear.recognize_google(audio,language='vi-VN')# nó sẽ lấy giọng của chị Google
    except:
        you ="Tôi không hiểu bạn nói gì."

    return you



