# Mettre le site en ligne sur WordPress — guide pas à pas

Ce dossier contient **votre maquette transformée en site réel**, découpée page par page,
prête à être collée dans WordPress. Aucune ligne de code à écrire : uniquement des
copier-coller, dans l'ordre indiqué.

Comptez **1 h 30 à 2 h** pour tout mettre en place la première fois.

---

## Ce qui est livré

```
site/
├── assets/style.css .................. la charte graphique (à coller UNE fois)
├── pages/ ............................ les pages à ouvrir dans votre navigateur
│   ├── 01-accueil.html                 pour VOIR le rendu avant de publier
│   ├── 02-mon-approche.html
│   ├── 03-accompagnements.html
│   ├── 04-atelier-nomade.html
│   ├── 05-a-propos.html
│   ├── 06-contact.html
│   ├── 07-faq.html
│   ├── 08-mentions-legales.html
│   ├── 09-politique-de-confidentialite.html
│   └── 10-quiz.html                    (page optionnelle)
├── a-coller/ ......................... LE contenu à copier dans WordPress
│   └── (mêmes noms de fichiers)        un fichier = une page, rien à trier
├── import-wordpress.xml .............. les 10 pages en un seul fichier à importer
├── quiz/index.html ................... le quiz interactif complet
├── maquette-originale.html ........... votre maquette, conservée telle quelle
├── build.sh .......................... régénère a-coller/ et le fichier d'import
└── import-wordpress.py ............... fabrique import-wordpress.xml
```

**La règle à retenir :** on regarde dans `pages/`, on copie depuis `a-coller/`.

---

## Avant de commencer : quelle est votre formule exactement ?

Le mot « premium » recouvre deux réalités très différentes, et **cela change deux étapes**
de ce guide (le formulaire et le quiz). Regardez l'adresse de votre tableau de bord :

| Ce que vous voyez | Votre cas | Conséquences |
|---|---|---|
| `wordpress.com/…` — formule Premium souscrite chez WordPress.com | **Cas A — WordPress.com Premium** | Le CSS fonctionne. Le JavaScript est bloqué dans les blocs HTML → voir l'étape 8 pour le quiz. Pas d'extensions (plugins). |
| Votre propre hébergeur (o2switch, OVH, Hostinger…) avec un thème acheté | **Cas B — WordPress auto-hébergé** | Tout fonctionne, y compris le quiz collé directement et les extensions. |

Les étapes 1 à 7 sont identiques dans les deux cas.

---

## Étape 1 — Coller la charte graphique (5 min, à faire en premier)

Sans cette étape, toutes les pages s'afficheront en texte brut, sans mise en forme.

1. Ouvrez `site/assets/style.css` avec un éditeur de texte (Bloc-notes, TextEdit).
2. Sélectionnez **tout** (Ctrl+A / Cmd+A), copiez (Ctrl+C / Cmd+C).
3. Dans WordPress : **Apparence › Personnaliser › CSS additionnel**.
4. Collez dans le grand cadre. Cliquez sur **Publier**.

C'est fait une fois pour tout le site. Si un jour la mise en forme disparaît, c'est ici qu'il
faut revenir voir.

> Tout le code est enfermé dans un préfixe `.ads` : il ne peut pas déranger le reste de votre
> thème (menu, pied de page, articles de blog).

---

## Étape 2 — Importer les 10 pages en une seule fois (10 min)

C'est la voie rapide : un seul fichier crée les neuf pages du site (plus celle du quiz),
avec leurs titres, leurs adresses et tout leur contenu déjà en place.

