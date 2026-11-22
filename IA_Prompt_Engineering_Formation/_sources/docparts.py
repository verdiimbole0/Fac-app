# -*- coding: utf-8 -*-
"""Blocs HTML partagés par le syllabus, le kit et le guide du formateur."""
from pdfkit import *
from content import *

def P(*paras): return "".join(f"<p>{p}</p>" for p in paras)
def UL(items, cls=""): return f'<ul class="{cls}">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"
def OL(items): return "<ol>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"

BOX_META = {"key": ("À retenir", "badge-check"), "warn": ("Erreur à éviter", "triangle-alert"), "tip": ("Conseil du formateur", "lightbulb"),
            "ex": ("Exemple concret", "briefcase"), "ask": ("À vous de jouer", "notebook-pen")}
BOX_COL = {"key": TEAL, "warn": RED, "tip": "9C7C2C", "ex": NAVY, "ask": TEAL}
def box(kind, inner, title=None):
    t, ic = BOX_META[kind]
    return f'<div class="box {kind}"><div class="bt">{icon(ic, BOX_COL[kind], 13)}{esc(title or t)}</div>{inner}</div>'

def prompt(text, label="Prompt"):
    return f'<div class="prompt"><span class="pl">{esc(label)}</span>{esc(text)}</div>'
def answer(text, label="Réponse de l'IA (exemple)"):
    return f'<div class="answer"><span class="pl">{esc(label)}</span>{esc(text)}</div>'

def table(headers, rows, widths=None):
    cg = "".join(f'<col style="width:{w}">' for w in widths) if widths else ""
    th = "".join(f"<th>{h}</th>" for h in headers)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="tbl"><colgroup>{cg}</colgroup><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>'

def cover(doc_type, title_html, subtitle, bullets, ic="sparkles", edition=f"Édition {VERIF_DATE}"):
    bl = "".join(f'<div style="display:flex;align-items:center;gap:9pt;margin:7pt 0;">{icon(i, GOLD, 16)}<span style="font-size:10.5pt;color:#fff;">{esc(t)}</span></div>' for i, t in bullets)
    return f"""<div class="full navy">
  <div style="position:absolute;left:0;top:0;width:7mm;height:100%;background:#{GOLD}"></div>
  <div style="position:absolute;right:-60mm;top:20mm;width:170mm;height:170mm;border-radius:50%;background:#{NAVY2}"></div>
  <div style="position:absolute;right:-35mm;top:45mm;width:120mm;height:120mm;border-radius:50%;background:#17366A"></div>
  <div style="position:absolute;right:-10mm;top:70mm;width:70mm;height:70mm;border-radius:50%;background:#1D4278"></div>
  <div style="position:absolute;right:13mm;top:93mm;">{badge(ic, TEAL, 'FFFFFF', 92, 46)}</div>
  <div style="position:absolute;left:24mm;top:26mm;right:24mm;">
    <div class="kicker" style="font-size:9pt;">{esc(doc_type)}</div>
    <div style="margin-top:46mm;font-family:Montserrat;font-weight:800;font-size:31pt;line-height:1.12;color:#fff;max-width:118mm;">{title_html}</div>
    <div style="width:30mm;height:1.6mm;background:#{GOLD};margin:9mm 0 7mm 0;"></div>
    <div style="font-size:12.5pt;line-height:1.5;color:#C9D3E6;max-width:112mm;">{esc(subtitle)}</div>
  </div>
  <div style="position:absolute;left:24mm;bottom:40mm;">{bl}</div>
  <div style="position:absolute;left:24mm;bottom:16mm;right:24mm;display:flex;justify-content:space-between;font-family:Montserrat;font-size:8pt;font-weight:600;color:#8EA0C2;letter-spacing:.8pt;">
    <span>IA &amp; PROMPT ENGINEERING APPLIQUÉS AUX ENTREPRISES</span><span>{esc(edition.upper())}</span></div>
</div>"""

