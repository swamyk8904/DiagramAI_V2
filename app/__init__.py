import os
from flask import Flask
from config import Config


def create_app():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    app = Flask(
        __name__,
        template_folder=os.path.join(project_root, "templates"),
        static_folder=os.path.join(project_root, "static"),
    )

    app.config.from_object(Config)

    from app.routes import main
    app.register_blueprint(main)

    return app