# -*- coding: utf-8 -*-

from app import app, website_constants, api
from flask import render_template, request
from app import DataBase as db


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        player_name, room_id = request.form.get('player_name'), request.form.get('room_id')
        # continue...
    return render_template('index.html', context=website_constants)


@app.route('/jsapi/<query>')
def api_request(query):
    params = request.args.get('jsdata')
    db.Game(api.get_current_room_id(query, request, params)).set_all_users({'updated': False})
    db.User(api.get_current_name(query, request, params), api.get_current_room_id(query, request, params))\
        .update({'updated': True})
    return api.get_data(query=query, request=request, params=params)


@app.route('/create', methods=['GET', 'POST'])
def create_room():
    return render_template('create.html')


@app.route('/game/<game_hash>', methods=['GET', 'POST'])
def game_room(game_hash):
    pass

