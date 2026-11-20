#!/usr/bin/env python3
"""Supprime les tirets cadratins « — » du texte selon le contexte."""
import re, sys

LIAISON = ("et ", "mais ", "ou ", "souvent", "en particulier", "surtout", "sans ", "pas ", "notamment", "y compris",
           "voire", "parfois", "avec ", "auquel", "puis", "même", "ni ", "non ", "plutôt", "jamais", "y ", "c'est-à-dire")

def join_single(a, b):
    bl = b.lower()
    if any(bl.startswith(x) for x in LIAISON):
        return a + ', ' + b
    return a + ' : ' + b

def fix_prose(l):
    if ' — ' not in l:
        return l
    parts = l.split(' — ')
    n = len(parts) - 1
    out = parts[0]
    i = 1
    while i < len(parts):
        if i + 1 < len(parts) and (n - (i - 1)) >= 2:
            inner, after = parts[i], parts[i + 1]
            if ',' in inner or ' : ' in inner:
                out += ' (' + inner + ')' + ('' if after[:1] in '.,;:)' else ' ') + after
            else:
                out += ', ' + inner + ('' if after[:1] in '.,;:)' else ', ') + after
            i += 2
        else:
            out = join_single(out, parts[i])
            i += 1
    return out

def fix(text):
    res, code = [], False
    for l in text.split('\n'):
        if l.startswith('```'):
            code = not code; res.append(l); continue
        l = re.sub(r'^- \*\*([CADRE]) — ([^*]+)\*\* — ', r'- **\1 (\2)** : ', l)
        l = l.replace('(mise en situation — ', '(mise en situation, ')
        l = re.sub(r'^(\*\*[^*]+\*\*) — ', r'\1 : ', l)
        l = re.sub(r'^(> \*\*[^*]+\*\*) — ', r'\1 : ', l)
        if l.startswith('|'):
            l = re.sub(r'(?<=\|)(\s*)—(\s*)(?=\|)', r'\1Néant\2', l)
            l = l.replace(' — ', ' : ')
        elif code or l.startswith('#') or l.startswith('![') or l.startswith('- [Figure') or l.startswith('Table:'):
            l = l.replace(' — ', ' : ')
        else:
            l = fix_prose(l)
        res.append(l)
    return '\n'.join(res)

for f in sys.argv[1:]:
    s = open(f, encoding='utf-8').read()
    open(f, 'w', encoding='utf-8').write(fix(s))
