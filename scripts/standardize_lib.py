import os
import re
import glob

HEAD_CANONICAL = """  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            umb: {
              guinda: '#681B2B',
              'guinda-dark': '#4F1420',
              'guinda-light': '#F9F5F6',
              dorado: '#9E773B',
              'dorado-dark': '#7F5E2B',
              'dorado-light': '#FEF3C7',
              surface: '#F4F5F7',
              card: '#FFFFFF',
              border: '#E2E8F0',
              carbon: '#1A1A1A',
              muted: '#544244',
              outline: '#877273',
              success: '#2D8C4E',
              warning: '#D69E2E',
              danger: '#C53030',
              info: '#2B6CB0'
            }
          },
          fontFamily: {
            sans: ['Inter', 'sans-serif']
          },
          borderRadius: {
            card: '8px',
            badge: '9999px',
            modal: '12px'
          },
          boxShadow: {
            card: '0 1px 3px 0 rgba(0, 0, 0, 0.06), 0 1px 2px -1px rgba(0, 0, 0, 0.04)',
            'card-hover': '0 10px 15px -3px rgba(104, 27, 43, 0.08), 0 4px 6px -4px rgba(0, 0, 0, 0.04)',
            modal: '0 20px 25px -5px rgba(0, 0, 0, 0.15), 0 8px 10px -6px rgba(0, 0, 0, 0.1)'
          }
        }
      }
    }
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
  <style>
    .material-symbols-outlined {
      font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
      display: inline-block;
      vertical-align: middle;
      line-height: 1;
    }
    .material-symbols-outlined.fill {
      font-variation-settings: 'FILL' 1, 'wght' 400, 'GRAD' 0, 'opsz' 24;
    }
    ::-webkit-scrollbar {
      width: 6px;
      height: 6px;
    }
    ::-webkit-scrollbar-track {
      background: #F4F5F7;
    }
    ::-webkit-scrollbar-thumb {
      background: #CBD5E1;
      border-radius: 9999px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: #94A3B8;
    }
  </style>"""

def get_floating_button(portal_path="../index.html"):
    return f"""<!-- BOTÓN FLOTANTE AL PORTAL (Solo para navegación del prototipo - Eliminar en producción) -->
<aside aria-label="Navegación al portal de prototipos" class="fixed bottom-6 right-6 z-50">
  <a href="{portal_path}" class="h-10 px-4 rounded-full bg-umb-guinda hover:bg-umb-guinda-dark text-white text-xs font-semibold shadow-xl border border-umb-dorado/40 flex items-center gap-2 backdrop-blur-md transition-all hover:scale-105 focus:outline-none focus:ring-2 focus:ring-umb-dorado">
    <span class="material-symbols-outlined text-sm text-amber-300">apps</span>
    <span>Ir al portal</span>
  </a>
</aside>"""

FOOTER_CANONICAL = """<footer class="pt-8 pb-4 text-center text-[12px] text-umb-outline space-y-1">
  <p>SIGRES-UMB — Sistema integral para la gestión de residencias profesionales</p>
  <p>Universidad Mexiquense del Bicentenario · UES San José del Rincón · Ciclo 26-27/1</p>
</footer>"""

