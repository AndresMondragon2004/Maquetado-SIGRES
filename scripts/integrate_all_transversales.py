import os
import re

print("Starting complete integration of transversal components across target screens...")

# =========================================================================
# HELPER SNIPPETS
# =========================================================================

TOAST_CONTAINER_HTML = '''
  <!-- CONTENEDOR DE NOTIFICACIONES TOAST (Transversal 03) -->
  <section id="toastContainer" aria-live="polite" aria-label="Notificaciones del sistema" class="fixed bottom-6 right-6 z-50 flex flex-col-reverse gap-3 max-w-[420px] w-[calc(100vw-48px)] sm:w-[400px] pointer-events-none"></section>
'''

TOAST_JS_HELPER = '''
    // HELPER GLOBAL TOAST NOTIFICACIONES (Transversal 03)
    function showToast(title, message, type = 'success', actionText = null, actionCallback = null) {
      const container = document.getElementById('toastContainer');
      if (!container) return;

      const toastId = 'toast-' + Date.now();
      const toast = document.createElement('div');
      toast.id = toastId;
      toast.className = 'pointer-events-auto bg-white rounded-lg p-4 custom-shadow border-l-4 flex items-start justify-between gap-3 animate-in fade-in slide-in-from-bottom-5 duration-200 relative overflow-hidden transition-all';
      
      let borderClass = 'border-[#2D8C4E]';
      let iconBg = 'bg-[#DCFCE7] text-[#2D8C4E]';
      let iconName = 'check_circle';
      let timerBg = 'bg-[#2D8C4E]';

      if (type === 'error' || type === 'danger') {
        borderClass = 'border-[#C53030]';
        iconBg = 'bg-[#FEE2E2] text-[#C53030]';
        iconName = 'error';
        timerBg = 'bg-[#C53030]';
      } else if (type === 'warning') {
        borderClass = 'border-[#D69E2E]';
        iconBg = 'bg-[#FEF3C7] text-[#D69E2E]';
        iconName = 'warning';
        timerBg = 'bg-[#D69E2E]';
      } else if (type === 'info') {
        borderClass = 'border-[#2B6CB0]';
        iconBg = 'bg-[#EFF6FF] text-[#2B6CB0]';
        iconName = 'info';
        timerBg = 'bg-[#2B6CB0]';
      }

      toast.classList.add(borderClass);

      toast.innerHTML = `
        <div class="flex-shrink-0 w-6 h-6 rounded-full ${iconBg} flex items-center justify-center mt-0.5">
          <span class="material-symbols-outlined text-[16px]">${iconName}</span>
        </div>
        <div class="flex-1 min-w-0 pr-1">
          <h3 class="text-sm font-semibold text-umb-carbon leading-tight">${title}</h3>
          <p class="text-xs text-umb-muted mt-0.5 leading-normal">${message}</p>
        </div>
        <div class="flex items-center space-x-1.5 flex-shrink-0">
          ${actionText ? `<button type="button" class="text-xs font-semibold text-umb-guinda hover:underline px-1.5 py-1">${actionText}</button>` : ''}
          <button type="button" onclick="closeToast('${toastId}')" class="text-umb-outline hover:text-umb-carbon p-1 rounded hover:bg-gray-100 transition" title="Cerrar">
            <span class="material-symbols-outlined text-[16px]">close</span>
          </button>
        </div>
        <div class="absolute bottom-0 left-0 h-[2px] bg-black/5 w-full">
          <div class="h-full ${timerBg} transition-all duration-4000 ease-linear" style="width: 100%;" id="timer-${toastId}"></div>
        </div>
      `;

      container.appendChild(toast);

      setTimeout(() => {
        const timer = document.getElementById(`timer-${toastId}`);
        if (timer) timer.style.width = '0%';
      }, 50);

      setTimeout(() => {
        closeToast(toastId);
      }, 4000);
    }

    function closeToast(id) {
      const toast = document.getElementById(id);
      if (toast) {
        toast.classList.add('opacity-0', 'translate-y-2');
        setTimeout(() => toast.remove(), 200);
      }
    }
'''

