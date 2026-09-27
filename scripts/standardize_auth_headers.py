import os
import re
import glob

BASE_DIR = r"c:\Users\Pc\Downloads\Maquetado - Residencia\respaldo-pre-estandarizacion-2026-09-17\sigres-umb"

STANDARD_PILL_HEADER = """  <!-- CABECERA INSTITUCIONAL ESTÁNDAR (Pill Capsule) -->
  <header class="w-full pt-8 pb-4 px-4 flex justify-center items-center">
    <a href="../index.html" class="inline-flex items-center gap-3.5 bg-white hover:bg-umb-surface/60 px-6 py-2.5 rounded-full border border-umb-border shadow-sm transition-all group" title="Ir al portal principal">
      <img src="../assets/logo_umb.png" alt="Logo UMB" class="h-9 w-auto object-contain" />
      <div class="h-6 w-px bg-umb-border"></div>
      <div class="flex items-center gap-2">
        <span class="text-umb-guinda font-bold text-base tracking-tight leading-none group-hover:text-umb-guinda-dark transition-colors">SIGRES-UMB</span>
        <span class="text-xs text-slate-500 font-normal leading-none hidden sm:inline">UES San José del Rincón</span>
      </div>
    </a>
  </header>"""

ONBOARDING_HEADER = """  <!-- CABECERA INSTITUCIONAL ESTÁNDAR (Pill Capsule + Saltar Tour) -->
  <header class="w-full border-b border-umb-border bg-white/95 backdrop-blur px-6 lg:px-12 py-3 flex items-center justify-between sticky top-0 z-30">
    <a href="../index.html" class="inline-flex items-center gap-3.5 bg-white hover:bg-umb-surface/60 px-5 py-2 rounded-full border border-umb-border shadow-xs transition-all group" title="Ir al portal principal">
      <img src="../assets/logo_umb.png" alt="Logo UMB" class="h-8 w-auto object-contain" />
      <div class="h-5 w-px bg-umb-border"></div>
      <div class="flex items-center gap-2">
        <span class="text-umb-guinda font-bold text-base tracking-tight leading-none group-hover:text-umb-guinda-dark transition-colors">SIGRES-UMB</span>
        <span class="text-xs text-slate-500 font-normal leading-none hidden sm:inline">UES San José del Rincón</span>
      </div>
    </a>

    <!-- BOTÓN SALTAR TOUR -->
    <div>
      <a href="../02-estudiante/01-dashboard.html" class="inline-flex items-center gap-1.5 text-xs font-semibold text-umb-muted hover:text-umb-guinda hover:bg-umb-guinda-light/50 px-3.5 py-2 rounded-lg transition-colors">
        <span>Saltar tour</span>
        <span class="material-symbols-outlined text-sm">skip_next</span>
      </a>
    </div>
  </header>"""

def standardize_auth_files():
    auth_dir = os.path.join(BASE_DIR, "01-autenticacion")
    
    # 02-verificacion-enlace.html
    f_02 = os.path.join(auth_dir, "02-verificacion-enlace.html")
    if os.path.exists(f_02):
        with open(f_02, "r", encoding="utf-8") as f:
            c = f.read()
        c = re.sub(r'<header.*?</header>', STANDARD_PILL_HEADER, c, count=1, flags=re.DOTALL | re.IGNORECASE)
        with open(f_02, "w", encoding="utf-8") as f:
            f.write(c)

    # 03-registro-estudiante.html
    f_03 = os.path.join(auth_dir, "03-registro-estudiante.html")
    if os.path.exists(f_03):
        with open(f_03, "r", encoding="utf-8") as f:
            c = f.read()
        c = re.sub(r'<header.*?</header>', STANDARD_PILL_HEADER, c, count=1, flags=re.DOTALL | re.IGNORECASE)
        with open(f_03, "w", encoding="utf-8") as f:
            f.write(c)

    # 04-acceso-denegado.html
    f_04 = os.path.join(auth_dir, "04-acceso-denegado.html")
    if os.path.exists(f_04):
        with open(f_04, "r", encoding="utf-8") as f:
            c = f.read()
        c = re.sub(r'<header.*?</header>', STANDARD_PILL_HEADER, c, count=1, flags=re.DOTALL | re.IGNORECASE)
        with open(f_04, "w", encoding="utf-8") as f:
            f.write(c)

    # 05-recuperar-acceso.html
    f_05 = os.path.join(auth_dir, "05-recuperar-acceso.html")
    if os.path.exists(f_05):
        with open(f_05, "r", encoding="utf-8") as f:
            c = f.read()
        c = re.sub(r'<header.*?</header>', STANDARD_PILL_HEADER, c, count=1, flags=re.DOTALL | re.IGNORECASE)
        with open(f_05, "w", encoding="utf-8") as f:
            f.write(c)

    # 06-onboarding.html
    f_06 = os.path.join(auth_dir, "06-onboarding.html")
    if os.path.exists(f_06):
        with open(f_06, "r", encoding="utf-8") as f:
            c = f.read()
        c = re.sub(r'<header.*?</header>', ONBOARDING_HEADER, c, count=1, flags=re.DOTALL | re.IGNORECASE)
        with open(f_06, "w", encoding="utf-8") as f:
            f.write(c)

    # 01-login.html: ensure the left side and top badge use canonical pill and institutional info
    f_01 = os.path.join(auth_dir, "01-login.html")
    if os.path.exists(f_01):
        with open(f_01, "r", encoding="utf-8") as f:
            c = f.read()
        # Ensure logo is ../assets/logo_umb.png
        c = re.sub(r'src="[^"]*logo_umb\.png"', 'src="../assets/logo_umb.png"', c)
        with open(f_01, "w", encoding="utf-8") as f:
            f.write(c)

    print("01-autenticacion headers standardized with exact Pill Capsule!")

def fix_transversal_sidebar_margins():
    # Remove lg:ml-[260px] from transversal full-page screens that don't have sidebars
    transversal_dir = os.path.join(BASE_DIR, "08-transversales")
    for fpath in glob.glob(os.path.join(transversal_dir, "*.html")):
        with open(fpath, "r", encoding="utf-8") as f:
            c = f.read()
        c = c.replace("lg:ml-[260px]", "")
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(c)
    print("08-transversales margins cleaned (removed unwanted lg:ml on standalone pages).")

if __name__ == "__main__":
    standardize_auth_files()
    fix_transversal_sidebar_margins()
