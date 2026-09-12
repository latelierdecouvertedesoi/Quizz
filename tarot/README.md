# Le Miroir des Arcanes

Outil de lecture du Tarot de Marseille dans la voie d'Alejandro Jodorowsky,
pour l'accompagnement et la formation. Page unique, autonome, sans dépendance :
`tarot/index.html` s'ouvre directement dans un navigateur.

## Ce que contient l'outil

| Onglet | Contenu |
|---|---|
| **Le tapis** | Six tirages, la lecture d'ensemble automatique, la méthode en 6 étapes, le calcul de l'arcane de naissance et de l'arcane de l'année |
| **Les 78 lames** | Les 22 majeurs (iconographie, encres, sens en élan, sens en tension, question à rendre, septénaire, colonne) et les 56 mineurs (série × nombre, figures) |
| **Grammaire** | Les encres, les dix nombres, les quatre séries et les quatre centres, les figures, les trois septénaires, les sept colonnes, la lecture des regards, le cadre déontologique et les sources |
| **Carnet** | Les tirages gardés, avec leur question, à relire plus tard |

## Les six tirages

1. **La lame-miroir** — une lame, en ouverture de séance ou le matin.
2. **Le tirage en croix** — quatre lames + un nœud **déduit** par addition des nombres (somme réduite à 22 ou moins), pas tiré.
3. **Les trois temps** — la racine, le présent, le devenir *si rien ne change*.
4. **Les quatre centres** — corps & matière, cœur & émotion, élan créateur, esprit & parole.
5. **Le pont** — pour une relation : ma place, ce qui circule, l'autre.
6. **Le septénaire** — sept lames sur les sept mouvements d'un cycle.

## Parti pris

Jodorowsky récuse la divination : le Tarot est « un miroir, pas une boule de
cristal ». L'outil ne prédit donc rien. Il déplie une situation, propose des
hypothèses et rend le tout au consultant **sous forme de questions ouvertes**.
Le cadre déontologique est intégré dans l'onglet *Grammaire*.

## Charte graphique

La page reprend `site/assets/style.css` : or `#B59659`, turquoise `#8ED8D8` /
`#4E9E9E`, pâle `#DBEEEE`, encre `#33383B`, crème `#FBFAF8` ; Fraunces en
graisse 300 pour les titres, Karla pour le corps ; boutons en or à rayon 9 px,
cartes à 12 px, le « fil » or-turquoise en signature, les pastilles d'étapes
reliées par le filet pointillé turquoise. Identité claire assumée : pas de
thème sombre, comme le site.

Seule exception : les **bandes d'encres** sur les lames gardent les pigments
réels du pochoir marseillais (rouge, bleu, jaune, vert, chair, noir). Ce sont
des données, pas de la décoration — l'outil s'en sert pour la première étape de
lecture. L'interface est à la charte ; le contenu reste fidèle au jeu.

## Mettre la page en ligne

- **Telle quelle** : déposer `index.html` sur un hébergement statique.
- **Sur WordPress** : créer une page, y insérer un bloc *HTML personnalisé*, et
  y coller le contenu du fichier. Les polices viennent de Google Fonts ; tout le
  reste est embarqué.
- Le carnet s'enregistre dans le navigateur (`localStorage`) hors de
  l'environnement Claude ; il n'y a aucun envoi de données.

## Sources

- A. Jodorowsky & M. Costa, *La Voie du Tarot*, Albin Michel, 2004.
- A. Jodorowsky, *L'Art du Tarot*, livret du Tarot de Marseille restauré (Camoin–Jodorowsky, 1997).
- M. Costa, *Le Tarot conjugal*.
- A. Jodorowsky, *Psychomagie*, *Métagénéalogie*.

Les textes de l'outil sont des synthèses rédigées dans l'esprit de cette
approche ; ils ne reproduisent pas les ouvrages, qui restent la référence.
