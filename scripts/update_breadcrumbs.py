import os
import re
import glob
from standardize_lib import ROLE_CONFIGS
from inject_personalized_notifications import build_role_header_with_dropdown, NOTIFICATIONS_DATA

BASE_DIR = r"c:\Users\Pc\Downloads\Maquetado - Residencia\respaldo-pre-estandarizacion-2026-09-17\sigres-umb"

def generate_perfect_breadcrumb_header(role_cfg, filename, role_key):
    logo_path = "../assets/logo_umb.png"
    screen_name = role_cfg["screen_names"].get(filename, "Detalle")
    notif_data = NOTIFICATIONS_DATA.get(role_key, NOTIFICATIONS_DATA["02-estudiante"])
    dashboard_link = role_cfg["sidebar_items"][0]["link"]
    
    is_dashboard = (filename == dashboard_link) or ("01-" in filename)
    
    if is_dashboard:
        breadcrumb_html = f"""      <div class="hidden sm:flex items-center text-xs text-white/90 ml-3 pl-3 border-l border-white/20 gap-1.5">
        <span class="material-symbols-outlined text-[16px] text-white">home</span>
        <span class="font-semibold text-white tracking-wide">Inicio</span>
      </div>"""
    else:
        breadcrumb_html = f"""      <div class="hidden sm:flex items-center text-xs text-white/80 ml-3 pl-3 border-l border-white/20 gap-1.5">
        <a href="{dashboard_link}" class="hover:text-white hover:underline flex items-center gap-1 transition-colors text-white/90">
          <span class="material-symbols-outlined text-[15px]">home</span>
          <span>Inicio</span>
        </a>
        <span class="material-symbols-outlined text-[13px] text-white/60">chevron_right</span>
        <span class="font-semibold text-white">{screen_name}</span>
      </div>"""

    unread_badge = f'<span id="notifBadge" class="absolute top-1.5 right-1.5 min-w-[18px] h-[18px] px-1 bg-umb-warning text-umb-carbon text-[10px] font-bold rounded-full flex items-center justify-center border-2 border-umb-guinda shadow-sm">{notif_data["unread_count"]}</span>'

    items_html = []
    for item in notif_data["items"]:
        unread_dot = '<span class="unread-dot w-2 h-2 rounded-full bg-umb-guinda flex-shrink-0"></span>' if item["unread"] else ''
        bg_cls = "bg-umb-guinda-light/40" if item["unread"] else "bg-white hover:bg-umb-surface"
        items_html.append(f"""            <a href="{item['link']}" class="notif-item block p-3 {bg_cls} transition-colors border-b border-umb-border/60 last:border-0 group">
              <div class="flex items-start gap-3">
                <div class="w-8 h-8 rounded-lg {item['icon_color']} flex items-center justify-center flex-shrink-0 border mt-0.5">
                  <span class="material-symbols-outlined text-[18px]">{item['icon']}</span>
                </div>
                <div class="flex-1 min-w-0">
                  <div class="flex items-center justify-between gap-1">
                    <p class="text-xs font-semibold text-umb-carbon group-hover:text-umb-guinda truncate leading-tight">{item['title']}</p>
                    {unread_dot}
                  </div>
                  <p class="text-[11px] text-umb-muted leading-snug mt-0.5">{item['desc']}</p>
                  <span class="text-[10px] text-umb-outline mt-1 block">{item['time']}</span>
                </div>
              </div>
            </a>""")

    notif_rows = "\n".join(items_html)

    dropdown_html = f"""        <!-- DROPDOWN PERSONALIZADO DE NOTIFICACIONES ({role_cfg['role_name']}) -->
        <div id="notifDropdown" class="hidden absolute right-0 top-12 w-[340px] sm:w-[380px] bg-white rounded-xl shadow-modal border border-umb-border z-50 overflow-hidden flex flex-col text-umb-carbon animate-in fade-in zoom-in-95 duration-150">
          
          <!-- Encabezado del Dropdown -->
          <div class="p-3.5 bg-gradient-to-r from-umb-surface to-white border-b border-umb-border flex items-center justify-between">
            <div class="flex items-center gap-2">
              <span class="material-symbols-outlined text-umb-guinda text-[20px]">notifications_active</span>
              <h3 class="text-xs font-bold text-umb-carbon">Notificaciones ({role_cfg['role_name']})</h3>
              <span id="notifHeaderBadge" class="bg-umb-guinda/10 text-umb-guinda text-[10px] font-bold px-2 py-0.5 rounded-full">{notif_data['unread_count']} nuevas</span>
            </div>
            <button type="button" onclick="markAllNotificationsAsRead(event)" class="text-[11px] font-medium text-umb-guinda hover:underline hover:text-umb-guinda-dark">
              Marcar leídas
            </button>
          </div>

          <!-- Lista de Notificaciones de Rol -->
          <div class="max-h-[320px] overflow-y-auto custom-scrollbar" id="notifListContainer">
{notif_rows}
          </div>

          <!-- Pie del Dropdown -->
          <div class="p-2.5 bg-umb-surface/80 border-t border-umb-border text-center">
            <a href="../08-transversales/04-centro-notificaciones.html" class="text-xs font-semibold text-umb-guinda hover:text-umb-guinda-dark flex items-center justify-center gap-1.5 py-1">
              <span>Abrir centro de notificaciones general</span>
              <span class="material-symbols-outlined text-[14px]">arrow_forward</span>
            </a>
          </div>
        </div>"""

    return f"""  <!-- APP BAR SUPERIOR CANÓNICA (64px) CON BREADCRUMB (Inicio / {screen_name}) -->
  <header class="fixed top-0 left-0 right-0 h-16 bg-umb-guinda text-white z-50 shadow-md border-b border-umb-guinda-dark flex items-center justify-between px-4 sm:px-6">
    <!-- Izquierda: Logo UMB + Nombre Sistema + Plantel + Breadcrumb (Inicio / Apartado) -->
    <div class="flex items-center gap-3 md:gap-4">
      <a href="{dashboard_link}" class="flex items-center gap-2.5 group">
        <div class="bg-white p-1 rounded h-9 w-auto flex items-center justify-center shadow-sm">
          <img src="{logo_path}" alt="Logo UMB" class="h-7 w-auto object-contain">
        </div>
        <div class="flex flex-col">
          <span class="font-bold text-base tracking-tight text-white leading-none">SIGRES-UMB</span>
          <span class="text-[11px] text-white/80 leading-tight mt-0.5 hidden sm:block">UES San José del Rincón</span>
        </div>
      </a>
      <div class="hidden sm:block h-6 w-px bg-white/20"></div>
{breadcrumb_html}
    </div>

    <!-- Derecha: Trigger Notificaciones Personalizadas + Avatar Usuario -->
    <div class="flex items-center gap-3 sm:gap-4">
      
      <!-- CONTENEDOR DE NOTIFICACIONES INTERACTIVO -->
      <div class="relative" id="notifContainer">
        <button type="button" 
                id="notifBellBtn"
                onclick="toggleRoleNotifications(event)"
                class="relative p-2 rounded-full hover:bg-white/10 transition-colors text-white focus:outline-none focus:ring-2 focus:ring-white/40 flex items-center justify-center" 
                title="Notificaciones de {role_cfg['role_name']}" 
                aria-label="Abrir notificaciones de {role_cfg['role_name']}">
          <span class="material-symbols-outlined text-[24px]">notifications</span>
          {unread_badge}
        </button>

{dropdown_html}
      </div>

      <div class="h-6 w-px bg-white/20"></div>
      
      <a href="{role_cfg['profile_link']}" class="flex items-center gap-2.5 hover:opacity-95 transition-opacity group">
        <div class="w-8 h-8 rounded-full bg-white/20 ring-1 ring-white/40 flex items-center justify-center text-white font-bold text-xs">
          {role_cfg['user_initials']}
        </div>
        <div class="hidden md:flex flex-col text-right">
          <span class="text-xs font-semibold text-white leading-tight">{role_cfg['user_short']}</span>
          <span class="text-[10px] text-white/75 leading-none">{role_cfg['role_name']}</span>
        </div>
      </a>
    </div>
  </header>"""

def update_all_headers():
    for role_key, role_cfg in ROLE_CONFIGS.items():
        role_dir = os.path.join(BASE_DIR, role_key)
        files = glob.glob(os.path.join(role_dir, "*.html"))
        
        for fpath in files:
            filename = os.path.basename(fpath)
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()

            new_header = generate_perfect_breadcrumb_header(role_cfg, filename, role_key)
            content = re.sub(r'<header.*?</header>', new_header, content, count=1, flags=re.DOTALL | re.IGNORECASE)

            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)

    print("All role headers updated with clear 'Inicio / <Apartado>' breadcrumbs and 'hidden sm:flex' visibility.")

if __name__ == "__main__":
    update_all_headers()
