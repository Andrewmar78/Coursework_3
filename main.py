from flask import Flask, render_template
from flask_restx import Api
from config import Config
from project.setup_db import db
from project.views.directors import directors_ns
from project.views.genres import genres_ns
from flask_cors import CORS

# import logging
# logging.basicConfig(filename="basic.log", level=logging.INFO)


def create_app(config):
    """Функция создания основного объекта app"""
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
    # api.add_namespace(directors_ns)
    # api.add_namespace(movies_ns)


    db.init_app(app)
    db.create_all()

    return app


# def configure_app(application: Flask):
#     """Функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)"""
#     db.init_app(application)
#     api = Api(app)
#     # api.add_namespace(movie_ns)
#     api.add_namespace(director_ns)
#     api.add_namespace(genre_ns)
#     # api.add_namespace(auth_ns)
#     # api.add_namespace(user_ns)
#     # create_data(app, db)


# def create_data(app, db):
    # """Создание пользователей в БД"""
    # with app.app_context():
    #     db.create_all()
    #
    #     u1 = User(username="Vasya", password="my_little_pony", role="user")
    #     u2 = User(username="Oleg", password="qwerty", role="user")
    #     u3 = User(username="Oleg", password="P@ssw0rd", role="admin")
        ## user_schema = UserSchema(many=True)
        ## res = user_schema.dump([u1, u2, u3])

        # with db.session.begin():
            ## db.session.add_all(res)
            # db.session.add_all([u1, u2, u3])


if __name__ == '__main__':
    application = create_app(Config)
    # configure_app(app)
    # create_data()
    application.run(port=25000)
