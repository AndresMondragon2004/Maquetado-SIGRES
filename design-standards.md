# DESIGN SYSTEM — SIGRES-UMB
**Sistema Integral para la Gestión de Residencias Profesionales**  
*Universidad Mexiquense del Bicentenario · UES San José del Rincón · Ciclo 26-27/1*  
**Versión del estándar:** 2.1 (Alineación Arquitectónica de Navegación, Notificaciones y Tokens)

---

## 1. TOKENS DE DISEÑO (Tailwind Config Unificado)

Para garantizar consistencia cromática, tipográfica y espacial en las 69 pantallas del sistema, se establece una única configuración canónica de Tailwind CSS cargada en el `<head>`.

```html
<script src="https://cdn.tailwindcss.com"></script>
<script>
  tailwind.config = {
    theme: {
      extend: {
        colors: {
          umb: {
            guinda: '#681B2B',
            'guinda-dark': '#4F1420',
            'guinda-light': '#F9F5F6',
            dorado: '#9E773B',
            'dorado-dark': '#7F5E2B',
            'dorado-light': '#FEF3C7',
            surface: '#F4F5F7',
            card: '#FFFFFF',
            border: '#E2E8F0',
            carbon: '#1A1A1A',
            muted: '#544244',
            outline: '#877273',
            success: '#2D8C4E',
            warning: '#D69E2E',
            danger: '#C53030',
            info: '#2B6CB0'
          }
        },
        fontFamily: {
          sans: ['Inter', 'sans-serif']
        },
        borderRadius: {
          card: '8px',
          badge: '9999px',
          modal: '12px'
        },
        boxShadow: {
          card: '0 1px 3px 0 rgba(0, 0, 0, 0.06), 0 1px 2px -1px rgba(0, 0, 0, 0.04)',
          'card-hover': '0 10px 15px -3px rgba(104, 27, 43, 0.08), 0 4px 6px -4px rgba(0, 0, 0, 0.04)',
          modal: '0 20px 25px -5px rgba(0, 0, 0, 0.15), 0 8px 10px -6px rgba(0, 0, 0, 0.1)'
        }
      }
    }
  }
</script>
```

---

## 2. ESTRATEGIA DE ICONOGRAFÍA

### Elección Oficial: **Opción A — Material Symbols Outlined (Google Fonts)**

#### Justificación Técnica y de Diseño:
1. **Consistencia Visual con los Prototipos de Stitch**: Todo el conjunto de pantallas de referencia y maquetación interactiva fue concebido bajo la métrica y proporción óptica de Google Material Symbols.
2. **Facilidad de Mantenimiento y Reducción de Ruido en el DOM**: Reemplazar bloques de código SVG inline por `<span class="material-symbols-outlined">icon_name</span>` reduce el peso de cada archivo HTML entre 25% y 40%, facilitando auditorías masivas y cambios globales.
3. **Control de Relleno Dinámico**: Permite alternar entre estado normal (outline) y estado activo (fill) en navegación mediante la clase de soporte `.fill`.

#### Implementación en `<head>`:
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />

<style>
  .material-symbols-outlined {
    font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
    display: inline-block;
    vertical-align: middle;
    line-height: 1;
  }
  .material-symbols-outlined.fill {
    font-variation-settings: 'FILL' 1, 'wght' 400, 'GRAD' 0, 'opsz' 24;
  }
