#!/usr/bin/env python3
"""
Génère import-wordpress.xml : un fichier d'import WordPress (format WXR 1.2)
contenant les 10 pages du site, prêtes à être créées en une seule opération
via Outils > Importer > WordPress.

Les pages sont importées en BROUILLON : rien ne devient public tant que
Véronique ne l'a pas décidé, page par page.
"""
import re, pathlib, xml.etree.ElementTree as ET
from datetime import datetime, timezone

RACINE = pathlib.Path(__file__).parent
PAGES  = RACINE / "pages"
SITE   = "https://latelierdecouvertedesoi.com"
AUTEUR = "veronique"

# (fichier, titre de la page, permalien, ordre dans le menu)
PLAN = [
    ("01-accueil.html",                      "Accueil",                      "accueil",                      1),
    ("02-mon-approche.html",                 "Mon approche",                 "mon-approche",                 2),
    ("03-accompagnements.html",              "Accompagnements",              "accompagnements",              3),
    ("04-atelier-nomade.html",               "L’Atelier nomade",             "atelier-nomade",               4),
    ("05-a-propos.html",                     "À propos",                     "a-propos",                     5),
    ("06-contact.html",                      "Contact",                      "contact",                      6),
    ("07-faq.html",                          "Questions fréquentes",         "faq",                          7),
    ("08-mentions-legales.html",             "Mentions légales",             "mentions-legales",             8),
    ("09-politique-de-confidentialite.html", "Politique de confidentialité", "politique-de-confidentialite", 9),
    ("10-quiz.html",                         "Le quiz",                      "quiz",                        10),
]

DEBUT = re.compile(r"<!--\s*=+\s*DÉBUT DU CONTENU À COLLER[^>]*-->")
FIN   = re.compile(r"<!--\s*=+\s*FIN DU CONTENU À COLLER[^>]*-->")

# Formulaire natif de WordPress.com (Jetpack), inséré entre les deux blocs
# de la page Contact. Si votre thème ne le reconnaissait pas, supprimez ce
# bloc dans l'éditeur et insérez le bloc « Formulaire » à la main.
FORMULAIRE = """<!-- wp:jetpack/contact-form {"subject":"Nouvelle demande depuis le site","to":"latelier.decouvertedesoi@gmail.com","style":{"color":{"background":"#DBEEEE"},"spacing":{"padding":{"top":"32px","bottom":"32px","left":"24px","right":"24px"}}}} -->
<div class="wp-block-jetpack-contact-form" style="background-color:#DBEEEE;padding-top:32px;padding-right:24px;padding-bottom:32px;padding-left:24px"><!-- wp:jetpack/field-name {"required":true,"label":"Prénom et nom"} /-->

<!-- wp:jetpack/field-email {"required":true,"label":"E-mail"} /-->

<!-- wp:jetpack/field-telephone {"label":"Téléphone (facultatif)"} /-->

<!-- wp:jetpack/field-textarea {"required":true,"label":"Votre message"} /-->

<!-- wp:jetpack/field-checkbox {"required":true,"label":"J’accepte que mes données soient utilisées pour répondre à ma demande."} /-->

<!-- wp:jetpack/button {"element":"button","text":"Envoyer mon message","borderRadius":9} /--></div>
<!-- /wp:jetpack/contact-form -->"""


def blocs_de(fichier: str) -> list[str]:
    """Renvoie les morceaux de HTML à coller de la page, dans l'ordre."""
    src = (PAGES / fichier).read_text(encoding="utf-8")
    debuts = [m.end() for m in DEBUT.finditer(src)]
    fins = [m.start() for m in FIN.finditer(src)]
    if not debuts or len(debuts) != len(fins):
        raise SystemExit(f"{fichier} : repères DÉBUT/FIN absents ou déséquilibrés")
    morceaux = []
    for d, f in zip(debuts, fins):
        bloc = src[d:f]
        # on retire les commentaires de travail, sauf les repères PHOTO
        bloc = re.sub(r"<!--(?!\s*PHOTO).*?-->", "", bloc, flags=re.S)
        morceaux.append(bloc.strip())
    return morceaux


def contenu_gutenberg(fichier: str) -> str:
    """Emballe les morceaux en blocs Gutenberg « HTML personnalisé »."""
    morceaux = [f"<!-- wp:html -->\n{m}\n<!-- /wp:html -->" for m in blocs_de(fichier)]
    if fichier.startswith("06-"):          # le formulaire natif s'intercale
        morceaux.insert(1, FORMULAIRE)
    return "\n\n".join(morceaux)


