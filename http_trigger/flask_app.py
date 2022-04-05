from flask import Flask

from src import blueprint
from src.config import cors


def create_app():  # noqa: ANN201
    flask_app = Flask(__name__)
    flask_app.config["RESTX_MASK_SWAGGER"] = False

    cors.cors.init_app(flask_app)

    flask_app.register_blueprint(blueprint, url_prefix="/")

    return flask_app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
