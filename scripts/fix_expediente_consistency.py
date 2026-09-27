import os
import re

BASE_DIR = r"c:\Users\Pc\Downloads\Maquetado - Residencia\respaldo-pre-estandarizacion-2026-09-17\sigres-umb"

def fix_mi_expediente_html():
    fpath = os.path.join(BASE_DIR, "02-estudiante", "02-mi-expediente.html")
    with open(fpath, "r", encoding="utf-8") as f:
        c = f.read()

    # 1. Replace header of page (Sección 1)
    old_sec1 = re.search(r'<!-- SECCIÓN 1: ENCABEZADO DE LA PÁGINA -->.*?</div>\s*</div>', c, flags=re.DOTALL)
    new_sec1 = """<!-- SECCIÓN 1: ENCABEZADO DE LA PÁGINA -->
      <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3 bg-white p-5 sm:p-6 rounded-xl border border-umb-border shadow-xs">
        <div>
          <h1 class="text-2xl font-bold text-umb-carbon tracking-tight">Mi expediente</h1>
          <p class="text-sm text-umb-muted mt-1 font-normal">Consulta tus 7 documentos obligatorios para la residencia profesional (Completados y autorizados).</p>
        </div>
        <div class="self-start sm:self-center">
          <span class="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs font-semibold bg-emerald-50 text-emerald-700 border border-emerald-200">
            <span class="h-2 w-2 rounded-full bg-emerald-500"></span>
            Expediente completo y validado
          </span>
        </div>
      </div>"""
    if old_sec1:
        c = c[:old_sec1.start()] + new_sec1 + c[old_sec1.end():]

    # 2. Replace progress section (Sección 2)
    old_sec2 = re.search(r'<!-- SECCIÓN 2: BARRA DE PROGRESO GENERAL -->.*?</section>', c, flags=re.DOTALL)
    new_sec2 = """<!-- SECCIÓN 2: BARRA DE PROGRESO GENERAL -->
      <section class="bg-white rounded-xl p-5 sm:p-6 border border-umb-border shadow-xs space-y-3.5">
        <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-1">
          <span class="text-sm font-medium text-umb-muted">Avance del expediente</span>
          <span class="text-sm font-bold text-umb-carbon">7 de 7 documentos completados y validados</span>
        </div>
        
        <!-- Barra visual 100% en verde institucional -->
        <div class="w-full bg-umb-border h-3 rounded-full overflow-hidden">
          <div class="bg-emerald-600 h-full rounded-full transition-all duration-500 ease-out" style="width: 100%"></div>
        </div>

        <div class="flex flex-wrap items-center justify-between gap-2 pt-0.5">
          <span class="text-xs font-semibold text-emerald-700 flex items-center gap-1">
            <span class="material-symbols-outlined text-[16px] text-emerald-600">verified</span>
            100% completado · Sin adeudos documentales
          </span>
          <span class="text-xs font-medium text-emerald-800 flex items-center gap-1 bg-emerald-50 px-2.5 py-0.5 rounded-md border border-emerald-200">
            <span class="material-symbols-outlined text-[16px] text-emerald-600">check_circle</span>
            Autorizado por Control Escolar (28 de agosto de 2026)
          </span>
        </div>
      </section>"""
    if old_sec2:
        c = c[:old_sec2.start()] + new_sec2 + c[old_sec2.end():]

    # 3. Replace Carta de presentación section (Sección 3)
    old_sec3 = re.search(r'<!-- SECCIÓN 3: GENERACIÓN DE LA CARTA DE PRESENTACIÓN.*?-->.*?</section>', c, flags=re.DOTALL)
    new_sec3 = """<!-- SECCIÓN 3: CARTA DE PRESENTACIÓN OFICIAL (TRÁMITE PREVIO FORMALIZADO) -->
      <section class="bg-white rounded-xl p-5 sm:p-6 border-l-4 border-l-umb-dorado border-y border-r border-umb-border shadow-xs">
        <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-5">
          <div class="space-y-1.5 max-w-3xl">
            <div class="flex items-center gap-2">
              <span class="inline-flex items-center px-2 py-0.5 rounded text-[11px] font-semibold bg-umb-dorado-light text-[#92400E]">
                Trámite previo formalizado
              </span>
              <h3 class="text-base font-semibold text-umb-carbon">Carta de presentación oficial</h3>
            </div>
            <p class="text-sm text-umb-muted leading-relaxed font-normal">
              Carta oficial generada y formalizada con la sede receptora <strong class="text-umb-carbon font-semibold">Universidad Mexiquense del Bicentenario · Dirección Académica</strong>, autorizada y firmada por la Coordinación de la UES San José del Rincón antes del inicio de residencias.
            </p>
          </div>

          <div class="flex flex-col sm:flex-row lg:flex-col items-start lg:items-end gap-3 shrink-0">
            <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-medium bg-[#DCFCE7] text-[#166534] border border-emerald-200">
              <span class="material-symbols-outlined text-[16px] text-emerald-600">check_circle</span>
              Carta emitida y firmada el 18 de agosto de 2026
            </span>
            <a href="07-carta-presentacion-generada.html" class="inline-flex items-center gap-2 px-4 py-2 rounded-lg border border-umb-guinda text-umb-guinda hover:bg-umb-guinda/5 text-xs font-semibold transition-colors shadow-xs">
              <span class="material-symbols-outlined text-[18px]">visibility</span>
              Ver carta oficial
            </a>
          </div>
        </div>
      </section>"""
    if old_sec3:
        c = c[:old_sec3.start()] + new_sec3 + c[old_sec3.end():]

    # 4. Replace the 7 documents checklist and final submission section
    old_sec4_and_5 = re.search(r'<!-- SECCIÓN 4: CHECKLIST DE LOS 7 DOCUMENTOS -->.*?</main>', c, flags=re.DOTALL)
    new_sec4_and_5 = """<!-- SECCIÓN 4: CHECKLIST DE LOS 7 DOCUMENTOS OBLIGATORIOS (TODOS VALIDADOS) -->
      <section class="space-y-4">
        <!-- Encabezado de la sección -->
        <div class="flex flex-col sm:flex-row sm:items-baseline sm:justify-between gap-1">
          <div>
            <h2 class="text-xl font-semibold text-umb-carbon tracking-tight">Documentos obligatorios</h2>
            <p class="text-xs text-umb-outline mt-0.5">Expediente formal integrado previamente al inicio del ciclo de residencias (1 de septiembre de 2026).</p>
          </div>
          <span class="text-xs text-emerald-700 font-semibold flex items-center gap-1">
            <span class="material-symbols-outlined text-[15px]">verified</span>
            7 de 7 validados por Control Escolar
          </span>
        </div>

        <!-- LISTA DE LAS 7 TARJETAS COMPLETADAS -->
        <div class="space-y-3.5">
          
          <!-- DOCUMENTO 1: Acuse de recibido de carta de presentación -->
          <article class="bg-white rounded-xl p-5 border border-umb-border border-l-4 border-l-[#2D8C4E] shadow-xs hover:shadow-sm transition-shadow">
            <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
              <div class="flex items-start gap-4">
                <div class="h-9 w-9 rounded-full bg-emerald-50 text-[#2D8C4E] border border-emerald-200 font-bold text-sm flex items-center justify-center shrink-0 mt-0.5">
                  1
                </div>
                <div class="space-y-1">
                  <div class="flex flex-wrap items-center gap-2">
                    <h3 class="text-sm font-semibold text-umb-carbon">Acuse de recibido de carta de presentación</h3>
                    <span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-semibold bg-[#DCFCE7] text-[#166534]">
                      <span class="material-symbols-outlined text-[14px]">check_circle</span>
                      Validado
                    </span>
                  </div>
                  <p class="text-xs text-umb-muted leading-relaxed">Copia sellada y firmada por la Dirección Académica UMB donde se confirma la recepción de la carta de presentación.</p>
                  
                  <div class="flex flex-wrap items-center gap-3 pt-1 text-[11px] text-umb-outline">
                    <span class="flex items-center gap-1 font-medium text-neutral-700">
                      <span class="material-symbols-outlined text-[14px] text-red-600">picture_as_pdf</span>
                      acuse_carta_presentacion_umb.pdf
                    </span>
                    <span>•</span>
                    <span>1.2 MB</span>
                    <span>•</span>
                    <span>Subido y validado el 21 de agosto de 2026</span>
                  </div>
                </div>
              </div>

              <div class="flex items-center gap-2 self-end md:self-center shrink-0">
                <button type="button" class="inline-flex items-center gap-1.5 px-3 py-2 rounded-lg border border-umb-border hover:bg-umb-surface text-umb-carbon text-xs font-medium transition-colors">
                  <span class="material-symbols-outlined text-[16px]">visibility</span>
                  Ver documento
                </button>
              </div>
            </div>
          </article>

          <!-- DOCUMENTO 2: Carta de aceptación de la empresa -->
          <article class="bg-white rounded-xl p-5 border border-umb-border border-l-4 border-l-[#2D8C4E] shadow-xs hover:shadow-sm transition-shadow">
            <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
              <div class="flex items-start gap-4">
                <div class="h-9 w-9 rounded-full bg-emerald-50 text-[#2D8C4E] border border-emerald-200 font-bold text-sm flex items-center justify-center shrink-0 mt-0.5">
                  2
                </div>
                <div class="space-y-1">
                  <div class="flex flex-wrap items-center gap-2">
                    <h3 class="text-sm font-semibold text-umb-carbon">Carta de aceptación de la sede receptora</h3>
                    <span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-semibold bg-[#DCFCE7] text-[#166534]">
                      <span class="material-symbols-outlined text-[14px]">check_circle</span>
                      Validado
                    </span>
                  </div>
                  <p class="text-xs text-umb-muted leading-relaxed">Carta membretada y sellada por la Dirección Académica UMB, especificando la jornada de 7 horas diarias (35 horas semanales).</p>
                  
                  <div class="flex flex-wrap items-center gap-3 pt-1 text-[11px] text-umb-outline">
                    <span class="flex items-center gap-1 font-medium text-neutral-700">
                      <span class="material-symbols-outlined text-[14px] text-red-600">picture_as_pdf</span>
                      carta_aceptacion_umb_firmada.pdf
                    </span>
                    <span>•</span>
                    <span>1.8 MB</span>
                    <span>•</span>
                    <span>Subido y validado el 22 de agosto de 2026</span>
                  </div>
                </div>
              </div>

              <div class="flex items-center gap-2 self-end md:self-center shrink-0">
                <button type="button" class="inline-flex items-center gap-1.5 px-3 py-2 rounded-lg border border-umb-border hover:bg-umb-surface text-umb-carbon text-xs font-medium transition-colors">
                  <span class="material-symbols-outlined text-[16px]">visibility</span>
                  Ver documento
                </button>
              </div>
            </div>
          </article>

          <!-- DOCUMENTO 3: Formato de autorización de uso de información (NDA) -->
          <article class="bg-white rounded-xl p-5 border border-umb-border border-l-4 border-l-[#2D8C4E] shadow-xs hover:shadow-sm transition-shadow">
            <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
              <div class="flex items-start gap-4">
                <div class="h-9 w-9 rounded-full bg-emerald-50 text-[#2D8C4E] border border-emerald-200 font-bold text-sm flex items-center justify-center shrink-0 mt-0.5">
                  3
                </div>
                <div class="space-y-1">
                  <div class="flex flex-wrap items-center gap-2">
                    <h3 class="text-sm font-semibold text-umb-carbon">Formato de autorización de uso de información (NDA)</h3>
                    <span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-semibold bg-[#DCFCE7] text-[#166534]">
                      <span class="material-symbols-outlined text-[14px]">check_circle</span>
                      Validado
                    </span>
                  </div>
                  <p class="text-xs text-umb-muted leading-relaxed">Documento oficial firmado donde se autoriza el uso de la información del proyecto para fines académicos institucionales.</p>
                  
                  <div class="flex flex-wrap items-center gap-3 pt-1 text-[11px] text-umb-outline">
                    <span class="flex items-center gap-1 font-medium text-neutral-700">
                      <span class="material-symbols-outlined text-[14px] text-red-600">picture_as_pdf</span>
                      nda_autorizacion_academica_umb.pdf
                    </span>
                    <span>•</span>
                    <span>940 KB</span>
                    <span>•</span>
                    <span>Subido y validado el 23 de agosto de 2026</span>
                  </div>
                </div>
              </div>

              <div class="flex items-center gap-2 self-end md:self-center shrink-0">
                <button type="button" class="inline-flex items-center gap-1.5 px-3 py-2 rounded-lg border border-umb-border hover:bg-umb-surface text-umb-carbon text-xs font-medium transition-colors">
                  <span class="material-symbols-outlined text-[16px]">visibility</span>
                  Ver documento
                </button>
              </div>
            </div>
          </article>

          <!-- DOCUMENTO 4: Anteproyecto de residencia profesional -->
          <article class="bg-white rounded-xl p-5 border border-umb-border border-l-4 border-l-[#2D8C4E] shadow-xs hover:shadow-sm transition-shadow">
            <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
              <div class="flex items-start gap-4">
                <div class="h-9 w-9 rounded-full bg-emerald-50 text-[#2D8C4E] border border-emerald-200 font-bold text-sm flex items-center justify-center shrink-0 mt-0.5">
                  4
                </div>
                <div class="space-y-1">
                  <div class="flex flex-wrap items-center gap-2">
                    <h3 class="text-sm font-semibold text-umb-carbon">Anteproyecto de residencia profesional</h3>
                    <span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-semibold bg-[#DCFCE7] text-[#166534]">
                      <span class="material-symbols-outlined text-[14px]">check_circle</span>
                      Validado y avalado
                    </span>
                  </div>
                  <p class="text-xs text-umb-muted leading-relaxed">Documento técnico con el planteamiento del sistema SIGRES-UMB, avalado formalmente por el Asesor Interno (I.S.C. Leonardo Becerril).</p>
                  
                  <div class="flex flex-wrap items-center gap-3 pt-1 text-[11px] text-umb-outline">
                    <span class="flex items-center gap-1 font-medium text-neutral-700">
                      <span class="material-symbols-outlined text-[14px] text-red-600">picture_as_pdf</span>
                      anteproyecto_sigres_jesus_mondragon.pdf
                    </span>
                    <span>•</span>
                    <span>3.4 MB</span>
                    <span>•</span>
                    <span>Subido el 24 de agosto de 2026 · Avalado el 26 de agosto de 2026</span>
                  </div>
                </div>
              </div>

              <div class="flex items-center gap-2 self-end md:self-center shrink-0">
                <button type="button" class="inline-flex items-center gap-1.5 px-3 py-2 rounded-lg border border-umb-border hover:bg-umb-surface text-umb-carbon text-xs font-medium transition-colors">
                  <span class="material-symbols-outlined text-[16px]">visibility</span>
                  Ver documento
                </button>
              </div>
            </div>
          </article>

          <!-- DOCUMENTO 5: Constancia de liberación de servicio social -->
          <article class="bg-white rounded-xl p-5 border border-umb-border border-l-4 border-l-[#2D8C4E] shadow-xs hover:shadow-sm transition-shadow">
            <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
              <div class="flex items-start gap-4">
                <div class="h-9 w-9 rounded-full bg-emerald-50 text-[#2D8C4E] border border-emerald-200 font-bold text-sm flex items-center justify-center shrink-0 mt-0.5">
                  5
                </div>
                <div class="space-y-1">
                  <div class="flex flex-wrap items-center gap-2">
                    <h3 class="text-sm font-semibold text-umb-carbon">Constancia de liberación de servicio social (2 copias)</h3>
                    <span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-semibold bg-[#DCFCE7] text-[#166534]">
                      <span class="material-symbols-outlined text-[14px]">check_circle</span>
                      Validado
                    </span>
                  </div>
                  <p class="text-xs text-umb-muted leading-relaxed">Constancia oficial que acredita la liberación reglamentaria del servicio social universitario (480 horas).</p>
                  
                  <div class="flex flex-wrap items-center gap-3 pt-1 text-[11px] text-umb-outline">
                    <span class="flex items-center gap-1 font-medium text-neutral-700">
                      <span class="material-symbols-outlined text-[14px] text-red-600">picture_as_pdf</span>
                      liberacion_servicio_social_13220024.pdf
                    </span>
                    <span>•</span>
                    <span>1.1 MB</span>
                    <span>•</span>
                    <span>Subido y validado el 20 de agosto de 2026</span>
                  </div>
                </div>
              </div>

              <div class="flex items-center gap-2 self-end md:self-center shrink-0">
                <button type="button" class="inline-flex items-center gap-1.5 px-3 py-2 rounded-lg border border-umb-border hover:bg-umb-surface text-umb-carbon text-xs font-medium transition-colors">
                  <span class="material-symbols-outlined text-[16px]">visibility</span>
                  Ver documento
                </button>
              </div>
            </div>
          </article>

          <!-- DOCUMENTO 6: Historial académico -->
          <article class="bg-white rounded-xl p-5 border border-umb-border border-l-4 border-l-[#2D8C4E] shadow-xs hover:shadow-sm transition-shadow">
            <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
              <div class="flex items-start gap-4">
                <div class="h-9 w-9 rounded-full bg-emerald-50 text-[#2D8C4E] border border-emerald-200 font-bold text-sm flex items-center justify-center shrink-0 mt-0.5">
                  6
                </div>
                <div class="space-y-1">
                  <div class="flex flex-wrap items-center gap-2">
                    <h3 class="text-sm font-semibold text-umb-carbon">Historial académico (Kárdex oficial 9º semestre)</h3>
                    <span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-semibold bg-[#DCFCE7] text-[#166534]">
                      <span class="material-symbols-outlined text-[14px]">check_circle</span>
                      Validado
                    </span>
                  </div>
                  <p class="text-xs text-umb-muted leading-relaxed">Kárdex actualizado con el 100% de créditos previos concluidos satisfactoriamente.</p>
                  
                  <div class="flex flex-wrap items-center gap-3 pt-1 text-[11px] text-umb-outline">
                    <span class="flex items-center gap-1 font-medium text-neutral-700">
                      <span class="material-symbols-outlined text-[14px] text-red-600">picture_as_pdf</span>
                      kardex_jesus_mondragon_9sem.pdf
                    </span>
                    <span>•</span>
                    <span>2.1 MB</span>
                    <span>•</span>
                    <span>Subido y validado el 19 de agosto de 2026</span>
                  </div>
                </div>
              </div>

              <div class="flex items-center gap-2 self-end md:self-center shrink-0">
                <button type="button" class="inline-flex items-center gap-1.5 px-3 py-2 rounded-lg border border-umb-border hover:bg-umb-surface text-umb-carbon text-xs font-medium transition-colors">
                  <span class="material-symbols-outlined text-[16px]">visibility</span>
                  Ver documento
                </button>
              </div>
            </div>
          </article>

          <!-- DOCUMENTO 7: Comprobante de pago de reinscripción -->
          <article class="bg-white rounded-xl p-5 border border-umb-border border-l-4 border-l-[#2D8C4E] shadow-xs hover:shadow-sm transition-shadow">
            <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
              <div class="flex items-start gap-4">
                <div class="h-9 w-9 rounded-full bg-emerald-50 text-[#2D8C4E] border border-emerald-200 font-bold text-sm flex items-center justify-center shrink-0 mt-0.5">
                  7
                </div>
                <div class="space-y-1">
                  <div class="flex flex-wrap items-center gap-2">
                    <h3 class="text-sm font-semibold text-umb-carbon">Comprobante de pago de reinscripción</h3>
                    <span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-semibold bg-[#DCFCE7] text-[#166534]">
                      <span class="material-symbols-outlined text-[14px]">check_circle</span>
                      Validado
                    </span>
                  </div>
                  <p class="text-xs text-umb-muted leading-relaxed">Comprobante de pago bancario de reinscripción correspondiente al ciclo 26-27/1.</p>
                  
                  <div class="flex flex-wrap items-center gap-3 pt-1 text-[11px] text-umb-outline">
                    <span class="flex items-center gap-1 font-medium text-neutral-700">
                      <span class="material-symbols-outlined text-[14px] text-red-600">picture_as_pdf</span>
                      comprobante_pago_reinscripcion_13220024.pdf
                    </span>
                    <span>•</span>
                    <span>850 KB</span>
                    <span>•</span>
                    <span>Subido y validado el 18 de agosto de 2026</span>
                  </div>
                </div>
              </div>

              <div class="flex items-center gap-2 self-end md:self-center shrink-0">
                <button type="button" class="inline-flex items-center gap-1.5 px-3 py-2 rounded-lg border border-umb-border hover:bg-umb-surface text-umb-carbon text-xs font-medium transition-colors">
                  <span class="material-symbols-outlined text-[16px]">visibility</span>
                  Ver documento
                </button>
              </div>
            </div>
          </article>

        </div>
      </section>

      <!-- SECCIÓN 5: DICTAMEN DE AUTORIZACIÓN DE CONTROL ESCOLAR -->
      <section class="bg-gradient-to-r from-white via-emerald-50/30 to-white rounded-xl p-5 sm:p-6 border border-emerald-200 shadow-xs space-y-4">
        <div class="flex items-start gap-3.5">
          <div class="h-11 w-11 rounded-xl bg-emerald-100 text-emerald-700 flex items-center justify-center shrink-0 border border-emerald-200">
            <span class="material-symbols-outlined text-[26px]">task_alt</span>
          </div>
          <div class="flex-1">
            <div class="flex items-center gap-2">
              <h3 class="text-base font-bold text-umb-carbon">Expediente autorizado formalmente por Control Escolar</h3>
              <span class="px-2.5 py-0.5 rounded-full text-[11px] font-semibold bg-emerald-100 text-emerald-800">Liberado para residencias</span>
            </div>
            <p class="text-sm text-umb-muted font-normal mt-1 leading-relaxed">
              Tu expediente completo fue cotejado y dictaminado favorablemente el <strong class="text-umb-carbon">28 de agosto de 2026</strong> por la Lic. Estefanía Yttesen Nava (Control Escolar). Cuentas con la autorización plena para desarrollar tu residencia profesional (Ciclo 26-27/1) a partir del <strong class="text-umb-carbon">1 de septiembre de 2026</strong>.
            </p>
          </div>
        </div>

        <div class="pt-2 flex flex-col sm:flex-row items-center justify-end gap-3 border-t border-emerald-200/60">
          <button type="button" class="w-full sm:w-auto h-10 px-4 rounded-lg bg-white border border-emerald-300 hover:bg-emerald-50 text-emerald-800 text-xs font-semibold flex items-center justify-center gap-2 transition-colors">
            <span class="material-symbols-outlined text-[18px]">download</span>
            <span>Descargar acuse de expediente completo (PDF)</span>
          </button>
          <a href="01-dashboard.html" class="w-full sm:w-auto h-10 px-5 rounded-lg bg-umb-guinda hover:bg-umb-guinda-dark text-white text-xs font-semibold flex items-center justify-center gap-2 transition-colors shadow-xs">
            <span>Ir al dashboard de residencia</span>
            <span class="material-symbols-outlined text-[16px]">arrow_forward</span>
          </a>
        </div>
      </section>

      <!-- PIE DE PÁGINA INSTITUCIONAL -->
      <footer class="pt-8 pb-4 text-center text-[12px] text-umb-outline space-y-1">
  <p>SIGRES-UMB — Sistema integral para la gestión de residencias profesionales</p>
  <p>Universidad Mexiquense del Bicentenario · UES San José del Rincón · Ciclo 26-27/1</p>
</footer>

    </main>"""
    if old_sec4_and_5:
        c = c[:old_sec4_and_5.start()] + new_sec4_and_5 + c[old_sec4_and_5.end():]

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(c)

    print("02-mi-expediente.html updated with 7/7 validated documents and August 2026 dates.")