def construire() -> str:
    maintenant = datetime.now(timezone.utc)
    date_locale = maintenant.strftime("%Y-%m-%d %H:%M:%S")
    date_gmt = maintenant.strftime("%Y-%m-%d %H:%M:%S")
    rfc = maintenant.strftime("%a, %d %b %Y %H:%M:%S +0000")

    NS = {
        "excerpt": "http://wordpress.org/export/1.2/excerpt/",
        "content": "http://purl.org/rss/1.0/modules/content/",
        "wfw":     "http://wellformedweb.org/CommentAPI/",
        "dc":      "http://purl.org/dc/elements/1.1/",
        "wp":      "http://wordpress.org/export/1.2/",
    }
    for prefixe, uri in NS.items():
        ET.register_namespace(prefixe, uri)

    # les déclarations xmlns sont posées par ElementTree via register_namespace
    rss = ET.Element("rss", {"version": "2.0"})
    canal = ET.SubElement(rss, "channel")

    def champ(parent, nom, texte, cdata=False):
        e = ET.SubElement(parent, nom)
        e.text = texte
        if cdata:
            e.set("__cdata__", "1")
        return e

    champ(canal, "title", "L'Atelier Découverte de Soi")
    champ(canal, "link", SITE)
    champ(canal, "description", "Connaissance de soi & gestion des émotions par le corps")
    champ(canal, "pubDate", rfc)
    champ(canal, "language", "fr-FR")
    champ(canal, "{http://wordpress.org/export/1.2/}wxr_version", "1.2")
    champ(canal, "{http://wordpress.org/export/1.2/}base_site_url", SITE)
    champ(canal, "{http://wordpress.org/export/1.2/}base_blog_url", SITE)

    auteur = ET.SubElement(canal, "{http://wordpress.org/export/1.2/}author")
    champ(auteur, "{http://wordpress.org/export/1.2/}author_id", "1")
    champ(auteur, "{http://wordpress.org/export/1.2/}author_login", AUTEUR, cdata=True)
    champ(auteur, "{http://wordpress.org/export/1.2/}author_email",
          "latelier.decouvertedesoi@gmail.com", cdata=True)
    champ(auteur, "{http://wordpress.org/export/1.2/}author_display_name", "Véronique", cdata=True)
    champ(auteur, "{http://wordpress.org/export/1.2/}author_first_name", "Véronique", cdata=True)
    champ(auteur, "{http://wordpress.org/export/1.2/}author_last_name", "", cdata=True)

    for indice, (fichier, titre, permalien, ordre) in enumerate(PLAN, start=1):
        ident = 100 + indice
        item = ET.SubElement(canal, "item")
        champ(item, "title", titre)
        champ(item, "link", f"{SITE}/{permalien}/")
        champ(item, "pubDate", rfc)
        champ(item, "{http://purl.org/dc/elements/1.1/}creator", AUTEUR, cdata=True)
        g = champ(item, "guid", f"{SITE}/?page_id={ident}")
        g.set("isPermaLink", "false")
        champ(item, "description", "")
        champ(item, "{http://purl.org/rss/1.0/modules/content/}encoded",
              contenu_gutenberg(fichier), cdata=True)
        champ(item, "{http://wordpress.org/export/1.2/excerpt/}encoded", "", cdata=True)
        champ(item, "{http://wordpress.org/export/1.2/}post_id", str(ident))
        champ(item, "{http://wordpress.org/export/1.2/}post_date", date_locale, cdata=True)
        champ(item, "{http://wordpress.org/export/1.2/}post_date_gmt", date_gmt, cdata=True)
        champ(item, "{http://wordpress.org/export/1.2/}comment_status", "closed", cdata=True)
        champ(item, "{http://wordpress.org/export/1.2/}ping_status", "closed", cdata=True)
        champ(item, "{http://wordpress.org/export/1.2/}post_name", permalien, cdata=True)
        champ(item, "{http://wordpress.org/export/1.2/}status", "draft", cdata=True)
        champ(item, "{http://wordpress.org/export/1.2/}post_parent", "0")
        champ(item, "{http://wordpress.org/export/1.2/}menu_order", str(ordre))
        champ(item, "{http://wordpress.org/export/1.2/}post_type", "page", cdata=True)
        champ(item, "{http://wordpress.org/export/1.2/}post_password", "", cdata=True)
        champ(item, "{http://wordpress.org/export/1.2/}is_sticky", "0")

    ET.indent(rss, space="  ")
    brut = ET.tostring(rss, encoding="unicode")

    # ElementTree ne sait pas écrire de CDATA : on rétablit les sections
    # marquées, en désérialisant les entités que la sérialisation a posées.
    def retablir_cdata(m):
        interieur = m.group(2)
        for entite, caractere in (("&lt;", "<"), ("&gt;", ">"), ("&amp;", "&"),
                                  ("&quot;", '"'), ("&apos;", "'")):
            interieur = interieur.replace(entite, caractere)
        return f"<{m.group(1)}><![CDATA[{interieur}]]></{m.group(1)}>"

    brut = re.sub(r'<([\w:]+) __cdata__="1"\s*/>', r"<\1></\1>", brut)
    brut = re.sub(r'<([\w:]+) __cdata__="1">(.*?)</\1>', retablir_cdata, brut, flags=re.S)
    return '<?xml version="1.0" encoding="UTF-8" ?>\n' + brut + "\n"


if __name__ == "__main__":
    xml = construire()
    cible = RACINE / "import-wordpress.xml"
    cible.write_text(xml, encoding="utf-8")
    # contrôle : le fichier doit être un XML valide et contenir les 10 pages
    arbre = ET.fromstring(xml)
    items = arbre.findall(".//item")
    print(f"✓ {cible.name} — {len(items)} pages, {len(xml)} caractères")
    for it in items:
        nom = it.find("{http://wordpress.org/export/1.2/}post_name").text
        titre = it.find("title").text
        taille = len(it.find("{http://purl.org/rss/1.0/modules/content/}encoded").text or "")
        print(f"    /{nom:<30} {titre:<30} {taille:>6} caractères")
