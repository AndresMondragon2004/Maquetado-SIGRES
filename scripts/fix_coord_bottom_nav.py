import os
import re

coordinacion_dir = 'sigres-umb/06-coordinacion'
files = {
    '01-dashboard-monitoreo.html': '01-dashboard-monitoreo.html',
    '02-cohortes-carreras.html': '02-cohortes-carreras.html',
    '03-supervision-riesgo.html': '03-supervision-riesgo.html',
    '04-contingencias.html': '04-contingencias.html',
    '06-reportes-ejecutivos.html': '06-reportes-ejecutivos.html',
    '07-notificaciones.html': '07-notificaciones.html',
    '08-mi-perfil.html': '08-mi-perfil.html'
}

def get_bottom_nav(current_file):
    items = [
        {"file": "01-dashboard-monitoreo.html", "icon": "monitoring", "label": "Monitoreo"},
        {"file": "03-supervision-riesgo.html", "icon": "warning", "label": "Riesgos"},
        {"file": "04-contingencias.html", "icon": "support", "label": "Contingencias"},
        {"file": "06-reportes-ejecutivos.html", "icon": "summarize", "label": "Reportes"},
        {"file": "08-mi-perfil.html", "icon": "person", "label": "Perfil"}
    ]
    
    html = ['  <!-- BOTTOM NAVIGATION MOBILE (< 1024px) -->']
    html.append('  <nav class="lg:hidden fixed bottom-0 left-0 right-0 h-16 bg-white border-t border-umb-border shadow-lg z-40 flex items-center justify-around px-2" aria-label="Navegación inferior móvil">')
    
    for it in items:
        is_active = (current_file == it['file'])
        if is_active:
            html.append(f'    <a href="{it["file"]}" class="flex flex-col items-center justify-center flex-1 py-1 text-umb-guinda" aria-current="page">')
            html.append(f'      <span class="material-symbols-outlined text-[22px] fill">{it["icon"]}</span>')
            html.append(f'      <span class="text-[11px] font-semibold mt-0.5">{it["label"]}</span>')
            html.append('    </a>')
        else:
            html.append(f'    <a href="{it["file"]}" class="flex flex-col items-center justify-center flex-1 py-1 text-umb-outline hover:text-umb-carbon">')
            html.append(f'      <span class="material-symbols-outlined text-[22px]">{it["icon"]}</span>')
            html.append(f'      <span class="text-[11px] font-medium mt-0.5">{it["label"]}</span>')
            html.append('    </a>')
            
    html.append('  </nav>')
    return '\n'.join(html)

nav_pattern = re.compile(
    r'\s*<!-- BOTTOM NAVIGATION MOBILE \(< 1024px\) -->\s*<nav[^>]*aria-label="Navegación inferior móvil"[^>]*>[\s\S]*?</nav>',
    re.MULTILINE
)

for fname in files:
    fpath = os.path.join(coordinacion_dir, fname)
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_nav = get_bottom_nav(fname)
    content = nav_pattern.sub('\n\n' + new_nav, content)
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Standardized bottom nav in {fname}")