ROLE_CONFIGS = {
    "02-estudiante": {
        "role_name": "Estudiante",
        "user_name": "Jesús Andrés Mondragón Tenorio",
        "user_short": "Jesús Andrés Mondragón",
        "user_initials": "JM",
        "user_subtitle": "Matrícula: 13220024 · ISC",
        "profile_link": "14-mi-perfil.html",
        "sidebar_items": [
            {"id": "01-dashboard", "label": "Inicio", "icon": "home", "link": "01-dashboard.html", "matches": ["01-dashboard.html"]},
            {"id": "08-mis-bitacoras", "label": "Bitácoras", "icon": "menu_book", "link": "08-mis-bitacoras.html", "matches": ["08-mis-bitacoras.html", "09-nueva-bitacora.html", "10-detalle-bitacora.html"]},
            {"id": "02-mi-expediente", "label": "Expediente", "icon": "folder", "link": "02-mi-expediente.html", "matches": ["02-mi-expediente.html", "03-buscar-empresa.html", "04-registrar-empresa.html", "05-estatus-validacion-empresa.html", "06-solicitud-residencia.html", "07-carta-presentacion-generada.html"]},
            {"id": "13-mis-informes", "label": "Informes", "icon": "description", "link": "13-mis-informes.html", "matches": ["13-mis-informes.html", "11-mi-progreso.html", "12-cronograma.html"]},
            {"id": "14-mi-perfil", "label": "Perfil", "icon": "person", "link": "14-mi-perfil.html", "matches": ["14-mi-perfil.html"]}
        ],
        "mobile_items": [
            {"label": "Inicio", "icon": "home", "link": "01-dashboard.html", "matches": ["01-dashboard.html"]},
            {"label": "Bitácoras", "icon": "menu_book", "link": "08-mis-bitacoras.html", "matches": ["08-mis-bitacoras.html", "09-nueva-bitacora.html", "10-detalle-bitacora.html"]},
            {"label": "Expediente", "icon": "folder", "link": "02-mi-expediente.html", "matches": ["02-mi-expediente.html", "03-buscar-empresa.html", "04-registrar-empresa.html", "05-estatus-validacion-empresa.html", "06-solicitud-residencia.html", "07-carta-presentacion-generada.html"]},
            {"label": "Informes", "icon": "description", "link": "13-mis-informes.html", "matches": ["13-mis-informes.html", "11-mi-progreso.html", "12-cronograma.html"]},
            {"label": "Perfil", "icon": "person", "link": "14-mi-perfil.html", "matches": ["14-mi-perfil.html"]}
        ],
        "screen_names": {
            "01-dashboard.html": "Inicio",
            "02-mi-expediente.html": "Mi expediente",
            "03-buscar-empresa.html": "Buscar empresa",
            "04-registrar-empresa.html": "Registrar empresa",
            "05-estatus-validacion-empresa.html": "Estatus de validación",
            "06-solicitud-residencia.html": "Solicitud de residencia",
            "07-carta-presentacion-generada.html": "Carta de presentación",
            "08-mis-bitacoras.html": "Mis bitácoras",
            "09-nueva-bitacora.html": "Nueva bitácora",
            "10-detalle-bitacora.html": "Detalle de bitácora",
            "11-mi-progreso.html": "Mi progreso de horas",
            "12-cronograma.html": "Cronograma de actividades",
            "13-mis-informes.html": "Mis informes",
            "14-mi-perfil.html": "Mi perfil"
        }
    },
    "03-asesor-interno": {
        "role_name": "Asesor interno",
        "user_name": "I.S.C. Leonardo Becerril Sánchez",
        "user_short": "I.S.C. Leonardo Becerril",
        "user_initials": "LB",
        "user_subtitle": "Docente Asesor · ISC",
        "profile_link": "08-mi-perfil.html",
        "sidebar_items": [
            {"id": "01-dashboard", "label": "Inicio", "icon": "home", "link": "01-dashboard.html", "matches": ["01-dashboard.html"]},
            {"id": "02-mis-alumnos", "label": "Mis alumnos", "icon": "group", "link": "02-mis-alumnos.html", "matches": ["02-mis-alumnos.html", "03-detalle-alumno.html"]},
            {"id": "04-registrar-asesoria", "label": "Asesorías", "icon": "assignment", "link": "04-registrar-asesoria.html", "matches": ["04-registrar-asesoria.html"]},
            {"id": "05-revisar-bitacoras", "label": "Evaluaciones", "icon": "fact_check", "link": "05-revisar-bitacoras.html", "matches": ["05-revisar-bitacoras.html", "06-evaluar-informe-parcial.html", "07-evaluar-informe-final.html"]},
            {"id": "08-mi-perfil", "label": "Perfil", "icon": "person", "link": "08-mi-perfil.html", "matches": ["08-mi-perfil.html"]}
        ],
        "mobile_items": [
            {"label": "Inicio", "icon": "home", "link": "01-dashboard.html", "matches": ["01-dashboard.html"]},
            {"label": "Mis alumnos", "icon": "group", "link": "02-mis-alumnos.html", "matches": ["02-mis-alumnos.html", "03-detalle-alumno.html"]},
            {"label": "Asesorías", "icon": "assignment", "link": "04-registrar-asesoria.html", "matches": ["04-registrar-asesoria.html"]},
            {"label": "Evaluaciones", "icon": "fact_check", "link": "05-revisar-bitacoras.html", "matches": ["05-revisar-bitacoras.html", "06-evaluar-informe-parcial.html", "07-evaluar-informe-final.html"]},
            {"label": "Perfil", "icon": "person", "link": "08-mi-perfil.html", "matches": ["08-mi-perfil.html"]}
        ],
        "screen_names": {
            "01-dashboard.html": "Inicio",
            "02-mis-alumnos.html": "Mis alumnos",
            "03-detalle-alumno.html": "Detalle de alumno",
            "04-registrar-asesoria.html": "Registrar asesoría",
            "05-revisar-bitacoras.html": "Evaluaciones y bitácoras",
            "06-evaluar-informe-parcial.html": "Evaluar informe parcial",
            "07-evaluar-informe-final.html": "Evaluar informe final",
            "08-mi-perfil.html": "Mi perfil"
        }
    },
    "04-asesor-externo": {
        "role_name": "Asesor externo",
        "user_name": "Mtro. Armando Alcalde Martínez",
        "user_short": "Mtro. Armando Alcalde",
        "user_initials": "AA",
        "user_subtitle": "Director Académico · UMB",
        "profile_link": "06-mi-perfil.html",
        "sidebar_items": [
            {"id": "01-dashboard", "label": "Inicio", "icon": "home", "link": "01-dashboard.html", "matches": ["01-dashboard.html"]},
            {"id": "02-bitacoras-por-validar", "label": "Bitácoras", "icon": "menu_book", "link": "02-bitacoras-por-validar.html", "matches": ["02-bitacoras-por-validar.html", "03-detalle-bitacora.html"]},
            {"id": "04-residentes-asignados", "label": "Residentes", "icon": "group", "link": "04-residentes-asignados.html", "matches": ["04-residentes-asignados.html"]},
            {"id": "05-historial-validaciones", "label": "Historial", "icon": "history", "link": "05-historial-validaciones.html", "matches": ["05-historial-validaciones.html"]},
            {"id": "06-mi-perfil", "label": "Perfil", "icon": "person", "link": "06-mi-perfil.html", "matches": ["06-mi-perfil.html"]}
        ],
        "mobile_items": [
            {"label": "Inicio", "icon": "home", "link": "01-dashboard.html", "matches": ["01-dashboard.html"]},
            {"label": "Bitácoras", "icon": "menu_book", "link": "02-bitacoras-por-validar.html", "matches": ["02-bitacoras-por-validar.html", "03-detalle-bitacora.html"]},
            {"label": "Residentes", "icon": "group", "link": "04-residentes-asignados.html", "matches": ["04-residentes-asignados.html"]},
            {"label": "Historial", "icon": "history", "link": "05-historial-validaciones.html", "matches": ["05-historial-validaciones.html"]},
            {"label": "Perfil", "icon": "person", "link": "06-mi-perfil.html", "matches": ["06-mi-perfil.html"]}
        ],
        "screen_names": {
            "01-dashboard.html": "Inicio",
            "02-bitacoras-por-validar.html": "Bitácoras por validar",
            "03-detalle-bitacora.html": "Detalle de bitácora",
            "04-residentes-asignados.html": "Residentes asignados",
            "05-historial-validaciones.html": "Historial de validaciones",
            "06-mi-perfil.html": "Mi perfil"
        }
    },
    "05-control-escolar": {
        "role_name": "Control Escolar",
        "user_name": "Lic. Estefanía Yttesen Nava",
        "user_short": "Lic. Estefanía Yttesen",
        "user_initials": "EY",
        "user_subtitle": "Responsable de Control Escolar",
        "profile_link": "09-mi-perfil.html",
        "sidebar_items": [
            {"id": "01-dashboard", "label": "Inicio", "icon": "home", "link": "01-dashboard.html", "matches": ["01-dashboard.html"]},
            {"id": "02-bandeja-expedientes", "label": "Expedientes", "icon": "folder_shared", "link": "02-bandeja-expedientes.html", "matches": ["02-bandeja-expedientes.html", "03-detalle-expediente.html"]},
            {"id": "04-validar-documentos", "label": "Documentos", "icon": "verified", "link": "04-validar-documentos.html", "matches": ["04-validar-documentos.html", "05-generar-carta.html"]},
            {"id": "06-catalogo-empresas", "label": "Empresas", "icon": "domain", "link": "06-catalogo-empresas.html", "matches": ["06-catalogo-empresas.html", "07-validar-empresas-nuevas.html"]},
            {"id": "08-reportes", "label": "Reportes", "icon": "analytics", "link": "08-reportes.html", "matches": ["08-reportes.html"]},
            {"id": "09-mi-perfil", "label": "Perfil", "icon": "person", "link": "09-mi-perfil.html", "matches": ["09-mi-perfil.html"]}
        ],
        "mobile_items": [
            {"label": "Inicio", "icon": "home", "link": "01-dashboard.html", "matches": ["01-dashboard.html"]},
            {"label": "Expedientes", "icon": "folder_shared", "link": "02-bandeja-expedientes.html", "matches": ["02-bandeja-expedientes.html", "03-detalle-expediente.html"]},
            {"label": "Documentos", "icon": "verified", "link": "04-validar-documentos.html", "matches": ["04-validar-documentos.html", "05-generar-carta.html"]},
            {"label": "Empresas", "icon": "domain", "link": "06-catalogo-empresas.html", "matches": ["06-catalogo-empresas.html", "07-validar-empresas-nuevas.html"]},
            {"label": "Perfil", "icon": "person", "link": "09-mi-perfil.html", "matches": ["09-mi-perfil.html"]}
        ],
        "screen_names": {
            "01-dashboard.html": "Inicio",
            "02-bandeja-expedientes.html": "Bandeja de expedientes",
            "03-detalle-expediente.html": "Detalle de expediente",
            "04-validar-documentos.html": "Validación de documentos",
            "05-generar-carta.html": "Generar cartas oficiales",
            "06-catalogo-empresas.html": "Catálogo de empresas",
            "07-validar-empresas-nuevas.html": "Validación de empresas",
            "08-reportes.html": "Reportes de control escolar",
            "09-mi-perfil.html": "Mi perfil"
        }
    },
    "06-coordinacion": {
        "role_name": "Coordinación",
        "user_name": "Mtro. Luis Ramón Vega Ramírez",
        "user_short": "Mtro. Luis Ramón Vega",
        "user_initials": "LV",
        "user_subtitle": "Coordinador de UES",
        "profile_link": "08-mi-perfil.html",
        "sidebar_items": [
            {"id": "01-dashboard-monitoreo", "label": "Monitoreo", "icon": "monitoring", "link": "01-dashboard-monitoreo.html", "matches": ["01-dashboard-monitoreo.html"]},
            {"id": "02-cohortes-carreras", "label": "Cohortes", "icon": "school", "link": "02-cohortes-carreras.html", "matches": ["02-cohortes-carreras.html"]},
            {"id": "03-supervision-riesgo", "label": "Riesgos", "icon": "warning", "link": "03-supervision-riesgo.html", "matches": ["03-supervision-riesgo.html"]},
            {"id": "04-contingencias", "label": "Contingencias", "icon": "support", "link": "04-contingencias.html", "matches": ["04-contingencias.html"]},
            {"id": "06-reportes-ejecutivos", "label": "Reportes", "icon": "summarize", "link": "06-reportes-ejecutivos.html", "matches": ["06-reportes-ejecutivos.html"]},
            {"id": "08-mi-perfil", "label": "Perfil", "icon": "person", "link": "08-mi-perfil.html", "matches": ["08-mi-perfil.html"]}
        ],
        "mobile_items": [
            {"label": "Monitoreo", "icon": "monitoring", "link": "01-dashboard-monitoreo.html", "matches": ["01-dashboard-monitoreo.html"]},
            {"label": "Riesgos", "icon": "warning", "link": "03-supervision-riesgo.html", "matches": ["03-supervision-riesgo.html"]},
            {"label": "Contingencias", "icon": "support", "link": "04-contingencias.html", "matches": ["04-contingencias.html"]},
            {"label": "Perfil", "icon": "person", "link": "08-mi-perfil.html", "matches": ["08-mi-perfil.html"]}
        ],
        "screen_names": {
            "01-dashboard-monitoreo.html": "Monitoreo de residencias",
            "02-cohortes-carreras.html": "Cohortes por carrera",
            "03-supervision-riesgo.html": "Supervisión de riesgo",
            "04-contingencias.html": "Gestión de contingencias",
            "06-reportes-ejecutivos.html": "Reportes ejecutivos",
            "07-notificaciones.html": "Gestión de notificaciones",
            "08-mi-perfil.html": "Mi perfil"
        }
    },
    "07-direccion": {
        "role_name": "Dirección",
        "user_name": "Mtro. Armando Alcalde Martínez",
        "user_short": "Mtro. Armando Alcalde",
        "user_initials": "AA",
        "user_subtitle": "Director Académico · UMB",
        "profile_link": "06-mi-perfil.html",
        "sidebar_items": [
            {"id": "01-dashboard-ejecutivo", "label": "Dashboard", "icon": "dashboard", "link": "01-dashboard-ejecutivo.html", "matches": ["01-dashboard-ejecutivo.html"]},
            {"id": "02-vinculacion-convenios", "label": "Vinculación", "icon": "handshake", "link": "02-vinculacion-convenios.html", "matches": ["02-vinculacion-convenios.html"]},
            {"id": "03-sectores-productivos", "label": "Sectores", "icon": "factory", "link": "03-sectores-productivos.html", "matches": ["03-sectores-productivos.html"]},
            {"id": "04-reportes-acreditacion", "label": "Acreditación", "icon": "verified_user", "link": "04-reportes-acreditacion.html", "matches": ["04-reportes-acreditacion.html"]},
            {"id": "05-configuracion-global", "label": "Configuración", "icon": "settings", "link": "05-configuracion-global.html", "matches": ["05-configuracion-global.html"]},
            {"id": "06-mi-perfil", "label": "Perfil", "icon": "person", "link": "06-mi-perfil.html", "matches": ["06-mi-perfil.html"]}
        ],
        "mobile_items": [
            {"label": "Dashboard", "icon": "dashboard", "link": "01-dashboard-ejecutivo.html", "matches": ["01-dashboard-ejecutivo.html"]},
            {"label": "Vinculación", "icon": "handshake", "link": "02-vinculacion-convenios.html", "matches": ["02-vinculacion-convenios.html"]},
            {"label": "Sectores", "icon": "factory", "link": "03-sectores-productivos.html", "matches": ["03-sectores-productivos.html"]},
            {"label": "Acreditación", "icon": "verified_user", "link": "04-reportes-acreditacion.html", "matches": ["04-reportes-acreditacion.html"]},
            {"label": "Perfil", "icon": "person", "link": "06-mi-perfil.html", "matches": ["06-mi-perfil.html"]}
        ],
        "screen_names": {
            "01-dashboard-ejecutivo.html": "Dashboard ejecutivo",
            "02-vinculacion-convenios.html": "Vinculación y convenios",
            "03-sectores-productivos.html": "Sectores productivos",
            "04-reportes-acreditacion.html": "Reportes de acreditación",
            "05-configuracion-global.html": "Configuración global",
            "06-mi-perfil.html": "Mi perfil"
        }
    }
}

