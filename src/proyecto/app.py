import os
from pathlib import Path

from flask import Flask

from proyecto.controllers.pdf_controller import pdf_bp

VIEWS_DIR = Path(__file__).parent / "views" / "templates"


def create_app() -> Flask:
    app = Flask(__name__, template_folder=str(VIEWS_DIR))
    app.register_blueprint(pdf_bp)
    return app


def main() -> None:
    port = int(os.environ.get("PORT", 5000))
    create_app().run(host="0.0.0.0", port=port)
