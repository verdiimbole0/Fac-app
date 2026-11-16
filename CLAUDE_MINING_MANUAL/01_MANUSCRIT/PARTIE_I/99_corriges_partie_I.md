## Corrigés des quiz — Partie I

*Chaque réponse est expliquée : pourquoi elle est juste, et pourquoi les autres propositions ne le sont pas.*

### Chapitre 1

1. **c) 73 %.** L'USGS estime la production congolaise de cobalt extrait à 230 000 t sur environ 310 000 t en 2025. 25 % et 50 % sous-estiment fortement ; 95 % surestime (l'Indonésie représente à elle seule environ 14 %).
2. **Faux.** L'IA générative agit surtout sur le travail documentaire et intellectuel (lire, écrire, analyser). Le pilotage des équipements relève de l'automatisation et, éventuellement, de l'IA prédictive, avec des systèmes de contrôle dédiés.
3. **b).** Prédire une panne à partir de vibrations exploite des données structurées pour produire une alerte : c'est de l'IA prédictive. Les trois autres tâches produisent du texte (générative).
4. *Exemples attendus :* rapports de poste et de production, plans de tir, ordres de travail de maintenance, déclarations d'incident, bilans métallurgiques, rapports de suivi environnemental. Toute réponse comportant trois familles pertinentes est correcte.
5. **Faux.** Partir des fonctionnalités conduit à des usages génériques. Il faut partir des tâches réelles, de leur volume et de leurs contraintes.
6. *Réponse attendue :* la décision d'arrêt d'un chantier pour raison de sécurité relève des personnes qualifiées et des procédures de l'entreprise. Claude peut aider à rédiger la procédure, à préparer un tableau de suivi des précipitations ou un message d'alerte, mais pas à décider.
7. **c).** Le fait que la tâche soit appréciée par l'équipe n'entre pas dans la qualification du potentiel et du risque. Les trois autres questions font partie de la grille.
8. *Réponse attendue :* exiger la source précise (auteurs, titre, date, lien), la consulter, vérifier que l'étude existe et qu'elle dit bien cela, et vérifier qu'elle est transposable à votre contexte. Sans source vérifiée, le chiffre ne doit pas être utilisé.
9. *Réponse attendue :* intérêt potentiellement fort (volume) mais risque **élevé** (relation avec les communautés, engagement de l'entreprise, sensibilité sociale). L'absence de relecture est inacceptable : Claude peut proposer des projets de réponse, relus et validés par le responsable des relations communautaires.
10. *Réponse attendue :* un modèle ne corrige pas des données erronées ; il peut produire une analyse impeccablement rédigée à partir de données fausses, ce qui rend l'erreur plus difficile à détecter.

### Chapitre 2

1. **b).** L'apprentissage profond est une sous-famille de l'apprentissage automatique (réseaux de neurones à nombreuses couches). Ce n'est ni une alternative, ni un synonyme de l'IA générative (qui en est une application).
2. **Faux.** Dans un système à règles, ce sont des humains qui écrivent les règles ; le système n'apprend pas.
3. **b) le Transformer**, présenté dans « Attention Is All You Need » (2017). Le perceptron est un modèle de neurone ancien ; le krigeage est une méthode géostatistique ; l'arbre de décision est un autre type de modèle.
4. *Réponse attendue :* un coefficient numérique qui pondère l'influence d'une entrée sur un neurone ; les poids sont ajustés pendant l'entraînement.
5. *Exemple :* prédire la récupération métallurgique à partir des caractéristiques du minerai ; la « bonne réponse » connue est la récupération mesurée lors des essais ou de l'exploitation passée.
6. **Faux.** Claude n'est pas conçu pour remplacer les logiciels spécialisés (modélisation géologique, planification). Il peut aider à documenter, expliquer, analyser des exports, écrire des scripts.
7. *Réponse attendue :* le modèle sort de son domaine de validité (minéralogie différente) ; ses prédictions risquent d'être fausses. Il faut le revalider ou le réentraîner sur des données sulfurées.
8. **c).** Un projet de procédure rédigé est un contenu nouveau. Les trois autres sorties sont typiques de l'IA prédictive.
9. *Réponse attendue :* parce que la responsabilité porte sur les effets des résultats (décisions, actions) ; insister sur l'influence rappelle que l'utilisateur doit maîtriser l'usage qui en est fait.
10. *Réponse attendue :* générative — affirmation fausse mais plausible (hallucination), erreur de calcul, omission dans une synthèse ; prédictive — fausse alerte ou panne non détectée.

### Chapitre 3

