# L'Atelier Découverte de Soi — site web

Site de Véronique, accompagnement à la connaissance de soi et à la gestion des émotions
par le corps. Rennes · Retiers · Visio · Atelier nomade.

## Par où commencer

👉 **[site/GUIDE-WORDPRESS.md](site/GUIDE-WORDPRESS.md)** — le mode d'emploi complet,
pas à pas, pour mettre le site en ligne.

## Contenu du dépôt

| Dossier | Rôle |
|---|---|
| `site/pages/` | Les 10 pages, à ouvrir dans un navigateur pour **voir** le rendu |
| `site/import-wordpress.xml` | Les 10 pages en **un seul fichier à importer** dans WordPress |
| `site/a-coller/` | Le contenu à **copier** page par page, si l'import ne passe pas |
| `site/assets/style.css` | La charte graphique, à coller dans *CSS additionnel* |
| `site/quiz/` | Le quiz interactif « Est-ce que mon accompagnement est fait pour vous ? » |
| `site/maquette-originale.html` | La maquette de référence, conservée telle quelle |
| `site/build.sh` | Régénère `a-coller/` après modification d'une page |

Les deux fichiers à la racine (`index.html.html`, `quiz_accompagnement linkee.html`)
sont l'ancienne version du quiz, conservée pour mémoire.
