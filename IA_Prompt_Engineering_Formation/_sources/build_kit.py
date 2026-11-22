# -*- coding: utf-8 -*-
"""Kit bonus : « Le Kit IA du professionnel moderne » (PDF)."""
from docparts import *
from kitdata import *

doc = Doc("Le Kit IA du professionnel moderne")
B = []; br = '<div class="page-break"></div>'

def part_header(n, title, sub, ic):
    return (f'{doc.mark(f"Partie {n} — {title}", 1)}<div style="background:#{NAVY};border-radius:9pt;padding:16pt 18pt;color:#fff;display:flex;gap:14pt;align-items:center;margin-bottom:12pt;">'
            f'{badge(ic, TEAL, "FFFFFF", 52)}<div><div class="kicker">Partie {n}</div>'
            f'<div style="font-family:Montserrat;font-weight:800;font-size:19pt;line-height:1.15;margin-top:2pt;">{esc(title)}</div>'
            f'<div style="color:#C9D3E6;font-size:9.8pt;margin-top:4pt;">{esc(sub)}</div></div></div>')

def level(n):
    lab = {1: "Débutant", 2: "Intermédiaire", 3: "Avancé"}[n]
    dots = "".join(f'<span style="display:inline-block;width:7pt;height:7pt;border-radius:50%;margin-right:2pt;background:#{TEAL if i < n else "D5DBE5"}"></span>' for i in range(3))
    return f'{dots}<span class="small" style="margin-left:3pt;">{lab}</span>'

# ---------------------------------------------------------------- intro
B.append(section_title(doc, "Bienvenue dans votre kit", first=True, kicker="Mode d'emploi"))
B.append(P("Ce kit prolonge la formation <strong>« IA & Prompt Engineering appliqués aux entreprises »</strong>. Il a un seul objectif : vous faire <strong>passer à l'action</strong> dès demain.",
           "Vous y trouverez une sélection d'outils réellement utiles en contexte professionnel, plus de vingt prompts prêts à copier-coller, la fiche mémo de la méthode PILOTE, les dix réflexes du professionnel, un défi de sept jours pour ancrer de nouvelles habitudes et une fiche pour identifier vos propres usages."))
B.append('<div class="grid g3">' + "".join(
    f'<div class="card">{badge(ic, c, "FFFFFF", 30)}<h4>{esc(t)}</h4><p>{esc(d)}</p></div>' for ic, c, t, d in [
    ("briefcase", NAVY, "1. Les outils", "18 outils sélectionnés et vérifiés, classés par besoin."),
    ("message-square", TEAL, "2. Les prompts", "25 prompts professionnels avec variables à personnaliser."),
    ("compass", NAVY, "3. Le prompt universel", "La méthode PILOTE sur une fiche à garder sous les yeux."),
    ("list-checks", TEAL, "4. Les 10 réflexes", "Les règles simples d'un usage efficace et responsable."),
    ("flag", NAVY, "5. Le défi 7 jours", "Un exercice de 10 à 15 minutes par jour."),
    ("lightbulb", TEAL, "6. Ma boîte à idées", "Pour repérer vos tâches à confier à l'IA.")]) + '</div>')
B.append(box("tip", P("Ne lisez pas ce kit d'une traite. Commencez par la Partie 3 (le prompt universel), lancez le défi de la Partie 5, et revenez aux outils et aux prompts au fil de vos besoins.")))
B.append(box("warn", P("Avant d'utiliser un outil avec des données de votre entreprise, vérifiez qu'il est autorisé par votre organisation et appliquez le <strong>feu tricolore des données</strong> : rien de confidentiel dans un outil non validé."), "Avant de commencer"))

