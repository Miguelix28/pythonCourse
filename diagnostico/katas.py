"""Sesión 1 — Prueba diagnóstica (45 min). Implemente cada función y ejecute:

    uv run pytest diagnostico -q

Mide: tipado, colecciones, comprensiones, funciones de orden superior, generadores,
manejo de errores, dataclasses y context managers. No requiere librerías externas.
"""

from __future__ import annotations

import re
from collections import Counter
from collections.abc import Callable, Iterable, Iterator
from dataclasses import dataclass
from functools import wraps


# 1. Comprensiones -----------------------------------------------------------
def palabras_por_longitud(texto: str) -> dict[int, list[str]]:
    """Agrupa palabras únicas (minúsculas, sin puntuación) por longitud, ordenadas."""
    palabras_compl = set(re.findall(r"\w+", texto.lower()))
    long_palabra = sorted({len(p) for p in palabras_compl})
    return {n: sorted(p for p in palabras_compl if len(p) == n) for n in long_palabra}


# 2. Colecciones -------------------------------------------------------------
def top_n(frecuencias: Iterable[str], n: int) -> list[tuple[str, int]]:
    """Los n elementos más frecuentes; empate → orden alfabético."""
    conteo = Counter(frecuencias)
    return sorted(conteo.items(), key=lambda par: (-par[1], par[0]))[:n]


# 3. Funciones de orden superior / closures ----------------------------------
def reintentar(veces: int) -> Callable[[Callable[..., object]], Callable[..., object]]:
    """Decorador: reintenta la función hasta `veces` si lanza excepción; luego la propaga."""

    def decorador(func: Callable[..., object]) -> Callable[..., object]:
        @wraps(func)
        def envoltura(*args: object, **kwargs: object) -> object:
            for intento in range(1, veces + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if intento == veces:
                        raise
            return None


# 4. Generadores -------------------------------------------------------------
def en_lotes[T](items: Iterable[T], tamano: int) -> Iterator[list[T]]:
    """Entrega listas de `tamano` elementos (la última puede ser menor). Perezoso."""
    lote: list[T] = []
    for item in items:
        lote.append(item)
        if len(lote) == tamano:
            yield lote
            lote = []


# 5. Dataclasses + propiedades -----------------------------------------------
@dataclass
class Factura:
    subtotal: float
    iva: float = 0.19

    @property
    def total(self) -> float:
        raise NotImplementedError

    def __post_init__(self) -> None:
        """Debe lanzar ValueError si subtotal < 0 o iva fuera de [0, 1]."""
        raise NotImplementedError


# 6. Context managers --------------------------------------------------------
class Cronometro:
    """with Cronometro() as c: ...  → c.segundos tiene la duración del bloque."""

    def __enter__(self) -> Cronometro:
        raise NotImplementedError

    def __exit__(self, *exc: object) -> None:
        raise NotImplementedError
