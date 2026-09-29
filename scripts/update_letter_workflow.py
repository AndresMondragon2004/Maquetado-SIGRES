import re
import glob

# 1. UPDATE 05-control-escolar/05-generar-carta.html
file_ce = 'sigres-umb/05-control-escolar/05-generar-carta.html'
with open(file_ce, 'r', encoding='utf-8') as f:
    ce_txt = f.read()

# Update subtitle and actions
ce_txt = ce_txt.replace(
    'Revisión y canalización a la Coordinación de la UES para firma.',
    'Cotejo de expediente y liberación de la carta oficial prellenada para descarga del estudiante.'
)
ce_txt = ce_txt.replace(
    '<span>Enviar a Coordinación</span>',
    '<span>Liberar carta para el estudiante</span>'
)
ce_txt = ce_txt.replace(
    'Estado: En firma de Coordinación',
    'Estado: Liberada para descarga e impresión del alumno'
)

# Update instructions workflow in CE
new_workflow_ce = """<!-- BEGIN: InstructionsWorkflowSection -->
<section class="bg-[#EFF6FF] border-l-4 border-[#3B82F6] rounded-r-lg p-5 shadow-sm" data-purpose="workflow-card">
<div class="flex items-center space-x-2 mb-3">
<span class="material-symbols-outlined text-[#1E40AF] text-[20px]">assignment_turned_in</span>
<h2 class="text-base font-semibold text-[#1E40AF]">Flujo reglamentario del trámite oficial</h2>
</div>
<!-- Pasos numerados secuenciales -->
<ol class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3 text-xs text-slate-700 mt-2">
<li class="flex items-start space-x-2.5 bg-white/80 p-3 rounded-lg border border-blue-100 shadow-2xs">
<span class="w-5 h-5 rounded-full bg-blue-600 text-white font-bold text-[11px] flex items-center justify-center shrink-0 mt-0.5">1</span>
<span class="leading-snug"><strong class="text-slate-900">Control Escolar libera:</strong> Se autoriza el folio y se habilita la descarga en el portal del alumno.</span>
</li>
<li class="flex items-start space-x-2.5 bg-white/80 p-3 rounded-lg border border-blue-100 shadow-2xs">
<span class="w-5 h-5 rounded-full bg-blue-600 text-white font-bold text-[11px] flex items-center justify-center shrink-0 mt-0.5">2</span>
<span class="leading-snug"><strong class="text-slate-900">El alumno descarga e imprime:</strong> El estudiante obtiene el PDF oficial prellenado desde su panel.</span>
</li>
<li class="flex items-start space-x-2.5 bg-white/80 p-3 rounded-lg border border-blue-100 shadow-2xs">
<span class="w-5 h-5 rounded-full bg-blue-600 text-white font-bold text-[11px] flex items-center justify-center shrink-0 mt-0.5">3</span>
<span class="leading-snug"><strong class="text-slate-900">Firma y sello presencial:</strong> El alumno acude con el Coordinador de la UES para recabar firma con tinta y sello oficial.</span>
</li>
<li class="flex items-start space-x-2.5 bg-white/80 p-3 rounded-lg border border-blue-100 shadow-2xs">
<span class="w-5 h-5 rounded-full bg-blue-600 text-white font-bold text-[11px] flex items-center justify-center shrink-0 mt-0.5">4</span>
<span class="leading-snug"><strong class="text-slate-900">Entrega a la empresa:</strong> El alumno entrega la carta sellada a la institución receptora.</span>
</li>
<li class="flex items-start space-x-2.5 bg-white/80 p-3 rounded-lg border border-blue-100 shadow-2xs">
<span class="w-5 h-5 rounded-full bg-blue-600 text-white font-bold text-[11px] flex items-center justify-center shrink-0 mt-0.5">5</span>
<span class="leading-snug"><strong class="text-slate-900">Emisión de aceptación:</strong> La empresa sella el acuse y entrega la carta de aceptación oficial.</span>
</li>
<li class="flex items-start space-x-2.5 bg-white/80 p-3 rounded-lg border border-blue-100 shadow-2xs">
<span class="w-5 h-5 rounded-full bg-blue-600 text-white font-bold text-[11px] flex items-center justify-center shrink-0 mt-0.5">6</span>
<span class="leading-snug"><strong class="text-slate-900">Cierre de expediente:</strong> El alumno escanea y sube el acuse sellado a SIGRES-UMB.</span>
</li>
</ol>
</section>
<!-- END: InstructionsWorkflowSection -->"""

ce_txt = re.sub(r'<!-- BEGIN: InstructionsWorkflowSection -->.*?<!-- END: InstructionsWorkflowSection -->', new_workflow_ce, ce_txt, flags=re.DOTALL)

with open(file_ce, 'w', encoding='utf-8') as f:
    f.write(ce_txt)
