import re
import glob

lucide_to_material = {
    'arrow-left': 'arrow_back',
    'chevron-right': 'chevron_right',
    'clock': 'schedule',
    'check': 'check',
    'calendar-clock': 'calendar_month',
    'video': 'videocam',
    'building-2': 'apartment',
    'map-pin': 'location_on',
    'link': 'link',
    'user-check': 'how_to_reg',
    'check-circle': 'check_circle',
    'clock-alert': 'schedule',
    'x-circle': 'cancel',
    'paperclip': 'attach_file',
    'upload': 'upload',
    'alert-triangle': 'warning',
    'file-text': 'description',
    'message-square-plus': 'add_comment',
    'cloud-upload': 'cloud_upload',
    'x': 'close',
    'bookmark': 'bookmark',
    'image': 'image',
    'eye': 'visibility',
    'info': 'info',
    'mail': 'mail',
}

files_to_fix = [
    'sigres-umb/03-asesor-interno/04-registrar-asesoria.html',
    'sigres-umb/04-asesor-externo/03-detalle-bitacora.html'
]

for f in files_to_fix:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace <i ... data-lucide="NAME" ...></i> with <span class="material-symbols-outlined ...">ICON</span>
    def replacer(match):
        tag_str = match.group(0)
        # extract data-lucide
        m_name = re.search(r'data-lucide="([^"]+)"', tag_str)
        if not m_name:
            return tag_str
        icon_name = m_name.group(1)
        mat_icon = lucide_to_material.get(icon_name, icon_name.replace('-', '_'))
        
        # extract class
        m_class = re.search(r'class="([^"]+)"', tag_str)
        cls = m_class.group(1) if m_class else ""
        # remove w-*, h-* or keep, but add material-symbols-outlined
        return f'<span class="material-symbols-outlined {cls}">{mat_icon}</span>'

    # Match <i ... data-lucide="...".*?>.*?</i>
    new_content = re.sub(r'<i\s+[^>]*data-lucide="[^"]+"[^>]*>.*?</i>', replacer, content, flags=re.DOTALL)
    # Also match reversed order: data-lucide before class or after
    new_content = re.sub(r'<i\s+[^>]*data-lucide=[^>]*>.*?</i>', replacer, new_content, flags=re.DOTALL)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(new_content)
    print(f"Updated {f}")
