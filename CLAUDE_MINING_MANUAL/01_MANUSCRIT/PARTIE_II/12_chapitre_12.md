## Chapitre 12. Gérer efficacement les conversations, les informations et les contextes

### A. Mise en situation professionnelle

Sarah Mwamba, ingénieure planification, travaille depuis trois semaines dans **une seule** conversation avec Claude pour préparer le plan minier trimestriel. La conversation contient des dizaines d'échanges, plusieurs versions de tableaux, des hypothèses abandonnées et des chiffres corrigés. Aujourd'hui, Claude réutilise un rapport de découverture de 6,5 que Sarah avait corrigé à 6,0 deux semaines plus tôt. La conversation est devenue un grenier encombré, où le modèle ne sait plus quelle version fait foi.

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Décider** quand poursuivre une conversation et quand en ouvrir une nouvelle.
2. **Rédiger** un résumé de passation pour transférer le contexte utile.
3. **Utiliser** à bon escient la mémoire, la recherche dans les conversations passées et les conversations incognito.
4. **Organiser** vos conversations (nommage, rangement, projets).
5. **Gérer** les versions des informations de référence pour éviter la confusion.

### C. Comprendre avant de pratiquer

#### C.1. Une conversation n'est pas un classeur

Comme expliqué au chapitre 3, Claude travaille à partir de ce qui figure dans la **fenêtre de contexte** : vos instructions, les documents, l'historique. Dans une conversation très longue, des informations contradictoires s'accumulent (anciennes et nouvelles versions), et le risque augmente que le modèle s'appuie sur une version périmée ou néglige un détail.

