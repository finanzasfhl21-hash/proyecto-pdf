from io import BytesIO

from flask import Blueprint, render_template, send_file

from proyecto.models.pdf_model import PdfModel

pdf_bp = Blueprint("pdf", __name__)


@pdf_bp.route("/")
def index():
    modelo = PdfModel()
    texto = modelo.extraer_texto()
    return render_template("index.html", texto=texto, nombre=modelo.nombre_archivo())


@pdf_bp.route("/exportar")
def exportar():
    modelo = PdfModel()
    texto = modelo.extraer_texto()
    buffer = BytesIO(texto.encode("utf-8"))
    return send_file(
        buffer,
        mimetype="text/plain",
        as_attachment=True,
        download_name=f"{modelo.nombre_archivo()}.txt",
    )
