# -*- coding: utf-8 -*-
"""À exécuter avec le Python de LibreOffice (/usr/bin/python3 + module uno).
Ouvre le DOCX, met à jour le sommaire et les champs, exporte en PDF.
Usage : /usr/bin/python3 maj_toc_pdf.py ENTREE.docx SORTIE.pdf"""
import os, sys, time, subprocess, uno
from com.sun.star.beans import PropertyValue

def prop(n, v):
    p = PropertyValue(); p.Name = n; p.Value = v; return p

def main(src, dst):
    port = 2002
    proc = subprocess.Popen(["soffice", "--headless", "--invisible", "--nologo", "--norestore",
                             f"--accept=socket,host=127.0.0.1,port={port};urp;"],
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    local = uno.getComponentContext()
    resolver = local.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", local)
    ctx = None
    for _ in range(60):
        try:
            ctx = resolver.resolve(f"uno:socket,host=127.0.0.1,port={port};urp;StarOffice.ComponentContext"); break
        except Exception:
            time.sleep(1)
    if ctx is None: raise SystemExit("LibreOffice injoignable")
    desktop = ctx.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)
    url = uno.systemPathToFileUrl(os.path.abspath(src))
    doc = desktop.loadComponentFromURL(url, "_blank", 0, (prop("Hidden", True),))
    idx = doc.getDocumentIndexes()
    for i in range(idx.getCount()):
        idx.getByIndex(i).update()
    doc.getTextFields().refresh()
    # deuxième passe : la pagination du sommaire lui-même décale les numéros
    for i in range(idx.getCount()):
        idx.getByIndex(i).update()
    filt = (prop("FilterName", "writer_pdf_Export"),
            prop("FilterData", uno.Any("[]com.sun.star.beans.PropertyValue", tuple([
                prop("ExportBookmarks", True), prop("UseTaggedPDF", True),
                prop("ExportNotes", False), prop("Quality", 90), prop("ReduceImageResolution", True),
                prop("MaxImageResolution", 220)]))))
    doc.storeToURL(uno.systemPathToFileUrl(os.path.abspath(dst)), filt)
    doc.close(True)
    try: desktop.terminate()
    except Exception: pass
    proc.wait(timeout=60)
    print("PDF exporté :", dst)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
