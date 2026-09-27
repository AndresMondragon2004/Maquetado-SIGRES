import os
import re
import glob

BASE_DIR = r"c:\Users\Pc\Downloads\Maquetado - Residencia\respaldo-pre-estandarizacion-2026-09-17\sigres-umb"
ROLE_DIRS = ['02-estudiante', '03-asesor-interno', '04-asesor-externo', '05-control-escolar', '06-coordinacion', '07-direccion']

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix VR initials -> JM
    # Match >VR< with optional whitespace
    content = re.sub(r'>\s*VR\s*<', '>JM<', content)
    # Match text or aria labels containing VR
    content = content.replace("Valeria Reyes Montiel", "Jesús Andrés Mondragón Tenorio")
    content = content.replace("Valeria Reyes", "Jesús Andrés Mondragón")
    content = content.replace("Valeria", "Jesús Andrés")

    # 2. Fix layout: ensure <main> has lg:ml-[260px] and min-w-0
    main_match = re.search(r'<main([^>]*)>', content, flags=re.IGNORECASE)
    if main_match:
        attrs = main_match.group(1)
        # Check class attribute
        class_match = re.search(r'class="([^"]*)"', attrs)
        if class_match:
            classes = class_match.group(1).split()
            
            # Remove any bad margins
            classes = [c for c in classes if c not in ['ml-64', 'md:ml-64', 'md:ml-[260px]', 'md:pl-64', 'pl-64', 'lg:pl-64', 'ml-[260px]', 'lg:pl-[260px]']]
            
            # Ensure lg:ml-[260px] and min-w-0 and flex-1
            if 'lg:ml-[260px]' not in classes:
                classes.insert(0, 'lg:ml-[260px]')
            if 'min-w-0' not in classes:
                classes.append('min-w-0')
            if 'flex-1' not in classes:
                classes.insert(0, 'flex-1')
            
            # Ensure pb-24 lg:pb-8 is present so bottom nav does not block footer
            if not any(c.startswith('pb-') for c in classes):
                classes.append('pb-24 lg:pb-8')
            
            new_attrs = re.sub(r'class="[^"]*"', f'class="{" ".join(classes)}"', attrs)
            content = content[:main_match.start()] + f'<main{new_attrs}>' + content[main_match.end():]

    # 3. Ensure wrapper container below header has pt-16
    # If there is a <div class="... flex ..."> right after </header>
    content = re.sub(r'(</header>\s*<div class=")([^"]*flex[^"]*)(")', lambda m: m.group(1) + ('pt-16 ' if 'pt-16' not in m.group(2) else '') + m.group(2).replace('pt-16 pt-16', 'pt-16') + m.group(3), content, count=1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for r in ROLE_DIRS:
    for f in glob.glob(os.path.join(BASE_DIR, r, '*.html')):
        fix_file(f)

# Also fix transversal files
for f in glob.glob(os.path.join(BASE_DIR, '08-transversales', '*.html')):
    fix_file(f)

print("Layout and personas fixed across all role and transversal files.")
