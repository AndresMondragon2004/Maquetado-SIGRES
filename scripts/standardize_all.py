import os
import re
import glob
from standardize_lib import (
    HEAD_CANONICAL,
    ROLE_CONFIGS,
    FOOTER_CANONICAL,
    get_floating_button,
    generate_header,
    generate_sidebar,
    generate_bottom_nav,
    replace_legacy_data
)

BASE_DIR = r"c:\Users\Pc\Downloads\Maquetado - Residencia\respaldo-pre-estandarizacion-2026-09-17\sigres-umb"

def process_role_file(role_key, filepath):
    filename = os.path.basename(filepath)
    role_cfg = ROLE_CONFIGS[role_key]

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Replace legacy names and colors
    content = replace_legacy_data(content)

    # 2. Standardize <head>
    head_match = re.search(r'<head>(.*?)</head>', content, flags=re.DOTALL | re.IGNORECASE)
    if head_match:
        # Extract title if present
        title_match = re.search(r'<title>(.*?)</title>', head_match.group(1), flags=re.IGNORECASE)
        title_str = title_match.group(1) if title_match else f"{role_cfg['screen_names'].get(filename, 'SIGRES-UMB')} — SIGRES-UMB"
        new_head = f"<head>\n  <meta charset=\"UTF-8\">\n  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n  <title>{title_str}</title>\n{HEAD_CANONICAL}\n</head>"
        content = content[:head_match.start()] + new_head + content[head_match.end():]

    # 3. Standardize Header
    new_header_html = generate_header(role_cfg, filename)
    header_match = re.search(r'<header.*?</header>', content, flags=re.DOTALL | re.IGNORECASE)
    if header_match:
        content = content[:header_match.start()] + new_header_html + content[header_match.end():]
    else:
        # Insert after <body ...>
        body_start = re.search(r'<body[^>]*>', content, flags=re.IGNORECASE)
        if body_start:
            insert_pos = body_start.end()
            content = content[:insert_pos] + "\n" + new_header_html + "\n" + content[insert_pos:]

    # 4. Standardize Desktop Sidebar
    new_sidebar_html = generate_sidebar(role_cfg, filename)
    aside_match = re.search(r'<aside.*?</aside>', content, flags=re.DOTALL | re.IGNORECASE)
    if aside_match:
        content = content[:aside_match.start()] + new_sidebar_html + content[aside_match.end():]
    else:
        # If no aside, look for main wrapper
        main_match = re.search(r'<main[^>]*>', content, flags=re.IGNORECASE)
        if main_match:
            insert_pos = main_match.start()
            content = content[:insert_pos] + new_sidebar_html + "\n" + content[insert_pos:]

    # Ensure main container has correct responsive margin for sidebar: lg:ml-[260px] or lg:pl-[260px]
    # Check if main or container has lg:ml-[260px] or lg:pl-[260px] or lg:ml-64
    content = re.sub(r'lg:ml-64', 'lg:ml-[260px]', content)
    content = re.sub(r'lg:pl-64', 'lg:pl-[260px]', content)

    # 5. Standardize Bottom Navigation
    new_bottom_nav_html = generate_bottom_nav(role_cfg, filename)
    # Check if bottom nav already exists: <nav class="lg:hidden ...>
    bottom_nav_match = re.search(r'<nav[^>]*lg:hidden[^>]*>.*?</nav>', content, flags=re.DOTALL | re.IGNORECASE)
    if bottom_nav_match:
        content = content[:bottom_nav_match.start()] + new_bottom_nav_html + content[bottom_nav_match.end():]
    else:
        # Insert before </body>
        body_end = re.search(r'</body>', content, flags=re.IGNORECASE)
        if body_end:
            insert_pos = body_end.start()
            content = content[:insert_pos] + "\n" + new_bottom_nav_html + "\n" + content[insert_pos:]

    # 6. Standardize Footer
    footer_match = re.search(r'<footer.*?</footer\s*>', content, flags=re.DOTALL | re.IGNORECASE)
    if footer_match:
        content = content[:footer_match.start()] + FOOTER_CANONICAL + content[footer_match.end():]
    else:
        # Insert before </main> or before bottom nav / body end
        main_end = re.search(r'</main\s*>', content, flags=re.IGNORECASE)
        if main_end:
            insert_pos = main_end.start()
            content = content[:insert_pos] + "\n" + FOOTER_CANONICAL + "\n" + content[insert_pos:]
        else:
            body_end = re.search(r'</body>', content, flags=re.IGNORECASE)
            if body_end:
                insert_pos = body_end.start()
                content = content[:insert_pos] + "\n" + FOOTER_CANONICAL + "\n" + content[insert_pos:]

    # 7. Add Floating Portal Button (if not already present)
    floating_btn = get_floating_button("../index.html")
    # Remove any existing floating button first
    content = re.sub(r'<!-- BOTÓN FLOTANTE AL PORTAL.*?-->\s*<aside.*?</aside>', '', content, flags=re.DOTALL)
    content = re.sub(r'<aside[^>]*aria-label="Navegación al portal[^>]*>.*?</aside>', '', content, flags=re.DOTALL)
    
    # Insert before </body>
    body_end = re.search(r'</body>', content, flags=re.IGNORECASE)
    if body_end:
        insert_pos = body_end.start()
        content = content[:insert_pos] + "\n" + floating_btn + "\n" + content[insert_pos:]

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Processed: {filepath}")