</style>
```

---

## 3. ESTRATEGIA DE ASSETS LOCALES Y PERSONAS DEL SISTEMA

### 3.1 Logotipo Institucional UMB
- Ruta relativa estándar: `../assets/logo_umb.png` (en carpetas `01-` a `08-`) o `assets/logo_umb.png` (en raíz del portal).
- Contenedor en App Bar: Contenedor blanco con bordes redondeados (`bg-white p-1 rounded h-9 w-auto flex items-center justify-center`).

### 3.2 Avatares de Usuario (Prohibido URLs Externas)
Todos los avatares se generan con **iniciales tipográficas** sobre fondo Guinda UMB:

#### Personal Directivo y Docente UMB:
- **Coordinador de la UES**: Mtro. Luis Ramón Vega Ramírez — Iniciales `LV` (`bg-umb-guinda text-white`)
- **Control Escolar**: Lic. Estefanía Yttesen Nava — Iniciales `EY` (`bg-umb-guinda text-white`)
- **Director Académico UMB + Asesor Externo**: Mtro. Armando Alcalde Martínez — Iniciales `AA` (`bg-umb-guinda text-white`)
- **Asesor Interno ISC**: I.S.C. Leonardo Becerril Sánchez — Iniciales `LB` (`bg-umb-guinda text-white`)
- **Asesor Interno IIAS**: Ing. Jesús Omar Espinoza Díaz — Iniciales `JE` (`bg-umb-guinda text-white`)
- **Asesor Interno LCONT**: L.C. Sergio Sánchez Sánchez — Iniciales `SS` (`bg-umb-guinda text-white`)

#### Estudiante Principal:
- **Jesús Andrés Mondragón Tenorio** — Iniciales `JM` (Matrícula: `13220024`, ISC)

#### Estudiantes Adicionales (Población de listas y tablas — Todos ISC):
- **Lizet Moreno Piña** — Iniciales `LM` (Matrícula: `13210045`)
- **Cristofer Piña Rodríguez** — Iniciales `CP` (Matrícula: `13200118`)
- **Rodolfo Cruz Ibarra** — Iniciales `RC` (Matrícula: `13210033`)
- **Marco Antonio García Cruz** — Iniciales `MG` (Matrícula: `13200089`)
- **Alan Fernando Sánchez Romero** — Iniciales `AS` (Matrícula: `13210112`)
- **Daniel Benítez** — Iniciales `DB` (Matrícula: `13200056`)
- **Sofía Cortez García** — Iniciales `SC` (Matrícula: `13210077`)

> [!IMPORTANT]
> **Nombres obsoletos / Prohibidos en el proyecto:**
> Queda estrictamente descartado el uso de: *Valeria Reyes Montiel, Dra. Patricia Morales Velázquez, Ing. Roberto Almanza Torres, Lic. Mariana Estrada Gómez, Carlos Mendoza Nava, Daniela Miranda Gómez, Jorge Luis Morales Ortiz, Andrea Lizbeth Peña Cruz, Carlos Mendoza Cruz, David Alanís Navarrete, Mariana Cruz Garduño, Mtra. Patricia Mora, Dra. Carmen Álvarez, Carlos Méndez, Mtro. Fernando Bernal*.

---

### 3.3 Datos Oficiales de la Empresa Receptora (Proyecto Interno UMB)

El proyecto de residencia profesional se desarrolla dentro de la **propia Universidad Mexiquense del Bicentenario (Dirección Académica)**, por tratarse de un desarrollo institucional estratégico.

- **Empresa receptora**: Universidad Mexiquense del Bicentenario · Dirección Académica
- **RFC**: `UMB850101HDFXXX01`
- **Sector**: Público · Educación Superior
- **Dirección**: Carretera a San José del Rincón, s/n, San José del Rincón, Estado de México
- **Convenio**: No aplica (proyecto interno institucional)
- **Asesor externo**: Mtro. Armando Alcalde Martínez (Director Académico UMB)

> [!CAUTION]
> **Prohibición de empresas externas ficticias:**
> No utilizar bajo ninguna circunstancia el nombre *"TechSol Solutions México S.A. de C.V."* en ninguna pantalla.

---

## 4. COMPONENTES ESTÁNDAR POR ROL

### 4.1 App Bar Superior Canónica (64px)

- **Altura fija**: `h-16` (64px).
- **Fondo**: `bg-umb-guinda` (`#681B2B`), texto en `text-white`.
- **Borde inferior**: `border-b border-umb-guinda-dark` (`#4F1420`).
- **z-index**: `z-50`.
- **Estructura fija izquierda**:
  - Logo UMB local (`../assets/logo_umb.png`) en cápsula blanca (`h-8`).
  - Separador vertical blanco sutil (`h-6 w-px bg-white/20 hidden sm:block`).
  - Nombre del sistema: `SIGRES-UMB` (`font-bold text-base tracking-tight text-white`).
  - Plantel: `UES San José del Rincón` (`text-[11px] text-white/80 hidden sm:block`).
  - Breadcrumb dinámico: `hidden lg:flex items-center text-xs text-white/80 ml-4 pl-4 border-l border-white/20` (ej. `Estudiante / Inicio`).