def generate_header(role_cfg, filename, is_root=False):
    logo_path = "assets/logo_umb.png" if is_root else "../assets/logo_umb.png"
    screen_name = role_cfg["screen_names"].get(filename, "Detalle")
    notif_link = "08-transversales/04-centro-notificaciones.html" if is_root else "../08-transversales/04-centro-notificaciones.html"
    
    return f"""  <!-- APP BAR SUPERIOR CANÓNICA (64px) -->
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

    <!-- Derecha: Notificaciones + Avatar Usuario -->
    <div class="flex items-center gap-3 sm:gap-4">
      <a href="{notif_link}" class="relative p-2 rounded-full hover:bg-white/10 transition-colors text-white focus:outline-none focus:ring-2 focus:ring-white/40" title="Centro de notificaciones" aria-label="Notificaciones">
        <span class="material-symbols-outlined text-[24px]">notifications</span>
        <span class="absolute top-1.5 right-1.5 w-2.5 h-2.5 bg-umb-warning rounded-full ring-2 ring-umb-guinda"></span>
      </a>
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

def generate_sidebar(role_cfg, filename):
    items_html = []
    for item in role_cfg["sidebar_items"]:
        is_active = filename in item["matches"]
        if is_active:
            items_html.append(f"""          <a href="{item['link']}" class="bg-umb-guinda text-white font-semibold rounded-lg h-11 px-3.5 flex items-center gap-3 shadow-sm transition-colors" aria-current="page">
            <span class="material-symbols-outlined text-[20px] fill">{item['icon']}</span>
            <span class="text-sm">{item['label']}</span>
          </a>""")
        else:
            items_html.append(f"""          <a href="{item['link']}" class="text-umb-muted hover:bg-umb-surface hover:text-umb-carbon font-medium rounded-lg h-11 px-3.5 flex items-center gap-3 transition-colors">
            <span class="material-symbols-outlined text-[20px]">{item['icon']}</span>
            <span class="text-sm">{item['label']}</span>
          </a>""")

    nav_block = "\n".join(items_html)

    return f"""    <!-- SIDEBAR ESCRITORIO (260px) -->
    <aside class="w-[260px] fixed top-16 bottom-0 left-0 bg-white border-r border-umb-border z-40 hidden lg:flex flex-col justify-between py-4 px-3 shadow-sm" aria-label="Navegación lateral">
      <div>
        <!-- Ficha de usuario activa -->
        <div class="p-3 mb-3 border-b border-umb-border bg-gradient-to-b from-white to-umb-surface/50 rounded-lg">
          <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-full bg-umb-guinda text-white flex items-center justify-center font-bold text-sm ring-2 ring-umb-guinda/10">
              {role_cfg['user_initials']}
            </div>
            <div class="flex-1 min-w-0">
              <p class="text-xs font-bold text-umb-carbon truncate">{role_cfg['user_name']}</p>
              <p class="text-[11px] text-umb-outline truncate">{role_cfg['user_subtitle']}</p>
              <div class="mt-1">
                <span class="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-semibold bg-emerald-50 text-emerald-700 border border-emerald-200">
                  Activo
                </span>
              </div>
            </div>
          </div>
        </div>

        <!-- Navegación vertical -->
        <nav class="space-y-1" aria-label="Navegación principal">
{nav_block}
        </nav>
      </div>

      <!-- Pie de navegación del sidebar -->
      <div class="p-3 border-t border-umb-border text-[11px] text-umb-outline flex items-center justify-between">
        <span>Ciclo 26-27/1</span>
        <span class="flex items-center gap-1.5 text-emerald-700 font-medium">
          <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
          En línea
        </span>
      </div>
    </aside>"""

def generate_bottom_nav(role_cfg, filename):
    items_html = []
    for item in role_cfg["mobile_items"]:
        is_active = filename in item["matches"]
        if is_active:
            items_html.append(f"""    <a href="{item['link']}" class="flex flex-col items-center justify-center flex-1 py-1 text-umb-guinda" aria-current="page">
      <span class="material-symbols-outlined text-[22px] fill">{item['icon']}</span>
      <span class="text-[11px] font-semibold mt-0.5">{item['label']}</span>
    </a>""")
        else:
            items_html.append(f"""    <a href="{item['link']}" class="flex flex-col items-center justify-center flex-1 py-1 text-umb-outline hover:text-umb-carbon">
      <span class="material-symbols-outlined text-[22px]">{item['icon']}</span>
      <span class="text-[11px] font-medium mt-0.5">{item['label']}</span>
    </a>""")

    inner_block = "\n".join(items_html)

    return f"""  <!-- BOTTOM NAVIGATION MOBILE (< 1024px) -->
  <nav class="lg:hidden fixed bottom-0 left-0 right-0 h-16 bg-white border-t border-umb-border shadow-lg z-40 flex items-center justify-around px-2" aria-label="Navegación inferior móvil">
{inner_block}
  </nav>"""

def replace_legacy_data(content):
    # Company names
    content = content.replace("TechSol Solutions México S.A. de C.V.", "Universidad Mexiquense del Bicentenario · Dirección Académica")
    content = content.replace("TechSol Solutions México S.A. de C.V", "Universidad Mexiquense del Bicentenario · Dirección Académica")
    content = content.replace("TechSol Solutions México", "Universidad Mexiquense del Bicentenario · Dirección Académica")
    content = content.replace("TechSol Solutions", "Universidad Mexiquense del Bicentenario")
    content = content.replace("TechSol", "UMB Académica")

    # Person names
    content = content.replace("Valeria Reyes Montiel", "Jesús Andrés Mondragón Tenorio")
    content = content.replace("Valeria Reyes", "Jesús Andrés Mondragón")
    content = content.replace("Patricia Morales Velázquez", "Lic. Estefanía Yttesen Nava")
    content = content.replace("Dra. Patricia Morales", "Lic. Estefanía Yttesen")
    content = content.replace("Roberto Almanza Torres", "I.S.C. Leonardo Becerril Sánchez")
    content = content.replace("Ing. Roberto Almanza", "I.S.C. Leonardo Becerril")
    content = content.replace("Lic. Mariana Estrada Gómez", "Lic. Estefanía Yttesen Nava")
    content = content.replace("Lic. Mariana Estrada", "Lic. Estefanía Yttesen")
    content = content.replace("Carlos Mendoza Nava", "Cristofer Piña Rodríguez")
    content = content.replace("Carlos Mendoza Cruz", "Alan Fernando Sánchez Romero")
    content = content.replace("Carlos Mendoza", "Cristofer Piña")
    content = content.replace("Daniela Miranda Gómez", "Lizet Moreno Piña")
    content = content.replace("Daniela Miranda", "Lizet Moreno")
    content = content.replace("Jorge Luis Morales Ortiz", "Rodolfo Cruz Ibarra")
    content = content.replace("Jorge Luis Morales", "Rodolfo Cruz")
    content = content.replace("Andrea Lizbeth Peña Cruz", "Sofía Cortez García")
    content = content.replace("Andrea Lizbeth Peña", "Sofía Cortez")
    content = content.replace("David Alanís Navarrete", "Marco Antonio García Cruz")
    content = content.replace("David Alanís", "Marco Antonio García")
    content = content.replace("Mariana Cruz Garduño", "Daniel Benítez")

    # External logo URLs
    content = re.sub(r'https://lh3\.googleusercontent\.com/aida-public/[A-Za-z0-9_-]+', '../assets/logo_umb.png', content)

    # Color class tokenization
    color_replacements = [
        ("bg-[#681B2B]", "bg-umb-guinda"),
        ("bg-[#4F1420]", "bg-umb-guinda-dark"),
        ("bg-[#9E773B]", "bg-umb-dorado"),
        ("bg-[#7F5E2B]", "bg-umb-dorado-dark"),
        ("bg-[#FEF3C7]", "bg-umb-dorado-light"),
        ("bg-[#F4F5F7]", "bg-umb-surface"),
        ("bg-[#1A1A1A]", "bg-umb-carbon"),
        ("bg-[#544244]", "bg-umb-muted"),
        ("bg-[#877273]", "bg-umb-outline"),
        ("bg-[#E2E8F0]", "bg-umb-border"),
        ("text-[#681B2B]", "text-umb-guinda"),
        ("text-[#4F1420]", "text-umb-guinda-dark"),
        ("text-[#9E773B]", "text-umb-dorado"),
        ("text-[#7F5E2B]", "text-umb-dorado-dark"),
        ("text-[#1A1A1A]", "text-umb-carbon"),
        ("text-[#544244]", "text-umb-muted"),
        ("text-[#877273]", "text-umb-outline"),
        ("border-[#681B2B]", "border-umb-guinda"),
        ("border-[#4F1420]", "border-umb-guinda-dark"),
        ("border-[#9E773B]", "border-umb-dorado"),
        ("border-[#E2E8F0]", "border-umb-border"),
        ("ring-[#681B2B]", "ring-umb-guinda"),
        ("ring-[#9E773B]", "ring-umb-dorado"),
        ("ring-[#4F1420]", "ring-umb-guinda-dark"),
        ("fill-[#681B2B]", "fill-umb-guinda"),
        ("fill-[#9E773B]", "fill-umb-dorado"),
        ("focus:ring-[#681B2B]", "focus:ring-umb-guinda"),
        ("focus:border-[#681B2B]", "focus:border-umb-guinda"),
        ("selection:bg-[#681B2B]", "selection:bg-umb-guinda"),
        ("selection:bg-brand-guinda", "selection:bg-umb-guinda"),
        ("bg-brand-guinda", "bg-umb-guinda"),
        ("text-brand-guinda", "text-umb-guinda"),
        ("border-brand-guinda", "border-umb-guinda"),
        ("bg-brand-dorado", "bg-umb-dorado"),
        ("text-brand-dorado", "text-umb-dorado"),
    ]

    for old_c, new_c in color_replacements:
        content = content.replace(old_c, new_c)

    return content

print("Standardize library loaded successfully.")
