import os
import logging
from flask import Flask

def create_app() -> Flask:
    app = Flask(__name__)

    app.config["APP_NAME"] = os.getenv("APP_NAME", "expense-tracker")
    app.config["APP_ENV"] = os.getenv("APP_ENV", "dev")

    logging.basicConfig(
        level=os.getenv("LOG_LEVEL", "INFO"),
        format="%(asctime)s %(levelname)s %(name)s - %(message)s",
    )

    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app
