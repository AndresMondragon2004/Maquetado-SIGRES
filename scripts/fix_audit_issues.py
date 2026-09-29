import os
import re

# 1. Fix 08-transversales links
transversales_files = [
    'sigres-umb/08-transversales/11-modal-sesion-expirada.html',
    'sigres-umb/08-transversales/12-busqueda-global.html',
    'sigres-umb/08-transversales/13-pagina-403.html'
]

for fpath in transversales_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            c = f.read()
        c = c.replace('../01-estudiante/01-dashboard.html', '../02-estudiante/01-dashboard.html')
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Fixed {fpath}")

# 2. Fix 06-coordinacion/01-dashboard-monitoreo.html button
coord_dash = 'sigres-umb/06-coordinacion/01-dashboard-monitoreo.html'
if os.path.exists(coord_dash):
    with open(coord_dash, 'r', encoding='utf-8') as f:
        c = f.read()
    
    old_btn = '''              <!-- Botón 3 -->
              <button class="w-full flex items-center justify-between px-4 py-3 bg-umb-guinda hover:bg-[#521422] text-white text-xs font-semibold rounded-lg shadow-sm transition-colors group">
                <div class="flex items-center gap-3">
                  <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z" />
                  </svg>
                  <span>Firmar cartas (3 pendientes)</span>
                </div>
                <span class="text-[10px] font-bold bg-white text-umb-guinda px-2 py-0.5 rounded-full">Firma e.firma</span>
              </button>'''

    new_btn = '''              <!-- Botón 3 -->
              <a href="06-reportes-ejecutivos.html" class="w-full flex items-center justify-between px-4 py-3 bg-umb-guinda hover:bg-[#521422] text-white text-xs font-semibold rounded-lg shadow-sm transition-colors group">
                <div class="flex items-center gap-3">
                  <span class="material-symbols-outlined text-[18px] text-white">summarize</span>
                  <span>Consultar reportes ejecutivos</span>
                </div>
                <span class="text-[10px] font-bold bg-white text-umb-guinda px-2 py-0.5 rounded-full">Ciclo 26-27/1</span>
              </a>'''
    
    if old_btn in c:
        c = c.replace(old_btn, new_btn)
        with open(coord_dash, 'w', encoding='utf-8') as f:
            f.write(c)
        print("Updated button in 01-dashboard-monitoreo.html")
    else:
        # Regex replacement if whitespace slightly differs
        c = re.sub(
            r'<!-- Botón 3 -->\s*<button[^>]*>\s*<div[^>]*>[\s\S]*?Firmar cartas[\s\S]*?</button>',
            new_btn,
            c
        )
        with open(coord_dash, 'w', encoding='utf-8') as f:
            f.write(c)
        print("Regex updated button in 01-dashboard-monitoreo.html")

# 3. Update scripts/generate_master_index.py to properly support prefix for 00-portal
gen_script = 'scripts/generate_master_index.py'
if os.path.exists(gen_script):
    with open(gen_script, 'r', encoding='utf-8') as f:
        gc = f.read()
    
    # Update build_index_html function signature / logic
    old_signature = 'def build_index_html(is_root=True):'
    new_signature = '''def build_index_html(prefix_type="root"):
    if prefix_type == "root":
        prefix = "sigres-umb/"
        logo_path = "sigres-umb/assets/logo_umb.png"
    elif prefix_type == "sigres":
        prefix = ""
        logo_path = "assets/logo_umb.png"
    elif prefix_type == "subfolder":
        prefix = "../"
        logo_path = "../assets/logo_umb.png"'''
    
    gc = gc.replace(
        '''def build_index_html(is_root=True):
    prefix = "sigres-umb/" if is_root else ""
    logo_path = "sigres-umb/assets/logo_umb.png" if is_root else "assets/logo_umb.png"''',
        new_signature
    )
    
    # Update main block
    old_main = '''if __name__ == "__main__":
    root_index = build_index_html(is_root=True)
    with open(r"c:\\Users\\Pc\\Downloads\\Maquetado - Residencia\\respaldo-pre-estandarizacion-2026-09-17\\index.html", "w", encoding="utf-8") as f:
        f.write(root_index)

    sigres_index = build_index_html(is_root=False)
    with open(r"c:\\Users\\Pc\\Downloads\\Maquetado - Residencia\\respaldo-pre-estandarizacion-2026-09-17\\sigres-umb\\index.html", "w", encoding="utf-8") as f:
        f.write(sigres_index)

    with open(r"c:\\Users\\Pc\\Downloads\\Maquetado - Residencia\\respaldo-pre-estandarizacion-2026-09-17\\sigres-umb\\00-portal\\index.html", "w", encoding="utf-8") as f:
        f.write(sigres_index)'''
        
    new_main = '''if __name__ == "__main__":
    root_index = build_index_html(prefix_type="root")
    with open(r"c:\\Users\\Pc\\Downloads\\Maquetado - Residencia\\respaldo-pre-estandarizacion-2026-09-17\\index.html", "w", encoding="utf-8") as f:
        f.write(root_index)

    sigres_index = build_index_html(prefix_type="sigres")
    with open(r"c:\\Users\\Pc\\Downloads\\Maquetado - Residencia\\respaldo-pre-estandarizacion-2026-09-17\\sigres-umb\\index.html", "w", encoding="utf-8") as f:
        f.write(sigres_index)

    subfolder_index = build_index_html(prefix_type="subfolder")
    with open(r"c:\\Users\\Pc\\Downloads\\Maquetado - Residencia\\respaldo-pre-estandarizacion-2026-09-17\\sigres-umb\\00-portal\\index.html", "w", encoding="utf-8") as f:
        f.write(subfolder_index)'''

    gc = gc.replace(old_main, new_main)
    with open(gen_script, 'w', encoding='utf-8') as f:
        f.write(gc)
    print("Updated generate_master_index.py")
