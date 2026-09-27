import os
import re
import glob

BASE_DIR = r"c:\Users\Pc\Downloads\Maquetado - Residencia\respaldo-pre-estandarizacion-2026-09-17\sigres-umb"

def clean_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Remove duplicate portal buttons
    # Old variant 1: <div class="fixed bottom-4 right-4 ... Portal SIGRES ... </div>
    content = re.sub(r'<!--\s*Botón flotante al portal\s*-->\s*<div[^>]*fixed[^>]*>.*?Portal SIGRES.*?</div>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<div[^>]*fixed bottom-4 right-4[^>]*>.*?Portal SIGRES.*?</div>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<div[^>]*fixed bottom-6 right-6[^>]*>.*?Portal SIGRES.*?</div>', '', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Old variant 2: duplicate <aside aria-label="Navegación al portal...
    portal_matches = list(re.finditer(r'<!-- BOTÓN FLOTANTE AL PORTAL.*?-->\s*<aside aria-label="Navegación al portal de prototipos".*?</aside>', content, flags=re.DOTALL))
    if len(portal_matches) > 1:
        # Keep only the last one
        for m in portal_matches[:-1]:
            content = content[:m.start()] + content[m.end():]

    # 2. Clean up stacked comments
    content = re.sub(r'<!-- APP BAR SUPERIOR FIJA.*?-->\s*<!-- APP BAR SUPERIOR CANÓNICA.*?-->', '<!-- APP BAR SUPERIOR CANÓNICA (64px) -->', content, flags=re.DOTALL)
    content = re.sub(r'<!-- SIDEBAR ESCRITORIO.*?-->\s*<!-- SIDEBAR ESCRITORIO.*?-->', '<!-- SIDEBAR ESCRITORIO (260px) -->', content, flags=re.DOTALL)
    content = re.sub(r'<!-- BARRA INFERIOR DE NAVEGACIÓN.*?-->\s*<!-- BOTTOM NAVIGATION MOBILE.*?-->', '<!-- BOTTOM NAVIGATION MOBILE (< 1024px) -->', content, flags=re.DOTALL)

    # 3. Clean up multiple consecutive footers
    footer_matches = list(re.finditer(r'<footer[^>]*>.*?</footer>', content, flags=re.DOTALL))
    if len(footer_matches) > 1:
        # If in role page, keep only the canonical one
        canonical_footer = """<footer class="pt-8 pb-4 text-center text-[12px] text-umb-outline space-y-1">
  <p>SIGRES-UMB — Sistema integral para la gestión de residencias profesionales</p>
  <p>Universidad Mexiquense del Bicentenario · UES San José del Rincón · Ciclo 26-27/1</p>
</footer>"""
        # Replace the first with canonical and delete others if they are duplicate institutional footers
        content = re.sub(r'(<footer class="pt-8 pb-4 text-center text-\[12px\] text-umb-outline space-y-1">.*?</footer>\s*){2,}', canonical_footer + '\n', content, flags=re.DOTALL)

    # 4. Clean up any remaining obsolete names
    content = content.replace("Valeria Reyes Montiel", "Jesús Andrés Mondragón Tenorio")
    content = content.replace("Valeria Reyes", "Jesús Andrés Mondragón")
    content = content.replace("TechSol Solutions México S.A. de C.V.", "Universidad Mexiquense del Bicentenario · Dirección Académica")
    content = content.replace("TechSol Solutions México", "Universidad Mexiquense del Bicentenario · Dirección Académica")
    content = content.replace("TechSol Solutions", "Universidad Mexiquense del Bicentenario")
    content = content.replace("TechSol", "UMB Académica")
    content = content.replace("Dra. Patricia Morales Velázquez", "Lic. Estefanía Yttesen Nava")
    content = content.replace("Dra. Patricia Morales", "Lic. Estefanía Yttesen")
    content = content.replace("Patricia Morales", "Estefanía Yttesen")
    content = content.replace("Ing. Roberto Almanza Torres", "I.S.C. Leonardo Becerril Sánchez")
    content = content.replace("Ing. Roberto Almanza", "I.S.C. Leonardo Becerril")
    content = content.replace("Roberto Almanza", "Leonardo Becerril")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

all_files = glob.glob(os.path.join(BASE_DIR, "**", "*.html"), recursive=True)
for f in all_files:
    clean_file(f)

print(f"Cleaned {len(all_files)} files successfully.")
