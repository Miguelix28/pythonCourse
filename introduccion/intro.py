"""Práctica de la introducción a Python.

Cada función tiene su firma, una docstring con lo que debe hacer y `raise NotImplementedError`.
Reemplace esa línea por la implementación y ejecute, desde la raíz del proyecto:

    uv run pytest introduccion -v          # todas
    uv run pytest introduccion -k saludo   # solo las de un ejercicio

Los ejercicios siguen el orden de la presentación "Python para quien ya programa".
"""

from __future__ import annotations

import functools  # noqa: F401  (lo necesita el ejercicio 12)
import math  # noqa: F401  (lo necesita el ejercicio 8)
from collections.abc import Callable, Iterator
from dataclasses import dataclass


# 1. Un programa es un archivo ----------------------------------------------------------
def saludo(nombre: str, formal: bool = False) -> str:
    nombre = nombre.strip()
    if formal:
        return f"Buenos días, {nombre}."
    return f"Hola, {nombre}"


def main() -> None:
    print(saludo("mundo"))


# 2. Bloques y condiciones --------------------------------------------------------------
def clasificar_temperatura(t: float) -> str:
    if t < 0 or t > 2:
        raise ValueError("La temperatura debe estar entre 0 y 2")
    if t < 0.3:
        return "precisa"
    if t <= 1:
        return "equilibrada"
    return "creativa"


# 3. Recorrer y contar ------------------------------------------------------------------
def contar_vocales(texto: str) -> dict[str, int]:
    minusculas = texto.lower()
    return {vocal: minusculas.count(vocal) for vocal in "aeiou"}


# 4. Funciones que devuelven varios valores ---------------------------------------------
def resumen(numeros: list[float]) -> tuple[float, float, float]:
    if not numeros:
        raise ValueError("La lista no puede estar vacía")
    return (min(numeros), max(numeros), sum(numeros) / len(numeros))


# 5. Al llamar, se pasa el objeto -------------------------------------------------------
def agregar_etiqueta(etiquetas: list[str] | None, nueva: str) -> list[str]:
    resultado = list(etiquetas) if etiquetas is not None else []
    if nueva not in resultado:
        resultado.append(nueva)
    return resultado


# 6. Comprensiones ----------------------------------------------------------------------
def largos(palabras: list[str]) -> dict[str, int]:
    return {p: len(p) for p in palabras if p.strip()}


# 7. Errores ----------------------------------------------------------------------------
def a_entero(texto: str, defecto: int = 0) -> int:
    try:
        return int(texto)
    except ValueError:
        return defecto


# 8. Módulos de la biblioteca estándar --------------------------------------------------
def hipotenusa(a: float, b: float) -> float:
    """La hipotenusa de un triángulo rectángulo, redondeada a 2 decimales.

    Use math.sqrt (el import ya está arriba). hipotenusa(1, 1) → 1.41
    """
    raise NotImplementedError


# 9. Clases -----------------------------------------------------------------------------
class Contador:
    """Contador que solo sube.

    Contador() empieza en 0; Contador(10), en 10. `valor` se lee como atributo (una property)
    y no se puede asignar. incrementar(paso=1) suma; con paso <= 0, ValueError. reiniciar()
    vuelve a 0. repr(c) → "Contador(6)".
    """

    def __init__(self, inicio: int = 0) -> None:
        raise NotImplementedError

    @property
    def valor(self) -> int:
        raise NotImplementedError

    def incrementar(self, paso: int = 1) -> None:
        raise NotImplementedError

    def reiniciar(self) -> None:
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError


# 10. dataclass -------------------------------------------------------------------------
@dataclass(frozen=True)
class Producto:
    """Producto inmutable. Precio negativo: ValueError al crearlo.

    `precio_con_iva` es una property: el precio por 1.19, redondeado a 2 decimales.
    """

    nombre: str
    precio: float
    etiquetas: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        raise NotImplementedError

    @property
    def precio_con_iva(self) -> float:
        raise NotImplementedError


# 11. Generadores -----------------------------------------------------------------------
def lineas_numeradas(texto: str) -> Iterator[str]:
    """Genera "1: texto", "2: texto"… por cada línea no vacía, sin espacios a los lados.

    Las líneas vacías no se cuentan. Debe ser un generador (yield), no devolver una lista.
    list(lineas_numeradas("a\\n\\n b ")) → ["1: a", "2: b"]
    """
    raise NotImplementedError


# 12. Decoradores -----------------------------------------------------------------------
def en_mayusculas(funcion: Callable[..., str]) -> Callable[..., str]:
    """Decorador: la función decorada devuelve su resultado en mayúsculas.

    Debe aceptar cualquier argumento (*args, **kwargs) y conservar el nombre y la docstring
    de la original con functools.wraps (el import ya está arriba).
    """
    raise NotImplementedError


if __name__ == "__main__":
    main()
