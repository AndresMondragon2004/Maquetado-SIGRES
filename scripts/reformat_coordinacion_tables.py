import re

file_path = 'sigres-umb/06-coordinacion/03-supervision-riesgo.html'

students_data = [
    {
        'initials': 'RM',
        'name': 'Rodrigo Mendoza Bautista',
        'matricula': '13200091',
        'asesor': 'I.S.C. Leonardo Becerril Sánchez',
        'carrera': 'ISC',
        'asistencia': '75%',
        'asistencia_tag': 'Mín. 80%',
        'horas': '180 / 640 hrs',
        'pct_label': '28% avance',
        'pct': 28,
        'riesgo': 'Crítico',
        'riesgo_type': 'critico',
        'accion_icon': 'assignment_late',
        'accion_icon_color': 'text-red-600',
        'accion_text': 'Citatorio emitido 8 oct',
        'btn_action': 'Citatorio',
        'btn_color': 'bg-red-700 hover:bg-red-800'
    },
    {
        'initials': 'BS',
        'name': 'Brenda Karina Soto',
        'matricula': '13210014',
        'asesor': 'L.C. Sergio Sánchez Sánchez',
        'carrera': 'LCONT',
        'asistencia': '78%',
        'asistencia_tag': 'Mín. 80%',
        'horas': '190 / 640 hrs',
        'pct_label': '30% avance',
        'pct': 30,
        'riesgo': 'Crítico',
        'riesgo_type': 'critico',
        'accion_icon': 'notification_important',
        'accion_icon_color': 'text-amber-600',
        'accion_text': 'Recordatorio 5 oct',
        'btn_action': 'Citatorio',
        'btn_color': 'bg-red-700 hover:bg-red-800'
    },
    {
        'initials': 'CM',
        'name': 'Cristofer Piña Rodríguez',
        'matricula': '13200018',
        'asesor': 'Ing. Jesús Omar Espinoza Díaz',
        'carrera': 'IIAS',
        'asistencia': '78%',
        'asistencia_tag': 'Mín. 80%',
        'horas': '190 / 640 hrs',
        'pct_label': '30% avance',
        'pct': 30,
        'riesgo': 'Crítico',
        'riesgo_type': 'critico',
        'accion_icon': 'remove',
        'accion_icon_color': 'text-slate-400',
        'accion_text': 'Sin acciones previas',
        'btn_action': 'Citatorio',
        'btn_color': 'bg-red-700 hover:bg-red-800'
    },
    {
        'initials': 'DB',
        'name': 'Daniel Benítez',
        'matricula': '13190042',
        'asesor': 'L.C. Sergio Sánchez Sánchez',
        'carrera': 'LCONT',
        'asistencia': '82%',
        'asistencia_tag': 'Rezago de 80 h',
        'horas': '240 / 640 hrs',
        'pct_label': '37.5% avance',
        'pct': 37.5,
        'riesgo': 'Moderado',
        'riesgo_type': 'moderado',
        'accion_icon': 'remove',
        'accion_icon_color': 'text-slate-400',
        'accion_text': 'Sin acciones previas',
        'btn_action': 'Recordatorio',
        'btn_color': 'bg-amber-600 hover:bg-amber-700'
    },
    {
        'initials': 'ES',
        'name': 'Emmanuel Sánchez Vilchis',
        'matricula': '13210039',
        'asesor': 'Ing. Jesús Omar Espinoza Díaz',
        'carrera': 'IIAS',
        'asistencia': '85%',
        'asistencia_tag': 'Rezago de 110 h',
        'horas': '210 / 640 hrs',
        'pct_label': '33% avance',
        'pct': 33,
        'riesgo': 'Moderado',
        'riesgo_type': 'moderado',
        'accion_icon': 'mark_email_read',
        'accion_icon_color': 'text-amber-600',
        'accion_text': 'Recordatorio 3 oct',
        'btn_action': 'Recordatorio',
        'btn_color': 'bg-amber-600 hover:bg-amber-700'
    },
    {
        'initials': 'DP',
        'name': 'Diana Laura Pérez Estrada',
        'matricula': '13220076',
        'asesor': 'I.S.C. Leonardo Becerril Sánchez',
        'carrera': 'ISC',
        'asistencia': '87%',
        'asistencia_tag': 'Rezago de 70 h',
        'horas': '250 / 640 hrs',
        'pct_label': '39% avance',
        'pct': 39,
        'riesgo': 'Moderado',
        'riesgo_type': 'moderado',
        'accion_icon': 'forum',
        'accion_icon_color': 'text-indigo-600',
        'accion_text': 'Revisión con asesor 6 oct',
        'btn_action': 'Recordatorio',
        'btn_color': 'bg-amber-600 hover:bg-amber-700'
    },
    {
        'initials': 'JC',
        'name': 'Jimena Cruz Garduño',
        'matricula': '13210088',
        'asesor': 'Ing. Jesús Omar Espinoza Díaz',
        'carrera': 'IIAS',
        'asistencia': '84%',
        'asistencia_tag': 'Rezago de 100 h',
        'horas': '220 / 640 hrs',
        'pct_label': '34% avance',
        'pct': 34,
        'riesgo': 'Moderado',
        'riesgo_type': 'moderado',
        'accion_icon': 'remove',
        'accion_icon_color': 'text-slate-400',
        'accion_text': 'Sin acciones previas',
        'btn_action': 'Recordatorio',
        'btn_color': 'bg-amber-600 hover:bg-amber-700'
    },
    {
        'initials': 'MS',
        'name': 'Mateo Salgado Navarrete',
        'matricula': '13200054',
        'asesor': 'I.S.C. Leonardo Becerril Sánchez',
        'carrera': 'ISC',
        'asistencia': '79%',
        'asistencia_tag': 'Mín. 80%',
        'horas': '185 / 640 hrs',
        'pct_label': '29% avance',
        'pct': 29,
        'riesgo': 'Crítico',
        'riesgo_type': 'critico',
        'accion_icon': 'assignment_late',
        'accion_icon_color': 'text-red-600',
        'accion_text': 'Citatorio emitido 7 oct',
        'btn_action': 'Citatorio',
        'btn_color': 'bg-red-700 hover:bg-red-800'
    }
]

