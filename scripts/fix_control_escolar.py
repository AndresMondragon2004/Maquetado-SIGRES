import re

# 1. FIX 04-validar-documentos.html layout & signature
file_04 = 'sigres-umb/05-control-escolar/04-validar-documentos.html'
with open(file_04, 'r', encoding='utf-8') as f:
    content_04 = f.read()

# Fix outer div and inner main
content_04 = content_04.replace(
    '<div class="flex-1 flex flex-col overflow-hidden bg-umb-surface">',
    '<div class="flex-1 flex flex-col overflow-hidden bg-umb-surface lg:ml-[260px]">'
)
content_04 = content_04.replace(
    '<main class="lg:ml-[260px] flex-1 flex overflow-hidden min-w-0 pb-24 lg:pb-8">',
    '<main class="flex-1 flex overflow-hidden min-w-0 pb-24 lg:pb-8">'
)
content_04 = content_04.replace(
    'Mariana Estrada G.',
    'Lic. Estefanía Yttesen Nava'
)
content_04 = content_04.replace(
    'Mariana Estrada Gómez',
    'Lic. Estefanía Yttesen Nava'
)

with open(file_04, 'w', encoding='utf-8') as f:
    f.write(content_04)
print("Updated 04-validar-documentos.html")

# 2. FIX 09-mi-perfil.html
file_09 = 'sigres-umb/05-control-escolar/09-mi-perfil.html'
with open(file_09, 'r', encoding='utf-8') as f:
    content_09 = f.read()

content_09 = content_09.replace('>ME</div>', '>EY</div>')
content_09 = content_09.replace('Mariana Estrada Gómez', 'Lic. Estefanía Yttesen Nava')
content_09 = content_09.replace('EAGM880512MDFXXX0', 'YANE890615XXX')
content_09 = content_09.replace('mariana.estrada@umb.mx', 'estefania.yttesen@umb.mx')
content_09 = content_09.replace('EAGM880512MDFRRN08', 'YANE890615MMNNVS01')
content_09 = content_09.replace('UMB-ADM-0215', 'UMB-CE-0142')

with open(file_09, 'w', encoding='utf-8') as f:
    f.write(content_09)
print("Updated 09-mi-perfil.html")
