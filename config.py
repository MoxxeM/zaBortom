import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '1730f0246b9301b86518775d180705c5'
