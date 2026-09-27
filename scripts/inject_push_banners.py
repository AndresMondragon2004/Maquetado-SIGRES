import os
import re
import glob

PUSH_CONFIGS = {
    "02-estudiante": {
        "banner_bg": "bg-emerald-50 border-emerald-200 text-emerald-900",
        "icon": "campaign",
        "icon_color": "text-emerald-700 bg-white border border-emerald-200",
        "tag": "Notificación Push del Sistema",
        "tag_badge": "bg-emerald-100 text-emerald-800 border-emerald-300",
        "title": "¡Tu anteproyecto de residencia ha sido avalado con éxito!",
        "desc": "El Asesor Interno (I.S.C. Leonardo Becerril Sánchez) ha evaluado y avalado formalmente tu anteproyecto de residencia en Universidad Mexiquense del Bicentenario · Dirección Académica. Tu estatus actual es <strong>Residencia activa</strong>.",
        "btn_text": "Ver dictamen oficial",
        "modal_title": "Dictamen de Aprobación de Anteproyecto",
        "modal_icon": "verified",
        "modal_icon_color": "text-emerald-700 bg-emerald-100",
        "modal_content": """
          <div class="space-y-4 text-xs text-umb-carbon">
            <div class="p-3.5 rounded-lg bg-emerald-50/70 border border-emerald-200 flex items-center gap-3">
              <span class="material-symbols-outlined text-emerald-700 text-[24px]">task_alt</span>
              <div>
                <p class="font-bold text-emerald-900 text-sm">Proyecto Aprobado y Avalado (Calificación: 100/100)</p>
                <p class="text-emerald-800 text-[11px] mt-0.5">Dictamen emitido el 24 de septiembre de 2026 · Ciclo 26-27/1</p>
              </div>
            </div>

            <div class="grid grid-cols-2 gap-3 p-3.5 rounded-lg bg-umb-surface border border-umb-border">
              <div>
                <p class="text-[10px] text-umb-outline uppercase font-semibold">Residente</p>
                <p class="font-bold text-umb-carbon mt-0.5">Jesús Andrés Mondragón Tenorio</p>
                <p class="text-[11px] text-umb-muted">Matrícula: 13220024 · ISC</p>
              </div>
              <div>
                <p class="text-[10px] text-umb-outline uppercase font-semibold">Asesor Interno</p>
                <p class="font-bold text-umb-carbon mt-0.5">I.S.C. Leonardo Becerril Sánchez</p>
                <p class="text-[11px] text-umb-muted">Docente Asesor UMB</p>
              </div>
            </div>

            <div class="p-3.5 rounded-lg bg-white border border-umb-border">
              <p class="text-[10px] text-umb-outline uppercase font-semibold">Empresa / Sede Receptora</p>
              <p class="font-bold text-umb-carbon mt-0.5">Universidad Mexiquense del Bicentenario · Dirección Académica</p>
              <p class="text-[11px] text-umb-muted mt-1 leading-relaxed">
                <strong>Observaciones del Asesor:</strong> <em>"El anteproyecto cumple a cabalidad con las competencias del perfil de egreso de Ingeniería en Sistemas Computacionales. Se autoriza la prosecución del registro semanal de bitácoras."</em>
              </p>
            </div>
          </div>
        """,
        "primary_action_btn": '<a href="08-mis-bitacoras.html" class="h-10 px-4 rounded-lg bg-umb-guinda hover:bg-umb-guinda-dark text-white font-semibold text-xs transition-all flex items-center justify-center gap-1.5 shadow-sm"><span>Ir a mis bitácoras</span><span class="material-symbols-outlined text-[16px]">arrow_forward</span></a>'
    },
    "03-asesor-interno": {
        "banner_bg": "bg-umb-guinda-light/70 border-umb-guinda/20 text-umb-carbon",
        "icon": "rate_review",
        "icon_color": "text-umb-guinda bg-white border border-umb-guinda/20",
        "tag": "Notificación Push Académica",
        "tag_badge": "bg-umb-guinda/10 text-umb-guinda border-umb-guinda/20",
        "title": "Entrega de informe parcial recibida para evaluación",
        "desc": "El estudiante <strong>Jesús Andrés Mondragón Tenorio (13220024 · ISC)</strong> ha completado 320 horas validadas y subió su Informe Parcial. Cuentas con 5 días para registrar la rúbrica oficial.",
        "btn_text": "Evaluar informe ahora",
        "modal_title": "Solicitud de Evaluación de Informe Parcial",
        "modal_icon": "assignment_turned_in",
        "modal_icon_color": "text-umb-guinda bg-umb-guinda-light",
        "modal_content": """
          <div class="space-y-4 text-xs text-umb-carbon">
            <div class="p-3.5 rounded-lg bg-umb-guinda-light/60 border border-umb-guinda/20 flex items-center gap-3">
              <span class="material-symbols-outlined text-umb-guinda text-[24px]">description</span>
              <div>
                <p class="font-bold text-umb-carbon text-sm">Informe Parcial (320 horas acumuladas)</p>
                <p class="text-umb-muted text-[11px] mt-0.5">Entregado el 26 de septiembre de 2026 · Estatus: Pendiente de rúbrica</p>
              </div>
            </div>

            <div class="grid grid-cols-2 gap-3 p-3.5 rounded-lg bg-umb-surface border border-umb-border">
              <div>
                <p class="text-[10px] text-umb-outline uppercase font-semibold">Alumno Asignado</p>
                <p class="font-bold text-umb-carbon mt-0.5">Jesús Andrés Mondragón Tenorio</p>
                <p class="text-[11px] text-umb-muted">Matrícula: 13220024 · 9° Semestre</p>
              </div>
              <div>
                <p class="text-[10px] text-umb-outline uppercase font-semibold">Proyecto Institucional</p>
                <p class="font-bold text-umb-carbon mt-0.5">SIGRES-UMB (Dirección Académica)</p>
                <p class="text-[11px] text-umb-muted">Asesor Ext: Mtro. Armando Alcalde</p>
              </div>
            </div>

            <div class="p-3.5 rounded-lg bg-white border border-umb-border">
              <p class="text-[10px] text-umb-outline uppercase font-semibold">Resumen de Actividades</p>
              <p class="text-umb-muted mt-1 leading-relaxed">
                Desarrollo del módulo de autenticación, diseño de arquitectura de bases de datos, maquetación de 71 pantallas y estandarización del manual de diseño institucional.
              </p>
            </div>
          </div>
        """,
        "primary_action_btn": '<a href="06-evaluar-informe-parcial.html" class="h-10 px-4 rounded-lg bg-umb-guinda hover:bg-umb-guinda-dark text-white font-semibold text-xs transition-all flex items-center justify-center gap-1.5 shadow-sm"><span>Abrir rúbrica de evaluación</span><span class="material-symbols-outlined text-[16px]">arrow_forward</span></a>'
    },
    "04-asesor-externo": {
        "banner_bg": "bg-amber-50 border-amber-200 text-amber-900",
        "icon": "pending_actions",
        "icon_color": "text-amber-700 bg-white border border-amber-200",
        "tag": "Notificación Push Empresarial",
        "tag_badge": "bg-amber-100 text-amber-800 border-amber-300",
        "title": "Bitácora semanal #6 lista para tu firma y validación",
        "desc": "El residente <strong>Jesús Andrés Mondragón Tenorio</strong> ha reportado 35 horas de avance en la Dirección Académica UMB durante la presente semana.",
        "btn_text": "Validar bitácora",
        "modal_title": "Validación de Bitácora Semanal",
        "modal_icon": "draw",
        "modal_icon_color": "text-amber-700 bg-amber-100",
        "modal_content": """
          <div class="space-y-4 text-xs text-umb-carbon">
            <div class="p-3.5 rounded-lg bg-amber-50/70 border border-amber-200 flex items-center gap-3">
              <span class="material-symbols-outlined text-amber-700 text-[24px]">menu_book</span>
              <div>
                <p class="font-bold text-amber-900 text-sm">Bitácora #6 · Semana 6 (35 horas)</p>
                <p class="text-amber-800 text-[11px] mt-0.5">Periodo: 21 al 25 de septiembre de 2026</p>
              </div>
            </div>

            <div class="grid grid-cols-2 gap-3 p-3.5 rounded-lg bg-umb-surface border border-umb-border">
              <div>
                <p class="text-[10px] text-umb-outline uppercase font-semibold">Residente Asignado</p>
                <p class="font-bold text-umb-carbon mt-0.5">Jesús Andrés Mondragón Tenorio</p>
                <p class="text-[11px] text-umb-muted">Matrícula: 13220024 · ISC</p>
              </div>
              <div>
                <p class="text-[10px] text-umb-outline uppercase font-semibold">Sede de Residencia</p>
                <p class="font-bold text-umb-carbon mt-0.5">Dirección Académica UMB</p>
                <p class="text-[11px] text-umb-muted">Total acumulado: 355 / 640 hrs</p>
              </div>
            </div>
          </div>
        """,
        "primary_action_btn": '<a href="02-bitacoras-por-validar.html" class="h-10 px-4 rounded-lg bg-umb-guinda hover:bg-umb-guinda-dark text-white font-semibold text-xs transition-all flex items-center justify-center gap-1.5 shadow-sm"><span>Firmar y validar bitácora</span><span class="material-symbols-outlined text-[16px]">arrow_forward</span></a>'
    },
    "05-control-escolar": {
        "banner_bg": "bg-purple-50 border-purple-200 text-purple-900",
        "icon": "folder_shared",
        "icon_color": "text-purple-700 bg-white border border-purple-200",
        "tag": "Notificación Push Control Escolar",
        "tag_badge": "bg-purple-100 text-purple-800 border-purple-300",
        "title": "Expediente digital completo en espera de Carta de Presentación",
        "desc": "El estudiante <strong>Jesús Andrés Mondragón Tenorio (13220024 · ISC)</strong> ha completado la validación documental para iniciar en Dirección Académica.",
        "btn_text": "Generar carta oficial",
        "modal_title": "Expediente de Residencia Listo para Trámite",
        "modal_icon": "print",
        "modal_icon_color": "text-purple-700 bg-purple-100",
        "modal_content": """
          <div class="space-y-4 text-xs text-umb-carbon">
            <div class="p-3.5 rounded-lg bg-purple-50/70 border border-purple-200 flex items-center gap-3">
              <span class="material-symbols-outlined text-purple-700 text-[24px]">verified</span>
              <div>
                <p class="font-bold text-purple-900 text-sm">Expediente Validado al 100%</p>
                <p class="text-purple-800 text-[11px] mt-0.5">Kárdex, carta compromiso y solicitud autorizados</p>
              </div>
            </div>
            <div class="p-3.5 rounded-lg bg-umb-surface border border-umb-border">
              <p class="font-semibold text-umb-carbon">Jesús Andrés Mondragón Tenorio (13220024)</p>
              <p class="text-umb-muted text-[11px] mt-0.5">Carrera: Ingeniería en Sistemas Computacionales · Plantel: San José del Rincón</p>
            </div>
          </div>
        """,
        "primary_action_btn": '<a href="05-generar-carta.html" class="h-10 px-4 rounded-lg bg-umb-guinda hover:bg-umb-guinda-dark text-white font-semibold text-xs transition-all flex items-center justify-center gap-1.5 shadow-sm"><span>Emitir carta oficial</span><span class="material-symbols-outlined text-[16px]">arrow_forward</span></a>'
    },
    "06-coordinacion": {
        "banner_bg": "bg-rose-50 border-rose-200 text-rose-900",
        "icon": "warning",
        "icon_color": "text-rose-700 bg-white border border-rose-200",
        "tag": "Alerta Push de Supervisión",
        "tag_badge": "bg-rose-100 text-rose-800 border-rose-300",
        "title": "Alerta de supervisión de cohorte: 2 alumnos en riesgo preventivo",
        "desc": "En la carrera de ISC se detectaron 2 alumnos con más de 14 días sin registro de bitácoras. Además, hay 4 cartas listas para tu firma digital.",
        "btn_text": "Ver semáforo de riesgo",
        "modal_title": "Supervisión Preventiva de Cohortes",
        "modal_icon": "crisis_alert",
        "modal_icon_color": "text-rose-700 bg-rose-100",
        "modal_content": """
          <div class="space-y-4 text-xs text-umb-carbon">
            <div class="p-3.5 rounded-lg bg-rose-50/70 border border-rose-200 flex items-center gap-3">
              <span class="material-symbols-outlined text-rose-700 text-[24px]">warning</span>
              <div>
                <p class="font-bold text-rose-900 text-sm">Alerta Preventiva de Rezago</p>
                <p class="text-rose-800 text-[11px] mt-0.5">Cohorte ISC Ciclo 26-27/1 · UES San José del Rincón</p>
              </div>
            </div>
            <div class="p-3.5 rounded-lg bg-umb-surface border border-umb-border">
              <p class="font-semibold text-umb-carbon">Acciones recomendadas:</p>
              <p class="text-umb-muted text-[11px] mt-1 leading-relaxed">
                1. Notificar a los asesores internos asignados.<br>
                2. Realizar firma digital de las 4 cartas de presentación autorizadas.
              </p>
            </div>
          </div>
        """,
        "primary_action_btn": '<a href="03-supervision-riesgo.html" class="h-10 px-4 rounded-lg bg-umb-guinda hover:bg-umb-guinda-dark text-white font-semibold text-xs transition-all flex items-center justify-center gap-1.5 shadow-sm"><span>Abrir semáforo de riesgos</span><span class="material-symbols-outlined text-[16px]">arrow_forward</span></a>'
    },
    "07-direccion": {
        "banner_bg": "bg-amber-100/60 border-amber-300 text-amber-950",
        "icon": "analytics",
        "icon_color": "text-amber-800 bg-white border border-amber-300",
        "tag": "Notificación Push Directiva",
        "tag_badge": "bg-amber-200 text-amber-900 border-amber-300",
        "title": "Indicador de acreditación institucional alcanza el 94% de cumplimiento",
        "desc": "El reporte mensual de residencias del ciclo 26-27/1 ha sido consolidado exitosamente para fines de acreditación académica CACEI.",
        "btn_text": "Ver métricas directivas",
        "modal_title": "Indicadores Estratégicos de Residencia",
        "modal_icon": "verified_user",
        "modal_icon_color": "text-amber-800 bg-amber-100",
        "modal_content": """
          <div class="space-y-4 text-xs text-umb-carbon">
            <div class="p-3.5 rounded-lg bg-amber-50 border border-amber-200 flex items-center gap-3">
              <span class="material-symbols-outlined text-amber-800 text-[24px]">military_tech</span>
              <div>
                <p class="font-bold text-amber-950 text-sm">94% de Cumplimiento Institucional</p>
                <p class="text-amber-900 text-[11px] mt-0.5">Indicador estándar CACEI para programas de educación superior UMB</p>
              </div>
            </div>
          </div>
        """,
        "primary_action_btn": '<a href="01-dashboard-ejecutivo.html" class="h-10 px-4 rounded-lg bg-umb-guinda hover:bg-umb-guinda-dark text-white font-semibold text-xs transition-all flex items-center justify-center gap-1.5 shadow-sm"><span>Ver dashboard ejecutivo</span><span class="material-symbols-outlined text-[16px]">arrow_forward</span></a>'
    }
}

