import marimo

__generated_with = "0.16.5"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Taller 1 — 23200 Programación — 20/10/2026

    ## Números amigos

    **Instrucciones:**

    - Sustituye el `pass` de cada función por tu implementación.
    - Cada función debe incluir type hints y docstring, y lanzar `ValueError` con un
      mensaje descriptivo si no se cumple alguna precondición.
    - Debajo de cada función hay una celda con los ejemplos del enunciado. Compara
      la salida de tu implementación con la salida esperada (indicada en los comentarios).
    - **Se permite el uso de asistentes de IA** (GitHub Copilot u otros).
    - Al terminar, guarda y sube tus cambios a tu repositorio (`commit` + `push`).
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Inciso 1

    Implementa la función `suma_divisores_propios(n: int) -> int`, que devuelve la suma
    de los divisores propios de `n` (los divisores positivos de `n` menores que `n`).
    Precondición: `n >= 1`. Si no se cumple, lanza `ValueError`.
    """
    )
    return


@app.cell
def _():
    def suma_divisores_propios(n: int) -> int:
        pass
    return (suma_divisores_propios,)


@app.cell
def _(suma_divisores_propios):
    print(suma_divisores_propios(1))     # 0     (1 no tiene divisores propios)
    print(suma_divisores_propios(13))    # 1     (primo: solo el 1)
    print(suma_divisores_propios(12))    # 16    (1 + 2 + 3 + 4 + 6)
    print(suma_divisores_propios(28))    # 28    (1 + 2 + 4 + 7 + 14 → número perfecto)
    print(suma_divisores_propios(220))   # 284   (1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110)
    print(suma_divisores_propios(284))   # 220   (1 + 2 + 4 + 71 + 142)

    try:
        suma_divisores_propios(0)
    except ValueError as e:
        print(e)                         # n debe ser un entero positivo
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Inciso 2

    Implementa `son_amigos(a: int, b: int) -> bool`, reutilizando
    `suma_divisores_propios`. Dos números distintos $a \neq b$ son **amigos** si
    $s(a) = b$ y $s(b) = a$, donde $s$ es la suma de divisores propios.
    Precondición: `a >= 1` y `b >= 1`.
    """
    )
    return


@app.cell
def _():
    def son_amigos(a: int, b: int) -> bool:
        pass
    return (son_amigos,)


@app.cell
def _(son_amigos):
    print(son_amigos(220, 284))     # True
    print(son_amigos(284, 220))     # True   (la relación es simétrica)
    print(son_amigos(1184, 1210))   # True
    print(son_amigos(12, 16))       # False  (s(12) = 16, pero s(16) = 15 ≠ 12)
    print(son_amigos(6, 6))         # False  (6 es perfecto: a = b no cuenta como par amigo)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Inciso 3

    Implementa `pares_amigos(limite: int) -> list[tuple[int, int]]`, que devuelve,
    ordenados por el primer elemento, todos los pares de números amigos $(a, b)$ con
    $a < b \leq$ `limite`. Precondición: `limite >= 1`.

    **Sugerencia:** no hace falta comparar todos los pares $(a, b)$, que es $O(n^2)$.
    Para cada `a` basta con calcular `b = suma_divisores_propios(a)` y comprobar que
    `b > a`, que `b <= limite` y que `suma_divisores_propios(b) == a`.
    """
    )
    return


@app.cell
def _():
    def pares_amigos(limite: int) -> list[tuple[int, int]]:
        pass
    return (pares_amigos,)


@app.cell
def _(pares_amigos):
    print(pares_amigos(283))     # []  (284 queda fuera del límite)
    print(pares_amigos(284))     # [(220, 284)]
    print(pares_amigos(1500))    # [(220, 284), (1184, 1210)]
    print(pares_amigos(10000))   # [(220, 284), (1184, 1210), (2620, 2924), (5020, 5564), (6232, 6368)]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Inciso 4

    Según la suma de sus divisores propios $s(n)$, todo entero positivo `n` es de uno
    de estos tres tipos:

    - **deficiente** si $s(n) < n$;
    - **perfecto** si $s(n) = n$;
    - **abundante** si $s(n) > n$.

    Implementa `agrupar_por_tipo(a: int, b: int) -> dict[str, list[int]]`, que devuelve
    un diccionario cuyas claves son `"deficiente"`, `"perfecto"` y `"abundante"`. A cada
    clave le corresponde la lista, en orden creciente, de los números del intervalo
    cerrado $[a, b]$ que son de ese tipo. El diccionario debe tener siempre las tres
    claves, aunque alguna lista esté vacía. Precondición: `1 <= a <= b`.
    """
    )
    return


@app.cell
def _():
    def agrupar_por_tipo(a: int, b: int) -> dict[str, list[int]]:
        pass
    return (agrupar_por_tipo,)


@app.cell
def _(agrupar_por_tipo):
    print(agrupar_por_tipo(1, 10))
    # {'deficiente': [1, 2, 3, 4, 5, 7, 8, 9, 10], 'perfecto': [6], 'abundante': []}

    print(agrupar_por_tipo(20, 30))
    # {'deficiente': [21, 22, 23, 25, 26, 27, 29], 'perfecto': [28], 'abundante': [20, 24, 30]}

    print(agrupar_por_tipo(5, 5))
    # {'deficiente': [5], 'perfecto': [], 'abundante': []}

    grupos = agrupar_por_tipo(1, 100)
    print({tipo: len(numeros) for tipo, numeros in grupos.items()})
    # {'deficiente': 76, 'perfecto': 2, 'abundante': 22}
    return


if __name__ == "__main__":
    app.run()