# =========================================================================
# 1. 02-estudiante/01-dashboard.html
# =========================================================================
f_dash_est = 'sigres-umb/02-estudiante/01-dashboard.html'
if os.path.exists(f_dash_est):
    with open(f_dash_est, 'r', encoding='utf-8') as f:
        c = f.read()

    # 1.1 Insert PWA Sync Banner right after </header>
    if 'id="pwaSyncBanner"' not in c:
        pwa_banner = '''
  <!-- ================= BARRA DE SINCRONIZACIÓN PWA (Transversal 08) ================= -->
  <div id="pwaSyncBanner" class="hidden w-full bg-umb-dorado-light border-b border-[#FDE68A] transition-all duration-300 relative z-30">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-10 flex items-center justify-between text-xs sm:text-[13px] font-medium text-[#92400E]">
      <div class="flex items-center gap-2.5 overflow-hidden">
        <span class="material-symbols-outlined text-[18px] text-[#92400E] shrink-0 animate-pulse">wifi_off</span>
        <span class="truncate">Modo sin conexión activo · 3 bitácoras pendientes de sincronizar</span>
      </div>
      <div class="flex items-center gap-2 shrink-0">
        <button type="button" onclick="syncPwaData()" class="px-2.5 py-1 rounded bg-[#D69E2E] hover:bg-[#B45309] text-white text-xs font-semibold shadow-xs transition-colors flex items-center gap-1 cursor-pointer">
          <span class="material-symbols-outlined text-[14px]">sync</span>
          <span class="hidden sm:inline">Sincronizar ahora</span>
        </button>
      </div>
    </div>
  </div>
'''
        c = c.replace('</header>', '</header>' + pwa_banner, 1)

    # 1.2 Insert Botón 1 (Simular expiración) and Botón 2 (Simular offline) and Session Expired Modal
    if 'openSessionExpiredModal' not in c:
        demo_buttons_and_modal = '''
  <!-- Botón de demostración para el video — eliminar en producción -->
  <aside aria-label="Demostración de expiración de sesión" class="fixed bottom-6 left-6 z-50">
    <button type="button" onclick="openSessionExpiredModal()" class="h-10 px-4 rounded-full bg-umb-warning hover:bg-[#B45309] text-white text-xs font-bold shadow-xl border border-white/20 flex items-center gap-2 backdrop-blur-md transition-all hover:scale-105 focus:outline-none focus:ring-2 focus:ring-amber-400 cursor-pointer" title="Simular expiración de sesión por inactividad">
      <span class="material-symbols-outlined text-sm text-white">schedule</span>
      <span>Simular expiración</span>
    </button>
  </aside>

  <!-- Botón de demostración para el video — eliminar en producción -->
  <aside aria-label="Demostración de modo offline" class="fixed bottom-24 right-6 z-50">
    <button type="button" onclick="toggleOfflineMode()" title="Simular modo offline" class="w-12 h-12 rounded-full bg-umb-carbon hover:bg-neutral-800 text-white shadow-xl border border-white/20 flex items-center justify-center transition-all hover:scale-105 focus:outline-none focus:ring-2 focus:ring-umb-dorado cursor-pointer">
      <span id="offlineIcon" class="material-symbols-outlined text-[22px]">wifi_off</span>
    </button>
  </aside>

  <!-- MODAL DE SESIÓN EXPIRADA (Transversal 11) -->
  <div id="sessionExpiredModal" class="hidden fixed inset-0 z-50 flex items-center justify-center p-4 sm:p-6 backdrop-blur-md bg-black/60 animate-in fade-in duration-200" role="dialog" aria-modal="true">
    <div class="bg-white rounded-2xl shadow-modal border border-slate-200/80 max-w-md w-full overflow-hidden animate-in zoom-in-95 duration-200 text-slate-800" onclick="event.stopPropagation()">
      <div class="bg-gradient-to-r from-umb-guinda to-umb-guinda-dark p-6 text-white text-center relative">
        <div class="w-14 h-14 rounded-2xl bg-white/10 backdrop-blur-md border border-white/20 flex items-center justify-center mx-auto shadow-inner mb-3">
          <span class="material-symbols-outlined text-[32px] text-amber-300">lock_clock</span>
        </div>
        <h2 class="text-lg font-bold tracking-tight">Tu sesión está a punto de expirar</h2>
        <p class="text-xs text-white/80 mt-1">Por seguridad institucional debido a inactividad en el sistema.</p>
        <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-black/30 border border-white/15 text-xs font-mono font-semibold text-amber-300 mt-3 shadow-inner">
          <span class="w-2 h-2 rounded-full bg-amber-400 animate-ping"></span>
          <span>Tiempo restante: <strong id="timerDisplay">02:30</strong> min</span>
        </div>
      </div>
      <div class="p-6 space-y-4">
        <div class="bg-emerald-50 border border-emerald-200 rounded-xl p-3 flex items-start gap-2.5">
          <span class="material-symbols-outlined text-emerald-600 text-[20px] shrink-0 mt-0.5">verified_user</span>
          <div class="text-xs">
            <p class="font-bold text-emerald-950">Tus datos en captura están seguros</p>
            <p class="text-emerald-800 text-[11px] mt-0.5 leading-relaxed">El borrador de tu sesión se encuentra respaldado localmente.</p>
          </div>
        </div>
        <div class="flex items-center gap-3 p-3 bg-slate-50 rounded-xl border border-slate-200">
          <div class="w-9 h-9 rounded-full bg-umb-guinda text-white flex items-center justify-center font-bold text-xs">JM</div>
          <div class="flex-1 min-w-0">
            <p class="text-xs font-bold text-slate-900 truncate">Jesús Andrés Mondragón Tenorio</p>
            <p class="text-[11px] text-slate-500 font-mono">13220024 · Estudiante ISC</p>
          </div>
          <span class="text-[10px] font-semibold bg-slate-200 text-slate-700 px-2 py-0.5 rounded-full">Activo</span>
        </div>
        <form onsubmit="handleReauth(event)" class="space-y-3">
          <div>
            <label class="block text-xs font-semibold text-slate-700 mb-1">Contraseña de acceso institucional</label>
            <input type="password" id="sessionPassInput" placeholder="••••••••" required class="w-full px-3 py-2 text-xs border border-slate-300 rounded-lg focus:ring-2 focus:ring-umb-guinda focus:outline-none">
          </div>
          <div class="flex items-center justify-between gap-2 pt-2">
            <a href="../01-autenticacion/01-login.html" class="px-3 py-2 text-xs font-semibold text-slate-600 hover:text-slate-800">Cerrar sesión</a>
            <button type="submit" class="px-4 py-2 bg-umb-guinda hover:bg-umb-guinda-dark text-white font-semibold text-xs rounded-lg shadow-sm transition-colors">Reactivar sesión</button>
          </div>
        </form>
      </div>
    </div>
  </div>
''' + TOAST_CONTAINER_HTML

        js_addition = TOAST_JS_HELPER + '''
    // CONTROL DE DEMOSTRACIÓN: EXPIRACIÓN Y MODO OFFLINE
    let isOfflineActive = false;

    function openSessionExpiredModal() {
      const modal = document.getElementById('sessionExpiredModal');
      if (modal) modal.classList.remove('hidden');
    }

    function closeSessionExpiredModal() {
      const modal = document.getElementById('sessionExpiredModal');
      if (modal) modal.classList.add('hidden');
    }

    function handleReauth(event) {
      event.preventDefault();
      closeSessionExpiredModal();
      showToast('Sesión renovada', 'Tu sesión institucional ha sido reactivada exitosamente.', 'success');
    }

    function toggleOfflineMode() {
      isOfflineActive = !isOfflineActive;
      const banner = document.getElementById('pwaSyncBanner');
      const icon = document.getElementById('offlineIcon');

      if (isOfflineActive) {
        if (banner) banner.classList.remove('hidden');
        if (icon) icon.textContent = 'wifi';
        showToast('Modo sin conexión', 'Trabajando en modo local (PWA Offline).', 'warning');
      } else {
        if (banner) banner.classList.add('hidden');
        if (icon) icon.textContent = 'wifi_off';
        showToast('Conexión restaurada', 'Sincronización automática completada.', 'success');
      }
    }

    function syncPwaData() {
      showToast('Sincronizando', 'Sincronizando 3 bitácoras locales con el servidor UMB...', 'info');
      setTimeout(() => {
        toggleOfflineMode();
      }, 1500);
    }
'''
        c = c.replace('</body>', demo_buttons_and_modal + '<script>' + js_addition + '</script>\n</body>')
        with open(f_dash_est, 'w', encoding='utf-8') as f:
            f.write(c)
        print("Updated 02-estudiante/01-dashboard.html")