# ---------------------------------------------------------------- Partie 1
B.append(br + part_header(1, "Les outils incontournables", "Une sélection pertinente, expliquée et exploitable, organisée par besoin.", "briefcase"))
B.append(P("Inutile de tout tester : <strong>un assistant généraliste bien maîtrisé couvre 80 % des besoins</strong>. Les outils spécialisés viennent ensuite, quand un besoin précis se présente (présentation, réunion, automatisation…)."))
B.append("<h3>Quel outil pour quel besoin ?</h3>" + table(["Mon besoin", "Outils conseillés"], [[f"<b>{esc(a)}</b>", esc(b)] for a, b in TOOL_MAP], ["38%", "62%"]))
B.append(box("ex", P(esc(PRICING_NOTE)), f"Tarifs vérifiés en {VERIF_DATE}"))
for i, t in enumerate(TOOLS):
    if i % 2 == 0: B.append(br)
    B.append(f'''<div class="avoid" style="border:1pt solid #DCE2EB;border-radius:9pt;overflow:hidden;margin-bottom:12pt;">
  <div style="background:#{LIGHT};padding:10pt 13pt;display:flex;gap:11pt;align-items:center;border-bottom:1pt solid #DCE2EB;">
    {badge(t["icon"], TEAL if i % 2 == 0 else NAVY, "FFFFFF", 38)}
    <div style="flex:1"><div style="font-family:Montserrat;font-weight:800;font-size:14pt;color:#{NAVY};line-height:1.1;">{esc(t["name"])}</div>
      <div class="small">{esc(t["editor"])} · <span style="color:#{TEAL};font-weight:600;">{esc(t["cat"])}</span></div></div>
    <div style="text-align:right">{level(t["level"])}</div></div>
  <div style="padding:9pt 13pt 10pt 13pt;font-size:8.8pt;">
    <p style="margin:0 0 6pt 0;"><b>Fonction principale :</b> {esc(t["func"])}</p>
    <div class="grid g2" style="margin:0;gap:10pt;">
      <div><div class="kicker" style="color:#{TEAL}">Ce qu'il peut faire</div>{UL([esc(c) for c in t["can"]])}
        <div class="kicker" style="color:#{TEAL}">Exemple professionnel</div><p>{esc(t["example"])}</p></div>
      <div><div class="kicker" style="color:#{TEAL}">Pourquoi vous en avez besoin</div><p>{esc(t["why"])}</p>
        <div class="kicker" style="color:#{TEAL}">Tarification ({VERIF_DATE})</div><p>{esc(t["price"])}</p>
        <div class="kicker" style="color:#{TEAL}">Lien officiel</div><p><a href="{t["url"]}" style="color:#{NAVY};font-weight:600;">{esc(t["url"])}</a></p></div></div>
    <div style="background:#FBF5E6;border-left:3pt solid #{GOLD};border-radius:4pt;padding:6pt 9pt;margin-top:3pt;">{icon("lightbulb", GOLD, 12)} <b style="color:#9C7C2C">Pour bien commencer :</b> {esc(t["tip"])}</div>
  </div></div>''')

# ---------------------------------------------------------------- Partie 2
B.append(br + part_header(2, "La bibliothèque de prompts", "25 prompts professionnels prêts à copier, organisés par besoin.", "message-square"))
B.append(P("Chaque prompt suit la méthode PILOTE. Remplacez les éléments entre <strong>[CROCHETS]</strong> par vos informations, supprimez ce qui ne sert pas, et n'oubliez pas de relancer l'IA pour affiner le résultat."))
B.append(table(["Catégorie", "Prompts"], [[f"<b>{esc(g)}</b>", ", ".join(esc(i["name"]) for i in items)] for g, ic, items in PROMPT_GROUPS], ["28%", "72%"]))
B.append(box("warn", P("Ne collez jamais de données sensibles dans un prompt : remplacez noms, coordonnées et montants confidentiels par des marqueurs neutres ([CLIENT A], [MONTANT]).")))
k = 0
for g, ic, items in PROMPT_GROUPS:
    B.append(br + f'{doc.mark(g, 2)}<div style="display:flex;align-items:center;gap:9pt;margin-bottom:6pt;">{badge(ic, TEAL, "FFFFFF", 30)}<h2 class="first" style="border:none;padding:0;margin:0;">{esc(g)}</h2></div>')
    for it in items:
        k += 1
        B.append(f'''<div class="avoid" style="margin:10pt 0 12pt 0;">
  <div style="display:flex;align-items:center;gap:8pt;"><span class="qn" style="background:#{GOLD};color:#{NAVY};font-family:Montserrat;font-weight:800;">{k}</span>
  <h3 style="margin:0">{esc(it["name"])}</h3></div>
  <div class="grid g2" style="margin:5pt 0 0 0;gap:8pt;font-size:8.7pt;">
   <div><b style="color:#{RED}">Le problème :</b> {esc(it["problem"])}</div><div><b style="color:#{TEAL}">Quand l'utiliser :</b> {esc(it["when"])}</div></div>
  {prompt(it["prompt"], "Prompt à copier")}
  <div class="grid g2" style="margin:0;gap:8pt;font-size:8.7pt;">
   <div><b>À personnaliser :</b> {esc(it["vars"])}</div><div><b>Résultat attendu :</b> {esc(it["result"])}</div></div></div>''')

