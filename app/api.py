# -*- coding: utf-8 -*-
from flask import render_template
from app import DataBase

available_params = ['player_name', 'room_id', 'missions', 'hand']
# 'missions' and 'hand' need validation through hash_code using 'secret_key'
# additional check on 'player_check'


def is_updated(query, request, params):
    """
    Checks whether any other player had a js request since last update
    :return: bool
    """


def error_message(msg=''):
    return """
    <center style="padding:5px;background:white;font-size:20px;border-radius:4px;">
    {}
    </center>
    """.format(msg or 'Ошибка! Вернуться <a href="/">на главную</a>')


def get_current_name(query, request, params):
    pass


def get_create_room(query, request, params):
    pass

# more functions


queries = {
    'current-name': get_current_name,
    'create-room': get_create_room,
    'is-updated': is_updated,
}


def query_is_valid(query):
    return queries.get(query) is not None


def get_data(query, request, params=None):
    if query_is_valid(query):
        return queries.get(query)(query, request, params) or error_message()
    return error_message()