# =========================================================================
# 2. 02-estudiante/02-mi-expediente.html (Modal de eliminación + Toasts)
# =========================================================================
f_exp = 'sigres-umb/02-estudiante/02-mi-expediente.html'
if os.path.exists(f_exp):
    with open(f_exp, 'r', encoding='utf-8') as f:
        c = f.read()

    if 'openDeleteDocModal' not in c:
        # Add delete action buttons next to 'Ver documento' on some documents
        # Replace first article action buttons to include delete option
        c = c.replace(
            '''<div class="flex items-center gap-2 self-end md:self-center shrink-0">
                <button type="button" class="inline-flex items-center gap-1.5 px-3 py-2 rounded-lg border border-umb-border hover:bg-umb-surface text-umb-carbon text-xs font-medium transition-colors">
                  <span class="material-symbols-outlined text-[16px]">visibility</span>
                  Ver documento
                </button>
              </div>''',
            '''<div class="flex items-center gap-2 self-end md:self-center shrink-0">
                <button type="button" onclick="openDeleteDocModal('Acuse de carta de presentación', 'acuse_carta_presentacion_umb.pdf')" class="inline-flex items-center gap-1 px-2.5 py-2 rounded-lg border border-rose-200 text-rose-700 bg-rose-50/60 hover:bg-rose-100 text-xs font-medium transition-colors cursor-pointer" title="Eliminar archivo">
                  <span class="material-symbols-outlined text-[16px]">delete</span>
                  <span class="hidden sm:inline">Eliminar</span>
                </button>
                <button type="button" class="inline-flex items-center gap-1.5 px-3 py-2 rounded-lg border border-umb-border hover:bg-umb-surface text-umb-carbon text-xs font-medium transition-colors">
                  <span class="material-symbols-outlined text-[16px]">visibility</span>
                  Ver documento
                </button>
              </div>''',
            1
        )

        modal_delete_html = '''
  <!-- MODAL DE ELIMINACIÓN DE DOCUMENTO (Transversal 02) -->
  <div id="deleteDocModal" class="hidden fixed inset-0 z-50 bg-black/50 backdrop-blur-xs flex items-center justify-center p-4 transition-opacity duration-200" role="dialog" aria-modal="true">
    <div class="bg-white rounded-xl shadow-modal w-full max-w-[440px] p-6 relative border border-slate-100 animate-in zoom-in-95 duration-150" onclick="event.stopPropagation()">
      <div class="flex justify-center">
        <div class="w-14 h-14 rounded-full bg-[#FEE2E2] border border-[#FEB2B2] flex items-center justify-center shadow-xs">
          <span class="material-symbols-outlined text-[30px] text-[#C53030]">delete_forever</span>
        </div>
      </div>
      <h3 class="mt-4 text-lg font-bold text-umb-carbon text-center tracking-tight">¿Eliminar este documento?</h3>
      <p class="mt-1.5 text-xs text-umb-muted text-center max-w-[340px] mx-auto">Esta acción no se puede deshacer. El archivo será eliminado del expediente digital.</p>
      
      <div class="mt-4 bg-[#FEE2E2] border-l-[3px] border-[#C53030] p-3 rounded-lg flex items-start gap-2.5 text-left">
        <span class="material-symbols-outlined text-[#C53030] text-[20px] shrink-0 mt-0.5">description</span>
        <div class="min-w-0 flex-1">
          <p class="text-xs font-bold text-[#991B1B] truncate" id="deleteDocTargetName">documento.pdf</p>
          <p class="text-[11px] text-[#7F1D1D] mt-0.5" id="deleteDocTargetSub">1.2 MB · Subido el 21 de agosto de 2026</p>
        </div>
      </div>

      <div class="mt-6 flex items-center justify-end gap-2.5">
        <button type="button" onclick="closeDeleteDocModal()" class="px-4 py-2 border border-slate-300 rounded-lg text-xs font-semibold text-slate-700 bg-white hover:bg-slate-50 transition-colors">Cancelar</button>
        <button type="button" onclick="confirmDeleteDoc()" class="px-4 py-2 rounded-lg text-xs font-semibold text-white bg-[#C53030] hover:bg-red-800 transition-colors shadow-xs">Sí, eliminar archivo</button>
      </div>
    </div>
  </div>
''' + TOAST_CONTAINER_HTML

        js_delete = TOAST_JS_HELPER + '''
    let docToDelete = '';

    function openDeleteDocModal(title, filename) {
      docToDelete = filename;
      document.getElementById('deleteDocTargetName').textContent = filename;
      document.getElementById('deleteDocTargetSub').textContent = title + ' · 1.2 MB';
      document.getElementById('deleteDocModal').classList.remove('hidden');
    }

    function closeDeleteDocModal() {
      document.getElementById('deleteDocModal').classList.add('hidden');
    }

    function confirmDeleteDoc() {
      closeDeleteDocModal();
      showToast('Documento eliminado', `El archivo ${docToDelete} ha sido removido del expediente.`, 'error');
    }
'''
        c = c.replace('</body>', modal_delete_html + '<script>' + js_delete + '</script>\n</body>')
        with open(f_exp, 'w', encoding='utf-8') as f:
            f.write(c)
        print("Updated 02-estudiante/02-mi-expediente.html")


