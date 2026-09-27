import re

files = ['sigres-umb/03-asesor-interno/04-registrar-asesoria.html', 'sigres-umb/04-asesor-externo/03-detalle-bitacora.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as fl:
        txt = fl.read()
    
    def repl(m):
        cls = m.group(1)
        # convert sizing
        cls = re.sub(r'\bw-3(\.5)?\b|\bh-3(\.5)?\b', 'text-[15px]', cls)
        cls = re.sub(r'\bw-4\b|\bh-4\b', 'text-[18px]', cls)
        cls = re.sub(r'\bw-5\b|\bh-5\b', 'text-[20px]', cls)
        cls = re.sub(r'\bw-6\b|\bh-6\b', 'text-[24px]', cls)
        cls = re.sub(r'\bw-8\b|\bh-8\b', 'text-[32px]', cls)
        parts = cls.split()
        seen = []
        for p in parts:
            if p not in seen:
                seen.append(p)
        return 'class="' + ' '.join(seen) + '"'

    txt = re.sub(r'class="([^"]*material-symbols-outlined[^"]*)"', repl, txt)
    with open(f, 'w', encoding='utf-8') as fl:
        fl.write(txt)
    print("Cleaned sizes for", f)
