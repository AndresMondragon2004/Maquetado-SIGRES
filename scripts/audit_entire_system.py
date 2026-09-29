import os
import re
from urllib.parse import urlparse

BASE_DIR = 'sigres-umb'
HTML_FILES = []

for root, dirs, files in os.walk(BASE_DIR):
    for f in files:
        if f.endswith('.html'):
            HTML_FILES.append(os.path.normpath(os.path.join(root, f)))

print(f"Total HTML files found: {len(HTML_FILES)}")

issues = []

# 1. Check broken links and images
for fpath in HTML_FILES:
    dir_path = os.path.dirname(fpath)
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Check <a href="...">
    links = re.findall(r'<a\s+[^>]*href=["\']([^"\']+)["\']', content, re.IGNORECASE)
    for link in links:
        if link.startswith('#') or link.startswith('mailto:') or link.startswith('tel:') or link.startswith('javascript:'):
            continue
        if link.startswith('http://') or link.startswith('https://'):
            continue
        
        # Resolve local relative link
        link_clean = link.split('#')[0].split('?')[0]
        if not link_clean:
            continue
        target_path = os.path.normpath(os.path.join(dir_path, link_clean))
        if not os.path.exists(target_path):
            issues.append({
                "file": fpath,
                "type": "BROKEN_LINK",
                "detail": f"Link target '{link}' does not exist (resolved: {target_path})"
            })

    # Check <img src="...">
    images = re.findall(r'<img\s+[^>]*src=["\']([^"\']+)["\']', content, re.IGNORECASE)
    for img in images:
        if img.startswith('data:') or img.startswith('http://') or img.startswith('https://'):
            continue
        img_clean = img.split('#')[0].split('?')[0]
        if not img_clean:
            continue
        target_img = os.path.normpath(os.path.join(dir_path, img_clean))
        if not os.path.exists(target_img):
            issues.append({
                "file": fpath,
                "type": "BROKEN_IMAGE",
                "detail": f"Image source '{img}' does not exist (resolved: {target_img})"
            })

    # Check for remaining placeholder / unwanted text like e.firma in non-appropriate files
    if '06-coordinacion' in fpath:
        if re.search(r'e\.firma|efirma', content, re.IGNORECASE):
            issues.append({
                "file": fpath,
                "type": "COORDINACION_EFIRMA_LEFTOVER",
                "detail": "Found e.Firma mention in Coordinación module"
            })

    # Check for placeholder Juan Ramírez in roles other than generic
    if '05-control-escolar' in fpath:
        # Check avatar initials in header / profile
        if 'JR' in content and 'Juan Ramírez' in content:
            issues.append({
                "file": fpath,
                "type": "WRONG_PERSONA_AVATAR",
                "detail": "Found 'JR' / 'Juan Ramírez' instead of 'EY' / 'Lic. Estefanía Yttesen' in Control Escolar"
            })

    # Check for generic logo / assets link
    if 'src="logo_umb.png"' in content:
        issues.append({
            "file": fpath,
            "type": "BAD_ASSET_PATH",
            "detail": "Found un-prefixed logo_umb.png"
        })

print(f"\n--- AUDIT RESULTS ({len(issues)} potential issues found) ---")
for idx, iss in enumerate(issues, 1):
    print(f"{idx}. [{iss['type']}] in {iss['file']}:\n   -> {iss['detail']}")

if not issues:
    print("ALL CLEAN! No broken links, broken images, or known discrepancies found.")