# =========================================================================
# 3. 02-estudiante/08-mis-bitacoras.html (Barra sync PWA + Estado sin conexión + Botón Offline)
# =========================================================================
f_bitacoras = 'sigres-umb/02-estudiante/08-mis-bitacoras.html'
if os.path.exists(f_bitacoras):
    with open(f_bitacoras, 'r', encoding='utf-8') as f:
        c = f.read()

    if 'id="pwaSyncBanner"' not in c:
        pwa_banner = '''
  <!-- ================= BARRA DE SINCRONIZACIÓN PWA (Transversal 08) ================= -->
  <div id="pwaSyncBanner" class="hidden w-full bg-umb-dorado-light border-b border-[#FDE68A] transition-all duration-300 relative z-30">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-10 flex items-center justify-between text-xs sm:text-[13px] font-medium text-[#92400E]">
      <div class="flex items-center gap-2.5 overflow-hidden">
        <span class="material-symbols-outlined text-[18px] text-[#92400E] shrink-0 animate-pulse">wifi_off</span>
        <span class="truncate">Modo sin conexión · Las bitácoras se guardarán localmente en el dispositivo</span>
      </div>
      <div class="flex items-center gap-2 shrink-0">
        <button type="button" onclick="syncPwaData()" class="px-2.5 py-1 rounded bg-[#D69E2E] hover:bg-[#B45309] text-white text-xs font-semibold shadow-xs transition-colors flex items-center gap-1 cursor-pointer">
          <span class="material-symbols-outlined text-[14px]">sync</span>
          <span class="hidden sm:inline">Sincronizar</span>
        </button>
      </div>
    </div>
  </div>
'''
        c = c.replace('</header>', '</header>' + pwa_banner, 1)

    if 'toggleOfflineMode' not in c:
        # We also add an offline view container inside main that can toggle
        offline_view_html = '''
  <!-- ESTADO SIN CONEXIÓN (Transversal 07) -->
  <div id="offlineStateContainer" class="hidden bg-white rounded-xl border border-umb-border shadow-sm p-8 text-center my-6 max-w-xl mx-auto animate-in fade-in duration-150">
    <div class="mx-auto w-24 h-24 rounded-full bg-umb-dorado-light border border-[#FDE68A] flex items-center justify-center mb-4">
      <span class="material-symbols-outlined text-[48px] text-[#D69E2E]">cloud_off</span>
    </div>
    <h3 class="text-lg font-bold text-umb-carbon tracking-tight">Sin conexión a internet</h3>
    <p class="text-xs text-umb-muted mt-1 max-w-md mx-auto leading-relaxed">
      Estás trabajando con las bitácoras guardadas en tu memoria local. Cualquier cambio se sincronizará automáticamente en cuanto recuperes señal.
    </p>
    <div class="mt-5 flex justify-center gap-2">
      <button type="button" onclick="toggleOfflineMode()" class="px-4 py-2 bg-umb-guinda hover:bg-umb-guinda-dark text-white rounded-lg text-xs font-semibold shadow-xs">Reintentar conexión</button>
    </div>
  </div>
'''
        demo_btn = '''
  <!-- Botón de demostración para el video — eliminar en producción -->
  <aside aria-label="Demostración de modo offline" class="fixed bottom-24 right-6 z-50">
    <button type="button" onclick="toggleOfflineMode()" title="Simular modo offline" class="w-12 h-12 rounded-full bg-umb-carbon hover:bg-neutral-800 text-white shadow-xl border border-white/20 flex items-center justify-center transition-all hover:scale-105 focus:outline-none focus:ring-2 focus:ring-umb-dorado cursor-pointer">
      <span id="offlineIcon" class="material-symbols-outlined text-[22px]">wifi_off</span>
    </button>
  </aside>
''' + TOAST_CONTAINER_HTML

        js_bitacoras = TOAST_JS_HELPER + '''
    let isOffline = false;
    function toggleOfflineMode() {
      isOffline = !isOffline;
      const banner = document.getElementById('pwaSyncBanner');
      const offlineCard = document.getElementById('offlineStateContainer');
      const icon = document.getElementById('offlineIcon');

      if (isOffline) {
        if (banner) banner.classList.remove('hidden');
        if (offlineCard) offlineCard.classList.remove('hidden');
        if (icon) icon.textContent = 'wifi';
        showToast('Modo sin conexión', 'Mostrando estado PWA Offline.', 'warning');
      } else {
        if (banner) banner.classList.add('hidden');
        if (offlineCard) offlineCard.classList.add('hidden');
        if (icon) icon.textContent = 'wifi_off';
        showToast('Conectado a la red', 'Conexión restaurada con el servidor UMB.', 'success');
      }
    }

    function syncPwaData() {
      showToast('Sincronizando', 'Sincronizando bitácoras...', 'info');
      setTimeout(toggleOfflineMode, 1000);
    }
'''
        c = c.replace('</main>', offline_view_html + '\n</main>')
        c = c.replace('</body>', demo_btn + '<script>' + js_bitacoras + '</script>\n</body>')
        with open(f_bitacoras, 'w', encoding='utf-8') as f:
            f.write(c)
        print("Updated 02-estudiante/08-mis-bitacoras.html")


