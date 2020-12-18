#!/usr/bin/env phyton3
# -*- coding: utf-8 -*-

# Ein einfacher Chatbot
# (c) 2020 by me, Lizence GLPv3

import random


class Chatbot:

    def __init__(self, reaktionen, zufallsantworten):
        self.__reaktionen = dict(reaktionen)
        self.__zufallsantworten = list(zufallsantworten)

    def __del__(self):
        pass

    def set_Message(self, message):
        self.__message = str(message)

    def get_response(self):
        self.__message = self.__message.lower()
        self.__words = self.__message.split()
        self.__intelligentanswers = False

        for word in self.__words:
            if word in self.__reaktionen:
                self.__intelligentanswers = True
                self.__response = self.__reaktionen[word]
        if not self.__intelligentanswers:
            self.__response = random.choice(self.__zufallsantworten)

        return self.__response


def main():

    # Listen
    zufallsantworten = ["Oh wirklich...", "Interessant", "Das kann man so sehen.", "Ich verstehe..."]
    reaktionen = {"hallo": "aber hallo",
                  "geht": "Was verstehst Du darunter",
                  "schmeckt": "Ich habe keinen Geschmackssinn"}

    # Ausgabe Head..
    print("Willkommen beim ChatBot (v2)")
    print("Worüber wollen Sie sprechen")
    print("Zum Beenden geben Sie bye ein...")
    print("")

    # Chatbot-Objekt
    bot = Chatbot(reaktionen, zufallsantworten)

    # Logik
    nutzereingabe = ""
    while nutzereingabe != "bye":
        nutzereingabe = ""
        while nutzereingabe == "":
            nutzereingabe = input("Ihre Frage oder Antwort: ")
        bot.set_Message(nutzereingabe)
        print(bot.get_response())

    # Ausgabe Verabschiedung
    print("Bis zum nächsten Mal.")


if __name__ == "__main__":
    main()
