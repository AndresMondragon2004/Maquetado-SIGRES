import os

def build_index_html(prefix_type="root"):
    if prefix_type == "root":
        prefix = "sigres-umb/"
        logo_path = "sigres-umb/assets/logo_umb.png"
    elif prefix_type == "sigres":
        prefix = ""
        logo_path = "assets/logo_umb.png"
    elif prefix_type == "subfolder":
        prefix = "../"
        logo_path = "../assets/logo_umb.png"

    modules_data = [
        {
            "id": "01-autenticacion",
            "num": "01",
            "title": "Autenticación y Acceso",
            "role": "Público / Aspirante / Todos los roles",
            "persona": "Múltiples accesos",
            "badge": "6 pantallas",
            "badge_color": "bg-slate-100 text-slate-700 border-slate-200",
            "icon": "lock",
            "desc": "Flujos de inicio de sesión institucional, verificación de enlace por correo, registro de estudiante, acceso denegado, recuperación y onboarding interactivo.",
            "main_link": f"{prefix}01-autenticacion/01-login.html",
            "screens": [
                {"name": "01 · Iniciar sesión", "file": f"{prefix}01-autenticacion/01-login.html", "icon": "login"},
                {"name": "02 · Verificación de enlace", "file": f"{prefix}01-autenticacion/02-verificacion-enlace.html", "icon": "mark_email_read"},
                {"name": "03 · Registro de estudiante", "file": f"{prefix}01-autenticacion/03-registro-estudiante.html", "icon": "person_add"},
                {"name": "04 · Acceso denegado", "file": f"{prefix}01-autenticacion/04-acceso-denegado.html", "icon": "block"},
                {"name": "05 · Recuperar acceso", "file": f"{prefix}01-autenticacion/05-recuperar-acceso.html", "icon": "lock_reset"},
                {"name": "06 · Onboarding interactivo", "file": f"{prefix}01-autenticacion/06-onboarding.html", "icon": "explore"}
            ]
        },
        {
            "id": "02-estudiante",
            "num": "02",
            "title": "Portal del Estudiante",
            "role": "Estudiante Residente",
            "persona": "Jesús Andrés Mondragón Tenorio (JM · 13220024 · ISC)",
            "badge": "14 pantallas",
            "badge_color": "bg-emerald-50 text-emerald-700 border-emerald-200",
            "icon": "school",
            "desc": "Gestión integral del residente: consulta de expediente, registro de empresa institucional, bitácoras semanales, cronograma, seguimiento de 640 horas e informes.",
            "main_link": f"{prefix}02-estudiante/01-dashboard.html",
            "screens": [
                {"name": "01 · Dashboard principal", "file": f"{prefix}02-estudiante/01-dashboard.html", "icon": "dashboard"},
                {"name": "02 · Mi expediente", "file": f"{prefix}02-estudiante/02-mi-expediente.html", "icon": "folder"},
                {"name": "03 · Buscar empresa", "file": f"{prefix}02-estudiante/03-buscar-empresa.html", "icon": "search"},
                {"name": "04 · Registrar empresa", "file": f"{prefix}02-estudiante/04-registrar-empresa.html", "icon": "domain_add"},
                {"name": "05 · Estatus validación empresa", "file": f"{prefix}02-estudiante/05-estatus-validacion-empresa.html", "icon": "verified"},
                {"name": "06 · Solicitud de residencia", "file": f"{prefix}02-estudiante/06-solicitud-residencia.html", "icon": "assignment"},
                {"name": "07 · Carta de presentación", "file": f"{prefix}02-estudiante/07-carta-presentacion-generada.html", "icon": "description"},
                {"name": "08 · Mis bitácoras", "file": f"{prefix}02-estudiante/08-mis-bitacoras.html", "icon": "menu_book"},
                {"name": "09 · Nueva bitácora", "file": f"{prefix}02-estudiante/09-nueva-bitacora.html", "icon": "post_add"},
                {"name": "10 · Detalle de bitácora", "file": f"{prefix}02-estudiante/10-detalle-bitacora.html", "icon": "article"},
                {"name": "11 · Mi progreso de horas", "file": f"{prefix}02-estudiante/11-mi-progreso.html", "icon": "hourglass_top"},
                {"name": "12 · Cronograma de actividades", "file": f"{prefix}02-estudiante/12-cronograma.html", "icon": "calendar_month"},
                {"name": "13 · Mis informes (Parcial/Final)", "file": f"{prefix}02-estudiante/13-mis-informes.html", "icon": "fact_check"},
                {"name": "14 · Mi perfil de estudiante", "file": f"{prefix}02-estudiante/14-mi-perfil.html", "icon": "person"}
            ]
        },
        {
            "id": "03-asesor-interno",
            "num": "03",
            "title": "Asesor Interno (Docente)",
            "role": "Docente Asesor Institucional",
            "persona": "I.S.C. Leonardo Becerril Sánchez (LB · ISC)",
            "badge": "8 pantallas",
            "badge_color": "bg-blue-50 text-blue-700 border-blue-200",
            "icon": "psychology",
            "desc": "Supervisión académica, seguimiento individual de alumnos asignados, registro de sesiones de asesoría y rúbricas de evaluación parcial y final.",
            "main_link": f"{prefix}03-asesor-interno/01-dashboard.html",
            "screens": [
                {"name": "01 · Dashboard de asesor", "file": f"{prefix}03-asesor-interno/01-dashboard.html", "icon": "dashboard"},
                {"name": "02 · Mis alumnos asignados", "file": f"{prefix}03-asesor-interno/02-mis-alumnos.html", "icon": "group"},
                {"name": "03 · Detalle y avance de alumno", "file": f"{prefix}03-asesor-interno/03-detalle-alumno.html", "icon": "person_search"},
                {"name": "04 · Registrar asesoría", "file": f"{prefix}03-asesor-interno/04-registrar-asesoria.html", "icon": "assignment"},
                {"name": "05 · Revisar bitácoras y entregas", "file": f"{prefix}03-asesor-interno/05-revisar-bitacoras.html", "icon": "fact_check"},
                {"name": "06 · Evaluar informe parcial", "file": f"{prefix}03-asesor-interno/06-evaluar-informe-parcial.html", "icon": "rate_review"},
                {"name": "07 · Evaluar informe final", "file": f"{prefix}03-asesor-interno/07-evaluar-informe-final.html", "icon": "grade"},
                {"name": "08 · Mi perfil docente", "file": f"{prefix}03-asesor-interno/08-mi-perfil.html", "icon": "person"}
            ]
        },
        {
            "id": "04-asesor-externo",
            "num": "04",
            "title": "Asesor Externo (Empresa)",
            "role": "Director Académico / Asesor Empresa",
            "persona": "Mtro. Armando Alcalde Martínez (AA · UMB)",
            "badge": "6 pantallas",
            "badge_color": "bg-amber-50 text-amber-700 border-amber-200",
            "icon": "business_center",
            "desc": "Validación empresarial de actividades reportadas en bitácoras, evaluación de desempeño en sede y control de historial de firmas.",
            "main_link": f"{prefix}04-asesor-externo/01-dashboard.html",
            "screens": [
                {"name": "01 · Dashboard asesor externo", "file": f"{prefix}04-asesor-externo/01-dashboard.html", "icon": "dashboard"},
                {"name": "02 · Bitácoras por validar", "file": f"{prefix}04-asesor-externo/02-bitacoras-por-validar.html", "icon": "pending_actions"},
                {"name": "03 · Detalle y validación de bitácora", "file": f"{prefix}04-asesor-externo/03-detalle-bitacora.html", "icon": "task_alt"},
                {"name": "04 · Residentes asignados", "file": f"{prefix}04-asesor-externo/04-residentes-asignados.html", "icon": "badge"},
                {"name": "05 · Historial de validaciones", "file": f"{prefix}04-asesor-externo/05-historial-validaciones.html", "icon": "history"},
                {"name": "06 · Mi perfil de asesor externo", "file": f"{prefix}04-asesor-externo/06-mi-perfil.html", "icon": "person"}
            ]
        },
        {
            "id": "05-control-escolar",
            "num": "05",
            "title": "Control Escolar",
            "role": "Responsable de Control Escolar",
            "persona": "Lic. Estefanía Yttesen Nava (EY)",
            "badge": "9 pantallas",
            "badge_color": "bg-purple-50 text-purple-700 border-purple-200",
            "icon": "inventory_2",
            "desc": "Recepción y validación de expedientes físicos/digitales, emisión de cartas oficiales de presentación, catálogo de empresas y reportes escolares.",
            "main_link": f"{prefix}05-control-escolar/01-dashboard.html",
            "screens": [
                {"name": "01 · Dashboard de control escolar", "file": f"{prefix}05-control-escolar/01-dashboard.html", "icon": "dashboard"},
                {"name": "02 · Bandeja de expedientes", "file": f"{prefix}05-control-escolar/02-bandeja-expedientes.html", "icon": "folder_shared"},
                {"name": "03 · Detalle de expediente", "file": f"{prefix}05-control-escolar/03-detalle-expediente.html", "icon": "folder_open"},
                {"name": "04 · Validar documentos", "file": f"{prefix}05-control-escolar/04-validar-documentos.html", "icon": "verified"},
                {"name": "05 · Generar cartas oficiales", "file": f"{prefix}05-control-escolar/05-generar-carta.html", "icon": "print"},
                {"name": "06 · Catálogo de empresas", "file": f"{prefix}05-control-escolar/06-catalogo-empresas.html", "icon": "domain"},
                {"name": "07 · Validar empresas nuevas", "file": f"{prefix}05-control-escolar/07-validar-empresas-nuevas.html", "icon": "add_business"},
                {"name": "08 · Reportes de control escolar", "file": f"{prefix}05-control-escolar/08-reportes.html", "icon": "analytics"},
                {"name": "09 · Mi perfil de control escolar", "file": f"{prefix}05-control-escolar/09-mi-perfil.html", "icon": "person"}
            ]
        },
        {
            "id": "06-coordinacion",
            "num": "06",
            "title": "Coordinación de Carrera / UES",
            "role": "Coordinador de UES",
            "persona": "Mtro. Luis Ramón Vega Ramírez (LV)",
            "badge": "7 pantallas",
            "badge_color": "bg-rose-50 text-rose-700 border-rose-200",
            "icon": "hub",
            "desc": "Supervisión global de cohortes por carrera, semáforo preventivo de riesgos, gestión de contingencias, reportes ejecutivos y emisión de alertas.",
            "main_link": f"{prefix}06-coordinacion/01-dashboard-monitoreo.html",
            "screens": [
                {"name": "01 · Dashboard de monitoreo general", "file": f"{prefix}06-coordinacion/01-dashboard-monitoreo.html", "icon": "monitoring"},
                {"name": "02 · Cohortes por carrera (ISC, IIAS, LCONT)", "file": f"{prefix}06-coordinacion/02-cohortes-carreras.html", "icon": "school"},
                {"name": "03 · Supervisión de riesgos (Semáforo)", "file": f"{prefix}06-coordinacion/03-supervision-riesgo.html", "icon": "warning"},
                {"name": "04 · Gestión de contingencias", "file": f"{prefix}06-coordinacion/04-contingencias.html", "icon": "support"},
                {"name": "06 · Reportes ejecutivos de coordinación", "file": f"{prefix}06-coordinacion/06-reportes-ejecutivos.html", "icon": "summarize"},
                {"name": "07 · Centro de notificaciones institucional", "file": f"{prefix}06-coordinacion/07-notificaciones.html", "icon": "campaign"},
                {"name": "08 · Mi perfil de coordinador", "file": f"{prefix}06-coordinacion/08-mi-perfil.html", "icon": "person"}
            ]
        },
        {
            "id": "07-direccion",
            "num": "07",
            "title": "Dirección Académica UMB",
            "role": "Director Académico",
            "persona": "Mtro. Armando Alcalde Martínez (AA)",
            "badge": "6 pantallas",
            "badge_color": "bg-amber-100 text-amber-900 border-amber-300",
            "icon": "account_balance",
            "desc": "Métricas estratégicas de residencias a nivel estatal, convenios de vinculación institucional, análisis de sectores productivos y acreditación.",
            "main_link": f"{prefix}07-direccion/01-dashboard-ejecutivo.html",
            "screens": [
                {"name": "01 · Dashboard ejecutivo directivo", "file": f"{prefix}07-direccion/01-dashboard-ejecutivo.html", "icon": "dashboard"},
                {"name": "02 · Vinculación y convenios", "file": f"{prefix}07-direccion/02-vinculacion-convenios.html", "icon": "handshake"},
                {"name": "03 · Sectores productivos", "file": f"{prefix}07-direccion/03-sectores-productivos.html", "icon": "factory"},
                {"name": "04 · Reportes para acreditación", "file": f"{prefix}07-direccion/04-reportes-acreditacion.html", "icon": "verified_user"},
                {"name": "05 · Configuración global del ciclo", "file": f"{prefix}07-direccion/05-configuracion-global.html", "icon": "settings"},
                {"name": "06 · Mi perfil de director", "file": f"{prefix}07-direccion/06-mi-perfil.html", "icon": "person"}
            ]
        },
        {
            "id": "08-transversales",
            "num": "08",
            "title": "Componentes Transversales",
            "role": "Sistema Global / UI Library",
            "persona": "Componentes compartidos",
            "badge": "13 pantallas",
            "badge_color": "bg-cyan-50 text-cyan-700 border-cyan-200",
            "icon": "widgets",
            "desc": "Biblioteca de estados de interfaz compartidos: centro de notificaciones, modales de confirmación/eliminación, toasts, estados vacíos, skeletons y páginas de error.",
            "main_link": f"{prefix}08-transversales/04-centro-notificaciones.html",
            "screens": [
                {"name": "01 · Modal de confirmación", "file": f"{prefix}08-transversales/01-modal-confirmacion.html", "icon": "check_circle"},
                {"name": "02 · Modal de eliminación", "file": f"{prefix}08-transversales/02-modal-eliminacion.html", "icon": "delete"},
                {"name": "03 · Toast y alertas flotantes", "file": f"{prefix}08-transversales/03-toast-notificacion.html", "icon": "notifications_active"},
                {"name": "04 · Centro de notificaciones desplegable", "file": f"{prefix}08-transversales/04-centro-notificaciones.html", "icon": "notifications"},
                {"name": "05 · Estados vacíos (Empty States)", "file": f"{prefix}08-transversales/05-estado-vacio.html", "icon": "inbox"},
                {"name": "06 · Skeleton screens (Carga diferida)", "file": f"{prefix}08-transversales/06-skeleton-screens.html", "icon": "hourglass_empty"},
                {"name": "07 · Estado sin conexión (Offline)", "file": f"{prefix}08-transversales/07-estado-sin-conexion.html", "icon": "wifi_off"},
                {"name": "08 · Barra de sincronización", "file": f"{prefix}08-transversales/08-barra-sincronizacion.html", "icon": "sync"},
                {"name": "09 · Error 404 - Página no encontrada", "file": f"{prefix}08-transversales/09-pagina-404.html", "icon": "search_off"},
                {"name": "10 · Error 500 - Error del servidor", "file": f"{prefix}08-transversales/10-pagina-500.html", "icon": "error"},
                {"name": "11 · Modal de sesión expirada", "file": f"{prefix}08-transversales/11-modal-sesion-expirada.html", "icon": "timer_off"},
                {"name": "12 · Búsqueda global (Cmd+K)", "file": f"{prefix}08-transversales/12-busqueda-global.html", "icon": "manage_search"},
                {"name": "13 · Error 403 - Acceso restringido", "file": f"{prefix}08-transversales/13-pagina-403.html", "icon": "lock"}
            ]
        }
    ]

    module_cards_html = []
    for m in modules_data:
        screen_items_html = []
        for s in m["screens"]:
            screen_items_html.append(f"""              <li class="screen-item">
                <a href="{s['file']}" class="flex items-center justify-between p-2 rounded-lg hover:bg-umb-guinda-light hover:text-umb-guinda text-umb-carbon text-xs font-medium transition-all group/link border border-transparent hover:border-umb-guinda/20">
                  <span class="flex items-center gap-2 truncate">
                    <span class="material-symbols-outlined text-[16px] text-umb-outline group-hover/link:text-umb-guinda">{s['icon']}</span>
                    <span class="truncate">{s['name']}</span>
                  </span>
                  <span class="material-symbols-outlined text-[14px] text-umb-outline/60 group-hover/link:text-umb-guinda group-hover/link:translate-x-0.5 transition-transform">arrow_forward</span>
                </a>
              </li>""")
        
        screens_joined = "\n".join(screen_items_html)

        card = f"""        <!-- TARJETA DE MÓDULO {m['num']}: {m['title']} -->
        <div class="module-card bg-white rounded-xl border border-umb-border shadow-card hover:shadow-card-hover transition-all flex flex-col justify-between overflow-hidden group" data-module="{m['id']}" data-title="{m['title'].lower()}" data-role="{m['role'].lower()}" data-persona="{m['persona'].lower()}">
          
          <!-- Encabezado de Tarjeta -->
          <div class="p-6 border-b border-umb-border bg-gradient-to-b from-white to-umb-surface/40">
            <div class="flex items-start justify-between gap-3 mb-3">
              <div class="flex items-center gap-3">
                <div class="w-11 h-11 rounded-xl bg-umb-guinda text-white flex items-center justify-center font-bold text-lg shadow-sm">
                  <span class="material-symbols-outlined text-[24px]">{m['icon']}</span>
                </div>
                <div>
                  <span class="text-[11px] font-bold tracking-widest text-umb-dorado uppercase">Módulo {m['num']}</span>
                  <h3 class="text-base font-bold text-umb-carbon tracking-tight">{m['title']}</h3>
                </div>
              </div>
              <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold border {m['badge_color']}">
                {m['badge']}
              </span>
            </div>

            <p class="text-xs text-umb-muted leading-relaxed mb-3">{m['desc']}</p>
            
            <div class="p-2.5 rounded-lg bg-umb-surface/80 border border-umb-border/60 flex items-center gap-2">
              <span class="material-symbols-outlined text-[16px] text-umb-guinda">person</span>
              <span class="text-[11px] font-medium text-umb-carbon truncate"><strong class="text-umb-muted">Persona:</strong> {m['persona']}</span>
            </div>
          </div>

          <!-- Listado Desplegable de Pantallas -->
          <div class="p-4 flex-1">
            <div class="text-[11px] font-bold text-umb-outline uppercase tracking-wider mb-2 px-1 flex items-center justify-between">
              <span>Pantallas del módulo</span>
              <span class="text-[10px] lowercase font-normal">{len(m['screens'])} rutas</span>
            </div>
            <ul class="space-y-1">
{screens_joined}
            </ul>
          </div>

          <!-- Pie con Botón de Inicio Rápido -->
          <div class="p-4 bg-umb-surface/50 border-t border-umb-border">
            <a href="{m['main_link']}" class="w-full h-10 px-4 rounded-lg bg-umb-guinda hover:bg-umb-guinda-dark text-white font-semibold text-xs transition-all shadow-sm flex items-center justify-center gap-2 group/btn">
              <span>Abrir flujo del módulo</span>
              <span class="material-symbols-outlined text-[16px] group-hover/btn:translate-x-1 transition-transform">login</span>
            </a>
          </div>
        </div>"""
        module_cards_html.append(card)

    all_cards = "\n\n".join(module_cards_html)

    return f"""<!DOCTYPE html>
<html lang="es" class="h-full bg-umb-surface">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SIGRES-UMB · Portal Central de Navegación y Auditoría de Módulos</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            umb: {{
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
            }}
          }},
          fontFamily: {{
            sans: ['Inter', 'sans-serif']
          }},
          borderRadius: {{
            card: '8px',
            badge: '9999px',
            modal: '12px'
          }},
          boxShadow: {{
            card: '0 1px 3px 0 rgba(0, 0, 0, 0.06), 0 1px 2px -1px rgba(0, 0, 0, 0.04)',
            'card-hover': '0 10px 15px -3px rgba(104, 27, 43, 0.08), 0 4px 6px -4px rgba(0, 0, 0, 0.04)',
            modal: '0 20px 25px -5px rgba(0, 0, 0, 0.15), 0 8px 10px -6px rgba(0, 0, 0, 0.1)'
          }}
        }}
      }}
    }}
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
  <style>
    .material-symbols-outlined {{
      font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
      display: inline-block;
      vertical-align: middle;
      line-height: 1;
    }}
    .material-symbols-outlined.fill {{
      font-variation-settings: 'FILL' 1, 'wght' 400, 'GRAD' 0, 'opsz' 24;
    }}
    ::-webkit-scrollbar {{
      width: 6px;
      height: 6px;
    }}
    ::-webkit-scrollbar-track {{
      background: #F4F5F7;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #CBD5E1;
      border-radius: 9999px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #94A3B8;
    }}
  </style>
</head>
<body class="min-h-full bg-umb-surface text-umb-carbon antialiased flex flex-col selection:bg-umb-guinda selection:text-white">

  <!-- ================= HERO HEADER INSTITUCIONAL ================= -->
  <header class="bg-gradient-to-r from-umb-guinda via-[#521422] to-umb-guinda-dark text-white border-b-4 border-umb-dorado shadow-2xl relative overflow-hidden">
    <!-- Decoración sutil de fondo -->
    <div class="absolute -right-20 -bottom-20 w-96 h-96 rounded-full bg-umb-dorado/20 pointer-events-none blur-3xl"></div>
    <div class="absolute -left-20 -top-20 w-96 h-96 rounded-full bg-white/5 pointer-events-none blur-2xl"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 md:py-12 relative z-10">
      <div class="flex flex-col md:flex-row items-center justify-between gap-6">
        
        <!-- Logo UMB + Títulos -->
        <div class="flex items-center gap-5 text-center md:text-left">
          <div class="h-20 sm:h-24 w-auto bg-white p-2 rounded-2xl flex items-center justify-center shadow-xl backdrop-blur-md flex-shrink-0">
            <img src="{logo_path}" alt="Logo UMB" class="h-16 sm:h-20 w-auto object-contain">
          </div>
          <div>
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/10 text-amber-200 border border-white/20 text-xs font-semibold uppercase tracking-wider mb-2">
              <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
              Prototipo Estandarizado · Ciclo 26-27/1
            </div>
            <h1 class="text-2xl sm:text-4xl font-extrabold tracking-tight text-white leading-tight">
              SIGRES-UMB
            </h1>
            <p class="text-sm sm:text-base text-white/90 font-medium mt-1">
              Sistema integral para la gestión de residencias profesionales
            </p>
            <p class="text-xs text-white/70 mt-0.5">
              Universidad Mexiquense del Bicentenario · Unidad de Estudios Superiores San José del Rincón
            </p>
          </div>
        </div>

        <!-- Métricas Rápidas del Prototipo -->
        <div class="grid grid-cols-3 gap-3 bg-black/20 p-3 rounded-xl border border-white/10 backdrop-blur-md">
          <div class="text-center px-3 py-1">
            <div class="text-2xl font-bold text-amber-300">71</div>
            <div class="text-[11px] text-white/80 font-medium">Pantallas</div>
          </div>
          <div class="text-center px-3 py-1 border-x border-white/10">
            <div class="text-2xl font-bold text-white">9</div>
            <div class="text-[11px] text-white/80 font-medium">Módulos</div>
          </div>
          <div class="text-center px-3 py-1">
            <div class="text-2xl font-bold text-emerald-400">100%</div>
            <div class="text-[11px] text-white/80 font-medium">Estandarizado</div>
          </div>
        </div>

      </div>
    </div>
  </header>

  <!-- ================= CONTROLES Y BUSCADOR RÁPIDO ================= -->
  <section class="max-w-7xl mx-auto w-full px-4 sm:px-6 lg:px-8 -mt-6 relative z-20">
    <div class="bg-white rounded-xl shadow-lg border border-umb-border p-4 flex flex-col md:flex-row items-center justify-between gap-4">
      
      <!-- Barra de búsqueda instantánea -->
      <div class="relative w-full md:w-96">
        <span class="material-symbols-outlined absolute left-3.5 top-1/2 -translate-y-1/2 text-umb-outline text-[20px]">search</span>
        <input type="text" id="searchInput" placeholder="Buscar módulo, pantalla o rol..." class="w-full h-11 pl-10 pr-4 rounded-lg bg-umb-surface border border-umb-border text-umb-carbon text-sm placeholder:text-umb-outline focus:outline-none focus:ring-2 focus:ring-umb-guinda transition-all">
      </div>

      <!-- Filtros Rápidos de Rol -->
      <div class="flex items-center gap-1.5 overflow-x-auto w-full md:w-auto pb-1 md:pb-0" id="filterButtons">
        <button type="button" class="filter-btn active h-9 px-3.5 rounded-lg bg-umb-guinda text-white text-xs font-semibold shadow-sm transition-all" data-filter="all">Todos (9)</button>
        <button type="button" class="filter-btn h-9 px-3.5 rounded-lg bg-umb-surface hover:bg-umb-border text-umb-carbon text-xs font-medium transition-all" data-filter="02-estudiante">Estudiante</button>
        <button type="button" class="filter-btn h-9 px-3.5 rounded-lg bg-umb-surface hover:bg-umb-border text-umb-carbon text-xs font-medium transition-all" data-filter="03-asesor-interno">Asesor Interno</button>
        <button type="button" class="filter-btn h-9 px-3.5 rounded-lg bg-umb-surface hover:bg-umb-border text-umb-carbon text-xs font-medium transition-all" data-filter="04-asesor-externo">Asesor Externo</button>
        <button type="button" class="filter-btn h-9 px-3.5 rounded-lg bg-umb-surface hover:bg-umb-border text-umb-carbon text-xs font-medium transition-all" data-filter="05-control-escolar">Control Escolar</button>
        <button type="button" class="filter-btn h-9 px-3.5 rounded-lg bg-umb-surface hover:bg-umb-border text-umb-carbon text-xs font-medium transition-all" data-filter="06-coordinacion">Coordinación</button>
        <button type="button" class="filter-btn h-9 px-3.5 rounded-lg bg-umb-surface hover:bg-umb-border text-umb-carbon text-xs font-medium transition-all" data-filter="07-direccion">Dirección</button>
      </div>

    </div>
  </section>

  <!-- ================= CONTENEDOR PRINCIPAL DE MÓDULOS ================= -->
  <main class="max-w-7xl mx-auto w-full px-4 sm:px-6 lg:px-8 py-10 flex-1">
    
    <!-- GUÍA DE FLUJO RECOMENDADO -->
    <div class="mb-10 bg-gradient-to-r from-white via-umb-guinda-light/40 to-white rounded-xl border border-umb-dorado/30 p-6 shadow-card">
      <div class="flex items-center gap-3 mb-3">
        <span class="material-symbols-outlined text-umb-guinda text-[24px]">route</span>
        <h2 class="text-base font-bold text-umb-carbon">Flujo Integral Recomendado para la Revisión</h2>
      </div>
      <p class="text-xs text-umb-muted mb-4">
        Puedes recorrer el ciclo de vida completo de residencias profesionales en orden cronológico siguiendo estos pasos:
      </p>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-6 gap-3">
        <a href="{prefix}01-autenticacion/01-login.html" class="p-3 rounded-lg bg-white border border-umb-border hover:border-umb-guinda hover:shadow-md transition-all text-left group">
          <div class="text-[10px] font-bold text-umb-dorado uppercase mb-1">Paso 1</div>
          <div class="text-xs font-bold text-umb-carbon group-hover:text-umb-guinda truncate">Autenticación</div>
          <div class="text-[11px] text-umb-outline mt-0.5">Login y registro</div>
        </a>
        <a href="{prefix}02-estudiante/01-dashboard.html" class="p-3 rounded-lg bg-white border border-umb-border hover:border-umb-guinda hover:shadow-md transition-all text-left group">
          <div class="text-[10px] font-bold text-umb-dorado uppercase mb-1">Paso 2</div>
          <div class="text-xs font-bold text-umb-carbon group-hover:text-umb-guinda truncate">Estudiante</div>
          <div class="text-[11px] text-umb-outline mt-0.5">Expediente y bitácoras</div>
        </a>
        <a href="{prefix}03-asesor-interno/01-dashboard.html" class="p-3 rounded-lg bg-white border border-umb-border hover:border-umb-guinda hover:shadow-md transition-all text-left group">
          <div class="text-[10px] font-bold text-umb-dorado uppercase mb-1">Paso 3</div>
          <div class="text-xs font-bold text-umb-carbon group-hover:text-umb-guinda truncate">Asesor Interno</div>
          <div class="text-[11px] text-umb-outline mt-0.5">Asesorías y rúbricas</div>
        </a>
        <a href="{prefix}04-asesor-externo/01-dashboard.html" class="p-3 rounded-lg bg-white border border-umb-border hover:border-umb-guinda hover:shadow-md transition-all text-left group">
          <div class="text-[10px] font-bold text-umb-dorado uppercase mb-1">Paso 4</div>
          <div class="text-xs font-bold text-umb-carbon group-hover:text-umb-guinda truncate">Asesor Externo</div>
          <div class="text-[11px] text-umb-outline mt-0.5">Validación en empresa</div>
        </a>
        <a href="{prefix}05-control-escolar/01-dashboard.html" class="p-3 rounded-lg bg-white border border-umb-border hover:border-umb-guinda hover:shadow-md transition-all text-left group">
          <div class="text-[10px] font-bold text-umb-dorado uppercase mb-1">Paso 5</div>
          <div class="text-xs font-bold text-umb-carbon group-hover:text-umb-guinda truncate">Control Escolar</div>
          <div class="text-[11px] text-umb-outline mt-0.5">Cartas y expedientes</div>
        </a>
        <a href="{prefix}06-coordinacion/01-dashboard-monitoreo.html" class="p-3 rounded-lg bg-white border border-umb-border hover:border-umb-guinda hover:shadow-md transition-all text-left group">
          <div class="text-[10px] font-bold text-umb-dorado uppercase mb-1">Paso 6</div>
          <div class="text-xs font-bold text-umb-carbon group-hover:text-umb-guinda truncate">Coordinación/Dir.</div>
          <div class="text-[11px] text-umb-outline mt-0.5">Monitoreo y firmas</div>
        </a>
      </div>
    </div>

    <!-- GRID DE MÓDULOS -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6" id="modulesGrid">
{all_cards}
    </div>

  </main>

  <!-- ================= PIE DE PÁGINA ================= -->
  <footer class="pt-8 pb-8 text-center text-[12px] text-umb-outline border-t border-umb-border bg-white mt-12 space-y-1">
    <p class="font-medium text-umb-carbon">SIGRES-UMB — Sistema integral para la gestión de residencias profesionales</p>
    <p>Universidad Mexiquense del Bicentenario · Unidad de Estudios Superiores San José del Rincón · Ciclo 26-27/1</p>
    <p class="text-[11px] text-umb-outline/80 mt-2">Maquetado estandarizado al 100% · Tokens oficiales UMB</p>
  </footer>

  <!-- ================= SCRIPT DE BÚSQUEDA Y FILTRADO ================= -->
  <script>
    const searchInput = document.getElementById('searchInput');
    const filterButtons = document.querySelectorAll('.filter-btn');
    const moduleCards = document.querySelectorAll('.module-card');

    let currentFilter = 'all';

    function filterContent() {{
      const query = searchInput.value.toLowerCase().trim();

      moduleCards.forEach(card => {{
        const modId = card.getAttribute('data-module');
        const title = card.getAttribute('data-title');
        const role = card.getAttribute('data-role');
        const persona = card.getAttribute('data-persona');
        const textContent = card.innerText.toLowerCase();

        const matchesFilter = (currentFilter === 'all' || modId === currentFilter);
        const matchesQuery = (
          query === '' || 
          title.includes(query) || 
          role.includes(query) || 
          persona.includes(query) || 
          textContent.includes(query)
        );

        if (matchesFilter && matchesQuery) {{
          card.style.display = 'flex';
        }} else {{
          card.style.display = 'none';
        }}
      }});
    }}

    searchInput.addEventListener('input', filterContent);

    filterButtons.forEach(btn => {{
      btn.addEventListener('click', () => {{
        filterButtons.forEach(b => {{
          b.classList.remove('bg-umb-guinda', 'text-white', 'font-semibold', 'shadow-sm');
          b.classList.add('bg-umb-surface', 'text-umb-carbon', 'font-medium');
        }});
        btn.classList.remove('bg-umb-surface', 'text-umb-carbon', 'font-medium');
        btn.classList.add('bg-umb-guinda', 'text-white', 'font-semibold', 'shadow-sm');

        currentFilter = btn.getAttribute('data-filter');
        filterContent();
      }});
    }});
  </script>

</body>
</html>"""

if __name__ == "__main__":
    root_index = build_index_html(prefix_type="root")
    with open(r"c:\Users\Pc\Downloads\Maquetado - Residencia\respaldo-pre-estandarizacion-2026-09-17\index.html", "w", encoding="utf-8") as f:
        f.write(root_index)

    sigres_index = build_index_html(prefix_type="sigres")
    with open(r"c:\Users\Pc\Downloads\Maquetado - Residencia\respaldo-pre-estandarizacion-2026-09-17\sigres-umb\index.html", "w", encoding="utf-8") as f:
        f.write(sigres_index)

    subfolder_index = build_index_html(prefix_type="subfolder")
    with open(r"c:\Users\Pc\Downloads\Maquetado - Residencia\respaldo-pre-estandarizacion-2026-09-17\sigres-umb\00-portal\index.html", "w", encoding="utf-8") as f:
        f.write(subfolder_index)

    print("Index files created successfully!")
