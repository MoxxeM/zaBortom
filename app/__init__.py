from flask import Flask
from datetime import datetime
from config import Config

app = Flask(__name__)
website_constants = {'project_name': '"За Бортом" Онлайн', 'url': '', 'year_of_creation': '2020', 'current_year':
                     str(datetime.now().year)}
app.config.from_object(Config)

from app import routes
