#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask, render_template, request, flash
from chatbot import Chatbot

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Pa$$w0rd'


@app.route('/', methods=('GET', 'POST'))


def index():

    chatbot_label = "Hallo. Worüber wollen Sie sprechen?"

    # Listen
    zufallsantworten = ["Oh wirklich...", "Interessant", "Das kann man so sehen.", "Ich verstehe..."]
    reaktionen = {"hallo": "aber hallo",
                "geht": "Was verstehst Du darunter",
                "schmeckt": "Ich habe keinen Geschmackssinn"}
    
    if request.method == 'POST':
        chatbot_input = request.form['chatbot_input']
        if not chatbot_input:
            flash('Ohne Frage kann ich nicht antworten!')
        else:
            bot = Chatbot(reaktionen, zufallsantworten)
            bot.set_Message(chatbot_input)
            chatbot_label = bot.get_response()

    return render_template('chatbot.html', chatbot_label=chatbot_label)
