import os
import re
import glob

base_dir = r"c:\Users\Pc\Downloads\Maquetado - Residencia\respaldo-pre-estandarizacion-2026-09-17\sigres-umb"
role_dirs = ['02-estudiante', '03-asesor-interno', '04-asesor-externo', '05-control-escolar', '06-coordinacion', '07-direccion']

fixed_files = []

for r in role_dirs:
    for fpath in glob.glob(os.path.join(base_dir, r, "*.html")):
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        rel = os.path.relpath(fpath, base_dir)
        header_end = content.find("</header>")
        if header_end == -1:
            continue

        after_header = content[header_end:]
        # Find the first opening div after header
        div_match = re.search(r'(</header>\s*(?:<!--.*?-->\s*)*<div\s+class=")([^"]*)(")', content, flags=re.DOTALL | re.IGNORECASE)
        if div_match:
            classes = div_match.group(2)
            if "pt-16" not in classes and "pt-20" not in classes:
                new_classes = "pt-16 " + classes.strip()
                content = content[:div_match.start(2)] + new_classes + content[div_match.end(2):]
                fixed_files.append((rel, classes, new_classes))
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(content)
        else:
            # If no div right after header, check if <main> is directly there
            main_match = re.search(r'(</header>\s*(?:<!--.*?-->\s*)*<main\s+class=")([^"]*)(")', content, flags=re.DOTALL | re.IGNORECASE)
            if main_match:
                classes = main_match.group(2)
                if "pt-16" not in classes and "pt-20" not in classes:
                    new_classes = "pt-20 " + classes.strip()
                    content = content[:main_match.start(2)] + new_classes + content[main_match.end(2):]
                    fixed_files.append((rel, classes, new_classes))
                    with open(fpath, "w", encoding="utf-8") as f:
                        f.write(content)

print(f"Fixed {len(fixed_files)} files:")
for rel, old_c, new_c in fixed_files:
    print(f" - {rel}: '{old_c}' -> '{new_c}'")
