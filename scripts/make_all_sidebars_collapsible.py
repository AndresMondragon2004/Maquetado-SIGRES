import os
import re

SIDEBAR_CSS = """    /* Transición suave para contracción de sidebar */
    #mainSidebar, #mainWorkspace {
      transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    }
    @media (min-width: 1024px) {
      body.sidebar-collapsed #mainSidebar {
        width: 72px !important;
        padding-left: 0.5rem !important;
        padding-right: 0.5rem !important;
      }
      body.sidebar-collapsed #mainWorkspace {
        margin-left: 72px !important;
      }
      body.sidebar-collapsed .sidebar-text {
        display: none !important;
      }
      body.sidebar-collapsed .sidebar-link {
        justify-content: center !important;
        padding-left: 0 !important;
        padding-right: 0 !important;
        gap: 0 !important;
      }
      body.sidebar-collapsed .sidebar-user-card {
        justify-content: center !important;
        padding: 0.5rem 0 !important;
      }
      body.sidebar-collapsed .sidebar-footer {
        justify-content: center !important;
      }
      body.sidebar-collapsed .sidebar-footer-text {
        display: none !important;
      }
    }
"""

TOGGLE_BTN = """      <!-- Botón para contraer/expandir menú lateral -->
      <button type="button" 
              id="sidebarToggleBtn"
              onclick="toggleSidebarCollapse()" 
              class="hidden lg:flex p-1.5 -ml-1 rounded-lg hover:bg-white/10 text-white transition-colors focus:outline-none focus:ring-2 focus:ring-white/40 items-center justify-center cursor-pointer" 
              title="Contraer / expandir menú lateral (Mayor espacio de lectura)" 
              aria-label="Alternar menú lateral">
        <span class="material-symbols-outlined text-[24px]" id="sidebarToggleIcon">menu_open</span>
      </button>

"""