def chapter_opener(doc, ch, minutes, sections):
    sec = "".join(f'<div style="display:flex;gap:8pt;margin:4.5pt 0;color:#fff;font-size:10pt;">{icon("arrow-right", TEAL, 14)}<span>{esc(s)}</span></div>' for s in sections)
    return f"""<div class="full navy">{doc.mark(f"Chapitre {ch['n']} — {ch['title']}", 1)}
  <div style="position:absolute;left:0;top:0;width:100%;height:3mm;background:#{GOLD}"></div>
  <div style="position:absolute;right:-45mm;top:30mm;width:140mm;height:140mm;border-radius:50%;background:#{NAVY2}"></div>
  <div style="position:absolute;right:20mm;top:72mm;">{badge(ch['icon'], TEAL, 'FFFFFF', 120, 60)}</div>
  <div style="position:absolute;left:22mm;top:30mm;right:22mm;">
    <div style="font-family:Montserrat;font-weight:800;font-size:92pt;line-height:1;color:#{GOLD};">0{ch['n']}</div>
    <div class="kicker" style="font-size:9.5pt;margin-top:8mm;">Chapitre {ch['n']} · {minutes} minutes en session</div>
    <div style="font-family:Montserrat;font-weight:700;font-size:25pt;line-height:1.15;color:#fff;margin-top:4mm;max-width:115mm;">{esc(ch['title'])}</div>
    <div style="width:22mm;height:1.3mm;background:#{GOLD};margin:8mm 0 6mm 0;"></div>
    <div style="font-size:11pt;color:#C9D3E6;max-width:112mm;line-height:1.55;"><b style="color:#{GOLD}">Objectif — </b>{esc(ch['objective'])}</div>
  </div>
  <div style="position:absolute;left:22mm;right:22mm;bottom:22mm;">
    <div class="kicker" style="margin-bottom:5pt;">Dans ce chapitre</div>{sec}
    <div style="margin-top:9mm;background:#{TEAL};border-radius:7pt;padding:11pt 14pt;color:#fff;font-family:Montserrat;font-weight:600;font-size:10.5pt;line-height:1.45;">{icon('key-round','FFFFFF',15)} &nbsp;Message clé : {esc(ch['message'])}</div>
  </div>
</div>"""

def quiz_html(n, with_marker_doc=None):
    q = QUIZZES[n]
    out = []
    if with_marker_doc: out.append(with_marker_doc.mark(f"Quiz du chapitre {n}", 2))
    out.append(f'<h2>Quiz du chapitre {n}</h2><p class="lead">{esc(q["thanks"])}</p>')
    for i, it in enumerate(q["questions"]):
        opts = "".join(f'<div class="opt"><span class="ol">{"ABCD"[j]}</span><span>{esc(o)}</span></div>' for j, o in enumerate(it["options"]))
        out.append(f'<div class="quiz-q"><div class="qt"><span class="qn">Q{i+1}</span><span>{esc(it["q"])}</span></div>{opts}</div>')
    return "".join(out)

def corr_html(n, with_marker_doc=None):
    q = QUIZZES[n]; out = []
    if with_marker_doc: out.append(with_marker_doc.mark(f"Corrigé du quiz {n}", 2))
    out.append(f'<h2>Corrigé du quiz {n}</h2>')
    for i, it in enumerate(q["questions"]):
        L = "ABCD"[it["answer"]]
        wrong = [f"<b>{'ABCD'[j]}</b> : {esc(o)}" for j, o in enumerate(it["options"]) if j != it["answer"]]
        out.append(f'<div class="corr"><div class="small" style="font-family:Montserrat;font-weight:700;">QUESTION {i+1} — {esc(it["q"])}</div>'
                   f'<div class="good">Bonne réponse : {L} — {esc(it["options"][it["answer"]])}</div>'
                   f'<p style="margin:3pt 0;"><b>Pourquoi ?</b> {esc(it["why"])}</p>'
                   f'<p class="small" style="margin:3pt 0;">Les autres propositions sont écartées : ' + " ; ".join(wrong) + '.</p>'
                   f'<p style="margin:3pt 0;color:#9C7C2C;font-weight:600;">{icon("lightbulb", GOLD, 12)} Astuce mémo : {esc(it["tip"])}</p></div>')
    return "".join(out)

def pilote_cards():
    cards = "".join(f'<div class="card" style="background:#{NAVY if i%2==0 else NAVY2};color:#fff;text-align:center;padding:10pt 6pt;">'
                    f'<div style="font-family:Montserrat;font-weight:800;font-size:28pt;color:#{GOLD};line-height:1;">{L}</div>'
                    f'<div style="font-family:Montserrat;font-weight:700;font-size:9.5pt;margin:4pt 0 3pt 0;">{w}</div>'
                    f'<div style="font-size:7.8pt;color:#C9D3E6;line-height:1.35;">{esc(d)}</div></div>'
                    for i, (L, w, d, ex, ic) in enumerate(PILOTE))
    return f'<div class="grid" style="grid-template-columns:repeat(6,1fr);gap:5pt;">{cards}</div>'

def section_title(doc, title, level=1, first=False, kicker=None):
    k = f'<div class="kicker" style="margin-bottom:3pt;">{esc(kicker)}</div>' if kicker else ""
    return f'{doc.mark(title, level)}{k}<h2 class="{"first" if first else ""}">{esc(title)}</h2>'
