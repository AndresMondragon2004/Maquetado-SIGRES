import glob
import re

for f in sorted(glob.glob('sigres-umb/03-asesor-interno/*.html')):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    symbols = re.findall(r'<span[^>]*class="[^"]*material-symbols-outlined[^"]*"[^>]*>(.*?)</span>', content, re.DOTALL)
    print(f, "-->", len(symbols), "material symbols found")
    
    # Check for empty symbols or strange symbols
    empty_or_weird = [s.strip() for s in symbols if len(s.strip()) == 0 or '\n' in s or len(s.strip()) > 35]
    if empty_or_weird:
        print("   Weird symbols:", empty_or_weird[:5])
    
    # Check for possible icon spans that missed class="material-symbols-outlined"
    # like <span class="material-symbols-rounded"> or <i class="...
    i_tags = re.findall(r'<i[^>]*>(.*?)</i>', content)
    if i_tags:
        print("   <i> tags found:", i_tags[:5])
        
    # Check if Material Symbols link and style are properly present
    has_link = 'Material+Symbols+Outlined' in content
    has_style = '.material-symbols-outlined' in content
    print(f"   has_link: {has_link}, has_style: {has_style}")