1. Récupérez le fichier **`site/import-wordpress.xml`**.
2. Dans WordPress : **Outils › Importer › WordPress** › *Lancer l'importateur*.
   (S'il n'est pas encore là, WordPress vous propose de l'installer en un clic.)
3. Choisissez le fichier, puis **Téléverser et importer**.
4. À l'écran suivant, WordPress demande à qui attribuer le contenu : choisissez
   **votre compte** dans la liste déroulante « ou attribuer les articles à un utilisateur existant ».
5. Ne cochez pas « Télécharger et importer les fichiers joints » : il n'y a aucune image
   dans ce fichier, vos photos s'ajoutent à l'étape 5.

**Les 10 pages arrivent en brouillon**, volontairement : rien ne devient public tant que
vous ne l'avez pas décidé. Vous les publierez une par une depuis **Pages**, quand leur
contenu sera complété.

Vérifiez ensuite dans **Pages** que vous avez bien :

| Titre de la page | Adresse | État |
|---|---|---|
| Accueil | `accueil` | brouillon |
| Mon approche | `mon-approche` | brouillon |
| Accompagnements | `accompagnements` | brouillon |
| L'Atelier nomade | `atelier-nomade` | brouillon |
| À propos | `a-propos` | brouillon |
| Contact | `contact` | brouillon |
| Questions fréquentes | `faq` | brouillon |
| Mentions légales | `mentions-legales` | brouillon |
| Politique de confidentialité | `politique-de-confidentialite` | brouillon |
| Le quiz | `quiz` | brouillon |

> **Ce que l'import ne fait pas** — et qui reste à faire ensuite : la charte graphique
> (étape 1, à faire avant sinon les pages s'affichent sans mise en forme), les photos
> (étape 5), le menu et la page d'accueil (étape 4), le lien Calendly (étape 7),
> et toutes les informations entre crochets (étape 9).

> **Si l'import échoue** (fichier refusé, formule qui ne propose pas l'importateur) :
> passez à l'étape 3, la voie manuelle. Elle donne exactement le même résultat,
> en une trentaine de minutes de copier-coller.

---

## Étape 3 — La voie manuelle (uniquement si l'import n'a pas fonctionné)

**Si l'étape 2 a réussi, sautez directement à l'étape 4.**

D'abord créer les pages vides, dans **Pages › Ajouter**. Le *titre* est ce que vous tapez
en haut ; l'*adresse* se règle dans le panneau de droite, onglet **Page › Permalien**.

| # | Titre de la page | Adresse (permalien) | Fichier source |
|---|---|---|---|
| 1 | Accueil | (laissez, ce sera la racine) | `a-coller/01-accueil.html` |
| 2 | Mon approche | `mon-approche` | `a-coller/02-mon-approche.html` |
| 3 | Accompagnements | `accompagnements` | `a-coller/03-accompagnements.html` |
| 4 | L'Atelier nomade | `atelier-nomade` | `a-coller/04-atelier-nomade.html` |
| 5 | À propos | `a-propos` | `a-coller/05-a-propos.html` |
| 6 | Contact | `contact` | `a-coller/06-contact.html` |
| 7 | Questions fréquentes | `faq` | `a-coller/07-faq.html` |
| 8 | Mentions légales | `mentions-legales` | `a-coller/08-mentions-legales.html` |
| 9 | Politique de confidentialité | `politique-de-confidentialite` | `a-coller/09-politique-de-confidentialite.html` |

**Les adresses doivent être exactement celles-ci** : les boutons d'une page à l'autre pointent
dessus. Une adresse différente = un bouton qui mène à une page « introuvable ».

*(Page 10, le quiz, est optionnelle — voir l'étape 8.)*

Puis coller le contenu. Pour **chaque** page, toujours le même geste :

1. Ouvrez le fichier correspondant dans `a-coller/`, sélectionnez tout, copiez.
2. Dans WordPress, ouvrez la page, cliquez dans la zone de contenu.
3. Cliquez sur le **+** › tapez `html` › choisissez **HTML personnalisé**.
4. Collez dans le bloc.
5. **Mettre à jour**.

Pour vérifier : bouton **Aperçu** en haut à droite. Dans l'éditeur, le bloc HTML reste affiché
comme du code brut — c'est normal, seul l'aperçu montre le vrai rendu.

> ⚠️ **La page Contact est la seule exception** : elle contient **deux** blocs HTML séparés par
> le formulaire. Le fichier `a-coller/06-contact.html` les signale clairement
> (`BLOC HTML n°1` / `BLOC HTML n°2`). Voir l'étape 6.

---

## Étape 4 — Page d'accueil et menu (10 min)

**Définir l'accueil :** Réglages › Lecture › « Votre page d'accueil affiche » → **Une page
statique** → Page d'accueil : *Accueil*.

**Construire le menu :** Apparence › Menus (ou Apparence › Éditeur › Navigation selon le thème).
L'ordre recommandé, repris de votre maquette :

```
Accueil · Mon approche · Accompagnements · L'Atelier nomade · À propos · Contact
```

Plus, si votre thème le permet, un bouton **Prendre rendez-vous** pointant vers `/contact`.

**Dans le pied de page**, ajoutez un second menu :
`FAQ · Mentions légales · Politique de confidentialité · Instagram · Facebook`

Ajoutez-y aussi la phrase de votre maquette, obligatoire pour votre activité :

> *Les séances proposées soutiennent votre bien-être et votre développement personnel.
> Elles ne constituent pas un acte médical et ne remplacent ni un diagnostic, ni un traitement,
> ni un suivi par un professionnel de santé.*

---

## Étape 5 — Les photos (le poste le plus important)

Cinq emplacements sont matérialisés par des **cadres en pointillés turquoise** qui décrivent
la photo attendue. Tant qu'ils sont là, le site n'est pas fini.

| Où | Photo attendue |
|---|---|
| Accueil, « Qui vous accompagne » | Portrait en extérieur, lumière douce du matin, regard caméra, cadrage buste |
| À propos | Portrait plus intime : en marche, ou assise dans le van, lumière latérale |
| Atelier nomade (haut) | **La photo différenciante** : le van face à la mer ou en lisière de forêt, portes ouvertes |
| Atelier nomade (bas) | Intérieur du van : plaid, deux places assises, lumière chaleureuse |
| Contact | La carte du cabinet (bloc natif « Carte » de WordPress) |

**Comment remplacer un cadre par une vraie photo :**

1. Médias › Ajouter, envoyez la photo, copiez son **URL de fichier**.
2. Dans le bloc HTML de la page, repérez le bloc qui commence par `<div class="ads-photo">`
   et se termine par `</div>` (une seule ligne, elle contient le mot « Emplacement photo »).
3. Remplacez **toute cette ligne** par :

```html
<figure class="ads-visuel"><img src="COLLEZ_L_URL_ICI" alt="Décrivez la photo en quelques mots" loading="lazy"></figure>
```

Le texte `alt` n'est pas décoratif : il est lu par les personnes malvoyantes et par Google.
Décrivez ce qu'on voit (« Véronique assise dans son van aménagé, portes ouvertes sur la forêt »).

**Format conseillé :** largeur 1400 px, format JPEG, poids sous 300 Ko. Des photos trop lourdes
ralentissent le site, ce que Google pénalise.

---

## Étape 6 — Le formulaire de contact

Un formulaire écrit en HTML brut **n'enverrait aucun message** : il faut le bloc natif de
WordPress, seul capable de vous transmettre les demandes.

**Si vous avez utilisé l'import (étape 2)**, le formulaire est déjà en place, réglé sur
`latelier.decouvertedesoi@gmail.com` et sur le fond turquoise pâle. Ouvrez la page Contact
et vérifiez qu'il s'affiche normalement. S'il apparaît en erreur (« ce bloc contient un
contenu inattendu »), supprimez-le et reconstruisez-le à la main en suivant la liste
ci-dessous — c'est l'affaire de deux minutes. Passez ensuite directement au point 7.

**Si vous avez collé les pages à la main :**

1. Sur la page Contact, collez d'abord le **BLOC HTML n°1**.
2. En dessous, **+** › cherchez **Formulaire** (ou « Formulaire de contact ») › insérez-le.
3. Réglez ses champs pour obtenir :
   - Prénom et nom *(obligatoire)*
   - E-mail *(obligatoire)*
   - Téléphone *(facultatif)*
   - Votre message *(obligatoire, zone de texte)*
   - Case à cocher : « J'accepte que mes données soient utilisées pour répondre à ma demande. » *(obligatoire)*
   - Bouton : **Envoyer mon message**
4. Dans les réglages du bloc, indiquez l'adresse de réception : `latelier.decouvertedesoi@gmail.com`.
5. Sélectionnez le bloc Formulaire, puis dans le panneau de droite mettez sa **couleur d'arrière-plan
   sur `#DBEEEE`** — c'est le turquoise pâle de votre maquette, pour que le formulaire ne fasse pas
   une rupture blanche au milieu de la section.
6. En dessous, collez le **BLOC HTML n°2**.
7. **Testez-le vous-même** : envoyez un message depuis le site et vérifiez qu'il arrive bien.
   Regardez aussi les indésirables.

---

## Étape 7 — Le bouton de réservation (Calendly)

Dans le **BLOC HTML n°1** de la page Contact, remplacez `[VOTRE-LIEN-CALENDLY]` par l'adresse
de votre agenda, par exemple :

```html
<a class="ads-btn ads-block" style="max-width:340px" href="https://calendly.com/veronique-atelier/appel-decouverte">Choisir mon créneau</a>
```

Un simple lien fonctionne dans tous les cas de figure et sur tous les téléphones.
*(L'agenda intégré directement dans la page nécessite du JavaScript : impossible en cas A.)*

---

## Étape 8 — Le quiz (optionnel)

Le quiz a besoin de JavaScript pour calculer le résultat.

**Cas B (WordPress auto-hébergé) —** collez tout le contenu de `quiz/index.html` situé entre
`<body>` et `</body>` dans un bloc HTML personnalisé, et le `<style>…</style>` juste avant.
Tout fonctionnera.

**Cas A (WordPress.com Premium) —** le JavaScript y est bloqué. La solution la plus simple, et
gratuite : héberger le quiz sur **GitHub Pages** depuis votre dépôt.

1. Sur GitHub, dans votre dépôt : **Settings › Pages**.
2. « Source » : *Deploy from a branch* › branche `main` › dossier `/ (root)` › **Save**.
3. Après quelques minutes, le quiz est accessible à une adresse du type
   `https://latelierdecouvertedesoi.github.io/Quizz/site/quiz/`.
4. Créez la page WordPress **Le quiz** (`/quiz`) avec `a-coller/10-quiz.html`, et remplacez-y
   `[ADRESSE_DU_QUIZ]` par cette adresse.

Le quiz s'ouvre alors depuis votre site, dans votre charte graphique, sans surcoût.
Si vous préférez faire simple pour l'instant : ne créez pas la page 10, et le reste du site
fonctionne parfaitement sans elle.

---

## Étape 9 — Les informations qu'il ne reste que vous à remplir

Tout ce qui est **entre crochets** dans les fichiers est un trou à combler. Je ne pouvais pas
les inventer : ce sont des informations juridiques ou commerciales qui vous engagent.

**Sur les pages publiques :**

- [ ] `[90 €]` — le tarif réel de la séance. Il apparaît **3 fois** :
      accueil (étape 4), accompagnements (informations pratiques), FAQ (1ʳᵉ question).
- [ ] `[lieu exact à préciser]` — l'adresse de Retiers, sur la page Contact.
- [ ] `[VOTRE-LIEN-CALENDLY]` — page Contact.
- [ ] `[ADRESSE_DU_QUIZ]` — page Quiz, si vous la créez.

**Sur les mentions légales** (obligatoires, et vérifiables par n'importe qui) :

- [ ] Nom complet, adresse professionnelle, SIRET, code APE, statut juridique
- [ ] Mention TVA (ou « TVA non applicable, article 293 B du CGI »)
- [ ] Assureur en responsabilité civile professionnelle + n° de contrat
- [ ] **Médiateur de la consommation** : l'adhésion est obligatoire dès lors que vous
      travaillez avec des particuliers. Si ce n'est pas encore fait, à régler avant la mise en ligne.
- [ ] Crédits photo

**Sur la politique de confidentialité :**

- [ ] Les outils réellement utilisés (agenda, messagerie, newsletter éventuelle)
- [ ] Les durées de conservation que vous retenez
- [ ] La date de mise à jour

> Ces deux pages sont un **modèle de travail sérieux, pas un conseil juridique**.
> Faites-les relire par votre comptable ou un juriste avant publication.

---

## Étape 10 — Avant de publier

- [ ] **Titres et descriptions SEO** : chaque fichier de `pages/` contient, tout en haut dans un
      commentaire, un titre et une méta-description rédigés pour cette page. Recopiez-les dans
      votre outil de référencement (Yoast, Rank Math, ou les réglages SEO de WordPress.com).
- [ ] **Testez sur téléphone** : plus de la moitié de vos visiteuses viendront de là.
- [ ] **Cliquez sur tous les boutons** d'une page à l'autre. Une adresse mal saisie à l'étape 2
      se voit immédiatement.
- [ ] **Envoyez-vous un message** via le formulaire et **réservez un créneau** de test.
- [ ] Vérifiez qu'il ne reste **plus aucun crochet `[ ]`** ni cadre en pointillés en ligne.
- [ ] Faites relire les textes à voix haute par quelqu'un qui ne connaît pas votre métier.

---

## Si quelque chose ne s'affiche pas correctement

| Symptôme | Cause la plus fréquente |
|---|---|
| Tout est en texte brut, sans couleurs | Le CSS de l'étape 1 n'a pas été collé, ou pas publié |
| Les polices sont différentes du modèle | Fraunces/Karla se chargent depuis Google Fonts : vérifiez la première ligne du CSS (`@import`), elle doit être **tout en haut** |
| Un bouton mène à une page « introuvable » | L'adresse de la page ne correspond pas au tableau de l'étape 2 |
| Le formulaire n'envoie rien | Vous avez collé du HTML au lieu d'utiliser le bloc natif (étape 6) |
| Le quiz ne calcule pas le résultat | Cas A : le JavaScript est bloqué, passez par l'étape 8 |
| Une section a perdu son fond coloré | Le bloc HTML a été coupé : recollez le fichier entier de `a-coller/` |

---

## Modifier le site plus tard

Modifiez le fichier concerné dans `pages/`, puis lancez :

```bash
bash site/build.sh
```

Le dossier `a-coller/` **et** le fichier `import-wordpress.xml` sont régénérés, et le script
vérifie au passage la cohérence des repères DÉBUT/FIN.

Pour une retouche ponctuelle, le plus simple reste de modifier directement le bloc dans
l'éditeur WordPress. Ne réimportez pas le fichier XML sur un site déjà en ligne : l'import
créerait des doublons au lieu de mettre à jour les pages existantes.

---

## Deux remarques honnêtes

**Sur les anciens fichiers du dépôt.** `index.html.html` et `quiz_accompagnement linkee.html`
(à la racine) sont deux copies identiques de l'ancien quiz. Le nouveau, dans `site/quiz/`,
les remplace. Je ne les ai pas supprimés : c'est votre décision, pas la mienne.

**Sur les textes du quiz.** J'ai réécrit ses questions pour les aligner sur le positionnement
de votre maquette — le corps, les émotions, les schémas — là où l'ancienne version parlait
surtout de tarot et de libération émotionnelle. Le nombre de questions et le calcul du score
sont inchangés. Si vous préfériez les formulations d'origine, elles sont conservées dans les
deux fichiers de la racine.
