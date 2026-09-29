import glob
import re

for f in sorted(glob.glob('sigres-umb/05-control-escolar/*.html')):
    with open(f, 'r', encoding='utf-8') as fl:
        txt = fl.read()
    
    # check aside and main
    aside = re.search(r'<aside[^>]*class="([^"]*)"', txt)
    mains = re.findall(r'<(?:main|div)[^>]*class="([^"]*lg:ml-\[260px\][^"]*)"', txt)
    
    print(f"File: {f}")
    if aside:
        print("  Aside fixed:", 'fixed' in aside.group(1))
    print("  Matches with lg:ml-[260px]:", len(mains))
    for m in mains:
        print("    -->", m[:70])
        
    # check name occurrences
    mariana = len(re.findall(r'Mariana|Estrada|ME', txt))
    estefania = len(re.findall(r'Estefan[ií]a|Yttesen|EY', txt))
    print(f"  Names: Mariana/ME count={mariana}, Estefanía/EY count={estefania}")