rows_html = []
for st in students_data:
    is_crit = st['riesgo_type'] == 'critico'
    row_bg = 'hover:bg-red-50/40' if is_crit else 'hover:bg-amber-50/40'
    badge_bg = 'bg-red-100 text-red-800 border-red-200' if is_crit else 'bg-amber-100 text-amber-800 border-amber-200'
    dot_color = 'bg-red-600' if is_crit else 'bg-amber-500'
    bar_color = 'bg-red-600' if is_crit else 'bg-amber-500'
    asist_color = 'text-red-700' if is_crit else 'text-amber-800'
    asist_tag_bg = 'bg-red-50 text-red-700 border-red-200' if is_crit else 'bg-amber-50 text-amber-800 border-amber-200'

    r = f"""              <!-- FILA: {st['name']} ({st['riesgo']}) -->
              <tr class="{row_bg} transition-colors">
                <!-- Estudiante & Asesor -->
                <td class="py-5 px-5 align-middle">
                  <div class="flex items-center gap-3.5">
                    <div class="w-11 h-11 rounded-full bg-slate-100 text-slate-700 font-bold text-xs flex items-center justify-center shrink-0 border border-slate-200 shadow-2xs">
                      {st['initials']}
                    </div>
                    <div class="space-y-1 min-w-0">
                      <div class="font-bold text-sm text-umb-carbon leading-tight truncate">{st['name']}</div>
                      <div class="flex flex-wrap items-center gap-x-2 gap-y-0.5 text-xs text-umb-outline">
                        <span class="font-mono font-semibold text-slate-700 bg-slate-100 px-2 py-0.5 rounded text-[11px] border border-slate-200/80">{st['matricula']}</span>
                        <span class="text-slate-300">•</span>
                        <span class="text-umb-muted text-[11px] truncate">Asesor: {st['asesor']}</span>
                      </div>
                    </div>
                  </div>
                </td>

                <!-- Carrera -->
                <td class="py-5 px-3 text-center align-middle">
                  <span class="inline-flex items-center justify-center px-2.5 py-1 font-bold rounded-md bg-slate-100 text-slate-700 border border-slate-200 text-xs shadow-2xs">
                    {st['carrera']}
                  </span>
                </td>

                <!-- Motivo del riesgo & Horas (Espacioso, sin saltos forzados de línea) -->
                <td class="py-5 px-5 align-middle">
                  <div class="space-y-2 min-w-[220px]">
                    <!-- Indicador de Asistencia -->
                    <div class="flex items-center gap-2.5 whitespace-nowrap">
                      <span class="text-xs font-bold {asist_color} whitespace-nowrap">{st['asistencia']} asistencia</span>
                      <span class="text-[10px] font-semibold {asist_tag_bg} px-2 py-0.5 rounded-full border whitespace-nowrap">
                        {st['asistencia_tag']}
                      </span>
                    </div>

                    <!-- Barra de progreso -->
                    <div class="w-full bg-slate-200 h-2 rounded-full overflow-hidden">
                      <div class="{bar_color} h-full rounded-full" style="width: {st['pct']}%"></div>
                    </div>

                    <!-- Conteo de Horas -->
                    <div class="flex items-center justify-between gap-2 text-[11px] text-umb-muted whitespace-nowrap">
                      <span>Horas: <strong class="text-slate-800 font-semibold">{st['horas']}</strong></span>
                      <span class="text-slate-500 font-medium">({st['pct_label']})</span>
                    </div>
                  </div>
                </td>

                <!-- Semáforo -->
                <td class="py-5 px-3 text-center align-middle">
                  <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold {badge_bg} border shadow-2xs whitespace-nowrap">
                    <span class="w-2 h-2 rounded-full {dot_color} {'animate-pulse' if is_crit else ''}"></span>
                    {st['riesgo']}
                  </span>
                </td>

                <!-- Última acción -->
                <td class="py-5 px-4 align-middle">
                  <div class="flex items-center gap-1.5 text-xs text-slate-700 font-medium whitespace-nowrap">
                    <span class="material-symbols-outlined text-[18px] {st['accion_icon_color']} shrink-0">{st['accion_icon']}</span>
                    <span>{st['accion_text']}</span>
                  </div>
                </td>

                <!-- Acciones -->
                <td class="py-5 px-5 text-right align-middle">
                  <div class="inline-flex items-center gap-2 justify-end whitespace-nowrap">
                    <button type="button" class="h-8 px-3 rounded-lg border border-umb-border hover:bg-umb-surface text-umb-carbon text-xs font-semibold transition-colors shadow-2xs" title="Ver expediente">
                      Expediente
                    </button>
                    <button type="button" class="h-8 px-3.5 rounded-lg {st['btn_color']} text-white text-xs font-semibold shadow-xs transition-colors" title="Acción recomendada">
                      {st['btn_action']}
                    </button>
                  </div>
                </td>
              </tr>"""
    rows_html.append(r)