# =========================================================================
# 4. 02-estudiante/09-nueva-bitacora.html (Modal eliminación evidencia + Toast envío + Offline)
# =========================================================================
f_nueva_bit = 'sigres-umb/02-estudiante/09-nueva-bitacora.html'
if os.path.exists(f_nueva_bit):
    with open(f_nueva_bit, 'r', encoding='utf-8') as f:
        c = f.read()

    if 'id="pwaSyncBanner"' not in c:
        pwa_banner = '''
  <!-- ================= BARRA DE SINCRONIZACIÓN PWA ================= -->
  <div id="pwaSyncBanner" class="hidden w-full bg-umb-dorado-light border-b border-[#FDE68A] transition-all duration-300 relative z-30">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-10 flex items-center justify-between text-xs sm:text-[13px] font-medium text-[#92400E]">
      <div class="flex items-center gap-2.5 overflow-hidden">
        <span class="material-symbols-outlined text-[18px] text-[#92400E] shrink-0 animate-pulse">wifi_off</span>
        <span class="truncate">Modo sin conexión · Esta bitácora se guardará localmente</span>
      </div>
      <div class="flex items-center gap-2 shrink-0">
        <span class="text-xs bg-[#D69E2E] text-white px-2 py-0.5 rounded font-bold">Borrador seguro</span>
      </div>
    </div>
  </div>
'''
        c = c.replace('</header>', '</header>' + pwa_banner, 1)

    if 'openDeleteEvidenceModal' not in c:
        modal_evidence_del = '''
  <!-- MODAL DE ELIMINACIÓN DE EVIDENCIA (Transversal 02) -->
  <div id="deleteEvidenceModal" class="hidden fixed inset-0 z-50 bg-black/50 backdrop-blur-xs flex items-center justify-center p-4" role="dialog" aria-modal="true">
    <div class="bg-white rounded-xl shadow-modal w-full max-w-[420px] p-6 relative border border-slate-100 animate-in zoom-in-95 duration-150" onclick="event.stopPropagation()">
      <div class="flex justify-center">
        <div class="w-14 h-14 rounded-full bg-[#FEE2E2] border border-[#FEB2B2] flex items-center justify-center shadow-xs">
          <span class="material-symbols-outlined text-[28px] text-[#C53030]">delete</span>
        </div>
      </div>
      <h3 class="mt-4 text-base font-bold text-umb-carbon text-center tracking-tight">¿Eliminar evidencia adjunta?</h3>
      <p class="mt-1 text-xs text-umb-muted text-center" id="deleteEvidenceName">evidencia_semana_10.jpg</p>

      <div class="mt-5 flex items-center justify-end gap-2.5">
        <button type="button" onclick="closeDeleteEvidenceModal()" class="px-3.5 py-2 border border-slate-300 rounded-lg text-xs font-semibold text-slate-700 bg-white hover:bg-slate-50 transition-colors">Cancelar</button>
        <button type="button" onclick="confirmDeleteEvidence()" class="px-3.5 py-2 rounded-lg text-xs font-semibold text-white bg-[#C53030] hover:bg-red-800 transition-colors shadow-xs">Eliminar archivo</button>
      </div>
    </div>
  </div>
'''
        demo_btn = '''
  <!-- Botón de demostración para el video — eliminar en producción -->
  <aside aria-label="Demostración de modo offline" class="fixed bottom-24 right-6 z-50">
    <button type="button" onclick="toggleOfflineMode()" title="Simular modo offline" class="w-12 h-12 rounded-full bg-umb-carbon hover:bg-neutral-800 text-white shadow-xl border border-white/20 flex items-center justify-center transition-all hover:scale-105 focus:outline-none focus:ring-2 focus:ring-umb-dorado cursor-pointer">
      <span id="offlineIcon" class="material-symbols-outlined text-[22px]">wifi_off</span>
    </button>
  </aside>
''' + TOAST_CONTAINER_HTML

        js_nueva_bit = TOAST_JS_HELPER + '''
    let isOffline = false;
    function toggleOfflineMode() {
      isOffline = !isOffline;
      const banner = document.getElementById('pwaSyncBanner');
      const icon = document.getElementById('offlineIcon');
      if (isOffline) {
        if (banner) banner.classList.remove('hidden');
        if (icon) icon.textContent = 'wifi';
        showToast('Modo sin conexión', 'Guardando borrador en almacenamiento local.', 'warning');
      } else {
        if (banner) banner.classList.add('hidden');
        if (icon) icon.textContent = 'wifi_off';
        showToast('Conexión en línea', 'Sincronizado con base de datos UMB.', 'success');
      }
    }

    function openDeleteEvidenceModal(filename = 'evidencia_captura.png') {
      document.getElementById('deleteEvidenceName').textContent = filename;
      document.getElementById('deleteEvidenceModal').classList.remove('hidden');
    }

    function closeDeleteEvidenceModal() {
      document.getElementById('deleteEvidenceModal').classList.add('hidden');
    }

    function confirmDeleteEvidence() {
      closeDeleteEvidenceModal();
      showToast('Evidencia eliminada', 'El archivo adjunto ha sido removido.', 'error');
    }

    function handleSendBitacora(event) {
      if (event) event.preventDefault();
      showToast('Bitácora enviada', 'Bitácora guardada exitosamente y enviada a revisión.', 'success');
      setTimeout(() => {
        window.location.href = '08-mis-bitacoras.html';
      }, 1800);
    }
'''
        # Intercept submit button
        c = re.sub(
            r'<button[^>]*type="submit"[^>]*>',
            r'<button type="button" onclick="handleSendBitacora(event)" class="h-10 px-5 rounded-lg bg-umb-guinda hover:bg-umb-guinda-dark text-white text-xs font-semibold flex items-center justify-center gap-2 shadow-xs transition-colors cursor-pointer">',
            c,
            count=1
        )

        c = c.replace('</body>', modal_evidence_del + demo_btn + '<script>' + js_nueva_bit + '</script>\n</body>')
        with open(f_nueva_bit, 'w', encoding='utf-8') as f:
            f.write(c)
        print("Updated 02-estudiante/09-nueva-bitacora.html")