# ---------------------------------------------------------------- Partie 3
B.append(br + part_header(3, "Le prompt universel", "La méthode PILOTE sur une fiche : à imprimer et garder près de votre écran.", "compass"))
B.append(pilote_cards())
B.append(prompt(PILOTE_TEMPLATE, "Le prompt universel — à copier"))
B.append("<h3>Les 5 relances magiques</h3>" + table(["Pour…", "Dites…"], [[f"<b>{esc(t)}</b>", f"<i>{esc(q)}</i>"] for t, q in ITERATIONS], ["28%", "72%"]))
B.append(box("key", P("Demander → Observer → Préciser. Puis vérifier : <strong>Vrai ? Juste ? Signable ?</strong>")))

# ---------------------------------------------------------------- Partie 4
B.append(br + part_header(4, "Les 10 réflexes du professionnel qui utilise l'IA", "Des règles simples, mémorables et directement applicables.", "list-checks"))
B.append('<div class="grid g2">' + "".join(
    f'<div class="card" style="display:flex;gap:10pt;align-items:flex-start;"><span class="qn" style="width:28pt;height:28pt;font-size:11pt;font-family:Montserrat;font-weight:800;background:#{NAVY if i % 2 == 0 else TEAL}">{i+1}</span>'
    f'<div><h4 style="margin:0 0 3pt 0;">{esc(t)}</h4><p>{esc(d)}</p></div></div>' for i, (t, d) in enumerate(REFLEXES)) + '</div>')
B.append("<h3>Le feu tricolore des données</h3>")
B.append('<div class="grid g3">' + "".join(f'<div class="card" style="border-top:4pt solid #{c}"><div class="kicker" style="color:#{c if c != ORANGE else "B5761A"};font-size:7pt;">{esc(t)}</div>{UL([esc(e) for e in ex])}</div>' for t, c, ex in TRAFFIC) + '</div>')
# ---------------------------------------------------------------- Partie 5
B.append(br + part_header(5, "Le défi IA de 7 jours", "Un exercice court par jour pour transformer la formation en habitude.", "flag"))
B.append(P("Chaque jour, consacrez <strong>10 à 15 minutes</strong> à une tâche réelle de votre travail. Le défi est progressif : on commence simple, on finit par construire sa propre bibliothèque de prompts. Cochez chaque journée terminée. Au bout de sept jours, vous aurez pratiqué toutes les compétences de la formation ; continuez ensuite avec <strong>un nouvel usage par semaine</strong>."))
B.append(table(["Jour", "Thème", "Fait", "Mon ressenti (1 à 5)"], [[f"<b>J{c['day']}</b>", esc(c["title"]), "☐", ""] for c in CHALLENGE], ["10%", "50%", "10%", "30%"]))
for c in CHALLENGE:
    if c["day"] in (2, 5): B.append(br)
    B.append(f'''<div class="avoid" style="border:1pt solid #DCE2EB;border-radius:9pt;overflow:hidden;margin:10pt 0;">
  <div style="background:#{NAVY};color:#fff;padding:8pt 13pt;display:flex;align-items:center;gap:11pt;">
   <div style="font-family:Montserrat;font-weight:800;font-size:20pt;color:#{GOLD};line-height:1;">J{c["day"]}</div>
   <div><div style="font-family:Montserrat;font-weight:700;font-size:12pt;">{esc(c["title"])}</div><div style="color:#C9D3E6;font-size:8.6pt;">Objectif : {esc(c["obj"])}</div></div></div>
  <div style="padding:8pt 13pt;font-size:8.8pt;">
   <p><b>Votre tâche :</b> {esc(c["task"])}</p>
   <p><b>Outil suggéré :</b> {esc(c["tool"])}</p>
   {prompt(c["prompt"], "Le prompt du jour")}
   <div class="grid g2" style="margin:0;gap:10pt;"><div><b style="color:#{TEAL}">Résultat à obtenir :</b> {esc(c["result"])}</div>
   <div><b style="color:#9C7C2C">Ma réflexion :</b> {esc(c["reflect"])}<div class="write"></div></div></div></div></div>''')
