import os
import re

print("Starting integration of transversal interactive modals and toasts...")

# 1. ENHANCE 05-control-escolar/06-catalogo-empresas.html
f_empresas = 'sigres-umb/05-control-escolar/06-catalogo-empresas.html'
if os.path.exists(f_empresas):
    with open(f_empresas, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add interactive action buttons to each company card
    # Add delete button to Empresa 1
    content = content.replace(
        '''<div class="flex items-center gap-2">
                    <button type="button" class="h-9 px-3 rounded-lg border border-umb-border hover:bg-umb-surface text-umb-carbon text-xs font-medium flex items-center gap-1.5 transition-colors">
                      <span class="material-symbols-outlined text-[16px]">visibility</span>
                      <span>Convenio PDF</span>
                    </button>
                    <button type="button" class="h-9 px-3.5 rounded-lg bg-umb-guinda hover:bg-umb-guinda-dark text-white text-xs font-semibold flex items-center gap-1.5 transition-colors shadow-xs">
                      <span class="material-symbols-outlined text-[16px]">edit</span>
                      <span>Gestionar</span>
                    </button>
                  </div>''',
        '''<div class="flex items-center gap-2">
                    <button type="button" onclick="openViewConvenio('Universidad Mexiquense del Bicentenario · Dirección Académica', 'CV-2024-042')" class="h-9 px-3 rounded-lg border border-umb-border hover:bg-umb-surface text-umb-carbon text-xs font-medium flex items-center gap-1.5 transition-colors" title="Ver archivo de convenio">
                      <span class="material-symbols-outlined text-[16px]">visibility</span>
                      <span>Convenio PDF</span>
                    </button>
                    <button type="button" onclick="openEditCompany('empresa-1', 'Universidad Mexiquense del Bicentenario · Dirección Académica', 'UMB0802209L5', 'Mtro. Armando Alcalde Martínez', '5')" class="h-9 px-3.5 rounded-lg bg-white border border-umb-border hover:bg-umb-surface text-umb-carbon text-xs font-semibold flex items-center gap-1.5 transition-colors shadow-xs" title="Modificar datos de empresa">
                      <span class="material-symbols-outlined text-[16px]">edit</span>
                      <span>Editar</span>
                    </button>
                    <button type="button" onclick="openDeleteModal('empresa-1', 'Universidad Mexiquense del Bicentenario · Dirección Académica', 'CV-2024-042')" class="h-9 px-3 rounded-lg border border-rose-200 text-rose-700 bg-rose-50/70 hover:bg-rose-100 text-xs font-semibold flex items-center gap-1.5 transition-colors shadow-xs" title="Dar de baja convenio de esta empresa">
                      <span class="material-symbols-outlined text-[16px]">delete</span>
                      <span>Baja</span>
                    </button>
                  </div>'''
    )

    # Add id to Empresa 1
    content = content.replace(
        '<!-- EMPRESA 1: UMB Dirección Académica (Sede de Jesús Andrés Mondragón) -->\n            <article class="bg-white rounded-xl border border-umb-border',
        '<!-- EMPRESA 1: UMB Dirección Académica (Sede de Jesús Andrés Mondragón) -->\n            <article id="empresa-1" class="bg-white rounded-xl border border-umb-border'
    )

    # Add buttons to Empresa 2
    content = content.replace(
        '<!-- EMPRESA 2: Sistemas Inteligentes de Toluca -->\n            <article class="bg-white rounded-xl border border-umb-border',
        '<!-- EMPRESA 2: Sistemas Inteligentes de Toluca -->\n            <article id="empresa-2" class="bg-white rounded-xl border border-umb-border'
    )

    # Add delete button to Empresa 2 and 3
    btn_replacement_2 = '''<div class="flex items-center gap-2">
                    <button type="button" onclick="openViewConvenio('Sistemas Inteligentes de Toluca S.A.P.I. de C.V.', 'CV-2023-018')" class="h-9 px-3 rounded-lg border border-umb-border hover:bg-umb-surface text-umb-carbon text-xs font-medium flex items-center gap-1.5 transition-colors">
                      <span class="material-symbols-outlined text-[16px]">visibility</span>
                      <span>Convenio PDF</span>
                    </button>
                    <button type="button" onclick="openEditCompany('empresa-2', 'Sistemas Inteligentes de Toluca S.A.P.I. de C.V.', 'SIT180914GH2', 'Ing. Roberto Morales Cruz', '6')" class="h-9 px-3.5 rounded-lg bg-white border border-umb-border hover:bg-umb-surface text-umb-carbon text-xs font-semibold flex items-center gap-1.5 transition-colors shadow-xs">
                      <span class="material-symbols-outlined text-[16px]">edit</span>
                      <span>Editar</span>
                    </button>
                    <button type="button" onclick="openDeleteModal('empresa-2', 'Sistemas Inteligentes de Toluca S.A.P.I. de C.V.', 'CV-2023-018')" class="h-9 px-3 rounded-lg border border-rose-200 text-rose-700 bg-rose-50/70 hover:bg-rose-100 text-xs font-semibold flex items-center gap-1.5 transition-colors shadow-xs">
                      <span class="material-symbols-outlined text-[16px]">delete</span>
                      <span>Baja</span>
                    </button>
                  </div>'''

    content = re.sub(
        r'<div class="flex items-center gap-2">\s*<button[^>]*>\s*<span[^>]*>visibility</span>\s*<span>Convenio PDF</span>\s*</button>\s*<button[^>]*>\s*<span[^>]*>edit</span>\s*<span>Gestionar</span>\s*</button>\s*</div>',
        btn_replacement_2,
        content,
        count=1
    )

    # Insert Modals (Delete Modal, Edit Modal, Empty state toggle, Toast notification) before </body>
    modals_html = '''
  <!-- MODAL DE ELIMINACIÓN / DAR DE BAJA CONVENIO (Transversal 02) -->
  <div id="deleteModal" class="hidden fixed inset-0 bg-black/60 backdrop-blur-xs z-50 flex items-center justify-center p-4 animate-in fade-in duration-150" aria-modal="true" role="dialog">
    <div class="bg-white rounded-2xl shadow-modal max-w-md w-full overflow-hidden border border-rose-200 animate-in zoom-in-95 duration-150" onclick="event.stopPropagation()">
      
      <!-- Cabecera del modal de eliminación -->
      <div class="p-6 text-center bg-gradient-to-b from-rose-50 to-white border-b border-rose-100">
        <div class="w-14 h-14 rounded-2xl bg-rose-100 text-rose-700 border border-rose-200 flex items-center justify-center mx-auto mb-3 shadow-inner">
          <span class="material-symbols-outlined text-[32px]">warning</span>
        </div>
        <h3 class="text-base font-bold text-slate-900 leading-tight">¿Dar de baja convenio institucional?</h3>
        <p class="text-xs text-slate-600 mt-1.5" id="deleteModalDesc">
          Estás a punto de dar de baja el convenio de <strong id="deleteTargetName" class="text-rose-900">...</strong>.
        </p>
      </div>

      <!-- Cuerpo del modal -->
      <div class="p-6 space-y-4">
        <div class="p-3.5 bg-amber-50 rounded-xl border border-amber-200 text-xs text-amber-900 flex items-start gap-2.5">
          <span class="material-symbols-outlined text-amber-600 text-[20px] shrink-0">info</span>
          <p class="leading-relaxed">
            Se revocarán los registros del catálogo y se notificará a Coordinación de Carrera. Esta acción quedará asentada en el libro de auditoría.
          </p>
        </div>

        <div>
          <label class="block text-xs font-semibold text-slate-700 mb-1.5">Motivo reglamentario de la baja:</label>
          <select id="deleteReason" class="w-full h-10 px-3 rounded-xl border border-slate-300 text-xs bg-white focus:ring-2 focus:ring-rose-500 outline-none">
            <option value="vencimiento">Conclusión del periodo trianual de convenio</option>
            <option value="cambio_razon">Cambio de razón social / Reestructuración jurídica</option>
            <option value="solicitud_empresa">Solicitud expresa de la unidad receptora</option>
            <option value="incumplimiento">Incumplimiento de cláusulas de residencia</option>
          </select>
        </div>
      </div>

      <!-- Botones de acción -->
      <div class="p-4 bg-slate-50 border-t border-slate-200 flex items-center justify-end gap-2.5">
        <button type="button" onclick="closeDeleteModal()" class="h-10 px-4 rounded-xl border border-slate-300 hover:bg-white text-slate-700 font-semibold text-xs transition">
          Cancelar
        </button>
        <button type="button" id="confirmDeleteBtn" onclick="confirmDeleteCompany()" class="h-10 px-5 rounded-xl bg-rose-700 hover:bg-rose-800 text-white font-semibold text-xs shadow-sm transition flex items-center gap-1.5">
          <span class="material-symbols-outlined text-[18px]">delete</span>
          <span>Confirmar baja de convenio</span>
        </button>
      </div>

    </div>
  </div>

  <!-- MODAL DE EDICIÓN / GESTIÓN DE EMPRESA (Transversal) -->
  <div id="editCompanyModal" class="hidden fixed inset-0 bg-black/50 backdrop-blur-xs z-50 flex items-center justify-center p-4 animate-in fade-in duration-150" aria-modal="true" role="dialog">
    <div class="bg-white rounded-2xl shadow-modal max-w-lg w-full overflow-hidden border border-umb-border animate-in zoom-in-95 duration-150" onclick="event.stopPropagation()">
      
      <div class="p-5 bg-gradient-to-r from-umb-surface to-white border-b border-umb-border flex items-center justify-between">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-xl bg-umb-guinda text-white flex items-center justify-center shadow-xs font-bold text-sm">
            <span class="material-symbols-outlined text-[20px]">domain</span>
          </div>
          <div>
            <h3 class="text-sm font-bold text-slate-900 leading-tight">Editar Datos de la Empresa</h3>
            <p class="text-[11px] text-slate-500">Actualización de ficha en catálogo institucional</p>
          </div>
        </div>
        <button type="button" onclick="closeEditModal()" class="w-8 h-8 rounded-lg text-slate-400 hover:text-slate-700 flex items-center justify-center">
          <span class="material-symbols-outlined text-[20px]">close</span>
        </button>
      </div>

      <div class="p-6 space-y-4 text-xs">
        <div>
          <label class="block font-semibold text-slate-700 mb-1">Razón Social</label>
          <input type="text" id="editNameInput" class="w-full h-10 px-3 rounded-xl border border-slate-300 font-medium focus:ring-2 focus:ring-umb-guinda outline-none">
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block font-semibold text-slate-700 mb-1">RFC</label>
            <input type="text" id="editRfcInput" class="w-full h-10 px-3 rounded-xl border border-slate-300 font-mono focus:ring-2 focus:ring-umb-guinda outline-none">
          </div>
          <div>
            <label class="block font-semibold text-slate-700 mb-1">Capacidad máxima</label>
            <input type="number" id="editCapInput" class="w-full h-10 px-3 rounded-xl border border-slate-300 font-medium focus:ring-2 focus:ring-umb-guinda outline-none">
          </div>
        </div>
        <div>
          <label class="block font-semibold text-slate-700 mb-1">Titular / Asesor Externo</label>
          <input type="text" id="editTitularInput" class="w-full h-10 px-3 rounded-xl border border-slate-300 font-medium focus:ring-2 focus:ring-umb-guinda outline-none">
        </div>
      </div>

      <div class="p-4 bg-slate-50 border-t border-slate-200 flex items-center justify-end gap-2.5">
        <button type="button" onclick="closeEditModal()" class="h-10 px-4 rounded-xl border border-slate-300 bg-white text-slate-700 font-semibold text-xs transition">
          Cancelar
        </button>
        <button type="button" onclick="saveCompanyEdit()" class="h-10 px-5 rounded-xl bg-umb-guinda hover:bg-umb-guinda-dark text-white font-semibold text-xs shadow-sm transition flex items-center gap-1.5">
          <span class="material-symbols-outlined text-[18px]">save</span>
          <span>Guardar cambios</span>
        </button>
      </div>

    </div>
  </div>

  <!-- TOAST FLOTANTE DE NOTIFICACIÓN INSTITUCIONAL (Transversal 03) -->
  <div id="interactiveToast" class="fixed top-20 right-6 z-50 bg-slate-900 text-white px-5 py-3.5 rounded-2xl shadow-2xl flex items-center gap-3 border border-slate-700 transform -translate-y-12 opacity-0 transition-all duration-300 pointer-events-none max-w-md">
    <div id="toastIconContainer" class="w-9 h-9 rounded-xl bg-emerald-600 flex items-center justify-center text-white shrink-0 shadow-xs">
      <span class="material-symbols-outlined text-[20px]" id="toastIcon">check_circle</span>
    </div>
    <div class="text-xs">
      <p class="font-bold text-white text-sm" id="toastTitle">Acción completada</p>
      <p class="text-slate-300 text-[11px] mt-0.5" id="toastMessage">La operación se registró con éxito en SIGRES-UMB.</p>
    </div>
  </div>

  <!-- JS INTERACTIVO PARA MODALES Y TOASTS EN CATÁLOGO DE EMPRESAS -->
  <script>
    let currentDeleteId = '';

    function openDeleteModal(id, name, convenio) {
      currentDeleteId = id;
      document.getElementById('deleteTargetName').textContent = name + ' (' + convenio + ')';
      document.getElementById('deleteModal').classList.remove('hidden');
    }

    function closeDeleteModal() {
      document.getElementById('deleteModal').classList.add('hidden');
    }

    function confirmDeleteCompany() {
      const btn = document.getElementById('confirmDeleteBtn');
      btn.disabled = true;
      btn.innerHTML = '<span class="material-symbols-outlined text-[18px] animate-spin">progress_activity</span> Procesando baja...';

      setTimeout(() => {
        closeDeleteModal();
        btn.disabled = false;
        btn.innerHTML = '<span class="material-symbols-outlined text-[18px]">delete</span><span>Confirmar baja de convenio</span>';

        if (currentDeleteId) {
          const card = document.getElementById(currentDeleteId);
          if (card) {
            card.style.opacity = '0';
            card.style.transform = 'scale(0.95)';
            card.style.transition = 'all 0.4s ease';
            setTimeout(() => card.remove(), 400);
          }
        }

        showToast('Convenio dado de baja', 'El convenio fue removido del catálogo institucional de forma satisfactoria.', 'success');
      }, 700);
    }

    let currentEditId = '';
    function openEditCompany(id, name, rfc, titular, cap) {
      currentEditId = id;
      document.getElementById('editNameInput').value = name;
      document.getElementById('editRfcInput').value = rfc;
      document.getElementById('editTitularInput').value = titular;
      document.getElementById('editCapInput').value = cap;
      document.getElementById('editCompanyModal').classList.remove('hidden');
    }

    function closeEditModal() {
      document.getElementById('editCompanyModal').classList.add('hidden');
    }

    function saveCompanyEdit() {
      closeEditModal();
      showToast('Empresa actualizada', 'Los datos del convenio y capacidad fueron guardados correctamente.', 'info');
    }

    function openViewConvenio(name, folio) {
      showToast('Convenio consultado', 'Abriendo anexo técnico y convenio ' + folio + ' de ' + name, 'info');
    }

    function showToast(title, message, type = 'success') {
      const toast = document.getElementById('interactiveToast');
      const toastTitle = document.getElementById('toastTitle');
      const toastMessage = document.getElementById('toastMessage');
      const toastIcon = document.getElementById('toastIcon');
      const iconContainer = document.getElementById('toastIconContainer');

      toastTitle.textContent = title;
      toastMessage.textContent = message;

      if (type === 'success') {
        iconContainer.className = 'w-9 h-9 rounded-xl bg-emerald-600 flex items-center justify-center text-white shrink-0 shadow-xs';
        toastIcon.textContent = 'check_circle';
      } else if (type === 'info') {
        iconContainer.className = 'w-9 h-9 rounded-xl bg-umb-guinda flex items-center justify-center text-white shrink-0 shadow-xs';
        toastIcon.textContent = 'info';
      }

      toast.classList.remove('-translate-y-12', 'opacity-0', 'pointer-events-none');
      setTimeout(() => {
        toast.classList.add('-translate-y-12', 'opacity-0', 'pointer-events-none');
      }, 3500);
    }
  </script>
'''

    content = content.replace('</body>', modals_html + '\n</body>')
    with open(f_empresas, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Enhanced 05-control-escolar/06-catalogo-empresas.html with interactive Delete Modal, Edit Modal & Toast!")

# 2. ENHANCE 05-control-escolar/04-validar-documentos.html
f_valdocs = 'sigres-umb/05-control-escolar/04-validar-documentos.html'
if os.path.exists(f_valdocs):
    with open(f_valdocs, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add Action Buttons bar at the bottom of the workspace
    action_bar_html = '''
      <!-- BARRA FLOTANTE DE ACCIONES DE VALIDACIÓN (Transversales 01 y 03) -->
      <div class="sticky bottom-0 bg-white/95 backdrop-blur-md border-t border-slate-200 p-4 px-6 flex flex-wrap items-center justify-between gap-3 shadow-lg z-30">
        <div class="flex items-center gap-2 text-xs text-slate-700">
          <span class="material-symbols-outlined text-amber-600 text-[20px]">assignment</span>
          <span>Documento activo: <strong>kardex_jesus_mondragon_9sem.pdf</strong></span>
          <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-amber-100 text-amber-800" id="currentDocStatusBadge">Pendiente cotejo</span>
        </div>

        <div class="flex items-center gap-2.5">
          <button type="button" onclick="openRejectModal('Historial Académico (Kárdex)', 'kardex_jesus_mondragon_9sem.pdf')" class="h-10 px-4 rounded-xl border border-rose-200 text-rose-700 bg-rose-50 hover:bg-rose-100 text-xs font-semibold flex items-center gap-1.5 transition-colors shadow-xs">
            <span class="material-symbols-outlined text-[18px]">cancel</span>
            <span>Solicitar corrección</span>
          </button>
          <button type="button" onclick="openApproveModal('Historial Académico (Kárdex)', 'kardex_jesus_mondragon_9sem.pdf')" class="h-10 px-5 rounded-xl bg-[#2D8C4E] hover:bg-emerald-700 text-white text-xs font-semibold flex items-center gap-1.5 transition-colors shadow-sm">
            <span class="material-symbols-outlined text-[18px]">verified</span>
            <span>Aprobar y cotejar documento</span>
          </button>
        </div>
      </div>
'''

    # Insert action_bar before footer in main
    content = content.replace(
        '<!-- BEGIN: BottomValidationBar -->',
        action_bar_html + '\n<!-- BEGIN: BottomValidationBar -->'
    )

    # Insert modals and scripts
    val_modals = '''
  <!-- MODAL DE CONFIRMACIÓN DE APROBACIÓN (Transversal 01) -->
  <div id="approveModal" class="hidden fixed inset-0 bg-black/50 backdrop-blur-xs z-50 flex items-center justify-center p-4 animate-in fade-in duration-150">
    <div class="bg-white rounded-2xl shadow-modal max-w-md w-full overflow-hidden border border-emerald-200">
      <div class="p-6 text-center bg-gradient-to-b from-emerald-50 to-white border-b border-emerald-100">
        <div class="w-14 h-14 rounded-2xl bg-emerald-100 text-emerald-700 border border-emerald-200 flex items-center justify-center mx-auto mb-3 shadow-inner">
          <span class="material-symbols-outlined text-[32px]">verified</span>
        </div>
        <h3 class="text-base font-bold text-slate-900 leading-tight">¿Aprobar y cotejar documento?</h3>
        <p class="text-xs text-slate-600 mt-1.5" id="approveDocName">Historial académico de Jesús Andrés Mondragón Tenorio</p>
      </div>
      <div class="p-5 text-xs text-slate-700 space-y-3">
        <div class="p-3 bg-emerald-50/70 rounded-xl border border-emerald-200 flex items-center gap-2">
          <span class="material-symbols-outlined text-emerald-700 text-[20px]">check_circle</span>
          <span>Se estampará el sello digital de <strong>Cotejado y Validado por Control Escolar</strong>.</span>
        </div>
      </div>
      <div class="p-4 bg-slate-50 border-t border-slate-200 flex items-center justify-end gap-2.5">
        <button type="button" onclick="closeApproveModal()" class="h-10 px-4 rounded-xl border border-slate-300 bg-white text-slate-700 font-semibold text-xs">Cancelar</button>
        <button type="button" onclick="confirmApproveDoc()" class="h-10 px-5 rounded-xl bg-emerald-700 hover:bg-emerald-800 text-white font-semibold text-xs shadow-sm flex items-center gap-1.5">
          <span class="material-symbols-outlined text-[18px]">check</span>
          <span>Aprobar documento</span>
        </button>
      </div>
    </div>
  </div>

  <!-- MODAL DE SOLICITUD DE CORRECCIÓN / RECHAZO (Transversal) -->
  <div id="rejectModal" class="hidden fixed inset-0 bg-black/50 backdrop-blur-xs z-50 flex items-center justify-center p-4 animate-in fade-in duration-150">
    <div class="bg-white rounded-2xl shadow-modal max-w-md w-full overflow-hidden border border-rose-200">
      <div class="p-5 bg-gradient-to-r from-rose-50 to-white border-b border-rose-100 flex items-center gap-3">
        <div class="w-10 h-10 rounded-xl bg-rose-100 text-rose-700 flex items-center justify-center font-bold">
          <span class="material-symbols-outlined text-[20px]">report</span>
        </div>
        <div>
          <h3 class="text-sm font-bold text-slate-900 leading-tight">Solicitar corrección de documento</h3>
          <p class="text-[11px] text-slate-500">Notificación inmediata al estudiante</p>
        </div>
      </div>
      <div class="p-5 space-y-3 text-xs">
        <div>
          <label class="block font-semibold text-slate-700 mb-1">Observaciones para el estudiante:</label>
          <textarea id="rejectNotes" rows="3" class="w-full p-2.5 rounded-xl border border-slate-300 outline-none focus:ring-2 focus:ring-rose-500" placeholder="Ej. El kárdex adjunto no cuenta con sello legible de la Unidad Académica."></textarea>
        </div>
      </div>
      <div class="p-4 bg-slate-50 border-t border-slate-200 flex items-center justify-end gap-2.5">
        <button type="button" onclick="closeRejectModal()" class="h-10 px-4 rounded-xl border border-slate-300 bg-white text-slate-700 font-semibold text-xs">Cancelar</button>
        <button type="button" onclick="confirmRejectDoc()" class="h-10 px-5 rounded-xl bg-rose-700 hover:bg-rose-800 text-white font-semibold text-xs shadow-sm flex items-center gap-1.5">
          <span class="material-symbols-outlined text-[18px]">send</span>
          <span>Enviar observaciones</span>
        </button>
      </div>
    </div>
  </div>

  <!-- TOAST FLOTANTE INSTITUCIONAL (Transversal 03) -->
  <div id="valToast" class="fixed top-20 right-6 z-50 bg-slate-900 text-white px-5 py-3.5 rounded-2xl shadow-2xl flex items-center gap-3 border border-slate-700 transform -translate-y-12 opacity-0 transition-all duration-300 pointer-events-none max-w-md">
    <div id="valToastIconContainer" class="w-9 h-9 rounded-xl bg-emerald-600 flex items-center justify-center text-white shrink-0 shadow-xs">
      <span class="material-symbols-outlined text-[20px]" id="valToastIcon">check_circle</span>
    </div>
    <div class="text-xs">
      <p class="font-bold text-white text-sm" id="valToastTitle">Acción registrada</p>
      <p class="text-slate-300 text-[11px] mt-0.5" id="valToastMessage">Estatus del expediente actualizado.</p>
    </div>
  </div>

  <script>
    function openApproveModal(docName, file) {
      document.getElementById('approveDocName').textContent = docName + ' (' + file + ')';
      document.getElementById('approveModal').classList.remove('hidden');
    }
    function closeApproveModal() {
      document.getElementById('approveModal').classList.add('hidden');
    }
    function confirmApproveDoc() {
      closeApproveModal();
      const badge = document.getElementById('currentDocStatusBadge');
      if (badge) {
        badge.textContent = '✓ Validado y cotejado';
        badge.className = 'px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-100 text-emerald-800';
      }
      showValToast('Documento Validado', 'Se ha registrado el cotejo oficial del kárdex satisfactoriamente.', 'success');
    }

    function openRejectModal(docName, file) {
      document.getElementById('rejectModal').classList.remove('hidden');
    }
    function closeRejectModal() {
      document.getElementById('rejectModal').classList.add('hidden');
    }
    function confirmRejectDoc() {
      closeRejectModal();
      const badge = document.getElementById('currentDocStatusBadge');
      if (badge) {
        badge.textContent = '⚠️ Observación enviada';
        badge.className = 'px-2 py-0.5 rounded-full text-[10px] font-bold bg-rose-100 text-rose-800';
      }
      showValToast('Observaciones Notificadas', 'Se notificó al estudiante para que reemplace el archivo digital.', 'info');
    }

    function showValToast(title, message, type = 'success') {
      const toast = document.getElementById('valToast');
      document.getElementById('valToastTitle').textContent = title;
      document.getElementById('valToastMessage').textContent = message;
      const icon = document.getElementById('valToastIcon');
      const iconCont = document.getElementById('valToastIconContainer');
      if (type === 'success') {
        iconCont.className = 'w-9 h-9 rounded-xl bg-emerald-600 flex items-center justify-center text-white shrink-0';
        icon.textContent = 'verified';
      } else {
        iconCont.className = 'w-9 h-9 rounded-xl bg-amber-600 flex items-center justify-center text-white shrink-0';
        icon.textContent = 'info';
      }
      toast.classList.remove('-translate-y-12', 'opacity-0', 'pointer-events-none');
      setTimeout(() => {
        toast.classList.add('-translate-y-12', 'opacity-0', 'pointer-events-none');
      }, 3500);
    }
  </script>
'''

    content = content.replace('</body>', val_modals + '\n</body>')
    with open(f_valdocs, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Enhanced 05-control-escolar/04-validar-documentos.html with interactive Document Approval & Rejection modals!")

# 3. ENHANCE 02-estudiante/09-nueva-bitacora.html with LIVE SYNC BAR (Transversal 08) and Submit Modal
f_bitacora = 'sigres-umb/02-estudiante/09-nueva-bitacora.html'
if os.path.exists(f_bitacora):
    with open(f_bitacora, 'r', encoding='utf-8') as f:
        bcontent = f.read()

    # Add live synchronization bar banner at top of form
    sync_bar_html = '''
        <!-- BARRA DE SINCRONIZACIÓN Y GUARDADO AUTOMÁTICO EN VIVO (Transversal 08) -->
        <section class="bg-white rounded-xl border border-slate-200 p-3.5 px-4 shadow-xs flex items-center justify-between gap-3 mb-6" id="syncStatusSection">
          <div class="flex items-center gap-2.5">
            <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse" id="syncIndicatorDot"></span>
            <span class="text-xs font-semibold text-slate-800" id="syncStatusTitle">Borrador sincronizado</span>
            <span class="text-slate-400 text-xs hidden sm:inline">·</span>
            <span class="text-xs text-slate-500 hidden sm:inline" id="syncStatusTime">Guardado automático hace 12 segundos</span>
          </div>
          <button type="button" onclick="triggerManualSync()" class="h-8 px-3 rounded-lg border border-slate-200 hover:bg-slate-50 text-slate-700 text-xs font-medium flex items-center gap-1.5 transition">
            <span class="material-symbols-outlined text-[16px] text-slate-500" id="syncSpinIcon">sync</span>
            <span>Guardar ahora</span>
          </button>
        </section>
'''
    bcontent = bcontent.replace(
        '<main class="lg:ml-[260px] flex-1 p-6 md:p-8 max-w-[1280px] w-full mx-auto space-y-6 min-w-0 pb-24 lg:pb-8">',
        '<main class="lg:ml-[260px] flex-1 p-6 md:p-8 max-w-[1280px] w-full mx-auto space-y-6 min-w-0 pb-24 lg:pb-8">\n' + sync_bar_html
    )

    # Add sync script before </body>
    bcontent = bcontent.replace(
        '</body>',
        '''  <!-- Script de Sincronización y Guardado en Vivo -->
  <script>
    function triggerManualSync() {
      const dot = document.getElementById('syncIndicatorDot');
      const title = document.getElementById('syncStatusTitle');
      const time = document.getElementById('syncStatusTime');
      const icon = document.getElementById('syncSpinIcon');

      dot.className = 'w-2.5 h-2.5 rounded-full bg-amber-500 animate-ping';
      title.textContent = 'Sincronizando con la nube institucional...';
      icon.classList.add('animate-spin');

      setTimeout(() => {
        dot.className = 'w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse';
        title.textContent = 'Borrador guardado exitosamente';
        time.textContent = 'Guardado ahora mismo (' + new Date().toLocaleTimeString() + ')';
        icon.classList.remove('animate-spin');
      }, 700);
    }
  </script>
</body>'''
    )

    with open(f_bitacora, 'w', encoding='utf-8') as f:
        f.write(bcontent)
    print("Enhanced 02-estudiante/09-nueva-bitacora.html with live sync bar!")

print("All transversal integrations completed!")
