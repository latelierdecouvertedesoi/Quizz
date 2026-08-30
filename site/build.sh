#!/usr/bin/env bash
# Reconstruit les fichiers du site.
#   1. injecte l'en-tête et le pied d'APERÇU dans chaque page (pages/_nav.html, pages/_pied.html)
#   2. extrait, pour chaque page, le seul contenu à coller dans WordPress -> a-coller/
# Usage :  bash build.sh
set -euo pipefail
cd "$(dirname "$0")"
python3 - <<'PY'
import re, pathlib

racine = pathlib.Path(__file__).parent if "__file__" in dir() else pathlib.Path(".")
pages = pathlib.Path("pages")
sortie = pathlib.Path("a-coller"); sortie.mkdir(exist_ok=True)

nav  = pages.joinpath("_nav.html").read_text(encoding="utf-8").strip()
pied = pages.joinpath("_pied.html").read_text(encoding="utf-8").strip()

def poser(html, balise, contenu):
    """Insère le fragment, que ce soit la 1re fois (placeholder) ou une mise à jour (entre repères)."""
    ouvert, ferme = f"<!--{balise}:DEBUT-->", f"<!--{balise}:FIN-->"
    bloc = f"{ouvert}\n{contenu}\n{ferme}"
    if ouvert in html:
        return re.sub(re.escape(ouvert) + r".*?" + re.escape(ferme), lambda m: bloc, html, flags=re.S)
    return html.replace(f"<!--{balise}-->", bloc)

DEBUT = re.compile(r"<!--\s*=+\s*DÉBUT DU CONTENU À COLLER[^>]*-->")
FIN   = re.compile(r"<!--\s*=+\s*FIN DU CONTENU À COLLER[^>]*-->")

total = 0
for f in sorted(pages.glob("[0-9]*.html")):
    html = f.read_text(encoding="utf-8")
    html = poser(html, "NAV", nav)
    html = poser(html, "PIED", pied)
    f.write_text(html, encoding="utf-8")

    # Extraction de tous les blocs à coller de la page (la page Contact en compte deux)
    debuts = [m.end()   for m in DEBUT.finditer(html)]
    fins   = [m.start() for m in FIN.finditer(html)]
    if len(debuts) != len(fins):
        raise SystemExit(f"{f.name} : repères DÉBUT/FIN déséquilibrés ({len(debuts)}/{len(fins)})")
    if not debuts:
        raise SystemExit(f"{f.name} : aucun repère DÉBUT/FIN trouvé")

    morceaux = [html[d:fin].strip() for d, fin in zip(debuts, fins)]
    if len(morceaux) == 1:
        corps = morceaux[0]
    else:
        corps = "\n\n".join(
            f"<!-- ======== BLOC HTML n°{i} — à coller dans un bloc « HTML personnalisé » distinct ======== -->\n{m}"
            for i, m in enumerate(morceaux, 1))
    sortie.joinpath(f.name).write_text(corps + "\n", encoding="utf-8")
    total += 1
    print(f"  ✓ {f.name}  ({len(morceaux)} bloc(s), {len(corps)} caractères)")

print(f"\n{total} page(s) prêtes dans a-coller/")
PY