def generate_push_banner_html(cfg):
    return f"""        <!-- BANNER DE NOTIFICACIÓN PUSH INSTITUCIONAL INTERACTIVO -->
        <section class="rounded-xl border {cfg['banner_bg']} p-4 sm:p-5 shadow-card transition-all hover:shadow-card-hover relative overflow-hidden" id="pushNotificationBanner">
          <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
            
            <div class="flex items-start sm:items-center gap-3.5 flex-1 min-w-0">
              <div class="w-10 h-10 rounded-xl {cfg['icon_color']} flex items-center justify-center flex-shrink-0 shadow-sm">
                <span class="material-symbols-outlined text-[22px]">{cfg['icon']}</span>
              </div>
              <div class="flex-1 min-w-0">
                <div class="flex items-center gap-2 mb-1">
                  <span class="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-bold uppercase tracking-wider border {cfg['tag_badge']}">
                    <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 mr-1 animate-pulse"></span>
                    {cfg['tag']}
                  </span>
                </div>
                <h3 class="text-sm font-bold tracking-tight text-umb-carbon leading-snug">{cfg['title']}</h3>
                <p class="text-xs mt-0.5 text-umb-muted leading-relaxed">{cfg['desc']}</p>
              </div>
            </div>

            <div class="flex items-center gap-2 self-end sm:self-center flex-shrink-0">
              <button type="button" onclick="openPushModal()" class="h-9 px-4 rounded-lg bg-umb-guinda hover:bg-umb-guinda-dark text-white text-xs font-semibold shadow-sm transition-all flex items-center gap-1.5 focus:outline-none focus:ring-2 focus:ring-umb-guinda">
                <span class="material-symbols-outlined text-[16px]">visibility</span>
                <span>{cfg['btn_text']}</span>
              </button>
              <button type="button" onclick="dismissPushBanner()" class="h-9 w-9 rounded-lg bg-white/80 hover:bg-white text-umb-outline hover:text-umb-carbon border border-umb-border flex items-center justify-center transition-colors" title="Descartar notificación" aria-label="Cerrar notificación">
                <span class="material-symbols-outlined text-[18px]">close</span>
              </button>
            </div>

          </div>
        </section>"""