![Figure 12.1. Conversations longues : pourquoi repartir sur une base propre. Courbes schématiques illustrant un principe d'usage, non une mesure. Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/GRAPHIQUES/fig12_1_contexte_conversation.png){width=85%}

#### C.2. Quand ouvrir une nouvelle conversation ?

| Signal | Action |
|---|---|
| Changement de sujet | Nouvelle conversation |
| Plusieurs versions d'un même chiffre ou document dans l'historique | Nouvelle conversation avec la seule version de référence |
| Réponses qui reprennent des hypothèses abandonnées | Nouvelle conversation + résumé de passation |
| Tâche récurrente avec les mêmes documents de référence | Créer un projet (chapitre 15) |
| Information sensible ponctuelle, à ne pas conserver | Conversation incognito (si autorisée par la charte) |

#### C.3. Le résumé de passation

Le **résumé de passation** est un texte court qui résume l'état d'un travail : objectif, décisions prises, données de référence (versions validées), points en suspens, prochaines étapes. Vous pouvez demander à Claude de le rédiger en fin de conversation, puis le relire, le corriger et le coller au début d'une nouvelle conversation.

::: retenir
Le résumé de passation doit être **validé par vous**. C'est lui qui « fait foi » pour la suite : une erreur qui s'y glisse se propagera.
:::

#### C.4. Mémoire, recherche dans les conversations et mode incognito

Le centre d'aide décrit trois fonctions complémentaires [@ANT-HC-MEMORY] :

- **La recherche dans les conversations passées** (offres payantes) : vous pouvez demander à Claude de retrouver ce qui a été dit dans une conversation antérieure ; la recherche apparaît comme un appel d'outil. Hors projets, elle porte sur les conversations hors projet ; dans un projet, elle est limitée au projet.
- **La mémoire** : Claude peut retenir des éléments de vos conversations et les réutiliser dans de nouvelles conversations. Depuis 2026, la mémoire fonctionne sous forme d'entrées catégorisées, consultables, modifiables et supprimables par thème dans les réglages ; certains sujets sensibles en sont exclus sauf activation explicite [@ANT-HC-RELEASE]. Dans les offres Team et Enterprise, ce sont les propriétaires de l'organisation qui décident de sa disponibilité.
- **Les conversations incognito** : conversations temporaires, non enregistrées dans l'historique et non utilisées par la recherche dans les conversations ; le centre d'aide précise que, pour les offres Team et Enterprise, elles restent incluses dans les exports de données et soumises aux règles de conservation de l'organisation.

::: attention
La mémoire est pratique, mais elle peut **mélanger les contextes** (une hypothèse d'un ancien projet ressurgit) ou **conserver des informations sensibles**. Consultez régulièrement ce que Claude a retenu et supprimez ce qui n'a pas lieu d'être.
:::

#### C.5. Organiser ses conversations

- **Nommer** chaque conversation importante selon une règle commune (chapitre 7).
- **Regrouper** les conversations d'un même dossier dans un **projet** : instructions et documents de référence y sont partagés (chapitre 15).
- **Supprimer** les conversations inutiles contenant des informations sensibles, conformément à la politique de conservation de l'entreprise.
- **Archiver hors de Claude** les livrables validés : Claude n'est pas votre système de gestion documentaire officiel.

#### C.6. Gérer les versions de référence

La règle d'or : **une seule version de référence par information**, clairement datée. Dans vos instructions, indiquez explicitement ce qui fait foi : « Les hypothèses de référence sont celles du tableau ci-dessous, version du 12/11/2026 ; ignore toute valeur antérieure. »

### D. Démonstration guidée : Remettre de l'ordre dans le plan minier de Sarah

1. **Diagnostic** : Sarah demande à Claude, dans la conversation encombrée, la liste de toutes les valeurs différentes utilisées pour chaque hypothèse clé (prompt 12.2). Le résultat met en évidence trois valeurs de découverture (6,5 ; 6,2 ; 6,0) et deux taux de disponibilité de la flotte.
2. **Validation** : Sarah établit elle-même le tableau des hypothèses de référence (version datée).
3. **Passation** : elle demande un résumé de passation (prompt 12.1), le corrige (une décision était mal résumée) et l'enregistre.
4. **Redémarrage** : elle crée un projet « Plan minier T1 2027 », place le tableau d'hypothèses dans les connaissances du projet, colle le résumé de passation dans une nouvelle conversation et reprend le travail.
5. **Discipline** : à chaque changement d'hypothèse, elle met à jour le tableau de référence du projet, et non la conversation.

### E. Prompts commentés

**Prompt 12.1. Résumé de passation**

```text
Nous allons poursuivre ce travail dans une nouvelle conversation.
Rédige un résumé de passation de 300 mots maximum, structuré ainsi :
1. Objectif du travail.
2. Décisions prises (avec la date ou l'échange où elles ont été prises).
3. Données de référence actuellement valides (valeurs, unités, versions).
4. Points en suspens et questions ouvertes.
5. Prochaines étapes.
Signale toute information pour laquelle plusieurs versions contradictoires
existent dans notre conversation, au lieu d'en choisir une.
```

*Commentaire.* La dernière consigne est essentielle : elle évite que Claude « tranche » silencieusement entre deux versions.

**Prompt 12.2. Inventaire des incohérences d'une conversation**

```text
Liste toutes les valeurs que nous avons utilisées dans cette conversation pour :
[rapport de découverture, disponibilité de la flotte, teneur moyenne, tonnage mensuel].
Pour chaque paramètre, indique chaque valeur rencontrée et le contexte où elle apparaît.
Ne choisis pas la « bonne » valeur.
```

**Prompt 12.3. Démarrage d'une nouvelle conversation**

```text
Voici le résumé de passation validé d'un travail en cours : <passation> … </passation>
Les données de référence de ce résumé font foi et remplacent toute autre valeur.
Confirme ta compréhension en 5 lignes, puis attends ma prochaine instruction.
```

**Prompt 12.4. Retrouver une information passée (offres payantes)**

```text
Cherche dans mes conversations précédentes ce que nous avions conclu sur
[sujet] et indique dans quelle conversation et à quelle date approximative.
Si tu trouves plusieurs conclusions différentes, présente-les toutes.
```

### F. Exercices pratiques

**Exercice 12.1 (guidé) : Passation**

Reprenez votre plus longue conversation avec Claude. Utilisez le prompt 12.1, corrigez le résumé, puis poursuivez dans une nouvelle conversation avec le prompt 12.3. Comparez la qualité des réponses avant et après.

**Exercice 12.2 (guidé) : Audit de mémoire**

Consultez ce que la mémoire de Claude a retenu sur vous (si la fonction est activée). Supprimez ce qui est inexact, obsolète ou sensible.

**Exercice 12.3 (autonome) : Règles d'organisation de votre équipe**

Rédigez une page de règles pour votre équipe : nommage, usage des projets, usage du mode incognito, durée de conservation, archivage des livrables.

### G. Livrable professionnel

**Tableau des données de référence** d'un dossier en cours (paramètre, valeur, unité, source, version, date de validation, validé par) et **résumé de passation** validé.

### H. Vérification des résultats

::: controle
- Le résumé de passation a été relu et corrigé avant usage.
- Une seule valeur de référence par paramètre, datée et sourcée.
- La mémoire ne contient pas d'information sensible ni obsolète.
- Les livrables validés sont archivés dans le système documentaire officiel.
:::

::: setrompe
Dans une conversation où deux versions d'un budget coexistent, Claude calcule un total en mélangeant des lignes de la version 1 et de la version 2. Le résultat est plausible, mais ne correspond à aucune version. **Contre-mesure** : une conversation propre par version, et demande systématique de la source de chaque chiffre.
:::

### I. Limites et précautions

- La recherche dans les conversations et la mémoire dépendent de l'offre et des réglages de l'organisation.
- Le mode incognito n'est pas un mode « secret » : dans les organisations, ces conversations restent soumises aux règles de conservation et d'export.
- Claude n'est pas un système d'archivage ; ne comptez pas sur l'historique des conversations pour la traçabilité réglementaire.

### J. Boîte à outils

**Les cinq règles d'hygiène des conversations**

1. Un sujet = une conversation.
2. Une version de référence par information, datée.
3. Passation écrite et validée à chaque redémarrage.
4. Projet pour tout dossier récurrent.
5. Revue mensuelle de la mémoire et des conversations sensibles.

### K. Quiz

1. **(Vrai ou faux)** Une conversation très longue améliore toujours la qualité des réponses parce que Claude dispose de plus de contexte.
2. **(QCM)** Que contient un bon résumé de passation ? a) toute la conversation copiée ; b) objectif, décisions, données de référence, points en suspens, prochaines étapes ; c) uniquement la dernière réponse ; d) les identifiants de connexion.
3. **(Compréhension)** Quelle est la différence entre la mémoire et la recherche dans les conversations passées ?
4. **(Vrai ou faux)** Dans une organisation Team ou Enterprise, les conversations incognito sont exclues de toute règle de conservation.
5. **(Mise en situation)** Claude utilise une ancienne valeur d'hypothèse. Que faites-vous ?
6. **(QCM)** Quand faut-il créer un projet plutôt qu'une simple conversation ? a) pour une question ponctuelle ; b) pour un dossier récurrent avec des documents de référence ; c) jamais ; d) pour chaque message.
7. **(Compréhension)** Pourquoi demander à Claude de signaler les versions contradictoires plutôt que de choisir ?
8. **(Application)** Rédigez la phrase qui indique à Claude quelles données font foi.
9. **(Analyse critique)** Pourquoi Claude ne doit-il pas servir de système d'archivage officiel ?
10. **(Vrai ou faux)** Il est recommandé de consulter et nettoyer régulièrement la mémoire de Claude.

<div class="carnet" titre="Chapitre 12. Gérer efficacement les conversations, les informations et les contextes"></div>
