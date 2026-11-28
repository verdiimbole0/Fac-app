## Chapitre 5. Ce que Claude sait faire et ce qu'il ne sait pas faire

### A. Mise en situation professionnelle

Me Henriette Ngoy, juriste principale de MCC, prépare une note sur les obligations de l'entreprise en matière de redevances. Elle demande à un assistant d'IA de citer « l'article du Code minier qui fixe le taux applicable au cobalt ». La réponse arrive en quelques secondes : un numéro d'article précis, un alinéa, un taux, et même une référence au Journal officiel. Tout semble parfait. Par réflexe professionnel, Me Ngoy ouvre le texte officiel : l'article cité ne traite pas du tout de ce sujet, et la référence du Journal officiel n'existe pas.

Elle n'a pas perdu de temps : elle a vérifié. Mais combien de collègues auraient copié la réponse dans leur note ?

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Lister** les grandes capacités de Claude utiles dans le travail minier.
2. **Expliquer** ce qu'est une hallucination et pourquoi elle se produit.
3. **Reconnaître** les signaux d'alerte d'une réponse potentiellement inventée.
4. **Classer** une tâche selon les conséquences d'une erreur et la facilité de vérification.
5. **Appliquer** les techniques qui réduisent les hallucinations (sources fournies, citations, droit de dire « je ne sais pas »).

### C. Comprendre avant de pratiquer

#### C.1. Ce que Claude sait bien faire

*Tableau 5.1. Capacités principales et exemples miniers.*

| Capacité | Exemple à MCC | Niveau de vigilance |
|---|---|---|
| Rédiger et reformuler | Premier jet d'un rapport d'incident, d'une procédure, d'un courrier à l'administration | Moyen : vérifier les faits |
| Résumer de longs documents | Synthèse d'une étude d'impact de 400 pages, d'un contrat de 80 pages | Moyen : vérifier qu'aucun point clé n'est omis |
| Extraire des informations | Obligations et échéances d'un contrat, valeurs d'un certificat d'analyse | Élevé : contrôle par échantillonnage |
| Comparer | Deux versions d'une procédure, un contrat et un modèle standard | Moyen |
| Analyser des données (avec exécution de code) | Écarts budgétaires, tendance des incidents, statistiques de sondages | Élevé : vérifier méthode et résultats |
| Classer et catégoriser | Plaintes communautaires par thème, incidents par type | Moyen : contrôler un échantillon |
| Traduire | Contrat de vente anglais-français, rapport technique | Moyen à élevé selon l'enjeu juridique |
| Expliquer, former | Expliquer une norme, préparer un quiz de formation | Faible à moyen |
| Programmer | Script d'analyse d'un fichier de production | Élevé : tester le code |
| Analyser des images | Photo de défaut sur une pièce, graphique de production | Élevé : interprétation prudente |

#### C.2. Ce que Claude ne sait pas faire (ou ne doit pas faire)