def generate_push_modal_html(cfg):
    return f"""  <!-- MODAL DE NOTIFICACIÓN PUSH DETALLADA -->
  <div id="pushNotificationModal" class="hidden fixed inset-0 bg-black/50 backdrop-blur-sm z-50 flex items-center justify-center p-4 animate-in fade-in duration-150" aria-modal="true" role="dialog">
    <div class="bg-white rounded-xl shadow-modal max-w-lg w-full overflow-hidden border border-umb-border animate-in zoom-in-95 duration-150" onclick="event.stopPropagation()">
      
      <!-- Encabezado del Modal -->
      <div class="p-4 sm:p-5 bg-gradient-to-r from-umb-surface to-white border-b border-umb-border flex items-center justify-between">
        <div class="flex items-center gap-3">
          <div class="w-9 h-9 rounded-lg {cfg['modal_icon_color']} flex items-center justify-center flex-shrink-0">
            <span class="material-symbols-outlined text-[22px]">{cfg['modal_icon']}</span>
          </div>
          <div>
            <span class="text-[10px] font-bold uppercase tracking-wider text-umb-dorado">Detalle de Notificación Push</span>
            <h3 class="text-sm font-bold text-umb-carbon leading-tight">{cfg['modal_title']}</h3>
          </div>
        </div>
        <button type="button" onclick="closePushModal()" class="w-8 h-8 rounded-lg text-umb-outline hover:text-umb-carbon hover:bg-umb-surface flex items-center justify-center transition-colors">
          <span class="material-symbols-outlined text-[20px]">close</span>
        </button>
      </div>

      <!-- Cuerpo del Modal -->
      <div class="p-5">
{cfg['modal_content']}
      </div>

      <!-- Pie del Modal -->
      <div class="p-4 bg-umb-surface/60 border-t border-umb-border flex items-center justify-end gap-2.5">
        <button type="button" onclick="closePushModal()" class="h-10 px-4 rounded-lg bg-white border border-umb-border hover:bg-umb-surface text-umb-carbon font-medium text-xs transition-all">
          Cerrar
        </button>
        {cfg['primary_action_btn']}
      </div>

    </div>
  </div>"""