# =========================================================================
# 5. 03-asesor-interno/04-registrar-asesoria.html (Toast al guardar)
# =========================================================================
f_reg_asesoria = 'sigres-umb/03-asesor-interno/04-registrar-asesoria.html'
if os.path.exists(f_reg_asesoria):
    with open(f_reg_asesoria, 'r', encoding='utf-8') as f:
        c = f.read()

    if 'handleSaveAsesoria' not in c:
        # Intercept button to call handleSaveAsesoria
        c = re.sub(
            r'<button[^>]*type="submit"[^>]*>',
            r'<button type="button" onclick="handleSaveAsesoria(event)" class="px-5 py-2.5 rounded-lg bg-umb-guinda hover:bg-umb-guinda-dark text-white font-semibold text-xs transition-colors shadow-xs flex items-center justify-center gap-1.5 cursor-pointer">',
            c,
            count=1
        )

        js_asesoria = TOAST_JS_HELPER + '''
    function handleSaveAsesoria(event) {
      if (event) event.preventDefault();
      showToast('Asesoría registrada', 'Asesoría técnica guardada correctamente en el expediente del alumno.', 'success');
      setTimeout(() => {
        window.location.href = '03-detalle-alumno.html';
      }, 1600);
    }
'''
        c = c.replace('</body>', TOAST_CONTAINER_HTML + '<script>' + js_asesoria + '</script>\n</body>')
        with open(f_reg_asesoria, 'w', encoding='utf-8') as f:
            f.write(c)
        print("Updated 03-asesor-interno/04-registrar-asesoria.html")


# =========================================================================
# 6. 03-asesor-interno/05-revisar-bitacoras.html (Modal confirmación + Toast)
# =========================================================================
f_rev_bit = 'sigres-umb/03-asesor-interno/05-revisar-bitacoras.html'
if os.path.exists(f_rev_bit):
    with open(f_rev_bit, 'r', encoding='utf-8') as f:
        c = f.read()

    if 'openApproveBitacoraModal' not in c:
        modal_confirm_html = '''
  <!-- MODAL DE CONFIRMACIÓN DE APROBACIÓN (Transversal 01) -->
  <div id="confirmBitacoraModal" class="hidden fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/50 backdrop-blur-xs transition-opacity duration-200" role="dialog" aria-modal="true">
    <div class="bg-white rounded-xl shadow-modal w-full max-w-[420px] p-6 flex flex-col items-center text-center border border-slate-100 animate-in zoom-in-95 duration-150" onclick="event.stopPropagation()">
      <div class="w-14 h-14 rounded-full bg-[#DCFCE7] flex items-center justify-center shrink-0 mb-3">
        <span class="material-symbols-outlined text-[30px] text-[#2D8C4E]">check_circle</span>
      </div>
      <h3 class="text-base font-bold text-umb-carbon tracking-tight">¿Aprobar esta bitácora?</h3>
      <p class="mt-1 text-xs text-umb-muted leading-relaxed max-w-[340px]" id="confirmBitacoraDesc">
        Estás a punto de aprobar la bitácora semanal del alumno por 35 horas.
      </p>

      <div class="mt-4 w-full bg-[#F9FAFB] border border-umb-border rounded-lg p-3 text-left flex items-center justify-between">
        <div>
          <div class="text-xs font-bold text-umb-carbon" id="confirmBitacoraTitle">Bitácora Semana 10 · 35 hrs</div>
          <div class="text-[11px] text-umb-outline" id="confirmBitacoraStudent">Jesús Andrés Mondragón Tenorio</div>
        </div>
        <span class="text-[10px] font-semibold bg-emerald-100 text-emerald-800 px-2 py-0.5 rounded-full">35 hrs</span>
      </div>

      <div class="mt-5 flex items-center justify-end gap-2.5 w-full">
        <button type="button" onclick="closeApproveBitacoraModal()" class="px-3.5 py-2 border border-slate-300 rounded-lg text-xs font-semibold text-slate-700 bg-white hover:bg-slate-50 transition-colors">Cancelar</button>
        <button type="button" onclick="confirmApproveBitacora()" class="px-4 py-2 rounded-lg text-xs font-semibold text-white bg-[#2D8C4E] hover:bg-emerald-700 transition-colors shadow-xs">Sí, aprobar bitácora</button>
      </div>
    </div>
  </div>
''' + TOAST_CONTAINER_HTML

        js_rev_bit = TOAST_JS_HELPER + '''
    let currentStudent = 'Jesús Andrés Mondragón';
    let currentWeek = 'Semana 10';

    function openApproveBitacoraModal(student = 'Jesús Andrés Mondragón Tenorio', week = 'Semana 10') {
      currentStudent = student;
      currentWeek = week;
      document.getElementById('confirmBitacoraStudent').textContent = student;
      document.getElementById('confirmBitacoraTitle').textContent = `Bitácora ${week} · 35 hrs`;
      document.getElementById('confirmBitacoraDesc').textContent = `Estás a punto de aprobar la bitácora de ${student} (${week}) por 35 horas.`;
      document.getElementById('confirmBitacoraModal').classList.remove('hidden');
    }

    function closeApproveBitacoraModal() {
      document.getElementById('confirmBitacoraModal').classList.add('hidden');
    }

    function confirmApproveBitacora() {
      closeApproveBitacoraModal();
      showToast('Bitácora aprobada', `La bitácora de ${currentStudent} (${currentWeek}) ha sido aprobada con éxito.`, 'success');
    }
'''
        # Replace approve button clicks
        c = re.sub(
            r'onclick="[^"]*aprobar[^"]*"',
            r'onclick="openApproveBitacoraModal(\'Jesús Andrés Mondragón Tenorio\', \'Semana 10\')"',
            c,
            flags=re.IGNORECASE
        )

        c = c.replace('</body>', modal_confirm_html + '<script>' + js_rev_bit + '</script>\n</body>')
        with open(f_rev_bit, 'w', encoding='utf-8') as f:
            f.write(c)
        print("Updated 03-asesor-interno/05-revisar-bitacoras.html")


