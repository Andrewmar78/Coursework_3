# Уже не актуален, т.к. запуск run.py и server.py

from flask import Flask, render_template
from flask_restx import Api
from config import Config
from project.setup_db import db
from project.views.directors import directors_ns
from project.views.genres import genres_ns
from flask_cors import CORS
from project.views.movies import movies_ns
# import logging
# logging.basicConfig(filename="basic.log", level=logging.INFO)


def create_app(config):
    """Функция создания основного объекта app, подключения расширений"""
    app = Flask(__name__)
    app.config.from_object(config)
    app.app_context().push()

    @app.route("/")
    def index():
        return render_template("index.html")

    api = Api(
        authorization={
            "Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}
        },
        title="Coursework 4",
        doc="/docs",
    )

    cors = CORS()
    cors.init_app(app)

    api.init_app(app)
    api.add_namespace(genres_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(movies_ns)

    db.init_app(app)
    db.create_all()

    return app


if __name__ == '__main__':
    application = create_app(Config)
    application.run(port=25000)
