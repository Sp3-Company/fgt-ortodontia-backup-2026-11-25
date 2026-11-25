"""Extrai uma página arquivada para abrir localmente no Chrome ou Edge."""

import argparse
import gzip
import json
import shutil
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PAGES = json.loads((REPO / "inventario/rotas.json").read_text())["pages"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pagina", choices=sorted(PAGES.values()), nargs="?", default="inicio")
    parser.add_argument("--destino", type=Path, default=Path.cwd())
    args = parser.parse_args()
    args.destino.mkdir(parents=True, exist_ok=True)
    source = REPO / "paginas" / (args.pagina + ".mhtml.gz")
    destination = args.destino / (args.pagina + ".mhtml")
    with gzip.open(source, "rb") as archive, destination.open("xb") as document:
        shutil.copyfileobj(archive, document)
    print(destination.resolve())


if __name__ == "__main__":
    main()