# =========================================================================
# 7. 03-asesor-interno/06-evaluar-informe-parcial.html (Modal dictamen + Toast)
# =========================================================================
f_eval_parcial = 'sigres-umb/03-asesor-interno/06-evaluar-informe-parcial.html'
if os.path.exists(f_eval_parcial):
    with open(f_eval_parcial, 'r', encoding='utf-8') as f:
        c = f.read()

    if 'openDictamenParcialModal' not in c:
        modal_dictamen_html = '''
  <!-- MODAL DE CONFIRMACIÓN DE DICTAMEN PARCIAL (Transversal 01) -->
  <div id="dictamenParcialModal" class="hidden fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/50 backdrop-blur-xs" role="dialog" aria-modal="true">
    <div class="bg-white rounded-xl shadow-modal w-full max-w-[440px] p-6 flex flex-col items-center text-center border border-slate-100 animate-in zoom-in-95 duration-150" onclick="event.stopPropagation()">
      <div class="w-14 h-14 rounded-full bg-emerald-50 text-emerald-700 border border-emerald-200 flex items-center justify-center mb-3">
        <span class="material-symbols-outlined text-[30px]">assignment_turned_in</span>
      </div>
      <h3 class="text-base font-bold text-umb-carbon tracking-tight">¿Emitir dictamen del informe parcial?</h3>
      <p class="mt-1 text-xs text-umb-muted leading-relaxed">
        Se asentará la calificación y retroalimentación oficial para el alumno Jesús Andrés Mondragón Tenorio.
      </p>

      <div class="mt-4 w-full bg-slate-50 border border-slate-200 rounded-lg p-3 text-left">
        <div class="flex justify-between items-center text-xs font-semibold text-slate-800">
          <span>Puntaje asignado:</span>
          <span class="text-emerald-700 font-bold text-sm">95 / 100 · Acreditado</span>
        </div>
      </div>

      <div class="mt-5 flex items-center justify-end gap-2.5 w-full">
        <button type="button" onclick="closeDictamenParcialModal()" class="px-3.5 py-2 border border-slate-300 rounded-lg text-xs font-semibold text-slate-700 bg-white hover:bg-slate-50 transition-colors">Cancelar</button>
        <button type="button" onclick="confirmDictamenParcial()" class="px-4 py-2 rounded-lg text-xs font-semibold text-white bg-umb-guinda hover:bg-umb-guinda-dark transition-colors shadow-xs">Confirmar y emitir</button>
      </div>
    </div>
  </div>
''' + TOAST_CONTAINER_HTML

        js_dictamen = TOAST_JS_HELPER + '''
    function openDictamenParcialModal() {
      document.getElementById('dictamenParcialModal').classList.remove('hidden');
    }

    function closeDictamenParcialModal() {
      document.getElementById('dictamenParcialModal').classList.add('hidden');
    }

    function confirmDictamenParcial() {
      closeDictamenParcialModal();
      showToast('Dictamen emitido', 'Evaluación de Informe Parcial registrada y notificada a Coordinación.', 'success');
      setTimeout(() => {
        window.location.href = '02-mis-alumnos.html';
      }, 1600);
    }
'''
        # Replace emitir dictamen button click
        c = re.sub(
            r'<button[^>]*>.*?Emitir dictamen.*?</button>',
            r'<button type="button" onclick="openDictamenParcialModal()" class="px-5 py-2.5 rounded-lg bg-umb-guinda hover:bg-umb-guinda-dark text-white font-semibold text-xs transition-colors shadow-xs flex items-center gap-1.5 cursor-pointer"><span class="material-symbols-outlined text-[18px]">verified</span><span>Emitir dictamen</span></button>',
            c,
            flags=re.DOTALL
        )

        c = c.replace('</body>', modal_dictamen_html + '<script>' + js_dictamen + '</script>\n</body>')
        with open(f_eval_parcial, 'w', encoding='utf-8') as f:
            f.write(c)
        print("Updated 03-asesor-interno/06-evaluar-informe-parcial.html")


# =========================================================================
# 8. 03-asesor-interno/07-evaluar-informe-final.html (Modal calificación final + Toast)
# =========================================================================
f_eval_final = 'sigres-umb/03-asesor-interno/07-evaluar-informe-final.html'
if os.path.exists(f_eval_final):
    with open(f_eval_final, 'r', encoding='utf-8') as f:
        c = f.read()

    if 'openCalificacionFinalModal' not in c:
        modal_final_html = '''
  <!-- MODAL DE CONFIRMACIÓN DE CALIFICACIÓN FINAL (Transversal 01) -->
  <div id="calificacionFinalModal" class="hidden fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/50 backdrop-blur-xs" role="dialog" aria-modal="true">
    <div class="bg-white rounded-xl shadow-modal w-full max-w-[440px] p-6 flex flex-col items-center text-center border border-slate-100 animate-in zoom-in-95 duration-150" onclick="event.stopPropagation()">
      <div class="w-14 h-14 rounded-full bg-amber-50 text-amber-700 border border-amber-200 flex items-center justify-center mb-3">
        <span class="material-symbols-outlined text-[30px]">workspace_premium</span>
      </div>
      <h3 class="text-base font-bold text-umb-carbon tracking-tight">¿Emitir calificación final de residencia?</h3>
      <p class="mt-1 text-xs text-umb-muted leading-relaxed">
        Esta acción emitirá el acta definitiva de liberación de residencia profesional para Jesús Andrés Mondragón Tenorio.
      </p>

      <div class="mt-4 w-full bg-amber-50/70 border border-amber-200 rounded-lg p-3 text-left space-y-1">
        <div class="flex justify-between items-center text-xs font-bold text-amber-950">
          <span>Calificación Final:</span>
          <span class="text-amber-800 text-sm">98 / 100 (Excelente)</span>
        </div>
        <p class="text-[11px] text-amber-900">Total de horas acreditadas: 640 hrs.</p>
      </div>

      <div class="mt-5 flex items-center justify-end gap-2.5 w-full">
        <button type="button" onclick="closeCalificacionFinalModal()" class="px-3.5 py-2 border border-slate-300 rounded-lg text-xs font-semibold text-slate-700 bg-white hover:bg-slate-50 transition-colors">Cancelar</button>
        <button type="button" onclick="confirmCalificacionFinal()" class="px-4 py-2 rounded-lg text-xs font-semibold text-white bg-umb-guinda hover:bg-umb-guinda-dark transition-colors shadow-xs">Asentar calificación</button>
      </div>
    </div>
  </div>
''' + TOAST_CONTAINER_HTML

        js_eval_final = TOAST_JS_HELPER + '''
    function openCalificacionFinalModal() {
      document.getElementById('calificacionFinalModal').classList.remove('hidden');
    }

    function closeCalificacionFinalModal() {
      document.getElementById('calificacionFinalModal').classList.add('hidden');
    }

    function confirmCalificacionFinal() {
      closeCalificacionFinalModal();
      showToast('Calificación registrada', 'Acta final asentada y liberada para trámite de titulación.', 'success');
      setTimeout(() => {
        window.location.href = '02-mis-alumnos.html';
      }, 1600);
    }
'''
        # Replace button click
        c = re.sub(
            r'<button[^>]*>.*?Emitir calificación final.*?</button>',
            r'<button type="button" onclick="openCalificacionFinalModal()" class="px-5 py-2.5 rounded-lg bg-umb-guinda hover:bg-umb-guinda-dark text-white font-semibold text-xs transition-colors shadow-xs flex items-center gap-1.5 cursor-pointer"><span class="material-symbols-outlined text-[18px]">verified</span><span>Emitir calificación final</span></button>',
            c,
            flags=re.DOTALL
        )

        c = c.replace('</body>', modal_final_html + '<script>' + js_eval_final + '</script>\n</body>')
        with open(f_eval_final, 'w', encoding='utf-8') as f:
            f.write(c)
        print("Updated 03-asesor-interno/07-evaluar-informe-final.html")


