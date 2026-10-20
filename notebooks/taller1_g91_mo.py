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
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Problema 1

    Implementa la función `suma_divisores_propios(n: int) -> int`, que devuelve la suma
    de los divisores propios de `n` (los divisores positivos de `n` menores que `n`).
    Precondición: `n >= 1`. Si no se cumple, lanza `ValueError`.
    """
    )
    return


@app.cell
def _():
    def suma_divisores_propios(n: int) -> int:
        """Devuelve la suma de los divisores positivos de n menores que n."""
        if n < 1:
            raise ValueError("n debe ser un entero positivo")

        suma = 0
        # Sumamos los números menores que n que lo dividen exactamente.
        for divisor in range(1, n):
            if n % divisor == 0:
                suma += divisor
        return suma
    return (suma_divisores_propios,)


@app.cell
def _(suma_divisores_propios):
    print(suma_divisores_propios(1))     # 0
    print(suma_divisores_propios(13))    # 1
    print(suma_divisores_propios(12))    # 16
    print(suma_divisores_propios(28))    # 28
    print(suma_divisores_propios(220))   # 284
    print(suma_divisores_propios(284))   # 220
    try:
        suma_divisores_propios(0)
    except ValueError as e:
        print(e)                         # n debe ser un entero positivo
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Problema 2

    Implementa `son_amigos(a: int, b: int) -> bool`, reutilizando
    `suma_divisores_propios`. Dos números distintos $a \neq b$ son **amigos** si
    $s(a) = b$ y $s(b) = a$, donde $s$ es la suma de divisores propios.
    Precondición: `a >= 1` y `b >= 1`.
    """
    )
    return


@app.cell
def _(suma_divisores_propios):
    def son_amigos(a: int, b: int) -> bool:
        """Indica si a y b son distintos y cada uno suma el otro."""
        if a < 1:
            raise ValueError("a y b deben ser enteros positivos")
        if b < 1:
            raise ValueError("a y b deben ser enteros positivos")

        # Un número no puede formar una pareja consigo mismo.
        if a == b:
            return False
        # Comprobamos que cada número sea la suma de divisores del otro.
        if suma_divisores_propios(a) == b and suma_divisores_propios(b) == a:
            return True
        return False
    return (son_amigos,)


@app.cell
def _(son_amigos):
    print(son_amigos(220, 284))     # True
    print(son_amigos(284, 220))     # True
    print(son_amigos(1184, 1210))   # True
    print(son_amigos(12, 16))       # False
    print(son_amigos(6, 6))         # False
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Problema 3

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
def _(suma_divisores_propios):
    def pares_amigos(limite: int) -> list[tuple[int, int]]:
        """Devuelve los pares amigos a < b cuyos dos valores no superan limite."""
        if limite < 1:
            raise ValueError("limite debe ser un entero positivo")

        pares = []
        for a in range(1, limite + 1):
            # La suma de divisores de a es el posible número amigo b.
            b = suma_divisores_propios(a)
            # Guardamos el par una sola vez y si b no supera el límite.
            if b > a and b <= limite:
                if suma_divisores_propios(b) == a:
                    pares.append((a, b))
        return pares
    return (pares_amigos,)


@app.cell
def _(pares_amigos):
    print(pares_amigos(283))     # []
    print(pares_amigos(284))     # [(220, 284)]
    print(pares_amigos(1500))    # [(220, 284), (1184, 1210)]
    print(pares_amigos(10000))   # [(220, 284), (1184, 1210), (2620, 2924), (5020, 5564), (6232, 6368)]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Problema 4

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
def _(suma_divisores_propios):
    def agrupar_por_tipo(a: int, b: int) -> dict[str, list[int]]:
        """Agrupa en orden creciente los enteros de [a, b] según su tipo."""
        if a < 1:
            raise ValueError("se requiere que a y b sean enteros y 1 <= a <= b")
        if b < 1:
            raise ValueError("se requiere que a y b sean enteros y 1 <= a <= b")
        if a > b:
            raise ValueError("se requiere que a y b sean enteros y 1 <= a <= b")

        # Creamos las tres listas aunque alguna quede vacía.
        grupos = {"deficiente": [], "perfecto": [], "abundante": []}
        for numero in range(a, b + 1):
            suma = suma_divisores_propios(numero)
            if suma < numero:
                grupos["deficiente"].append(numero)
            elif suma == numero:
                grupos["perfecto"].append(numero)
            else:
                grupos["abundante"].append(numero)
        return grupos
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