1. **b).** Un token est un fragment de texte. Ce n'est ni un mot de passe, ni un fichier ; le coût via l'API dépend du nombre de tokens, mais un token n'est pas un coût fixe par question.
2. **Faux.** Le modèle génère du texte à partir de régularités apprises ; il ne consulte pas une base de faits (sauf s'il utilise un outil de recherche).
3. *Réponse attendue :* l'analyse de texte correspond à sa force (langage) ; une addition « de tête » repose sur une génération token par token, avec des nombres fragmentés, sans calcul exact. Avec l'exécution de code, le calcul devient fiable.
4. **c) 1 million de tokens**, selon la documentation consultée le 16/11/2026.
5. **Faux.** Ses connaissances s'arrêtent à sa date limite d'entraînement ; il ne connaît un texte récent que si vous le fournissez ou s'il effectue une recherche.
6. *Exemple de consigne :* « Avec l'exécution de code, calcule la teneur moyenne en Cu pondérée par la longueur des passes (a − de) pour les 40 lignes du fichier joint ; affiche la formule, le nombre de lignes utilisées et le code. »
7. **b) IA constitutionnelle** (Bai et al., 2022). Les autres termes désignent d'autres techniques ou n'ont pas de rapport.
8. *Réponse attendue :* faux. Une grande fenêtre permet beaucoup, mais un contexte surchargé d'informations inutiles augmente le risque que des détails importants soient négligés. Mieux vaut fournir des documents ciblés.
9. *Réponse attendue :* capacité à traiter plusieurs types de données (texte, images). Exemples : analyser une photo de pièce usée, lire un graphique de production, extraire un tableau d'un PDF scanné.
10. *Réponse attendue :* exiger l'exécution de code, afficher la formule et le code, indiquer le nombre de lignes traitées, recouper avec un tableur.

### Chapitre 4

1. **c) Opus 5.5**, d'après la page « Models overview ». Haiku et Sonnet sont recommandés pour la vitesse et le volume ; Fable 5.2 pour les raisonnements les plus exigeants.
2. **Vrai.** Claude Code est un outil de développement et d'automatisation, surtout destiné aux profils techniques.
3. *Réponse attendue :* l'application est une interface prête à l'emploi pour les utilisateurs ; l'API permet aux développeurs d'intégrer les modèles dans des applications de l'entreprise.
4. **a) Haiku 5.5**, positionné pour les tâches à fort volume, sensibles à la latence (classification, extraction, routage).
5. **Faux.** Ils changent plusieurs fois par an ; il faut consulter la documentation officielle.
6. *Réponse attendue :* ne pas le faire ; utiliser l'environnement validé par l'entreprise (offre d'entreprise), après vérification du niveau de confidentialité et des règles de la charte IA.
7. *Réponse attendue :* politique d'utilisation, politique de confidentialité, conditions commerciales, documentation des modèles, centre de transparence.
8. **a)** Le partage de projets entre collègues est réservé aux offres Team et Enterprise. Les autres propositions sont fausses ou décrivent des limites de l'offre gratuite.
9. *Réponse attendue :* la mémoire du modèle peut être dépassée (date limite d'entraînement) ; l'extrait fourni est à jour et vérifiable.
10. *Réponse attendue :* l'accès aux modèles via la plateforme cloud déjà utilisée (Amazon Bedrock, Google Cloud ou Microsoft Foundry).

### Chapitre 5

1. **b).** Une hallucination est un contenu faux ou inventé présenté avec assurance. Ce n'est ni un bug d'interface, ni un refus, ni une question de longueur.
2. **Faux.** La documentation précise que ces techniques réduisent le risque sans l'éliminer.
3. *Réponse attendue :* le modèle sait à quoi ressemble une référence et peut en générer une plausible sans disposer de l'information exacte.
4. **b) l'ancrage par citations directes.**
5. *Réponse attendue :* complaisance ou présupposition dans la question. Reformuler de manière neutre, demander les hypothèses alternatives et les éléments qui contredisent l'hypothèse.
6. **Faux.** Seule une personne qualifiée, membre d'une organisation professionnelle reconnue, peut être personne compétente.
7. *Réponse attendue :* conséquences graves + vérification difficile hors expertise → quadrant « Claude ne décide pas ». La validation d'un plan de tir appartient aux personnes habilitées.
8. *Réponse attendue :* précision excessive, références introuvables, ton très assuré sans source, chiffres trop parfaits, contradiction avec vos documents.
9. *Réponse attendue :* faux. La qualité rédactionnelle n'est pas un indicateur d'exactitude ; les hallucinations sont souvent très bien rédigées.
10. **b) confabulation.**

### Chapitre 6

1. **Faux.** La personne compétente est un professionnel qualifié, membre d'une organisation reconnue, qui engage sa responsabilité.
2. **b)** La validation d'un plan de tir. Les trois autres tâches sont des usages acceptables avec relecture.
3. *Réponse attendue :* une organisation dans laquelle un humain cadre, vérifie, corrige et valide les résultats produits avec l'IA, à des étapes définies.
4. *Réponse attendue :* illusion de contrôle ; les erreurs passent inaperçues ; la responsabilité de l'erreur reste la sienne.
5. **a) ICMM.**
6. *Réponse attendue :* préparer la check-list d'inspection, structurer le compte rendu d'inspection, synthétiser les données d'auscultation déjà validées, rédiger la note de transmission — sans conclure sur la stabilité.
7. **Vrai.**
8. *Réponse attendue :* la sécurité de l'usage repose sur la capacité de l'expert à juger le résultat ; si cette capacité s'érode, les erreurs ne sont plus détectées.
9. *Réponse attendue :* cadrer, vérifier, valider et signer.
10. *Exemple :* « Ton rôle est limité à structurer les éléments factuels fournis et à lister les questions à instruire ; la détermination des causes et des actions appartient à l'équipe d'enquête. »
