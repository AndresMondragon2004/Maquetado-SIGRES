import os
import re
import glob

NOTIFICATIONS_DATA = {
    "02-estudiante": {
        "unread_count": 2,
        "items": [
            {
                "icon": "task_alt",
                "icon_color": "text-emerald-600 bg-emerald-50 border-emerald-200",
                "title": "Bitácora #5 validada",
                "desc": "El Asesor Externo (Mtro. Armando Alcalde) ha firmado tu bitácora de la semana 5.",
                "time": "Hace 25 min",
                "unread": True,
                "link": "08-mis-bitacoras.html"
            },
            {
                "icon": "event_upcoming",
                "icon_color": "text-amber-600 bg-amber-50 border-amber-200",
                "title": "Entrega de informe parcial",
                "desc": "Tienes 3 días para subir tu Informe Parcial (320 horas meta requeridas).",
                "time": "Hace 2 horas",
                "unread": True,
                "link": "13-mis-informes.html"
            },
            {
                "icon": "verified",
                "icon_color": "text-blue-600 bg-blue-50 border-blue-200",
                "title": "Empresa receptora validada",
                "desc": "Control Escolar ha aprobado el registro de UMB · Dirección Académica.",
                "time": "Ayer",
                "unread": False,
                "link": "02-mi-expediente.html"
            }
        ]
    },
    "03-asesor-interno": {
        "unread_count": 2,
        "items": [
            {
                "icon": "rate_review",
                "icon_color": "text-umb-guinda bg-umb-guinda-light border-umb-guinda/20",
                "title": "Informe parcial por evaluar",
                "desc": "Jesús Andrés Mondragón Tenorio (13220024) envió su Informe Parcial.",
                "time": "Hace 15 min",
                "unread": True,
                "link": "06-evaluar-informe-parcial.html"
            },
            {
                "icon": "fact_check",
                "icon_color": "text-amber-600 bg-amber-50 border-amber-200",
                "title": "Bitácoras por revisar",
                "desc": "3 alumnos han registrado nuevas actividades semanales de seguimiento.",
                "time": "Hace 1 hora",
                "unread": True,
                "link": "05-revisar-bitacoras.html"
            },
            {
                "icon": "event_available",
                "icon_color": "text-emerald-600 bg-emerald-50 border-emerald-200",
                "title": "Asesoría registrada con éxito",
                "desc": "Se guardó la minuta de asesoría técnica con Jesús Andrés Mondragón.",
                "time": "Hace 2 días",
                "unread": False,
                "link": "04-registrar-asesoria.html"
            }
        ]
    },
    "04-asesor-externo": {
        "unread_count": 2,
        "items": [
            {
                "icon": "pending_actions",
                "icon_color": "text-umb-guinda bg-umb-guinda-light border-umb-guinda/20",
                "title": "Bitácora #6 por validar",
                "desc": "Jesús Andrés Mondragón reportó 35 horas en Dirección Académica.",
                "time": "Hace 10 min",
                "unread": True,
                "link": "02-bitacoras-por-validar.html"
            },
            {
                "icon": "badge",
                "icon_color": "text-blue-600 bg-blue-50 border-blue-200",
                "title": "Residente activo asignado",
                "desc": "Se ha confirmado la asignación de Jesús Andrés Mondragón al proyecto.",
                "time": "Hace 1 día",
                "unread": True,
                "link": "04-residentes-asignados.html"
            },
            {
                "icon": "task_alt",
                "icon_color": "text-emerald-600 bg-emerald-50 border-emerald-200",
                "title": "Validación completada",
                "desc": "Firmaste satisfactoriamente la bitácora #5 de Jesús Andrés Mondragón.",
                "time": "Hace 3 días",
                "unread": False,
                "link": "05-historial-validaciones.html"
            }
        ]
    },
    "05-control-escolar": {
        "unread_count": 2,
        "items": [
            {
                "icon": "folder_shared",
                "icon_color": "text-umb-guinda bg-umb-guinda-light border-umb-guinda/20",
                "title": "Expediente digital recibido",
                "desc": "Expediente de Jesús Andrés Mondragón (ISC) listo para validación de requisitos.",
                "time": "Hace 30 min",
                "unread": True,
                "link": "02-bandeja-expedientes.html"
            },
            {
                "icon": "print",
                "icon_color": "text-amber-600 bg-amber-50 border-amber-200",
                "title": "Carta de presentación solicitada",
                "desc": "2 estudiantes solicitaron emisión oficial de carta de presentación.",
                "time": "Hace 3 horas",
                "unread": True,
                "link": "05-generar-carta.html"
            },
            {
                "icon": "add_business",
                "icon_color": "text-purple-600 bg-purple-50 border-purple-200",
                "title": "Empresa nueva registrada",
                "desc": "Se agregó 'Dirección Académica UMB' para confirmación de convenio.",
                "time": "Ayer",
                "unread": False,
                "link": "07-validar-empresas-nuevas.html"
            }
        ]
    },
    "06-coordinacion": {
        "unread_count": 2,
        "items": [
            {
                "icon": "warning",
                "icon_color": "text-rose-600 bg-rose-50 border-rose-200",
                "title": "Alerta de riesgo de cohorte",
                "desc": "2 alumnos de ISC presentan retraso mayor a 2 semanas en bitácoras.",
                "time": "Hace 15 min",
                "unread": True,
                "link": "03-supervision-riesgo.html"
            },
            {
                "icon": "draw",
                "icon_color": "text-umb-guinda bg-umb-guinda-light border-umb-guinda/20",
                "title": "Cartas para firma digital",
                "desc": "4 cartas de presentación de ISC listas para firma institucional.",
                "time": "Hace 1 hora",
                "unread": True,
                "link": "05-firma-cartas.html"
            },
            {
                "icon": "support",
                "icon_color": "text-amber-600 bg-amber-50 border-amber-200",
                "title": "Contingencia atendida",
                "desc": "Se validó el cambio de asesor interno para la carrera de IIAS.",
                "time": "Hace 2 días",
                "unread": False,
                "link": "04-contingencias.html"
            }
        ]
    },
    "07-direccion": {
        "unread_count": 2,
        "items": [
            {
                "icon": "analytics",
                "icon_color": "text-umb-guinda bg-umb-guinda-light border-umb-guinda/20",
                "title": "Reporte ejecutivo mensual listo",
                "desc": "Consolidado de avance de residencias ciclo 26-27/1 disponible.",
                "time": "Hace 40 min",
                "unread": True,
                "link": "01-dashboard-ejecutivo.html"
            },
            {
                "icon": "verified_user",
                "icon_color": "text-emerald-600 bg-emerald-50 border-emerald-200",
                "title": "Acreditación institucional",
                "desc": "El 94% de expedientes cumplen los indicadores de acreditación CACEI.",
                "time": "Hace 4 horas",
                "unread": True,
                "link": "04-reportes-acreditacion.html"
            },
            {
                "icon": "handshake",
                "icon_color": "text-blue-600 bg-blue-50 border-blue-200",
                "title": "Convenio institucional renovado",
                "desc": "Se renovaron los acuerdos de residencia con la Dirección Académica.",
                "time": "Ayer",
                "unread": False,
                "link": "02-vinculacion-convenios.html"
            }
        ]
    }
}