def fix_other_student_expediente_dates():
    # 06-solicitud-residencia.html
    f_sol = os.path.join(BASE_DIR, "02-estudiante", "06-solicitud-residencia.html")
    if os.path.exists(f_sol):
        with open(f_sol, "r", encoding="utf-8") as f:
            c = f.read()
        c = c.replace("15 de octubre de 2026", "18 de agosto de 2026")
        with open(f_sol, "w", encoding="utf-8") as f:
            f.write(c)

    # 07-carta-presentacion-generada.html
    f_carta = os.path.join(BASE_DIR, "02-estudiante", "07-carta-presentacion-generada.html")
    if os.path.exists(f_carta):
        with open(f_carta, "r", encoding="utf-8") as f:
            c = f.read()
        c = c.replace("15 de octubre de 2026", "18 de agosto de 2026")
        with open(f_carta, "w", encoding="utf-8") as f:
            f.write(c)

    # 05-estatus-validacion-empresa.html
    f_stat = os.path.join(BASE_DIR, "02-estudiante", "05-estatus-validacion-empresa.html")
    if os.path.exists(f_stat):
        with open(f_stat, "r", encoding="utf-8") as f:
            c = f.read()
        c = c.replace("18 de octubre de 2026", "17 de agosto de 2026")
        with open(f_stat, "w", encoding="utf-8") as f:
            f.write(c)

    print("Auxiliary student expediente files updated with August 2026 dates (prior to Sept 1st).")

if __name__ == "__main__":
    fix_mi_expediente_html()
    fix_other_student_expediente_dates()