- **Estructura fija derecha**:
  - **Campana de notificaciones**:
    - Para los roles **Estudiante, Asesor Interno, Asesor Externo, Control Escolar y Dirección**: El ícono de campana despliega el panel/dropdown transversal [`08-transversales/04-centro-notificaciones.html`](file:///c:/Users/Pc/Downloads/Maquetado%20-%20Residencia/sigres-umb/08-transversales/04-centro-notificaciones.html) (NO tienen pantalla de notificaciones en su sidebar).
    - Para el rol **Coordinación**: Además del componente de notificaciones en el App Bar, cuenta con la pantalla dedicada de emisión y gestión institucional [`06-coordinacion/07-notificaciones.html`](file:///c:/Users/Pc/Downloads/Maquetado%20-%20Residencia/sigres-umb/06-coordinacion/07-notificaciones.html).
    - Indicador de alerta: `absolute top-1.5 right-1.5 w-2.5 h-2.5 bg-umb-warning rounded-full ring-2 ring-umb-guinda`.
  - Separador vertical (`h-6 w-px bg-white/20`).
  - Widget de usuario: Avatar con iniciales circulares (`w-8 h-8 rounded-full bg-white/20 ring-1 ring-white/40 flex items-center justify-center font-bold text-xs`) + Nombre y Rol (`hidden md:flex flex-col text-right`).

---

### 4.2 Sidebar Desktop (260px) por Rol

- **Ancho**: `w-[260px]` fijo.
- **Posición**: `fixed top-16 bottom-0 left-0 bg-white border-r border-umb-border z-40 hidden lg:flex flex-col justify-between py-4 px-3`.
- **Ficha superior de usuario**:
  - Avatar con iniciales (`w-10 h-10 rounded-full bg-umb-guinda text-white flex items-center justify-center font-bold text-sm ring-2 ring-umb-guinda/10`).
  - Nombre completo, matrícula/cargo y badge de estatus activo.
- **Estilo de Ítem de Navegación**:
  - **Activo**: `bg-umb-guinda text-white font-semibold rounded-lg h-11 px-3.5 flex items-center gap-3 shadow-sm` (ícono con `.fill`).
  - **Inactivo**: `text-umb-muted hover:bg-umb-surface hover:text-umb-carbon font-medium rounded-lg h-11 px-3.5 flex items-center gap-3 transition-colors`.
- **Pie del Sidebar**:
  - Indicador de ciclo (`Ciclo 26-27/1`) y punto de estatus verde pulsante (`Sistema en línea`).

#### Lista Oficial de Ítems de Navegación en Sidebar:

1. **Estudiante** (`02-estudiante/`) — Usuario: *Jesús Andrés Mondragón Tenorio (JM)*
   - 1. `home` — **Inicio** (`01-dashboard.html`)
   - 2. `menu_book` — **Bitácoras** (`08-mis-bitacoras.html`)
   - 3. `folder` — **Expediente** (`02-mi-expediente.html`)
   - 4. `description` — **Informes** (`13-mis-informes.html`)
   - 5. `person` — **Perfil** (`14-mi-perfil.html`)

2. **Asesor Interno** (`03-asesor-interno/`) — Usuario: *I.S.C. Leonardo Becerril Sánchez (LB)*
   - 1. `home` — **Inicio** (`01-dashboard.html`)
   - 2. `group` — **Mis alumnos** (`02-mis-alumnos.html`)
   - 3. `assignment` — **Asesorías** (`04-registrar-asesoria.html`)
   - 4. `fact_check` — **Evaluaciones** (`05-revisar-bitacoras.html` — *Hub central desde donde se evalúa el informe parcial y final*)
   - 5. `person` — **Perfil** (`08-mi-perfil.html`)

3. **Asesor Externo** (`04-asesor-externo/`) — Usuario: *Mtro. Armando Alcalde Martínez (AA)*
   - 1. `home` — **Inicio** (`01-dashboard.html`)
   - 2. `menu_book` — **Bitácoras** (`02-bitacoras-por-validar.html`)
   - 3. `group` — **Residentes** (`04-residentes-asignados.html`)
   - 4. `history` — **Historial** (`05-historial-validaciones.html`)
   - 5. `person` — **Perfil** (`06-mi-perfil.html`)

4. **Control Escolar** (`05-control-escolar/`) — Usuario: *Lic. Estefanía Yttesen Nava (EY)*
   - 1. `home` — **Inicio** (`01-dashboard.html`)
   - 2. `folder_shared` — **Expedientes** (`02-bandeja-expedientes.html`)
   - 3. `verified` — **Documentos** (`04-validar-documentos.html`)
   - 4. `domain` — **Empresas** (`06-catalogo-empresas.html`)
   - 5. `analytics` — **Reportes** (`08-reportes.html`)
   - 6. `person` — **Perfil** (`09-mi-perfil.html`)

5. **Coordinación** (`06-coordinacion/`) — Usuario: *Mtro. Luis Ramón Vega Ramírez (LV)*
   - 1. `monitoring` — **Monitoreo** (`01-dashboard-monitoreo.html`)
   - 2. `school` — **Cohortes** (`02-cohortes-carreras.html`)
   - 3. `warning` — **Riesgos** (`03-supervision-riesgo.html`)
   - 4. `support` — **Contingencias** (`04-contingencias.html`)
   - 5. `summarize` — **Reportes** (`06-reportes-ejecutivos.html`)
   - 6. `person` — **Perfil** (`08-mi-perfil.html`)
   *(Nota: Cuenta adicionalmente con la pantalla de `07-notificaciones.html` accesible desde el flujo de gestión).*

6. **Dirección Académica** (`07-direccion/`) — Usuario: *Mtro. Armando Alcalde Martínez (AA)*
   - 1. `dashboard` — **Dashboard** (`01-dashboard-ejecutivo.html`)
   - 2. `handshake` — **Vinculación** (`02-vinculacion-convenios.html`)
   - 3. `factory` — **Sectores** (`03-sectores-productivos.html`)
   - 4. `verified_user` — **Acreditación** (`04-reportes-acreditacion.html`)
   - 5. `settings` — **Configuración** (`05-configuracion-global.html`)
   - 6. `person` — **Perfil** (`06-mi-perfil.html`)

---

### 4.3 Bottom Navigation Mobile (Dispositivos < 1024px — Máximo 5 Ítems)

- **Altura**: `h-16` (64px).
- **Breakpoint**: `lg:hidden fixed bottom-0 left-0 right-0 bg-white border-t border-umb-border shadow-lg z-40 flex items-center justify-around px-2`.
- **Regla de 5 Ítems en Mobile**:
  - Para los roles con más de 5 ítems en el sidebar, se priorizan los 5 accesos operativos críticos en la barra inferior móvil, dejando los ítems analíticos/secundarios accesibles desde el sidebar o dashboards:
    - **Estudiante** (5 ítems): Inicio, Bitácoras, Expediente, Informes, Perfil.
    - **Asesor Interno** (5 ítems): Inicio, Mis alumnos, Asesorías, Evaluaciones, Perfil.
    - **Asesor Externo** (5 ítems): Inicio, Bitácoras, Residentes, Historial, Perfil.
    - **Control Escolar** (5 ítems): Inicio, Expedientes, Documentos, Empresas, Perfil. *(Reportes accesible desde el menú secundario o dashboard)*.
    - **Coordinación** (5 ítems): Monitoreo, Riesgos, Contingencias, Reportes, Perfil. *(Cohortes accesible desde el menú secundario o dashboard)*.
    - **Dirección** (5 ítems): Dashboard, Vinculación, Sectores, Acreditación, Perfil. *(Configuración accesible desde el menú secundario o dashboard)*.
- **Estilo de Ítem Mobile**:
  - **Activo**: `flex flex-col items-center justify-center flex-1 py-1 text-umb-guinda` (ícono `text-[22px]` con clase `.fill` + texto `text-[11px] font-semibold`).
  - **Inactivo**: `flex flex-col items-center justify-center flex-1 py-1 text-umb-outline hover:text-umb-carbon` (ícono `text-[22px]` + texto `text-[11px] font-normal`).

---

### 4.4 Footer Institucional Estándar

- **Ubicación**: Al final del contenedor principal `<main>`, con margen inferior de seguridad (`pb-24 lg:pb-8`).
- **Fondo**: Transparente sobre `bg-umb-surface`.
- **Alineación**: Centrado.
- **Estructura y Texto Exacto**:
```html
<footer class="pt-8 pb-4 text-center text-[12px] text-umb-outline space-y-1">
  <p>SIGRES-UMB — Sistema integral para la gestión de residencias profesionales</p>
  <p>Universidad Mexiquense del Bicentenario · UES San José del Rincón · Ciclo 26-27/1</p>
</footer>
```

---

## 5. COMPONENTES REUTILIZABLES

### 5.1 Botones (Target táctil mínimo 44px)

| Tipo de Botón | Clases Tailwind Estándar | Uso / Contexto |
| :--- | :--- | :--- |
| **Primario (Guinda)** | `h-11 px-5 rounded-lg bg-umb-guinda hover:bg-umb-guinda-dark text-white font-semibold text-sm transition-all shadow-sm focus:outline-none focus:ring-2 focus:ring-umb-guinda/40 active:scale-[0.98] inline-flex items-center justify-center gap-2` | Acción principal (Guardar, Registrar, Validar, Firmar) |
| **Secundario (Dorado / Contorno)** | `h-11 px-5 rounded-lg bg-white border border-umb-dorado text-umb-dorado hover:bg-umb-dorado-light font-semibold text-sm transition-all focus:outline-none focus:ring-2 focus:ring-umb-dorado/40 inline-flex items-center justify-center gap-2` | Acción secundaria de apoyo o descarga |
| **Neutro / Outline** | `h-11 px-5 rounded-lg bg-white border border-umb-border hover:bg-umb-surface text-umb-carbon font-medium text-sm transition-all focus:outline-none focus:ring-2 focus:ring-umb-border inline-flex items-center justify-center gap-2` | Cancelar, Volver, Filtros |
| **Ghost (Sin borde)** | `h-11 px-4 rounded-lg text-umb-muted hover:text-umb-guinda hover:bg-umb-guinda-light font-medium text-sm transition-all inline-flex items-center justify-center gap-2` | Enlaces secundarios en tablas o acciones rápidas |
| **Peligro (Destructivo)** | `h-11 px-5 rounded-lg bg-umb-danger hover:bg-red-700 text-white font-semibold text-sm transition-all shadow-sm focus:outline-none focus:ring-2 focus:ring-umb-danger/40 inline-flex items-center justify-center gap-2` | Eliminar registro, Dar de baja, Rechazar |
| **Éxito (Confirmación)** | `h-11 px-5 rounded-lg bg-umb-success hover:bg-emerald-700 text-white font-semibold text-sm transition-all shadow-sm focus:outline-none focus:ring-2 focus:ring-umb-success/40 inline-flex items-center justify-center gap-2` | Aprobar trámite, Liberar cartas |

---

### 5.2 Badges de Estatus (Pill `rounded-full` con Tokens UMB)

Todos los badges llevan `rounded-full`, tipografía `text-xs` (o `text-[11px]`), `font-semibold`, y espaciado `px-2.5 py-0.5`:

| Estado | Clases Tailwind con Tokens UMB | Ejemplo de Uso |
| :--- | :--- | :--- |
| **Aprobado / Completado** | `bg-umb-success/10 text-umb-success border border-umb-success/30` | Informe aprobado, Empresa validada, Horas cumplidas |
| **Pendiente / En revisión** | `bg-umb-warning/15 text-umb-warning border border-umb-warning/40` | Bitácora por validar, Documento en revisión |
| **Rechazado / Peligro** | `bg-umb-danger/10 text-umb-danger border border-umb-danger/30` | Documento observado, Residencia cancelada |
| **En curso / Activo** | `bg-umb-success/5 text-umb-success border border-umb-success/40` | Residencia activa, Ciclo activo |
| **En riesgo (Alerta preventiva)**| `bg-orange-100 text-orange-800 border border-orange-200` | Asistencia < 85%, Retraso en bitácoras |
| **Informativo / Neutro** | `bg-umb-surface text-umb-muted border border-umb-border` | 640 horas meta, Ciclo 26-27/1 |

---

### 5.3 Tarjetas (Cards)

- **Card Base**: `bg-white rounded-lg border border-umb-border shadow-card p-5 sm:p-6 transition-all`
- **Card Destacada (Acento Guinda)**: `bg-white rounded-lg border border-umb-border border-l-4 border-l-umb-guinda shadow-card p-6`
- **Card de Métrica (KPI)**: `bg-white rounded-lg border border-umb-border p-5 flex flex-col justify-between hover:shadow-card-hover transition-all`
  - Encabezado: Título descriptivo (`text-xs font-semibold text-umb-muted uppercase tracking-wider`) + Ícono en contenedor circular `w-9 h-9 rounded-full bg-umb-guinda-light text-umb-guinda`.
  - Número principal: `text-3xl font-bold text-umb-carbon tracking-tight`.
  - Subtexto / Tendencia: `text-xs text-umb-outline mt-1`.
- **Card de Alerta / Callout**:
  - Advertencia: `bg-umb-warning/10 rounded-lg border border-umb-warning/30 p-4 text-umb-warning text-sm`
  - Error: `bg-umb-danger/10 rounded-lg border border-umb-danger/30 p-4 text-umb-danger text-sm`
  - Info: `bg-umb-info/10 rounded-lg border border-umb-info/30 p-4 text-umb-info text-sm`

---

### 5.4 Inputs y Controles de Formulario

- **Text / Email / Number**: `w-full h-11 px-3.5 rounded-lg bg-white border border-umb-border text-umb-carbon text-sm placeholder:text-umb-outline/70 focus:outline-none focus:ring-2 focus:ring-umb-guinda focus:border-transparent transition-all`
- **Select**: `w-full h-11 px-3.5 rounded-lg bg-white border border-umb-border text-umb-carbon text-sm focus:outline-none focus:ring-2 focus:ring-umb-guinda focus:border-transparent transition-all`
- **Textarea**: `w-full p-3 rounded-lg bg-white border border-umb-border text-umb-carbon text-sm placeholder:text-umb-outline/70 focus:outline-none focus:ring-2 focus:ring-umb-guinda focus:border-transparent transition-all`
- **Checkbox**: `w-4 h-4 rounded border-umb-border text-umb-guinda focus:ring-umb-guinda`

---

### 5.5 Modales

- **Overlay**: `fixed inset-0 bg-black/50 backdrop-blur-sm z-50 flex items-center justify-center p-4`
- **Contenedor Modal**: `bg-white rounded-xl shadow-modal max-w-lg w-full overflow-hidden border border-umb-border animate-in fade-in zoom-in duration-200`
- **Estructura**:
  - Encabezado con título e ícono de cierre.
  - Cuerpo con texto explicativo e inputs o detalles del registro.
  - Pie con acciones alineadas a la derecha (`Cancelar` neutro y `Aceptar` primario o de peligro).

---

## 6. REGLAS DE ESCRITURA Y FORMATO EDITORIAL

1. **Regla de Sentence Case Obligatoria**:
   - **Solo la primera letra en mayúscula** en títulos de sección, subtítulos, encabezados de tarjeta, etiquetas de campo, botones y opciones de menú.
   - *Correcto*: "Mis bitácoras", "Registrar asesoría", "Generar carta de presentación", "Progreso de horas".
   - *Incorrecto*: "Mis Bitácoras", "REGISTRAR ASESORÍA", "Generar Carta De Presentación".
2. **Excepciones de Siglas y Títulos Académicos**:
   - Siglas institucionales y de carrera: `UMB`, `SIGRES-UMB`, `UES`, `ISC`, `IIAS`, `LCONT`, `I.S.C.`, `L.C.`
   - Títulos y grados: `Ing.`, `Mtro.`, `Mtra.`, `Dr.`, `Dra.`, `Lic.`
3. **Formatos Oficiales de Negocio**:
   - **Matrícula estudiantil**: Exactamente 10 dígitos numéricos (ejemplo: `13220024`, `13210045`).
   - **Ciclo activo**: `26-27/1`.
   - **Folio de residencia**: `UMB-SJR-2026-XXX` (ejemplo: `UMB-SJR-2026-042`).
   - **Folio de convenio**: `No aplica` (proyecto interno institucional).
   - **Métricas de tiempo**: "320 horas", "640 horas", "7 horas diarias", "35 horas semanales".
   - **Asistencia**: "80% asistencia mínima", "Alerta preventiva al 85%".
   - **Calificación**: Escala 0 a 100, mínima aprobatoria "70/100".

---

## 7. REGLAS DE RESPONSIVIDAD Y BREAKPOINTS

```
+-------------------------------------------------------------------------+
| Breakpoint Mobile (< 768px):                                           |
| - Sidebar oculto                                                        |
| - Bottom Nav visible (fijo abajo, 64px, máx 5 ítems)                    |
| - Padding contenido: p-4 pb-24                                          |
| - Grids a 1 columna                                                     |
+-------------------------------------------------------------------------+
| Breakpoint Tablet (768px - 1023px):                                     |
| - Sidebar oculto (drawer colapsable)                                    |
| - Bottom Nav visible (fijo abajo, 64px, máx 5 ítems)                    |
| - Padding contenido: p-6 pb-24                                          |
| - Grids adaptables a 2 columnas                                         |
+-------------------------------------------------------------------------+
| Breakpoint Desktop (≥ 1024px / lg):                                     |
| - Sidebar visible fijo a la izquierda (w-[260px])                       |
| - Bottom Nav oculto (hidden)                                            |
| - Contenedor principal con margen izquierdo: lg:ml-[260px]              |
| - Padding contenido: p-8 max-w-[1280px] centrado                        |
| - Grids complejos (60%/40%, 3 columnas de KPIs)                         |
+-------------------------------------------------------------------------+
```

---

## 8. BOTÓN FLOTANTE DE ACCESO AL PORTAL (Navegación del Prototipo)

Para facilitar la auditoría y navegación fluida entre las 69 pantallas del prototipo sin alterar la experiencia de usuario, se incluye un botón flotante estándar en todas las pantallas de roles:

- **Posición**: `fixed bottom-6 right-6 z-50`
- **Fondo**: `bg-umb-guinda` con borde sutil dorado `border-umb-dorado/40`
- **Texto**: `Ir al portal`
- **Snippet estándar con comentario de producción**:

```html
<!-- BOTÓN FLOTANTE AL PORTAL (Solo para navegación del prototipo - Eliminar en producción) -->
<aside aria-label="Navegación al portal de prototipos" class="fixed bottom-6 right-6 z-50">
  <a href="../index.html" class="h-10 px-4 rounded-full bg-umb-guinda hover:bg-umb-guinda-dark text-white text-xs font-semibold shadow-xl border border-umb-dorado/40 flex items-center gap-2 backdrop-blur-md transition-all hover:scale-105 focus:outline-none focus:ring-2 focus:ring-umb-dorado">
    <span class="material-symbols-outlined text-sm text-amber-300">apps</span>
    <span>Ir al portal</span>
  </a>
</aside>
```

---

## 9. MAPA DE NAVEGACIÓN Y ENLACES RELATIVOS POR ROL

Para asegurar que todas las pantallas estén interconectadas de manera consistente y sin enlaces muertos (`#`), se establece el mapa canónico de rutas relativas:

### 9.1 Rol Estudiante (`02-estudiante/`)
- **Inicio**: `01-dashboard.html` (Breadcrumb: `Estudiante / Inicio`)
- **Expediente**: `02-mi-expediente.html` (Breadcrumb: `Estudiante / Mi expediente`)
  - Registro de empresa: `04-registrar-empresa.html`
  - Estatus validación empresa: `05-estatus-validacion-empresa.html`
  - Solicitud de residencia: `06-solicitud-residencia.html`
  - Carta de presentación: `07-carta-presentacion-generada.html`
- **Bitácoras**: `08-mis-bitacoras.html` (Breadcrumb: `Estudiante / Mis bitácoras`)
  - Nueva bitácora: `09-nueva-bitacora.html`
  - Detalle bitácora: `10-detalle-bitacora.html`
- **Informes**: `13-mis-informes.html` (Breadcrumb: `Estudiante / Mis informes`)
  - Progreso: `11-mi-progreso.html`
  - Cronograma: `12-cronograma.html`
- **Perfil**: `14-mi-perfil.html` (Breadcrumb: `Estudiante / Mi perfil`)

### 9.2 Rol Asesor Interno (`03-asesor-interno/`)
- **Inicio**: `01-dashboard.html` (Breadcrumb: `Asesor interno / Inicio`)
- **Mis alumnos**: `02-mis-alumnos.html` (Breadcrumb: `Asesor interno / Mis alumnos`)
  - Detalle alumno: `03-detalle-alumno.html`
- **Asesorías**: `04-registrar-asesoria.html` (Breadcrumb: `Asesor interno / Registrar asesoría`)
- **Evaluaciones**: `05-revisar-bitacoras.html` (Breadcrumb: `Asesor interno / Evaluaciones`)
  - Evaluar informe parcial: `06-evaluar-informe-parcial.html`
  - Evaluar informe final: `07-evaluar-informe-final.html`
- **Perfil**: `08-mi-perfil.html` (Breadcrumb: `Asesor interno / Mi perfil`)

### 9.3 Rol Asesor Externo (`04-asesor-externo/`)
- **Inicio**: `01-dashboard.html` (Breadcrumb: `Asesor externo / Inicio`)
- **Bitácoras**: `02-bitacoras-por-validar.html` (Breadcrumb: `Asesor externo / Bitácoras por validar`)
  - Detalle bitácora: `03-detalle-bitacora.html`
- **Residentes**: `04-residentes-asignados.html` (Breadcrumb: `Asesor externo / Residentes asignados`)
- **Historial**: `05-historial-validaciones.html` (Breadcrumb: `Asesor externo / Historial de validaciones`)
- **Perfil**: `06-mi-perfil.html` (Breadcrumb: `Asesor externo / Mi perfil`)

### 9.4 Rol Control Escolar (`05-control-escolar/`)
- **Inicio**: `01-dashboard.html` (Breadcrumb: `Control Escolar / Inicio`)
- **Expedientes**: `02-bandeja-expedientes.html` (Breadcrumb: `Control Escolar / Bandeja de expedientes`)
  - Detalle expediente: `03-detalle-expediente.html`
- **Documentos**: `04-validar-documentos.html` (Breadcrumb: `Control Escolar / Validar documentos`)
  - Generar carta: `05-generar-carta.html`
- **Empresas**: `06-catalogo-empresas.html` (Breadcrumb: `Control Escolar / Catálogo de empresas`)
  - Validar empresas nuevas: `07-validar-empresas-nuevas.html`
- **Reportes**: `08-reportes.html` (Breadcrumb: `Control Escolar / Reportes`)
- **Perfil**: `09-mi-perfil.html` (Breadcrumb: `Control Escolar / Mi perfil`)

### 9.5 Rol Coordinación (`06-coordinacion/`)
- **Monitoreo**: `01-dashboard-monitoreo.html` (Breadcrumb: `Coordinación / Monitoreo`)
- **Cohortes**: `02-cohortes-carreras.html` (Breadcrumb: `Coordinación / Cohortes por carrera`)
- **Riesgos**: `03-supervision-riesgo.html` (Breadcrumb: `Coordinación / Supervisión de riesgo`)
- **Contingencias**: `04-contingencias.html` (Breadcrumb: `Coordinación / Contingencias`)
- **Reportes**: `06-reportes-ejecutivos.html` (Breadcrumb: `Coordinación / Reportes ejecutivos`)
- **Notificaciones**: `07-notificaciones.html` (Breadcrumb: `Coordinación / Notificaciones`)
- **Perfil**: `08-mi-perfil.html` (Breadcrumb: `Coordinación / Mi perfil`)

### 9.6 Rol Dirección Académica (`07-direccion/`)
- **Dashboard**: `01-dashboard-ejecutivo.html` (Breadcrumb: `Dirección / Dashboard ejecutivo`)
- **Vinculación**: `02-vinculacion-convenios.html` (Breadcrumb: `Dirección / Vinculación y convenios`)
- **Sectores**: `03-sectores-productivos.html` (Breadcrumb: `Dirección / Sectores productivos`)
- **Acreditación**: `04-reportes-acreditacion.html` (Breadcrumb: `Dirección / Reportes de acreditación`)
- **Configuración**: `05-configuracion-global.html` (Breadcrumb: `Dirección / Configuración global`)
- **Perfil**: `06-mi-perfil.html` (Breadcrumb: `Dirección / Mi perfil`)

---

## 10. LISTA DE VERIFICACIÓN PARA AUDITORÍA MASIVA

Cada archivo HTML debe cumplir con:
- [ ] Tailwind Config unificado con prefijo `umb-`.
- [ ] Inclusión de Google Fonts Inter y Material Symbols Outlined.
- [ ] Logo UMB local `../assets/logo_umb.png` sin URLs externas.
- [ ] Persona y matrícula actualizada según el rol y escenario institucional.
- [ ] Empresa receptora: *Universidad Mexiquense del Bicentenario · Dirección Académica*.
- [ ] App Bar fija `h-16`, color `bg-umb-guinda`, z-50 con campana de notificaciones y dropdown transversal.
- [ ] Sidebar fijo `w-[260px]` con los ítems y enlaces relativos exactos.
- [ ] Bottom Navigation móvil funcional en `< 1024px` con máximo 5 ítems prioritarios.
- [ ] Regla *Sentence case* en títulos, botones y etiquetas.
- [ ] Botón flotante "Ir al portal" en `bottom-6 right-6` con comentario HTML para producción.