SIDEBAR_JS = """
    // CONTROL DE CONTRACCIÓN DE MENÚ LATERAL (Mayor espacio de lectura)
    function toggleSidebarCollapse() {
      const isCollapsed = document.body.classList.toggle('sidebar-collapsed');
      try {
        localStorage.setItem('sigres_sidebar_collapsed', isCollapsed ? 'true' : 'false');
      } catch (e) {}
      const icon = document.getElementById('sidebarToggleIcon');
      if (icon) {
        icon.textContent = isCollapsed ? 'menu' : 'menu_open';
      }
    }

    // Restaurar estado guardado del menú
    (function initSidebar() {
      try {
        if (localStorage.getItem('sigres_sidebar_collapsed') === 'true') {
          document.body.classList.add('sidebar-collapsed');
          const icon = document.getElementById('sidebarToggleIcon');
          if (icon) icon.textContent = 'menu';
        }
      } catch (e) {}
    })();
"""

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Only process files that have an aside sidebar
    if '<aside' not in content or 'w-[260px]' not in content:
        return False

    changed = False

    # 1. Add CSS if not present
    if '#mainSidebar' not in content:
        if '</style>' in content:
            content = content.replace('</style>', SIDEBAR_CSS + '  </style>', 1)
            changed = True

    # 2. Add toggle button in header if not present
    if 'sidebarToggleBtn' not in content:
        # Match the header left group
        # Typically: <div class="flex items-center gap-3 md:gap-4">\n      <a href="01-dashboard
        # Or: <div class="flex items-center gap-2.5 ...">
        pattern = re.compile(r'(<header[^>]*>\s*<!--[^-]*-->\s*<div class="flex items-center gap-[^"]*">\s*)(<a href=)', re.IGNORECASE)
        if pattern.search(content):
            content = pattern.sub(r'\1' + TOGGLE_BTN + r'\2', content, count=1)
            changed = True
        else:
            # Fallback pattern for other header variations
            pattern2 = re.compile(r'(<header[^>]*>.*?<div class="flex items-center[^"]*">\s*)(<a )', re.DOTALL | re.IGNORECASE)
            if pattern2.search(content):
                content = pattern2.sub(r'\1' + TOGGLE_BTN + r'\2', content, count=1)
                changed = True

    # 3. Add id="mainSidebar" to aside if missing
    if 'id="mainSidebar"' not in content:
        content = re.sub(r'<aside\s+class="w-\[260px\]', '<aside id="mainSidebar" class="w-[260px]', content, count=1)
        changed = True

    # 4. Add id="mainWorkspace" to central workspace div if missing
    if 'id="mainWorkspace"' not in content:
        content = re.sub(r'<div class="flex-1 flex flex-col overflow-hidden bg-umb-surface lg:ml-\[260px\]"', '<div id="mainWorkspace" class="flex-1 flex flex-col overflow-hidden bg-umb-surface lg:ml-[260px]"', content, count=1)
        changed = True

    # 5. Add sidebar-text and sidebar-link classes inside aside if not already present
    # Add sidebar-user-card
    if 'sidebar-user-card' not in content:
        content = re.sub(r'(<aside[^>]*>.*?)(<div class="p-3 mb-3 border-b border-umb-border bg-gradient-to-b from-white to-umb-surface/50 rounded-lg)', r'\1<div class="sidebar-user-card p-3 mb-3 border-b border-umb-border bg-gradient-to-b from-white to-umb-surface/50 rounded-lg flex items-center gap-3', content, count=1, flags=re.DOTALL)
        changed = True

    # Add sidebar-text to user info in aside
    # <div class="flex-1 min-w-0">\s*<p class="text-xs font-bold text-umb-carbon
    if 'sidebar-text' not in content:
        content = re.sub(r'(<div class="w-10 h-10[^>]*>.*?</div>\s*)<div class="flex-1 min-w-0">', r'\1<div class="sidebar-text flex-1 min-w-0">', content, count=1, flags=re.DOTALL)
        # Add sidebar-link and sidebar-text to nav items inside aside
        # <a href="..." class="... flex items-center gap-3 ...">\s*<span class="material-symbols-outlined[^"]*">([^<]+)</span>\s*<span class="text-sm">([^<]+)</span>
        nav_pattern = re.compile(r'(<nav class="space-y-1"[^>]*>.*?</nav>)', re.DOTALL)
        nav_match = nav_pattern.search(content)
        if nav_match:
            nav_html = nav_match.group(1)
            new_nav_html = re.sub(r'<a href="([^"]+)" class="([^"]* flex items-center[^"]*)"', r'<a href="\1" class="sidebar-link \2"', nav_html)
            new_nav_html = re.sub(r'(<span class="material-symbols-outlined[^"]*">[^<]+</span>\s*)<span class="text-sm">([^<]+)</span>', r'\1<span class="sidebar-text text-sm">\2</span>', new_nav_html)
            content = content.replace(nav_html, new_nav_html, 1)
            changed = True

    # Add sidebar-footer and sidebar-footer-text
    if 'sidebar-footer' not in content:
        footer_pattern = re.compile(r'<div class="p-3 border-t border-umb-border text-\[11px\] text-umb-outline flex items-center justify-between">\s*<span>([^<]+)</span>\s*<span class="flex items-center gap-1.5 text-emerald-700 font-medium">\s*(<span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>)\s*([^<]+)\s*</span>\s*</div>', re.DOTALL)
        if footer_pattern.search(content):
            content = footer_pattern.sub(r'<div class="sidebar-footer p-3 border-t border-umb-border text-[11px] text-umb-outline flex items-center justify-between">\n        <span class="sidebar-footer-text">\1</span>\n        <span class="flex items-center gap-1.5 text-emerald-700 font-medium">\n          \2\n          <span class="sidebar-footer-text">\3</span>\n        </span>\n      </div>', content, count=1)
            changed = True

    # 6. Add JS functions if not present
    if 'toggleSidebarCollapse' not in content:
        if '</body>' in content:
            content = content.replace('</body>', f'<script>{SIDEBAR_JS}</script>\n</body>', 1)
            changed = True

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    root = 'sigres-umb'
    updated = []
    for dirpath, _, filenames in os.walk(root):
        for fname in filenames:
            if fname.endswith('.html'):
                full_path = os.path.join(dirpath, fname)
                if update_file(full_path):
                    updated.append(full_path)
    print(f"Updated {len(updated)} files with collapsible sidebar support.")

if __name__ == '__main__':
    main()
