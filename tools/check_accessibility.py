"""Student Bites structural audit. Requires beautifulsoup4; not a WCAG/axe scan.
Run: python tools/check_accessibility.py from project root.
"""
from pathlib import Path
from bs4 import BeautifulSoup
import json,sys
root=Path(__file__).resolve().parent.parent
results=[]
for path in sorted(root.glob('*.html')):
    doc=BeautifulSoup(path.read_text(encoding='utf-8'),'html.parser')
    findings=[]
    if not doc.title or not doc.title.get_text(strip=True): findings.append('Missing title')
    if len(doc.select('h1'))!=1: findings.append('Expected exactly one H1')
    for landmark in ('header','nav','main','footer'):
        if not doc.select_one(landmark):findings.append('Missing '+landmark)
    for image in doc.select('img'):
        if not image.has_attr('alt'):findings.append('Image missing alt')
        if not all(image.has_attr(k) for k in ('width','height')):findings.append('Image lacks dimensions')
        if not (root/image.get('src','')).is_file():findings.append('Image source missing')
    for link in doc.select('a[href]'):
        if not link.get_text(' ',strip=True) and not link.select_one('img[alt]'):findings.append('Unnamed link')
        dest=link['href'].split('#')[0]
        if dest and not dest.startswith(('http:','https:','mailto:')) and not (root/dest).exists():findings.append('Missing local link '+dest)
        if link['href'].startswith('#') and not doc.find(id=link['href'][1:]):findings.append('Missing page anchor')
    for element in doc.select('details'):
        if not element.find('summary',recursive=False):findings.append('Details missing summary')
    results.append({'file':path.name,'findings':findings,'pass':not findings})
print(json.dumps(results,indent=2))
sys.exit(0 if all(x['pass'] for x in results) else 1)
