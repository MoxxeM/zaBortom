# -*- coding: utf-8 -*-

from app import app, website_constants, api
from flask import render_template, request


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        player_name, room_id = request.form.get('player_name'), request.form.get('room_id')
        # continue...
    return render_template('index.html', context=website_constants)


@app.route('/jsapi/<query>')
def api_request(query):
    params = request.args.get('jsdata')
    return api.get_data(query=query, request=request, params=params)


@app.route('/create', methods=['GET', 'POST'])
def create_room():
    pass


@app.route('/game/<game_hash>', methods=['GET', 'POST'])
def game_room(game_hash):
    pass