MODAL_JS_SCRIPT = """  <!-- SCRIPT DE CONTROL PARA BANNER Y MODAL PUSH -->
  <script>
    function openPushModal() {
      const modal = document.getElementById('pushNotificationModal');
      if (modal) modal.classList.remove('hidden');
    }

    function closePushModal() {
      const modal = document.getElementById('pushNotificationModal');
      if (modal) modal.classList.add('hidden');
    }

    function dismissPushBanner() {
      const banner = document.getElementById('pushNotificationBanner');
      if (banner) {
        banner.style.opacity = '0';
        banner.style.transform = 'translateY(-10px)';
        banner.style.transition = 'all 0.3s ease';
        setTimeout(() => banner.remove(), 300);
      }
    }

    // Cerrar modal al hacer clic en el backdrop
    document.addEventListener('DOMContentLoaded', () => {
      const modal = document.getElementById('pushNotificationModal');
      if (modal) {
        modal.addEventListener('click', (e) => {
          if (e.target === modal) closePushModal();
        });
      }
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') closePushModal();
    });
  </script>"""

def inject_banners_into_dashboards():
    base_dir = r"c:\Users\Pc\Downloads\Maquetado - Residencia\respaldo-pre-estandarizacion-2026-09-17\sigres-umb"
    
    for role_key, cfg in PUSH_CONFIGS.items():
        role_dir = os.path.join(base_dir, role_key)
        # Apply banner to 01-dashboard (and main role screens)
        files = glob.glob(os.path.join(role_dir, "*.html"))
        
        for fpath in files:
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()

            filename = os.path.basename(fpath)
            banner_html = generate_push_banner_html(cfg)
            modal_html = generate_push_modal_html(cfg)

            # Check if this is a dashboard or main screen to inject the push banner at the top of <main>
            if filename.startswith("01-") or "dashboard" in filename:
                # Remove any existing banner
                content = re.sub(r'<!-- BANNER DE NOTIFICACIÓN PUSH.*?-->\s*<section[^>]*id="pushNotificationBanner".*?</section>', '', content, flags=re.DOTALL)
                
                # Insert banner right after <main ...> or after first section in main
                # Find <div class="w-full max-w-[1280px] space-y-6"> or <main ...>
                main_inner = re.search(r'(<main[^>]*>\s*<div[^>]*space-y-6[^>]*>)', content, flags=re.IGNORECASE)
                if main_inner:
                    content = content[:main_inner.end()] + "\n" + banner_html + "\n" + content[main_inner.end():]
                else:
                    main_tag = re.search(r'(<main[^>]*>)', content, flags=re.IGNORECASE)
                    if main_tag:
                        content = content[:main_tag.end()] + "\n" + banner_html + "\n" + content[main_tag.end():]

            # Inject Modal and JS in all role files
            content = re.sub(r'<!-- MODAL DE NOTIFICACIÓN PUSH.*?-->\s*<div id="pushNotificationModal".*?</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)
            content = re.sub(r'<!-- SCRIPT DE CONTROL PARA BANNER.*?-->\s*<script>.*?</script>', '', content, flags=re.DOTALL)

            body_end = re.search(r'</body>', content, flags=re.IGNORECASE)
            if body_end:
                insert_pos = body_end.start()
                content = content[:insert_pos] + "\n" + modal_html + "\n" + MODAL_JS_SCRIPT + "\n" + content[insert_pos:]

            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)

    print("Push notification banners and interactive modals injected into all role screens successfully.")

if __name__ == "__main__":
    inject_banners_into_dashboards()
