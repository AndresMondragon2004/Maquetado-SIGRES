import os
import re

print("Enhancing Estudiante and Coordinacion with interactive modals and toasts...")

# 1. ENHANCE 02-estudiante/08-mis-bitacoras.html
f_bitacoras = 'sigres-umb/02-estudiante/08-mis-bitacoras.html'
if os.path.exists(f_bitacoras):
    with open(f_bitacoras, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add a Draft card at the top of Section 3 with interactive Delete & Submit buttons
    draft_card_html = '''
          <!-- BITÁCORA BORRADOR: SEMANA 11 (Interactivo) -->
          <article id="bitacora-borrador-11" class="bg-amber-50/40 rounded-lg shadow-sm border border-amber-300 border-l-4 border-l-amber-500 p-5 transition hover:shadow-md">
            <div class="flex items-start justify-between gap-3">
              <div>
                <div class="flex items-center space-x-2">
                  <h3 class="text-sm font-semibold text-slate-900">Semana 11</h3>
                  <span class="inline-flex items-center px-2 py-0.5 rounded text-[11px] font-bold bg-amber-100 text-amber-800 border border-amber-200">
                    <span class="material-symbols-outlined text-[14px] mr-1 animate-pulse">edit_note</span>
                    Borrador en captura
                  </span>
                </div>
                <p class="text-xs text-slate-500 mt-0.5">9 al 13 de octubre de 2026 · Guardado automático activo</p>
              </div>
              <div class="flex items-center space-x-2">
                <span class="inline-flex items-center px-2.5 py-1 rounded text-xs font-semibold bg-white text-slate-700 border border-slate-200 shadow-2xs">
                  35 horas proyectadas
                </span>
              </div>
            </div>

            <p class="text-sm text-slate-700 mt-3 leading-relaxed">
              Implementación del microservicio de auditoría de eventos y vinculación con la base de datos PostgreSQL institucional.
            </p>

            <div class="mt-4 pt-3 border-t border-amber-200/70 flex flex-wrap items-center justify-between gap-3 text-xs">
              <div class="flex items-center space-x-1.5 text-slate-500">
                <span class="material-symbols-outlined text-[16px] text-slate-400">attach_file</span>
                <span>2 evidencias adjuntas (.png, .pdf)</span>
              </div>
              <div class="flex items-center gap-2">
                <button type="button" onclick="openDeleteDraftModal('Semana 11 (9 al 13 de octubre)')" class="px-3 py-1.5 rounded-lg border border-rose-200 bg-white hover:bg-rose-50 text-rose-700 font-semibold transition flex items-center gap-1">
                  <span class="material-symbols-outlined text-[15px]">delete</span>
                  <span>Eliminar borrador</span>
                </button>
                <a href="09-nueva-bitacora.html" class="px-3 py-1.5 rounded-lg border border-slate-300 bg-white hover:bg-slate-50 text-slate-700 font-semibold transition flex items-center gap-1">
                  <span class="material-symbols-outlined text-[15px]">edit</span>
                  <span>Continuar editando</span>
                </a>
                <button type="button" onclick="openSubmitDraftModal('Semana 11')" class="px-3.5 py-1.5 rounded-lg bg-umb-guinda hover:bg-umb-guinda-dark text-white font-semibold transition flex items-center gap-1 shadow-xs">
                  <span class="material-symbols-outlined text-[15px]">send</span>
                  <span>Enviar a revisión</span>
                </button>
              </div>
            </div>
          </article>
'''

    content = content.replace(
        '<!-- SECCIÓN 3: LISTA DE BITÁCORAS SEMANALES (5 tarjetas representativas) -->\n        <section class="space-y-3.5" aria-label="Historial de bitácoras">',
        '<!-- SECCIÓN 3: LISTA DE BITÁCORAS SEMANALES (5 tarjetas representativas) -->\n        <section class="space-y-3.5" aria-label="Historial de bitácoras">\n' + draft_card_html
    )

    # Add Modals and Toasts
    bitacora_modals = '''
  <!-- MODAL DE ELIMINACIÓN DE BORRADOR (Transversal 02) -->
  <div id="deleteDraftModal" class="hidden fixed inset-0 bg-black/60 backdrop-blur-xs z-50 flex items-center justify-center p-4 animate-in fade-in duration-150">
    <div class="bg-white rounded-2xl shadow-modal max-w-md w-full overflow-hidden border border-rose-200">
      <div class="p-6 text-center bg-gradient-to-b from-rose-50 to-white border-b border-rose-100">
        <div class="w-14 h-14 rounded-2xl bg-rose-100 text-rose-700 border border-rose-200 flex items-center justify-center mx-auto mb-3">
          <span class="material-symbols-outlined text-[32px]">delete_forever</span>
        </div>
        <h3 class="text-base font-bold text-slate-900 leading-tight">¿Eliminar borrador de bitácora?</h3>
        <p class="text-xs text-slate-600 mt-1.5" id="deleteDraftTargetText">Semana 11</p>
      </div>
      <div class="p-5 text-xs text-slate-600">
        <p>Se borrarán las 35 horas capturadas y las evidencias adjuntas de esta semana. Esta acción no se puede deshacer.</p>
      </div>
      <div class="p-4 bg-slate-50 border-t border-slate-200 flex items-center justify-end gap-2.5">
        <button type="button" onclick="closeDeleteDraftModal()" class="h-10 px-4 rounded-xl border border-slate-300 bg-white text-slate-700 font-semibold text-xs">Cancelar</button>
        <button type="button" onclick="confirmDeleteDraft()" class="h-10 px-5 rounded-xl bg-rose-700 hover:bg-rose-800 text-white font-semibold text-xs shadow-sm flex items-center gap-1.5">
          <span class="material-symbols-outlined text-[18px]">delete</span>
          <span>Eliminar definitivamente</span>
        </button>
      </div>
    </div>
  </div>

  <!-- MODAL DE ENVÍO A REVISIÓN (Transversal 01) -->
  <div id="submitDraftModal" class="hidden fixed inset-0 bg-black/50 backdrop-blur-xs z-50 flex items-center justify-center p-4 animate-in fade-in duration-150">
    <div class="bg-white rounded-2xl shadow-modal max-w-md w-full overflow-hidden border border-emerald-200">
      <div class="p-6 text-center bg-gradient-to-b from-emerald-50 to-white border-b border-emerald-100">
        <div class="w-14 h-14 rounded-2xl bg-emerald-100 text-emerald-700 border border-emerald-200 flex items-center justify-center mx-auto mb-3">
          <span class="material-symbols-outlined text-[32px]">send</span>
        </div>
        <h3 class="text-base font-bold text-slate-900 leading-tight">¿Enviar bitácora a revisión?</h3>
        <p class="text-xs text-slate-600 mt-1.5">Se notificará a tu Asesor Interno (I.S.C. Leonardo Becerril) y Asesor Externo.</p>
      </div>
      <div class="p-5 text-xs text-slate-600">
        <p>Al enviar la bitácora quedará bloqueada para edición hasta que tus asesores emitan sus observaciones o aprobación.</p>
      </div>
      <div class="p-4 bg-slate-50 border-t border-slate-200 flex items-center justify-end gap-2.5">
        <button type="button" onclick="closeSubmitDraftModal()" class="h-10 px-4 rounded-xl border border-slate-300 bg-white text-slate-700 font-semibold text-xs">Cancelar</button>
        <button type="button" onclick="confirmSubmitDraft()" class="h-10 px-5 rounded-xl bg-umb-guinda hover:bg-umb-guinda-dark text-white font-semibold text-xs shadow-sm flex items-center gap-1.5">
          <span class="material-symbols-outlined text-[18px]">check_circle</span>
          <span>Confirmar y enviar</span>
        </button>
      </div>
    </div>
  </div>

  <!-- TOAST FLOTANTE INSTITUCIONAL (Transversal 03) -->
  <div id="studentToast" class="fixed top-20 right-6 z-50 bg-slate-900 text-white px-5 py-3.5 rounded-2xl shadow-2xl flex items-center gap-3 border border-slate-700 transform -translate-y-12 opacity-0 transition-all duration-300 pointer-events-none max-w-md">
    <div id="studentToastIconContainer" class="w-9 h-9 rounded-xl bg-emerald-600 flex items-center justify-center text-white shrink-0">
      <span class="material-symbols-outlined text-[20px]" id="studentToastIcon">check_circle</span>
    </div>
    <div class="text-xs">
      <p class="font-bold text-white text-sm" id="studentToastTitle">Acción completada</p>
      <p class="text-slate-300 text-[11px] mt-0.5" id="studentToastMessage">La bitácora se actualizó correctamente.</p>
    </div>
  </div>

  <script>
    function openDeleteDraftModal(name) {
      document.getElementById('deleteDraftTargetText').textContent = name;
      document.getElementById('deleteDraftModal').classList.remove('hidden');
    }
    function closeDeleteDraftModal() {
      document.getElementById('deleteDraftModal').classList.add('hidden');
    }
    function confirmDeleteDraft() {
      closeDeleteDraftModal();
      const card = document.getElementById('bitacora-borrador-11');
      if (card) {
        card.style.opacity = '0';
        card.style.transform = 'scale(0.95)';
        card.style.transition = 'all 0.3s ease';
        setTimeout(() => card.remove(), 300);
      }
      showStudentToast('Borrador eliminado', 'El borrador de la Semana 11 fue descartado.', 'info');
    }

    function openSubmitDraftModal(name) {
      document.getElementById('submitDraftModal').classList.remove('hidden');
    }
    function closeSubmitDraftModal() {
      document.getElementById('submitDraftModal').classList.add('hidden');
    }
    function confirmSubmitDraft() {
      closeSubmitDraftModal();
      const card = document.getElementById('bitacora-borrador-11');
      if (card) {
        card.className = 'bg-white rounded-lg shadow-sm border border-gray-200/90 border-l-4 border-l-amber-500 p-5 transition';
        card.innerHTML = `
          <div class="flex items-start justify-between gap-3">
            <div>
              <div class="flex items-center space-x-2">
                <h3 class="text-sm font-semibold text-slate-900">Semana 11</h3>
                <span class="inline-flex items-center px-2 py-0.5 rounded text-[11px] font-medium bg-amber-50 text-amber-800 border border-amber-200">
                  <span class="w-1.5 h-1.5 rounded-full bg-amber-500 mr-1.5 animate-pulse"></span>
                  Enviada a revisión
                </span>
              </div>
              <p class="text-xs text-slate-500 mt-0.5">9 al 13 de octubre de 2026</p>
            </div>
            <span class="inline-flex items-center px-2.5 py-1 rounded text-xs font-medium bg-umb-surface text-slate-700 border border-slate-200">
              35 horas
            </span>
          </div>
          <p class="text-sm text-slate-700 mt-3 leading-relaxed">
            Implementación del microservicio de auditoría de eventos y vinculación con la base de datos PostgreSQL institucional.
          </p>
          <div class="mt-4 pt-3 border-t border-gray-100 flex items-center justify-between text-xs text-slate-500">
            <span>En espera de firma del Asesor Interno</span>
            <span class="text-xs font-semibold text-umb-guinda">Ver detalle →</span>
          </div>
        `;
      }
      showStudentToast('Bitácora enviada con éxito', 'Se notificó a tus asesores para su revisión reglamentaria.', 'success');
    }

    function showStudentToast(title, message, type = 'success') {
      const toast = document.getElementById('studentToast');
      document.getElementById('studentToastTitle').textContent = title;
      document.getElementById('studentToastMessage').textContent = message;
      const icon = document.getElementById('studentToastIcon');
      const iconCont = document.getElementById('studentToastIconContainer');
      if (type === 'success') {
        iconCont.className = 'w-9 h-9 rounded-xl bg-emerald-600 flex items-center justify-center text-white shrink-0';
        icon.textContent = 'check_circle';
      } else {
        iconCont.className = 'w-9 h-9 rounded-xl bg-slate-700 flex items-center justify-center text-white shrink-0';
        icon.textContent = 'delete';
      }
      toast.classList.remove('-translate-y-12', 'opacity-0', 'pointer-events-none');
      setTimeout(() => {
        toast.classList.add('-translate-y-12', 'opacity-0', 'pointer-events-none');
      }, 3500);
    }
  </script>
'''

    content = content.replace('</body>', bitacora_modals + '\n</body>')
    with open(f_bitacoras, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Enhanced 02-estudiante/08-mis-bitacoras.html with interactive Draft card, Delete Modal, Submit Modal & Toast!")

# 2. ENHANCE 06-coordinacion/04-contingencias.html
f_contingencias = 'sigres-umb/06-coordinacion/04-contingencias.html'
if os.path.exists(f_contingencias):
    with open(f_contingencias, 'r', encoding='utf-8') as f:
        ccontent = f.read()

    # Enhance action button in Active Case 2
    ccontent = ccontent.replace(
        '<button class="px-3.5 py-1.5 text-xs font-semibold text-white bg-umb-guinda hover:bg-[#521422] rounded-lg shadow-sm transition-colors" type="button">\n                Aprobar reubicación\n              </button>',
        '<button onclick="openDictamenModal(\'Daniel Benítez (13210112)\', \'Reubicación a SAT Módulo Atlacomulco\', \'240 hrs reconocidas\')" class="px-3.5 py-1.5 text-xs font-semibold text-white bg-umb-guinda hover:bg-umb-guinda-dark rounded-lg shadow-sm transition-colors flex items-center gap-1" type="button">\n                <span class="material-symbols-outlined text-[15px]">verified</span>\n                <span>Aprobar reubicación</span>\n              </button>'
    )

    # Enhance action button in Active Case 1
    ccontent = ccontent.replace(
        '<button class="px-3.5 py-1.5 text-xs font-semibold text-white bg-emerald-600 hover:bg-emerald-700 rounded-lg shadow-sm transition-colors" type="button">\n                Reanudar\n              </button>',
        '<button onclick="openDictamenModal(\'Marco Antonio García Cruz (13220018)\', \'Reanudación tras pausa médica\', \'350 hrs reactivadas\')" class="px-3.5 py-1.5 text-xs font-semibold text-white bg-emerald-600 hover:bg-emerald-700 rounded-lg shadow-sm transition-colors flex items-center gap-1" type="button">\n                <span class="material-symbols-outlined text-[15px]">play_arrow</span>\n                <span>Reanudar</span>\n              </button>'
    )

    coord_modals = '''
  <!-- MODAL DE DICTAMEN DE CONTINGENCIA (Transversal 01) -->
  <div id="dictamenModal" class="hidden fixed inset-0 bg-black/50 backdrop-blur-xs z-50 flex items-center justify-center p-4 animate-in fade-in duration-150">
    <div class="bg-white rounded-2xl shadow-modal max-w-md w-full overflow-hidden border border-umb-border">
      <div class="p-6 bg-gradient-to-r from-umb-surface to-white border-b border-umb-border flex items-center gap-3">
        <div class="w-12 h-12 rounded-xl bg-umb-guinda text-white flex items-center justify-center font-bold">
          <span class="material-symbols-outlined text-[24px]">gavel</span>
        </div>
        <div>
          <h3 class="text-sm font-bold text-slate-900 leading-tight">Emitir Dictamen de Coordinación</h3>
          <p class="text-[11px] text-slate-500" id="dictamenSubTitle">Resolución reglamentaria de caso</p>
        </div>
      </div>
      <div class="p-5 space-y-3 text-xs text-slate-700">
        <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
          <p class="font-semibold text-slate-900" id="dictamenStudent">Alumno: ...</p>
          <p class="text-slate-500 mt-0.5" id="dictamenDetail">Resolución: ...</p>
        </div>
        <div>
          <label class="block font-semibold text-slate-700 mb-1">Observaciones en acta:</label>
          <textarea rows="2" class="w-full p-2.5 rounded-xl border border-slate-300 outline-none focus:ring-2 focus:ring-umb-guinda" placeholder="Dictamen favorable conforme al Art. 45 del Reglamento de Residencias."></textarea>
        </div>
      </div>
      <div class="p-4 bg-slate-50 border-t border-slate-200 flex items-center justify-end gap-2.5">
        <button type="button" onclick="closeDictamenModal()" class="h-10 px-4 rounded-xl border border-slate-300 bg-white text-slate-700 font-semibold text-xs">Cancelar</button>
        <button type="button" onclick="confirmDictamen()" class="h-10 px-5 rounded-xl bg-umb-guinda hover:bg-umb-guinda-dark text-white font-semibold text-xs shadow-sm flex items-center gap-1.5">
          <span class="material-symbols-outlined text-[18px]">verified</span>
          <span>Firmar dictamen</span>
        </button>
      </div>
    </div>
  </div>

  <!-- TOAST FLOTANTE COORDINACIÓN (Transversal 03) -->
  <div id="coordToast" class="fixed top-20 right-6 z-50 bg-slate-900 text-white px-5 py-3.5 rounded-2xl shadow-2xl flex items-center gap-3 border border-slate-700 transform -translate-y-12 opacity-0 transition-all duration-300 pointer-events-none max-w-md">
    <div class="w-9 h-9 rounded-xl bg-emerald-600 flex items-center justify-center text-white shrink-0 shadow-xs">
      <span class="material-symbols-outlined text-[20px]">verified</span>
    </div>
    <div class="text-xs">
      <p class="font-bold text-white text-sm" id="coordToastTitle">Dictamen Registrado</p>
      <p class="text-slate-300 text-[11px] mt-0.5" id="coordToastMessage">El expediente de contingencia fue actualizado.</p>
    </div>
  </div>

  <script>
    function openDictamenModal(student, motive, hours) {
      document.getElementById('dictamenStudent').textContent = 'Estudiante: ' + student;
      document.getElementById('dictamenDetail').textContent = motive + ' · ' + hours;
      document.getElementById('dictamenModal').classList.remove('hidden');
    }
    function closeDictamenModal() {
      document.getElementById('dictamenModal').classList.add('hidden');
    }
    function confirmDictamen() {
      closeDictamenModal();
      const toast = document.getElementById('coordToast');
      toast.classList.remove('-translate-y-12', 'opacity-0', 'pointer-events-none');
      setTimeout(() => {
        toast.classList.add('-translate-y-12', 'opacity-0', 'pointer-events-none');
      }, 3500);
    }
  </script>
'''

    ccontent = ccontent.replace('</body>', coord_modals + '\n</body>')
    with open(f_contingencias, 'w', encoding='utf-8') as f:
        f.write(ccontent)
    print("Enhanced 06-coordinacion/04-contingencias.html with interactive Dictamen Modal & Toast!")
