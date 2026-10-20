# taller1-g91

Repositorio del **Taller 1 (Grupo 91)** de la asignatura Programación (23200): *Números amigos*.

Este repositorio contiene el notebook Marimo [`notebooks/taller1_g91_mo.py`](notebooks/taller1_g91_mo.py) con los enunciados de los ejercicios. Cada ejercicio tiene una celda con la signatura de la función que debes programar (con `pass` en el cuerpo) y, a continuación, una celda con los ejemplos y la salida esperada.

> [!NOTE]
> **En este taller se permite el uso de asistentes de IA.** El Codespace tiene habilitadas todas las sugerencias de código de VS Code y GitHub Copilot (completado, sugerencias de edición y chat).

> [!IMPORTANT]
> **Lee las secciones a continuación para trabajar correctamente en tu propio repositorio y Codespace**.

---

## 1. Crear tu propia copia del repositorio

Este repositorio es una **plantilla** ("Template repository") de GitHub. Puedes crear tu propio repositorio a partir de él, con tu propio historial y bajo tu propia cuenta, sin necesidad de hacer un fork.

1. En la página de este repositorio en GitHub, pulsa el botón verde **"Use this template"** (arriba a la derecha, junto a "Code").
2. Elige **"Create a new repository"**.
3. Selecciona tu cuenta personal como propietario ("Owner"), ponle un nombre a tu repositorio (**mantén `taller1-g91` preferiblemente**) y márcalo como **privado**.
4. Pulsa **"Create repository"**.

> No necesitas clonar nada en tu ordenador. Todo el trabajo se hace en un Codespace, como se explica a continuación.

---

## 2. Levantar un Codespace

1. Entra en **tu** repositorio (el que has creado en el paso anterior), no en la plantilla original.
2. Pulsa el botón verde **"Code"**.
3. Ve a la pestaña **"Codespaces"**.
4. Pulsa **"Create codespace on main"**.

GitHub construirá el contenedor definido en [.devcontainer/devcontainer.json](.devcontainer/devcontainer.json) e instalará automáticamente las dependencias del proyecto (`uv sync`). La primera vez puede tardar uno o dos minutos. Al terminar se abrirá el notebook del taller en VS Code.

---

## 3. Resolver los ejercicios

Abre [`notebooks/taller1_g91_mo.py`](notebooks/taller1_g91_mo.py) con Marimo. Si no se abre automáticamente en modo notebook, haz clic en el botón **"Open in Marimo"** de la parte superior derecha del editor.

- Sustituye el `pass` de cada función por tu implementación.
- Ejecuta la celda de ejemplos que hay debajo de cada función y compara la salida con la esperada (indicada en los comentarios).
- Mientras una función no esté implementada, sus ejemplos mostrarán `None` o un error. Es lo esperado.

---

## 4. Guardar y subir tus cambios (`push`)

Desde VS Code (en el Codespace), sin usar la terminal:

1. Abre la pestaña **"Source Control"** de la barra lateral (icono de rama con un punto).
2. Escribe un mensaje breve describiendo qué has hecho (por ejemplo: `Implementado suma_divisores_propios`).
3. Pulsa **"Commit"** (el símbolo ✓).
4. Pulsa **"Sync Changes"** (o "Push") para subir el commit a tu repositorio en GitHub.

Si prefieres usar la terminal:

```bash
git add .
git commit -m "Implementado suma_divisores_propios"
git push
```

---

## 5. Terminar la ejecución del Codespace

**Esto es muy importante**: un Codespace que se deja abierto sigue consumiendo horas de cómputo aunque no estés trabajando en él, y la cuota mensual gratuita es limitada.

**Desde el Codespace:** abre la paleta de comandos con `F1` (o `Ctrl+Shift+P`) y escribe **"Stop Current Codespace"** → Enter.

**Desde la página del repositorio en GitHub:** pestaña **Code** → sección **Codespaces** → tres puntos **⋯** junto al Codespace activo → **Stop Codespace**.
