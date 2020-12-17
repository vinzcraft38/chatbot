#!/usr/bin/env phyton3
# -*- coding: utf-8 -*-

# Ein einfacher Chatbot
# (c) 2020 by me, Lizence GLPv3

import random


# zufälligen Antworten
zufallantworten = ["Oh wirklich...", "Interessant", "Das kann man so sehen.", "Ich verstehe..."]
# Stopwörter
reaktionen = {"hallo": "Aber hallo",
              "geht": "was verestehst Du darunter?",
              "schmeckt": "Ich habe keine Geschmacksinn"}

# Ausgabe Head..
print("Willkommen beim chatbot (v1)")
print("Woruber wollensir sprechen?")
print("Zum Beenden geben Sie bye ein...")
print("")

# main
nutzereingabe = ""
while nutzereingabe != "bye":
    nutzereingabe = ""
    while nutzereingabe == "":
        nutzereingabe = input("Ihre Frage oder Antwort: ")
    nutzereingabe = nutzereingabe.lower()
    nutzerewoerter = nutzereingabe.split()

    intelligentantworten = False
    for einzelwoerter in nutzerewoerter:
        if einzelwoerter in reaktionen:
            print(reaktionen[einzelwoerter])
            intelligentantworten = True
    if not intelligentantworten:
        print(random.choice(zufallantworten))

print("Einen schönen Tag.")