# =========================================================================
# 9. 04-asesor-externo/03-detalle-bitacora.html (Modal aprobación + Toast)
# =========================================================================
f_ext_bit = 'sigres-umb/04-asesor-externo/03-detalle-bitacora.html'
if os.path.exists(f_ext_bit):
    with open(f_ext_bit, 'r', encoding='utf-8') as f:
        c = f.read()

    if 'openApproveExternoModal' not in c:
        modal_ext_html = '''
  <!-- MODAL DE CONFIRMACIÓN ASESOR EXTERNO (Transversal 01) -->
  <div id="approveExternoModal" class="hidden fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/50 backdrop-blur-xs" role="dialog" aria-modal="true">
    <div class="bg-white rounded-xl shadow-modal w-full max-w-[420px] p-6 flex flex-col items-center text-center border border-slate-100 animate-in zoom-in-95 duration-150" onclick="event.stopPropagation()">
      <div class="w-14 h-14 rounded-full bg-[#DCFCE7] text-[#2D8C4E] flex items-center justify-center mb-3">
        <span class="material-symbols-outlined text-[30px]">verified</span>
      </div>
      <h3 class="text-base font-bold text-umb-carbon tracking-tight">¿Validar horas y actividades en empresa?</h3>
      <p class="mt-1 text-xs text-umb-muted leading-relaxed">
        Confirmas que el alumno Jesús Andrés Mondragón Tenorio cubrió satisfactoriamente las 35 horas de la Semana 10.
      </p>

      <div class="mt-5 flex items-center justify-end gap-2.5 w-full">
        <button type="button" onclick="closeApproveExternoModal()" class="px-3.5 py-2 border border-slate-300 rounded-lg text-xs font-semibold text-slate-700 bg-white hover:bg-slate-50 transition-colors">Cancelar</button>
        <button type="button" onclick="confirmApproveExterno()" class="px-4 py-2 rounded-lg text-xs font-semibold text-white bg-[#2D8C4E] hover:bg-emerald-700 transition-colors shadow-xs">Firmar y validar</button>
      </div>
    </div>
  </div>
''' + TOAST_CONTAINER_HTML

        js_ext = TOAST_JS_HELPER + '''
    function openApproveExternoModal() {
      document.getElementById('approveExternoModal').classList.remove('hidden');
    }

    function closeApproveExternoModal() {
      document.getElementById('approveExternoModal').classList.add('hidden');
    }

    function confirmApproveExterno() {
      closeApproveExternoModal();
      showToast('Bitácora validada', 'La bitácora semanal ha sido firmada por la sede receptora.', 'success');
      setTimeout(() => {
        window.location.href = '02-bitacoras-por-validar.html';
      }, 1600);
    }
'''
        # Replace approve button
        c = re.sub(
            r'<button[^>]*>.*?Validar y firmar bitácora.*?</button>',
            r'<button type="button" onclick="openApproveExternoModal()" class="px-5 py-2.5 rounded-lg bg-[#2D8C4E] hover:bg-emerald-700 text-white font-semibold text-xs transition-colors shadow-xs flex items-center gap-1.5 cursor-pointer"><span class="material-symbols-outlined text-[18px]">verified</span><span>Validar y firmar bitácora</span></button>',
            c,
            flags=re.DOTALL
        )

        c = c.replace('</body>', modal_ext_html + '<script>' + js_ext + '</script>\n</body>')
        with open(f_ext_bit, 'w', encoding='utf-8') as f:
            f.write(c)
        print("Updated 04-asesor-externo/03-detalle-bitacora.html")


# =========================================================================
# 10. 05-control-escolar/04-validar-documentos.html (Toast al aprobar)
# =========================================================================
f_ce_val = 'sigres-umb/05-control-escolar/04-validar-documentos.html'
if os.path.exists(f_ce_val):
    with open(f_ce_val, 'r', encoding='utf-8') as f:
        c = f.read()

    if 'confirmApproveDoc' not in c:
        # Check openApproveModal in 04-validar-documentos
        c = c.replace(
            '''function confirmApprove() {
      closeApproveModal();
      alert('Documento aprobado exitosamente');
    }''',
            '''function confirmApprove() {
      closeApproveModal();
      showToast('Documento validado', 'Acuse de carta cotejado y aprobado en expediente oficial.', 'success');
    }'''
        )

        c = c.replace('</body>', TOAST_CONTAINER_HTML + '<script>' + TOAST_JS_HELPER + '</script>\n</body>')
        with open(f_ce_val, 'w', encoding='utf-8') as f:
            f.write(c)
        print("Updated 05-control-escolar/04-validar-documentos.html")

print("All integrations completed successfully.")
