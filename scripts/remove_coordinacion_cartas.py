import os
import re

# 1. Files in 06-coordinacion to update
coordinacion_dir = 'sigres-umb/06-coordinacion'
coord_files = [
    '01-dashboard-monitoreo.html',
    '02-cohortes-carreras.html',
    '03-supervision-riesgo.html',
    '04-contingencias.html',
    '06-reportes-ejecutivos.html',
    '07-notificaciones.html',
    '08-mi-perfil.html'
]

for fname in coord_files:
    fpath = os.path.join(coordinacion_dir, fname)
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # A. Remove sidebar link for 05-firma-cartas.html
    # Pattern matching the <a> block for 05-firma-cartas in desktop sidebar
    sidebar_link_pattern = re.compile(
        r'\s*<a\s+href="05-firma-cartas\.html"[^>]*>[\s\S]*?</a>',
        re.MULTILINE
    )
    content = sidebar_link_pattern.sub('', content)

    # B. Replace notification item pointing to 05-firma-cartas.html with 06-reportes-ejecutivos.html
    old_notif_pattern = re.compile(
        r'<a\s+href="05-firma-cartas\.html"\s+class="notif-item[^"]*"[^>]*>[\s\S]*?</a>',
        re.MULTILINE
    )
    new_notif_item = '''<a href="06-reportes-ejecutivos.html" class="notif-item block p-3 bg-umb-guinda-light/40 transition-colors border-b border-umb-border/60 last:border-0 group">
              <div class="flex items-start gap-3">
                <div class="w-8 h-8 rounded-lg text-umb-guinda bg-umb-guinda-light border-umb-guinda/20 flex items-center justify-center flex-shrink-0 border mt-0.5">
                  <span class="material-symbols-outlined text-[18px]">summarize</span>
                </div>
                <div class="flex-1 min-w-0">
                  <div class="flex items-center justify-between gap-1">
                    <p class="text-xs font-semibold text-umb-carbon group-hover:text-umb-guinda truncate leading-tight">Reporte ejecutivo disponible</p>
                    <span class="unread-dot w-2 h-2 rounded-full bg-umb-guinda flex-shrink-0"></span>
                  </div>
                  <p class="text-[11px] text-umb-muted leading-snug mt-0.5">Estadísticas y avance general del ciclo 2026-2027/1 listos para consulta.</p>
                  <span class="text-[10px] text-umb-outline mt-1 block">Hace 1 hora</span>
                </div>
              </div>
            </a>'''
    content = old_notif_pattern.sub(new_notif_item, content)

    # C. Update bottom mobile nav if it had 05-firma-cartas.html
    # Replace the mobile bottom nav item
    mobile_pattern = re.compile(
        r'<a\s+href="05-firma-cartas\.html"\s+class="flex flex-col[^"]*"[^>]*>[\s\S]*?</a>',
        re.MULTILINE
    )
    new_mobile_item = '''<a href="06-reportes-ejecutivos.html" class="flex flex-col items-center justify-center flex-1 py-1 text-umb-outline hover:text-umb-carbon">
      <span class="material-symbols-outlined text-[22px]">summarize</span>
      <span class="text-[11px] font-medium mt-0.5">Reportes</span>
    </a>'''
    content = mobile_pattern.sub(new_mobile_item, content)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {fpath}")

# 2. Update index portals (sigres-umb/index.html, index.html, sigres-umb/00-portal/index.html)
portal_files = ['sigres-umb/index.html', 'index.html', 'sigres-umb/00-portal/index.html']
for pfile in portal_files:
    if not os.path.exists(pfile):
        continue
    with open(pfile, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the list item with 05-firma-cartas.html
    item_pattern = re.compile(
        r'\s*<li\s+class="screen-item">\s*<a\s+href="[^"]*06-coordinacion/05-firma-cartas\.html"[^>]*>[\s\S]*?</a>\s*</li>',
        re.MULTILINE
    )
    content = item_pattern.sub('', content)

    with open(pfile, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated portal {pfile}")

# 3. Update standardize_lib.py
lib_file = 'scripts/standardize_lib.py'
if os.path.exists(lib_file):
    with open(lib_file, 'r', encoding='utf-8') as f:
        lcontent = f.read()
    
    # Remove from COORDINACION config
    lcontent = re.sub(r'\s*\{"id":\s*"05-firma-cartas"[^\}]*\},?', '', lcontent)
    lcontent = re.sub(r'\s*\{"label":\s*"Firmas"[^\}]*\},?', '', lcontent)
    lcontent = re.sub(r'\s*"05-firma-cartas\.html":\s*"[^"]*",?', '', lcontent)

    with open(lib_file, 'w', encoding='utf-8') as f:
        f.write(lcontent)
    print(f"Updated {lib_file}")

# 4. Remove sigres-umb/06-coordinacion/05-firma-cartas.html
removed_file = 'sigres-umb/06-coordinacion/05-firma-cartas.html'
if os.path.exists(removed_file):
    os.remove(removed_file)
    print(f"Deleted {removed_file}")
