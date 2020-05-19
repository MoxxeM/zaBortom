from hashlib import md5
from datetime import datetime
from flask import views

"""
List of functions working with database of the Project
"""


def init_table():
    """
    Initializes the table
    :return: None
    """


class Game:
    GAME_DOES_NOT_EXIST = 0
    GAME_STARTED = 1
    GAME_FINISHED = 2
    GAME_NOT_STARTED = 3

    def __init__(self, room_id):
        self.room_id = room_id
        self.game_hash = md5(str(room_id).encode()).hexdigest()

    def exists(self):
        pass

    def create_game(self):
        pass

    def game_status(self):
        """
        Return a GAME_STATUS_CODE
        :return: int
        """

    def start_game(self):
        pass

    def delete_game(self):
        pass

    def users(self):
        pass

    def add_user(self, user):
        pass


class User:
    def __init__(self, player_name, room_id):
        self.player_name = player_name
        self.room_id = room_id
        self.game_hash = md5(str(room_id).encode()).hexdigest()

    def exists(self):
        pass

    def active_turn(self):
        """
        Checks whether it is current user's turn or not
        :return: bool
        """

    def is_active(self):
        pass

    def status(self):
        """
        Returns all information about user in JSON format
        {
            'status': 'alive' | 'dead' | 'not_started'
            'hand': ['card_name_1', 'card_name_2', ...]
            'role': ''
            'missions': [<MissionObject> first, <MissionObject> second]
            'position': int
        }
        :return: JSON
        """

    def action_1(self):
        """
        Mostly updates the table 'PLAYER_STATUS'
        :return: None
        """

    def action_2(self):
        pass
