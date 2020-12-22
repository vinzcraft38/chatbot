#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask
import flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hallo Welt!"
