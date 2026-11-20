# Contrôle scientifique et technique

## Exactitude des explications techniques (modules 1, 2, 3, 9, 19)

| Point | Vérification | Résultat |
|---|---|---|
| Fonctionnement des modèles de langage (prédiction du jeton suivant, pré-entraînement, ajustement, fenêtre de contexte, date de coupure) | Cohérence avec la littérature (Vaswani et al., 2017) et les descriptions usuelles | Conforme, vulgarisé sans simplification fautive |
| RAG : recherche de passages puis génération sourcée | Lewis et al. (2020) | Conforme |
| Hallucinations : définition et typologie | Ji et al. (2023) ; NIST AI 600-1 (« confabulation ») | Conforme |
| Injection de prompt et agents | OWASP Top 10 LLM 2025 | Conforme ; recommandations (moindre privilège, validation humaine) standard |
| RPA distinguée de l'IA | Définition usuelle | Conforme |
| Tests analytiques d'audit (module 13) | **Exécutés réellement** sur le fichier fictif `depenses_RCE_T1_2026.csv` avec `07_OUTILS/tests_audit.py` ; résultats reproduits dans le module (22 opérations signalées, détail par test) | Conforme et reproductible |
| Formules de tableur citées (SOMME.SI.ENS, RECHERCHEV, SOMMEPROD) | Noms de fonctions de tableurs en français | Conformes ; le texte rappelle de vérifier les noms selon la langue et le logiciel |

## Limites assumées

- Aucun prompt n'a été exécuté dans un outil d'IA pour produire les « exemples de résultats » : ils sont **rédigés à titre illustratif** et signalés comme tels, conformément au cahier des charges. Recommandation : avant publication, l'auteur peut tester chaque fiche (annexe 18) sur l'outil de son choix et remplacer les exemples par des sorties réelles, en indiquant l'outil, la version et la date.
- Aucune fonctionnalité ni aucun prix d'outil commercial nommé n'est affirmé ; les outils sont décrits par catégories.

## Pédagogie

- Structure en 18 rubriques présente dans chaque module (contrôle automatique : aucune alerte, voir `controles_automatiques.json`).
- 22 QCM × 10 questions = 220 questions, 4 propositions chacune, corrigé complet regroupé après les questions, barème /20 et niveaux de maîtrise.
- Répartition des bonnes réponses des questions à réponse unique rééquilibrée lors du contrôle (a 36, b 41, c 35, d 42) ; corrigés remappés et vérifiés par échantillonnage.
- 40 fiches prompts complètes (rubriques A à K), toutes contrôlées automatiquement.
- Progression : fondamentaux → diagnostic → fondations → métiers → déploiement → laboratoire ; exemples concrets avant les concepts.