# ---------------------------------------------------------------- Partie 6
B.append(br + part_header(6, "Ma boîte à idées IA", "Identifiez les tâches de votre quotidien que l'IA peut transformer.", "lightbulb"))
B.append(P("Prenez 10 minutes au calme. Pour chaque catégorie, notez deux ou trois tâches concrètes de votre travail."))
cats = [("repeat", "Les tâches répétitives", "Ce que je refais chaque semaine de la même façon"),
        ("hourglass", "Les tâches qui me prennent trop de temps", "Ce qui me prend plus de temps que cela ne le mérite"),
        ("pen-tool", "Les tâches difficiles à rédiger", "Ce que je repousse parce que je ne sais pas comment l'écrire"),
        ("search", "Les tâches qui demandent des recherches", "Ce qui m'oblige à chercher, lire, comparer"),
        ("wand-sparkles", "Les tâches que j'aimerais simplifier", "Ce qui m'agace, me fatigue ou me freine")]
for ic, t, d in cats:
    B.append(f'<div class="card avoid" style="margin:7pt 0;"><div style="display:flex;gap:9pt;align-items:center;">{badge(ic, TEAL, "FFFFFF", 26)}<div><h4 style="margin:0">{esc(t)}</h4><div class="small">{esc(d)}</div></div></div>'
             + '<div class="write"></div></div>')
B.append('<div class="avoid" style="border:2pt solid #' + GOLD + ';border-radius:9pt;padding:11pt 14pt;margin-top:10pt;">'
         f'<h3 style="margin-top:0">{icon("target", GOLD, 17)} Ma tâche à expérimenter cette semaine</h3>'
         + "".join(f'<div style="display:flex;gap:8pt;align-items:flex-end;margin-top:6pt;"><span class="small" style="width:52mm;flex:none;">{lab}</span><div class="write" style="flex:1"></div></div>'
                   for lab in ["La tâche choisie", "Pourquoi celle-ci ?", "Ce que je fournis à l'IA (contexte)", "Le livrable attendu", "Données à anonymiser", "Mon prompt PILOTE (brouillon)", "Résultat et temps gagné"]) + '</div>')

# ---------------------------------------------------------------- sources
B.append(br + section_title(doc, "Sources et mise à jour", first=True, kicker="Transparence"))
B.append(P(f"Les informations sur les outils (fonctionnalités, offres, tarifs) ont été vérifiées en <strong>{VERIF_DATE}</strong> à partir des pages officielles des éditeurs et recoupées avec des comparatifs récents. "
           "Lorsque les sources divergeaient, nous avons retenu la formulation la plus prudente. Les offres d'IA changent fréquemment : nouvelles fonctionnalités, nouveaux noms, nouveaux prix. Avant toute souscription, consultez la page officielle."))
B.append(table(["Outil", "Site officiel"], [[esc(t["name"]), f'<a href="{t["url"]}" style="color:#{NAVY}">{esc(t["url"])}</a>'] for t in TOOLS], ["35%", "65%"]))
B.append(P('<span class="small">Les noms de produits cités appartiennent à leurs propriétaires respectifs. Ce kit est un document pédagogique indépendant, sans lien commercial avec les éditeurs mentionnés.</span>'))

def body(toc): return '<h2 class="first">Sommaire</h2>' + toc + br + "".join(B)
cov = cover("Bonus · Kit pratique", 'Le Kit IA <span style="color:#' + GOLD + '">du professionnel moderne</span>',
            "Outils, prompts, méthodes et défis pratiques pour transformer votre quotidien professionnel.",
            [("briefcase", "18 outils sélectionnés et vérifiés"), ("message-square", "25 prompts prêts à l'emploi"), ("compass", "Le prompt universel PILOTE"), ("flag", "Le défi IA de 7 jours")], ic="briefcase")
build(doc, cov, body, os.path.join(HERE, "..", "03_Bonus", "Kit_IA_Professionnel.pdf"), "KIT IA DU PROFESSIONNEL MODERNE")