def build_role_header_with_dropdown(role_cfg, filename, role_key):
    logo_path = "../assets/logo_umb.png"
    screen_name = role_cfg["screen_names"].get(filename, "Detalle")
    notif_data = NOTIFICATIONS_DATA.get(role_key, NOTIFICATIONS_DATA["02-estudiante"])
    
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

    return f"""  <!-- APP BAR SUPERIOR CANÓNICA (64px) CON NOTIFICACIONES PERSONALIZADAS -->
  <header class="fixed top-0 left-0 right-0 h-16 bg-umb-guinda text-white z-50 shadow-md border-b border-umb-guinda-dark flex items-center justify-between px-4 sm:px-6">
    <!-- Izquierda: Logo UMB + Nombre Sistema + Plantel + Breadcrumb -->
    <div class="flex items-center gap-3 md:gap-4">
      <a href="{role_cfg['sidebar_items'][0]['link']}" class="flex items-center gap-2.5 group">
        <div class="bg-white p-1 rounded h-9 w-auto flex items-center justify-center shadow-sm">
          <img src="{logo_path}" alt="Logo UMB" class="h-7 w-auto object-contain">
        </div>
        <div class="flex flex-col">
          <span class="font-bold text-base tracking-tight text-white leading-none">SIGRES-UMB</span>
          <span class="text-[11px] text-white/80 leading-tight mt-0.5 hidden sm:block">UES San José del Rincón</span>
        </div>
      </a>
      <div class="hidden sm:block h-6 w-px bg-white/20"></div>
      <div class="hidden lg:flex items-center text-xs text-white/80 ml-2 gap-1.5">
        <span class="font-medium text-white/90">{role_cfg['role_name']}</span>
        <span class="material-symbols-outlined text-[14px]">chevron_right</span>
        <span class="text-white font-semibold">{screen_name}</span>
      </div>
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

NOTIF_SCRIPT = """  <!-- SCRIPT INTERACTIVO DE NOTIFICACIONES PERSONALIZADAS POR ROL -->
  <script>
    function toggleRoleNotifications(event) {
      if (event) event.stopPropagation();
      const dropdown = document.getElementById('notifDropdown');
      if (dropdown) {
        dropdown.classList.toggle('hidden');
      }
    }

    function markAllNotificationsAsRead(event) {
      if (event) event.stopPropagation();
      const badge = document.getElementById('notifBadge');
      const headerBadge = document.getElementById('notifHeaderBadge');
      const dots = document.querySelectorAll('.unread-dot');
      const items = document.querySelectorAll('.notif-item');

      if (badge) badge.classList.add('hidden');
      if (headerBadge) {
        headerBadge.textContent = '0 nuevas';
        headerBadge.classList.remove('bg-umb-guinda/10', 'text-umb-guinda');
        headerBadge.classList.add('bg-slate-100', 'text-slate-500');
      }
      dots.forEach(d => d.remove());
      items.forEach(i => {
        i.classList.remove('bg-umb-guinda-light/40');
        i.classList.add('bg-white');
      });
    }

    // Cerrar al hacer clic fuera
    document.addEventListener('click', function(e) {
      const container = document.getElementById('notifContainer');
      const dropdown = document.getElementById('notifDropdown');
      if (container && dropdown && !container.contains(e.target)) {
        dropdown.classList.add('hidden');
      }
    });

    // Cerrar con Escape
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') {
        const dropdown = document.getElementById('notifDropdown');
        if (dropdown) dropdown.classList.add('hidden');
      }
    });
  </script>"""

def apply_personalized_notifications():
    from standardize_lib import ROLE_CONFIGS
    base_dir = r"c:\Users\Pc\Downloads\Maquetado - Residencia\respaldo-pre-estandarizacion-2026-09-17\sigres-umb"
    
    for role_key, role_cfg in ROLE_CONFIGS.items():
        role_dir = os.path.join(base_dir, role_key)
        files = glob.glob(os.path.join(role_dir, "*.html"))
        
        for fpath in files:
            filename = os.path.basename(fpath)
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()

            # Replace Header with role-customized notification header
            new_header = build_role_header_with_dropdown(role_cfg, filename, role_key)
            content = re.sub(r'<header.*?</header>', new_header, content, count=1, flags=re.DOTALL | re.IGNORECASE)

            # Ensure notification script is included before </body>
            if 'toggleRoleNotifications' not in content:
                body_end = re.search(r'</body>', content, flags=re.IGNORECASE)
                if body_end:
                    content = content[:body_end.start()] + "\n" + NOTIF_SCRIPT + "\n" + content[body_end.start():]
            else:
                # Replace existing script if any
                content = re.sub(r'<!-- SCRIPT INTERACTIVO DE NOTIFICACIONES.*?-->\s*<script>.*?</script>', NOTIF_SCRIPT, content, flags=re.DOTALL)

            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)

    print("Personalized notifications applied to all role screens successfully.")

if __name__ == "__main__":
    apply_personalized_notifications()