def process_auth_file(filepath):
    filename = os.path.basename(filepath)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    content = replace_legacy_data(content)

    head_match = re.search(r'<head>(.*?)</head>', content, flags=re.DOTALL | re.IGNORECASE)
    if head_match:
        title_match = re.search(r'<title>(.*?)</title>', head_match.group(1), flags=re.IGNORECASE)
        title_str = title_match.group(1) if title_match else "Autenticación — SIGRES-UMB"
        new_head = f"<head>\n  <meta charset=\"UTF-8\">\n  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n  <title>{title_str}</title>\n{HEAD_CANONICAL}\n</head>"
        content = content[:head_match.start()] + new_head + content[head_match.end():]

    floating_btn = get_floating_button("../index.html")
    content = re.sub(r'<!-- BOTÓN FLOTANTE AL PORTAL.*?-->\s*<aside.*?</aside>', '', content, flags=re.DOTALL)
    content = re.sub(r'<aside[^>]*aria-label="Navegación al portal[^>]*>.*?</aside>', '', content, flags=re.DOTALL)
    body_end = re.search(r'</body>', content, flags=re.IGNORECASE)
    if body_end:
        insert_pos = body_end.start()
        content = content[:insert_pos] + "\n" + floating_btn + "\n" + content[insert_pos:]

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Processed auth: {filepath}")

def process_transversal_file(filepath):
    filename = os.path.basename(filepath)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    content = replace_legacy_data(content)

    head_match = re.search(r'<head>(.*?)</head>', content, flags=re.DOTALL | re.IGNORECASE)
    if head_match:
        title_match = re.search(r'<title>(.*?)</title>', head_match.group(1), flags=re.IGNORECASE)
        title_str = title_match.group(1) if title_match else "Módulo Transversal — SIGRES-UMB"
        new_head = f"<head>\n  <meta charset=\"UTF-8\">\n  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n  <title>{title_str}</title>\n{HEAD_CANONICAL}\n</head>"
        content = content[:head_match.start()] + new_head + content[head_match.end():]

    floating_btn = get_floating_button("../index.html")
    content = re.sub(r'<!-- BOTÓN FLOTANTE AL PORTAL.*?-->\s*<aside.*?</aside>', '', content, flags=re.DOTALL)
    content = re.sub(r'<aside[^>]*aria-label="Navegación al portal[^>]*>.*?</aside>', '', content, flags=re.DOTALL)
    body_end = re.search(r'</body>', content, flags=re.IGNORECASE)
    if body_end:
        insert_pos = body_end.start()
        content = content[:insert_pos] + "\n" + floating_btn + "\n" + content[insert_pos:]

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Processed transversal: {filepath}")

def process_portal_file(filepath, is_root=False):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    content = replace_legacy_data(content)

    head_match = re.search(r'<head>(.*?)</head>', content, flags=re.DOTALL | re.IGNORECASE)
    if head_match:
        title_match = re.search(r'<title>(.*?)</title>', head_match.group(1), flags=re.IGNORECASE)
        title_str = title_match.group(1) if title_match else "Portal de Prototipos — SIGRES-UMB"
        new_head = f"<head>\n  <meta charset=\"UTF-8\">\n  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n  <title>{title_str}</title>\n{HEAD_CANONICAL}\n</head>"
        content = content[:head_match.start()] + new_head + content[head_match.end():]

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Processed portal: {filepath}")

def run_all():
    # 1. Portal
    process_portal_file(os.path.join(BASE_DIR, "index.html"), is_root=True)
    process_portal_file(os.path.join(BASE_DIR, "00-portal", "index.html"), is_root=False)

    # 2. Auth (01-autenticacion)
    for f in glob.glob(os.path.join(BASE_DIR, "01-autenticacion", "*.html")):
        process_auth_file(f)

    # 3. Roles (02 to 07)
    for role_key in ROLE_CONFIGS.keys():
        for f in glob.glob(os.path.join(BASE_DIR, role_key, "*.html")):
            process_role_file(role_key, f)

    # 4. Transversales (08)
    for f in glob.glob(os.path.join(BASE_DIR, "08-transversales", "*.html")):
        process_transversal_file(f)

if __name__ == "__main__":
    run_all()
