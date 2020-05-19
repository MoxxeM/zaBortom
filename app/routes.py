# -*- coding: utf-8 -*-

from app import app, website_constants
from flask import render_template, request


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        args = request.args.get('jsData')
        print(args)
    if request.method == 'POST':
        player_name, room_id = request.form.get('player_name'), request.form.get('room_id')
        print(player_name, room_id)
    return render_template('index.html', context=website_constants)


@app.route('/create', methods=['GET', 'POST'])
def create_room():
    pass


@app.route('/game/<game_hash>', methods=['GET', 'POST'])
def game_room(game_hash):
    pass