print("Updated 05-control-escolar/05-generar-carta.html")

# 2. UPDATE 06-coordinacion/05-firma-cartas.html
file_coord_carta = 'sigres-umb/06-coordinacion/05-firma-cartas.html'
with open(file_coord_carta, 'r', encoding='utf-8') as f:
    coord_txt = f.read()

# Replace title and description
coord_txt = coord_txt.replace(
    '<h1 class="text-2xl font-bold text-gray-900 tracking-tight">Firma de cartas</h1>',
    '<h1 class="text-2xl font-bold text-gray-900 tracking-tight">Cartas de presentación emitidas</h1>'
)
coord_txt = coord_txt.replace(
    'Cartas de presentación pendientes de firma para el ciclo 26-27/1.',
    'Registro de cartas liberadas por Control Escolar para firma autógrafa y sello oficial presencial en ventanilla.'
)

# Replace e.firma SAT badge with physical signature & university stamp info
old_efirma_badge = r'<div class="flex items-center space-x-3 bg-white border border-gray-200 rounded-xl px-4 py-2\.5 shadow-sm">.*?</div>\s*</div>\s*</div>'
new_stamp_badge = """<div class="flex items-center space-x-3 bg-white border border-gray-200 rounded-xl px-4 py-2.5 shadow-sm">
              <div class="w-9 h-9 rounded-lg bg-umb-guinda-light text-umb-guinda flex items-center justify-center border border-umb-guinda/15">
                <span class="material-symbols-outlined text-[20px]">approval_delegation</span>
              </div>
              <div>
                <div class="text-xs font-bold text-gray-900 flex items-center space-x-1.5">
                  <span>Firma y Sello Oficial Presencial</span>
                </div>
                <div class="text-[11px] text-gray-500">UES San José del Rincón · Mtro. Luis Ramón Vega</div>
              </div>
            </div>
          </div>
        </div>"""

coord_txt = re.sub(old_efirma_badge, new_stamp_badge, coord_txt, flags=re.DOTALL)

# Replace instructions blue box
old_box_pattern = r'<section class="bg-\[#EFF6FF\] border-l-4 border-blue-600 p-4 rounded-r-xl shadow-xs">.*?</section>'
new_box = """<section class="bg-blue-50/80 border-l-4 border-blue-600 p-4.5 rounded-r-xl shadow-xs">
          <div class="flex items-start space-x-3.5">
            <div class="text-blue-600 text-base mt-0.5">
              <span class="material-symbols-outlined text-[22px]">info</span>
            </div>
            <div class="space-y-1">
              <h3 class="text-xs font-bold text-blue-900 uppercase tracking-wider">Lineamiento reglamentario de residencias profesionales</h3>
              <p class="text-xs text-blue-800 leading-relaxed">
                Control Escolar libera las cartas de presentación en el sistema. Los estudiantes imprimen su documento y acuden a la oficina de Coordinación para recabar la <strong>firma autógrafa del Coordinador y el sello de tinta oficial del plantel</strong>. El alumno es responsable de entregarlo a la empresa y subir el acuse sellado al sistema.
              </p>
            </div>
          </div>
        </section>"""
coord_txt = re.sub(old_box_pattern, new_box, coord_txt, flags=re.DOTALL)

# Replace button "Firmar digitalmente" with "Ver formato oficial" / "Registrar firma y sello"
coord_txt = coord_txt.replace(
    '<span>Firmar digitalmente</span>',
    '<span>Validar firma y sello</span>'
)
coord_txt = coord_txt.replace(
    '<i class="fas fa-pen-nib text-institutional-gold"></i>',
    '<span class="material-symbols-outlined text-[16px]">verified</span>'
)
coord_txt = coord_txt.replace(
    '<i class="far fa-eye text-gray-500"></i>',
    '<span class="material-symbols-outlined text-[16px] text-gray-500">visibility</span>'
)

with open(file_coord_carta, 'w', encoding='utf-8') as f:
    f.write(coord_txt)
print("Updated 06-coordinacion/05-firma-cartas.html")

# 3. UPDATE sidebar label in all 06-coordinacion/*.html
for f_coord in glob.glob('sigres-umb/06-coordinacion/*.html'):
    with open(f_coord, 'r', encoding='utf-8') as f:
        t = f.read()
    # Replace sidebar "Firmas" text with "Cartas"
    t = re.sub(r'<span class="text-sm">Firmas</span>', '<span class="text-sm">Cartas</span>', t)
    t = re.sub(r'<span class="material-symbols-outlined text-\[20px\](?: fill)?">draw</span>', '<span class="material-symbols-outlined text-[20px]">description</span>', t)
    t = re.sub(r'Cartas para firma digital', 'Cartas de presentación emitidas', t)
    with open(f_coord, 'w', encoding='utf-8') as f:
        f.write(t)
    print(f"Updated sidebar in {f_coord}")