table_full_html = """<!-- Indicador visual responsivo para pantallas compactas -->
          <div class="md:hidden flex items-center justify-end gap-1.5 text-[11px] text-umb-outline px-1 mb-1.5">
            <span class="material-symbols-outlined text-[15px] text-umb-dorado">swipe</span>
            <span>Desliza para ver más información →</span>
          </div>

          <!-- Tabla de Datos Espaciosa y Legible -->
          <div class="overflow-x-auto rounded-xl border border-slate-200/80 shadow-xs bg-white">
            <table class="w-full min-w-[1020px] text-left border-collapse text-xs">
              <thead>
                <tr class="bg-slate-50 border-b border-slate-200 text-slate-700 font-bold uppercase tracking-wider text-[11px]">
                  <th class="py-4 px-5 w-[30%]">Estudiante & Tutor Asignado</th>
                  <th class="py-4 px-3 w-[8%] text-center">Carrera</th>
                  <th class="py-4 px-5 w-[28%]">Motivo del riesgo & Horas</th>
                  <th class="py-4 px-3 w-[11%] text-center">Semáforo</th>
                  <th class="py-4 px-4 w-[12%]">Última acción</th>
                  <th class="py-4 px-5 w-[11%] text-right">Acciones</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-200/70">
""" + "\n".join(rows_html) + """
              </tbody>
            </table>
          </div>"""

with open(file_path, 'r', encoding='utf-8') as fl:
    content = fl.read()

# Replace the table block
old_table_pattern = r'(?:<!-- Indicador visual responsivo.*?-->\s*)?<!-- Tabla de Datos Espaciosa y Legible -->.*?<div class="overflow-x-auto.*?</table>\s*</div>'
new_content = re.sub(old_table_pattern, table_full_html, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as fl:
    fl.write(new_content)

print("Applied refined spacious formatting to 03-supervision-riesgo.html.")