- **Connaître ce qu'il n'a pas vu** : vos procédures internes, vos données de production, les événements postérieurs à sa date limite de connaissances (sauf si vous les fournissez ou s'il effectue une recherche).
- **Observer le terrain** : il ne voit pas le front de taille, ne sent pas l'odeur d'un échauffement, n'entend pas le bruit d'un roulement.
- **Garantir l'exactitude** : il produit du texte plausible, qui peut être faux.
- **Assumer une responsabilité** : il ne signe pas un rapport, n'est pas « personne compétente » au sens des codes de déclaration des ressources, ne porte pas la responsabilité juridique d'une décision.
- **Décider en matière de sécurité critique** : tirs et explosifs, stabilité des talus, des digues et des galeries, interventions d'urgence, autorisation de travaux dangereux.

#### C.3. Les hallucinations

Une **hallucination** est une réponse fausse, inventée ou non fondée, présentée avec la même assurance qu'une réponse exacte. Le profil de risque de l'IA générative publié par le NIST parle de **confabulation** : la production de contenus erronés ou faux présentés avec assurance [@NIST-GAI]. Les travaux de recherche distinguent notamment les contenus **incohérents avec la source fournie** et les contenus **impossibles à vérifier ou contraires aux faits** [@JI-2023].

![Figure 5.1. Anatomie d'une hallucination. La réponse est précise, assurée et bien formulée… mais rien ne garantit que ses éléments existent. Les signaux d'alerte aident à repérer les réponses à vérifier en priorité. Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/SCHEMAS/fig05_1_hallucination.png){width=95%}

**Pourquoi se produisent-elles ?** Parce que le modèle génère ce qui est probable dans le contexte (chapitre 3). Si la question appelle un numéro d'article, le modèle sait à quoi ressemble un numéro d'article ; s'il ne dispose pas de l'information exacte, il peut produire un numéro plausible. Les hallucinations sont plus fréquentes :

- sur les **références précises** (articles de loi, numéros de norme, pages, DOI, auteurs) ;
- sur les **faits peu documentés** ou très locaux (une mine précise, une décision administrative locale) ;
- sur les **informations récentes** ;
- sur les **chiffres** et les **calculs** non outillés ;
- lorsque la question **présuppose** une information fausse (« Pourquoi la teneur de coupure a-t-elle été relevée en 2024 ? » alors qu'elle ne l'a pas été).

#### C.4. Réduire les hallucinations

La documentation d'Anthropic propose plusieurs techniques [@ANT-HALLU] :

1. **Autoriser explicitement l'incertitude** : permettre à Claude de répondre « je ne sais pas » ou « l'information n'est pas disponible ».
2. **Ancrer la réponse dans des citations directes** : pour les longs documents, demander d'abord l'extraction de citations exactes, puis l'analyse fondée sur ces citations.
3. **Vérifier par citation** : demander que chaque affirmation soit appuyée par une citation ; supprimer les affirmations non étayées.
4. **Restreindre aux documents fournis** : interdire l'usage des connaissances générales lorsque seule la source fournie fait foi.
5. **Comparer plusieurs réponses** : poser plusieurs fois la même question ; des réponses incohérentes signalent un risque.
6. **Affiner par itérations** : demander à Claude de vérifier ou de développer ses propres affirmations.

La même documentation rappelle que ces techniques **réduisent** les hallucinations sans les éliminer complètement, et qu'il faut toujours valider les informations critiques [@ANT-HALLU].

::: retenir
La meilleure protection contre les hallucinations n'est pas une formule magique : c'est **la source fournie + la citation exigée + la vérification humaine**.
:::

#### C.5. Les autres limites et risques

| Risque | Description | Exemple minier |
|---|---|---|
| Omission | Une synthèse oublie un point important | Le résumé d'une EIES omet un engagement de suivi des eaux souterraines |
| Biais | Réponse influencée par des représentations dominantes | Recommandations RH reproduisant des stéréotypes de genre sur certains postes |
| Erreur de calcul | Résultat numérique faux | Moyenne simple au lieu d'une moyenne pondérée |
| Complaisance | Le modèle abonde dans le sens de la question | Il « confirme » une hypothèse de cause d'incident suggérée dans la question |
| Instructions cachées | Un document contient des instructions malveillantes (injection de prompt) | Une procédure piégée demande à l'IA de déclarer un document conforme (chapitre 38) |
| Confidentialité | Des données sensibles sont partagées hors du cadre autorisé | Contrat confidentiel analysé sur un compte personnel |
| Dépendance | Perte de compétences ou d'esprit critique | Un jeune ingénieur ne sait plus rédiger sans assistant |

#### C.6. Une matrice pour décider

![Figure 5.2. Matrice de décision. Croisez les conséquences d'une erreur et la facilité de vérification pour déterminer le niveau d'usage approprié. Le quadrant « conséquences graves, difficile à vérifier » reste hors du champ de délégation. Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/SCHEMAS/fig05_2_matrice_risque_verif.png){width=78%}

### D. Démonstration guidée : Transformer une question à risque en question sûre

Me Ngoy reprend sa question sur les redevances, cette fois avec méthode.

**Version risquée :**

```text
Quel article du Code minier fixe le taux de redevance du cobalt ? Cite-le.
```

**Version sûre, en trois étapes :**

1. Elle télécharge le texte officiel du Code minier tel que modifié en 2018 [@RDC-CODE-2018] et les textes d'application pertinents, depuis une source fiable.
2. Elle les fournit à Claude avec le prompt 5.1 (ci-dessous), qui exige des citations exactes et autorise la réponse « non trouvé ».
3. Elle vérifie chaque citation dans le texte original, puis rédige sa note en citant le texte officiel, et non la réponse de Claude.

Résultat : Claude identifie les dispositions pertinentes, cite les passages, signale qu'une partie de l'information (le classement d'une substance comme « stratégique ») dépend d'un acte réglementaire distinct qui n'a pas été fourni, et suggère de l'obtenir. La note finale est exacte et traçable.

### E. Prompts commentés

**Prompt 5.1. Recherche ancrée dans un texte officiel**

```text
Tu assistes une juriste d'entreprise minière. Voici le texte officiel fourni :
<texte_officiel>
[coller le texte ou joindre le PDF]
</texte_officiel>

Question : quelles dispositions de ce texte traitent du taux de la redevance minière
et de son assiette ?

Règles impératives :
1. Réponds uniquement à partir du texte fourni, sans utiliser tes connaissances générales.
2. Pour chaque disposition, cite le passage exact entre guillemets et indique l'article.
3. Si le texte renvoie à un autre acte (décret, arrêté) non fourni, signale-le.
4. Si l'information n'est pas dans le texte, écris « Non trouvé dans le texte fourni ».
5. N'interprète pas : distingue clairement citation et commentaire.
```

*Commentaire.* Chaque règle correspond à une technique anti-hallucination : restriction aux documents, citation directe, droit de dire « non trouvé ». La règle 3 est particulièrement utile en droit minier, où les taux et modalités dépendent souvent de textes d'application.

**Prompt 5.2. Vérification a posteriori**

```text
Reprends ta réponse précédente. Pour chaque affirmation factuelle :
- indique la citation exacte du document qui la justifie ;
- si tu ne trouves pas de citation, retire l'affirmation et signale-la par [retirée].
Présente ensuite la version nettoyée de la réponse.
```

**Prompt 5.3. Détecter une question piégée**

```text
Avant de répondre, vérifie si ma question contient une présupposition non démontrée.
Si c'est le cas, signale-la et ne la traite pas comme un fait.
Question : [votre question]
```

### F. Exercices pratiques

**Exercice 5.1 (guidé) : Chasse aux hallucinations**

Posez à Claude, **sans lui fournir de source**, les trois questions suivantes, puis vérifiez chaque élément de réponse dans une source officielle :

1. « Quelle est la date de publication de la Norme mondiale de l'industrie sur la gestion des résidus miniers (GISTM) et qui l'a co-organisée ? »
2. « Cite trois articles précis du Code minier congolais relatifs aux obligations environnementales, avec leur contenu. »
3. « Donne la référence complète (auteurs, titre, revue, année) de trois articles scientifiques sur l'IA générative dans les mines. »

Pour chaque question, classez la réponse : exacte, partiellement exacte, inventée, invérifiable. *Indice : la GISTM a été publiée le 5 août 2020, à l'issue d'un processus co-organisé par l'ICMM, le PNUE et les PRI [@GISTM-2020].*

**Exercice 5.2 (guidé) : Reformuler avec les techniques anti-hallucination**

Reprenez la question 2 en fournissant un texte officiel et en utilisant le prompt 5.1. Comparez la qualité et la traçabilité des deux réponses.

**Exercice 5.3 (autonome) : Votre matrice personnelle**

Placez dix tâches de votre métier dans la matrice de la figure 5.2. Pour chaque quadrant, définissez votre règle d'usage (libre, avec relecture, avec vérification systématique, exclu).

### G. Livrable professionnel

**Fiche « Règles d'usage selon le risque »** pour votre service : la matrice remplie avec vos tâches, la règle par quadrant, et les techniques anti-hallucination obligatoires pour les tâches du quadrant « vérification systématique ».

### H. Vérification des résultats

::: controle
**Check-list anti-hallucination**

- Chaque référence (article, norme, rapport, auteur) a été retrouvée dans la source originale.
- Chaque chiffre provient d'un document fourni ou d'un calcul outillé, vérifié.
- Les citations entre guillemets correspondent mot pour mot au document.
- Les réponses « trop parfaites » (précision excessive, ton très assuré, absence de nuance) ont été contrôlées en priorité.
- La question ne contenait pas de présupposition fausse.
:::

::: setrompe
Vous fournissez un rapport de 120 pages et demandez « les cinq principales recommandations ». Claude en restitue cinq, dont quatre figurent dans le rapport et une qui « ressemble » aux autres mais n'y figure pas. **Contre-mesure** : exigez la page et la citation exacte pour chaque recommandation, puis contrôlez-les.
:::

### I. Limites et précautions

- Même avec toutes les techniques, **le risque zéro n'existe pas** : la vérification humaine reste obligatoire pour toute information engageante.
- Un document fourni peut lui-même contenir des erreurs : Claude les reproduira fidèlement.
- La qualité diminue lorsque la demande est vague, le contexte insuffisant ou le document de mauvaise qualité (scan illisible, tableaux mal structurés).

### J. Boîte à outils

**Les six techniques anti-hallucination (d'après Anthropic)**

1. Autoriser « je ne sais pas ».
2. Extraire d'abord des citations exactes.
3. Exiger une citation pour chaque affirmation.
4. Restreindre aux documents fournis.
5. Comparer plusieurs réponses.
6. Itérer en demandant vérification.

**Phrase type à ajouter aux prompts sensibles**

```text
Si tu n'es pas certain d'une information, dis-le explicitement. Je préfère
une réponse incomplète mais exacte à une réponse complète mais incertaine.
```

### K. Quiz

1. **(QCM)** Une hallucination est : a) un bug de l'interface ; b) une réponse fausse ou inventée présentée avec assurance ; c) un refus de répondre ; d) une réponse trop longue.
2. **(Vrai ou faux)** Les techniques anti-hallucination recommandées par Anthropic éliminent totalement le risque.
3. **(Compréhension)** Pourquoi les références précises (numéros d'articles, DOI) sont-elles particulièrement exposées aux hallucinations ?
4. **(QCM)** Quelle technique consiste à demander d'abord des extraits mot pour mot d'un long document ? a) la comparaison de réponses ; b) l'ancrage par citations directes ; c) l'itération ; d) l'apprentissage par renforcement.
5. **(Mise en situation)** Claude vous propose une cause d'incident qui confirme exactement l'hypothèse formulée dans votre question. Quel risque soupçonnez-vous et que faites-vous ?
6. **(Vrai ou faux)** Claude peut être désigné comme « personne compétente » pour signer une déclaration de ressources minérales.
7. **(Application)** Dans quel quadrant de la matrice placez-vous « valider un plan de tir » ? Pourquoi ?
8. **(Compréhension)** Citez quatre signaux d'alerte d'une réponse potentiellement inventée.
9. **(Analyse critique)** « Si la réponse est bien rédigée, elle est probablement exacte. » Discutez.
10. **(QCM)** Le profil de risque de l'IA générative du NIST désigne la production de contenus faux présentés avec assurance par le terme : a) dérive ; b) confabulation ; c) surapprentissage ; d) latence.

<div class="carnet" titre="Chapitre 5. Ce que Claude sait faire et ce qu'il ne sait pas faire"></div>
