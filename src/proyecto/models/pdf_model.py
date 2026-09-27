from pathlib import Path

from pypdf import PdfReader

PDF_PATH = Path(
    r"C:\Users\pedro\OneDrive\Desktop\Proyecto PDF\PDF\El Aprendiz de Trading (alta calidad).pdf"
)


class PdfModel:
    def __init__(self, ruta: Path = PDF_PATH) -> None:
        self.ruta = ruta

    def extraer_texto(self) -> str:
        reader = PdfReader(self.ruta)
        return "\n".join(pagina.extract_text() or "" for pagina in reader.pages)

    def nombre_archivo(self) -> str:
        return self.ruta.stem
