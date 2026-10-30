#!/usr/bin/env python3
"""Add (or refresh) the Updates button and screen in a LODESTAR / ORION / OTR dashboard page.
   python3 tools/add_updates_tab.py <page.html> --id otr|tactical|nova --version 1.1.0
Safe to run again: the old copy of the Updates block is replaced."""
import argparse, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
BTN = '\n    <button id="btnUpdates" type="button">Updates</button>'

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("page"); ap.add_argument("--id", required=True); ap.add_argument("--version", required=True)
    a = ap.parse_args()
    frag = open(os.path.join(HERE, "updates_tab.html"), encoding="utf-8").read().replace("__DASH_ID__", a.id).replace("__DASH_VERSION__", a.version)
    t = open(a.page, encoding="utf-8").read()
    t = re.sub(r"<!--UPDATES-TAB-BEGIN-->.*?<!--UPDATES-TAB-END-->\n?", "", t, flags=re.S)
    t = t.replace(BTN, "")
    m = re.search(r'<button id="btnTheme"[^>]*>[^<]*</button>', t)
    if not m: sys.exit("no Theme button found in " + a.page)
    t = t[:m.end()] + BTN + t[m.end():]
    i = t.rfind("</body>")                       # the real end of the page (a page may also mention </body> inside a script)
    if i < 0: sys.exit("no </body> in " + a.page)
    t = t[:i] + frag + t[i:]
    open(a.page, "w", encoding="utf-8").write(t)
    print("updates tab added to", a.page, "(id", a.id + ", version", a.version + ")")

if __name__ == "__main__":
    main()
